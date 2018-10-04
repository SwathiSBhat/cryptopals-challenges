
def hex_to_b64(s):
    if len(s)%2 == 1:
        s = s.zfill(len(s)+1)
    encoded=s.decode('hex').encode('base64')
    return encoded


if __name__ == "__main__":
    string=raw_input("Enter hex string: ")
    """
    Since everything is represented in bytes
    it requires 2 hexadecimal digits
    Hence it string is of odd length, gives an error
    """
    print hex_to_b64(string)
