lar = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = lar * alt
print('Sua parede tem dimensão de {}x{} e sua área é {}m²'.format(lar, alt, area))
tinta = area / 2
print('Para pintar {}m² precisa de {}L de tinta'.format(area, tinta))