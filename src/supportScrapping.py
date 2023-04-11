from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = False
options.add_argument("--window-size=1920,1200")

driver = webdriver.Firefox(options=options)

def _extract_href(item):
    return item.get_attribute('href')

def loadAllListings(url):
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    driver.find_element('css selector', 'button.sui-AtomButton--primary:nth-child(2)').click()
    sleep(2)
    js = "const fun = async function scrollToAll(){ do{ var elements = document.getElementsByClassName('re-CardPackPremiumPlaceholder'); for (const index in elements){ const item = elements[index]; console.log(elements); if (item != null && item instanceof HTMLElement){ console.log(item); item.scrollIntoView(); await new Promise(r => setTimeout(r, 1000)); } } }while(elements.length > 0); }; fun().then(function(){alert('done')});"
    driver.execute_script(js)
    WebDriverWait(driver, 30).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    # Get all links to listings
    elements = driver.find_elements(By.XPATH, '//article[contains(@class, "re-CardPackPremium") or contains(@class, "re-CardPackAdvance") or contains(@class, "re-CardPackMinimal")]/a')
    href_list = list(map(_extract_href, elements))
    driver.quit()
    return href_list

def getMaxPages(url): #Requires running loadAllListings(url) before
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    driver.find_element('css selector', 'button.sui-AtomButton--primary:nth-child(2)').click()
    sleep(2)
    max_page = None
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight-4000)")
    sleep(1)
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/main/div/div[3]/ul/li[6]/a/span')
                                                    #/html/body/div[1]/div[1]/div[2]/main/div/div[3]/ul/li[4]/a/span
    if element:
        max_page = element.text
    driver.quit()
    return max_page