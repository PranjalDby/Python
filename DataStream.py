import os


filename = str(input('Enter the File name: '))
# isexist = bool(input('This File Exist or not.'))
currdir = os.curdir
print(currdir)
isexist = False
try:
    for i in os.listdir(currdir):
        if(i==filename):
            isexist = True
    if(not isexist):
        print('File Not Found Creating new File.')
        inptstream = open(filename,'x');
        data = str(input('enter the data that you want to write: '))
        if(inptstream.write(data)):
            print('Writing Data Succesfully.')
        else:
            print('Unsuccesful..')
    else:
        print('File Found At \t ' + currdir.__repr__())
        inptstream = open(filename,'a')
        data = str(input('enter the data that you want to write: '))
        if(inptstream.write(data)):
            print('Writing Data Succesfully.')
        else:
            print('Unsuccesful..')
except:
    print('FIle Not Found')
