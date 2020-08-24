with open('output.txt', 'r') as f:
    txt = f.read().splitlines()

str_len = len(txt[0])

res = ''
for i in range(str_len):
    amount_zero = 0
    amount_one = 0
    for j in range(len(txt)):
        if txt[j][i] == '1':
            amount_one += 1
        else:
            amount_zero += 1
    if amount_zero > amount_one:
        res += '1'
    else:
        res += '0'
print(bytes.fromhex(hex(int(res, 2))[2:]).decode())