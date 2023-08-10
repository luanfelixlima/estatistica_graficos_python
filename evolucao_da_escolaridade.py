import matplotlib.pyplot as plt

# fonte: https://seriesestatisticas.ibge.gov.br/series.aspx?no=4&op=0&vcodigo=ECE370&t=media-anos-+estudo-pessoas-10-anos

# carregando dados
anos = [1995, 1996, 1999, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009]
total = [5.2, 5.3, 5.8, 6.1, 6.3, 6.5, 6.6, 6.7, 6.9, 7.0, 7.1, 7.2]  # media de anos de estudo

# verificando integridade
if len(anos) == len(total):
    print("Dados carregados...")

# configrando a plotagem
x = anos
y = total

plt.title("Evolução da escolaridade da parcela da população brasileira com idade > 10 anos")
plt.ylabel("Anos de estudo (pessoas > 10 anos)")
plt.xlabel("Ano")

# plotando o gráfico
plt.plot(x, y, linestyle='--', marker='o', color='k')
plt.show()


