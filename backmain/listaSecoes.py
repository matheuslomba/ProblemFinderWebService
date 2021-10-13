def lista_Secoes(bs):
    secoes = bs.find_all('span', {'class': 'feed-post-metadata-section'})

    temas = []
    for i in secoes:
        if i.get_text() not in temas:
            temas.append(i.get_text()[1:-1])

    return temas