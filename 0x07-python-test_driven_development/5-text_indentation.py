#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for a in ['.', '?', ':']:
        text = text.replace(a, a + '\n''\n')
    print(text)
