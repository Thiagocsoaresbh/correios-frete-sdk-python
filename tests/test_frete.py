from correios_frete_sdk import calcular_frete

def test_calculo_frete_valido():
    resultado = calcular_frete("30140-071", "01310-100", 1.0, "SEDEX")
    assert "Valor" in resultado
    assert "PrazoEntrega" in resultado

def test_servico_invalido():
    try:
        calcular_frete("30140-071", "01310-100", 1.0, "EXPRESSO")
    except ValueError as e:
        assert "não suportado" in str(e)
