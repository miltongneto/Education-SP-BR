# Education-SP-BR
O objetivo deste projeto é utilizar dados abertos e inteligência artificial para melhorar a educação do estado de São Paulo. 

O código principal do projeto está na pasta *notebooks*, onde os arquivos estão numerados de acordo com a lógica de execução e seguindo o processos comuns em Ciência de Dados.
Na pasta *notebooks*:
- Os arquivos os arquivos *eda* (de *Exploratory Data Analysis*) são os primeiros a serem executados (ou apenas lidos). Nesses arquivos é realizado uma análise e manipulação dos dados. Resultando uma base de dados transformada e salva em *data/processed*. Este resultado conta com agregação e mudança de grão (ou nível) dos dados brutos, em geral passando para o grão escola, além da limpeza, tratamento, criação de atributos, etc.
- O primeiro arquivo que deve ser executado é o 00-eda-saresp.ipynb. Ele deve ser o primeiro pois algumas arquivos de *EDA* utilizam ele.
- A ordem dos arquivos *01-eda-\** não tem interfere no resultado ou entendimento.
- Em *02-feature_engineering.ipynb*, é realizado a preparação dos dados para etapa de Machine Learning. Exercendo o refinamento do tratamento feito na etapa anterior, juntando as diversas bases e criando novas features (atributos).
- Na etapa de modelagem, em *03-machine_learning.ipynb*, é construído um classificador para predizer se uma escola terá bom desempenho no SARESP (Sistema de Avaliação de Rendimento Escolar do Estado de São Paulo) ou não. Com intuito de alcançar uma taxa elevada de assertividade e mapear bem as características da escola, que incluem fatores externos e aspectos da gestão escolar. 
- Depois de construir o modelo e alcançar um bom desempenho, é feita a interpretabilidade do modelo em *04-interpretability.ipynb*. Nesta fase, é analisado a relevância dos atributos e de que forma eles impactam.

## Features
| Atributo | Descrição |
| --- | --- |
| LoCapital | Indica se a escola é na Capital do estado |
| LoArea | Área do município | 
| LoPopEstimada | Estimativa da população no município segundo o IBGE |
| LoRuralUrbano | Indica se a escola está numa área rural ou urbana | 
| LoVAB_publico | Valor Adicionado Bruto público | 
| LoVAB_total | Valor Adicionado Bruto total  | 
| LoPIB |  PIB (Produto Interno Bruto) do município | 
| LoPIB_perCapita | PIB per capita do município | 
| LoCompEdu | Número de companhias de Educação | 
| LoCluster | Informa qual cluster a escola faz parte de acordo com o agrupamento com k-Means | 
| PrFormacao | Percentual de professores de acordo com a titulação | 
| PrQtdProfessores | Quantidade de professores na escola | 
| PrQtdFormacaoCont | Quantidade de professores com formação continuada (pós-graduação) | 
| SeQtdCargosDistintos | Quantidade de cargos distintos dos servidores da escola | 
| AlQtdTotalAlunos | Quantidade total de alunos na escola  | 
| AlQtdAlunosSalaMedia | Quantidade média de alunos por sala | 
| AlQtdAlunosSalaStd | Desvio padrão da quantidade de alunos na sala | 
| AlQtdClassesTipo | Quantidade de classes de acordo com o tipo de ensino. Sendo as modalidades de ensino: fundamental I e II, e ensino médio  | 
| AlQtdAlunosTipo | Quantidade de alunos de acordo com o tipo de ensino | 
| GeQtdGestores2018 | Quantidade de gestores no ano de 2018. Esse atributo é construído para cada tipo de gestor, sendo eles: diretor, vice-diretor e coordenador | 
| GeQtdGestores5Anos | Quantidade de gestores nos últimos 5 anos. Esse atributo é construído para cada tipo de gestor | 
| DiIdadeDiretor | Idade do(a) diretor(a) atual  | 
| DiAnosCargoC | Anos do(a) diretor(a) trabalhando no cargo de classificação | 
| DiAnosCargoE | Anos do(a) diretor(a) trabalhando no cargo de exercício | 
| DiTitulacao | Titulação do(a) diretor(a) | 
| JoQtdDisciplinasMedia | Média do número de disciplinas que os docentes ministram | 
| JoQtdDisciplinasStd | Desvio padrão do número de disciplinas que os docentes ministram | 
| JoQtdDisciplinasMax | Quantidade máxima de disciplinas que os docentes ministra | 
| JoQtdTotalAulasStd | Desvio padrão do total de aulas que os docentes ministram | 
| JoQtdTotalAulaSMax | Quantidade máxima de aulas que os docentes ministram | 
| JoQtdTotalAulasMedia | Média da quantidade de aulas que os docentes ministram | 
| SeIdadeMedia | Média da idade dos servidores | 
| SeIdadeStd | Desvio padrão da idade dos servidores | 
| SeTempCargoC_Media | Tempo médio dos servidores no cargo de classificação | 
| SeTempCargoC_Std | Desvio padrão do tempo dos servidores no cargo de classificação | 
| SeCategFuncional | Percentual de servidores em cada categoria funcional |
| ANA | Nota do município na última ANA. Os resultados são representados em três notas: matemática, escrita e leitura | 
| SeRelacaoAlunoServ | Relação do numero de alunos para o numero de servidores | 
| SeRelacaoAlunoProf | Relação do numero de alunos para o numero de professores |

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
