n=int(input())
for i in range(1,((n+1)//2)+1):
  print(' ' * (((n+1)//2)-i) + '*' * (2*i-1))