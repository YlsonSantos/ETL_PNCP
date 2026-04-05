import requests

class PNCPExtractor:
    """
    Classe responsável pela extração de dados da API do PNCP.
    """

    def __init__(self):
        self.base_url = "https://pncp.gov.br/api/pncp/v1/contratacoes"

    def extrair_contratacoes(self, data_consulta, pagina=1):
        """
        Realiza a chamada GET para a API do PNCP.

        Args:
            data_consulta (str): Data no formato AAAAMMDD.
            pagina (int): Número da página.

        Returns:
            dict: Dados brutos ou None.
        """
        params = {
            "data": data_consulta,
            "pagina": pagina,
            "tamanhoPagina": 10
        }
        
        try:
            response = requests.get(self.base_url, params=params, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return None