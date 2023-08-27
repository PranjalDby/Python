from __future__ import print_function
from email import encoders
import os.path
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
SCOPES = ['https://mail.google.com/']
our_email = 'pranjalorg11@gmail.com'
service = None
def gmail_auth():
    global service
    creds = None
    if os.path.exists('token1.json'):
        creds = Credentials.from_authorized_user_file('token1.json',SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(request=Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                    "gmailProject/client_secret.json",
                    SCOPES
                )
            creds = flow.run_local_server(port=0)

        with open('token.json','w') as token:
            token.write(creds.to_json())
    try:
         # calling the api
        service = build(
                'gmail',
                'v1',
                credentials=creds
            )
    except HttpError as e:
        print(e)

    return service

flag = 0
import requests
def return_guessed_mime_type(file_name):
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
def add_attachment(message,filename):
    ext_file = {}
    extension_list = []
    files_=[]
    count = -1
    size = len(filename)
    for ex in filename:
        _,extension = os.path.splitext(ex)
        if(count != size):
            count+=1
        extension_list.insert(count,extension)
        ext_file[extension_list[count]] = _

    else:    
        for i in filename:
            print(i)
            mt_,sub = return_guessed_mime_type(i)
            print(f'''
                  selected file is: ==========
                  maint type ={mt_} sub = {sub}
''')
            with open(i,"rb") as fp:
                part = MIMEBase(mt_,sub)
                part.set_payload(fp.read())
                part.add_header('Content-Disposition',"attachments; filename= %s" % os.path.basename(i))
                encoders.encode_base64(part)
                message.attach(part)

def create_body(body,destination,subject):
    attachment = str(input('Do you Want to Add Attachemnt: yes or no: ').lower())
    if(attachment == 'yes'):
        print('Here an attachments...')
        message =MIMEMultipart()
        message['To'] = destination
        message['From'] = 'pranjalorg11@gmail.com'
        message['Subject'] = subject
        # tks = tk.Tk()
        message.attach(MIMEText(body or '','html'))
        # file = askopenfilenames()
        files_list = []
        for i in file:
            files_list.append(i)
        add_attachment(message=message,filename=files_list)
    elif attachment == 'no':
        message = MIMEText(body)
        message['To'] = destination
        message['From'] = 'pranjalorg11@gmail.com'
        message['Subject'] = subject
    return {
         'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()
    }

def send_email():
    mess = str(input('Enter the message: '))
    des = str(input('Enter the Destination: '))
    sub =str(input('Enter the Subject: '))
    if mess is not None and des is not None or sub is not None:
        return service.users().messages().send(
          userId='me',
          body = create_body(mess,des,sub)
        ).execute()
    else:
        raise HttpError


def show_threads(service_auth):
    creds,_ = google.auth.default(scopes=SCOPES)
    try:
        service = service_auth
        threads = service.users().threads().list(userId='me').execute().get('threads',[])
        print(type(threads))
        for i in threads:
            tdata = service.users().threads().get(userId='me',id=threads['id']).execute()
            nmsgs = len(tdata['messages'])
            print(nmsgs)
            if nmsgs > 1:
                msg = tdata['messages'][0]['payloads']
                subject=''
                for header in msg['headers']:
                    if header['name'] == 'Subject':
                        subject = header['value']
                        break
                print(f'- {subject}, {nmsgs}')
                return threads
    except HttpError as e:
        print('Eroror',e)

service = gmail_auth()


def get_user_messages(service):
    try:
        threads = service.users().messages().list(userId='me').execute().get('messages',[])
        lists = []
        for i in threads:
            mess_obj = service.users().messages().get(userId='me',id=i['id']).execute()
            print(mess_obj)

            
    except HttpError as e:
        print(e)
try:
    opt1 = int(input(
'''\bEnter the options Showed Belowed:
    1> Send
    2> Show Thread
    3> get_user_message 
    :
    '''))
    print(opt1)
    if opt1 == 1:
        send_email()
    elif opt1 == 2:
        show_threads(service_auth=service)
    else:
        get_user_messages(service)

    resp = requests.get("https://mail.google.com/v1/users/'pranjalorg11@gmail.com'/messages/{'1897df511a4a938b'}")
    
except HttpError as e:
    print(e.error_details)
except requests.exceptions.JSONDecodeError as e2:
    print("Json File or Something..")
else:
    print("😊 send Successfully....................")


