real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.17
euro = real / 5.61
iene = real / 0.033
print('Com tantos R${:.2f} você pode comprar tantos US${:.2f}'.format(real, dolar))
print('Com tantos R${:.2f} voce pode comprar tantos EUR{:.2f}'.format(real, euro))
print('Com tantos R${:.2f} você pode comprar tantos JPY{:.2f}'.format(real, iene))