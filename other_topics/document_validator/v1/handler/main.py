import json

from validate_docbr import CPF, CNPJ

cpf = CPF()
cnpj = CNPJ()


def validate_cpf(doc: str) -> bool:
    return cpf.validate(doc)


def validate_cnpj(doc: str) -> bool:
    return cnpj.validate(doc)


if __name__ == '__main__':
    # Document Validator - v1
    # Validating, Generating and Masking CPFs and CNPJs

    doc = cpf.generate()
    print(f'\nGenerated CPF [{doc}]')
    print(f'Is this CPF valid? [{validate_cpf(doc)}]')
    print(f'Masking it now: [{cpf.mask(doc)}]\n')

    list_length = 5
    doc_list = cpf.generate_list(n=list_length, mask=True, repeat=False)
    print(f'Generated a list of [{list_length}] CPFs')
    print(json.dumps(doc_list, indent=4))
    print("---------- | ---------- | ----------\n")

    doc = cnpj.generate()
    print(f'Generated CNPJ [{doc}]')
    print(f'Is this CNPJ valid? [{validate_cnpj(doc)}]')
    print(f'Masking it now: [{cnpj.mask(doc)}]\n')

    doc_list = cnpj.generate_list(n=list_length, mask=True, repeat=False)
    print(f'Generated a list of [{list_length}] CNPJs')
    print(json.dumps(doc_list, indent=4))
    print("---------- | ---------- | ----------\n")

    print("And it also works for: "
          "CNH, Renavam, PIS, CNS, Titulo Eleitoral and Certidões de Nascimento, Casamento e Óbito")
