# PEP8:

PEP8 é uma abreviação para "Python Enhancement Proposal 8". É um documento que define as diretrizes e recomendações oficiais para escrever código Python legível e de fácil manutenção. Essas diretrizes incluem convenções de nomenclatura para identificadores, estilo de codificação, espaçamento, indentação e outras práticas recomendadas.

O objetivo do PEP8 é tornar o código Python mais fácil de ler e entender para outros programadores, além de garantir que o código seja consistente em toda a base de código. Ele também ajuda a evitar erros comuns de codificação e a tornar o código mais fácil de manter e modificar.

Algumas das recomendações do PEP8 incluem:

Usar espaços em vez de tabs para indentação.
Limitar o comprimento das linhas de código a 79 caracteres.
Usar nomes descritivos para variáveis, funções e classes.
Separar as funções e classes por duas linhas em branco.
Usar letras minúsculas e underscores para separar palavras em nomes de variáveis e funções.
Evitar linhas em branco no final do arquivo.
Essas recomendações são amplamente aceitas pela comunidade Python e são seguidas por muitos programadores Python em todo o mundo. É uma boa prática seguir as diretrizes do PEP8 ao escrever código Python para tornar o seu código mais legível, manutenível e compatível com outros projetos Python.

# Usando DIR e HELP:

O comando dir
O comando dir é usado para listar todos os atributos e métodos disponíveis para um objeto. Você pode usá-lo assim:

```
objeto = "Olá mundo"
dir(objeto)

```

A função help
A função help é usada para obter ajuda e documentação sobre um objeto específico. Você pode usá-la assim:


```
objeto = "Olá mundo"
help(objeto.upper)

```

O comando dir
O comando dir é usado para listar todos os atributos e métodos disponíveis para um objeto. Você pode usá-lo assim:


```
objeto = "Olá mundo"
dir(objeto)
```
Por exemplo como eu faço um code que recebe um nome e idade e que em cada
palavra a primeira letra precisa ser maiuscula?


```
print("Qual o seu nome?")
name = input().title()
print(f"{name} is happy!")
```
Vamos usar o python3 interativo:


```
pytthon3

name = "francisco welbster oliveira da silva"
```

Como eu faço para ver os metodos que name recebe?

```
>>> dir(name)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

```
Agora como eu acho o motodo que deixa a primeira letra de cada palavra maiscula?

```
help(name.title)
title() method of builtins.str instance
Return a version of the string where each word is titlecased.

More specifically, words start with uppercased characters and all remaining
cased characters have lower case.
```