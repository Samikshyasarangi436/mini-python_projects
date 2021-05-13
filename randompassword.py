#Topics:random module,joining strings,taking input

import random
password_length=int(input("Enter the desired length of your password:\n"))
string_characters="qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM!@#$%&*?"
password="".join(random.sample(string_characters,password_length))
print("\nYour generated password is:6",password)