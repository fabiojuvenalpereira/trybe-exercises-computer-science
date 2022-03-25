
def qtd_tinta(metros):
    lata = 80
    rendimento = 3

    tinta_necessaria = metros / rendimento
    total_tinta = tinta_necessaria // 18
    print(tinta_necessaria % 18)

    if tinta_necessaria % 18:
      total_tinta +=1

    return (total_tinta, total_tinta * lata)

print(qtd_tinta(50))

