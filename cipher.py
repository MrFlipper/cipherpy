alph = 'abcdefghijklmnopqrstuvwxyz'
keyword = input('please enter the keyword: ')
cipherbet = alph+keyword
cipherbet = sorted(set(cipherbet))
print(cipherbet)
