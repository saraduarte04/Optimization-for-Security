print("Informações das Graduações")

nome = input("Insira seu nome completo?").title()
graduacao = input("Insira o tipo de sua graduação: (Tecnólogo ou Bacharelado?)").title()
if graduacao != "Tecnologo" and graduacao != "Tecnólogo" and graduacao != "Bacharelado":
    print("Graduação Inexistente")
    graduacao = input("Insira o tipo de sua graduação: (Tecnológo ou Bacharelado?").title()

if graduacao == "Bacharelado":
    print("Duração de 4 até 6 anos.")
elif graduacao == "Tecnologo" or graduacao == "Tecnólogo":
    print("Duração de 2 até 3 anos.")
else:
    print("Graduação Inaceitável.")