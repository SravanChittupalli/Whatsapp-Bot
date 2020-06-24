from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://web.whatsapp.com/')
time.sleep(5)


chat_name = input("Enter chat name: ")
chat = browser.find_element_by_xpath('//span[@title="{0}"]'.format(chat_name)) 
chat.click()


message = input("Enter message to be sent: ")
no = int(input("No. of messages: "))

for i in range (0 , no , 1):
    message_box = browser.find_element_by_xpath('//div[@class="_3uMse"]')
    message_box.send_keys('{}'.format(message))

    send = browser.find_element_by_xpath('//button[@class="_1U1xa"]')
    send.click()