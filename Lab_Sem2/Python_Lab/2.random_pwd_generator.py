import random,string
letters=string.ascii_letters
digits=string.digits
spl_characters=string.punctuation
password=""
n=int(input("Enter the password limit:"))
for i in range(0,n):
    val=random.choice(letters+digits+spl_characters)
    password=password+val
print("Randomly generated password is:",password)

