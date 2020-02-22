project('RaceBugTest')
lang = 'd'
add_languages(lang)
python = import('python').find_installation('python3')

header_suffixes = {
    'cpp': 'h',
    'd': 'd'
}

gen = generator(python,
                output  : '@BASENAME@.' + header_suffixes[lang],
                arguments : [ 
                    meson.current_source_dir()/'gen.py', 
                    '@INPUT@', 
                    '@OUTPUT@',
                    lang
                ])

gen_src = gen.process('test_struct.json')

include_dir = include_directories('.')

executable('program', 
           [lang / 'main.' + lang, gen_src]
           )