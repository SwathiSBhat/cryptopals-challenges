from __future__ import print_function

def pkcs7(s,block_size):
    num_of_bytes = block_size - (len(s) % block_size)
    padding = chr(num_of_bytes)*num_of_bytes
    res = repr(s+padding)
    return res 


if __name__ == "__main__":
    block_size = int(raw_input("Enter block size: "))
    s = raw_input("Enter message: ")
    res = pkcs7(s,block_size)
    print("res: ",res)
