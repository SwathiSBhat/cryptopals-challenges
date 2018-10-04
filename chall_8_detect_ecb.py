
def detect_ecb(filename):
    aes_ecb_blocks = []
    with open(filename,"r") as f:
        count = 0 
        for line in f:
            count += 1
            seen = []
            a = [line[i:i+32] for i in range(0,len(line),32)]
            for x in a:
                if x not in seen:
                    seen.append(x)
                else:
                    aes_ecb_blocks.append(line)
    return aes_ecb_blocks 


if __name__ == "__main__":
    print detect_ecb("8.txt")
