import Pmf

def PrintPmf(pmf):
    for value, prob in pmf.Items():
        print value, prob

"""
Write a function called ProbBigger that takes two Pmf objects 
and returns the probability that a value chosen at random from 
the first Pmf is greater than a value chosen from the second.
Hint: enumerate all pairs of values and their probabilities.

prob(val1 > val2) = p(v11 > v21) + p(v12 > v22) + ... + p(v1i > p2j)
				  = p(v11)p(v21) + p(v12)p(v22) + ... + p(v1i)p(v2i)
"""
def ProbBigger(pmf1, pmf2):
    total = 0;

    for v1, p1 in pmf1.Items():
    	for v2, p2 in pmf2.Items():
    		if(v1 > v2):
    			total += p1*p2

    return total

six_sided_die = Pmf.MakePmfFromList([1, 2, 3, 4, 5, 6])
ten_sided_die = Pmf.MakePmfFromList(range(1, 11))

for value, prob in ten_sided_die.Items():
	print value, '->', prob

print 'Prob ten sided die is bigger', ProbBigger(ten_sided_die, six_sided_die)

