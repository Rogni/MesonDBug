add_languages('c','vala')

gen = generator(python,
                output  : '@BASENAME@.vala',
                arguments : [ 
                    meson.source_root()/'gen.py', 
                    '@INPUT@', 
                    '@OUTPUT@',
                    'vala'
                ])

gen_src = gen.process(meson.source_root()/'test_struct.json')

include_dir = include_directories('.')

executable('program', 
           ['main.vala', gen_src],
           vala_args:'--profile=posix'
           )