import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory():
    def read_csv(path):
        result = []
        with open(path, "r") as file:
            file_csv = csv.DictReader(file)

            for item in file_csv:
                result.append(item)

        return result

    def read_json(path):
        with open(path) as file:
            file_json = json.load(file)
            return file_json

    def read_xml(path):
        with open(path, encoding="utf-8") as file:
            file_xml = file.read()
            file_read = xmltodict.parse(file_xml)['dataset']
            print(file_read)
            return file_read['record']

    def import_data(path, type):
        data = []
        if path.endswith('.csv'):
            data = Inventory.read_csv(path)
        if path.endswith('.json'):
            data = Inventory.read_json(path)
        if path.endswith('.xml'):
            data = Inventory.read_xml(path)

        if type == 'simples':
            return SimpleReport.generate(data)
        else:
            return CompleteReport.generate(data)
