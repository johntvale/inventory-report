from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        12345001,
        'notebook',
        'dell',
        '01/01/2022',
        '01/01/2030',
        123456789,
        'instrucoes de armazenamento',
        )

    assert product.id == 12345001
    assert product.nome_do_produto == 'notebook'
    assert product.nome_da_empresa == 'dell'
    assert product.data_de_fabricacao == '01/01/2022'
    assert product.data_de_validade == '01/01/2030'
    assert product.numero_de_serie == 123456789
    assert product.instrucoes_de_armazenamento == 'instrucoes de armazenamento'
