calorias = 0
elfos = []
with open("input.txt", encoding="utf-8",mode="r")as tabela:
  line = [(a.replace('\n', " ")) if a=='\n' else int(a.replace('\n', "")) for a in tabela.readlines()]
  for x in line:
    if x == " ":
      elfos.append(calorias)
      calorias = 0
    else:
      calorias += int(x)
  print(max(elfos))
