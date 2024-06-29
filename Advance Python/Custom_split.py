def custom_split(s, delimiter=None):
    if delimiter is None:
        delimiter = ' '

    word = []
    l = len(s)
    i = 0

    while i < l:
        if delimiter == ' ':
            if s[i].isspace():
                if word:
                    yield ''.join(word)
                    word = []
            else:
                word.append(s[i])
            i += 1
        else:
            if s[i:i+len(delimiter)] == delimiter:
                if word:
                    yield ''.join(word)
                    word = []
                i += len(delimiter)
            else:
                word.append(s[i])
                i += 1

    if word:
        yield ''.join(word)


test_string = "This is a test, string"
print(list(custom_split(test_string))) 
