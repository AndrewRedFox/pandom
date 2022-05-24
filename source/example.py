import fileinput
from panflute import *
from sys import stderr

ListOfHeaders = []

def Bold(document):
    document.replace_keyword("BOLD", Strong(Str("BOLD")))

def HeaderRepeat(element, document):
    if isinstance(element, Header):
        text = stringify (element)
        if text in ListOfHeaders:
            print ("Пристуствуют повторные заголовки: " + text, file = stderr)
        else:
            ListOfHeaders.append(text)

def HeaderLevel(element, document):
    if isinstance(element, Header) and element.level > 2:
        return Header(Str(stringify(element).upper()), level = element.level)


if __name__ == "__main__":
    run_filters ([HeaderRepeat, HeaderLevel], prepare = Bold)