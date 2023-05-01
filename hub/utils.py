import string

import requests
from bs4 import BeautifulSoup


def parse_hub(search, page=1):
    if not str(page).isnumeric():
        page=1

    url = 'https://rt.pornhub.com/video/search?search=' + search + f"&page={page}"
    agent = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=agent)
    soup = BeautifulSoup(response.text, 'lxml')
    title_href_span_els = soup.find("ul", class_="search-video-thumbs").find_all("span", class_="title")
    name_url = [i.find("a") for i in title_href_span_els]
    videos = {el.text.strip(): el["href"] for el in name_url}

    pages_els = soup.find("div", class_="pagination3").find_all("li")
    # print(f"pagesels {pages_els}")
    page_url = [i.find("a") for i in pages_els]
    # print(f"000_{page_url[1].text}")
    pages = [el.text for el in pages_els if el.text.isnumeric()]
    print(pages)
    return {"videos": videos,
            "pages": pages
            }