user_input=input("please enter a list")
user=user_input.split(",")
list_length=len(user)
print(list_length)

if len(user)>1:
    user[0],user[-1]=user[-1],user[0]
print("list after being swapping first and last character",user)