nome = input("Insira seu nome?:").title()
genero = input("Qual seu genero? (Masculino ou Feminino):").title()
nivel_acesso = input("Qual seu nivel de acesso? (Adm, Usr ou Guest):").title()

if genero == "Masculino" and nivel_acesso == "Adm":
    print("Olá administrador")
elif genero == "Feminino" and nivel_acesso == "Adm":
    print("Olá administradora")
elif genero == "Masculino" and nivel_acesso == "Usr":
    print("Olá usuário")
elif genero == "Feminino" and nivel_acesso == "Usr":
    print("Olá usuária")
elif nivel_acesso == "Guest":
    print("Olá visitante")
else: 
    print("Olá desconhecido(a)")