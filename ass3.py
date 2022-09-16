'''
1.Why are functions advantageous to have in your programs?
Ans.Advantages of using functions
- it enhances of your code clarity
- we can reuse of code
- we can make complex problems into simpler by using fuctions

2.When does the code in a function run: when it is specified or when it is called?
Ans.A Function runs when it is referenced.
- We define a function with the def keyword,
 then write the function identifier (name) followed by parentheses and a colon.
-To call a function we simply type the function name with appropriate parameters.

3.What statement creates a function?
- def

4.What is the difference between a function and a function call?
Ans. To define a function use def keyword and To call a function we simply type
the function name with appropriate parameters.

5.How many global scopes are there in a Python program? How many local scopes?
Ans.-There's only one global Python scope
 its names are forgotten.
Variables that are defined inside a function body have a local scope,
and those defined outside have a global scope.

6.What happens to variables in a local scope when the function call returns?
Ans.When the execution of the function terminates (returns), the local variables are destroyed.

7.What is the concept of a return value? Is it possible to have a return value in an expression?
Ans.In general, a function takes arguments and then performs some operations and returns a value or object.
 The value that a function returns to the caller is generally known as the function's return value.
-A Python function will always have a return value.

8.If a function does not have a return statement, what is the return value of a call to that function?
Ans. None

9.How do you make a function variable refer to the global variable?
Ans. To create a global variable inside a function, you can use the global keyword.
       exp.
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)

10.What is the data type of None?
Ans.None is a data type of its own (NoneType) and only None can be None.

11.What does the sentence import areallyourpetsnamederic do?
Ans.That import statement imports a module named areallyourpetsnamederic.

12.If you had a bacon() feature in a spam module, what would you call it after importing spam?
Ans.This function can be called with spam. bacon().

13.What can you do to save a programme from crashing if it encounters an error?
Ans.Try running the program and it should throw an error message instead of crashing the program. The reason for the exception is also returned as an exception message.
 In the above code, we have handled the file reading inside an IOError exception handler

14.What is the purpose of the try clause? What is the purpose of the except clause?
Ans.In the try clause, all statements are executed until an exception is encountered.
 except is used to catch and handle the exception that are encountered in the try clause.
 else lets you code sections that should run only when no exceptions are encountered in the try clause.

'''