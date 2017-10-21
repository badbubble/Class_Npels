from selenium import webdriver
import os

class Show(object):
    def __init__(self):
        URL = 'http://115.159.122.237/'
        self.drive = webdriver.Chrome()
        self.drive.get(URL)