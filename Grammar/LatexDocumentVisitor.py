from .LatexParserVisitor import LatexParserVisitor
from .LatexParser import LatexParser
from .MarkdownFile import MarkdownFile, MarkdownFormat


class LatexDocumentVisitor(LatexParserVisitor):
    def __init__(self, output_name:None, inline_html:False) -> None:
        super().__init__()
        self.output_name = output_name
        self.inline_html = inline_html

    def visitLatexDocument(self, ctx: LatexParser.LatexDocumentContext):
        text = self.visit(ctx.documentContent())
        return MarkdownFile(text).generate(self.output_name)

    def visitDocumentContent(self, ctx: LatexParser.DocumentContentContext):
        return self.visitChildren(ctx)

    def visitLatexElement(self, ctx: LatexParser.LatexElementContext):
        return self.visitChildren(ctx)

    def visitElementContent(self, ctx: LatexParser.ElementContentContext):
        return self.visitChildren(ctx)

    def visitLatexNestedElement(self, ctx: LatexParser.LatexNestedElementContext):
        return self.visitChildren(ctx)

    def visitHeader1(self, ctx: LatexParser.Header1Context):
        content = ctx.text().getText()
        return MarkdownFormat(content).heading1()

    def visitHeader2(self, ctx: LatexParser.Header2Context):
        content = ctx.text().getText()
        return MarkdownFormat(content).heading2()

    def visitHeader3(self, ctx: LatexParser.Header3Context):
        content = ctx.text().getText()
        return MarkdownFormat(content).heading3()

    def visitBold(self, ctx: LatexParser.BoldContext):
        content = self.visitChildren(ctx.elementContent())
        return MarkdownFormat(content).bold()

    def visitItalics(self, ctx: LatexParser.ItalicsContext):
        content = self.visitChildren(ctx.elementContent())
        return MarkdownFormat(content).italics()

    def visitText(self, ctx: LatexParser.TextContext):
        if ctx.LINE_END():
            return MarkdownFormat().line_break()
        else:
            return ctx.getText()

    def visitCode(self, ctx: LatexParser.CodeContext):
        content = ctx.text().getText()
        return MarkdownFormat(content).code()

    def visitItem(self, ctx: LatexParser.ItemContext):
        content = self.visitChildren(ctx.elementContent())
        return content

    def visitItemize(self, ctx: LatexParser.ItemizeContext):
        items = [self.visit(child) for child in ctx.children if isinstance(child, LatexParser.ItemContext)]
        return MarkdownFormat().unordered_list(items)

    def visitNumbered_list(self, ctx: LatexParser.Numbered_listContext):
        items = [self.visit(child) for child in ctx.children if isinstance(child, LatexParser.ItemContext)]
        return MarkdownFormat().ordered_list(items)

    def visitChildren(self, ctx):
        elements = [self.visit(child) for child in ctx.children]
        content = ''.join(elements)
        return content
    
    def visitTable(self, ctx:LatexParser.TableContext):
        align = ctx.TABLE_ALIGN()
        # prepare list of cells - without newlines (both Windows and Linux) and leading/trailing spaces
        cells = [cell.getText().replace('\n', '').replace('\r', '').strip() for cell in ctx.text()]
        return MarkdownFormat().table(cells, align)

    def visitColor(self, ctx:LatexParser.ColorContext):
        contents = [text.getText() for text in ctx.text()]
        return MarkdownFormat(contents[1]).color(contents[0], self.inline_html)

