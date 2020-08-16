# import requests, os, sys

# currentdir = os.path.dirname(os.path.realpath(__file__))
# parentdir = os.path.dirname(currentdir)
# sys.path.append(parentdir)

# from resources.links import Links

# links = Links()

# URL = links.course_calendar_json
# ***********************************************

import requests

URL = "https://s3-us-west-2.amazonaws.com/static.codefellows.org/courses/schedule.json"

def calendar_data(URL):
    response = requests.get(URL)
    if response.ok == False:
        return None

    cf_courses = response.json()["courses"]

    calendar = []

    for course in cf_courses:
        cf_normalized = {
        course["course"]["title"] : {
            'code' : course["course"]["code"],
            'start date' : course["course"]["startDate"],
            'track' : course["course"]["track"],
            'handle' : course["course"]["sequenceAndFamily"]
        }}

        calendar.append(cf_normalized)

# sort the calendar by start date:

    # sorted_calendar = sorted(calendar, key="start date")

    print(calendar)     # REMOVE THIS ****************************
    # return calendar


def course_calendar_by_track(handle):
    pass

    # course_by_track = ""
    # for offering in calendar:
    #     if handle in course['handle'] and track in course['track']:

    # calendar_data()


# def course_calendar_by_course(handle):
#     pass
#     course_cat = {}

#     source_list = calendar_data(URL)
#     # try:
#     for offering in source_list:
#         for item in offering:
#             try:
#                 course_cat[offering[item]["handle"]]
#             except KeyError:
#                 course_cat[offering[item]["handle"]] = []
#             course_cat[offering[item]["handle"]].append(offering)
#     # except:
#     #     print("I don't think that means what you think it means.")

#     print(course_cat["code-101"])








if __name__ == "__main__":
    URL = "https://s3-us-west-2.amazonaws.com/static.codefellows.org/courses/schedule.json"
    calendar_data(URL)
    # course_calendar_by_course("code-201")
