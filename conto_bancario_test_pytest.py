import pytest

from conto_bancario import ContoBancario

# pip freeze > requirements.txt crea file requisiti
# mkdir -p .github/workflows    creare cartella workflows che testa prima di pushare

@pytest.fixture #decoratore
def test_conto():
    return ContoBancario("Mario Rossi", 100)


def test_creazione_conto(conto):
    # self.assertEqual(self.conto.nome, "Mario Rossi")
    # self.assertEqual(self.conto.saldo, 100)

    assert conto.nome == "Mario Rossi"
    assert conto.saldo == 100

def test_deposita_conto(conto):
    # self.conto.deposita(50)
    # self.assertEqual(self.conto.saldo, 150)

    conto.deposita(50)
    assert conto.saldo == 150

def test_deposito_negativo(conto):

    # with self.assertRaises(ValueError):
    #     self.conto.deposita(-20)
    # self.assertEqual(self.conto.saldo, 100)

    with pytest.raises(ValueError):
        conto.deposita(-20)

    assert conto.saldo == 100
