# n = [5,3,2,2,1,5,5,7,5,10]
# m = [10,111,1,9,5,67,2]

# hash_list = [0]* 11
# for num in n:
#     hash_list[num] += 1
#     for num in m :
#         if num < 1 or num > 10:
#             print(0)
#         else:
#             print(hash_list[num])
# 
n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]   

freq_Dict = {}
for idx in n:
    if idx in freq_Dict:
        freq_Dict[idx] += 1
    else:
        freq_Dict[idx] = 1

for num in m:
    if num < 1 or num > 10:
        print(0)
    else:
        print(freq_Dict.get(num, 0))