**Testes automatizados:** TDD com Python

**setUp** <br>
Cria os objetos utilizados pelos testes. Esse método é executado antes de cada teste, dessa forma, garante que um teste não influencia outro, já que sempre irá ter novos objetos.

[pytest](https://docs.pytest.org/en/7.0.x/)

<details>
    <summary><strong>Comandos</strong></summary>
    <br>
    <strong>Rodar o comando em cima da Classe para iniciar um teste:</strong>
    <pre>Ctrl + Shift + t</pre>
    <br>
    <strong>Rodar os testes pelo terminal:</strong>
    <pre>python -m unittest src/leilao/test_dominio.py</pre>
    <br>
    <strong>Renomear:</strong>
    <pre>Shift + F6</pre>
    <br>
    <strong>pytest</strong>
    <pre>pip install pytest</pre>
    <pre>pytest --version</pre>
    <pre>pytest</pre>
    <br>
    <strong>Rodar todos os testes:</strong>
    <pre>Ctrl + Shift + F10</pre>
</details>
