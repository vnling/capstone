import requests
from bs4 import BeautifulSoup
import io

def download_pdf(url, filename):
    response = requests.get(url)
    file = open(filename + ".pdf", 'wb')
    file.write(response.content)
    file.close()

url = "https://www.aeaweb.org/journals/aer/issues"
page = requests.get(url)
page_content = page.content
soup = BeautifulSoup(page_content, "html.parser")

# Get the links to the issues
article_links = set()
l = soup.find_all('article')
for article in l:
    p = article.find_all('a')
    for article_link in p:
        href = article_link.get('href')
        article_links.add(href)

# Get the links to the articles
pdf_links = set()
for url in article_links:
    nurl = "https://www.aeaweb.org" + url
    npage = requests.get(nurl)
    npage_content = npage.content
    nsoup = BeautifulSoup(npage_content, "html.parser")

    front_matters = nsoup.find('article')
    front_matters_link = front_matters.find_all('a')
    for link in front_matters_link:
        link_to_access = "https://www.aeaweb.org" + link.get('href')
        doi = link_to_access.split("=")[-1]
        pdf_links.add(doi)
# print(pdf_links)

# Access each pdf link and save the pdf
for doi in pdf_links:
    pdf_url = "https://pubs.aeaweb.org/doi/pdfplus/" + doi
    filename = doi.replace("/", "_")
    filename = "./../pdf/" + filename
    print(filename)
    download_pdf(pdf_url, filename) # windows doesn't like / in filenames