import re
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
# from store_details import stores
class stores:
    def __init__(self,store_name,driver='chrome',zip=44141) -> None:
        self.all_addresses=[]
        self.all_distances=[]
        self.all_quants=[]
        self.store_name=store_name
        self.driver_type="chrome"
        self.zip=zip
        # self.driver=webdrive.chrome()
        CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
        s=Service(CHROMEDRIVER_PATH)
        self.chrome_options=Options() 
        self.chrome_options.add_argument("--headless")
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
            print(self.all_quants)
            return skus
    def _parse_skus_(self,url,sku_num):
        self.driver=webdriver.Chrome(options=self.chrome_options) 
        # time.sleep(5)
        self.driver.implicitly_wait(3)
        self.driver.get(url)

        print("sending keys to sku...")
        sku_form=self.driver.find_element(By.ID,"inventory-checker-form-sku")
        sku_form.send_keys(sku_num)

        print("sending keys to zip...")
        zip_form=self.driver.find_element(By.ID,"inventory-checker-form-zip")
        zip_form.send_keys(self.zip)

        print("clicking dropdown for quantity...")
        sort_by_button=self.driver.find_element(By.ID,"inventory-checker-form-sort")
        sort_by_button.click()
        item=sort_by_button.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/main/div/form/div/div[3]/div/div/select/option[3]")
        item.click()

        print("sending click...")
        button_click=self.driver.find_element(By.CLASS_NAME,'bs-button').click()
        # time.sleep(5)
        self.driver.implicitly_wait(5)
        html=self.driver.page_source
        self._soup_things(html)
        # self._get_table_row(html)

        self.driver.close()



    def _soup_things(self,html):
        soup=BeautifulSoup(html,"html.parser")
        self.addresses=self._get_addr(soup)
        # print(self.addresses[0])
        # self.distances=self._get_distance(soup)
        # i=self.distances
        self._get_table_row(soup)

    def _get_table_row(self,soup):
        rows=soup.select("div",{"class":"table__row"})
        addrs=[]
        for row in rows:
            i=row.find("address",{"class":"address"})
            addrs.append(i)
        dists=self._get_distance(soup)
        addrs=self._get_addr(soup)
        quant=self._get_quantity_(soup)
        
        self.all_addresses.append(addrs)
        self.all_distances.append(dists)
        self.all_quants.append(quant)
    def _get_quantity_(self,soup):
        soup=str(soup)
        quants=re.findall(r"Qty: (\d+)",soup)
        return quants
        # print(soup)
        # pass
    def _get_distance(self,soup):
        self.distances=re.findall(r"(\d.+) Miles",str(soup))
        return self.distances


    def _get_addr(self,soup):
        self.div=soup.select_one("table#inventory-checker-table inventory-checker-table--store-availability-price inventory-checker-table--columns-3")
        self.addresses1=soup.find_all('address')
        all_addy=[]
        for addy in self.addresses1:
            experiment=str(addy).replace("<br/>","").split(">")[1].split("<")[0].replace('\n','')
            all_addy.append(experiment)
        return all_addy

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
            # {"store":"cvs","url":"https://brickseek.com/cvs-inventory-checker/","sku_nums":[550147]}
    ]
        for i in self.store_paths:
            if i['store'] == self.store_name:
                return i

if __name__=="__main__":
    i=stores('cvs')    
    items=i.scrape_items()
    # print(items)
    