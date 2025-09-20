# If you wan to Scrape a Website:
# 1.use API
# 2.Html Scraping using some tool like bs4

# Step 0: requirements
# pip install requests
# pip install bs4
# pip install html5lib

import requests
from bs4 import BeautifulSoup
url = "https://google.com"

# step 1: get the html

r = requests.get(url)
htmlContent =  r.content
# print(htmlContent)

# stp2: Parse the html
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)

# stp3: html Tree traversal
# types of Objects
# 1.Tag
# 2.NavigableString
# 3.BeatifulSoup
# 4 Comment
# print(soup )
# print(title)
# print(type(title.string))

# markup = "<p><!-- this is a comment --></p>"
# soup2 = BeautifulSoup(markup)
# print(type(soup2.p.string))
# exit()



# get the title of the html page

title = soup.title

# Get all the paragraph from the page
paras = soup.find_all('p')
# print(paras)

# Get all the anchor tags from the page
# anchors = soup.find_all('p')
# all_links = set()

# print(anchors)

# print(soup.find('p')['class'])

# find all the elements with class lead
# print(soup.find_all("P",class_ = "lead"))

# get the text from the tags/soup
# print(soup.find('p').get_text())
# print(soup.get_text())

# Get all the anchor tags from the page
anchors = soup.find_all('a') 
# all_links = set()

# for link in anchors:
#     href = link.get('href')
#     if href and href != '#':
#         if href.startswith("http"):
#             print(href)  # check if not None
#         else:
#             print("https://google.com" + href)

# .contents - A tag's chidren are available as a list.
# .children - A tag's children are available as a generator.

navbarSupportedContent = soup.find(id='navbarSupportedContent')
# if navbarSupportedContent:
#     for elem in navbarSupportedContent.children:
#         print(elem)
# else:
#     print("Not Found")


# if navbarSupportedContent:
#     for item in navbarSupportedContent.stripped_strings:
#             print(item)
# else:
#     print("Not Found")

print(navbarSupportedContent.parent)