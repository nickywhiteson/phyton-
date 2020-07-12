#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("Press q for quit.")
while True:
    number = input(
        "Please enter a number to check if it's an Armstrong Number : ").lower().strip()
    if number == "q":
        print("See you...")
        break
    len_num = len(number)
    list_num = list(number)
    armstrong = 0
    if number.isalpha():
        print("Do not use any entries other than numeric values")
    elif number.startswith("-"):
        a = list_num.remove[0]
        if a.isdigit():
            print("Please enter a positive number")
    elif ("." in list_num) or ("," in list_num):
        print("Please enter an integer number")
    else:
        for i in list_num:
            armstrong += int(i) ** len_num
        if int(number) == armstrong:
            print("{} is an Armstrong number".format(int(number)))
        else:
            print("{} is not an Armstrong number".format(int(number)))


# In[ ]:




