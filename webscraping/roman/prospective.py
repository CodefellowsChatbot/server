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
print(how_to_apply('https://www.codefellows.org/how-to-apply/'))
    
