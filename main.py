import json
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

# Function to set up the browser and log in to LinkedIn
def login_to_linkedin(username, password, proxy):
    # Set up Chrome WebDriver with headless option
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('--proxy-server=%s' % proxy)
    driver = webdriver.Chrome(executable_path='/Userfolder/your_username_here/chromedriver_mac_or_windows_or_linux/chromedriver', options=options)
   
    # Load LinkedIn login page
    driver.get('https://www.linkedin.com/login')
    time.sleep(2)

    # Enter login credentials and submit
    username_input = driver.find_element_by_name('session_key')
    password_input = driver.find_element_by_name('session_password')
    username_input.send_keys(username)
    password_input.send_keys(password)
    password_input.submit()
    time.sleep(2)

    # Check if login was successful
    try:
        assert 'LinkedIn' in driver.title
        print('Login successful!')
        return driver
    except AssertionError:
        print('Login failed. Please check your credentials.')
        driver.quit()
        return None


# Function to scrape LinkedIn profiles
def scrape_profiles(driver, urls):
    data = []
    for url in urls:
        # Load profile page
        driver.get(url)
        time.sleep(2)

        # Parse HTML response with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Extract profile information
        name = soup.find('li', {'class': 'inline t-24 t-black t-normal break-words'})
        if name:
            name = name.get_text().strip()
        else:
            name = ''
        headline = soup.find('h2', {'class': 'mt1 t-18 t-black t-normal break-words'})
        if headline:
            headline = headline.get_text().strip()
        else:
            headline = ''
        location = soup.find('li', {'class': 't-16 t-black t-normal inline-block'})
        if location:
            location = location.get_text().strip()
        else:
            location = ''
        summary = soup.find('section', {'class': 'pv-about-section'})
        if summary:
            summary = summary.find('div', {'class': 'pv-about__summary-text'})
            if summary:
                summary = summary.get_text().strip()
            else:
                summary = ''
        else:
            summary = ''

        # Store profile information in a dictionary
        profile_data = {
            'name': name,
            'headline': headline,
            'location': location,
            'summary': summary,
            'url': url
        }
        data.append(profile_data)

    return data


# Function to save data to a JSON file
def save_data_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


# Main function
def main():
    # Set up browser and log in to LinkedIn
    username = 'your_sockpuppet_linkedin_account_login'
    password = 'your_sockpuppet_linkedin_password'
    proxies = ['your_proxy1_here', 'your_proxy2_here', 'your_proxy3_here']
    proxy = random.choice(proxies)
    driver = login_to_linkedin(username, password, proxy)

    if driver:
        # Set target URLs to scrape
        urls = ['https://www.linkedin.com/in/examplepersonslinkedinpage/']
    if driver:
        # Set target URLs to scrape
        urls = ['https://www.linkedin.com/in/examplepersonslinkedinpage/']
        data = scrape_profiles(driver, urls)
        save_data_to_json(data, 'profiles.json')
        print('Data saved to profiles.json')
