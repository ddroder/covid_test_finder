import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
# from store_details import stores
class stores:
    def __init__(self,store_name,driver='chrome',zip=44141) -> None:
        self.store_name=store_name
        self.driver_type="chrome"
        self.zip=zip
        # self.driver=webdrive.chrome()
        CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
        s=Service(CHROMEDRIVER_PATH)
        self.chrome_options=Options() 
        # self.chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--no-sandbox") 
        



    def scrape_items(self):
        """
        scrape function, no inputs needed because of general attributes of init class.
        """
        skus=self._get_skus()
        url=skus['url']
        if self.driver_type=='chrome':

            for sku in skus['sku_nums']:
                self._parse_skus_(url,sku)
            return skus
    def _parse_skus_(self,url,sku_num):
        self.driver=webdriver.Chrome(options=self.chrome_options) 
        time.sleep(5)
        self.driver.get(url)

        print("sending keys to sku...")
        sku_form=self.driver.find_element(By.ID,"inventory-checker-form-sku")
        sku_form.send_keys(sku_num)

        print("sending keys to zip...")
        zip_form=self.driver.find_element(By.ID,"inventory-checker-form-zip")
        zip_form.send_keys(self.zip)
        print("sending click...")
        button_click=self.driver.find_element(By.CLASS_NAME,'bs-button').click()
        time.sleep(2)
        self.driver.close()

    def _get_skus(self):
        """
        helper function that returns a dictionary.

        RETURNS
            dict:
                STORE_NAME,URL,SKU_NUMBERS
        """
        self.store_paths=[
            {"store":'walmart',"url":'https://brickseek.com/walmart-inventory-checker/',"sku_nums":[142089281,373165472,953499978,916411293]},
            {"store":"cvs","url":"https://brickseek.com/cvs-inventory-checker/","sku_nums":[550147,823994]}
    ]
        for i in self.store_paths:
            if i['store'] == self.store_name:
                return i

if __name__=="__main__":
    i=stores('cvs')    
    items=i.scrape_items()
    print(items)
    