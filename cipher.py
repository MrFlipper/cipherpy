alph = 'abcdefghijklmnopqrstuvwxyz'
keyword = raw_input('please enter the keyword: ')


cipherbet = keyword+alph
CipherAlphabet = ""
for i in keyword:
     for j in alph:
          if keyword[i] != alph[j]:
                CipherAlphabet[i] = keyword[i]




print cipherbet
print CipherAlphabet
