import string
import random

# all valid chars stored in lists
l1 = list(string.ascii_lowercase)
l2 = list(string.ascii_uppercase)
l3 = list(string.digits)
l4 = list(string.punctuation)

# input how many characters should the password be
num_chars = input("How many characters do you need? >")
num_chars = int(num_chars)
# shuffle the lists
random.shuffle(l1)
random.shuffle(l2)
random.shuffle(l3)
random.shuffle(l4)

# find the percentages for letters, symbols and numbers
letters = round(num_chars * (60/100))
symbols = round(num_chars * (20/100))
nums = round(num_chars * (20/100))

# generate a password that's 60% letters, 20% symbols and 20% numbers
result = []

for i in range(letters):
    result.append(l1[i])
    result.append(l2[i])

for i in range(symbols):
    result.append(l4[i])

for i in range(nums):
    result.append(l3[i])

# shuffle the password
random.shuffle(result)

# join and print the password
password = "".join(result)
print(password)
