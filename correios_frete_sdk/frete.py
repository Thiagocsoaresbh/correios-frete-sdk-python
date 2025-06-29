from typing import Dict
import requests
from xml.etree import ElementTree
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

BASE_URL = "http://ws.correios.com.br/calculador/CalcPrecoPrazo.aspx"

SERVICOS = {
    "PAC": "04510",
    "SEDEX": "04014"
}

def get_session() -> requests.Session:
    session = requests.Session()
    retry = Retry(total=3, backoff_factor=0.5) 
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    return session

def calcular_frete(cep_origem: str, cep_destino: str, peso: float, servico: str = "SEDEX") -> Dict[str, str]:
    if servico not in SERVICOS:
        raise ValueError(f"Serviço '{servico}' não suportado. Use: {list(SERVICOS.keys())}")

    params = {
        "nCdEmpresa": "",
        "sDsSenha": "",
        "nCdServico": SERVICOS[servico],
        "sCepOrigem": cep_origem,
        "sCepDestino": cep_destino,
        "nVlPeso": str(peso),
        "nCdFormato": "1",
        "nVlComprimento": "20.0",
        "nVlAltura": "5.0",
        "nVlLargura": "15.0",
        "nVlDiametro": "0.0",
        "sCdMaoPropria": "N",
        "nVlValorDeclarado": "0.0",
        "sCdAvisoRecebimento": "N",
        "StrRetorno": "xml"
    }

    session = get_session()
    try:
        response = session.get(BASE_URL, params=params, timeout=(3, 10))
        response.encoding = 'utf-8'
    except requests.exceptions.RequestException as e:
        print(f"[ERRO] Não foi possível se conectar aos Correios: {e}")
        return {}

    root = ElementTree.fromstring(response.content)
    resultado: Dict[str, str] = {}
    for child in root.iter():
        resultado[child.tag] = child.text or ""

    return resultado
