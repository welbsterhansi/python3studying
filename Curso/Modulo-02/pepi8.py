"""
Exibiçao de texto no python
Ler sobre pepi8

- 4 espaços sempre para idenntar.
- Classes começa com letra maiusculas, exemplo:
class Calculadora:
    pass
- Funcao usa  nome minusculo ou nomes com _


"""
class Calculadora:
    pass

def testing():
    pass

def soma_texto():
    pass

if 'a' in "banana":
    print ("tem")

"""
Explicando a sintaxe acima:

def: é a palavra-chave que indica que estamos definindo uma função;
nome_da_funcao: é o nome que você escolhe para a função. É importante escolher um nome que descreva bem o que a função faz;
argumentos: são os valores que a função recebe como entrada. Você pode ter zero ou mais argumentos, separados por vírgulas. Caso não haja argumentos, deixe os parênteses vazios;
:: indica que a definição da função está terminando e o corpo da função começará na próxima linha;
# corpo da função: é onde você escreve o código que será executado quando a função for chamada;
return: é a palavra-chave que indica o valor que será retornado pela função. Caso a função não precise retornar nenhum valor, você pode omitir essa linha.
"""

# Exemplo de funcao:

def soma(a, b):
    result = a + b
    return result
a = 100
b = -2
total = soma(a, b)
print(total)

"""
Sobre linhas em branco antes de uma classe:

Não há um número exato de linhas em branco que você precisa colocar antes de uma classe em Python. De acordo com o guia de estilo 
PEP 8, recomenda-se usar duas linhas em branco antes da definição de uma nova classe, ou uma linha em branco caso a classe seja definida 
no topo de um módulo. No entanto, essa é uma recomendação e não uma regra obrigatória. 
"""

class Modulo02:
    pass


class Hello:
    pass

"""
Imports devem ser sempre colocados em linhas separadas
"""
import sys
import os







