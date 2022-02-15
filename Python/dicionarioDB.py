from distutils.log import info

banco={}
i = 0
while i < 2:
    
    name = input("insira o nome para o cadastro: ")
    info = input("insira uma informação para o banco: ")
    info2 = input("insira uma segunda informação: ")
    banco[name] = [info, info2]
    i+=1

print(banco)