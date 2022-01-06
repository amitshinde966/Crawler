# The below crawler will crawl the Google search space and go through page 1 result of google for term "gate cse
# syllabus". It will then go through each  URL and within each page it will search for anchor tags with the provided
# keywords.

import requests
from bs4 import BeautifulSoup

# Google search URL
url = "https://www.google.com/search?q=gate+cse+syllabus&oq=gate+cse+syllabus&aqs=chrome..69i57j0i512l9.4646j0j7&" \
      "sourceid=chrome&ie=UTF-8"

# Headers to supply "requests" to enable crawling
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 '
                  'Safari/537.36 QIHU 360SE '
}

# Keywords to search on each page
keywords = ['download', 'cse', 'computer', 'computer science', 'computer engineering',
            'computer science engineering', 'computer science and information technology']

# GET request for the URL
f = requests.get(url, headers)

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
        url_f = requests.get(checkUrl, headers=headers)
        url_soup = BeautifulSoup(url_f.content, 'lxml')

        url_filtered_contents = []
        url_content = url_soup.find_all('a', href=True, download=True)
        # print(url_content)

        for key in keywords:
            # print("Checking key: " + key)

            for content in url_content:
                # Case-insensitive search
                if key.lower() in content.text.lower():
                    url_filtered_contents.append(content)

        # Print the links that satisfied the keywords
        print('\033[1m' + "Result: " + '\033[0m', url_filtered_contents)
        print("****************")
