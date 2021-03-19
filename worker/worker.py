import os
from m2r import parse_from_file
from pipeit import *

main_dir = os.path.abspath('../')
dst_dir = os.path.abspath('../docs/source/content')
index_dir = os.path.abspath('../docs/source')

for files in os.walk(main_dir):
    files = files[2] ; break
files = files | Filter(lambda x:os.path.splitext(x)[1] == '.md') | list

def post_flt_string(string):
    string = string.replace('\r\n','\n')
    string = string.split('\n')
    for index , line in enumerate(string):
        if len(line) > 2:
            if line[0] not in ['.',':',' ','\t']:
                title = line.strip()
                break
    string = string[index:]
    string_head = [f'.. _{title}:','',f'{(len(title)*2 + 1) * "*"}' , title , f'{(len(title)*2 + 1) * "*"}','']
    string_head.extend(string)
    string = string_head | Map(lambda x:x+'\n') | list
    return string

for file_name in files:
    src_dir = os.path.join(main_dir , file_name)
    to_dir = os.path.join(dst_dir , os.path.splitext(file_name)[0] + '.rst')

    output = parse_from_file(src_dir)
    with open(to_dir,'w',encoding='utf-8') as f:
        f.writelines(post_flt_string(output))

# 清理过期文件
names = files | Map(lambda x:os.path.splitext(x)[0]) | set
for dst_files in os.walk(dst_dir):
    dst_files = dst_files[2] ; break

dst_names = dst_files | Map(lambda x:os.path.splitext(x)[0]) | set
for file_name in dst_files:
    if os.path.splitext(file_name)[0] in (dst_names - names):
        os.remove(os.path.join(dst_dir , file_name))

for dst_files in os.walk(dst_dir):
    dst_files = dst_files[2] ; break
dst_files = dst_files | Filter(lambda x:os.path.splitext(x)[1] == '.rst') | list
dst_files.sort()

# index.rst
with open(os.path.join(index_dir , 'index.rst'),'r',encoding='utf-8') as f:
    cont = f.read()

cont = cont.replace('\r\n','\n').split('\n')
st , ed = 0 , 0
for index , line in enumerate(cont):
    if line.strip() == '.. toctree::':
        st = index + 2
    if line.strip() == 'Indices and tables':
        ed = index
cont_t = cont[:st]
cont_t.append('')
cont_t.extend([f'    content/{file_name}' for file_name in dst_files])
cont_t.append('')
cont_t.extend(cont[ed:])
cont_t = cont_t | Map(lambda x:x+'\n') | list
with open(os.path.join(index_dir , 'index.rst'),'w',encoding='utf-8') as f:
    f.writelines(cont_t)