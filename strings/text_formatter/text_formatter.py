from os import path


def text_formatter(text, limit=40):

    lines = text.splitlines(keepends=True)
    words = [word for line in lines for word in line.split(" ")]

    output = ""
    i = 0

    while i < len(words):
        current_row = ""

        while i < len(words):
            current_word = " " + words[i] if len(current_row) > 0 else words[i]

            if len(current_row) + len_check(current_word) <= limit:
                current_row += current_word
                if current_word.endswith("\n"):
                    current_row = justify_text(current_row, limit)
                    i += 1
                    break
            else:
                current_row = justify_text(current_row, limit)
                current_row += "\n"
                break
            i += 1

        output += current_row

    return output.strip()


def justify_text(line, limit):
    spaces_missing = limit - len_check(line)

    if spaces_missing > 0 and line != "\n":
        gaps_count = line.count(" ")
        row_words = line.split(" ")
        additional_spaces = spaces_missing // gaps_count
        uneven_spaces = spaces_missing % gaps_count

        if additional_spaces:
            for index in enumerate(row_words):
                row_words[index[0]] += " "*additional_spaces

        j = 0
        while j < uneven_spaces:
            row_words[j] += " "
            j += 1

        line = " ".join(row_words)

    return line


def len_check(string):
    return len(string) - string.count("\n")


def main():
    filename = "input.txt"
    basepath = path.dirname(__file__)
    filepath = path.abspath(path.join(basepath, filename))
    try:
        with open(filepath) as f:
            input_text = f.read()
            output = text_formatter(input_text)
            print(output)
    except FileNotFoundError:
        print("Arquivo não encontrado! Certifique-se de que o seu texto está em um arquivo chamado 'input.txt' na mesma pasta deste script.")


if __name__ == '__main__':
    main()
