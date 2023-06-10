# The Fibonacci sequence is a series of numbers in which each number is the 
# sum of the two preceding ones. It starts with 0 and 1, and each subsequent
# number is the sum of the two previous numbers. The sequence begins as follows:

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...


def fibonacci(n):
    fib_seq = [0, 1]  # Initialize the Fibonacci sequence with the first two numbers
    for i in range(2, n):
    	# apply the formular F(n) = F(n-1) + F(n-2)
        fib_seq.append(fib_seq[i-1] + fib_seq[i-2]) 
         # Calculate the next Fibonacci number ((2-1) + (2-2)), ((3-1) + (3-2))      																							#  after 0, 1, the next is 1,  
         # accessing the the index of first and second element
    return fib_seq

fib_numbers = fibonacci(50)  # Generate the first 50 Fibonacci numbers
fib_sum = sum(fib_numbers)  # Calculate the sum of the Fibonacci numbers

print("Sum of the first 50 Fibonacci numbers:", fib_sum)

