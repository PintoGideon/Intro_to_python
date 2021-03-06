import os
import collections

SearchResult = collections.namedtuple('SeachResult', 'file, line, text')


def main():
    print_header()
    folder = get_folder_from_user()
    if not folder:
        print("Sorry we can't search that location")
        return

    text = get_search_text_from_user()
    if not text:
        print("We can't search for nothing")
        return

    matches = search_folders(folder, text)
    match_count = 0
    for m in matches:
        match_count += 1
        print('------------Match-------------')
        print('File:'+m.file)
        print('Line: {}'.format(m.line))
        print('match: '+m.text.strip())
        print()


def print_header():
    print('-------------------------------')
    print('        File Search App          ')
    print('------------------------------------')


def get_folder_from_user():
    folder = input("What folder do you want to search?")
    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


def get_search_text_from_user():
    text = input("What are you searching for? [single phrases only]")


def search_folders(folder, text):

    #all_matches = []
    items = os.listdir(folder)

    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            # searching sub folders
            # Recursively search the subtree of the parent directory
            matches = search_folders(full_item, text)
            # all_matches.extend(matches)
            yield from matches
        else:
            matches = search_file(full_item, text)
            # all_matches.extend(matches)
            yield from matches

    # return all_matches


def search_file(filename, search_text):
    #matches = []
    with open(filename, 'r', encoding='utf-8') as fin:

        line_num = 0
        for line in fin:
            line_num += 1
            if line.lower().find(search_text) >= 0:
                m = SearchResult(file=filename, line=line_num, text=line)
                yield m
                # matches.append(m)
       # return matches


if __name__ == '__main__':
    main()
