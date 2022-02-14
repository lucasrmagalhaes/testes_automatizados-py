from unittest import TestCase

from src.leilao.dominio import Usuario, Lance, Leilao


class TestAvaliador(TestCase):

    def setUp(self):
        self.lucas = Usuario('Lucas')
        self.lance_do_lucas = Lance(self.lucas, 100.0)

        self.leilao = Leilao('Celular')

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        fulano = Usuario('Fulano')
        lance_do_fulano = Lance(fulano, 150.0)

        self.leilao.propoe(self.lance_do_lucas)
        self.leilao.propoe(lance_do_fulano)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_descrescente(self):
        fulano = Usuario('Fulano')
        lance_do_fulano = Lance(fulano, 150.0)

        self.leilao.propoe(lance_do_fulano)
        self.leilao.propoe(self.lance_do_lucas)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_leilao_tiver_um_lance(self):
        fulano = Usuario('Fulano')
        lance_do_fulano = Lance(fulano, 150.0)

        self.leilao.propoe(lance_do_fulano)

        self.assertEqual(150.0, self.leilao.menor_lance)
        self.assertEqual(150.0, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):
        fulano = Usuario('Fulano')
        beltrano = Usuario('Beltrano')

        lance_do_fulano = Lance(fulano, 150.0)
        lance_do_beltrano = Lance(beltrano, 200.0)

        self.leilao.propoe(self.lance_do_lucas)
        self.leilao.propoe(lance_do_fulano)
        self.leilao.propoe(lance_do_beltrano)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)
