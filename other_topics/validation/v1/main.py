import json
from cerberus import Validator

# Data
dict_a: dict = {
    'name': 'Gabriel'
}

dict_b: dict = {
    'name': 'Gabriel',
    'age': 18
}

dict_c: dict = {
    'name': 'Gabriel',
    'teams': [
        'Palmeiras',
        'Miami Heat',
        'Seattle Seahawks',
        1
    ]
}

# Schemas
schema_a: dict = {
    'name': {
        'type': 'string',
        'maxlength': 10
    }
}

schema_b: dict = {
    'age': {
        'type': 'integer',
        'min': 18
    }
}

schema_c: dict = {
    'name': {
        'type': 'string',
        'maxlength': 10
    },
    'teams': {
        'type': 'list',
        'maxlength': 2,
        'schema': {
            'type': 'string',
        }
    }
}


def check(schema_validator, data_name, data, schema):
    print(f'\nValidating data [{data_name}]...')

    if schema_validator.validate(data, schema):
        print(f'Data [{data_name}] is valid!')
    else:
        print(f'Data [{data_name}] is not valid!')
        print(json.dumps(schema_validator.errors, indent=4))


if __name__ == '__main__':
    validator = Validator()

    check(validator, 'A', dict_a, schema_a)
    check(validator, 'B', dict_b, schema_b)
    check(validator, 'C', dict_c, schema_c)
