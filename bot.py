from selenium import webdriver
import time

class init_bot():
	# Init function only initializes the the driver instance.
	def __init__(self):
		path_to_edge_driver = 'C:\\Users\\Ashish\\Desktop\\Codes For Fun\\Py Automation\\edgedriver_win64\\msedgedriver.exe'
		self.driver = webdriver.Edge(path_to_edge_driver)

class fetch_responses(init_bot):
    def select_yes(self):
        driver = self.driver
        url = 'https://docs.google.com/forms/d/e/1FAIpQLSelUSzWllrU9H7ML30XtU3ghBYMdZYKMjXZo4sXwQxxpiJVIA/viewform'
        driver.get(url)
        
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//*[contains(text(), 'Yes')]").click()
        time.sleep(3)
        
        driver.find_element_by_xpath("//*[contains(text(), 'Hell Yea!')]").click()
        time.sleep(3)
        
        driver.find_element_by_xpath("//*[contains(text(), 'Submit')]").click()
        driver.quit()
        # driver.find_element_by_xpath("//*[contains(text(), 'Submit another response')]").click()
        
    def select_no(self):
        driver = self.driver
        url = 'https://docs.google.com/forms/d/e/1FAIpQLSelUSzWllrU9H7ML30XtU3ghBYMdZYKMjXZo4sXwQxxpiJVIA/viewform'
        driver.get(url)
        
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//*[contains(text(), 'No'").click()
        time.sleep(3)
        
        driver.find_element_by_xpath("//*[contains(text(), 'No.')]").click()
        time.sleep(3)
        
        driver.find_element_by_xpath("//*[contains(text(), 'Submit')]").click()
        driver.quit()
        
        # driver.find_element_by_xpath("//*[contains(text(), 'Submit another response')]").click()
    
    def select_no_pref(self):
        driver = self.driver
        url = 'https://docs.google.com/forms/d/e/1FAIpQLSelUSzWllrU9H7ML30XtU3ghBYMdZYKMjXZo4sXwQxxpiJVIA/viewform'
        driver.get(url)
        
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//*[contains(text(), 'No Preference.')]").click()
        time.sleep(3)
        
        driver.find_element_by_xpath("//*[contains(text(), 'No Preference.')]").click()
        time.sleep(3)
        
        driver.find_element_by_xpath("//*[contains(text(), 'Submit')]").click()
        # driver.implicitly_wait(10)
        driver.quit()

if __name__ == '__main__':
    for i in range(20):
        bot = fetch_responses()
        bot.select_yes()
        bot.select_no()
        bot.select_no_pref()
        print(i)