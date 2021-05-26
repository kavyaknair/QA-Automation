import pytest
import sys
from selenium import webdriver
import time

#Q) Assert Broken images
def test_broken_images():
    driver = webdriver.Firefox()
    driver.get("http://the-internet.herokuapp.com/broken_images")
    element = driver.find_element_by_xpath('/html/body/div[2]/div/div/img')
    e = bool(driver.execute_script("return arguments[0].complete && typeof arguments[0].naturalWidth != \"undefined\" && arguments[0].naturalWidth == 0", element))
    assert e == True

#Q) Assert forgot password success message on the page
def test_forgot_password():
    driver = webdriver.Firefox()
    driver.get("http://the-internet.herokuapp.com/forgot_password")
    message = driver.find_elements_by_tag_name('h2')[0].text
    assert message == "Forgot Password"

#Q) Assert form validation functionality Post entering a dummy username and password on
def test_form_validation():
    driver = webdriver.Firefox()
    driver.get("http://the-internet.herokuapp.com/login")
    username = driver.find_element_by_id("username")
    password = driver.find_element_by_id("password")
    username.send_keys("user@name")
    password.send_keys("pass@word")
    time.sleep(25)
    driver.find_elements_by_xpath('/html/body/div[2]/div/div/form/button/i')[0].click()
    time.sleep(10)
    element = bool(driver.find_elements_by_xpath('//*[@id="flash"]'))
    assert element == True

#Q) Write a test to enter alphabets on this and mark it as a failure if we cannot enter on page
def test_enter_text():
    driver = webdriver.Firefox()
    driver.get("http://the-internet.herokuapp.com/inputs")
    element = driver.find_element_by_xpath("//input[@type='number']").is_enabled()
    assert element == True

#Q) Write a looped script to assert a 'successful notification" after repeated unsuccessful notification on page
def test_successful_notification(): 
    driver = webdriver.Firefox()
    driver.get("http://the-internet.herokuapp.com/notification_message_rendered")
    driver.find_elements_by_xpath('//*[@id="content"]/div/p/a')[0].click()
    while driver.find_elements_by_xpath('//div[contains(text(), "Action unsuccesful, please try again")]'):
        driver.find_elements_by_xpath('//*[@id="content"]/div/p/a')[0].click()
    element = driver.find_elements_by_xpath('//*[@id="flash"]')[0].text
    assert "Action successful" in element

#Q) Write a test to sort the table by the amount due on page
def test_get_current_element_order():
    driver = webdriver.Firefox()
    driver.get("http://the-internet.herokuapp.com/tables")
    rws = driver.find_element_by_xpath('//*[@id="table1"]/tbody')
    element = []
    for row in rws.find_elements_by_xpath('.//tr'):
        row_text = [row_val.text for row_val in row.find_elements_by_xpath('.//td')]
        element.append(row_text)
    print(element)
    element.sort(key = lambda x:float(x[3].replace('$', '')))
    print(element)
    assert element