from email.mime import image
from PIL import Image
file = str(input("Enter the File Name: "))
print(file.endswith(".png"))
if(file.endswith(".png")):
    img = Image.open(file)
    img.show("Image")
else:
    path = open(file,'r')
    for i in path:
        print(f'{i}\t')
    path.close() 