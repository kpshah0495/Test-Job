from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys
import os
from dotenv import load_dotenv
import requests
import json

''' Setting up ENV Variables'''


load_dotenv()

load_dotenv(verbose=True)

from pathlib import Path  # Python 3.6+ only

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)



''' Call API From Airtable '''

header= {"Authorization": "Bearer " + "keynRNfKupAXaHbAO"}

response = requests.get("https://api.airtable.com/v0/appOJoA8DZDOHUgmd/Positions/", headers=header)
api_records=response.json()


'''Manageing the Data'''

data=api_records.values()
data=list(data)
data=data[0]
copy_data=data.copy()
for i in range(len(copy_data)):
    j=copy_data[i]
    j=j['fields']
    if '[Confirmation] Auto-posted' in j:
        data.remove(data[i])

d = {'role':'Developer','Location':['Mumbai','Banglore']}

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.maximize_window()
browser.get('https://recruit.hirist.com/login')

'''Selenium automation For Hirist Website'''

email_xpath = '//*[@id="email"]'
email_click = browser.find_element_by_xpath(email_xpath)
email_click.send_keys('nikezeon@gmail.com');

password_xpath = '//*[@id="password"]'
password_click = browser.find_element_by_xpath(password_xpath)
password_click.send_keys('Test@1234')

login_xpath = '//*[@id="login"]'
login_click = browser.find_element_by_xpath(login_xpath)
login_click.click()

time.sleep(5)
Jobs='//*[@class="myJobsLink header-links"]'
jobs_click = browser.find_element_by_xpath(Jobs)
jobs_click.click()

post_job="//*[@class='post-job green']"
post_jobs=browser.find_element_by_xpath(post_job)
post_jobs.click()

for i in range(len(data)):


    role_xpath = '//*[@id="title"]'
    browser.find_element_by_xpath(role_xpath).send_keys(data[i]['fields']['Position Name'])

    location_xpath = '//*[@id="location"]'
    browser.find_element_by_xpath(location_xpath).send_keys(d['Location'][0])
    browser.find_element_by_xpath(location_xpath).send_keys(Keys.ENTER)

    browser.find_element_by_xpath(location_xpath).send_keys(d['Location'][1])
    browser.find_element_by_xpath(location_xpath).send_keys(Keys.ENTER)

    YoE_min_xpath = '//*[@id="min_experience"]'
    browser.find_element_by_xpath(YoE_min_xpath).send_keys(data[i]['fields']['Desired Experience Minimum'])

    YoE_max_xpath = '//*[@id="max_experience"]'
    browser.find_element_by_xpath(YoE_max_xpath).send_keys(data[i]['fields']['Desired Experience Maximum'])
    
    a=data[i]['fields']['Job Description text ']
    a = a.replace("###", "")
    
    browser.find_element_by_name('Description').send_keys(a)

    sel_category = Select(browser.find_element_by_xpath("//select[@id='category']"))
    sel_category.select_by_visible_text(data[i]['fields']['Categories A (Hirist)'][0])

    sel_area = Select(browser.find_element_by_xpath("//select[@id='functional_area']"))
    sel_area.select_by_visible_text(data[i]['fields']['Sub categories A (Hirist)'][0])

    sel_grad_min = Select(browser.find_element_by_xpath("//select[@id='graduating_start_year']"))
    sel_grad_min.select_by_visible_text("2013")

    sel_grad_max = Select(browser.find_element_by_xpath("//select[@id='graduating_end_year']"))
    sel_grad_max.select_by_visible_text("2017")

    course_type_xpath = '//*[@id="courseType"]/div[2]/div[1]/label/div/span[1]/i'
    browser.find_element_by_xpath(course_type_xpath).click()

    work_xpath = '//*[@id="preferences"]/div[2]/div[5]/label/div/span[1]/i'
    browser.find_element_by_xpath(work_xpath).click()

    submit_form = browser.find_element_by_xpath('//*[@id="submitForm"]')
    submit_form.click()

    time.sleep(2)
    add_another_job = browser.find_element_by_xpath('//*[@id="congrats"]/a')
    add_another_job.click()
    

