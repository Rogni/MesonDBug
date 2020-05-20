add_languages('rust')

gen = generator(python,
                output  : '@BASENAME@.rs',
                arguments : [ 
                    meson.source_root()/'gen.py', 
                    '@INPUT@', 
                    '@OUTPUT@',
                    'rs'
                ])

gen_src = gen.process(meson.source_root()/'test_struct.json')

include_dir = include_directories('.')

executable('program', 
           ['main.rs', gen_src]
           )