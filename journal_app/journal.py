import os


def load(name):
    # todo: populate from file if it exists
    """
    :param_name: The base name of the journal to load
    :return: A new journal data structure populated with the file data
    """
    data = []
    filename = get_full_pathname(name)

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())
    return data


def save(name, journal_data):
    filename = os.path.abspath(os.path.join('./journal/journals', name+'.jrl'))
    print('.....Saving to file'.format(filename))

    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry+'\n')


def get_full_pathname(name):
    filename = os.path.abspath(os.path.join('./journal/journals', name+'.jrl'))
    return filename


def add_entry(text, journal_data):
    return journal_data.append(text)
