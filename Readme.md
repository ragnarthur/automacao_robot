# Projeto de Automação de Cadastro de Clientes

Este projeto tem como objetivo automatizar o cadastro de clientes em um sistema web a partir de dados fornecidos em um arquivo Excel. A automação é realizada utilizando a biblioteca Selenium para interagir com o navegador e a biblioteca `openpyxl` para ler os dados do Excel.

## Estrutura do Projeto

- `robot.py`: Contém a lógica para realizar o login no sistema web e iterar sobre o arquivo Excel para cadastrar os clientes.
- `automacao_cadastro.py`: Script principal que lê o arquivo Excel e chama a função de cadastro.
- `.env`: Arquivo contendo as variáveis de ambiente sensíveis (URL de login, email e senha).
- `.gitignore`: Arquivo para ignorar arquivos e diretórios específicos no controle de versão.
- `README.md`: Este arquivo de documentação.

## Pré-requisitos

- Python 3.6 ou superior
- Google Chrome
- ChromeDriver
- Bibliotecas Python: `selenium`, `openpyxl`, `python-dotenv`

## Instalação

1. Clone o repositório:
   ```sh
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio