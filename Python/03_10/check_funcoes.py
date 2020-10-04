def salvar():
    arquivo = input("Digite o endereço do arquivo que deseja realizar backup:")
    abrir = open(arquivo , "r") 
    salvar = open("bkp" , "w")
    salvar.writelines(abrir) 
    print('\n_____________________________')
    print('\033[1;92m\nUfa... backup realizado com sucesso!\033[0;0m')
    print('_____________________________')

def backup():
    arquivo = input("Digite o endereço do arquivo que deseja restaurar:")
    abrir = open("bkp", "r")
    salvar = open(arquivo , "w")
    salvar.writelines(abrir) 
    print('\n_____________________________')
    print('\033[1;92m\nUfa... restauração realizada com sucesso!\033[0;0m')
    print('_____________________________')