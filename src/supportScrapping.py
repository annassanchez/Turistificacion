from time import sleep
import re
import pickle

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

def seleniumFotocasa(url, dict_):
    driver = webdriver.Firefox()
    driver.get(url)
    driver.maximize_window()
    driver.set_window_size(1920, 1080)
    driver.implicitly_wait(30)
    driver.find_element('css selector', 'html body.search.br-Firefox.os-MacOS.osv-10_15 div#App div.re-SharedCmp div.sui-TcfFirstLayer div.sui-MoleculeModal.is-static.is-MoleculeModal-open div.sui-MoleculeModal-dialog.sui-MoleculeModal-dialog--fit footer.sui-MoleculeModalFooter div.sui-TcfFirstLayer-buttons button.sui-AtomButton.sui-AtomButton--primary.sui-AtomButton--solid.sui-AtomButton--center').click()
    js = """const fun = async function scrollToAll(){ 
        do{ 
            var elements = document.getElementsByClassName('re-CardPackPremiumPlaceholder'); 
            for (const index in elements){ 
                const item = elements[index]; 
                console.log(elements); 
                if (item != null && item instanceof HTMLElement){ 
                    console.log(item); item.scrollIntoView(); 
                    await new Promise(r => setTimeout(r, 1000)); 
                    } 
                    } 
                    }
                    while(elements.length > 0); 
                    }; 
                    """
    driver.execute_script(js)
    try: 
        print('lo intento')
        for i in range(1,31):
            print('element:', i, 'page:')
            try:
                element = driver.find_element(By.CLASS_NAME, "re-CardPackPremiumPlaceholder")
                driver.execute_script("arguments[0].scrollIntoView();", element)
                try:
                    name = driver.find_element(By.XPATH, f'/html/body/div[1]/div[1]/div[2]/main/div/div[2]/section/article[{i}]/div[2]/a/h3/span[1]').text
                                                    #/html/body/div[1]/div[1]/div[2]/main/div/div[2]/section/article[2]/div[2]/a/h3/span[1]
                                                    #/html/body/div[1]/div[1]/div[2]/main/div/div[2]/section/article[30]/div[2]/a/h3/span[1]
                except: name = None
                try:
                    price = driver.find_element(By.XPATH, f'/html/body/div[1]/div[1]/div[2]/main/div/div[2]/section/article[{i}]/div[2]/a/h3/span[2]/span[1]/span').text
                                                    #/html/body/div[1]/div[1]/div[2]/main/div/div[2]/section/article[2]/div[2]/a/h3/span[2]/span[1]/span
                except: price = None
                try:
                    address = re.findall(r'en|con(.*)', driver.find_element(By.XPATH, f'/html/body/div[1]/div[1]/div[2]/main/div/div[2]/section/article[{i}]/div[2]/a/h3/span[1]').text)
                except: address = None    
                try:
                    owner = driver.find_element(By.XPATH, f'/html/body/div[1]/div[1]/div[2]/main/div/div[2]/section/article[{i}]/div[1]/span/span[1]').text
                                                        #/html/body/div[1]/div[1]/div[2]/main/div/div[2]/section/article[1]/div[1]/span/span[1]
                                                        #/html/body/div[1]/div[1]/div[2]/main/div/div[2]/section/article[2]/div[1]/span/span[1]
                except: owner = None  
                try:
                    url = driver.find_element(By.XPATH, f'/html/body/div[1]/div[1]/div[2]/main/div/div[2]/section/article[{1}]/div[2]/a').get_attribute('href')
                                                        #/html/body/div[1]/div[1]/div[2]/main/div/div[2]/section/article[1]/div[2]/a
                                                        #/html/body/div[1]/div[1]/div[2]/main/div/div[2]/section/article[2]/div[2]/a
                except: url = None   
                dict_['name'].append(name)
                dict_['price'].append(price)
                dict_['address'].append(address)
                dict_['owner'].append(owner)
                dict_['url'].append(url)
            except:
                pass
        print('done with page x')
        with open(f'../data/dict_test.pickle', 'wb') as data_scrapeado:
            pickle.dump(dict_, data_scrapeado)
    except:
        print('no lo intento')

def scroll_down(self):
    """A method for scrolling the page."""

    # Get scroll height.
    last_height = self.driver.execute_script("return document.body.scrollHeight")

    while True:

        # Scroll down to the bottom.
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load the page.
        sleep(2)

        # Calculate new scroll height and compare with last scroll height.
        new_height = self.driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:

            break

        last_height = new_height