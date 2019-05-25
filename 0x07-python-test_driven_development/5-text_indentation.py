#!/usr/bin/python3

"""Module text_identation

This Module you can pass a text how parameter and validate if this text
has some characters . ? : if the text found that the function do a space_line
and print the text in the next liene and the cahracteres too.

"""


def text_indentation(text):
    """Example function text identation

    Args:
        text: Unique parameter.

    Print:
        Print pharagraph.

    """
    i = 0
    if type(text) != str:
        raise TypeError('text must be a string')

    while i < len(text):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print('{}'.format(text[i]))
            print()
            i += 2
        print('{}'.format(text[i]), end='')
        i += 1
