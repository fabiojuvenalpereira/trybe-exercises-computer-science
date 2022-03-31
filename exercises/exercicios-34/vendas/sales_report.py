from abc import ABC, abstractmethod
from csv import DictWriter
import gzip
import json
from zipfile import ZipFile


class Serializer(ABC):
    @abstractmethod
    def serialize(cls, data):
        raise NotImplementedError


class ZipCompressor(Serializer):
    FILE_PATH = 'exercises/exercicios-34/sales-report/'

    @classmethod
    def compress(cls, file_name):
        with ZipFile(cls.FILE_PATH + file_name + '.zip', 'w') as zip_file:
            zip_file.write(file_name)


class GzCompressor(Serializer):
    @staticmethod
    def compress(file_name):
        with open(file_name, 'rb') as content:
            with gzip.open(file_name + '.gz', 'wb') as gzip_file:
                gzip_file.writelines(content)

class SalesReport(ABC):
    FILE_EXTENSION = ''

    def __init__(self, export_file, compressor=GzCompressor):
        self.export_file = export_file
        self.compressor = compressor

    def build(self):
        return [{
                'Coluna 1': 'Dado 1',
                'Coluna 2': 'Dado 2',
                'Coluna 3': 'Dado 3'
                },
                {
                'Coluna 1': 'Dado A',
                'Coluna 2': 'Dado B',
                'Coluna 3': 'Dado C'
                }]

    def get_export_file_name(self):
      return self.export_file + self.FILE_EXTENSION

    def compress(self):
        self.serialize()
        self.compressor.compress(self.get_export_file_name())


class SalesReportJSON(SalesReport):
    FILE_EXTENSION = '.json'

    def serialize(self):
        with open(self.export_file + '.json', 'w') as file:
            json.dump(self.build(), file)


class SalesReportCSV(SalesReport):
     def serialize(self):
         with open(f"exercises/exercicios-34/sales-report/{self.export_file}" + '.csv', 'w') as file:
            headers = ["Coluna 1", "Coluna 2", "Coluna 3"]
            csv_writer = DictWriter(file, headers)
            csv_writer.writeheader()
            for item in self.build():
                csv_writer.writerow(item)


relatorio_de_compras = SalesReportJSON('meu_relatorio_1')
relatorio_de_vendas = SalesReportJSON('meu_relatorio_2', ZipCompressor)

relatorio_de_compras.compress()
relatorio_de_vendas.compress()
