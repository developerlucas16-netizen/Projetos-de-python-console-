# crie um codigo em python que teste se o site pudim está acessivel

import urllib
import urllib.request

try:
  site = urllib.request.urlopen('https://www.pudim.com.br')
except urllib.error.URLError:
  print('O site pudim não esta assecivel no momento')
else:
  print('Consegui acessar o site pudim')
  print(site.read())