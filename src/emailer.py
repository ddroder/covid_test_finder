try:
    from src.store_details import stores
except:
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
    def send_mail(self):
        self._send_email()

    def _format_msg(self,person):
        """
        does all of the scraping based on things 
        found in json file. Then converts all DF's
        into HTML-ified single DF and attachs that to
        the message.
        """
        user_email,user_store,user_zip=person[0],person[1],person[2]
        scraping=stores(user_store,zip=user_zip)
        info=scraping.scrape_items()
        html_df=pd.concat(scraping.scrape_items()).to_html()
        msg=MIMEMultipart("alternative")
        msg['Subject']="Covid Scraping Results"
        msg['From']=self.creds['personal-email']
        msg['To']=user_email
        mime_msg=MIMEText(html_df,'html')
        msg.attach(mime_msg)
        return msg

        
    def _send_email(self):
        """
        initalizes SMTP server through gmail on port 587.
        Then sends HTML-ified version of scraped data through email
        given from json file to recipients listed in json file.
        """
        sender_addy=self.creds['personal-email']
        mailing_list=self.creds['mailing-list-info']
        sender_pass=self.creds['personal-password']
        serv=smtplib.SMTP("smtp.gmail.com",587)
        serv.starttls()
        serv.login(sender_addy,sender_pass)
        for person in mailing_list:
            msg=self._format_msg(person)
            serv.sendmail(sender_addy,person[0],msg.as_string())
        serv.quit()


    def _read_json(self,path):
        """
        helper function to read in json data
        """
        f=open(path)
        file=json.load(f)
        return file


if __name__=="__main__":
    pass