fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    
numbers = [1,2,3,4,5,7]
for number in numbers:
    print(number)
    
#using a while loop to count from 1 to 5
count = 1
while count <= 5:
    print(count)
count += 1   # increase the count by 7

fruits = ["apple", "banana", "cherry"]

# This loop stops when it finds "cherry"
for fruit in fruits:
    if fruit == "cherry":
        break  # exits the loop if cherry is found
    print(fruit)
    
for fruit in fruits:
    if fruit == "cherry":
     continue # skips cherry and moves to he iteration
print(fruit)

