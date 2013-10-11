import os
import selenium.webdriver as webdriver
import contextlib

import settings

with contextlib.closing(webdriver.Firefox()) as driver:
    
    driver.implicitly_wait(10)

    driver.get(settings.auth_url)
    login_email = driver.find_element_by_id(settings.auth_username_id)
    login_email.send_keys(settings.username)
    login_password = driver.find_element_by_id(settings.auth_password_id)
    login_password.send_keys(settings.password)
    login_submit = driver.find_element_by_css_selector(settings.auth_submit_class)
    login_submit.click()
    
    for key in settings.urls.keys():
        
        print key, settings.urls[key]
    
        driver.get(settings.urls[key])
        
        driver.set_window_size(1280,800)
        os.rename('new/desktop/desktop ' + key + '.png','old/desktop/desktop ' + key + '.png')
        driver.get_screenshot_as_file('new/desktop/desktop ' + key + '.png') 
    
        driver.set_window_size(768,1024)
        os.rename('new/ipad/ipad ' + key + '.png','old/ipad/ipad ' + key + '.png')
        driver.get_screenshot_as_file('new/ipad/ipad ' + key + '.png') 
    
        driver.set_window_size(320,568)
        os.rename('new/iphone/iphone ' + key + '.png','old/iphone/iphone ' + key + '.png')
        driver.get_screenshot_as_file('new/iphone/iphone ' + key + '.png')
    
        driver.set_window_size(320,640)
        os.rename('new/galaxys4/galaxys4 ' + key + '.png','old/galaxys4/galaxys4 ' + key + '.png')
        driver.get_screenshot_as_file('new/galaxys4/galaxys4 ' + key + '.png') 
    
        driver.set_window_size(601,906)
        os.rename('new/nexus7/nexus7 ' + key + '.png','old/nexus7/nexus7 ' + key + '.png')
        driver.get_screenshot_as_file('new/nexus7/nexus7 ' + key + '.png')
    
        driver.set_window_size(384,592)
        os.rename('new/nexus4/nexus4 ' + key + '.png','old/nexus4/nexus4 ' + key + '.png')
        driver.get_screenshot_as_file('new/nexus4/nexus4 ' + key + '.png')

driver.quit()
