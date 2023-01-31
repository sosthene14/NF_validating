import unicodedata


def nf_validating(parametere):
    to_list = parametere.split()
    to_string = " ".join(to_list)
    only_ascii = unicodedata.normalize('NFKD', to_string).encode('ASCII', 'ignore').decode('utf-8').strip().replace(
        " ", "")
    if only_ascii.isalpha():
        return to_string.strip()
    else:
        return False

