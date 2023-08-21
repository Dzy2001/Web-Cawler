from selenium.webdriver import ChromeOptions
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

#

class Douyu(object):
    def __init__(self, url):
        self.url = url
        self.opt = ChromeOptions()
        self.opt.add_argument('--headless')
        self.opt.add_argument('--disable-')
        self.driver = Chrome(r'C:\Program Files\Google\Chrome\Application\chromedriver.exe', chrome_options = self.opt)

    def parse_data(self):
        a_list = self.driver.find_elements(By.XPATH, '//*[@id="listAll"]/section[2]/div[2]/ul/li/div')
        #print(a_list)
        print(len(a_list))
        temp_list = []
        for a in a_list:
            temp = {}
            temp['title'] = a.find_element(By.XPATH, r'./a/div[2]/div[1]/h3').text
            temp['type'] = a.find_element(By.XPATH, r'./a/div[2]/div[1]/span').text
            temp['owner'] = a.find_element(By.XPATH, r'./a/div[2]/div[2]/h2').text
            temp['fans'] = a.find_element(By.XPATH, r'./a/div[2]/div[2]/span').text
            #print(temp)
            temp_list.append(temp)
        return temp_list

    def save_data(self, data_list):
        for data in data_list:
            print(data)

    def run(self):
        # url
        # driver
        # get
        self.driver.get(self.url)
        while True:
            time.sleep(10)
            # parse
            temp_list = self.parse_data()
            # save
            self.save_data(temp_list)
            # next_page
            try:
                next_page = self.driver.find_element(By.XPATH, r'//*[@id="listAll"]/section[2]/div[2]/div/ul/li[9]/span')
                time.sleep(10)
                next_page.click()
            except:
                break


if __name__ == "__main__":
    url = 'https://www.douyu.com/directory/all'
    douyu = Douyu(url)
    douyu.run()
