from src.extractor import PNCPExtractor
from src.transformer import PNCPTransformer
from src.loader import PNCPLoader

def executar_pipeline():
    """
    Orquestra o fluxo ETL.
    """
    extrator = PNCPExtractor()
    dados_brutos = extrator.extrair_contratacoes(data_consulta="20240320")
    
    transformador = PNCPTransformer()
    dados_limpos = transformador.tratar_dados(dados_brutos)
    
    carregador = PNCPLoader()
    carregador.salvar_no_mongo(dados_limpos)

if __name__ == "__main__":
    executar_pipeline()