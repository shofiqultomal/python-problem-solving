people = input("Enter the people in cycle :")
cycle = people.split()
n=int(input("Enter the number of people :"))
index = 0
while len(cycle)>1 :
    index = (index+n-1) % len(cycle)
    remove=cycle.pop(index)
    print(f"The removed  : {remove}")


print(f"The last number people name is : {cycle[0]}")



