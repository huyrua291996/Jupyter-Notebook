from selenium import webdriver

driver = webdriver.Firefox(executable_path="C:\Users\huyru\Downloads\Compressed\geckodriver-v0.19.1-win64\geckodriver")
re = driver.get("https://facebook.com")
re = driver.find_element_by_name('email')
re.send_keys('ngochuy_gerrard_96@yahoo.com')
re = driver.find_element_by_name('pass')
re.send_keys('nguyenngochuy')
re = driver.find_element_by_id('loginbutton')
re.click()