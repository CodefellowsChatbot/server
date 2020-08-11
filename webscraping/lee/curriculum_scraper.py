import requests
from bs4 import BeautifulSoup
from resources.links import Links
links = Links()

def get_tuition_and_duration(page) -> dict:
    big_soup = BeautifulSoup(page.content, "html.parser")
    side_bar = big_soup.find_all("div", class_="sidebar_bg")
    paragraphs = side_bar[0].find_all("p")
    output = {"Tuition": 0, "day duration": "", "night duration": ""}
    for para in paragraphs:
        if "Tuition" in para.text:
            tuition_str = para.text.strip()
            tuition_lst = tuition_str.split()
            output["Tuition"] = tuition_lst[1]
        elif "Nights" in para.text:
            night_str = para.text.strip()
            night_lst = night_str.split(":")
            output["night duration"] = night_lst[1].strip()
        elif "Daytime" in para.text:
            night_str = para.text.strip()
            night_lst = night_str.split(":")
            output["day duration"] = night_lst[1].strip()
        else:
            pass
    return output

def get_overview(page):
    big_soup = BeautifulSoup(page.content, "html.parser")
    articles = big_soup.find_all("article")
    print(len(articles))
    articles_dict = {}
    for art in articles:
        for entry in art.find_all("div"):
            title = entry.find("h2").text.strip()
            body = entry.text.strip()
            articles_dict[title] = body
    print(articles_dict.keys())

page = requests.get(links.courses["javascript"][301])
get_overview(page)

# for course in links.courses:
#     for level in links.courses[course]:
#         try:
#             page = requests.get(links.courses[course][level])
#             output = get_tuition_and_duration(page)
#             print(f"info for {course} {level}")
#             print(output)
#         except IndexError:
#             print(f"error with {course}:{level}")

# for language in links