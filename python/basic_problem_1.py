'''
Write a function that takes a list of integers and returns the sum of all even numbers in the list.
def sum_even(numbers):
    # Your code here
    pass

print(sum_even([1, 2, 3, 4, 5, 6]))  # Output: 12
'''

'''
okay there is a function to find the sunm of even numbers only
psudocode:
-write a even odd check
-write the sum check
-return the sum
take a input'''

#checking odd even
def odd_even(x):
    if x% 2==0:
        return 0
    else:
        return 1

#the sum
def add(num):
    sum=0
    for i in num:
        #z storing the return value
        z=odd_even(i)
        if z==0:
            sum+=i
        else :
            continue
    return sum 

x=[]
#taking input
count=int(input("Enter how many items are there in tthe list"))
for i in range(count):
    y=int(input("Enter the numbers in the list"))
    x.append(y)
    
print(x)
#printing sum
sums=add(x)
print("The sum is ",sums)