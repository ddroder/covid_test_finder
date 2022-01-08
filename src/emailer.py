from store_details import stores
from functools import reduce
import pandas as pd
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
class emailer:
    #emailer? i hardly know her!
    def __init__(self,path_to_creds) -> None:
        self.path=path_to_creds
        self.creds=self._read_json(self.path)

    def _format_msg(self,person):
        user_email,user_store,user_zip=person[0],person[1],person[2]
        scraping=stores(user_store,zip=user_zip)
        info=scraping.scrape_items()
        # dfs=reduce(lambda x,y:pd.merge(x,y),info)
        print(info)

        # scraping=stores(self.creds['store'],zip=self.creds['zip']))
        
    def _send_email(self):
        sender_addy=self.creds['personal-email']
        mailing_list=self.creds['mailing-list-info']
        # store=self.creds['store']
        sender_pass=self.creds['personal-password']
        for person in mailing_list:
            msg=self._format_msg(person)


    def _read_json(self,path):
        f=open(path)
        file=json.load(f)
        return file


if __name__=="__main__":
    email=emailer("/home/danieldroder/Coding/covid_test_finder/real.json")
    print(email.creds)
    email._send_email()