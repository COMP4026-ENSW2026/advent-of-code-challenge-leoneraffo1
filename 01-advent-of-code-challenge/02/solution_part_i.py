points = int(0)
with open("i2.txt", encoding="utf-8",mode="r")as tabela:
  tabela = tabela.read()
  line = tabela.splitlines()
  for x in line:
    if x == "A X":
      points += 4
    elif x == "A Y":
      points += 8
    elif x == "A Z":
      points += 3
    elif x == "B X":
      points += 1
    elif x == "B Y":
      points += 5
    elif x == "B Z":
      points += 9
    elif x == "C X":
      points += 7
    elif x == "C Y":
      points += 2
    elif x == "C Z":
      points += 6
  print(points)
