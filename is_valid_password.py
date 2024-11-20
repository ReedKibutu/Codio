def is_valid_password (word): 
  cap = False
  num = False
  special = False
  leng = False
  for x in word:
    if x.isupper() == True:
      cap = True
    if x.isnumeric() == True:
      num = True
    if (len(word) + 1) >= 11:
      leng = True 
    if x in "[]#%^*+=_\|~<>€£¥•?!.,":
      special = True
  return cap and num and leng and special
