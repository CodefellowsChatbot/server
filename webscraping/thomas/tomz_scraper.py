import requests
from bs4 import BeautifulSoup

URL = "https://www.codefellows.org/"

def drill_down(URL):
    response = requests.get(URL)
    # print(response)

    soup = BeautifulSoup(response.content, "html.parser")
    print(soup.prettify())





if __name__ == "__main__":
    URL = "https://www.codefellows.org/"
    drill_down(URL)
