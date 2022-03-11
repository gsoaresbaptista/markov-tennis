# Markov Chain - Tennis Simulation

### Introdução

Este projeto foi realizado para a disciplina de Processos Estocásticos Aplicados à Computação (INF09322), ofertada pela Universidade Federal do Espírito Santo - Ufes, no período 2021/2, ministrada pelo professor Rodolfo da Silva Villaça. O grupo que o produziu é composto por [Gabriel Soares](https://github.com/gsoaresbaptista), [Humberto Giuri](https://github.com/humbertogiuri) e [Lucca Passos](https://github.com/LuccaPassos).
O trabalho consiste em modelar uma partida de tênis como uma Cadeia de Markov, gerar simulações de _matches_ e fazer uma análise estatística dos resultados.

### Desenvolvimento

A linguagem utilizada para o desenvolvimento foi o Python, por ser versátil e bem recomendada para se trabalhar com dados, estatística, geração de gráficos, etc. O código para gerar a cadeia e simular os jogos está em `src/tennis`. Já a análise dos resultados, juntamente com maiores detalhes sobre o trabalho encontram-se no Jupter Notebook `analise.ipynb`.

Os _datasets_ contendo o log com o resultado de cada simulação encontram-se em `datasets`. O formato utilizado foi o `parquet.gzip`, uma vez que ele é altamente compactado, facilitando o trabalho com um volume grande de dados. Esses arquivos podem ser lidos utilizando a biblioteca pandas de Python, gerando _DataFrames_ que permitem a manipulação descomplicada dos valores.

### Gerando valores

Parar gerar as simulações basta executar o Notebook, escolhendo valores para _n_sample_ (número de simulações) e _probability_ (valor de p, onde p é a probabilidade do jogador A pontuar). Automaticamente será gerado um _dataset_ com os resultados computados.  
Para rodar o Notebook, garanta que todos os pacotes necessários descritos em `requirements.txt` estão instalados.

- Com pip

```
pip install -r .\requirements.txt --user
```
