from selenium import webdriver  #Imports the selenium web driver
driver = webdriver.Firefox()    #Creates a Firefox Webdriver
driver.get("https://www.facebook.com/")  #Tells the driver to go to the facebook.com
driver.find_element_by_css_selector("#email").send_keys("Your User name for facebook") # Finds email and writes your email address.
driver.find_element_by_css_selector("#pass").send_keys("Your Password") # Finds password and writes your password.
buttons = element = driver.find_element_by_id("u_0_s")
buttons.click()

