print(''' 
 _____     _                 _      
|_   _|_ _| |__ _  _ __ _ __| |__ _ 
  | |/ _` | '_ \ || / _` / _` / _` |
  |_|\__,_|_.__/\_,_\__,_\__,_\__,_|
                                    

''')


a = input("Digite um numero para ver a tabuada\n>")
i = 0

for i in range(11):
  print("{} X {} = {}".format(a, i, a * i))
