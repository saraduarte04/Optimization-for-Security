dicionario = {'numeros':['943607291', '979901657', '966478419', '910194174', '940848848', '914740487', '938290200', '927182276', '961862236', '975008938', '959931740', '968664851', '985713324', '917013906', '980187043', '929637109', '931952663', '964573691', '996749612', '933487573', '940246703', '963202877', '938081420', '987562686', '957663983', '961944853', '995014770', '939765421', '910147231', '916116618', '996190176'],
'nomes':['Alberico', 'Lucas', 'Benício', 'Gael', 'Joaquim', 'Nicolas', 'Henrique', 'Rafael', 'Isaac', 'Guilherme', 'Murilo', 'Lucca', 'Gustavo', 'João Miguel', 'Noah', 'Felipe', 'Anthony', 'Enzo', 'João Pedro', 'Pietro', 'Bryan', 'Daniel', 'Pedro Henrique', 'Enzo Gabriel', 'Leonardo', 'Vicente', 'Valentim', 'Eduardo', 'Antônio', 'Emanuel', 'Davi Lucca']}

print('=================================')
print('|Verificação de Numeros Expostos|')
print('=================================')


pergunta = input("Qual o seu nome?\n").title()

x = 0
for b in dicionario['nomes']:
    if pergunta == dicionario['nomes'][x]:
        dic = (dicionario['numeros'][x])
        print('''
         ___      __   __   __   ___  __  
        |__  \_/ |__) /  \ /__` |__  |  \ 
        |___ / \ |    \__/ .__/ |___ |__/ 

        ''')
        print("\033[31mSegundo a verificação, o nome "+pergunta+' teve o numero '+dic+' exposto')
        break
    x += 1
else:
    print('''
         __        ___  ___ 
        /__`  /\  |__  |__  
        .__/ /--\ |    |___         
    
    ''')
    print('\033[32m O nome pesquisado não teve nenhum numero exposto')