num  = 0
n = 0
while num<10:
    print("""""""""KKKK}#{KKKK"""""""""+"\t")
    num+=1
print("")     
while n<3:
    print("[[]].. <><>..")
    print(">>>>>>>>>>>>>>>>>"+"\t")
    n+=1
print("\n")
print('""""""""""""""""""""""')

secret_word = "Pranjal"
guess = ""
notime = 3
flag = 0
while(guess != secret_word):
    if(notime != 0):
        guess = input("Enter The Guess ")
        notime-=1
        if(flag==0):
            print("try left = ", notime)
        if guess == secret_word:
            flag = 1 
            print("Win")
    else:
        print("Loose")
        break