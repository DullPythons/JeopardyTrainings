#!/usr/bin/python
# -*- coding: utf-8 -*-
from collections import Counter
import operator

"""
find the key length for vigenere
"""
def idx_of_coincidence(msg):
    c = Counter(list(msg))
    return sum(x*(x-1) for x in c.values())/(len(msg)*(len(msg) - 1))


"""
cesar decryptor
"""
def cesar(text):
    alpha = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя '
    s = text.strip()
    result = []
    for n in range(1,34):
        res = ''
        for c in s:
            res += alpha[(alpha.index(c) + n) % len(alpha)]
        result.append(res)
    return result


"""
cesar decryptor with current letter - shift
"""
def cesar_decr(text, letter):
    result = ''
    text = text.strip()
    alpha = ' абвгдежзийклмнопрстуфхцчшщъыьэюя'
    shift = alpha.index(letter)
    for c in text:
        result += alpha[(alpha.index(c)-shift) % len(alpha)]
    return result


"""
count frequency for unique letters in all text
"""
def frequency_analyze(text):
    result = {}
    amount_letters = len(Counter(list(text)).values())
    for c in text:
        result[c] = text.count(c)
    for letter in result.keys():
        result[letter] = 100 * result[letter] / len(text)
    return result


if __name__ == '__main__':

    mes = 'тфщгщпьзершгждяыэйбэшояфазпжсяэнтйрабьпъпухзхлотйббкмгрффйфиъпжпббпфпушъзтмпщзисыэшэрюьзафюахгспрбмспэщраоьъумпьзисфофпртымтвюощпфюохоспючйббптэююоцпфынлжьрофбрьэфунупжйрхфжуцььбжрыбюйббймачшсбжруъзиспазлряяхтщоъпаырщжвгфахаяэошлсчптацщоюуябэжоцюрблююсмоююоьпаюжмжрээжпюпцфбьпещпрхтхафврба  эпиюх тйрычяэряяхтвюфжрашсмуббспжряэщпэпспеппещпрффйфиъпжлсъообуюяхзцэьз раыхуашажоспчопт пнжюшфжтсыпубюфябаюрочфырсмацуэжугцбчлщпчжоспуптып жхцэчстяьоцсщъэтпвкшжлруяъещпэфашртхгя чт'
    decr_tmp = []
    #find key length
    idc = min([(i,idx_of_coincidence(mes[::i])) for i in range(1, 50)],
              key=lambda x: abs(0.0667 - x[1]))
    print('key length: ', idc[0])

    #separate at groups
    print('separete at groups')
    res_groups = []
    for i in range(idc[0]):
        res_groups.append("")

    i = 0
    for c in mes:
        res_groups[i%idc[0]] += c
        i += 1

    output = open('analyze.txt','w')
    # output_cesar = open('cesar_brute_force.txt', 'w')

    j = 0
    max_len = 0
    for current_string in res_groups:

        #frequency analisys
        res = frequency_analyze(current_string)
        output.write(current_string + '\n')
        for key in res.keys():
            output.write(str(key)+': '+str(res[key])+'\n')
        output.write('\n')

        # all_variants = cesar(current_string)
        # output_cesar.write('CESAR for string: '+current_string+'\n')
        # for el in range(len(all_variants)):
        #     output_cesar.write(str(el)+': '+str(all_variants[el])+'\n')
        # output_cesar.write('\n')

        # find space
        max_letter = max(res.items(), key=operator.itemgetter(1))[0]
        if j == 3:
            max_letter = 'а'

        # decr cesar
        res_string = cesar_decr(current_string, max_letter)
        if len(res_string) > max_len:
            max_len = len(res_string)
        decr_tmp.append(res_string)
        j += 1

    # the whole text
    text = ''
    for i in range(max_len):
        if i < len(decr_tmp[0]):
            text += decr_tmp[0][i]
        if i < len(decr_tmp[1]):
            text += decr_tmp[1][i]
        if i < len(decr_tmp[2]):
            text += decr_tmp[2][i]
        if i < len(decr_tmp[3]):
            text += decr_tmp[3][i]
        if i < len(decr_tmp[4]):
            text += decr_tmp[4][i]
    print(text)
