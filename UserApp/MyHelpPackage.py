import smtplib
from smtplib import SMTPException
from email.mime.text import MIMEText
import secrets
import string
# from .models import EmailVerifyCodes
import hashlib
import socket
import httpagentparser
import re, uuid
import os, sys
from getmac import get_mac_address
from forex_python.bitcoin import BtcConverter
from coinmarketcap import Market
import urllib, json
import requests as r
from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def SendMail(toaddr, message):
    fromaddr = "arcturuscoin@gmail.com"
    password = "arc@2019"
    toaddr = toaddr
    subject = 'Arcturus'
    print("*"*60)
    print("Hi i am from mailsend ",message)
    message = 'Subject: {}\n\n{}'.format(subject, message)
    # msg = MIMEText(u'message', 'html')
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  ## smtp.mail.yahoo.com
        server.starttls()
        server.ehlo()
        server.login(fromaddr, password)
        server.sendmail(fromaddr, toaddr, message)
        server.quit()

    except SMTPException:
        print("Mail id is Invalid !!")
        
    # try:
    #     s = smtplib.SMTP('smtp.gmail.com', 587) 
    #     s.starttls() 
    #     s.login("arcturuscoin@gmail.com", "arc@2019")  
    #     s.sendmail("arcturuscoin@gmail.com", toaddr, message) 
    #     s.quit()
    # except Exception as e:
    #     print("HI I AM FROM MAIL SEND ",e)



def SendMailWithSubject(toaddr, subject, message):
    fromaddr = "arcturuscoin@gmail.com"
    password = "arc@2019"
    toaddr = toaddr
    subject = subject
    message = 'Subject: {}\n\n{}'.format(subject, message)
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  ## smtp.mail.yahoo.com
        server.starttls()
        server.ehlo()
        server.login(fromaddr, password)
        server.sendmail(fromaddr, toaddr, message)
        server.quit()
        return True
    except SMTPException:
        print("Mail id is Invalid !!")
        return False


def Number_Generator():
    letters = string.ascii_letters + string.digits + string.hexdigits
    l = [secrets.choice(letters) for i in range(10)]
    num = ''
    for i in l:
        num = num + i

    return num


def GenerateOnlyNumber():
    letters = string.digits + string.digits + string.digits + string.digits + string.digits + string.digits
    l = [secrets.choice(letters) for i in range(10)]
    num = ''
    for i in l:
        num = num + i

    return num


def Big_Number_Generator():
    letters = string.ascii_letters + string.digits + string.hexdigits
    l = [secrets.choice(letters) for i in range(20)]
    num = ''
    for i in l:
        num = num + i

    return num


def HideMyData(data):
    result = ''
    result = hashlib.sha256(data.encode())
    return result.hexdigest()


def GetHostNamePC():
    hostname = ''
    hostname = socket.gethostname()
    return hostname


def GetIPLocationPC(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def GetMacAddress(request):
    ip = GetIPLocationPC(request)
    mac_address = get_mac_address(ip=ip)
    return mac_address
    # mac_address = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
    # mac_address = mac_address.upper()
    # return mac_address


def DetectBrowser(request):
    agent = request.environ.get('HTTP_USER_AGENT')
    browser = httpagentparser.detect(agent)
    if not browser:
        browser = agent.split('/')[0]
    else:
        browser_name = browser['browser']['name'] 
        browser_version = browser['browser']['version']
        browser = browser_name + " " + browser_version

    return browser


def arcturus_cal(money,arcturus_rate,c_type,bonus=0):
    c = CurrencyRates()
    b = BtcConverter()
    print(c_type)
    if c_type=="USD":
        if int(money)>=100:
            usd=float(money)
            no_of_btc=b.convert_to_btc(usd,'USD')
            return {"no_of_arcturus":float(usd)/float(arcturus_rate)}
        else:
            return {"no_of_arcturus":"Error... Minimum transaction should be more then 100 usd"}
    elif c_type.upper()=="BTC":
        usd=b.convert_btc_to_cur(float(money), 'USD')
        if int(usd)>=100:
            usd=float(usd)
            return {"no_of_arcturus":float(usd)/float(arcturus_rate)}
        else:
            return {"no_of_arcturus":"Minimum transaction should be more then 100 usd"}
    else:
        return {"no_of_arcturus":"Usupported cryptotype.... "}



def price():
    b = BtcConverter()
    bitcoin_price=b.get_latest_price('USD')
    coinmarketcap = Market()
    y=coinmarketcap.ticker(start=0, limit=2, convert='USD')
    return {"btc":bitcoin_price,"eth":y["data"]["1027"]["quotes"]['USD']['price']}

