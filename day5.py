import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')','_']

print("Welcome to Password Generator")
l = int(input("Enter the number of letters in your password: "))
n = int(input("Enter the number of numbers in your password: "))
s = int(input("Enter the number of symbols in your password: "))

password = []
for i in range(1, l + 1):
    ltr = random.choice(letters)
    password.append(ltr)
        
for i in range(1, n + 1):
    num = random.choice(numbers)
    password.append(num)
    
for i in range(1, s + 1):
    sym = random.choice(symbols)
    password.append(sym)
    
print(password)

random.shuffle(password)

a = ''.join(password)
print(a)

