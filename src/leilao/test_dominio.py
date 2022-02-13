from unittest import TestCase

from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador


class TestAvaliador(TestCase):

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        lucas = Usuario('Lucas')
        fulano = Usuario('Fulano')

        lance_do_lucas = Lance(lucas, 100.0)
        lance_do_fulano = Lance(fulano, 150.0)

        leilao = Leilao('Celular')

        leilao.lances.append(lance_do_lucas)
        leilao.lances.append(lance_do_fulano)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_descrescente(self):
        lucas = Usuario('Lucas')
        fulano = Usuario('Fulano')

        lance_do_lucas = Lance(lucas, 100.0)
        lance_do_fulano = Lance(fulano, 150.0)

        leilao = Leilao('Celular')

        leilao.lances.append(lance_do_fulano)
        leilao.lances.append(lance_do_lucas)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)
