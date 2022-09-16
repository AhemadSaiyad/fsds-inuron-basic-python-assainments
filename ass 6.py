'''
1.What are escape characters, and how do you use them?
Ans.Escape characters represent characters in string values
that would otherwise be difficult or impossible to type into code.

2.What do the escape characters n and t stand for?
Ans.\n is a newline
    \t is a tab.

3.What is the way to include backslash characters in a string?
Ans.The \\ escape character will represent a backslash character.

4.The string "Howl's Moving Castle" is a correct value. Why isn't the single quote character in the
word Howl's not escaped a problem?
Ans.The single quote in Howl's is fine because you’ve used
double quotes to mark the beginning and end of the string.

5.How do you write a string of newlines if you don't want to use the n character?
Ans.Multiline strings allow you to use newlines in strings without the \n escape character.

6.What are the values of the given expressions?
Ans.
'Hello, world!'[1] = "e"
'Hello, world!'[0:5] = "Hello"
'Hello, world!'[:5] = "Hello"
'Hello, world!'[3:] = "lo, world!"

7.What are the values of the following expressions?
Ans.
'Hello.upper() = "HELLO"
'Hello.upper().isupper() = True
'Hello.upper().lower() = "hello"

8.What are the values of the following expressions?
Remember, remember, the fifth of July.split()
"-".join(There can only one.'.split())
Ans. 1. ['Remember,', 'remember,', 'the', 'fifth', 'of', 'July.']
     2.'There-can-be-only-one.'

9.  What are the methods for right-justifying, left-justifying, and centering a string?
Ans.The rjust(), ljust(), and center() string methods, respectively

10.What is the best way to remove whitespace characters from the start or end?
Ans. lstrip() and rstrip() methods





'''

print("Hello".upper().isupper())

