project('RaceBugTest','c')
lang = 'vala'
add_languages(lang)
python = import('python').find_installation('python3')

header_suffixes = {
    'cpp': 'h',
    'd': 'd',
    'vala': 'vala'
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

if lang == 'vala'
    add_project_arguments('--profile=posix', language:'vala')
    add_languages('c')
endif

executable('program', 
           [lang / 'main.' + lang, gen_src]
           )