
freq={}

freq[' ']=22
freq['e']=12.02
freq['t']=9.10
freq['a']=8.12
freq['o']=7.68
freq['i']=7.31
freq['n']=6.95
freq['s']=6.28
freq['h']=6.02
freq['r']=5.92
freq['d']=4.32
freq['l']=3.98
freq['u']=2.88
freq['c']=2.71
freq['m']=2.61
freq['f']=2.30
freq['y']=2.11
freq['w']=2.09
freq['g']=2.03
freq['p']=1.82
freq['b']=1.49
freq['v']=1.11
freq['k']=0.69
freq['x']=0.17
freq['q']=0.11
freq['j']=0.10
freq['z']=0.07

def scoring(s):
	score=0
	for i in s.lower():
		if i in freq:
			score+=freq[i]
	return score
		

def single_byte_xor(str1):
	maxi=0
	for i in range(0,256):
		s=xor(str1,i)
		if scoring(s) > maxi:
			maxi=scoring(s)
			t=s
                        char = chr(i)
	return char,t

def xor(s1,s2):
	return ''.join(chr(ord(c) ^ s2) for c in s1)

if __name__ == "__main__":
	
	# str1=raw_input(" Enter hex encoded str\n")
	
	"""with open("chall4-file.txt") as f:
		for line in f:
		line=line.decode('hex')
		print single_byte_xor(line),"\n"
	"""

	# str1=str1.decode('hex')
	# print single_byte_xor(str1),"\n"

	str1 = "TWWNPZOAASWNUHZBNWWGSNBVCSLYPMM"
	print single_byte_xor(str1)




