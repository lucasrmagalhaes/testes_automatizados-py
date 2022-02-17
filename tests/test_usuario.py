from src.leilao.dominio import Usuario, Leilao

import pytest

from src.leilao.excecoes import LanceInvalido


@pytest.fixture
def lucas():
    return Usuario('Lucas', 100.0)


@pytest.fixture
def leilao():
    return Leilao('Celular')


def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance(lucas, leilao):
    lucas.propoe_lance(leilao, 50.0)
    assert lucas.carteira == 50.0


def test_deve_permitir_propor_lance_quando_o_valor_eh_menor_que_o_valor_da_carteira(lucas, leilao):
    lucas.propoe_lance(leilao, 1.0)
    assert lucas.carteira == 99.0


def test_deve_permitir_propor_lance_quando_o_valor_eh_igual_ao_valor_da_carteira(lucas, leilao):
    lucas.propoe_lance(leilao, 100.0)
    assert lucas.carteira == 0.0


def test_nao_deve_permitir_propor_lance_com_valor_maior_que_o_da_carteira(lucas, leilao):
    with pytest.raises(LanceInvalido):
        lucas.propoe_lance(leilao, 200.0)
