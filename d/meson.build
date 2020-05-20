add_languages('d')

gen = generator(python,
                output  : '@BASENAME@.d',
                arguments : [ 
                    meson.source_root()/'gen.py', 
                    '@INPUT@', 
                    '@OUTPUT@',
                    'd'
                ])

gen_src = gen.process(meson.source_root()/'test_struct.json')

include_dir = include_directories('.')

executable('program', 
           ['main.d', gen_src]
           )