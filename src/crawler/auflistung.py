import requests
from bs4 import BeautifulSoup

class postCrawled():
    
    def __init__(self, titulo, emoticono, contenido, imagen):
        
        self.titulo = titulo
        self.emoticono = emoticono
        self.contenido = contenido
        self.imagen = imagen

class postExtractor():
    
    def extraerInfo(self):
        
        miDoc = requests.get("http://python.beispiel.programmierenlernen.io/index.php")
        
        docFinal = BeautifulSoup(miDoc.text, "html.parser")
        
        posts = []
        
        for card in docFinal.select(".card"):
            
            titulo = card.select(".card-title span")[1].text
            emoticomo = card.select_one(".emoji").text
            contenido = card.select_one(".card-text").text
            imagen = card.select_one("img").attrs["src"]
            
            
            crawled = postCrawled(titulo, emoticomo, contenido, imagen)
            
            posts.append(crawled)
        
        return posts
    
unPost = postExtractor()
    
listaPost = unPost.extraerInfo()       
        
for elPost in listaPost:
    
    print(elPost.emoticono)
    print(elPost.titulo)
    print(elPost.contenido)
    print(elPost.imagen)
    print("")





