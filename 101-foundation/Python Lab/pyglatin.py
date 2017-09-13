w = raw_input("Please enter a valid word: ")

def translate(w):
  wlist = list(w)
  wlist.append(wlist[0].lower())
  del(wlist[0])
  wlist.append('a')
  wlist.append('y')
  w = ''.join(wlist)
  return w
  
print translate(w)
