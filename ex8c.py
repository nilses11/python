import string


def getRule(alphabet, i, strls):
	l = []
	for x in range((strls-1)/2):
		l.append((i+1+x)%strls)
	return [alphabet[index] for index in l]


strls = input()
assert strls % 2 != 0

alphabet = list(string.ascii_lowercase)

rules = {}
for i in range(strls):
	rules[alphabet[i]] = getRule(alphabet, i, strls)

print rules


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

