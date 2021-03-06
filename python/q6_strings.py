# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    count_int = int(count)
        if count_int > 9:
	    print "Number of donuts: many"
	else:
	    print 'Number of donuts: %d' %count_int
	
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.

    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """
    raise NotImplementedError


def both_ends(s):
    s_len = len(s)
	if s_len < 2:
            print ""
	else:
	    print s[0:2] + s[s_len-2:s_len]
		
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    raise NotImplementedError


def fix_start(s):
    s_list = []
    s_list = list(s)
    for x in range(len(s_list)):
        if x == 0:
	    s_list[0] = s[0]
	elif s[x] == s[0]:
	    s_list[x] = "*"
	else:
	    s_list[x] = s[x]
    print ''.join(s_list)
	
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
    raise NotImplementedError


def mix_up(a, b):
    a_list = []
    b_list = []
    a_list = list(a)
    b_list = list(b)
    a_list[0] = b[0]
    a_list[1] = b[1]
    b_list[0] = a[0]
    b_list[1] = a[1]
    print "".join(a_list) + " " + "".join(b_list)
	
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    raise NotImplementedError


def verbing(s):
    s_len = len(s)
    if s_len < 3:
	pass
    elif s[s_len-3:s_len] == "ing":
        s = s + "ly"
    else:
	s = s + "ing"
    print s
	
	"""
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    raise NotImplementedError


def not_bad(s):
    t = []
    t = s.split()
        for i in range(len(t)):
            if t[i].find('not') >= 0:
                not_index = t.index(t[i])
            else:
                not_index = -1
        for i in range(len(t)):
            if t[i].find('bad') >= 0:
                bad_index = t.index(t[i])
            else:
                bad_index = -1
        if not_index >=0 and bad_index > not_index:
            t[bad_index] = t[bad_index].replace('bad', 'good')
            del t[not_index:bad_index]
            print " ".join(t)
        else:
            print " ".join(t)	
            
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """
    raise NotImplementedError


def front_back(a, b):
    a_len = len(a)
    b_len = len(b)
    if a_len % 2 == 0:
	a_front = a_len / 2
    else:
	a_front = a_len / 2 + 1 
    if b_len % 2 == 0:
	b_front = b_len / 2
    else:
	b_front = b_len / 2 + 1
    a_back = a_len / 2
    b_back = b_len / 2
    print a[0:a_front] + b[0:b_front] + a[a_front:a_front+a_back] + b[b_front:b_front+b_back]
	
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    raise NotImplementedError
