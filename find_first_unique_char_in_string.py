def get_first_unique_char(s):
    frequency = {}
    for i in s:
        if i not in frequency:
            frequency[i] = 1
        else:
            frequency[i] += 1
    for i in range(len(s)):
        if frequency[s[i]] == 1:
            return i+1
    return -1


if __name__ == '__main__':
    s = 'falafalllllllllllllllssr'
    print(get_first_unique_char(s))