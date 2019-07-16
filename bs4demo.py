
# Libraries to use for webscraping html pages 
from bs4 import BeautifulSoup
import requests

# library for spreadsheet reading and writing
import csv

# store the url in a variable
url = "https://www.nathancollins.net.au"

# we need to open the file with the html code
# and store that in a variable 
htmlCode = open("demo.html", "r")

# now we can parse that files contents into BeautifulSoup,
# lets write that into a variable for later use
soup = BeautifulSoup(htmlCode, "html.parser")

# lets look for button and input tags
# write them into variables for later use
buttons = soup.find_all("button")
inputs = soup.find_all("input")

# lets print the output and see what we get
print(f"Buttons: {buttons}\nInputs: {inputs}")

# loop over the array of tags that was created by
# the find_all function, get the text only with the
# get_text() function
for text in buttons:
    print(f"Get the Text Only: {text.get_text()}")

# Use the select function with css selectors
# to extract data according to class id etc..
loremIpsumParagraphs = soup.select(".lorem-ipsum")
# loop through the array of paragraphs
for paragraph in loremIpsumParagraphs:
    # use the strip function to remove unnecessary spaces
    print(paragraph.get_text().strip())

# extract data using next_sibling
# first select / find the closest unique tag
firstParagraph = soup.select("#first-paragraph a")
for text in firstParagraph:
    print(text.next_sibling.strip())

# store the response from the website,
# so that we can extract data from it using
# BeautifulSoup
response = requests.get(url)

# if the response is ok lets start extracting data
if response.status_code == 200:

# parse the response into BeautifulSoup write the result
# to a variable called websiteSoup
    websiteSoup = BeautifulSoup(response.content, "html.parser")

    # narrow down the search using css selectors 
    # and the select function
    picLinks = websiteSoup.select(".project a")
    
# get project images on main page and
#  write their url links into a csv file
    with open("CSVDEMO.csv", mode="w", newline="") as csvfile:
        # set the csv parameters
        data = csv.writer(csvfile, delimiter=',')
        # write the header row
        data.writerow(["article-url","image-url"])
        # loop through the results of our data extract performed earlier
        for links in picLinks:
            data.writerow([links.attrs["href"],links.find("img").attrs['data-src']])

# print a error message to the console if we dont get the right response 
else:
    print(f"Sorry the website responded with a error code: {response.status_code}")