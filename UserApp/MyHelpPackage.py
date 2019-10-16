import smtplib
from smtplib import SMTPException
import secrets
import string
from .models import EmailVerifyCodes
import hashlib
import socket
import httpagentparser
import re, uuid
import os, sys
from getmac import get_mac_address


def SendMail(toaddr, message):
    fromaddr = "arcturuscoin@gmail.com"
    password = "arc@2019"
    toaddr = toaddr
    subject = 'Arcturus'
    message = 'Subject: {}\n\n{}'.format(subject, message)
    
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