import requests
from bs4 import BeautifulSoup

def get_event_calendar(URL):
    """
    This function takes in a url and returns a dictionary with events data.
    """
    event_calendar = {'events': {}}
    event_calendar['what events do you have'] = ''
    response = requests.get(URL)

    content = response.content

    soup = BeautifulSoup(content, 'html.parser')

    result = soup.find_all(class_= 'details')
    for el in result:
        h1 = el.find('h1').get_text()
        h2 = el.find('h2').get_text()
        event_calendar['events'][f'{h1}'] = {}
        event_calendar['events'][f'{h1}']['when is'] = el.find('h2').get_text() + ' ' + el.find('h2').find_next_sibling('h2').get_text()
        event_calendar['events'][f'{h1}']['where is'] = el.find('h2').find_next_sibling().find_next_sibling().get_text()
        event_calendar['events'][f'{h1}']['what description'] = el.find('p').get_text().split('.')[0]
        event_calendar['events'][f'{h1}']['Tell me about'] = el.find('p').get_text().split('.')[0]
        event_calendar['what events do you have'] += h1 + ', '

    return event_calendar


def how_to_apply(URL):
    """
    This function takes in a url and returns a dictionary with applying data.
    """
    data = {'steps': {}}
    data['how to apply to school steps'] = ''
    response = requests.get(URL)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    prep = soup.find(id='preparation')
    step_1 = soup.find(id='step-1')
    step_2 = soup.find(id='step-2')
    step_3 = soup.find(id='step-3')
    step_4 = soup.find(id='step-4')
    reserve = soup.find(id='reserve')
    data['how to apply to school steps'] = step_1.get_text() + ', ' + step_2.get_text() + ', ' + step_3.get_text() + ', ' + step_4.get_text()
    data['steps'][f'how to be prepared to school preparation {prep.get_text()}'] = prep.find_next_sibling().get_text()
    data['steps'][f'how to submit the application'] = step_1.find_next_sibling().get_text()
    data['steps'][f'about phone interview'] = step_2.find_next_sibling().get_text()
    data['steps'][f'what is pre-work the entrance test'] = ''
    for i in range(4):
        data['steps'][f'what is pre-work the entrance test'] += step_3.find_all_next()[i].get_text() + ' '
    data['steps'][f'what the final interview'] = step_4.find_next_sibling().get_text()+ " " + step_4.find_next_sibling().find_next().get_text()
    data['steps'][f'how to reserve a spot'] = ''
    for i in range(8):
        data['steps'][f'how to reserve a spot'] += reserve.find_all_next()[i].get_text() + ' '
    return data

def employment_data(URL):
    """
    This function takes in a url and returns a dictionary with employment data.
    """
    data = {'employment': {}}
    response = requests.get(URL) 
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    result1 = soup.find('td', text='Job Seekers - Graduates')
    data['employment']['how many job seekers - graduates do'] = result1.find_next().get_text()
    data['employment']['what is the percentage of job seekers - graduates %'] = result1.find_next_sibling().find_next().get_text()
    result2 = soup.find('td', text='Job Seekers - Non-Graduates')
    data['employment']['how many Job Seekers - Non-Graduates do'] = result2.find_next().get_text()
    data['employment']['what is % percentage of Job Seekers - Non-Graduates'] = result2.find_next_sibling().find_next().get_text()
    result4 = soup.find_all('td', class_='secondary-row')
    for el in result4:
        data['employment'][f'how many {el.get_text()}'] = el.find_next().get_text()
        data['employment'][f'what is the percentage {el.get_text()}'] = el.find_next_sibling().find_next().get_text()
    result5 = soup.find_all('tr', class_='bold')
    for el in result5:
        td = el.find('td')
        data['employment'][f'what is {td.get_text()}'] = td.find_next().get_text()
        data['employment'][f'how many students {td.get_text()}'] = td.find_next().get_text()
        data['employment'][f'what is percentage % {td.get_text()}'] = td.find_next_sibling().find_next().get_text()
    result6 = soup.find('td', text='Non-Seeking Graduates')
    data['employment']['how many Non-Seeking Graduates do'] = result6.find_next().get_text()
    data['employment']['what percentage % Non-Seeking Graduates'] = result6.find_next_sibling().find_next().get_text()
    result7 = soup.find('td', text='Non-Reporting Graduates')
    data['employment']['how many Non-Reporting Graduates do'] = result7.find_next().get_text()
    data['employment']['what is the percentage % Non-Reporting Graduates'] = result7.find_next_sibling().find_next().get_text()
    result8 = soup.find('table', class_='center')
    caption = result8.find('caption').get_text()
    data['employment'][f'what {caption}'] = ''
    top_jobs = result8.find_all('tr')
    for el in top_jobs:
        data['employment'][f'what {caption}'] += el.get_text().replace('\n','') + ', '
    return data
    

def financing_scholarship(URL):
    """
    This function takes in a url and returns a dictionary with financing & scholarships data.
    """
    data = {'financing': {}}
    response = requests.get(URL)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    result1 = soup.find('h2', id='student-loans').get_text()
    result2 = soup.find('p', text='Immediate Repayment')
    data['financing']['what is Immediate Repayment'] = result2.find_next_sibling().get_text() + ' ' + result2.find_next_sibling().find_next_sibling().get_text()
    result3 = soup.find('p', text='Deferred Repayment')
    data['financing']['do you have deffered repayment'] = result3.find_next_sibling().get_text() + ' ' + result3.find_next_sibling().find_next_sibling().get_text() 
    result4 = soup.find('p', text='Interest-Only')
    data['financing']['do you have interest-only payment'] = result4.find_next_sibling().get_text() + ' ' + result4.find_next_sibling().find_next_sibling().get_text() 
    result5 = soup.find('p', text='Fully-Deferred Option')
    data['financing']['do you have fully-deferred option'] = result5.find_next_sibling().get_text() + ' ' + result5.find_next_sibling().find_next_sibling().get_text() 
    result6 = soup.find('p', text='Interest-Only Option')
    data['financing']['do you have intersest-only option'] = result6.find_next_sibling().get_text() + '. ' + result6.find_next_sibling().find_next_sibling().get_text()
    result7 = soup.find('h2', id='early-bird')
    data['financing']['what early bird discount is'] = result7.find_next_sibling().get_text()
    result8 = soup.find('h2', id='course-bundle')
    data['financing']['what course bundle discount is'] = result8.find_next_sibling().get_text()
    data['financing']['do you have discounts'] = 'Yup!'
    data['financing']['what discounts do you have'] = f'{result7.get_text()}' + ', ' f'{result8.get_text()}'
    result9 = soup.find('h2', id='scholarships')
    data['financing']['do you have scholarship fund'] = 'Yes, we do!'
    data['financing']['what scholarship fund do you have'] = result9.find_next_sibling().get_text() + ' ' + result9.find_next_sibling().find_next_sibling().get_text() 
    data['financing']['who can apply for scholarship'] = soup.find('h3', text='Who Can Apply').find_next_sibling().get_text()
    how_to_apply = soup.find('h3', text='How to Apply')
    data['financing']['how to apply for scholarship'] = how_to_apply.find_next_sibling().get_text() + ' ' + how_to_apply.find_next_sibling().find_next_sibling().get_text()
    result10 = soup.find('h2', id='gi-bill')
    data['financing']['what is gi bill'] = result10.find_next_sibling().get_text() + ' ' + result10.find_next_sibling().find_next_sibling().get_text()
    result11 = soup.find('h2', id='wa-retraining')
    data['financing']['do you have the worker retraining program'] = 'Yes!'
    data['financing']['what is the worker retraining program'] = result11.find_next_sibling().get_text()
    data['financing']['who can apply for the worker retraining program'] = result11.find_next_sibling('ul').get_text()
    data['financing']['how to apply for the worker retraining program'] = result11.find_next_sibling('ul').find_next_sibling('p').get_text()

    return data

if __name__ == "__main__":
    print(get_event_calendar('https://testing-www.codefellows.org/events-calendar/'))
    how_to_apply('https://testing-www.codefellows.org/how-to-apply/')
    employment_data('https://testing-www.codefellows.org/employment-data/')
    financing_scholarship('https://testing-www.codefellows.org/financing-and-scholarships/')


