import urllib
import urllib.error
import urllib.request


try:
    site = urllib.request.urlopen('https://www.w3schools.com/python/')
except urllib.error.URLError:
    print('O Site W3School não está acessível no momento')
else:
    print('Consegui acessar o site W3Shool com sucesso')
    # print(site.read()) # Pegar o conteúdo em HTMl da página