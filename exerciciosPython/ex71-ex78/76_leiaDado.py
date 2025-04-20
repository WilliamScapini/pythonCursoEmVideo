from modulos.moeda import moeda
from modulos.dado import dados
p = dados.leiaDinheiro("Digite o preço R$ ")
moeda.resumo(p,30,20)