import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory():
    def read_csv(path):
        result = []
        with open(path, "r") as file:
            file_csv = csv.DictReader(file, delimiter=",")

            for item in file_csv:
                result.append(item)

        return result

    def import_data(path, type):
        data = Inventory.read_csv(path)
        if type == 'simples':
            return SimpleReport.generate(data)
        if type == 'completo':
            return CompleteReport.generate(data)
