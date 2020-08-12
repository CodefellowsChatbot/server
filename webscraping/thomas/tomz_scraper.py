import requests

URL = "https://s3-us-west-2.amazonaws.com/static.codefellows.org/courses/schedule.json"

def data_harvest(URL):
    response = requests.get(URL)
    # print(response.json()["courses"][0]["course"]["title"])

# replicate the above function, but that will access all of the courses, not just courses[0]

    cf_courses = response.json()["courses"]

    cf_offerings = []
    for course in cf_courses:
        cf_normalized = {
        'course_code' : course["course"]["code"],
        'course_title' : course["course"]["title"],
        'course_start' : course["course"]["startDate"],
        'course_track' : course["course"]["track"],
        'course_tuition' : course["course"]["price"],
        'course_seq_and_fam' : course["course"]["sequenceAndFamily"]
        }
        cf_offerings.append(cf_normalized)
    print(cf_offerings)


         



if __name__ == "__main__":
    URL = "https://s3-us-west-2.amazonaws.com/static.codefellows.org/courses/schedule.json"
    data_harvest(URL)
