# 1. Explain Exception handling? What is an error in Python.
# which disturb the normal flow of the program, exception which is handle by try and except block its called excception handling. 
# Errors can be defined as the problems that occur in program due to any illogical operation performed by user  or by fault of a programmmer.

# 2. How many except statements can a try-except block have? Name some bulit in exception classes.
# At least one  except statement.
# E.g:
"""
1. ValueError
2. ZeroDivisionError
3. KeyError
4. SyntaxError
5. IndexError
6. TypeError
"""
#  3. When will the else part of try-except-else be executed?
# The else part is executed when no exception occurs.
"""
try:
    exception block
except:
        after exception executable statement
else:   
        without execution

"""

# 4. Can one block of except statements handle multiple exception?
# Yes.

# 5. When is the finally block executed?
# Always.

#6. What happens when ,,1" == 1 is executed?
# It will evaluate false and does not raise any exception.

# 7. How do you handle Eexceptions with Try/Except/Finally/ in Python? Explain with coding snippets.

"""
try:
    exception block
except:
        after exception executable statement
else:   
        without execution
finally:
        it always occur
"""
# try:
#         # variable definition
#         a = 10
#         b = 20
#         ans = a + b
#         print(ans)

# except:
#         print("invalid input")
# else:
#         print("Welcome to math world")
# # it always execute exception occur or not

# finally:
#         print("Thank you for using this application")

# 8. Write a Python program that user to enter only odd numbers, else will raise an exception.


n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
ans = n1 + n2
print(ans)