# Please write a program which asks the user to type in a number.
# The program then prints out all the positive integer values from 1 up to the number.
# However, the order of the numbers is changed so that each pair or numbers is flipped.
# That is, 2 comes before 1, 4 before 3 and so forth. See the examples below for details.
#
# Sample output
# Please type in a number: 5
# 2
# 1
# 4
# 3
# 5
#
# Sample output
# Please type in a number: 6
# 2
# 1
# 4
# 3
# 6
# 5
limit=int(input("Please type in a number: "))
num1=0
num2=0
counter=1
while counter<=limit:
    num1=counter
    if num1<limit:
        num2=counter+1
        print(num2)
        print(num1)
        counter = num2 + 1
    else:
        print(num1)
        counter +=1
