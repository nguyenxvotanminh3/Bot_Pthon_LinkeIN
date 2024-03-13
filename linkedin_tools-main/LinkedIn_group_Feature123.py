from copy import copy
import csv
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import pytz
import selenium
import configparser
from termcolor import colored
import numpy as np
from selenium import webdriver
import random

print("Current tesst version is:", selenium.__version__)
# Select webdriver profile to use in selenium or not.
import sys
import os
import undetected_chromedriver as uc
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def driver_Profile(Profile_name):
    if Profile_name == "Yes":
        ### Selenium Web Driver Chrome Profile in Python
        # set proxy and other prefs.
        profile = webdriver.FirefoxProfile()
        profile.set_preference("network.proxy.type", 1)
        profile.set_preference("network.proxy.http", allproxs[0]['IP Address'])
        profile.set_preference("network.proxy.http_port", int(allproxs[0]['Port']))
        # update to profile. you can do it repeated. FF driver will take it.
        profile.set_preference("network.proxy.ssl", allproxs[0]['IP Address']);
        profile.set_preference("network.proxy.ssl_port", int(allproxs[0]['Port']))
        # profile.update_preferences()
        # You would also like to block flash
        # profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', False)
        profile.set_preference("media.peerconnection.enabled", False)

        # save to FF profile
        profile.update_preferences()
        driver = webdriver.Firefox(profile, executable_path='./geckodriver')
        # webrtcshield = r'/home/qtdata/PycharmProjects/BotSAM/webrtc_leak_shield-1.0.7.xpi'
        # driver.install_addon(webrtcshield)
        # urbanvpn = r'/home/qtdata/PycharmProjects/BotSAM/urban_vpn-3.9.0.xpi'
        # driver.install_addon(urbanvpn)
        # driver.profile.add_extension(webrtcshield)
        # driver.profile.add_extension(urbanvpn)
        # driver.profile.set_preference("security.fileuri.strict_origin_policy", False)
        ### Check the version of Selenium currently installed, from Python
        print("Current test version is:", selenium.__version__)
        print("Current web browser is", driver.name)
        ### Current time using time module
        ## current_time = time.strftime("%H:%M:%S", time.localtime())
        ## print("Current time is:",current_time)
        ### datetime object containing current date and time
        now = datetime.now()
        ### dd/mm/YY H:M:S
        dt_string = now.strftime("%B %d, %Y    %H:%M:%S")
        print("Current date & time is:", dt_string)
        print(colored("You are using webdriver profile!", "red"))
    else:
        driver = uc.Chrome(executable_path=r'/home/qtdata/PycharmProjects/BotSAM/chromedriver')
        ### Check the version of Selenium currently installed, from Python
        print("khong print gi ca: ", selenium.__version__)
        print("Current web browser is", driver.name)
        ### Current time using time module
        ## current_time = time.strftime("%H:%M:%S", time.localtime())
        ## print("Current time is:",current_time)
        ### datetime object containing current date and time
        now = datetime.now()
        ### dd/mm/YY H:M:S
        dt_string = now.strftime("%B %d, %Y    %H:%M:%S")
        print("Current date & time is:", dt_string)
        print(colored("You are NOT using webdriver profile!", "red"))
    return driver


# unused function
def Scroll_Pages_infinite_loading():
    ### Scroll to a page with infinite loading, like social network ones, facebook etc.
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    print("Begin scroll to a page with infinite loading.")
    # print("Begin Document Height", last_height)
    y = 0
    while True:
        # Scroll down to bottom
        for timer in range(0, 100):
            driver.execute_script("window.scrollTo(0, " + str(y) + ")")
            y += random.choice(np.arange(50, 60, 1))  # increase height random
            # print(random.choice(np.arange(50, 60, 1)), "&", y)
            time.sleep(0.1)
        # Wait to load page
        time.sleep(round(random.choice(np.arange(2, 5, 0.1)), 1))  # time sleep random
        # print("time sleep", round(random.choice(np.arange(2, 5, 0.1)), 1))
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            print("Stop scroll page with infinite loading.")
            break
        else:
            # print("new height", new_height, "last height", last_height)
            last_height = new_height


def Login_Linkedin(driver):
    baseDir = os.path.dirname(os.path.realpath(sys.argv[0])) + os.path.sep
    """ Setup Argument Parameters """
    config = configparser.RawConfigParser()
    config.read(baseDir + 'input/Account.cfg')
    api_key = config.get('API_KEYS', 'hunter')
    username = config.get('CREDS', 'linkedin_username')
    password = config.get('CREDS', 'linkedin_password')
    print(username, password)
    # head to Linkedin login page
    driver.get("https://www.linkedin.com/login")
    time.sleep(2)
    # find username/email field and send the username itself to the input field
    driver.find_element(By.ID, "username").send_keys(username)
    # find password input field and insert password as well
    driver.find_element(By.ID, "password").send_keys(password)
    # click login button
    driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div[1]/form/div[3]/button").submit()
    # wait for check robot
    WebDriverWait(driver, 60).until(EC.title_contains('Feed'))


def get_groups(driver):
    links = {}
    with open('input/keywords.csv', 'r') as csvfile:
        datareader = csv.reader(csvfile)
        for row in datareader:
            keyword = ''.join(row)
            for i in range(1, 2):
                pagenum = '&page=' + str(i)
                driver.get('https://www.linkedin.com/search/results/groups/?keywords=' + keyword + pagenum)
                time.sleep(2)
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                for website in soup.findAll('a', class_='app-aware-link', href=True):
                    links[website.get_text(strip=True)] = website['href']
                time.sleep(1)
            time.sleep(random.randint(3, 9))  # Let the user actually see something!
    linkedin_groups = pd.DataFrame(list(links.items()), columns=['Name', 'Website'])
    linkedin_groups.to_csv(f'{keyword}_linkedin_groups.csv', index=False)


def get_edited(driver, keyword):
    # from csv, check if group is already in requested or joined
    driver.get('https://www.linkedin.com/groups')
    # Check for each joined group is in csv files
    groups = driver.find_elements("name", "ember-view link-without-visited-state t-black")
    # Make a copy of the keyword csv
    filename = f'{keyword}_linkedin_groups'
    df = pd.read_csv(filename + '.csv')
    for group in groups:
        if group in copy:
            copy.drop(group)

    # Go to linkedin.com/groups/requested
    driver.get('https://www.linkedin.com/groups/requests')
    groups = driver.find_elements("name", "ember-view link-without-visited-state t-black")
    # Make a copy of the keyword csv
    for group in groups:
        if group in copy:
            copy.drop(group)
    df.to_csv('edited_' + filename + '_df.csv')


def join_group(driver, keyword):
    df = pd.read_csv(f'edited_{keyword}_linkedin_groups_df.csv', usecols=['Name', 'Website'])
    websites = df['Website']
    i = 0
    status = check_status(driver)
    while status[0] < 100 and status[1] < 20 and i < len(websites):
        url = websites[i]
        driver.get(url)
        time.sleep(5)
        try:
            element = driver.find_element("xpath",
                                          '/html/body/div[5]/div[3]/div/div[3]/div/div/main/div/div[1]/section/div/button/span/span[2]')
            if (element.get_attribute('innerText') == 'Join'):
                driver.find_element("xpath",
                                    '/html/body/div[5]/div[3]/div/div[3]/div/div/main/div/div[1]/section/div/button/span/span[2]').click()
        except:
            try:
                element = driver.find_element("xpath",
                                              '/html/body/div[4]/div[3]/div/div[3]/div/div/main/div/div[1]/section/div/button/span')
                if (element.get_attribute('innerText') == 'Join'):
                    driver.find_element("xpath",
                                        '/html/body/div[4]/div[3]/div/div[3]/div/div/main/div/div[1]/section/div/button/span').click()
            except:
                print('Join ' + url + ' failed')
        time.sleep(3)
        status = check_status(driver)
        i += 1
    # check for current status
    if status[0] == 100:
        print('Maximum number of groups joined (100)')
    if status[1] == 20:
        print('Maximum number of requests reached (20)')


def check_status(driver):
    # go to groups page
    time.sleep(3)
    driver.get('https://www.linkedin.com/groups')
    time.sleep(5)
    status = []
    # check the joined page
    num_of_joined = len(
        driver.find_elements("xpath", "//a[contains(@class, 'ember-view link-without-visited-state t-black')]"))
    time.sleep(3)
    # check the num of requests
    driver.get('https://www.linkedin.com/groups/requests')
    time.sleep(5)
    num_of_requests = len(
        driver.find_elements("xpath", "//a[contains(@class, 'ember-view link-without-visited-state t-black')]"))
    status = [num_of_joined, num_of_requests]
    return status


def returnLink(join_requested):
    return join_requested.get_attribute('href')


def get_result(driver):
    allstatus = {'Name': [], 'LinkedIn group': [], 'Result': [], 'Date': []}
    # go to groups page for joined
    driver.get('https://www.linkedin.com/groups')
    time.sleep(3)
    join_groups = driver.find_elements("xpath",
                                       "//a[contains(@class, 'ember-view link-without-visited-state t-black')]")
    list_link_join_group = list(map(returnLink, join_groups))
    for link in list_link_join_group:
        driver.get(link)
        time.sleep(5)
        date_joined = driver.find_element("xpath", "//p[contains(@class, 't-12 t-black--light')]").text.replace(
            'Joined group: ', '')
        name = driver.find_element("xpath", '//*[@id="group-entity-page"]/div/div/main/div/div[1]/section/div/h1/span')
        allstatus['Name'].append(name.text)
        allstatus['LinkedIn group'].append(link)
        allstatus['Result'].append('Joined')
        date = datetime.strptime(date_joined, '%b %Y')
        date1 = date.strftime('%m/%Y')
        allstatus['Date'].append(date.strftime('%m/%Y'))
        print(date1)

    # go to groups page for requested
    driver.get('https://www.linkedin.com/groups/requests')
    time.sleep(3)
    join_requested = driver.find_elements("xpath",
                                          "//a[contains(@class, 'ember-view link-without-visited-state t-black')]")
    list_link_join_requested = list(map(returnLink, join_requested))
    for link in list_link_join_requested:
        driver.get(link)
        time.sleep(5)
        name = driver.find_element("xpath", '//*[@id="group-entity-page"]/div/div/main/div/div[1]/section/div/h1/span')
        date_joined = datetime.today().strftime('%m/%d/%Y')
        allstatus['Name'].append(name.text)
        allstatus['LinkedIn group'].append(link)
        allstatus['Result'].append('Requested')
        allstatus['Date'].append(date_joined)

    # update status for the rest of the groups
    with open('input/keywords.csv', 'r') as csvfile:
        datareader = csv.reader(csvfile)
        for row in datareader:
            keyword = ''.join(row)
            df = pd.read_csv(f'{keyword}_linkedin_groups.csv')
            row_count = df.shape[0]
            for i in range(1, row_count):
                if df['Name'][i] not in allstatus['Name']:
                    allstatus['Name'].append(df['Name'][i])
                    allstatus['LinkedIn group'].append(df['Website'][i])
                    allstatus['Result'].append('Limit request to join')
                    allstatus['Date'].append('')

    allstatus = pd.DataFrame(allstatus)
    allstatus.to_csv('results.csv')


def post_and_get_link_in_group(driver):
    # go through each row
    df = pd.read_csv('Content.csv')
    num_of_comments = len(df.index)
    for i in range(0, num_of_comments):
        if df['Content'][i] != None:
            # get the link and go to link, assuming all groups here are joined
            driver.get(df['Linkedin group'][i])
            # check if group is joined
            time.sleep(3)
            # find the post button
            try:
                text_button = driver.find_element(By.Name,
                                                  'artdeco-button artdeco-button--muted artdeco-button--4 artdeco-button--tertiary ember-view share-box-feed-entry__trigger')
                text_button.click()
                time.sleep(2)
                driver.find_element(By.CLASS_NAME, "ql-editor").send_keys(df['Date'][i])
                time.sleep(5)
                post_button = driver.find_element("xpath",
                                                  '//*[@id="ember418"]')
                post_button.click()
                # find the link to the post (Assume post does not need to be under review)
                time.sleep(2)
                driver.find_element("xpath",
                                    '/html/body/div[6]/div[3]/div/div[2]/div/div/main/div/div[6]/div[1]/div/div/div/div/div/div/div[3]/div/button').click()
                time.sleep(2)
                viewpost = driver.find_element("xpath", '/html/body/div[1]/section/div/div/div/p/a').click()
                time.sleep(5)
                post_link = driver.current_url
                # get today's date as the date posted
                post_date = datetime.today().strftime('%m/%d/%Y')
                # append post link and post date to df
                df.loc[i, 'Result'] = post_link
                df.loc[i, 'Date'] = post_date
            except:
                print('You have not joined the group')
                df.loc[i, 'Result'] = ''
                df.loc[i, 'Date'] = ''
    df.to_csv('Content.csv')



def Google_search():
    #
    companies = {}
    board_of_directors = ["President", "Chief Executive Officer", "Chief Technology Officer",
                          "Chief Operating Officer", "Chief Customer Officer", "Chief Human Resources Officer",
                          "Chief Legal Officer and General Counsel", "Chief Financial Officer",
                          "Chief Investment Officer", "Owner", "Co-Owner", "Chairman", "Founder", "Co-Founder",
                          "Chief Security Officer"]
    with open('nonprofit.csv', 'r') as csvfile:
        datareader = csv.reader(csvfile)
        for row in datareader:
            company = ''.join(row)
            companies[company] = {}
            for position in board_of_directors:
                url = "http://www.google.com/search?q=" + " " + company + " " + position + " linkedin"
                driver.get(url)
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                website = soup.find('div', class_="yuRUbf")
                if type(website) != None:
                    link = website.a.get('href')
                    description = str(soup.find('div', class_="NJo7tc Z26q7c uUuwM"))
                    if company in description:
                        if "linkedin.com" in link:
                            if link not in str(companies[company].values()):
                                name = soup.find('h3').getText().split('-')[0]
                                companies[company][position] = name + link
                                print(companies[company][position])
                time.sleep(random.randint(3, 9))  # Let the user actually see something!
    return companies

def auto_join_group(driver):
    with open('input/keywords.csv', 'r') as csvfile:
        datareader = csv.reader(csvfile)
        for row in datareader:
            keyword = ''.join(row)
            get_edited(driver, keyword)
            # Join LinkedIn group
            join_group(driver, keyword)
    get_result(driver)  # returns the date joined

def auto_connect(driver):
    data = pd.read_csv('input/url_linkedin.csv')
    print(data['LinkedIn_Link'])

    # Enter the URL for 2nd Connections
    for index, row in data.iterrows():
        link = row['LinkedIn_Link']  # Thay 'LinkedIn_Link' bằng tên cột chứa URL LinkedIn
        # Kiểm tra URL của người dùng trên LinkedIn

        # Mở URL trên trình duyệt
        driver.get(link)
        time.sleep(2)
        # Tìm nút "Connect" và nhấn vào nó nếu có
        try:
            # all_buttons = driver.find_elements_by_tag_name("button")
            all_buttons = driver.find_elements(By.TAG_NAME, "button")
            connect_buttons = [btn for btn in all_buttons if btn.text == "Connect"]
            for btn in connect_buttons:
                driver.execute_script("arguments[0].click();", btn)

                time.sleep(2)
                add_a_note_button = driver.find_element(By.XPATH, '//button[@aria-label="Add a note"]')
                driver.execute_script("arguments[0].click();", add_a_note_button)
                time.sleep(2)
                # #find and click the Send now button
                # send = driver.find_element (By.XPATH, "//button[@aria-label = 'Send now']")
                # driver.execute_script("arguments[0].click();", send)
                # Tìm ô nhập note và điền nội dung
                note_input = driver.find_element(By.XPATH, "//textarea[@name='message']")
                note_input.send_keys("Xin chào! Tôi muốn kết nối với bạn.")
                time.sleep(2)

                # Click 'Send' button
                send_note = driver.find_element(By.XPATH, '//button[@aria-label="Send now"]')
                driver.execute_script("arguments[0].click();", send_note)
                time.sleep(2)

                # if the contact has secrurity settings enabled,
                # limiting adding to people they know, close the window and skip
                close_btn = driver.find_element(By.XPATH, "//button[@aria-label = 'Dismiss']")
                driver.execute_script("arguments[0].click();", close_btn)

                time.sleep(2)
        except Exception as e:
            print(f"Không tìm thấy nút Connect hoặc có lỗi: {e}")


if __name__ == '__main__':
    ### Select using drive profile or not ("Yes" or "No")
    ### Get time of a Python program's execution
    start_time = datetime.now()
    driver = driver_Profile('No')
    # linkedin groups
    results = Login_Linkedin()

    if results == True:
        links = get_groups()
        with open('input/keywords.csv', 'r') as csvfile:
            datareader = csv.reader(csvfile)
            for row in datareader:
                keyword = ''.join(row)
                get_edited(keyword)
                # Join LinkedIn group
                join_group(keyword)
        get_result()  # returns the date joined
        # post_and_get_link_in_group()  # returns the post date

    # If wait till accepted, login again
    # Login_Linkedin()
    # get_result('volunteer') #returns the date joined
    # post_and_get_link_in_group() #returns the post date

    time.sleep(1)

    self.driver.quit()
    ###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    ### Get time of a Python program's execution
    ## start_time = datetime.now()
    ## do your work here
    end_time = datetime.now()
    print(colored('Duration time: {} seconds '.format(end_time - start_time), "blue"), "\n start_time:", start_time,
          "\n", "end_time  :", end_time)
