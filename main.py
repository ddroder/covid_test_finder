import argparse

from src.store_details import stores

parser=argparse.ArgumentParser(description="Check stores for rapid covid antigen tests.")
parser.add_argument('--store',help='Name of the store to search. Walmart, CVS',required=True)
parser.add_argument('--zip',help='zip code to look at.',required=True,type=int)

if __name__=="__main__":
    args=parser.parse_args()
    # print(args.store)
    i=stores(store_name=args.store,zip=args.zip)    
    items=i.scrape_items()
    print(items)



