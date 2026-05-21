s = "a,z,y,x,y,y,z,a,a,a,a"
q = ["d","a","y","x"]
hash_list = {}

for ch in s.split(','):
    ascii_value = ord(ch)
    index = ascii_value - 97
    hash_list[index] = hash_list.get(index, 0) + 1

for ch in q:
    ascii_value = ord(ch)
    index = ascii_value - 97
    print(hash_list.get(index, 0))