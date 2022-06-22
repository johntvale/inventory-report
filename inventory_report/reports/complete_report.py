from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def products_in_stock(list):
        aux_product_list = []
        for item in list:
            aux_product_list.append(item['nome_da_empresa'])
        product_per_company = Counter(aux_product_list).most_common(10)
        return product_per_company

    def generate(list):
        stock_list = CompleteReport.products_in_stock(list)
        generated_report = (
            f"{SimpleReport.generate(list)}\n"
            f"Produtos estocados por empresa:\n"
        )
        for item in stock_list:
            generated_report += f"- {item[0]}: {item[1]}\n"

        return generated_report
