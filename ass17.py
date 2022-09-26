
def coat(a):
    print(a.replace('&#39;' , "'"))


'''1.Assign the value 7 to the variable guess_me. Then, write the conditional tests (if, else, and elif) to
print the string 'too low' if guess_me is less than 7, 'too high' if greater than 7, and 'just right' if equal
to 7.'''
#Ans
guess_me = 7
if guess_me < 7:
    print('too low')
elif guess_me == 7:
    print('just right')
else:
    print('too high')


''' (2) Assign the value 7 to the variable guess_me and the value 1 to the variable start. Write a while
loop that compares start with guess_me. Print too low if start is less than guess me. If start equals
guess_me, print 'found it!' and exit the loop. If start is greater than guess_me, print 'oops' and exit
the loop. Increment start at the end of the loop.'''
#Ans.
guess_me = 7
start = 1

while True:

    if start < guess_me:
        print('low')
    elif start == guess_me:
        print('found it!')
        break
    else:
        print('oops')
        break
    start = start + 1

'''3. Print the following values of the list [3, 2, 1, 0] using a for loop.'''
#Ans.
for i in  range (0,4):
    print(i)

print("....................")

'''4. Use a list comprehension to make a list of the even numbers in range(10)'''
#Ans.
for i in range (10):
    if i % 2 == 0 :
        print(i)

'''5.Use a dictionary comprehension to create the dictionary squares. Use range(10) to return the
keys, and use the square of each key as its value.'''
#Ans.
squares = {num : num * num for num in range(10)}
print(squares)

'''6. Construct the set odd from the odd numbers in the range using a set comprehension (10).'''
#Ans:
odd = {num for num in range(10) if num % 2 == 1}
print(odd)

'''7. Use a generator comprehension to return the string 'Got ' and a number for the numbers in
range(10). Iterate through this by using a for loop.'''
#Ans.
string_generator = ('Got ' + str(num) for num in range(10))
for item in string_generator:
    print(item)

'''8. Define a function called good that returns the list ['Harry', 'Ron', 'Hermione'].'''
#Ans.
def good():
    print(['Harry', 'Ron', 'Hermione'])
good()

'''9. Define a generator function called get_odds that returns the odd numbers from range(10). Use a
for loop to find and print the third value returned.'''
#Ans.
get_odds = (num for num in range(10) if num % 2 != 0)
count = 0
for num in get_odds:
    if count == 2:
        print(num)
        break
    count += 1


'''10. Define an exception called OopsException. Raise this exception to see what happens. Then write
the code to catch this exception and print 'caught an oops.'''
#Ans.
a = 1
b = 0
try:
    print(a / b)
except Exception as OopsException:
    print ('Caught an oops')

'''11.Use zip() to make a dictionary called movies that pairs these lists: titles = ['Creature of Habit',
'Crewel Fate'] and plots = ['A nun turns into a monster', 'A haunted yarn shop'].'''
#Ans :
list1  = ("titles", "plots")
list2 = (['Creature of Habit','Crewel Fate'],['A nun turns into a monster', 'A haunted yarn shop'])
ziped_dict = dict(zip(list1,list2))
print(ziped_dict)