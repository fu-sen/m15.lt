# Character code list
c=0
cls()
while c!=256:
  lc(c%32,c/32)
  print(chr(c))
  c=c+1

