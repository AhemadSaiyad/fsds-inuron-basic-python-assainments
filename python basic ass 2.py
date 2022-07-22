1.What are the two values of the Boolean data type? How do you write them?
ans : 1 true
      2 false
      To declare a Boolean variable we use the keyword "bool"
      using capital T and F, with the rest of the word in lowercase

2.What are the three different types of Boolean operators?
ans : 1.and  2.or 3.not

3.Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean
values for the operator and what it evaluate ).
ans : rue and True is True.
True and False is False.
False and True is False.
False and False is False.
True or True is True.
True or False is True.
False or True is True.
False or False is False.
not True is False.
not False is True.

4.What are the values of the following expressions?
ans :
(5 > 4) and (3 == 5)  = False
not (5 > 4) = False
(5 > 4) or (3 == 5) = True
not ((5 > 4) or (3 == 5)) = False
(True and True) and (True == False) = False
(not False) or (not True) = True

5.What are the six comparison operators?
ans : ==, !=, <, >, <=, and >=

6.What is the difference between the equal to operator and the assignment operator?
ans : "==" is the equal to operator that compares two values and evaluates to a Boolean,
and "=" is the assignment operator that stores a value in a variable.

7.Identify the three blocks in this code:
spam = 0
if spam == 10:
print('eggs')
if spam > 5:
print('bacon')
else:
print('ham')
print('spam')
print('spam')

ans :
print('eggs')

if spam > 5:
print('bacon')

else:
print('ham')
print('spam')

8.Write code that prints Hello if 1 is stored in spam,
prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam
ans :
if spam == 1:
    print('Hello')

elif spam == 2:
    print('Howdy')

else:
    print('Greetings!')