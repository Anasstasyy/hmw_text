import os
import os.path


def string_count(file):
    with open(file, 'r', encoding = 'utf-8') as f:
        return sum(1 for line in f)

def filewriting (file_write: str, base_path, location):
    files = []
    for i in list(os.listdir(os.path.join(base_path, location))):
        files.append([string_count(os.path.join(base_path, location, i)), os.path.join(base_path, location, i), i])
        for file_write in sorted(files):
            open_f = open (file_write, 'a', encoding = 'utf-8')
            open_f.write(f'{file_write[2]}\n')
            open_f.write(f'{file_write[0]}\n')
            with open(file[1], 'r', encoding = 'utf-8') as file:
                count =1
                for line in file:
                    open_f.write(f'строка № {count} в файле {file_write[2]}: {line}')
                    count +=1
                    open_f.write(f'\n')
                    open_f.close()


        
        