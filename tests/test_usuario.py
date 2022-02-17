from src.leilao.dominio import Usuario, Leilao


def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance():
    lucas = Usuario('Lucas', 100.0)
    leilao = Leilao('Celular')

    lucas.propoe_lance(leilao, 50.0)

    assert lucas.carteira == 50.0


def test_deve_permitir_propor_lance_quando_o_valor_eh_menor_que_o_valor_da_carteira():
    lucas = Usuario('Lucas', 100.0)
    leilao = Leilao('Celular')

    lucas.propoe_lance(leilao, 1.0)

    assert lucas.carteira == 99.0


def test_deve_permitir_propor_lance_quando_o_valor_eh_igual_ao_valor_da_carteira():
    lucas = Usuario('Lucas', 100.0)
    leilao = Leilao('Celular')

    lucas.propoe_lance(leilao, 100.0)

    assert lucas.carteira == 0.0


def test_nao_deve_permitir_propor_lance_com_valor_maior_que_o_da_carteira():
    lucas = Usuario('Lucas', 100.0)
    leilao = Leilao('Celular')

    lucas.propoe_lance(leilao, 200.0)

    assert lucas.carteira == 100.0
