
# assert : This function is used for debugging purposes. 
# Usually used to check the correctness of code. If a statement evaluated to true,
# nothing happens, but when it is false, “AssertionError” is raised. 

# break : “break” is used to control the flow of the loop.
# The statement is used to break out of the loop 
# and passes the control to the statement 
# following immediately after loop

# continue : “continue” is also used to control the flow of code.
# The keyword skips the current iteration of the loop, 
# but does not end the loop.
# class : This keyword is used to declare user defined classes

#  def : This keyword is used to declare user defined functions
# It is a control statement for decision making.
# Truth expression forces control to go in “if” statement block.

# else : It is a control statement for decision making. 
# False expression forces control to go in “else” statement block.
# elif : It is a control statement for decision making. It is short for “else if”
# del : del is used to delete a reference to an object. 
# Any variable or list value can be deleted using del.

a = [1,2,3]
print("the list before deleting any value")
print(a)

del a[1]

print("the list after deleting a value")
print(a)

assert 5 < 3, "5 is not smaller than 3"

