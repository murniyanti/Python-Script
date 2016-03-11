import swalign
import re
from sys import argv

#How to use: python FtoM.py ExampleFile.dat

# In swalign folder (once you install it), 
#class Alignment(object)
#__init__.py, 
#def dump() : write return self.score  in the end of the def


script, filename = argv

f = open(filename)

b = []

for line in f:
	if re.match('^>', line):
		b.append(next(f))
f.close()

#MANIPULATED VARIABLE, CAN CHANGE TO YOUR PREFERENCES
match = 1
mismatch = -3
gap = -1


fw = open('Matrix_swalign_{0}_match={1}_mismatch={2}.txt'.format(filename, match, mismatch), 'w+')

scoring = swalign.NucleotideScoringMatrix(match, mismatch)
sw = swalign.LocalAlignment(scoring)

for i in range(len(b)):
	for j in range(len(b)):
		if i==j:
			print >> fw, "0,",
		else:
			scoring = swalign.NucleotideScoringMatrix(match, mismatch)
			sw = swalign.LocalAlignment(scoring, gap)	#CAN ADD MORE VARIABLE. REFER SWALIGN FILES
			a = sw.align(b[i], b[j])
			s = a.dump()
			print >> fw, "{0},".format(s),
	print >> fw, "\n",

fw.close()