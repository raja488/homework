fruits = ["strawberry", "kiwi", "banana", "lemon", "watermelon", "tomato", "orange", "berrier", "plum", "blueberry"]


for fruit in fruits:
    print(f"Fruit: {fruit}")
    for letter in fruit:
        print(letter)

print(fruits.count(fruit))
print(len(fruits))