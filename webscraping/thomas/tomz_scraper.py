import json
import requests

URL = "https://s3-us-west-2.amazonaws.com/static.codefellows.org/courses/schedule.json"

def data_harvest(URL):
    response = requests.get(URL)
    # data = json.load(response.content)
    print(response.json()["courses"][0]["course"]["title"])

# replicate the above function, but that will access all of the courses, not just courses[0]





if __name__ == "__main__":
    URL = "https://s3-us-west-2.amazonaws.com/static.codefellows.org/courses/schedule.json"
    data_harvest(URL)
