
def coat(a):
    print(a.replace('&#39;' , "'"))

'''1. Add the current date to the text file today.txt as a string.'''
#Ans:
import datetime
file = open('today.txt','w')
data = str(datetime.date.today())
file.write(data)
file.close()

'''Read the text file today.txt into the string today_string'''
#Ans:
file2 = open('today.txt','r')
today_string = file2.read()
print(today_string)
file2.close()

'''Parse the date from today_string.'''
#Ans:
a = today_string.split("-")
print(a[2])

'''4. List the files in your current directory'''
'''5. Create a list of all of the files in your parent directory (minimum five files should be available).'''
#Ans of Q no.4 and 5
import os

path = "C:\\Users\\Admin\\PycharmProjects\\ass21"
dir_list = os.listdir(path)

print("Files and directories in '", path, "' :")

print(dir_list)

'''6.Use multiprocessing to create three separate processes. Make each one wait a random number of
seconds between one and five, print the current time, and then exit.'''
#Ans:
import multiprocessing

def printsec(seconds):
    from datetime import datetime
    from time import sleep
    sleep(seconds)
    print('wait', seconds, 'seconds, time is', datetime.utcnow())


if __name__ == '__main__':
    import random

    for n in range(3):
        seconds = random.random()
        proc = multiprocessing.Process(target=printsec, args=(seconds,))
        proc.start()

'''7. Create a date object of your day of birth.'''
from datetime import datetime
from datetime import date
my_dob = date(1995,4,26)
print(my_dob)

'''8. What day of the week was your day of birth?'''
print(my_dob.weekday())

'''9. When will you be (or when were you) 10,000 days old?'''
#Ans:
from datetime import timedelta
old = my_dob + timedelta(days=10000)
print(old)