length=int(input("enter the length of the rectangle "))
breadth=int(input("enter the height of the product "))

def get_area(length,breadth):
    area=length*breadth
    return area

def get_perimeter(lenght,breadth):
    perimiter=(length*2)+(breadth*2)
    return perimiter

area=get_area(length,breadth)
print(area)
perimiter=get_perimeter(length,breadth)
print(perimiter)

income=int(input("what is your monthly income"))
expense=int(input("what is your monthly expense"))

def get_balance(income,expense):
    balance=income-expense
    return balance

balance=get_balance(income,expense)
print("your remaining balance is:",balance)




