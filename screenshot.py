import os
import subprocess
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
        oldFile = 'old/desktop/desktop ' + key + '.png'
        newFile = 'new/desktop/desktop ' + key + '.png'
        diffFile = 'diff/desktop/desktop ' + key + '.png'
        os.rename(newFile,oldFile)
        driver.get_screenshot_as_file(newFile)
        subprocess.call(["imgdiff", oldFile, newFile, "-o", diffFile])
    
        driver.set_window_size(768,1024)
        oldFile = 'old/ipad/ipad ' + key + '.png'
        newFile = 'new/ipad/ipad ' + key + '.png'
        diffFile = 'diff/ipad/ipad ' + key + '.png'
        os.rename(newFile,oldFile)
        driver.get_screenshot_as_file(newFile)
        subprocess.call(["imgdiff", oldFile, newFile, "-o", diffFile])
    
        driver.set_window_size(320,568)
        oldFile = 'old/iphone/iphone ' + key + '.png'
        newFile = 'new/iphone/iphone ' + key + '.png'
        diffFile = 'diff/iphone/iphone ' + key + '.png'
        os.rename(newFile,oldFile)
        driver.get_screenshot_as_file(newFile)
        subprocess.call(["imgdiff", oldFile, newFile, "-o", diffFile])
    
        driver.set_window_size(320,640)
        oldFile = 'old/galaxys4/galaxys4 ' + key + '.png'
        newFile = 'new/galaxys4/galaxys4 ' + key + '.png'
        diffFile = 'diff/galaxys4/galaxys4 ' + key + '.png'
        os.rename(newFile,oldFile)
        driver.get_screenshot_as_file(newFile)
        subprocess.call(["imgdiff", oldFile, newFile, "-o", diffFile])
    
        driver.set_window_size(601,906)
        oldFile = 'old/nexus7/nexus7 ' + key + '.png'
        newFile = 'new/nexus7/nexus7 ' + key + '.png'
        diffFile = 'diff/nexus7/nexus7 ' + key + '.png'
        os.rename(newFile,oldFile)
        driver.get_screenshot_as_file(newFile)
        subprocess.call(["imgdiff", oldFile, newFile, "-o", diffFile])
    
        driver.set_window_size(384,592)
        oldFile = 'old/nexus4/nexus4 ' + key + '.png'
        newFile = 'new/nexus4/nexus4 ' + key + '.png'
        diffFile = 'diff/nexus4/nexus4 ' + key + '.png'
        os.rename(newFile,oldFile)
        driver.get_screenshot_as_file(newFile)
        subprocess.call(["imgdiff", oldFile, newFile, "-o", diffFile])

driver.quit()
