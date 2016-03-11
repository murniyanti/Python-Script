import random
import copy

def StaticRepair(P):

	for k in range(len(P)):
		if P[k]>=len(P):
			P[k]=random.randrange(0, len(P))

	for k in range(len(P)):
		indexi=[y for y, x in enumerate(P) if x==k]

		if len(indexi)>1:
			for h in range(1, len(indexi)):
				i=0
				while i<len(P):
					if i not in P:
						P[indexi[h]]=i
						break
					i=i+1

	return P

def RandomRepair(P):

	for k in range(len(P)):
		if P[k]>=len(P):
			P[k]=None

	for k in range(len(P)):
		indexi=[y for y, x in enumerate(P) if x==k]
		if len(P)>1:
			for h in range(1, len(indexi)):
				P[indexi[h]]=None

	PossibleCity=[]

	i=0

	while i<len(P):
		if i not in P:
			PossibleCity.append(copy.deepcopy(i))
		i=i+1

	for k in range(len(P)):
		if P[k]==None:
			P[k]=copy.deepcopy(random.choice(PossibleCity))
			PossibleCity.remove(P[k])

	return P