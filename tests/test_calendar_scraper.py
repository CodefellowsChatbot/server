import pytest
import json
from webscraping.thomas.calendar_scraper import (
    calendar_data,
    course_calendar_by_track,
    course_calendar_by_course,
    course_filters,
)
from unittest import mock


# Functions reachable:
def test_calendar_scraper_exists():
    assert calendar_data


def test_course_calendar_by_track_exists():
    assert course_calendar_by_track


def test_course_calendar_by_course_exists():
    assert course_calendar_by_course


def test_course_filters_exists():
    assert course_filters


@pytest.fixture
def mock_source():
    with open("tests/calendar_mock_source.json", "r") as file:
        data = file.read()
        json_data = json.loads(data)

    return json_data


# Calendar data function tests
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


def test_calendar_data_returns_data():

    with mock.patch('webscraping.thomas.calendar_scraper.requests.get') as mock_get:
        mock_get.return_value.json.return_value = { "courses" :[{'course': {'code': 'seattle-code-102n53', 'title': 'Code 102: Intro to Software Development', 'startDate': '2020-10-05', 'endDate': '2020-10-15', 'quarter': '4', 'meetingTimes': 'n', 'track': 'night', 'holidays': '', 'applicationDeadline': '2020-09-21', 'scholarshipDeadline': '2020-09-14', 'cancelled': False, 'family': '102', 'price': 1000.0, 'signupUrl': 'http://learn.codefellows.org/apply-now?utm_source=course-calendar&utm_medium=website&utm_campaign=coding-for-beginners&utm_content=code-102', 'courseStatus': '', 'dailySchedule': '', 'sequence': 'code', 'sequenceAndFamily': 'code-102', 'publicationState': 'Published', 'location': {'name': 'Code Fellows', 'streetAddress': '2901 3rd Ave, Suite 300', 'city': 'Seattle', 'state': 'WA', 'zipCode': '98121'}}}]}
        actual = calendar_data(mock_get)
    assert actual == [{'code': 'seattle-code-102n53', 'title': 'Code 102: Intro to Software Development', 'start date': '2020-10-05', 'track': 'night', 'handle': 'code-102'}]


# course_calendar_by_track function tests
def test_course_calendar_by_track_pass(mock_source):

    with mock.patch('webscraping.thomas.calendar_scraper.requests.get') as mock_get:
        mock_get.return_value.json.return_value = mock_source
        sorted_source = calendar_data(mock_get)

    calendar = sorted_source
    track = "night"
    actual = course_calendar_by_track(calendar, track)
    for course in actual:
        assert course["track"] == track


# course_calendar_by_course function tests
def test_course_calendar_by_course_pass(mock_source):

    with mock.patch('webscraping.thomas.calendar_scraper.requests.get') as mock_get:
        mock_get.return_value.json.return_value = mock_source
        sorted_source = calendar_data(mock_get)

    calendar = sorted_source
    handle = "code-102"
    actual = course_calendar_by_course(calendar, handle)
    for course in actual:
        assert course["handle"] == handle


# course_filters function tests
def test_course_filters_pass(mock_source):

    with mock.patch('webscraping.thomas.calendar_scraper.requests.get') as mock_get:
        mock_get.return_value.json.return_value = mock_source
        sorted_source = calendar_data(mock_get)

    calendar = sorted_source
    test_handle = "code-102"
    test_track = "night"
    actual = course_filters(calendar, test_handle, test_track)
    assert actual == {'code': 'seattle-code-102n53', 'title': 'Code 102: Intro to Software Development', 'start date': '2020-10-05', 'track': 'night', 'handle': 'code-102'}
