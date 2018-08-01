from collections import Counter

from perfil.person.models import Person
from perfil.utils.management.commands import ImportCsvCommand
from perfil.utils.tools import probably_same_entity


class Command(ImportCsvCommand):

    help = "Import CSV generated by: https://brasil.io/dataset/eleicoes-brasil/candidatos"  # noqa
    model = Person
    bulk_size = 2 ** 13

    @staticmethod
    def group_names_by_cpf(reader):
        grouped = {}
        for line in reader:
            cpf, name = line['cpf_candidato'], line['nome_candidato']
            names = grouped.get(cpf, set())
            names.add(name)
            grouped[cpf] = names

        return grouped

    def serialize(self, reader):
        print('Cleaning the dataset…')
        data = self.group_names_by_cpf(reader)

        print('Importing data…')
        for cpf, names in data.items():
            if len(names) == 1 or probably_same_entity(names):
                *_, name = names  # last should be the most recent one
                yield Person(civil_name=name, cpf=cpf)
