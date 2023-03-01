# VirtualEnvs:

As virtual envs (abreviação de ambientes virtuais) são uma ferramenta essencial para o desenvolvimento em Python, especialmente quando trabalhamos com projetos complexos que têm várias dependências e requerem diferentes versões de bibliotecas ou pacotes. Um ambiente virtual é basicamente uma cópia do ambiente Python padrão que permite que você instale pacotes e bibliotecas específicas para um projeto sem afetar outros projetos ou o ambiente global do sistema.

Ao criar um ambiente virtual, você isola o ambiente Python do sistema global, permitindo que você instale pacotes específicos para um projeto sem afetar outros projetos ou o sistema global. Isso torna mais fácil gerenciar e controlar as dependências do projeto e garante que as bibliotecas instaladas em um projeto não entrem em conflito com outras bibliotecas instaladas no sistema.

Ao ativar um ambiente virtual, você pode instalar pacotes e bibliotecas usando pip, que são armazenados localmente no ambiente virtual. Você também pode especificar a versão exata de um pacote ou biblioteca que o projeto requer sem afetar outros projetos.

O Python vem com uma biblioteca padrão para criar e gerenciar ambientes virtuais chamada venv, que é usada para criar e ativar ambientes virtuais. Existem também outras ferramentas, como virtualenv e conda, que podem ser usadas para criar e gerenciar ambientes virtuais em Python.

## Como usar?

```
python -m venv myenv
source myenv/bin/activate

```

Agora que o ambiente virtual está ativado, você pode instalar pacotes Python sem afetar o sistema principal do Python. Para instalar um pacote, use o comando pip install nome_do_pacote.

Quando terminar de trabalhar com o ambiente virtual, você pode desativá-lo digitando o seguinte comando:

```
python -m venv myenv

```