from selenium import webdriver
import random
url_yes = 'https://docs.google.com/forms/d/e/1FAIpQLSelUSzWllrU9H7ML30XtU3ghBYMdZYKMjXZo4sXwQxxpiJVIA/viewform?usp=pp_url&entry.181540442=Yes&entry.1535349196=Hell+Yea!'
url_no = 'https://docs.google.com/forms/d/e/1FAIpQLSelUSzWllrU9H7ML30XtU3ghBYMdZYKMjXZo4sXwQxxpiJVIA/viewform?usp=pp_url&entry.181540442=No&entry.1535349196=No.'
url_no_pref = 'https://docs.google.com/forms/d/e/1FAIpQLSelUSzWllrU9H7ML30XtU3ghBYMdZYKMjXZo4sXwQxxpiJVIA/viewform?usp=pp_url&entry.181540442=No+Preference.&entry.1535349196=No+Preference.'

path_to_edge_driver = 'C:\\Users\\Ashish\\Desktop\\Codes For Fun\\Py Automation\\edgedriver_win64\\msedgedriver.exe'
driver = webdriver.Edge(path_to_edge_driver)

url_list = [url_yes, url_no, url_no_pref]

for i in range(20):
    url = random.choice(url_list)
    driver.get(url_yes)
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//*[contains(text(), 'Submit')]").click()
    driver.find_element_by_xpath("//*[contains(text(), 'Submit another response')]").click()
    driver.implicitly_wait(5)

