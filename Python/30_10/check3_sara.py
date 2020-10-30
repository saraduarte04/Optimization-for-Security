aliceprivada = 18
bobesponjaprivada = 5
prime = 13
generator = 6
alice2 = (generator ** aliceprivada) % prime
bobesponja2 = (generator ** bobesponjaprivada) % prime
alicepublica = (bobesponja2 ** aliceprivada) % prime
bobesponjapublica = (aliceprivada ** bobesponja2) % prime
if bobesponjapublica == alicepublica:
    print('I G U A I S')