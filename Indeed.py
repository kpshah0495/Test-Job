from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
#from pyvirtualdisplay import Display
import time
import requests
import json
import pickle

#display = Display(visible=False, size=(800, 600))
#display.start()

header= {"Authorization": "Bearer " + "keynRNfKupAXaHbAO"}
response = requests.get("https://api.airtable.com/v0/appOJoA8DZDOHUgmd/Positions/", headers=header)
api_records=response.json()
data=api_records.values()
data=list(data)
data=data[0]
copy_data=data.copy()
for i in range(len(copy_data)):
    j=copy_data[i]
    j=j['fields']
    if '[Confirmation] Auto-posted' in j:
        data.remove(data[i])
for i in range(len(data)):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389 Safari/537.36"
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--window-size=1200,1040")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    browser = webdriver.Chrome(ChromeDriverManager().install(),options=options)


    #browser.maximize_window()
    browser.get('https://www.indeed.com/hire')
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        browser.add_cookie(cookie)
    browser.get('https://www.indeed.com/hire')
    action = ActionChains(browser)


    #time.sleep(5)
    
    #W(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="hireHeroPostJobButton"]'))).click()
    #browser.find_element_by_xpath('//*[@id="hireHeroPostJobButton"]').click()
    
    time.sleep(5)
    
    browser.find_element_by_xpath('/html/body/nav/div/div[1]/div/div[3]/div[1]/a').click()
    
    time.sleep(5)
    
    browser.find_element_by_xpath('//*[@id="postJobButton"]').click()
    
#     handles = browser.window_handles
#     print(handles)
    

    time.sleep(20)
    
    browser.save_screenshot("sample.png")

    indeed_job_title_xpath = '//*[@id="JobTitle"]'
    indeed_job_title_click = browser.find_element_by_xpath(indeed_job_title_xpath)
    indeed_job_title_click.send_keys(data[i]['fields']['Position Name']);
    
    #browser.find_element_by_xpath('//*[@id="plugin_container_CoreFunnel_JobTitleContainer"]/div/div/div/div/div/div/div/div[2]').send_keys(data[i]['fields']['Position Name']);

    #time.sleep(2)

    indeed_loc_xpath = '//*[@id="cityOrPostalCode"]'
    indeed_loc_xpath_click = browser.find_element_by_xpath(indeed_loc_xpath)
    indeed_loc_xpath_click.send_keys("Mumbai");

    indeed_hires_xpath = '//*[@id="IntHiresNeeded_Stepper-1"]'
    indeed_hires_click = browser.find_element_by_xpath(indeed_hires_xpath)
    indeed_hires_click.send_keys(data[i]['fields']['Positions Open']);

    indeed_next_xpath = '//*[@id="sheet-next-button"]/span/a'
    browser.find_element_by_xpath(indeed_next_xpath).click()

    time.sleep(5)

    indeed_sel_emp_type = Select(browser.find_element_by_xpath('//*[@id="ifl-SelectFormField-7"]'))
    indeed_sel_emp_type.select_by_visible_text("Full-time")

    indeed_schedule_xpath = '//*[@id="plugin_container_TaxonomyScheduleCustomClassAttributesContainer"]/div/div/div/div/div/div/fieldset/div[2]/label[7]/div[1]'
    browser.find_element_by_xpath(indeed_schedule_xpath).click()


    time.sleep(2)
    indeed_salary_min_xpath = '//*[@id="JobSalary1"]'
    browser.find_element_by_xpath(indeed_salary_min_xpath).send_keys(Keys.CONTROL + "a")

    time.sleep(2)

    browser.find_element_by_xpath(indeed_salary_min_xpath).send_keys(Keys.DELETE)
    time.sleep(2)

    browser.find_element_by_xpath(indeed_salary_min_xpath).send_keys(data[i]['fields']['Minimum Annual Budget'])

    time.sleep(2)

    indeed_salary_max_xpath = '//*[@id="JobSalary2"]'
    browser.find_element_by_xpath(indeed_salary_max_xpath).send_keys(Keys.CONTROL + "a")
    browser.find_element_by_xpath(indeed_salary_max_xpath).send_keys(Keys.DELETE)
    browser.find_element_by_xpath(indeed_salary_max_xpath).send_keys(data[i]['fields']['Maximum Annual Budget'])

    time.sleep(2)

    indeed_resume_submit = '//*[@id="ApplicationEmailResumeRequirement"]/fieldset/label[3]/div[2]'
    browser.find_element_by_xpath(indeed_resume_submit).click()


    browser.execute_script("window.open('https://docs.google.com/document/d/1XoCLRKiO7lJNLF8a4z2PmCvbjYtJF4RNlkMpw5pFZe0/edit','new window')")

    handles = browser.window_handles

    browser.switch_to.window(handles[1])


    action = ActionChains(browser)
    action.key_down(Keys.CONTROL).send_keys("a").perform()
    action.key_down(Keys.CONTROL).send_keys("c").perform()

    time.sleep(2)

    browser.close()

    browser.switch_to.window(handles[0])

    time.sleep(2)

    action = ActionChains(browser)
    indeed_job_desc = browser.find_element_by_xpath('//*[@id="AppendedJobDescription-editor-content"]')
    action.click_and_hold(indeed_job_desc).perform()
    action.key_down(Keys.CONTROL).send_keys("v").perform()

    indeed_nxt = '//*[@id="sheet-next-button"]/span/a'
    browser.find_element_by_xpath(indeed_nxt).click()

    time.sleep(10)

    #indeed_off_xpath = '//*[@id="QualificationsVisibility"]/div[1]/div[2]/div/label/div[2]/div/div[2]'
    #browser.find_element_by_xpath(indeed_off_xpath).click()
    #//*[@id="QualificationsVisibility"]/div[1]/div[2]/label/div[1]
    
    W(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="QualificationsVisibility"]/div[1]/div[2]/label/div[1]'))).click()

    #indeed_off_2_xpath = '//*[@id="SkillsAssessmentVisibility"]/div[1]/div[2]/div/label/div[2]'
    #browser.find_element_by_xpath(indeed_off_2_xpath).click()
    
    W(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="SkillsAssessmentVisibility"]/div[1]/div[2]/label/div[1]'))).click()

    time.sleep(2)

    indeed_nxt_xpath = '//*[@id="sheet-next-button"]/span/a'
    browser.find_element_by_xpath(indeed_nxt_xpath).click()

    time.sleep(5)

    indeed_final_cont = '//*[@id="sheet-next-button"]/span/a'
    browser.find_element_by_xpath(indeed_final_cont).click()

    time.sleep(5)

    #wait_time_out = 15
    #wait_variable = W(browser, wait_time_out)
    #links = wait_variable.until(EC.visibility_of_any_elements_located((By.TAG_NAME, "a")))

    #for link in links:
    #    print (link.text)

    #elements = browser.find_elements_by_css_selector(".inserted_next_button")
    #print(elements)

    #indeed_dnt_optimize = '//*[@id="uniqueId1"]'
    #browser.find_element_by_class_name('inserted_next_button').submit()
    #browser.find_element_by_link_text('javascript:void(0)').click()
    #browser.find_element_by_id('uinqueId1').click()

    #print("Indeed Job Posting Completed")


    W(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="uniqueId1"]'))).click()

    time.sleep(5)

    browser.close()
#display.stop()
print("Indeed Auto-Post Done Successfully")
