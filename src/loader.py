import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

class PNCPLoader:
    """
    Classe responsável por carregar os dados no MongoDB Atlas.
    """

    def __init__(self):
        self.uri = os.getenv("MONGO_URI")
        self.db_name = "projeto_pncp"
        self.collection_name = "contratacoes"

    def salvar_no_mongo(self, dados_tratados):
        """
        Insere os documentos no MongoDB.

        Args:
            dados_tratados (list): Lista de dicionários prontos para inserção.
        """
        if not dados_tratados:
            return

        try:
            # Adicionado tls=True para garantir conexão segura com o Atlas
            client = MongoClient(self.uri, tls=True)
            db = client[self.db_name]
            collection = db[self.collection_name]
            collection.insert_many(dados_tratados)
            client.close()
            print(f"Sucesso: {len(dados_tratados)} registros inseridos.")
        except Exception as e:
            print(f"Erro: {e}")