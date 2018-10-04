str1=raw_input("enter str1\n")
str2=raw_input("enter str2\n")
if(len(str1)==len(str2)):
	print hex(int(str1,16) ^ int(str2,16))
