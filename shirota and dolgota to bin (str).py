s = input(Enter the shirota and dolgota: ")

def encode(s):
    return list(map(lambda x: "{0:b}".format(ord(x)).zfill(16), s))

def decode(lst):
    return ''.join(map(lambda x: chr(int(x,2)), lst))
    
    
print(encode(s))
