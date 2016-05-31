rules = {}

rules['stein'] = 'saks'
rules['saks'] = 'papir'
rules['papir'] = 'stein'


def getResult(s1, s2):
	if s1 == rules[s2]:
		return 'P2 wins!'
	elif s2 == rules[s1]:
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

