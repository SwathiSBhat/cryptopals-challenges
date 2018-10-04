def xor(s,k):
    xorstr=""
    for i in range(0,len(s)):
        xorstr=xorstr+chr(ord(s[i]) ^ ord(k[i]))
    xorstr=xorstr.encode('hex')
    return xorstr

def repeat(s):
    key=k
    c=keylen
    while c+keylen<=l:
        key+=k
        c+=keylen
    i=0
    c+=1
    while c<=l:
        key=key+key[i]
        i+=1
        c+=1
    return key

if __name__ == "__main__":
    #s=raw_input("Enter string\n")
    s="Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    l=len(s)
    print "String: ",s
    k=raw_input("Enter key\n")
    keylen=len(k)
    cipher= xor(s,repeat(s))
    expected = b'0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'
    print cipher
    #print expected
    if str(cipher)==str(expected):
        print "True!"
    else:
        print "false"


    
        
    
