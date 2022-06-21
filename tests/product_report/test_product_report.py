from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        12345002,
        'Mouse',
        'logitech',
        '01/01/2020',
        '01/01/2050',
        987654321,
        'em um lugar seguro',
        )

    result = product.__repr__()

    assert type(result) == str
    assert result == (
        "O produto Mouse "
        "fabricado em 01/01/2020 "
        "por logitech com validade "
        "até 01/01/2050 "
        "precisa ser armazenado em um lugar seguro."
    )
