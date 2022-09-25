'''1. Create a list called years_list, starting with the year of your birth, and each year thereafter until
the year of your fifth birthday. For example, if you were born in 1980. the list would be years_list =
[1980, 1981, 1982, 1983, 1984, 1985].'''
#Ans.
import xml.sax.saxutils

years_list=[1995,1196,1997,1998,1999]

'''2.In which year in years_list was your third birthday? Remember, you were 0 years of age for your
first year.'''
#Ans :
print(years_list[2])

'''3.In the years list, which year were you the oldest?'''
#Ans.
print(years_list[-1])

'''4.Make a list called things with these three strings as elements: 'mozzarella' ,  'cinderella'
'salmonella')'''
#Ans :
things = ['mozzarella' ,  'cinderella', 'salmonella']
print(things)

'''5. Capitalize the element in things that refers to a person and then print the list. Did it change the
element in the list?'''
#Ans :
list = [x.upper()for x in things]
print(list)

'''6.Make a surprise list with the elements 'Groucho' 'Chico' and 'Harpo'. '''
#Ans:
surprise_list = ["Groucho", "Chico", "Harpo"]

'''7.Lowercase the last element of the surprise list, reverse it, and then capitalize it.'''
#Ans :
surprise_list1 = ["Groucho", "Chico", "HaRpo"]
print(surprise_list[2].lower()[::-1].capitalize())

'''8.Make an English-to-French dictionary called e2f and print it. Here are your starter words: dog is
chien, cat is chat, and walrus is morse.'''
#Ans :
e2f = {'dog' : 'chien','cat' : 'chat', 'walrus' : 'morse' }
print(e2f)

'''9.Write the French word for walrus in your three-word dictionary e2f.'''
#Ans:
print(e2f["walrus"])

'''10.Make a French-to-English dictionary called f2e from e2f. Use the items method.'''
#Ans
f2e = dict()
for key, value in e2f.items():
    f2e[value] = key
print(f2e)

'''11.Print the English version of the French word chien using f2e.'''
#Ans:
print(f2e["chien"])

'''12. Make and print a set of English words from the keys in e2f.'''
#Ans:
a = set(e2f.keys())
print(a)


'''13.Make a multilevel dictionary called life. Use these strings for the topmost keys: 'animals', 'plants',
and 'other'. Make the 'animals' key refer to another dictionary with the keys 'cats', 'octopi', and
'emus'. Make the 'cats' key refer to a list of strings with the values 'Henri', 'Grumpy', and 'Lucy'.
Make all the other keys refer to empty dictionaries.'''
#Ans :
life= {'animals' : { 'cats' : ["Henri",'Grumpy', 'Lucy' ] , 'octopi' : " ",'emus' : " " }
    , "plants" : " ", "others" : " "}

'''14.Print the top-level keys of life.'''
#Ans :
print(life.keys())

'''15. Print the keys for life['animals'].'''
#Ans:
print(life['animals'].keys())

'''16.Print the values for life['animals']['cats']'''
#Ans:
print(life['animals']['cats'])