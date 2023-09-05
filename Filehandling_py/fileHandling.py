filename = str(input('enter the name of file with ext: '))
mode = str(input('enter the mode you want r = read w - write r+ - read and write: '))
with open(filename,mode) as file:
    print('data inside the the file')
    for line in file:
        print(line)

