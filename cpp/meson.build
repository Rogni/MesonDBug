add_languages('cpp')

gen = generator(python,
                output  : '@BASENAME@.h',
                arguments : [ 
                    meson.source_root()/'gen.py', 
                    '@INPUT@', 
                    '@OUTPUT@',
                    'cpp'
                ])

gen_src = gen.process(meson.source_root()/'test_struct.json')

include_dir = include_directories('.')

executable('program', 
           ['main.cpp', gen_src]
           )