# Rock = 1 (a,x)
# Paper = 2 (b,y)
# Scissor = 3 (c,z)
# win = 6
# draw = 3 each
# loss = 0

points = int(0)
with open("i2.txt", encoding="utf-8",mode="r")as tabela:
  tabela = tabela.read()
  line = tabela.splitlines()
  for x in line:
    if x == "A X":
      points += 3
    elif x == "A Y":
      points += 4
    elif x == "A Z":
      points += 8
    elif x == "B X":
      points += 1
    elif x == "B Y":
      points += 5
    elif x == "B Z":
      points += 9
    elif x == "C X":
      points += 2
    elif x == "C Y":
      points += 6
    elif x == "C Z":
      points += 7
  print(points)
    
  
