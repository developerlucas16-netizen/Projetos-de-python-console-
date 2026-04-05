from myPacks import dados
from myPacks import moeda

p = dados.leiaDinheiro('Digite o valor: R$')
moeda.resumo(p, 80, 20)