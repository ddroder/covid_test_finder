class stores:
    def __init__(self,store_name,zip=44141) -> None:
        self.store_name=store_name
        self.zip=zip

    def scrape_items(self):
        skus=self._get_skus()
        url=skus['url']
        return skus

    def _get_skus(self):
        """
        helper function that returns a dictionary.

        RETURNS
            dict:
                STORE_NAME,URL,SKU_NUMBERS
        """
        self.store_paths=[
            {"store":'walmart',"url":'https://brickseek.com/walmart-inventory-checker/',"sku_num":[142089281,373165472,953499978,916411293]},
            {"store":"cvs","url":"https://brickseek.com/cvs-inventory-checker/","sku_nums":[550147,823994]}
    ]
        for i in self.store_paths:
            if i['store'] == self.store_name:
                return i

if __name__=="__main__":
    i=stores('cvs')    
    items=i.scrape_items()
    print(items)
    