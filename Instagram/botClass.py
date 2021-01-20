from selenium import webdriver
from time import sleep

class InstaBot:
    def __init__(self,username, password):
        '''Initializer of the InstaBot'''
        self.chromedriver = r"C:\Users\Andre\Desktop\chromedriver_win32\chromedriver.exe"
        self.driver = webdriver.Chrome(self.chromedriver)
        self.driver.get ("https://www.instagram.com/")
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/article/div[2]/div[1]/div/form/div[4]").click()
        sleep(2)
        loginUsername = self.driver.find_element_by_xpath('//input[@name=\"username\"]').send_keys(username)
        loginPassword = self.driver.find_element_by_xpath('//input[@name=\"password\"]').send_keys(password)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(4)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
        sleep(2)

    def storySlider(self):
        '''method that opens up instagram stories '''
        #opens up the stories
        #opens up the first story
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div/div[1]/div/div/div/div/ul/li[3]/div/button').click()

    def storyClicker(self):
        '''Method that clicks the next button on instagram stories'''
        #click that lets me press the next arrow
        self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div/section/div[2]/button[2]').click()

    def getNumOfStories(self):
        '''returns the number of instagram stories'''
        num = len(self.driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/section/div/div[1]/div/div/div/div/ul/li[3]/div/button'))
        int(num)
        return num

    def storyCancel(self):
        '''Clicks out'''
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div/section/div[2]/button[3]').click()

