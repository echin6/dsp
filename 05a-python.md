# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples are both sequence of values.  The values can be of any type and both are indexed by integers.  The important difference is that lists are mutable while tuples are immutable.  Tuples, not lists, will work as keys in dictionaries.  Keys need to be hashable and mutable types like lists cannot be keys.  If a key is modified then the mapping won't work because it would go to different location when hashed.  

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists are mutable ordered sequences of elements.  Sets are immutable unordered lists of unique elements.  For example, it might be better to use lists for tracking a list of email addresses while sets are preferred when tracking the set of words used in a document.  Python uses an algorithm called hashtable to implement sets and as a result the search time for sets is far superior to lists.  Hashtables do not require the elements to be ordered and can search at constant time regardless of the size of the dataset.  For lists the search time is proportional to the lists' length. 

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Python's 'lambda' is an anonymous function that can be defined without a name.  For example, here's a list of tuples:
>>
>>matrix = [(1, 5, 8), (3, 6, 7,), (5, 2, 9)]  
>>
>>If we want to sort this list we can use the build-in function 'sorted', which will sort the list by the first value of each tuple.  However, if we want to sort the list by its 2nd or 3rd value, we would need to use the 'key' argument and define a lambda function from within it.  A 'def' function could work as well but 'lambda' saves computational space.  The following demonstrates how to sort the list by its 3rd value using 'lambda':

>>sorted(matrix, key=lambda matrix: matrix[2])  
>>[(3, 6, 7), (1, 5, 8), (5, 2, 9)]

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions is a Python's construct that performs a transform operation on a list, with optional filters, which creates a new sequence (list) in the process.  List comprehension can be a complete substitute for list operators like map(), filter() and reduce(). Here are some examples that demonstrate equivalent results using list comprehensions versus list operators like 'map' and 'filter'.
>>
>>miles = [55, 65, 90]
>>km = [(x*1.60934) for x in miles]
>>print km
>>[88.5137, 104.6071, 144.8406]
---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





