import argparse

from src.store_details import stores

parser=argparse.ArgumentParser(description="Check stores for at home rapid covid antigen tests.")
parser.add_argument('-s','--store',help='Name of the store to search. Walmart, CVS',required=True)
parser.add_argument('-z','--zip',help='zip code to look at.',required=True,type=int)
parser.add_argument('-H','--headless',help="Boolean to run in headless mode or not.",required=False,default=0,type=bool)

if __name__=="__main__":
    args=parser.parse_args()
    i=stores(store_name=args.store,zip=args.zip,headless=args.headless)    
    items=i.scrape_items()



