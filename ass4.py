'''
1.What exactly is []?
Ans.[] called Index brackets or square brackets
-they are used to define "list literals"

2.In a list of values stored in a variable called spam, how would you assign the value 'hello' as the
third value? (Assume [2, 4, 6, 8, 10] are in spam.)
Ans.Spam[2] = 'hello'
the third value in a list is at index 2 because the first index is 0.

Let&#39;s pretend the spam includes the list ['a', 'b', 'c', 'd'] for the next three queries.

3.What is the value of spam[int(int('3' * 2) / 11)]?
Ans. 'd'

4.What is the value of spam[-1]?
Ans.'d'

5.What is the value of spam[:2]?
Ans.['a', 'b']

For the following three questions, let's say bacon contains the list [3.14, 'cat', 11, 'cat', True].

6.What is the value of bacon.index(cat)?
Ans. 1

7.How does bacon.append(99) change the look of the list value in bacon?
Ans.[3.14, 'cat', 11, 'cat', True, 99]

8.How does bacon.remove(cat) change the look of the list in bacon?
Ans.[3.14, 11, 'cat', True]

9.What are the list concatenation and list replication operators?
Ans.The operator for list concatenation is +, while the operator for replication is *.

10.What is difference between the list methods append() and insert()?
Ans.Append() function allow  add the element only at end of the list.
where insert function allows us to add a specific element at a specified index of the list.

11.What are the two methods for removing items from a list?
Ans. 1) remove()
     2) pop()

12.Describe how list values and string values are identical.
Ans. a list is an ordered sequence of object types and a string is an ordered sequence of characters.
 generally list eliment in [] and string in ' or '' .

13.What is the difference between tuples and lists?
Ans.List is mutable and consumes more memory and its iteration is slower and is time consuming,
 where Tuple is immutable, consumes less memory and its iteration is faster.
 generally list in [] and tupels in ()

14.How do you type a tuple value that only contains the integer 42?
Ans.(42,)

15.How do you get a list value's tuple form? How do you get a tuple value's list form?
Ans.We can use the list() function to convert tuple to list and tuple() for convert list in to tuple.

16.Variables that "contain" list values are not necessarily lists themselves. Instead, what do they
contain?
Ans.They contain references to list values.

17.How do you distinguish between copy.copy() and copy.deepcopy()?
Ans.The copy.copy() function will do a shallow copy of a list,
 while the copy.deepcopy() function will do a deep copy of a list.
 That is, only copy.deepcopy() will duplicate any lists inside the list.

'''