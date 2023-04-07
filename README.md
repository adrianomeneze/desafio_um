# Operações Financeiras

### - Este projeto de uma aplicação utilizando a arquitetura limpa (clean architecture), separando as camadas de domínio, aplicação e infraestrutura.

### - A aplicação possui dois serviços: "Operações em aberto" e "Renegociação". O serviço "Operações em aberto" gera a cada final de mês, uma lista dos associados e do saldo de suas operações financeiras que estão em atraso. Já o serviço "Renegociação" retorna uma lista com os associados que já renegociaram seus atrasos.

# Tecnologias utilizadas
#### - *Python 3.x*
#### - *Biblioteca pytest para a realização dos testes unitários*

## Estrutura do projeto
````
domain/: contém as classes que representam o domínio da aplicação.
application/: contém as classes que representam a camada de aplicação.
infrastructure/: contém as classes que representam a camada de infraestrutura (arquivos, banco de dados, etc.).
tests/: contém os testes do projeto.
main.py: arquivo principal para a execução da aplicação.
````

# Executando a aplicação
1. Clone este repositório.
2. Certifique-se de que você possui o Python 3.x instalado em sua máquina.
3. No terminal, navegue até o diretório raiz do projeto.
4. Execute o arquivo main.py com o seguinte comando:

## Executando os testes
1. Certifique-se de que você possui o Python 3.x instalado em sua máquina.
2. No terminal, navegue até o diretório raiz do projeto.
3. Execute o seguinte comando para executar os testes:
````
pytest
````
4. Execute o seguinte comando para executar uma cobertura de codigo
````
pytest --cov=./
````

# Autor
### Este projeto foi desenvolvido por [Adriano Candido].