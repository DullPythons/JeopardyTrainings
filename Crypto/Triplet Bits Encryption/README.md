# Triplet Bits Encryption

I have to encrypt super secret information, so I used triplet bits. Is it really safe? <br/>
Формат флага Poseidon{a-zA-Z0-9!\_ }

# Решение

Если посмотреть на таблицу истинности для функции mixkeybit, то видно, что единиц больше, чем нулей. <br/>
Так же из кода видно, что полученный файл - это 256 раз зашифрованная одна и та же строчка.
Именно поэтому для того, чтобы понять, какой бит во флаге достаточно посмотреть в каждом столбце больше нулей или же больше единиц. <br/>
Соответственно, если больше нулей, то изначально была 1 и наоборот. Это следует из особенностей функции mixkeybit. <br/>
Решение в triplet_bits.py <br/>
**Poseidon{7h3_u53_0f_pr0b4b1l17y_15_57r0n6}**


https://www.josephsurin.me/posts/2020-08-09-poseidonctf-2020-writeups#triplet-bits-encryption
