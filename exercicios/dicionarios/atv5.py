entrada = input("Digite uma frase: ")
palavras = entrada.split()
frequencia = {}
total_palavras = len(palavras)

for palavra in palavras:
    if palavra in frequencia:
        frequencia[palavra] += 1
    else:
        frequencia[palavra] = 1

print("Frequência das palavras:")
for palavra, freq in frequencia.items():
    print(f"- {palavra}: {freq}")

print(f"Total de palavras: {total_palavras}")
