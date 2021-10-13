from urllib.request import urlopen
from bs4 import BeautifulSoup

from listaSecoes import lista_Secoes
from entraMateria import entra_Materia
from pegaConteudo import pega_Conteudo

def mainbusca(metodo, url):

    html = urlopen(url)
    bs = BeautifulSoup(html, 'html.parser')

    if metodo == 1:
        #Lista todos os tópicos existentes na tela iniciao do G1 (Política, economia, etc)
        temas = lista_Secoes(bs)
        return temas

    elif metodo == 2:
        #Entra no link da matéria e pega o conteúdo
        '''
        links = entra_Materia(bs)
        
        pega_Conteudo(links[1])
        
        for l in links:
            pega_Conteudo(l)
        '''