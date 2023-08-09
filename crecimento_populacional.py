import matplotlib.pyplot as plt
import csv

with open('dados/populacao_brasileira.csv', 'r') as arquivo:
    arquivo_csv = csv.reader(arquivo)

    c = 0
    anos = []
    populacao = []
    for linha in arquivo_csv:
        if c == 0:  # separando o titulo do csv
            c += 1
            pass
        else:  # separando os dados ano e população pelo separador ";"
            separador = linha[0].find(";")
            anos.append(int(linha[0][:separador]))
            populacao_parcial = int(linha[0][separador + 1:]) / 100_000_000
            populacao.append(populacao_parcial)

plt.title("População Brasileira 1980 - 2016")
plt.xlabel("Ano")
plt.ylabel("População x100.000.000")
plt.bar(anos, populacao)
plt.plot(anos, populacao, linestyle="--", color="k")
plt.show()
