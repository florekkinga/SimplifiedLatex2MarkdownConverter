class MarkdownFile:
    def __init__(self, text):
        self.text = text

    def generate(self):
        # this is probably good place to create .md file, but we can do this later
        return self.text


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
