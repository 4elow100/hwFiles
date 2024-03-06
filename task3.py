files = []


def read_from_file(filename):
    info = {}
    with open(filename, encoding='UTF-8') as f:
        info['Name'] = filename[-5::]
        info['Count of lines'] = len(f.readlines())
    with open(filename, encoding='UTF-8') as f:
        info['Text'] = f.read().replace("\ufeff", '')
    return info


def get_count(filename):
    return filename.get('Count of lines')


def write_to_file(filename, info):
    with open(filename, 'w', encoding='UTF') as f:
        final_text = ''
        for i in range(len(info)):
            final_text = final_text + (f'{info[i]["Name"]}\n'
                                       f'{info[i]["Count of lines"]}\n'
                                       f'{info[i]["Text"]}\n')
        f.write(final_text)


files.append(read_from_file('task3/1.txt'))
files.append(read_from_file('task3/2.txt'))
files.append(read_from_file('task3/3.txt'))
files_sorted = sorted(files, key=get_count)
write_to_file('task3/result.txt', files_sorted)
