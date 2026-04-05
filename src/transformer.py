class PNCPTransformer:
    """
    Classe responsável pelo tratamento e transformação dos dados brutos.
    """

    def tratar_dados(self, dados_brutos):
        """
        Transforma a lista de contratações filtrando campos essenciais.

        Args:
            dados_brutos (dict): Resposta original da API.

        Returns:
            list: Lista de dicionários filtrados.
        """
        if not dados_brutos or 'data' not in dados_brutos:
            return []

        dados_limpos = []
        
        for item in dados_brutos['data']:
            registro = {
                "numero_controle": item.get("numeroControlePNCP"),
                "orgao": item.get("orgaoEntidade", {}).get("razaoSocial"),
                "cnpj_orgao": item.get("orgaoEntidade", {}).get("cnpj"),
                "objeto": item.get("objeto"),
                "valor_total": item.get("valorTotalEstimado"),
                "data_publicacao": item.get("dataPublicacaoPncp"),
                "situacao": item.get("situacaoContratacaoNome")
            }
            dados_limpos.append(registro)
            
        return dados_limpos