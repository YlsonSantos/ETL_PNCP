# "ETL PNCP" - Extração de Contratações Públicas

## Descrição do Projeto
Este projeto consiste em uma solução de Engenharia de Dados para a extração, transformação e carga (ETL) de dados provenientes da API do **Portal Nacional de Contratações Públicas (PNCP)**. O objetivo é coletar informações sobre contratações públicas brasileiras, tratar os dados brutos e armazená-los de forma estruturada no banco de dados NoSQL **MongoDB Atlas**.

## Arquitetura da Solução
A solução foi desenvolvida utilizando **Orientação a Objetos (POO)** em Python, dividida em módulos com responsabilidades distintas:

* **Extractor (`PNCPExtractor`):** Responsável pelo consumo da API REST do PNCP.
* **Transformer (`PNCPTransformer`):** Responsável pela limpeza, filtragem e normalização dos dados.
* **Loader (`PNCPLoader`):** Responsável pela conexão e persistência no MongoDB Atlas.
* **Main:** Orquestrador que executa o fluxo completo do pipeline.

### Fluxo de Dados
1.  **Extract:** O pipeline solicita dados à API do PNCP utilizando parâmetros de data e paginação.
2.  **Transform:** O JSON bruto é processado para remover campos desnecessários e padronizar chaves como CNPJ e valores monetários.
3.  **Load:** Os documentos tratados são inseridos em um cluster na nuvem (MongoDB Atlas).

## Requisitos Técnicos
* Python 3.10+
* MongoDB Atlas (Cluster configurado)
* Bibliotecas: `requests`, `pymongo`, `python-dotenv`

## Configuração do Ambiente

1.  **Clonar o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/projeto_etl_pncp.git](https://github.com/seu-usuario/projeto_etl_pncp.git)
    cd projeto_etl_pncp
    ```

2.  **Configurar Variáveis de Ambiente:**
    Crie um arquivo `.env` na raiz do projeto e adicione sua string de conexão do MongoDB:
    ```text
    MONGO_URI=mongodb+srv://<usuario>:<senha>@cluster.mongodb.net/
    ```

3.  **Instalar dependências:**
    ```bash
    pip install -r requirements.txt
    ```

## Como Executar
Para iniciar o processo de ETL, execute o script principal:
```bash
python src/main.py
```

## Estrutura do Repositório

```Plaintext
├── src/
│   ├── main.py          # Orquestrador do pipeline
│   ├── extractor.py     # Classe de extração (API)
│   ├── transformer.py   # Classe de transformação (Limpeza)
│   └── loader.py        # Classe de carga (MongoDB)
├── .env                 # Credenciais (não versionado)
├── .gitignore           # Filtro de arquivos para o Git
├── requirements.txt     # Dependências do projeto
└── README.md            # Documentação
```

## Grupo

* Ylson Santos