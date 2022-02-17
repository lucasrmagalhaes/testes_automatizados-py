**Testes automatizados:** TDD com Python

**setUp** <br>
Cria os objetos utilizados pelos testes. Esse método é executado antes de cada teste, dessa forma, garante que um teste não influencia outro, já que sempre irá ter novos objetos.

[pytest](https://docs.pytest.org/en/7.0.x/)

<details>
    <summary>Comandos</summary>
    <br>
    Rodar o comando em cima da Classe para iniciar um teste:
    <pre>Ctrl + Shift + t</pre>
    Rodar os testes pelo terminal:
    <pre>python -m unittest src/leilao/test_dominio.py</pre>
    Renomear:
    <pre>Shift + F6</pre>
    <br>
    pytest
    <pre>pip install pytest</pre>
    <pre>pytest --version</pre>
</details>
