from selenium import webdriver
import time
import random
import string

letters = string.ascii_lowercase
Firstname = ''.join(random.choice(letters) for i in range(5))
Lastname = ''.join(random.choice(letters) for i in range(5))
Emailting = ''.join(random.choice(letters) for i in range(5))

PATH = "/usr/local/chromedriver/"
driver = webdriver.Chrome(PATH)

driver.get("https://www.currys.co.uk/perks-prizes.html")

Accept_Cookies = driver.find_element_by_xpath("/html/body/div[7]/div[3]/div/div/div[2]/div/div/button")
Accept_Cookies.click()

driver.execute_script("window.scrollTo(0, 500)")
time.sleep(1)

frame = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div/div/div/iframe")
driver.switch_to.frame(frame)

Get_Cracking = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/input[1]")
Get_Cracking.click()

time.sleep(1)

Egg = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div[2]/div[2]/div[1]/div[2]")
Egg.click()

time.sleep(1)
el = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div[2]/div[1]/div/div[1]/div/select')
Mr = el.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/div[2]/div[1]/div/div[1]/div/select/option[2]')
Mr.click()

Forename = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div[2]/div[2]/div/input")
Forename.send_keys(Firstname)

Surname = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div[2]/div[3]/div/input")
Surname.send_keys(Lastname)


Email = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div[2]/div[4]/div/input")
Email.send_keys(Emailting + "@gmail.com")
