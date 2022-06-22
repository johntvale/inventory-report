from collections import Counter


class SimpleReport():

    def oldest_manufacturing_date(list):
        aux_list_date = []
        for product in list:
            aux_list_date.append(product['data_de_fabricacao'])
        return min(aux_list_date)

    def closest_expiration_date(list):
        aux_list_date = []
        for product in list:
            aux_list_date.append(product['data_de_validade'])
        return min(aux_list_date)

    def largest_amount_of_product(list):
        aux_list_companies = []
        for product in list:
            aux_list_companies.append(product['nome_da_empresa'])
        company_name = Counter(aux_list_companies).most_common(1)[0][0]
        return company_name

    def generate(list):
        oldest_date = SimpleReport.oldest_manufacturing_date(list)
        expiration_date = SimpleReport.closest_expiration_date(list)
        company_name = SimpleReport.largest_amount_of_product(list)
        return (
          f"Data de fabricação mais antiga: {oldest_date}\n"
          f"Data de validade mais próxima: {expiration_date}\n"
          f"Empresa com mais produtos: {company_name}"
        )
