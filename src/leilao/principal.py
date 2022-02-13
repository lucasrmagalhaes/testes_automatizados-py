from src.leilao.dominio import Usuario, Lance, Leilao

lucas = Usuario('Lucas')
fulano = Usuario('Fulano')

lance_do_lucas = Lance(lucas, 100.0)
lance_do_fulano = Lance(fulano, 150.0)

leilao = Leilao('Celular')

leilao.lances.append(lance_do_lucas)
leilao.lances.append(lance_do_fulano)

for lance in leilao.lances:
    print(f'O usuário {lance.usuario.nome} deu um lance de {lance.valor}')