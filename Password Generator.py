# TASK 3 PASSWORD GENERATOR
import random
print("PASSWORD GENERATOR")
array = ['!','$','%','*','&','#']                              # made an array including some random characters
num = int(input("Enter your desired length of password: "))    # to specify the desired length of the password
password = "".join(random.choices(array, k=num))
print("Password: ", end="")
for i in password:
    print(i, end="")
