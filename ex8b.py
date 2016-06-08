rules = {}

#rules['a'] = ['b','c']
#rules['b'] = ['c','d']
#rules['c'] = ['d','e']
#rules['d'] = ['e','a']
#rules['e'] = ['a','b']


rules['a'] = ['b','c', 'd']
rules['b'] = ['c','d', 'e']
rules['c'] = ['d','e', 'f']
rules['d'] = ['e','f', 'g']
rules['e'] = ['f','g', 'a']
rules['f'] = ['g','a', 'b']
rules['g'] = ['a','b', 'c']




def getResult(s1, s2):
	if s1 in rules[s2]:
		return 'P2 wins!'
	elif s2 in rules[s1]:
		return 'P1 wins!'
	elif s1 == s2:
		return 'Draw!'
	else:
		return 'illegal value(s)?'

s1 = ''
while s1 != 'q':
	s1 = input("p1 chooses?")
	s2 = input("p2 chooses?")
	print getResult(s1, s2)

