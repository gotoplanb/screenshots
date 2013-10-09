import selenium.webdriver as webdriver
import contextlib

urls = {
    'search': 'http://www.google.com/',
    'images': 'https://www.google.com/imghp',
}

with contextlib.closing(webdriver.Firefox()) as driver:
    
    driver.implicitly_wait(10)
    
    for key in urls.keys():
        
        print key, urls[key]
    
        driver.get(urls[key])
        
        driver.set_window_size(1280,800)
        driver.get_screenshot_as_file('new/desktop/desktop ' + key + '.png') 
    
        driver.set_window_size(768,1024)
        driver.get_screenshot_as_file('new/ipad/ipad ' + key + '.png') 
    
        driver.set_window_size(320,568)
        driver.get_screenshot_as_file('new/iphone/iphone ' + key + '.png')
    
        driver.set_window_size(320,640)
        driver.get_screenshot_as_file('new/galaxys4/galaxys4 ' + key + '.png') 
    
        driver.set_window_size(601,906)
        driver.get_screenshot_as_file('new/nexus7/nexus7 ' + key + '.png')
    
        driver.set_window_size(384,592)
        driver.get_screenshot_as_file('new/exus4/nexus4 ' + key + '.png')
