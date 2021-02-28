# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 21:45:22 2021

@author: watar
"""

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

driver.get('https://')　#ここにログイン画面など最初のURLを入力する
print(driver.title)

search_box1 = driver.find_element_by_css_selector("#number1")　#ここにテキストを入力するところのCSSを入力する
search_box1.send_keys('aaaaa') #ここにテキストを入力する（パスワードなど）
driver.save_screenshot('search_results1.png')　#ここでスクショを取る
search_box2 = driver.find_element_by_css_selector("#number2")
search_box2.send_keys('aaaaa') #ここにテキストを入力する（パスワードなど）　#ここにテキストを入力するところのCSSを入力する
driver.save_screenshot('search_results2.png')　#ここでスクショを取る
search_box3 = driver.find_element_by_css_selector("#password")　#ここにテキストを入力するところのCSSを入力する
search_box3.send_keys('aaaaa') #ここにテキストを入力する（パスワードなど）
driver.save_screenshot('search_results3.png')　#ここでスクショを取る
search_btn1 = driver.find_element_by_css_selector("#idLogon")　#ここにボタンのCSSを入力する
search_btn1.click()　#ここでボタンをクリックする
driver.save_screenshot('search_results4.png')　#ここでスクショを取る
search_btn2 = driver.find_element_by_css_selector("#content > div:nth-child(2) > div > a")　#ここにボタンのCSSを入力する
search_btn2.click()　#ここでボタンをクリックする
driver.save_screenshot('search_results5.png')　#ここでスクショを取る
search_btn3 = driver.find_element_by_css_selector("#targetIdMenuobjectAAC")　#ここにボタンのCSSを入力する
search_btn3.click()　#ここでボタンをクリックする
driver.save_screenshot('search_results6.png')　#ここでスクショを取る
search_btn4 = driver.find_element_by_css_selector("#content > form:nth-child(1) > div:nth-child(4) > div > div:nth-child(1) > a")　#ここにボタンのCSSを入力する
search_btn4.click()　#ここでボタンをクリックする
driver.save_screenshot('search_results7.png')　#ここでスクショを取る




driver.save_screenshot('search_results.png')
driver.quit()
