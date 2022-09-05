# -*- coding: utf-8 -*-
from util.read_ini import ReadIni
from selenium.webdriver.common.by import By


class FindElement:
    """读取ini文件，匹配css路径"""
    def __init__(self, driver):
        self.driver = driver

    def read_in(self,key):
        read_ini = ReadIni()
        data = read_ini.get_value(key)
        by = data.split('>>')[0]
        value = data.split('>>')[1]
        return by,value

    def get_element(self, key):
        read_ini = ReadIni()
        data = read_ini.get_value(key)
        by = data.split('>>')[0]
        value = data.split('>>')[1]
        try:
            if by == 'id':
                return self.driver.find_element(By.ID,value)
            elif by == 'name':
                return self.driver.find_element(By.NAME,value)
            elif by == 'class':
                return self.driver.find_element(By.CLASS_NAME,value)
            elif by == 'xpath':
                return self.driver.find_element(By.XPATH,value)
            elif by == 'css':
                return self.driver.find_element(By.CSS_SELECTOR, value)
            elif by == 'link_text':
                return self.driver.find_element(By.LINK_TEXT, value)
            elif by == 'tag_name':
                return self.driver.find_element(By.TAG_NAME, value)
        except:
            return None

    def get_elements(self, key):
        read_ini = ReadIni()
        data = read_ini.get_value(key)
        by = data.split('>>')[0]
        value = data.split('>>')[1]
        try:
            if by == 'id':
                return self.driver.find_elements(By.ID, value)
            elif by == 'name':
                return self.driver.find_elements(By.NAME, value)
            elif by == 'class':
                return self.driver.find_elements(By.CLASS_NAME, value)
            elif by == 'xpath':
                return self.driver.find_elements(By.XPATH, value)
            elif by == 'css_selector':
                return self.driver.find_elements(By.CSS_SELECTOR, value)
            elif by == 'link_text':
                return self.driver.find_elements(By.LINK_TEXT, value)
            elif by == 'tag_name':
                return self.driver.find_elements(By.TAG_NAME, value)
        except:
            return None