# Please write a program which asks the user for a positive integer N. 
# The program then prints out all numbers between -N and N inclusive, 
# but leaves out the number 0. Each number should be printed on a separate line.

# An example of expected behaviour:

# Sample output
# Please type in a positive integer: 4
# -4
# -3
# -2
# -1
# 1
# 2
# 3
# 4

# NB: this exercise doesn't ask you to write any functions, so you should not 
# place any code within an if __name__ == "__main__" block.

# Write your solution here
entero=int(input("Please type in a positive integer: "))
for numero in range(-1 * entero,entero + 1,1):
    if numero!=0:
        print(numero)