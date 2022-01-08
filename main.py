import argparse

from src.store_details import stores
from src.emailer import emailer
parser=argparse.ArgumentParser(description="Check stores for at home rapid covid antigen tests.")
parser.add_argument('-s','--store',help='Name of the store to search. Walmart, CVS',)
parser.add_argument('-z','--zip',help='zip code to look at.',type=int)
parser.add_argument('-f','--file',help="Enables emailing. Reads in a json file of data about emailing. Format: {personal-email :'', personal-password:'',mailing-list-info:[['email1']]}")

if __name__=="__main__":
    args=parser.parse_args()
    if args.file is not None: #json filepath given.
        email=emailer(args.file)
        email.send_mail()
    else: #no email file given, will print to terminal
        i=stores(store_name=args.store,zip=args.zip)    
        items=i.scrape_items()
        for i in items:
            print(i)



