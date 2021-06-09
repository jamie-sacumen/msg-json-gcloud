#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/2/29/029 22:03
# @Author : H
# @File : getEmailHeader.py

import os
import re
from email.parser import Parser

def read_mail(path):
    if os.path.exists(path):
        with open(path) as fp:
            email=fp.read()
            return email
    else:
        print ("file not exist!")

def emailInfo(emailpath):
    raw_email = read_mail(emailpath)  #Read the email into a string
    emailcontent = Parser().parsestr(raw_email)	#Generate a dictionary after parsestr processing
    # for k,v in emailcontent.items():
    #     print(k,v)
    From = emailcontent['From']
    To = emailcontent['To']
    Subject = emailcontent['Subject']
    Date = emailcontent['Date']
    MessageID = emailcontent['Message-ID']
    XOriginatingIP = emailcontent['X-Originating-IP']
    if "<" in From:
        From = re.findall(".*<(.*)>.*", From)[0]
    if "<" in To:
        To = re.findall(".*<(.*)>.*", To)[0]

    print("From:\t", From)
    print("X-Originating-IP", XOriginatingIP)
    print("To:\t", To)
    print("Subject:\t", Subject)
    print("Message-ID:\t", MessageID)
    print("Date:\t", Date)


    # Circulate each mime data block in the letter
    for par in emailcontent.walk():
        if not par.is_multipart(): # Here to determine whether it is a multipart, if so, the data inside is useless
            content = par.get_payload(decode=True)
            # print(str(content,"utf-8",errors='ignore'))
            print ("content:\t", content) # Decode the text content and output it directly.
            
if __name__ == '__main__':
    email = "testmail.eml"
    emailInfo(email)

