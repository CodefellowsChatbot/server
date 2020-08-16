import pytest
from webscraping.thomas.calendar_scraper import calendar_data
from unittest import mock
# from unittest.mock import patch



def test_calendar_scraper_exists():
    assert calendar_data


def test_calendar_data_pass():
    with mock.patch('webscraping.thomas.calendar_scraper.requests.get') as mock_get:
        mock_get.return_value.ok = True
        response = calendar_data(mock_get)
    assert response == []
    

def test_calendar_data_pass_fail():
    with mock.patch('webscraping.thomas.calendar_scraper.requests.get') as mock_get:
        mock_get.return_value.ok = False
        response = calendar_data(mock_get)
    assert response == None


# @pytest.mark.skip
def test_calendar_data_returns_data():

    with mock.patch('webscraping.thomas.calendar_scraper.requests.get') as mock_get:
        mock_get.return_value.json.return_value = { "courses" :[{'course': {'code': 'seattle-code-102n53', 'title': 'Code 102: Intro to Software Development', 'startDate': '2020-10-05', 'endDate': '2020-10-15', 'quarter': '4', 'meetingTimes': 'n', 'track': 'night', 'holidays': '', 'applicationDeadline': '2020-09-21', 'scholarshipDeadline': '2020-09-14', 'cancelled': False, 'family': '102', 'price': 1000.0, 'signupUrl': 'http://learn.codefellows.org/apply-now?utm_source=course-calendar&utm_medium=website&utm_campaign=coding-for-beginners&utm_content=code-102', 'courseStatus': '', 'dailySchedule': '', 'sequence': 'code', 'sequenceAndFamily': 'code-102', 'publicationState': 'Published', 'location': {'name': 'Code Fellows', 'streetAddress': '2901 3rd Ave, Suite 300', 'city': 'Seattle', 'state': 'WA', 'zipCode': '98121'}}}]}
        actual = calendar_data(mock_get)
    assert actual == [{'Code 102: Intro to Software Development': {'code': 'seattle-code-102n53', 'start date': '2020-10-05', 'track': 'night', 'Tuition': '$1,000.00'}}]
