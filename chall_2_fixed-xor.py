from __future__ import print_function

def fixed_xor(s1, s2):
	if len(s1) == len(s2):
		return hex(int(s1, 16) ^ int(s2, 16))
	else:
		raise ValueError("Strings not of equal length!")

if __name__ == "__main__":
	str1=raw_input("enter hex str1\n")
	str2=raw_input("enter hex str2\n")
	print("Fixed xor of {} and {} = {}".format(str1,str2,fixed_xor(str1,str2)))
