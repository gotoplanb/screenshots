import selenium.webdriver as webdriver
import contextlib

urls = {
    'home': 'http://cloud.qa1.kony.com/',
    'cloud-products': 'http://cloud.qa1.kony.com/cloud-products',
    'products-visualization-gettingstarted': 'http://cloud.qa1.kony.com/products/visualization/getting-started',
    'products-development-gettingstarted': 'http://cloud.qa1.kony.com/products/development/getting-started',
    'products-management-gettingstarted': 'http://cloud.qa1.kony.com/products/management/getting-started',
    'blog': 'http://cloud.qa1.kony.com/blog',
    'blog-testingyourappsios': 'http://cloud.qa1.kony.com/blog/platform/testing-your-apps-ios',
    'support': 'http://cloud.qa1.kony.com/support',
    'manage': 'https://manage.qa-kony.com/#/manage-clouds/'
}

with contextlib.closing(webdriver.Firefox()) as driver:
    
    driver.implicitly_wait(10)

    driver.get('http://cloud.qa1.kony.com')
    login_email = driver.find_element_by_id('PrimaryEmail')
    login_email.send_keys('user.one@example.com')
    login_password = driver.find_element_by_id('Password')
    login_password.send_keys('password')
    login_submit = driver.find_element_by_css_selector('.konyButton')
    login_submit.click()
    
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
        driver.get_screenshot_as_file('new/nexus4/nexus4 ' + key + '.png')

driver.quit()
