import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from dotenv import load_dotenv

load_dotenv()

linkedin_username = os.getenv("LINKEDIN_USERNAME")
linkedin_password = os.getenv("LINKEDIN_PASSWORD")
url = "https://www.linkedin.com/jobs/search/?currentJobId=3932298060&f_AL=true&f_WT=2&geoId=105072130&keywords=python%20developer&location=Poland&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(url)

# Click the sign-in button after getting the URL above
time.sleep(2)
sign_in_button = driver.find_element(By.XPATH, value="/html/body/div[4]/a[1]")
sign_in_button.click()

# Fill in the username and password, and click on the sign-in button
time.sleep(2)
email_textbox = driver.find_element(By.ID, value="username")
email_textbox.send_keys(linkedin_username)
password_textbox = driver.find_element(By.ID, value="password")
password_textbox.send_keys(linkedin_password)
submit_button = driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
submit_button.click()

# Click through each job
time.sleep(2)
jobs = driver.find_elements(By.CSS_SELECTOR, value=".jobs-search-results__list-item")

for job in jobs:
    #print("looking at job")
    driver.execute_script("arguments[0].scrollIntoView();", job)
    job.click()
    time.sleep(2)
    #print("looking for save button")
    save_button = driver.find_element(By.CSS_SELECTOR, value=".jobs-save-button")
    save_button.click()
    time.sleep(2)
    #print("looking for follow button")
    follow_button = driver.find_element(By.CLASS_NAME, value="follow")
    actions = ActionChains(driver)
    actions.move_to_element(follow_button).perform()
    time.sleep(2)
    follow_button.click()
    time.sleep(2)
    
