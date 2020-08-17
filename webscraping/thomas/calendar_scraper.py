import requests
import pprint   # Pretty Print


URL = "https://s3-us-west-2.amazonaws.com/static.codefellows.org/courses/schedule.json"

def calendar_data(URL):
    response = requests.get(URL)
    if response.ok == False:
        return None

    cf_courses = response.json()["courses"]

    calendar = []

    for course in cf_courses:
        cf_normalized = {
        'code' : course["course"]["code"],
        'title' : course["course"]["title"],
        'start date' : course["course"]["startDate"],
        'track' : course["course"]["track"],
        'handle' : course["course"]["sequenceAndFamily"]
        }

        calendar.append(cf_normalized)

    # sort the calendar by start date:
    sorted_calendar = sorted(calendar, key=lambda course: course["start date"])


    # pprint.pp(sorted_calendar)     # REMOVE THIS ****************************
    return sorted_calendar


def course_calendar_by_track(calendar, track):

    day_track_course = []
    night_track_course = []

    for course_track in calendar:
        if course_track["track"] == "day":
            day_track_course.append(course_track)
        elif course_track["track"] == "night":
            night_track_course.append(course_track)

    if track == "day":
        return day_track_course
    elif track == "night":
        return night_track_course


def course_calendar_by_course(calendar, handle):

    course_cat = []

    for course_code in calendar:
        try:
            if course_code["handle"] == handle:
                course_cat.append(course_code)
        except KeyError:
            course_cat[course_code["handle"]] = []
    
    return course_cat[0]
        

def course_filters(calendar, course_family=None, track=None):
    if course_family:
        result = course_calendar_by_course(calendar, course_family)
    if track:
        track_info = course_calendar_by_track(calendar, track)
        result = course_calendar_by_course(track_info, course_family)

    return result





if __name__ == "__main__":
    URL = "https://s3-us-west-2.amazonaws.com/static.codefellows.org/courses/schedule.json"
    sorted_calendar = calendar_data(URL)
    # pprint.pp(sorted_calendar)
    # course_filters(sorted_calendar, "code-201", "night")
    # sample = course_calendar_by_course(sorted_calendar, "code-201")
    sample = course_filters(sorted_calendar, "code-301", "day")
    # sample = course_filters(sorted_calendar, "code-201")

    print(sample)
