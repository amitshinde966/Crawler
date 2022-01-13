#!/usr/bin/env python3
"""
The below crawler will crawl the Google search space and go through page 1 result of google for term "gate cse
syllabus". It will then go through each  URL and within each page it will search for anchor tags with the provided
keywords.
"""

__author__ = "Pranav Parge"
__version__ = "1.0.0"
__license__ = "MIT"

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

from parameterizeUrl import parameterize_url
from findAnchor import find_anchor


def main(search_str):
    # Headers to supply "requests" to enable crawling
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 '
                    'Safari/537.36 QIHU 360SE '
    }

    # Split the string by space
    search_strs = search_str.split(' ')

    # Google search URL for first 100 links & if skip/not "syllabus" keyword from search
    url = parameterize_url(search_strs)

    print('\033[91m' + '\033[1m' + 'GOOGLE URL:', url + '\033[0m' + '\033[0m')

    # Keywords to search on each page
    keywords = search_strs

    # GET request for the Google URL
    try:
        f = requests.get(url, headers)
    except Exception as e:
        print('\033[91m' + '\033[1m' + 'GOOGLE NOT REACHABLE', e, '\033[0m' + '\033[0m')
        raise Exception("GOOGLE NOT REACHABLE")

    # Convert HTML TO XML using fast lxml parser
    soup = BeautifulSoup(f.content, 'lxml')

    # Find all anchor tags on the page
    links = soup.find_all('a')

    # For each link on the Google page 1
    for link in links:
        if link["href"].startswith("/url?"):
            # Split string in accordance
            checkUrl = link["href"].split('q=')[1].split('&sa')[0]

            print('\033[1m' + "Checking URL: " + checkUrl + '\033[0m')

            # Again through the crawl process
            try:
                url_f = requests.get(checkUrl, headers=headers)
            except Exception as e:
                print('\033[91m' + '\033[1m' + 'NOT REACHABLE:', e, '\033[0m' + '\033[0m')
                continue

            url_soup = BeautifulSoup(url_f.content, 'lxml')

            # Search for downloadable link
            url_content = url_soup.find_all('a', href=True, download=True)

            # Find all the desired URLs/Links with specific text
            url_filtered_contents = find_anchor(keywords, url_content)

            # Print the links that satisfied the keywords
            print('\033[1m' + "Result: " + '\033[0m', url_filtered_contents)
            print("****************")

            # Download any pdf available
            for index, dwnld_links in enumerate(url_filtered_contents):
                parsedUrl = urlparse(checkUrl)
                fetchUrl = parsedUrl.scheme + '://' + parsedUrl.netloc + '/' + dwnld_links['href']
                # print('HREF', parsedUrl.scheme + '://' + parsedUrl.netloc + '/' + dwnld_links['href'])
                dwnld_f = requests.get(fetchUrl, headers=headers)
                with open(f'syllabus_{index}.pdf', 'wb') as f:
                    f.write(dwnld_f.content)


if __name__ == "__main__":
    # Pass the searched string
    main("gate me syllabus")
