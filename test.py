import unittest
import soma

class TestSum(unittest.TestCase):

    def test_soma_correta(self):
        """
        Testa a função soma com resultado correto
        """
        resultado = soma.soma()
        self.assertEqual(resultado, 7)

    def teste_soma_errada(self):
        """
        Testa a função de soma com resultado errado
        """
        resultado = soma.soma()
        self.assertNotEqual(resultado, 10)
