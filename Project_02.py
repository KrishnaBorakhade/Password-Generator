import random as r
import string
print('\t\t\t\t\t\t\t\t\t___________!!! Welcome Password Generator !!!___________')
letters = input('How many letters you want in your password ?\n')
letters_1 = string.ascii_letters
list_0 = []
for i in range(int(letters)):
    letters_11 = r.choice(letters_1)
    list_0.append(letters_11)
result = ''.join(list_0)
Symbols = input('Enter number of symbols you want in your password ?\n')
list_1 = []
symbols_list = ['!', '@', '#', '$', '%', '^', '&', '*']
for j in range(int(Symbols)):
    Symbols_1 = r.choice(symbols_list)
    list_1.append(Symbols_1)
result_1 = ''.join(list_1)
Num = input('Enter number of numbers you want in your password ?\n')
list_2 = []
for k in range(int(Num)):
    Num_1 = str(r.randint(0, 9))
    list_2.append(Num_1)
result_2 = ''.join(list_2)
result_3 = result+result_1+result_2
# print("Your required Passsword is : ",result_3)  #Without shufffle
passward = list(result_3)
r.shuffle(passward)   
password_1 = ''.join(passward)
print("Your required Passsword is : "+password_1)


