import requests
from bs4 import BeautifulSoup
from resources.links import Links

links = Links()


def get_tuition_and_duration(page, course) -> dict:
    big_soup = BeautifulSoup(page.content, "html.parser")
    side_bar = big_soup.find_all("div", class_="sidebar_bg")
    paragraphs = side_bar[0].find_all("p")
    output = {}
    for para in paragraphs:
        if "Tuition" in para.text:
            tuition_raw = para.text.strip()
            tuition = tuition_raw.split()[1]
            tuition_str = f"Tuition for that class is {tuition}"
            output["How much does cost"] = tuition_str
            output["What is the price of"] = tuition_str
            output["How much is"] = tuition_str
            output["what does cost"] = tuition_str
            output["what is the cost for"] = tuition_str
            output["how much for"] = tuition_str
            output["what is the tuition for"] = tuition_str
        elif "Nights" in para.text:
            night_raw = para.text.strip()
            night = night_raw.split(":")[1].strip()
            night_str = (
                f"The duration of that course is {night} on nights/weekends track"
            )
            output["What is the night duration of"] = night_str
            output["How long is at night"] = night_str
            output["how long does take at night"] = night_str
        elif "Daytime" in para.text:
            day_raw = para.text.strip()
            day = day_raw.split(":")[1].strip()
            day_str = f"The duration of that course is {day}"
            output["What is the day duration of"] = day_str
            output["How long is at day"] = day_str
            output["how long does take"] = day_str
            output["how long is"] = day_str
            output["how long does take for day"] = day_str

        else:
            pass
    return output


def get_articles(page):
    big_soup = BeautifulSoup(page.content, "html.parser")
    articles = big_soup.find_all("article")
    articles_dict = {}
    for art in articles:
        for entry in art.find_all("div"):
            try:
                title = entry.find("h2").text.strip()
                body = entry.text.strip()[len(title) + 1 :]
                articles_dict[title] = body
                articles_dict[f"tell me about the {title}"] = body
                articles_dict[f"what is the {title}"] = body
                articles_dict[f"tell me what the is{title}"] = body
                articles_dict[f"tell me about {title}"] = body
                articles_dict[f"what is the of {title}"] = body
                articles_dict[f"what's the for {title}"] = body

            except AttributeError:
                pass
    return articles_dict


def get_course_info():
    course_obj = {}
    for course in links.courses:
        for level in links.courses[course]:
            try:
                page = requests.get(links.courses[course][level])
                tuition_and_duration = get_tuition_and_duration(
                    page, f"{course} {level}"
                )
                articles = get_articles(page)
                tuition_and_duration.update(articles)
                output = tuition_and_duration

                # print(f"info for {course} {level}")
                try:
                    course_obj[course]
                except KeyError:
                    course_obj[course] = {}
                course_obj[course][level] = output
                # print(output)
            except IndexError:
                print(f"error with {course}:{level}")
    return course_obj


if __name__ == "__main__":
    output = get_course_info()
    print(output)
