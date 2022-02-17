from src.leilao.dominio import Usuario, Leilao


def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance():
    lucas = Usuario('Lucas', 100.0)
    leilao = Leilao('Celular')

    lucas.propoe_lance(leilao, 50.0)
    assert lucas.carteira == 50.0
