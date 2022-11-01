from operator import le
from pydoc import cli
from time import sleep, time
from tqdm import tqdm
from ppadb.client import Client as Adbclient
client = Adbclient(host="127.0.0.1",port=5037)
try:
    device = client.devices()
    print("No of Devices:",len(device))
    print("Device Name is : ",client.BOOTLOADER)
    if(len(device)!=0):
        for i in tqdm(range(100),desc="Loading.."):
            sleep(0.01)
        dev = device[0]
        opt = 0
        while opt != -1:
            print('''
                3: home button
                4: back button
                5: call
                6: end call
                66: enter
                150 : input 
                24: volume up
                25: volume down
                26: turn device on or off
                27: open camera
                64: open browser
                277:cut
                -1:Exit
                ''')
            opt = int(input("Enter the opt:: "))
            if(opt == 3):
                dev.shell(f'input keyevent {opt}')
            elif(opt == 24):
                dev.shell(f'input keyevent {opt}')
            elif(opt == 26):
                dev.shell(f'input keyevent {opt}')
            elif(opt == 27):
                dev.shell(f'input keyevent {opt}')
            elif(opt == 64):
                dev.shell(f'input keyevent {opt}')
            elif(opt == 5):
                dev.shell(f'input keyevent {opt}')
            elif(opt == 66):
                dev.shell(f'input keyevent {opt}')
            elif(opt == 150):
                text = str(input("Enter The text: "))
                dev.shell(f'input text {text}')
            elif(opt == 277):
                dev.shell(f'input keyevent {opt}')
                
    else:
        print("No devices")
        quit()
except RuntimeError as e:
    print("Please Install Platform tools and Start Adb Server - Then Try Again")