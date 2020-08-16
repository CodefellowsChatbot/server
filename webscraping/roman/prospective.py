import requests
from bs4 import BeautifulSoup

def get_event_calendar(URL):
    """
    This function takes in a url and returns a dictionary with events data.
    """
    event_calendar = {'events': {}}
    event_calendar['what upcoming events do you have hold'] = ''
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
        event_calendar['events'][f'{h1}']['Tell me about what is description of'] = el.find('p').get_text().split('.')[0]
        event_calendar['what upcoming events do you have hold'] += h1 + ', '

    return event_calendar


def how_to_apply(URL):
    """
    This function takes in a url and returns a dictionary with applying data.
    """
    data = {'steps': {}}
    data['how to apply what are the steps'] = ''
    response = requests.get(URL)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    prep = soup.find(id='preparation')
    step_1 = soup.find(id='step-1')
    step_2 = soup.find(id='step-2')
    step_3 = soup.find(id='step-3')
    step_4 = soup.find(id='step-4')
    reserve = soup.find(id='reserve')
    data['how to apply what are the steps'] = step_1.get_text() + ', ' + step_2.get_text() + ', ' + step_3.get_text() + ', ' + step_4.get_text()
    data['steps'][f'preparation how to be prepered what is skill level {prep.get_text()}'] = prep.find_next_sibling().get_text()
    data['steps'][f'how submit application {step_1.get_text()}'] = step_1.find_next_sibling().get_text()
    data['steps'][f'tell about the phone interview{ step_2.get_text()}'] = step_2.find_next_sibling().get_text()
    data['steps'][f'what is pre-work and the entrance test {step_3.get_text()}'] = step_3.find_next_sibling().get_text()
    data['steps'][f'what the final interview {step_4.get_text()}'] = step_4.find_next_sibling().get_text()
    data['steps'][f'how to reserve my spot {reserve.get_text()}'] = [reserve.find_all_next()[i].get_text() for i in range(8)]
    return data


def employment_data(URL):
    """
    This function takes in a url and returns a dictionary with employment data.
    """
    data = {'employment data': {}}
    response = requests.get(URL) 
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    result1 = soup.find('td', text='Job Seekers - Graduates')
    data['employment data'][f'{result1.get_text()}'] = {}
    data['employment data'][f'{result1.get_text()}']['job seekers - graduates how many graduated students'] = result1.find_next().get_text()
    data['employment data'][f'{result1.get_text()}']['what is percentage of graduated students / %'] = result1.find_next_sibling().find_next().get_text()
    result4 = soup.find_all('td', class_='secondary-row')
    for el in result4:
        data['employment data'][f'{el.get_text()}'] = {}
        data['employment data'][f'{el.get_text()}']['how many students'] = el.find_next().get_text()
        data['employment data'][f'{el.get_text()}']['what is the percentage / %'] = el.find_next_sibling().find_next().get_text()
    result5 = soup.find_all('tr', class_='bold')
    for el in result5:
        td = el.find('td')
        data['employment data'][f'{td.get_text()}'] = {}
        data['employment data'][f'{td.get_text()}']['how many students'] = td.find_next().get_text()
        data['employment data'][f'{td.get_text()}']['what is the percentage / %'] = td.find_next_sibling().find_next().get_text()
    result6 = soup.find('td', text='Non-Seeking Graduates')
    data['employment data'][f'{result6.get_text()}'] = {}
    data['employment data'][f'{result6.get_text()}']['how many'] = result6.find_next().get_text()
    data['employment data'][f'{result6.get_text()}']['what percentage / %'] = result6.find_next_sibling().find_next().get_text()
    result7 = soup.find('td', text='Non-Reporting Graduates')
    data['employment data'][f'{result7.get_text()}'] = {}
    data['employment data'][f'{result7.get_text()}']['how many'] = result7.find_next().get_text()
    data['employment data'][f'{result7.get_text()}']['what percentage / %'] = result7.find_next_sibling().find_next().get_text()
    result8 = soup.find('table', class_='center')
    caption = result8.find('caption').get_text()
    data['employment data'][f'what are {caption}'] = ''
    top_jobs = result8.find_all('tr')
    for el in top_jobs:
        data['employment data'][f'what are {caption}'] += el.get_text().replace('\n','') + ', '
    return data
    

def financing_scholarship(URL):
    """
    This function takes in a url and returns a dictionary with financing & scholarships data.
    """
    data = {'financing & scholarships': {}}
    response = requests.get(URL)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    result1 = soup.find('h2', id='student-loans').get_text()
    data['financing & scholarships'][f'{result1}'] = {}
    result2 = soup.find('p', text='Immediate Repayment')
    data['financing & scholarships'][f'{result1}'][f'what is how can I immediately repay repaying {result2.get_text()}'] = result2.find_next_sibling().get_text() + ' ' + result2.find_next_sibling().find_next_sibling().get_text()
    result3 = soup.find('p', text='Deferred Repayment')
    data['financing & scholarships'][f'{result1}'][f'what is how can deffer {result3.get_text()}'] = result3.find_next_sibling().get_text() + ' ' + result3.find_next_sibling().find_next_sibling().get_text() 
    result4 = soup.find('p', text='Interest-Only')
    data['financing & scholarships'][f'{result1}'][f'how to make low interest payments payment{result4.get_text()}'] = result4.find_next_sibling().get_text() + ' ' + result4.find_next_sibling().find_next_sibling().get_text() 
    result5 = soup.find('p', text='Fully-Deferred Option')
    data['financing & scholarships'][f'{result1}'][f'what is how learn now pay later{result5.get_text()}'] = result5.find_next_sibling().get_text() + ' ' + result5.find_next_sibling().find_next_sibling().get_text() 
    result6 = soup.find('p', text='Interest-Only Option')
    data['financing & scholarships'][f'{result1}'][f'what interest only affordable payments {result6.get_text()}'] = result6.find_next_sibling().get_text() + ' ' + result6.find_next_sibling().find_next_sibling().get_text() 
    result7 = soup.find('h2', id='early-bird')
    data['financing & scholarships'][f'what early bird discount discounts {result7.get_text()}'] = result7.find_next_sibling().get_text()
    result8 = soup.find('h2', id='course-bundle')
    data['financing & scholarships'][f'what course bundle discounts discount {result8.get_text()}'] = result8.find_next_sibling().get_text()
    result9 = soup.find('h2', id='scholarships')
    data['financing & scholarships'][f'{result9.get_text()}'] = {}
    data['financing & scholarships'][f'{result9.get_text()}']['what do you have scolarship scolarships fund'] = result9.find_next_sibling().get_text() + ' ' + result9.find_next_sibling().find_next_sibling().get_text() 
    data['financing & scholarships'][f'{result9.get_text()}']['who can apply for scolarship'] = soup.find('h3', text='Who Can Apply').find_next_sibling().get_text()
    how_to_apply = soup.find('h3', text='How to Apply')
    data['financing & scholarships'][f'{result9.get_text()}']['how to apply for scolarship'] = how_to_apply.find_next_sibling().get_text() + ' ' + how_to_apply.find_next_sibling().find_next_sibling().get_text()
    result10 = soup.find('h2', id='gi-bill')
    data['financing & scholarships'][f'Department of Veterans Affairs gi bill benefits {result10.get_text()}'] = result10.find_next_sibling().get_text() + ' ' + result10.find_next_sibling().find_next_sibling().get_text()
    result11 = soup.find('h2', id='wa-retraining')
    data['financing & scholarships'][f'{result11.get_text()}'] = {}
    data['financing & scholarships'][f'{result11.get_text()}']['what is do you have the worker retraining program'] = result11.find_next_sibling().get_text()
    data['financing & scholarships'][f'{result11.get_text()}']['who can apply for the worker retraining program'] = result11.find_next_sibling('ul').get_text().replace('\n','')
    data['financing & scholarships'][f'{result11.get_text()}']['how to apply for the worker retraining program'] = result11.find_next_sibling('ul').find_next_sibling('p').get_text().replace('\n', '')

    return data

if __name__ == "__main__":
    print(get_event_calendar('https://testing-www.codefellows.org/events-calendar/'))
    how_to_apply('https://testing-www.codefellows.org/how-to-apply/')
    employment_data('https://testing-www.codefellows.org/employment-data/')
    financing_scholarship('https://testing-www.codefellows.org/financing-and-scholarships/')


