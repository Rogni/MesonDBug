VALA_TYPES={
    'uint8': 'uint8',
    'string': 'string'
}

FILE_TEMPLATE = '''
struct {typename} {{
    {fields}
}}
'''

def generate_field(field_obj) -> str:
    return '    {type} {name};\n'.format(
            type=VALA_TYPES.get(field_obj['type']), 
            name=field_obj['name']
        )

def generate_fields(fields_list, field_generator):
    return ''.join(field_generator(field) for field in fields_list)

def generator(obj) -> str:
    return FILE_TEMPLATE.format(
            filename=obj["type"],
            typename=obj["type"],
            fields=generate_fields(obj["fields"], generate_field)
        )