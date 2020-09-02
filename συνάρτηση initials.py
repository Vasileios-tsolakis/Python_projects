def initials(text):
    para = text.split()
    to_print = ''
    for p in para:
        words = p.upper()
        to_print += words[0] + '.'+' '
    return to_print
