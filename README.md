# RPA Exercise 

# Sobre o projeto

Atividade realizada com base no exercício 'RPA Exercice' proposto no site: https://rpaexercise.aisingapore.org/.

RPA Exercise é uma aplicação web para treinamento de RPA, onde deve ser feito download de um arquivo CSV e realizar a leitura e o preenchimento de dados sobre vagas de emprego
no formulário do site, e após isso, fazer uma verificação na lista de candidatos para as vagas, realizando uma leitura dos dados e assim aprovando e rejeitando candidatos.

Ao final da inclusão e verificação dos candidatos, a página mostra uma mensagem de Congratulations, nesse momento o robô faz um screenshot da tela e salva na pasta do projeto.

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
