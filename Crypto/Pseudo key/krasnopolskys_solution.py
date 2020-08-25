#!/usr/bin/env python3

from string import ascii_lowercase


chr_to_num = {c: i for i, c in enumerate(ascii_lowercase)}
num_to_chr = {i: c for i, c in enumerate(ascii_lowercase)}


flag_encrypted = 'z_jjaoo_rljlhr_gauf_twv_shaqzb_ljtyut'
key_pseudo = 'iigesssaemk'
key_first = ''
key_second = ''
log = open('log', 'w')


for i, ch in enumerate(key_pseudo):
    f = False
    for ch in ascii_lowercase:
        if num_to_chr[chr_to_num[ch] * 2 % 26] == key_pseudo[i]:
            if not f:
                f = True
                key_first += ch
            else:
                f = False
                key_second += ch


for i in range(int('1' + '0' * 10, 2), int('1' * 11, 2) + 1):
    key_num = bin(i)[2:]
    flag_decryted = ''
    key = ''

    for i, num in enumerate(key_num):
        if num == '0':
            key += key_first[i]
        else:
            key += key_second[i]

    for i, ch in enumerate(flag_encrypted):
        if ch == '_':
            flag_decryted += ch
            continue
        flag_decryted += num_to_chr[(chr_to_num[ch] - chr_to_num[key[i % len(key)]]) % 26]

    log.write(f'Binary key: {key_num.zfill(11)} | key: {key} | flag: {flag_decryted}\n')


log.close()