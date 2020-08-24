"""
Key 1 = 5dcec311ab1a88ff66b69ef46d4aba1aee814fe00a4342055c146533
Key 1 ^ Key 3 = 9a13ea39f27a12000e083a860f1bd26e4a126e68965cc48bee3fa11b
Key 2 ^ Key 3 ^ Key 5 = 557ce6335808f3b812ce31c7230ddea9fb32bbaeaf8f0d4a540b4f05
Key 1 ^ Key 4 ^ Key 5 = 7b33428eb14e4b54f2f4a3acaeab1c2733e4ab6bebc68436177128eb
Key 3 ^ Key 4 = 996e59a867c171397fc8342b5f9a61d90bda51403ff6326303cb865a
Flag ^ Key 1 ^ Key 2 ^ Key 3 ^ Key 4 ^ Key 5 = 306d34c5b6dda0f53c7a0f5a2ce4596cfea5ecb676169dd7d5931139
"""
def encrypt1(var, key):
    return bytes(a ^ b for a, b in zip(var, key))

key1 = bytes.fromhex('5dcec311ab1a88ff66b69ef46d4aba1aee814fe00a4342055c146533')
key1_key3 = bytes.fromhex('9a13ea39f27a12000e083a860f1bd26e4a126e68965cc48bee3fa11b')
key_2_key_3_key_5 = bytes.fromhex('557ce6335808f3b812ce31c7230ddea9fb32bbaeaf8f0d4a540b4f05')
key_1_key_4_key_5 = bytes.fromhex('7b33428eb14e4b54f2f4a3acaeab1c2733e4ab6bebc68436177128eb')
key_3_key_4 = bytes.fromhex('996e59a867c171397fc8342b5f9a61d90bda51403ff6326303cb865a')
Flag_key_1_key_2_key_3_key_4_key_5 = bytes.fromhex('306d34c5b6dda0f53c7a0f5a2ce4596cfea5ecb676169dd7d5931139')

flag = encrypt1(key1_key3, key_2_key_3_key_5)
flag = encrypt1(key_3_key_4, flag)
flag = encrypt1(flag, Flag_key_1_key_2_key_3_key_4_key_5)
print(flag)