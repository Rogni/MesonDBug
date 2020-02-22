
CPP_TYPES = {
    'uint8': 'uint8_t',
    'string': 'std::string'
}

FILE_TEMPLATE='''
#ifndef {filename}_H
#define {filename}_H

#include <cstdint>
#include <string>

struct {typename} {{
{fields}
}};

#endif // {filename}_H
'''

def generate_field(field_obj) -> str:
    return '    {type} {name};\n'.format(
            type=CPP_TYPES.get(field_obj['type']), 
            name=field_obj['name']
        )

def generate_fields(fields_list, field_generator):
    return ''.join(field_generator(field) for field in fields_list)

def generator(obj) -> str:
    return FILE_TEMPLATE.format(
            filename=obj["type"].upper(),
            typename=obj["type"],
            fields=generate_fields(obj["fields"], generate_field)
        )
