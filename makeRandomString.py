import random, string

balancedAlph = ['e']*21912+['t']*16587+['a']*14810+['o']*14003+['i']*13318+['n']*12666+['s']*11450+['r']*10977+['h']*10795+['d']*7874+['l']*7253+['u']*5246+['c']*4943+['m']*4761+['f']*4200+['y']*3853+['w']*3819+['g']*3693+['p']*3316+['b']*2715+['v']*2019+['k']*1257+['x']*315+['q']*205+['j']*188+['z']*128

def letter():
    return(balancedAlph)

def makeRandomString(length):
    return ''.join(random.choice(string.ascii_lowercase +string.ascii_uppercase + ' '+' '+' ') for _ in range(length))

def makeRandomStringCapital(length):
    return ''.join(random.choice(string.ascii_uppercase + ' '+' '+' ') for _ in range(length))

def makeRandomStringLower(length):
    return ''.join(random.choice(balancedAlph) for _ in range(length))

def makeRandomTyson(length):
    return ''.join(random.choice('T'+'y'+'s'+'o'+'n'+' ') for _ in range(length))

##takes list and integer as arguments
def stringFrom(letters,length):
    return ''.join(random.choice(letters) for _ in range(length))

def thingsBeginToFallApart(spaces,length):
	return ''.join(makeRandomStringLower(random.randint(1,4)) + ' '*random.randint(1,spaces)for i in range(length))


###makes a random string with english letter frequencies and customisable frequency of spaces###
def makeRow(length, spaces):
	spaces = spaces*len(balancedAlph)
	a = ''.join(balancedAlph)
	return ''.join([random.choice(a+spaces*' ') for i in range(length)])


def makeParagraph(rows,rowLen):
	return '\n'.join([makeRow(rowLen,9) for i in range(rows)])

