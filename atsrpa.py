from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import sys
import os
from dotenv import load_dotenv
load_dotenv()

load_dotenv(verbose=True)

from pathlib import Path  # Python 3.6+ only
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
email=os.getenv('EMAIL_ID')
#t.setup()

d = {'role':'Developer','Location':['Mumbai','Banglore']}

browser = webdriver.Chrome(
        executable_path = 'D:\Python_codes\chromedriver.exe')
browser.maximize_window()
browser.get('https://recruit.hirist.com/login')



email_xpath = '//*[@id="email"]'
email_click = browser.find_element_by_xpath(email_xpath)
email_click.send_keys(os.getenv('EMAIL_ID'));

password_xpath = '//*[@id="password"]'
password_click = browser.find_element_by_xpath(password_xpath)
password_click.send_keys(os.getenv('password'))

login_xpath = '//*[@id="login"]'
login_click = browser.find_element_by_xpath(login_xpath)
login_click.click()

time.sleep(5)

role_xpath = '//*[@id="onBoarding"]/div/div[1]/div[1]/div/input'
browser.find_element_by_xpath(role_xpath).send_keys(d['role'])

continue_xpath = '//*[@id="onBoarding"]/div/div[1]/div[1]/div/button'
browser.find_element_by_xpath(continue_xpath).click()


location_xpath = '//*[@id="location"]'
browser.find_element_by_xpath(location_xpath).send_keys(d['Location'][0])
browser.find_element_by_xpath(location_xpath).send_keys(Keys.ENTER)

browser.find_element_by_xpath(location_xpath).send_keys(d['Location'][1])
browser.find_element_by_xpath(location_xpath).send_keys(Keys.ENTER)

YoE_min_xpath = '//*[@id="min_experience"]'
browser.find_element_by_xpath(YoE_min_xpath).send_keys("2")

YoE_max_xpath = '//*[@id="max_experience"]'
browser.find_element_by_xpath(YoE_max_xpath).send_keys("5")

browser.find_element_by_name('Description').send_keys("Need to Know Python Language")

sel_category = Select(browser.find_element_by_xpath("//select[@id='category']"))
sel_category.select_by_visible_text("DevOps")

sel_area = Select(browser.find_element_by_xpath("//select[@id='functional_area']"))
sel_area.select_by_visible_text("Software Developer")

sel_grad_min = Select(browser.find_element_by_xpath("//select[@id='graduating_start_year']"))
sel_grad_min.select_by_visible_text("2013")

sel_grad_max = Select(browser.find_element_by_xpath("//select[@id='graduating_end_year']"))
sel_grad_max.select_by_visible_text("2017")

course_type_xpath = '//*[@id="courseType"]/div[2]/div[1]/label/div/span[1]/i'
browser.find_element_by_xpath(course_type_xpath).click()

work_xpath = '//*[@id="preferences"]/div[2]/div[5]/label/div/span[1]/i'
browser.find_element_by_xpath(work_xpath).click()

print("Job Completed Successfully")
