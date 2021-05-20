import requests
from bs4 import BeautifulSoup

miReq = requests.get("https://www.movistar.com.mx/")
print(miReq.status_code)
print(miReq.headers)
print(miReq.text)


miDoc ="""
    
    <html>
        <style>
            .pImportante{
                
                color:red;
            }
        
        
        </style>
        
        <body>
            <p class='pImportante'>Este es el primer parrafo</p>
            <p>Este es el psegundo parrafo</p>
            
            <a>Es un vinculo</a>
        </body>
    
    
    </html>
"""

docFinal =BeautifulSoup(miDoc, "html.parser")

for parrafo in docFinal.find_all("p"):
    print(parrafo.attrs)
    print(parrafo.text)

print(docFinal)