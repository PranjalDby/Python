from __future__ import print_function
from datetime import date
from email import encoders
import json
import os.path
import time
import requests
import base64
import google.auth
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from mimetypes import guess_type as guess_mime_type
from email.mime.text import MIMEText
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import zipfile
import tkinter
from tkinter.filedialog import askopenfiles
from tkinter.filedialog import askopenfilename
import asyncio
SCOPES = ['https://mail.google.com/']
our_email = 'pranjalorg11@gmail.com'
service = None
tk = tkinter.Tk()
tk.withdraw()

choose_secret = askopenfilename()

def gmail_auth():
    global service
    creds = None
    if os.path.exists('@hhsh22ss.json'):
        creds = Credentials.from_authorized_user_file('@hhsh22ss.json',SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(request=Request())
        else:
            if choose_secret != None:
                try:
                    flow = InstalledAppFlow.from_client_secrets_file(
                            choose_secret,
                            SCOPES
                        )
                    creds = flow.run_local_server(port=0)
                
                except Exception as e:
                    print("Some Error at line 46")
            
            else:
                print("No client_secret found...")

        with open('token.json','w') as token:
            token.write(creds.to_json())
    try:
         # calling the api
        service = build(
                'gmail',
                'v1',
                credentials=creds,
                cache_discovery=False,
            )
    except HttpError as e:
        print(e)

    return service

# request Authenticated id 
service = gmail_auth()


async def add_attachment(message,filename):
    if type(filename) is not type(list):
        print("File selected = ",filename)
        t1 = asyncio.create_task(file_attach_helper(message,filename))
        await asyncio.sleep(1)
    else:
        t2 = asyncio.create_task(file_attach_helper(message,filename))
        await asyncio.sleep(1.34)


async def file_attach_helper(message,filename):

    if type(filename) != type(list):
        task  = asyncio.create_task(message_attach_multiple(filename,message))
        await asyncio.sleep(0.982)
    else:
        for files in filename:
            task  = asyncio.create_task(message_attach_multiple(files,message))
            await asyncio.sleep(0.982)
    
    return

async def message_attach_multiple(filename,message):
    ext_file = {}
    extension_list = []
    count = -1
    _,extension = os.path.splitext(filename)
    if extension != None:
        extension_list.insert(count,extension)
        ext_file[extension_list[count]] = _
        task_type = asyncio.create_task(return_guessed_mime_type(filename))
        await asyncio.sleep(0.3)
        mt_,sub = task_type.result()
        print(f'''
                selected file is: ==========
                maint type ={mt_} sub = {sub}
                ''')
        with open(filename,"rb") as fp:
            part = MIMEBase(mt_,sub)
            part.set_payload(fp.read())
            part.add_header('Content-Disposition',"attachments; filename= %s" % os.path.basename(filename))
            encoders.encode_base64(part)
            message.attach(part)
    
async def return_guessed_mime_type(file_name):
    _mtype,sub = guess_mime_type(file_name,False)
    print(_mtype)
    print(sub)
    if(_mtype is not None and sub is None):
            mtype,sub = _mtype.split('/')
    else:
        f_name,ext = os.path.splitext(file_name)
        with zipfile.ZipFile(f_name+".zip",'w') as zips:
            zips.write(file_name,compress_type=zipfile.ZIP_DEFLATED)
            f_name = os.path.basename(zips.filename)
            print(f_name)
            mtype,sub = return_guessed_mime_type(f_name)


    return [mtype,sub]

async def create_body(body,destination,subject):
    attachment = str(input('Do you Want to Add Attachemnt: yes or no: ').lower())
    message = None
    if(attachment == 'yes'):
        print('Here an attachments...')
        message = MIMEMultipart()
        message['To'] = destination
        message['From'] = 'pranjalorg11@gmail.com'
        message['Subject'] = subject
        if int(input("want to select multiple files: 1 - YES: ")) == 1:
            files = askopenfiles('r')
            str1 = []
            for i in files:
                str1.append(i.name)
            for i in str1:
                task  = asyncio.create_task(add_attachment(message,str(i)))
                await asyncio.sleep(2)

        else:
            files  = askopenfilename()

    elif attachment == 'no':
        message = MIMEMultipart()
        message['To'] = destination
        message['From'] = 'pranjalorg11@gmail.com'
        message['Subject'] = subject
        message.attach(body)
    
    return {
         'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()
    }


async def send_email(des=None):
    if des == None:
        des = str(input('Enter the Destination: '))
    print("Message To :{}".format(des))
    mess = str(input('Enter the message: '))
    sub =str(input('Enter the Subject: '))
    if mess is not None and des is not None or sub is not None:
        res  = await create_body(mess,des,sub)
        try:
            return service.users().messages().send(
            userId='me',
            body = res
            ).execute()
        
        except TimeoutError as e:
            print("Timeout...")
    else:
        raise HttpError
    
email_liss = ["dpranjal.088@gmail.com","pranjalkdubey@outlook.com"]
def send_to_multiple():
    global email_liss
    files = askopenfilename()
    with open(files,'r') as file:
        for lines in file.readlines():
            email_liss.append(lines)

async def main():
    try:
        opt1 = int(input(
    '''\bEnter the options Showed Belowed:
        1> Send to multiple user
        2> Send to single user\n
        '''))
        print(opt1)
        if opt1 == 1:
            if email_liss is not None:
                for i in email_liss:
                    task1 = asyncio.create_task(send_email(i))
                    await asyncio.sleep(0.88)
                
                print("😊 send Successfully....................")
            return
        else:
            await send_email()
    except HttpError as e:
        print("Http Error at line 206")
    except requests.exceptions.JSONDecodeError as e2:
        print("Json File or Something..")

    else:
        print("😊 send Successfully....................")

if __name__ == "__main__":
    cr = asyncio.run(main=main())
