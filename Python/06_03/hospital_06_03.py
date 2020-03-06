print("Registro Hospitalar")

nome = input("Qual o nome completo do Paciente?:").title()
idade = int(input("Qual a idade do Paciente?:"))
risco = input("Esta no grupo de risco? (sim ou nao?)").upper()
if risco != "SIM" and risco != "NAO":
    risco = input("Digite somente (sim ou nao)").upper()

if idade < 15:
    print("Permanece na Fila de Espera.")
elif idade > 60:
    print("Prioritario.")
elif risco == ("SIM"):
    print("Triagem")
else:
    print("Tranquilo")
