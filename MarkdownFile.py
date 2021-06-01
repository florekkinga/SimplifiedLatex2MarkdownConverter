class MarkdownFile:
    def __init__(self, text):
        self.text = text

    def generate(self, output_name=None):
        # this is probably good place to create .md file, but we can do this later
        if output_name != None:
            self.generate_file(output_name)
        return self.text

    def generate_file(self, output_name):
        text_file = open(output_name, "w")
        text_file.write(self.text.strip())
        text_file.close()
        print("Saved Markdown content as a file: " + output_name)


class MarkdownFormat:
    def __init__(self, text=""):
        self.text = text

    def bold(self):
        return '**' + self.text + '**'

    def italics(self):
        return '*' + self.text + '*'

    def heading1(self):
        return '# ' + self.text + '\n'

    def heading2(self):
        return '## ' + self.text + '\n'

    def heading3(self):
        return '### ' + self.text + '\n'

    def code(self):
        return '```' + self.text + '```'

    def ordered_list(self, items):
        ordered_list = [(str(i) + '. ' + item.lstrip().rstrip() + '\n') for i, item in enumerate(items)]
        return ''.join(ordered_list)

    def unordered_list(self, items):
        unordered_list = [('- ' + item.lstrip().rstrip() + '\n') for item in items]
        return ''.join(unordered_list)

    def line_break(self):
        return '<br>'

    def table(self, align):
        align = self.table_align(align)
        column_count = align.count('|') - 1

        table = " | "
        for i, v in enumerate(self.text):
            if i == column_count:
                table += "\n" + align + "\n | "
            elif i % column_count == 0 and i > 0:
                table += "\n | "
            table += v + " | "
        return table

    def table_align(self, source):
        align = " | "
        for i in str(source)[1:-1]:
            if i == "|":
                continue
            align += self.__convert_align_char(i)
            align += " | "
        return align

    def __convert_align_char(self, ch):
        if ch == 'l':
            return ':---'
        elif ch == 'c':
            return ':---:'
        elif ch == 'r':
            return '---:'
