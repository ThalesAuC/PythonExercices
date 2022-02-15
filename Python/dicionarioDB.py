from distutils.log import info

banco={}
i = 0
while i < 10:
    
    name = input("insira o nome para o cadastro: ")
    info = input("insira uma informação para o banco: ")
    banco[name] = info
    i+=1

print(banco)