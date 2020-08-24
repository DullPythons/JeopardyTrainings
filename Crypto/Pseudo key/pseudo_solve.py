from string import ascii_lowercase

chr_to_num = {c: i for i, c in enumerate(ascii_lowercase)}
num_to_chr = {i: c for i, c in enumerate(ascii_lowercase)}

ctx = 'z_jjaoo_rljlhr_gauf_twv_shaqzb_ljtyut'
pseudo_key = 'iigesssaemk'

# find letters of original key
variants = {}

# 2x % 26 = a -> 2x = 26y + a
for letter in pseudo_key:
    variants[letter] = []
    for y in range(51):
        x = (26 * y + chr_to_num[letter])
        if x % 2 == 0 and x // 2 <= 25:
            variants[letter].append(num_to_chr[int(x//2)])

i = variants['i']
g = variants['g']
e = variants['e']
s = variants['s']
a = variants['a']
m = variants['m']
k = variants ['k']

keys = []

for letter_i in i:
    for letter_ii in i:
        for letter_g in g:
            for letter_e in e:
                for letter_s in s:
                    for letter_ss in s:
                        for letter_sss in s:
                            for letter_a in a:
                                for letter_ee in e:
                                    for letter_m in m:
                                        for letter_k in k:
                                            tmp = letter_i + letter_ii + letter_g + letter_e + letter_s + \
                                                  letter_ss + letter_sss + letter_a + letter_ee + letter_m + letter_k
                                            keys.append(tmp)

output = open('result.txt', 'w')
for key in keys:
    current_key = ''.join(key[i % len(key)] for i in range(len(ctx))).lower()
    ptx = ''
    for i in range(len(ctx)):
        if ctx[i] == '_':
            ptx += '_'
            continue
        c = chr_to_num[ctx[i]]  #ciph letter
        k = chr_to_num[current_key[i]] # key letter
        ptx += num_to_chr[(c+ 26- k) % 26]
    output.write(ptx+'\n')