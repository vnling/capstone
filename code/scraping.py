import requests
from bs4 import BeautifulSoup
import io

url = "https://www.aeaweb.org/journals/aer/issues"
page = requests.get(url)
page_content = page.content
soup = BeautifulSoup(page_content, "html.parser")

# created an empty list for putting the pdfs
list_of_pdf = set()
l = soup.find('article')
# accessed all the anchors tag from given p tag
p = l.find_all('a')
# iterate through p for getting all the href links
for link in p:
    # original html links
    link_to_access = link.get('href')
    print("link: ", link_to_access)
    # added all the pdf links to set
    list_of_pdf.add(link_to_access)

for url in list_of_pdf:
    new_url = "https://www.aeaweb.org" + url
    new_page = requests.get(new_url)
    new_page_content = new_page.content
    new_soup = BeautifulSoup(new_page_content, "html.parser")

    # find the front matters link
    new_list_of_pdf = set()
    front_matters = new_soup.find('article')
    # accessed all the anchors tag from given p tag
    front_matters_link = front_matters.find_all('a')
    # iterate through p for getting all the href links
    for link in front_matters_link:
        # original html links
        link_to_access = "https://www.aeaweb.org" + link.get('href')
        print("new link: ", link_to_access)
        # added all the pdf links to set
        new_list_of_pdf.add(link_to_access)