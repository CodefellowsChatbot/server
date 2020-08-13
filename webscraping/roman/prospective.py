import requests
from bs4 import BeautifulSoup

def get_event_calendar(URL):
    """
    This function takes in a url and returns a dictionary.
    """
    event_calendar = []
    response = requests.get(URL)

    content = response.content

    soup = BeautifulSoup(content, 'html.parser')

    result = soup.find_all(class_= 'details')
    for el in result:
        course = {'events': {'event': {}}}
        course['events']['event']['name'] = el.find('h1').get_text()
        course['events']['event']['date'] = el.find('h2').get_text() + ' ' + el.find('h2').find_next_sibling('h2').get_text()
        course['events']['event']['location'] = el.find('h2').find_next_sibling().find_next_sibling().get_text()
        course['events']['event']['description'] = el.find('p').get_text().split('.')[0]

        event_calendar.append(course)
    return event_calendar

def how_to_apply(URL):
    data = {'how to apply': {}}
    response = requests.get(URL)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    prep = soup.find(id='preparation')
    step_1 = soup.find(id='step-1')
    step_2 = soup.find(id='step-2')
    step_3 = soup.find(id='step-3')
    step_4 = soup.find(id='step-4')
    reserve = soup.find(id='reserve')
    data['how to apply'][f'{prep.get_text()}'] = prep.find_next_sibling().get_text()
    data['how to apply'][f'{step_1.get_text()}'] = step_1.find_next_sibling().get_text()
    data['how to apply'][f'{step_2.get_text()}'] = step_2.find_next_sibling().get_text()
    data['how to apply'][f'{step_3.get_text()}'] = step_3.find_next_sibling().get_text()
    data['how to apply'][f'{step_4.get_text()}'] = step_4.find_next_sibling().get_text()
    data['how to apply'][f'{reserve.get_text()}'] = [reserve.find_all_next()[i].get_text() for i in range(8)]
    return data
    
def employment_data(URL):
    data = {'employment data': {}}
    response = requests.get(URL)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    result1 = soup.find('td', text='Job Seekers - Graduates')
    data['employment data'][f'{result1.get_text()}'] = {}
    data['employment data'][f'{result1.get_text()}']['count'] = result1.find_next().get_text()
    data['employment data'][f'{result1.get_text()}']['percentage / %'] = result1.find_next_sibling().find_next().get_text()
    result4 = soup.find_all('td', class_='secondary-row')
    for el in result4:
        data['employment data'][f'{el.get_text()}'] = {}
        data['employment data'][f'{el.get_text()}']['count'] = el.find_next().get_text()
        data['employment data'][f'{el.get_text()}']['percentage / %'] = el.find_next_sibling().find_next().get_text()
    result5 = soup.find_all('tr', class_='bold')
    for el in result5:
        td = el.find('td')
        data['employment data'][f'{td.get_text()}'] = {}
        data['employment data'][f'{td.get_text()}']['count'] = td.find_next().get_text()
        data['employment data'][f'{td.get_text()}']['percentage / %'] = td.find_next_sibling().find_next().get_text()
    result6 = soup.find('td', text='Non-Seeking Graduates')
    data['employment data'][f'{result6.get_text()}'] = {}
    data['employment data'][f'{result6.get_text()}']['count'] = result6.find_next().get_text()
    data['employment data'][f'{result6.get_text()}']['percentage / %'] = result6.find_next_sibling().find_next().get_text()
    result7 = soup.find('td', text='Non-Reporting Graduates')
    data['employment data'][f'{result7.get_text()}'] = {}
    data['employment data'][f'{result7.get_text()}']['count'] = result7.find_next().get_text()
    data['employment data'][f'{result7.get_text()}']['percentage / %'] = result7.find_next_sibling().find_next().get_text()
    result8 = soup.find('table', class_='center')
    caption = result8.find('caption').get_text()
    data['employment data'][f'{caption}'] = []
    top_jobs = result8.find_all('tr')
    for el in top_jobs:
        data['employment data'][f'{caption}'].append(el.get_text().replace('\n',''))
    return data
    
        

print(employment_data('https://testing-www.codefellows.org/employment-data/'))
