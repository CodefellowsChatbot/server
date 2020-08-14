from webscraping.lee.curriculum_scraper import get_course_info
from webscraping.roman.prospective import get_event_calendar, how_to_apply, employment_data, financing_scholarship

class Info:
    def __init__(self):
        self.courses = get_course_info()
        self.events = get_event_calendar(('https://testing-www.codefellows.org/events-calendar/'))
        self.apply = how_to_apply('https://testing-www.codefellows.org/how-to-apply/')
        self.employment = employment_data('https://testing-www.codefellows.org/employment-data/')
        self.financing = financing_scholarship('https://testing-www.codefellows.org/financing-and-scholarships/')