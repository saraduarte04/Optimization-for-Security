import base64

with open("cp.jpg", "rb") as var:
    ler = var.read()
    encode = base64.b64encode(ler)
    tratamento = encode.decode("utf-8")

arquivo = tratamento
rotacao = 2
alfabeto = "abcdefghijklmnopqrstuvwxyz"
resultado = ""

for letra in arquivo:
    if letra in alfabeto:
        posicao = alfabeto.find(letra)
        posicao = (posicao + rotacao) %26
        resultado = resultado + alfabeto[posicao]
                
print (resultado)
print ("H4K34D0")


        