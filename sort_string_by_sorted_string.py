def sorted_string(string: str):
    return ''.join(sorted(string))


if __name__ == '__main__':
    data = ['yo', 'asd', 'ads', 'fds', 'oy', 'sda', 'ssdaa', 'oy', 'fds']
    dict_words = dict()
    out = []
    for ind, item in enumerate(data):
        dict_words.setdefault(sorted_string(item), []).append(item)  # by name
        # dict_words.setdefault(sorted_string(item), []).append(ind)  # by index
    print(dict_words)
    for values in dict_words.values():
        out.append(values)
    print(out)
