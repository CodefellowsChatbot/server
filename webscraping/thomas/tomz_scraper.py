import json
import requests

URL = "https://s3-us-west-2.amazonaws.com/static.codefellows.org/courses/schedule.json"

# def data_harvest(URL):
#     response = requests.get(URL)
    # print(response.json()["courses"][0]["course"]["title"])

# replicate the above function, but that will access all of the courses, not just courses[0]

def cf_calendar(URL):
    response = requests.get(URL)
    print("Status code ", response.status_code)
    print(response.json()["courses"])

    for i in response:
        # fields to capture:
        #     code, 
        print(response.json()["courses"][i]["course"]["code"])
        #     title, 
        print(response.json()[courses][i]["course"]["title"])
        #     startDate, 
        print(response.json()[courses][i]["course"]["startDate"])
        #     track, 
        print(response.json()[courses][i]["course"]["track"])
        #     price, 
        print(response.json()[courses][i]["course"]["price"])
        #     sequenceAndFamily.
        print(response.json()[courses][i]["course"]["sequenceAndFamily"])

         



if __name__ == "__main__":
    URL = "https://s3-us-west-2.amazonaws.com/static.codefellows.org/courses/schedule.json"
    data_harvest(URL)
    # cf_calendar(URL)
    # calendar_dict(URL)
