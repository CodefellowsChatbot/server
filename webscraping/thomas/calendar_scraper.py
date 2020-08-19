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
    # return calendar


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
    if len(course_cat) == 0:
        course_cat = [{"start date": "Null"}]
    
    return course_cat
        

def course_filters(calendar, course_family=None, track=None):
    if track:
        track_info = course_calendar_by_track(calendar, track)
        result = course_calendar_by_course(track_info, course_family)
    elif course_family:
        result = course_calendar_by_course(calendar, course_family)
    else:
        result = [{"start date": "Null"}]
    # print(result)
    return result[0]



def final_output():
    calendar = calendar_data(URL)

    preamble1 = "When is the next start date for"
    preamble2 = "When is the next"
    preamble3 = "When does the next"
    preamble4 = "When does start"
    preamble5 = "What is the schedule for"
    preamble6 = "What is the start date for"

    days_101 = course_filters(calendar, "code-101","day")["start date"]
    days_201 = course_filters(calendar, "code-201","day")["start date"]
    nights_201 = course_filters(calendar, "code-201","night")["start date"]
    days_301 = course_filters(calendar, "code-301","day")["start date"]
    nights_301 = course_filters(calendar, "code-301","night")["start date"]
    dotnet_days = course_filters(calendar, "code-dotnet-401","day")["start date"]
    java_days = course_filters(calendar, "code-java-401","night")["start date"]
    javascript_days = course_filters(calendar, "code-javascript-401","day")["start date"]
    javascript_nights = course_filters(calendar, "code-javascript-401","night")["start date"]
    python_days = course_filters(calendar, "code-python-401","day")["start date"]
    python_nights = course_filters(calendar, "code-python-401","night")["start date"]
  
    return {
        "code": {
            "101":{
                "day":{
                preamble1:f"The next course starts on Saturday, {days_101}",
                preamble2:f"The next course starts on Saturday, {days_101}",
                preamble3:f"The next course starts on Saturday, {days_101}",
                preamble4:f"The next course starts on Saturday, {days_101}",
                preamble5:f"The next course starts on Saturday, {days_101}",
                preamble6:f"The next course starts on Saturday, {days_101}"
                }
            },
            "201":{
                "day":{
                preamble1:f"The next day course starts on {days_201}",
                preamble2:f"The next day course starts on {days_201}",
                preamble3:f"The next day course starts on {days_201}",
                preamble4:f"The next day course starts on {days_201}",
                preamble5:f"The next day course starts on {days_201}",
                preamble6:f"The next day course starts on {days_201}"
                },
                "night": {
                preamble1:f"The next night course starts on {nights_201}",
                preamble2:f"The next night course starts on {nights_201}",
                preamble3:f"The next night course starts on {nights_201}",
                preamble4:f"The next night course starts on {nights_201}",
                preamble5:f"The next night course starts on {nights_201}",
                preamble6:f"The next night course starts on {nights_201}"
                }
            },
            "301":{
                "day":{
                preamble1:f"The next day course starts on {days_301}",
                preamble2:f"The next day course starts on {days_301}",
                preamble3:f"The next day course starts on {days_301}",
                preamble4:f"The next day course starts on {days_301}",
                preamble5:f"The next day course starts on {days_301}",
                preamble6:f"The next day course starts on {days_301}"
                },
                "night": {
                preamble1:f"The next night course starts on {nights_301}",
                preamble2:f"The next night course starts on {nights_301}",
                preamble3:f"The next night course starts on {nights_301}",
                preamble4:f"The next night course starts on {nights_301}",
                preamble5:f"The next night course starts on {nights_301}",
                preamble6:f"The next night course starts on {nights_301}"
                }
            }
        },
        "python": {
            401:{
                "day":{
                preamble1:f"The next day course starts on {python_days}",
                preamble2:f"The next day course starts on {python_days}",
                preamble3:f"The next day course starts on {python_days}",
                preamble4:f"The next day course starts on {python_days}",
                preamble5:f"The next day course starts on {python_days}",
                preamble6:f"The next day course starts on {python_days}"
                },
                "night": {
                preamble1:f"The next night course starts on {python_nights}",
                preamble2:f"The next night course starts on {python_nights}",
                preamble3:f"The next night course starts on {python_nights}",
                preamble4:f"The next night course starts on {python_nights}",
                preamble5:f"The next night course starts on {python_nights}",
                preamble6:f"The next night course starts on {python_nights}"
                }
            }
        },
        "javascript": {
            401:{
                "day":{
                preamble1:f"The next day course starts on {javascript_days}",
                preamble2:f"The next day course starts on {javascript_days}",
                preamble3:f"The next day course starts on {javascript_days}",
                preamble4:f"The next day course starts on {javascript_days}",
                preamble5:f"The next day course starts on {javascript_days}",
                preamble6:f"The next day course starts on {javascript_days}"
                },
                "night": {
                preamble1:f"The next night course starts on {javascript_nights}",
                preamble2:f"The next night course starts on {javascript_nights}",
                preamble3:f"The next night course starts on {javascript_nights}",
                preamble4:f"The next night course starts on {javascript_nights}",
                preamble5:f"The next night course starts on {javascript_nights}",
                preamble6:f"The next night course starts on {javascript_nights}"
                }
            }
        },
        "java": {
            401:{
                "day":{
                preamble1:f"The next day course starts on {java_days}",
                preamble2:f"The next day course starts on {java_days}",
                preamble3:f"The next day course starts on {java_days}",
                preamble4:f"The next day course starts on {java_days}",
                preamble5:f"The next day course starts on {java_days}",
                preamble6:f"The next day course starts on {java_days}"
                }
            }
        },
        "dotnet": {
            401:{
                "day":{
                preamble1:f"The next day course starts on {dotnet_days}",
                preamble2:f"The next day course starts on {dotnet_days}",
                preamble3:f"The next day course starts on {dotnet_days}",
                preamble4:f"The next day course starts on {dotnet_days}",
                preamble5:f"The next day course starts on {dotnet_days}",
                preamble6:f"The next day course starts on {dotnet_days}"
                }
            }
        } 
    }





if __name__ == "__main__":
    # URL = "https://s3-us-west-2.amazonaws.com/static.codefellows.org/courses/schedule.json"
    # sorted_calendar = calendar_data(URL)
    # print(sorted_calendar)
    # pprint.pp(sorted_calendar)
    # course_filters(sorted_calendar, "code-201", "night")
    # sample = course_calendar_by_course(sorted_calendar, "code-401")
    # sample = course_filters(sorted_calendar, "code-301", "day")
    # sample = course_filters(sorted_calendar, "code-201")
    sample = final_output()
    print(sample)
