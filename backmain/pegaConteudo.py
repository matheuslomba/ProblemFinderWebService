from newspaper import Article
import nltk

def pega_Conteudo(link):

    artigo = Article(link)
    artigo.download()
    artigo.parse()
    nltk.download('punkt')
    artigo.nlp()

    titulo = artigo.title
    print('Título:', titulo)

    data_publ = artigo.publish_date
    print('Data de Publicação:', data_publ)

    conteudo = artigo.text
    print('Conteúdo:', conteudo)

    pal_chaves = artigo.keywords
    print('Palavras-Chave:', pal_chaves)