import string

import requests
from bs4 import BeautifulSoup


def parse_hub(search, page=1):
    print(f"search {search}")
    if not str(page).isnumeric():
        page=1
    if search=="":
        url = "https://www.xvideos.com/?p=" + str(page)
    else:
        url = 'https://www.xvideos.com/?k=' + search + f"&p={page}"
    agent = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=agent)
    soup = BeautifulSoup(response.text, 'lxml')
    # print(soup)
    title_href_span_els = soup.find("div", class_="mozaique").find_all("p", class_="title")
    name_url = [i.find("a") for i in title_href_span_els]
    videos = {el.text.strip(): el["href"] for el in name_url}
    # print(f"videos {videos}")

    pages_els = soup.find("div", class_="pagination").find_all("li")
    # print(f"pagesels {pages_els}")
    page_url = [i.find("a") for i in pages_els]
    # print(f"000_{page_url[1].text}")
    pages = [el.text for el in pages_els if el.text.isnumeric()]
    print(pages)
    return {"videos": videos,
            "pages": pages
            }
