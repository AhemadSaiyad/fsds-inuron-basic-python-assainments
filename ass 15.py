'''
1.How many seconds are in an hour? Use the interactive interpreter as a calculator and multiply the
number of seconds in a minute (60) by the number of minutes in an hour (also 60).
Ans. 60 * 60

2.Assign the result from the previous task (seconds in an hour) to a variable called
seconds_per_hour.
Ans.seconds per hour = 3600

3.How many seconds do you think there are in a day? Make use of the variables seconds per hour
and minutes per hour.
Ans.seconds per hour * 24

4.Calculate seconds per day again, but this time save the result in a variable called seconds_per_day
Ans.seconds_per_day = seconds per hour * 24

5.Divide seconds_per_day by seconds_per_hour. Use floating-point (/) division.
Ans.seconds_per_day / seconds per hour

6.Divide seconds_per_day by seconds_per_hour, using integer (//) division. Did this number agree
with the floating-point value from the previous question, aside from the final .0?
Ans.yes,
seconds_per_day // seconds_per_hour

7.Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to
its next() method: 2, 3, 5, 7, 11, ...
Ans.
def gemPrime():
    primes = []
    last = 1
    while True:
        last = last + 1
        for x in primes:
            if last % x == 0:
                break
        else:
            primes.append(last)
            print(last)
'''