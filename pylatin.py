pyg = 'ay'
original = raw_input('Enter a word:')
word = original.lower()
first = word[0]


if len(word) > 0 and original.isalpha():
    print word[1:] + first + pyg
else:
    print 'empty'