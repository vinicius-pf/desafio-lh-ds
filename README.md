# Titanic Classification Problem

## Preparando a máquina

- Instalação de [Python](https://www.python.org/). Esse projeto foi desenvolvido na versão [3.8.10](https://www.python.org/downloads/release/python-3810/). Também é necessário a instalação do [Git](https://git-scm.com/downloads)

- A pasta pode ser importada para o computador local, no destino que preferir, usando o comando
`git clone https://github.com/vinicius-pf/desafio-lh-ds.git`

- Após isso, caso ainda não tenha feito, é necessário criar um [ambiente virtual(venv)](https://docs.python.org/3/library/venv.html), utilizando `python3 -m venv ./venv`.

- Sempre que abrir o projeto, é necessário ativar a venv com `venv/Scripts/activate` no Windows. Caso estejas utiliando Linux, o comando é `source venv/Scripts/activate`. Quando o ambiente for ativado com sucesso, irá aparecer uma flag `(venv)` ao lado do caminho do diretório no terminal. Para desativar, basta rodar `deactivate`.

- Por último, instalar as bibliotecas necessárias utilizando pip, via `pip install -r > requirements.txt`. Para conferir as biliotecas instaladas, use `pip list`.
  
## Localização dos dados

Os dados brutos estão disponíveis na pasta `titanic-classification/data/01_raw`. Caso não se encontrem, podem ser baixados do [Kaggle](https://www.kaggle.com/competitions/titanic/data). O arquivo `gender_submission.csv` pode ser ignorado.

## Rodando o projeto

Esse projeto foi desenvolvido usando o framework Kedro. Durante o desenvolvimento dele foram criadas 3 pipelines, uma para a etapa de feature engineering, uma para a etapa de treinamento do modelo e a última para gerar as previsões do modelo.

É possível rodar todas as pipelines utilizando o comando `kedro run`. Ao rodar o projeto completo, serão gerados o dataset de *input* do modelo na pasta `titanic-classification\data\05_model_input`, o modelo de machine learning em um arquivo pickle na pasta `titanic-classification\data\06_models`, e as previsões do modelo para os passageiros do arquivo de teste na pasta `titanic-classification\data\07_model_output`.

Também é possível rodar cada pipeline de maneira individual. A pipeline de feature engineering gera o dataset de *input* do modelo de machine learning. O comando para rodar a pipeline é `kedro run --pipeline feature_engineering`.

Para criar e treinar o modelo de ML, é necessário o comando `kedro run --pipeline model_training `.

Por último, é possível rodar apena a pipeline que gera as previsões dos dados de teste utilizando o comando `kedro run --pipeline  model_prediction`.