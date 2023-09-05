# imutable ordered collection of element and itis barely mutable

mytuple = (1,2,3,4,5)
second_tuple = (7,8,9,10)
strin = ('geeek',)
for i in range(8):
    strin = (strin,);
print(strin)
print(mytuple.__len__())