from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

ser = Service('../env/chromedriver.exe')

class Request:

        def __init__(self,url):
                self.url = url

        def get_selenium(self, class_name):
                '''
                This is the fuction inputs a URL and will output a parse that is headless and also will
                randomize the user. 
                '''
                software_names = [SoftwareName.CHROME.value]
                operating_systems = [OperatingSystem.WINDOWS.value,
                                     OperatingSystem.LINUX.value]
                user_agent_rotator = UserAgent(software_names=software_names,
                                                operating_systems=operating_systems,
                                                limit=100)
                user_agent = user_agent_rotator.get_random_user_agent()
                chrome_options = Options()
                chrome_options.add_argument("--headless")
                chrome_options.add_argument('--no-sandbox')
                chrome_options.add_argument('--window-size=1420,1080')
                chrome_options.add_argument('--disable-gpu')
                chrome_options.add_argument(f'user-agent={user_agent}')     
                browser = webdriver.Chrome(service=ser,options=chrome_options)
                browser.get(self.url)       
                time_to_wait = 15   
                try:
                        WebDriverWait(browser, time_to_wait).until(
                                EC.presence_of_element_located((By.CLASS_NAME, class_name))
                        )   
                except (TimeoutException, WebDriverException):
                        browser.quit()
                else:
                        browser.maximize_window()
                        page_html = browser.page_source
                        browser.quit()
                        return page_html     