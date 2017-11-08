#!/usr/bin/python3
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048')

htmlElem = browser.find_element_by_tag_name('html')
moves = [Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT]

gameOver = browser.find_element_by_class_name('mailing-list-email-field')
while True:
    for move in moves:
        try:
            htmlElem.send_keys(move)
        except KeyboardInterrupt:                   # TODO: exit on finish
            sys.exit()
