import requests
from bs4 import BeautifulSoup
import io

def download_pdf(url, filename):
    response = requests.get(pdf_url)
    file = open(filename + ".pdf", 'wb')
    file.write(response.content)
    file.close()

url = "https://www.aeaweb.org/journals/aer/issues"
page = requests.get(url)
page_content = page.content
soup = BeautifulSoup(page_content, "html.parser")

# Get the links to the issues
article_links = set()
l = soup.find('article')
p = l.find_all('a')
for link in p:
    article_link = link.get('href')
    article_links.add(article_link)

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

# Access each pdf link and save the pdf
for doi in pdf_links:
    pdf_url = "https://pubs.aeaweb.org/doi/pdfplus/" + doi
    download_pdf(pdf_url, "_".join(doi.split("/"))) # windows doesn't like / in filenames