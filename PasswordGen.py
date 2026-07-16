import random

print("Welcome in password generator program")
print("Fill the required details and have your password ready!!!")

letters= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols=['!','@','#','$','%','&','*','(',')','^']
digits= ['1','2','3','4','5','6','7','8','9','0']

my_letters= int(input("How many letters do you want in your password: "))
my_symbols= int(input("How many symbols do you want in your password: "))
my_digits= int(input("How many digits do you want in your password: "))

password= []

for i in range(my_letters):
    password.append(random.choice(letters))

for i in range(my_symbols):
    password.append(random.choice(symbols))

for i in range(my_digits):
    password.append(random.choice(digits))

random.shuffle(password)

passwordf=''

for i in password:
    passwordf+=i

print(f"The final password: {passwordf}")