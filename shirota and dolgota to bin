def perevod(shd):
  listshd = shd.split()
  #shirota(n or s)
  dd = int(listshd[0])
  mm = int(listshd[1])
  ss = int(listshd[2])
  znak = listshd[3]
  ddd = dd + mm/60 + ss/3600
  ddd = int(ddd)
  if znak == 'N':
    ddd = ddd
  else:
    ddd = -(ddd)
  #dolgota(w or e)
  dd2 = int(listshd[5])
  mm2 = int(listshd[6])
  ss2 = int(listshd[7])
  znak2 = listshd[8]
  ddd2 = dd2 + mm2/60 + ss2/3600
  ddd2 = int(ddd2)
  if znak2 == 'W':
    ddd2 = ddd2
  else:
    ddd2 = -(ddd2)
  return bin(ddd), bin(ddd2)


# Paris = 48 50 00 N , 2 20 00 E
shd = input('Enter the dolgota and shirota: ')
print(perevod(shd))            
