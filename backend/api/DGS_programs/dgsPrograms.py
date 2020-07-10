from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import os
import re
import sys


class DGSPrograms:


    def __init__(self, csis_id = ""):
        self.csis_id = csis_id
    
    def get_file_content(self, filename):
        file = open(filename, 'r')
        result = file.read()
        file.close()
        return result
    
    def save_file_content(self, filename, file_content):
        file = open(filename, 'w')
        file.write(file_content)
        file.close()

    def requestHeaders(self):
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
		'Accept-Encoding': 'none',
		'Accept-Language': 'en-US,en;q=0.8',
		'Connection': 'keep-alive'}
        return headers
    
    def DGS_program(self):

        programs = []
        child_family_community_studies = []
        commerce_business_administration = []
        health_sciences = []
        humanities_social_sciences = []
        language_literatrue_programing_arts = []
        science_technology = []

        URL = "https://www.douglascollege.ca/programs-courses/catalogue/programs"

        # Get the driver to use Webdriver which is ued in scraping data from JavaScript
        driver = webdriver.Chrome(executable_path='./drivers/chromedriver')
        driver.get(URL)

        soup = BeautifulSoup(driver.page_source,"html.parser")
        
        all_div = soup.find_all("div", class_= 'column program-section')
        for div in all_div:
            all_prgs = div.find_all("a")
            for prg in all_prgs:
                data = prg.text
                programs.append(data)
        
        #Delete None value in list
        programs = filter(None, programs)

        #`All programs in Douglas College`
        #child_family_community_studies.extend(programs[:23])
        commerce_business_administration.extend(programs[23:91])
        #health_sciences.extend(programs[91:101])
        #humanities_social_sciences.extend(programs[101:130])
        #language_literatrue_programing_arts.extend(programs[130:152])
        #science_technology.extend(programs[152:173])

        return commerce_business_administration
        
        #close browser session
        driver.quit()
        
    # Get the only CSIS data 
    def CSIS_Program(self,commerce_business_administration):
        csis_programs = []
        csis_programs.extend(commerce_business_administration[33:40])
        for values in csis_programs:
            print(values)


    @staticmethod
    def run():
        dgs = DGSPrograms()
        cmrbsnadmin= dgs.DGS_program()
        dgs.CSIS_Program(cmrbsnadmin)
        

