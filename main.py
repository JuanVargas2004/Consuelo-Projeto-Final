import indeed

cargo = "Cozinheiro" #SUBSTITUA PARA O CARGO DESEJADO
localidade = "Acre" #SUBISTITUA PARA A LOCALIDADE DESEJADA

indeed.pesquisar(cargo, localidade)
vagas = indeed.scrap_indeed(cargo, localidade)

for vaga in vagas:
    print("#"*50)
    print(vaga)
    print("#"*50)
