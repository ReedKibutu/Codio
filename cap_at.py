def cap_at(word, x):
  word = str(word)
  x = int(x)
  if x in range(0, len(word)):
    word2 = word[x].upper()
    word = word[0:x] + word2 + word[(x+1):]
    return word  
  else:
    return word
