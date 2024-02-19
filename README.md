# RPA Challenge 

# Sobre o projeto

Atividade realizada com base no exercício 'RPA Challenge' proposto no site: https://rpachallenge.com/.

RPA Challenge é uma aplicação web para treinamento de RPA, onde deve ser feito download de um arquivo xlsx e realizar a leitura e o preenchimento de dados no formulário do site, 
o desafio é que os campos são dinâmicos e mudam de lugar a cada inserção na página, então a dificuldade está em mapear os seletores desses elementos inputs,
no meu projeto fiz o mapeamento pelo seletor Xpath de cada elemento input.

Ao final da inclusão a página mostra uma mensagem mostrando o tempo que o robô levou para a execução, nesse momento o robô faz a tradução dessa mensagem e
faz um screenshot da tela, salvando na pasta do projeto.

## Layout da web
![Web 1](https://github.com/Samaelpicoli/RPA_Challenge/blob/main/assets/web1.PNG)

# Tecnologias Utilizadas

Python

## Bibliotecas Utilizadas

Estão listadas no arquivo requirements.txt

## Sobre o código

O projeto foi dividido em módulos, onde um arquivo (desafio_rpa.py) contém a classe que faz todas as interações com o site (inicializa, faz a requisição do arquivo, leitura do arquivo e preenchimento dos dados),
e outro arquivo (traducao.py) contém a classe que traduz a mensagem final do site para PT-BR, ao final do processo o robô salva um screenshot da tela final do site.

Os arquivos são chamados dentro do arquivo main que instância a classe Desafio e executa o processo.

No main, o projeto foi desenvolvido como uma máquina de estados (INITIALIZATION, GET TRANSACTION, PROCESS, END), emulando o ReFramework do UiPath,
auxiliando a criar automações mais confiáveis, flexíveis e fáceis de manter ao longo do tempo.

# Como executar o projeto
Pré-requisitos: Python 3.11

```bash
#insalar dependências, dentro do seu projeto e com ambiente virtual ativo:
pip install -r requirements.txt
```

# Executar o projeto
python main.py

# Autor
Samael Muniz Picoli
