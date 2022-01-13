"""
The below function will find all the links that match the searched keywords

Parameters : 
    1. Keywords : Searched string split on space
    2. url_content : Content of the URL to be searched
"""


def find_anchor(keywords, url_content):
    url_filtered_contents = []
    for key in keywords:
        for content in url_content:
            # Case-insensitive search
            if key.lower() in content.text.lower():
                url_filtered_contents.append(content)

    return url_filtered_contents
