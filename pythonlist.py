# find maximum and minimum value of a list

user_input = input("Enter the number by seperate by space :")
input_list= [int(num)for num in user_input.split()]
maximum = max(input_list)
minimum = min (input_list)
print(f"the maximum value is : {maximum}")
print(f"The minimum value is : {minimum}")

# sum of the list
user_input=input("enter the number by seperate by space :")
input_list = [int(num) for num in  user_input.split()]
sum = sum(input_list)
print(f"the sum value is : {sum}")

# list append a new list using input
user_input = input("Enter the numbers separated by space: ")
input_list = [int(num) for num in user_input.split()]

new_number = int(input("Enter one more number to add: "))
input_list.append(new_number)

print(f"The new list value is: {input_list}")

# two or more number ta be added
user_input =input("Enter the number seperate by space : ")
input_list = [int(num) for num in user_input.split()]
new_number = input("two or more number you can add :")
input_list.extend(int(num) for num in new_number.split())
print(f"the new list value is: {input_list}")

# remove the number of three digit of a list

numb_list=[1,2,3,4,5,6,7,8,9]
index = 0

while len(numb_list) > 0 :
     index = (index+2) % len(numb_list)
     remove=numb_list.pop(index)
     print(f"The removed number is : {remove}")
     print(f"The new list value is: {numb_list}")

# user input index delete
number = int(input("numbar :"))
number_list=list(range(1,10,number))
index = 0
while len(number_list) > 0 :
    index = (index+n-1) % len(number_list)
    remove=number_list.pop(index)
    print(f"The removed number is : {remove}")
    print(f"The new list value is: {number_list}")








