from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep



class Task:
    url = "https://www.instagram.com/guviofficial/"

class Insta_Guvi(Task):

    def __init__(self, url):# constructor method , this is one call automatically
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) # Initialize the web driver

    #Open the URL
    def open(self):
            self.driver.maximize_window()
            self.driver.get(self.url)
            sleep(5)
            return True

    # Extract the no. of GUVI Insta followers
    def Insta_Followers(self):

        followers_element = self.driver.find_element(by=By.XPATH, value="//ul[@class='x78zum5 x1q0g3np xieb3on']//li[2]//div//span/span")
        sleep(3)

        print("Followers :", followers_element.text)
        return True

    # Extract the no. of GUVI Insta following
    def Insta_Following(self):

        following_element=self.driver.find_element(by=By.XPATH, value="//ul[@class='x78zum5 x1q0g3np xieb3on']//li[3]//div//span//span")
        sleep(3)

        print("Following :", following_element.text)
        return True

    def close(self):

        self.driver.quit()
        return None



if __name__ == "__main__":
    syed = Insta_Guvi("https://www.instagram.com/guviofficial/")
    syed.open()
    syed.Insta_Followers()
    syed.Insta_Following()
    syed.close()
