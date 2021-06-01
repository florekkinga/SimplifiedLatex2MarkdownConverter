// Generated from /home/kinga/uni/sem6/tkik/Latex2MarkdownConverter/Grammar/LatexParser.g4 by ANTLR 4.9.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link LatexParser}.
 */
public interface LatexParserListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link LatexParser#latexDocument}.
	 * @param ctx the parse tree
	 */
	void enterLatexDocument(LatexParser.LatexDocumentContext ctx);
	/**
	 * Exit a parse tree produced by {@link LatexParser#latexDocument}.
	 * @param ctx the parse tree
	 */
	void exitLatexDocument(LatexParser.LatexDocumentContext ctx);
	/**
	 * Enter a parse tree produced by {@link LatexParser#documentContent}.
	 * @param ctx the parse tree
	 */
	void enterDocumentContent(LatexParser.DocumentContentContext ctx);
	/**
	 * Exit a parse tree produced by {@link LatexParser#documentContent}.
	 * @param ctx the parse tree
	 */
	void exitDocumentContent(LatexParser.DocumentContentContext ctx);
	/**
	 * Enter a parse tree produced by {@link LatexParser#text}.
	 * @param ctx the parse tree
	 */
	void enterText(LatexParser.TextContext ctx);
	/**
	 * Exit a parse tree produced by {@link LatexParser#text}.
	 * @param ctx the parse tree
	 */
	void exitText(LatexParser.TextContext ctx);
	/**
	 * Enter a parse tree produced by {@link LatexParser#latexElement}.
	 * @param ctx the parse tree
	 */
	void enterLatexElement(LatexParser.LatexElementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LatexParser#latexElement}.
	 * @param ctx the parse tree
	 */
	void exitLatexElement(LatexParser.LatexElementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LatexParser#elementContent}.
	 * @param ctx the parse tree
	 */
	void enterElementContent(LatexParser.ElementContentContext ctx);
	/**
	 * Exit a parse tree produced by {@link LatexParser#elementContent}.
	 * @param ctx the parse tree
	 */
	void exitElementContent(LatexParser.ElementContentContext ctx);
	/**
	 * Enter a parse tree produced by {@link LatexParser#latexNestedElement}.
	 * @param ctx the parse tree
	 */
	void enterLatexNestedElement(LatexParser.LatexNestedElementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LatexParser#latexNestedElement}.
	 * @param ctx the parse tree
	 */
	void exitLatexNestedElement(LatexParser.LatexNestedElementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LatexParser#bold}.
	 * @param ctx the parse tree
	 */
	void enterBold(LatexParser.BoldContext ctx);
	/**
	 * Exit a parse tree produced by {@link LatexParser#bold}.
	 * @param ctx the parse tree
	 */
	void exitBold(LatexParser.BoldContext ctx);
	/**
	 * Enter a parse tree produced by {@link LatexParser#italics}.
	 * @param ctx the parse tree
	 */
	void enterItalics(LatexParser.ItalicsContext ctx);
	/**
	 * Exit a parse tree produced by {@link LatexParser#italics}.
	 * @param ctx the parse tree
	 */
	void exitItalics(LatexParser.ItalicsContext ctx);
	/**
	 * Enter a parse tree produced by {@link LatexParser#header1}.
	 * @param ctx the parse tree
	 */
	void enterHeader1(LatexParser.Header1Context ctx);
	/**
	 * Exit a parse tree produced by {@link LatexParser#header1}.
	 * @param ctx the parse tree
	 */
	void exitHeader1(LatexParser.Header1Context ctx);
	/**
	 * Enter a parse tree produced by {@link LatexParser#header2}.
	 * @param ctx the parse tree
	 */
	void enterHeader2(LatexParser.Header2Context ctx);
	/**
	 * Exit a parse tree produced by {@link LatexParser#header2}.
	 * @param ctx the parse tree
	 */
	void exitHeader2(LatexParser.Header2Context ctx);
	/**
	 * Enter a parse tree produced by {@link LatexParser#header3}.
	 * @param ctx the parse tree
	 */
	void enterHeader3(LatexParser.Header3Context ctx);
	/**
	 * Exit a parse tree produced by {@link LatexParser#header3}.
	 * @param ctx the parse tree
	 */
	void exitHeader3(LatexParser.Header3Context ctx);
	/**
	 * Enter a parse tree produced by {@link LatexParser#numbered_list}.
	 * @param ctx the parse tree
	 */
	void enterNumbered_list(LatexParser.Numbered_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link LatexParser#numbered_list}.
	 * @param ctx the parse tree
	 */
	void exitNumbered_list(LatexParser.Numbered_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link LatexParser#itemize}.
	 * @param ctx the parse tree
	 */
	void enterItemize(LatexParser.ItemizeContext ctx);
	/**
	 * Exit a parse tree produced by {@link LatexParser#itemize}.
	 * @param ctx the parse tree
	 */
	void exitItemize(LatexParser.ItemizeContext ctx);
	/**
	 * Enter a parse tree produced by {@link LatexParser#item}.
	 * @param ctx the parse tree
	 */
	void enterItem(LatexParser.ItemContext ctx);
	/**
	 * Exit a parse tree produced by {@link LatexParser#item}.
	 * @param ctx the parse tree
	 */
	void exitItem(LatexParser.ItemContext ctx);
	/**
	 * Enter a parse tree produced by {@link LatexParser#code}.
	 * @param ctx the parse tree
	 */
	void enterCode(LatexParser.CodeContext ctx);
	/**
	 * Exit a parse tree produced by {@link LatexParser#code}.
	 * @param ctx the parse tree
	 */
	void exitCode(LatexParser.CodeContext ctx);
	/**
	 * Enter a parse tree produced by {@link LatexParser#table}.
	 * @param ctx the parse tree
	 */
	void enterTable(LatexParser.TableContext ctx);
	/**
	 * Exit a parse tree produced by {@link LatexParser#table}.
	 * @param ctx the parse tree
	 */
	void exitTable(LatexParser.TableContext ctx);
	/**
	 * Enter a parse tree produced by {@link LatexParser#quote}.
	 * @param ctx the parse tree
	 */
	void enterQuote(LatexParser.QuoteContext ctx);
	/**
	 * Exit a parse tree produced by {@link LatexParser#quote}.
	 * @param ctx the parse tree
	 */
	void exitQuote(LatexParser.QuoteContext ctx);
	/**
	 * Enter a parse tree produced by {@link LatexParser#color}.
	 * @param ctx the parse tree
	 */
	void enterColor(LatexParser.ColorContext ctx);
	/**
	 * Exit a parse tree produced by {@link LatexParser#color}.
	 * @param ctx the parse tree
	 */
	void exitColor(LatexParser.ColorContext ctx);
}