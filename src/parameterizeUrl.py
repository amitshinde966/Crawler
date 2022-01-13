"""
The below function will architect a Google URL in accordance to the searched string.

Parameters : 
    1. Searched string split using space

Example : 
    Input : gate me
    Output : https://www.google.com/search?num=100&q=syllabus+gate+me

    Input : gate cse syllabus
    Output : https://www.google.com/search?num=100&q=gate+cse+syllabus
"""


def parameterize_url(split_search_strs):
    google_url = "https://www.google.com/search?num=100&q=syllabus+"

    for search_str in split_search_strs:
        if search_str.lower() == "syllabus":
            google_url = "https://www.google.com/search?num=100&q="
            break

    # Add searched string to Google URL
    for index, search_str in enumerate(split_search_strs):
        if index == len(split_search_strs) - 1:
            google_url += search_str
        else:
            google_url += search_str + '+'

    return google_url
