
from time import sleep
from tqdm import tqdm
import pintut.Databases as Databases
import Game1
opt = int(input('1.for Delete or New Pin 2.for Sign_In 3.For exit '))
while(opt!=3):
    if(opt==1):
        newuser = (input('Are you newUSer?: '))
        if(newuser == 'True' or newuser == 'True'):
            userEntry= int(input('Enter The Pin:(4 Digits only): '))
            Databases.create_db(userEntry)
            print("Insertion Success. 3.exit 2.Continue: ")
            opt = int(input('Enter the Opt: '))
        else:
            pinEnter = int(input('Enter The Pin : '))
            Databases.DeletePin(pinEnter)
            print('Pin Removed..')
    elif(opt==2):
        pinEnter = int(input('Enter The Pin : '))
        for i in tqdm(range(100),desc='Processing...'):
                sleep(0.01)
        if Databases.checkpin(pinEnter):
                print('Correct.')
                Game1.start()
        else:
                print('Wrong Pin.')
    else:
        print('Wrong Opt..')
    
