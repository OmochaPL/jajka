#moja wesja

phrase = "Podaj jajko!"
plist = list(phrase)
print(phrase)
print(plist)
for i in range(3):
    plist.pop()
plist.remove('P')
plist.remove('a')
plist.remove('j')
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)


# z książki

phrase = "Podaj jajko!"
plist = list(phrase)
print(phrase)
print(plist)
for i in range(4):
    plist.pop()
plist.remove('P')
plist.remove('a')
plist.extend([plist.pop(), plist.pop()])
plist.insert(2, plist.pop(3))
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
