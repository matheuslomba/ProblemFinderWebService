def entra_Materia(bs):

    linkMateria = bs.find_all('a', {'class':'feed-post-link gui-color-primary gui-color-hover'})

    links = []

    for i in linkMateria:
        links.append(i.get('href'))
    return links