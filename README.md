# Titanic Classification Problem

## Preparando a máquina

- Instalação de [Python](https://www.python.org/). Esse projeto foi desenvolvido na versão [3.8.10](https://www.python.org/downloads/release/python-3810/). Também é necessário a instalação do [Git](https://git-scm.com/downloads)

- A pasta pode ser importada para o computador local, no destino que preferir, usando o comando
`git clone https://github.com/vinicius-pf/desafio-lh-ds.git`

- Após isso, caso ainda não tenha feito, é necessário criar um [ambiente virtual(venv)](https://docs.python.org/3/library/venv.html), utilizando `python3 -m venv ./venv`.

- Após isso, é necessário ativar a venv com `venv/Scripts/activate` no Windows. Caso estejas utiliando Linux, o comando é `source venv/Scripts/activate`. Caso o ambiente foi ativado com sucesso, irá aparecer uma flag `(venv)` ao lado do caminho do diretório no terminal. Para desativar, basta rodar `deactivate`.

- Por último, instalar as bibliotecas necessárias utilizando pip, via `pip install -r > requirements.txt`. Para conferir as biliotecas instaladas, use `pip list`.
  
## Localização dos dados

Os dados brutos estão disponíveis na pasta `titanic-classification/data/01_raw`. Caso não se encontrem, podem ser baixados do [Kaggle](https://www.kaggle.com/competitions/titanic/data). O arquivo `gender_submission.csv` pode ser ignorado.

## Rodando o projeto

O projeto foi desenvolvido em Kedro, então para rodar o sistema é necessário efetuar o comando `kedro run`

## Deploy local
