'''
1.Is the Python Standard Library included with PyInputPlus?
Ans.PyInputPlus is not a part of the Python Standard Library, we have to install it separately using Pip

2.Why is PyInputPlus commonly imported with import pyinputplus as pypi?
Ans.pypi it just a shorter name of library.so that we can enter a shorter name when calling the module's functions

3.How do you distinguish between inputInt() and inputFloat()?
Ans.The inputInt() function returns an integer
    The inputFloat() function returns a float value.

4.Using PyInputPlus, how do you ensure that the user enters a whole number between 0 and 99?
Ans.pyip.inputInt(min = 0, max =99)

5.What is transferred to the keyword arguments allowRegexes and blockRegexes?
Ans.We can also use regular expressions to specify whether an input is allowed or not.
- The allowRegexes and blockRegexes keyword arguments take a list of regular expression strings to determine
what the PyInputPlus function will accept or reject as valid input.

6.If a blank input is entered three times, what does inputStr(limit=3) do?
Ans.it gives RetryLimitException exception.

7.If blank input is entered three times, what does inputStr(limit=3, default='hello') do?
Ans.The function returns the default value instead of raising an exception.





'''