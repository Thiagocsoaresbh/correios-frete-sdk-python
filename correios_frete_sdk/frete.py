from typing import Dict
import requests
from xml.etree import ElementTree

BASE_URL = "http://ws.correios.com.br/calculador/CalcPrecoPrazo.aspx"

SERVICOS = {
    "PAC": "04510",
    "SEDEX": "04014"
}

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

    response = requests.get(BASE_URL, params=params)
    response.encoding = 'utf-8'

    root = ElementTree.fromstring(response.content)
    resultado: Dict[str, str] = {}
    for child in root.iter():
        resultado[child.tag] = child.text or ""

    return resultado
