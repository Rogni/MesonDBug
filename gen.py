'''Generate test cpp files'''

import argparse
import json
import time
from cpp.cpp import generator as cpp_gen
from d.d import generator as d_gen

GENERATORS = {
    'd': d_gen,
    'cpp': cpp_gen
}


def generate_source(input_path, output_path, generator):
    time.sleep(1)
    with open(input_path, 'r') as input_file:
        with open(output_path, 'w') as output_file:
            output_file.write(
                generator(
                        json.load(input_file)
                    )
                )


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('input_path')
    parser.add_argument('output_path')
    parser.add_argument('lang')
    args = parser.parse_args()
    
    generate_source(args.input_path, args.output_path, GENERATORS[args.lang])

