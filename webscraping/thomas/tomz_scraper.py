# import requests, os, sys
# currentdir = os.path.dirname(os.path.realpath(__file__))
# parentdir = os.path.dirname(currentdir)
# sys.path.append(parentdir)
# from resources.links import Links

# links = Links()

# URL = links.course_calendar_json

import requests

URL = "https://s3-us-west-2.amazonaws.com/static.codefellows.org/courses/schedule.json"

def data_harvest(URL):
    response = requests.get(URL)

    cf_courses = response.json()["courses"]

    calendar = []

    for course in cf_courses:
        cf_normalized = {
        course["course"]["title"] : {
            'code' : course["course"]["code"],
            'start date' : course["course"]["startDate"],
            'track' : course["course"]["track"],
            'Tuition' : "${:,.2f}".format(course["course"]["price"]),
        }

        }
        calendar.append(cf_normalized)
    print(calendar[0])     # REMOVE THIS ****************************



         

if __name__ == "__main__":
    URL = "https://s3-us-west-2.amazonaws.com/static.codefellows.org/courses/schedule.json"
    data_harvest(URL)
