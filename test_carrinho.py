import unittest

from carrinho import CarrinhoDeCompras


class TestCarrinhoDeCompras(unittest.TestCase):
    def criar_carrinho_com_total(self, total: float) -> CarrinhoDeCompras:
        carrinho = CarrinhoDeCompras()
        carrinho.adicionar_item("Produto", total)
        return carrinho

    def test_compra_sem_desconto_com_frete(self):
        carrinho = self.criar_carrinho_com_total(50.00)

        self.assertEqual(carrinho.calcular_desconto(), 0.0)
        self.assertEqual(carrinho.calcular_frete(), 20.0)
        self.assertEqual(carrinho.calcular_total_final(), 70.0)

    def test_desconto_de_10_porcento_a_partir_de_100(self):
        with self.subTest(total=99.99):
            carrinho = self.criar_carrinho_com_total(99.99)
            self.assertEqual(carrinho.calcular_desconto(), 0.0)

        with self.subTest(total=100.00):
            carrinho = self.criar_carrinho_com_total(100.00)
            self.assertAlmostEqual(carrinho.calcular_desconto(), 10.00)

    def test_desconto_de_20_porcento_a_partir_de_500(self):
        with self.subTest(total=499.99):
            carrinho = self.criar_carrinho_com_total(499.99)
            self.assertAlmostEqual(carrinho.calcular_desconto(), 49.999)

        with self.subTest(total=500.00):
            carrinho = self.criar_carrinho_com_total(500.00)
            self.assertAlmostEqual(carrinho.calcular_desconto(), 100.00)

    def test_frete_gratis_a_partir_de_200(self):
        with self.subTest(total=199.99):
            carrinho = self.criar_carrinho_com_total(199.99)
            self.assertEqual(carrinho.calcular_frete(), 20.0)

        with self.subTest(total=200.00):
            carrinho = self.criar_carrinho_com_total(200.00)
            self.assertEqual(carrinho.calcular_frete(), 0.0)

    def test_preco_negativo_lanca_value_error(self):
        carrinho = CarrinhoDeCompras()

        with self.assertRaises(ValueError):
            carrinho.adicionar_item("Produto inválido", -0.01)

    def test_preco_nulo_lanca_value_error(self):
        carrinho = CarrinhoDeCompras()

        with self.assertRaises(ValueError):
            carrinho.adicionar_item("Produto sem preço", None)

    def test_checkout_de_carrinho_vazio_lanca_value_error(self):
        carrinho = CarrinhoDeCompras()

        with self.assertRaises(ValueError):
            carrinho.calcular_total_final()


if __name__ == "__main__":
    unittest.main(verbosity=2)