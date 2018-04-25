def text_formatter(text, limit=40):

    lines = text.splitlines(keepends=True)
    words = [word for line in lines for word in line.split(" ")]

    output = ""
    i = 0

    while i < len(words):
        current_row = ""

        while i < len(words):
            current_word = " " + words[i] if len(current_row) > 0 else words[i]
            if len(current_row) + len(current_word) <= limit:
                current_row += current_word
                if current_word.endswith("\n"):
                    i += 1
                    break
            else:
                current_row += "\n"
                break
            i += 1

        output += current_row

    return output.strip()


def main():
    filename = "input_example.txt"
    with open(filename) as f:
        input_text = f.read()
        output = text_formatter(input_text)
        print(output)


if __name__ == '__main__':
    main()
