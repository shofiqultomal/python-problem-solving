user_input=input("enter the numbr seperated by space")
input_set=set(user_input.split())
print(input_set)



user_input1= input("List 1 : ")
input_set1= set(user_input1.split())
user_input2= input("List 2 : ")
input_set2= set(user_input2.split())

common = set(user_input1) & set(  user_input2)
print(common)
# 2rd highet number
numbers=input("Enter the number is : ")
input_num=[int(num)for num in numbers.split()]
unique_numbers=list(set(input_num))
if len(unique_numbers)<2:
    print("There is no 2rd higest number in here .")
else:
    unique_numbers.sort(reverse=True)
    print("The 2rd higest number is: {}".format(unique_numbers[1]))



#Assending order

# dublicate number

numbers= input("Enter the number is : ")
input_num= [int(num)for num in numbers.split()]
unique_numbers=list(set(input_num))
if len(unique_numbers)<2:
    print("There is no unique number is here .")
else:
    unique_numbers.sort()
    print(f"the num is : {unique_numbers}")

    print(f"total number is assending order :{len(unique_numbers)}")


