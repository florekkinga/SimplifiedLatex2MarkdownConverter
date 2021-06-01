// Generated from /home/kinga/uni/sem6/tkik/Latex2MarkdownConverter/Grammar/LatexParser.g4 by ANTLR 4.9.1
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link LatexParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface LatexParserVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link LatexParser#latexDocument}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLatexDocument(LatexParser.LatexDocumentContext ctx);
	/**
	 * Visit a parse tree produced by {@link LatexParser#documentContent}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDocumentContent(LatexParser.DocumentContentContext ctx);
	/**
	 * Visit a parse tree produced by {@link LatexParser#text}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitText(LatexParser.TextContext ctx);
	/**
	 * Visit a parse tree produced by {@link LatexParser#latexElement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLatexElement(LatexParser.LatexElementContext ctx);
	/**
	 * Visit a parse tree produced by {@link LatexParser#elementContent}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitElementContent(LatexParser.ElementContentContext ctx);
	/**
	 * Visit a parse tree produced by {@link LatexParser#latexNestedElement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLatexNestedElement(LatexParser.LatexNestedElementContext ctx);
	/**
	 * Visit a parse tree produced by {@link LatexParser#bold}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBold(LatexParser.BoldContext ctx);
	/**
	 * Visit a parse tree produced by {@link LatexParser#italics}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitItalics(LatexParser.ItalicsContext ctx);
	/**
	 * Visit a parse tree produced by {@link LatexParser#header1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitHeader1(LatexParser.Header1Context ctx);
	/**
	 * Visit a parse tree produced by {@link LatexParser#header2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitHeader2(LatexParser.Header2Context ctx);
	/**
	 * Visit a parse tree produced by {@link LatexParser#header3}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitHeader3(LatexParser.Header3Context ctx);
	/**
	 * Visit a parse tree produced by {@link LatexParser#numbered_list}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNumbered_list(LatexParser.Numbered_listContext ctx);
	/**
	 * Visit a parse tree produced by {@link LatexParser#itemize}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitItemize(LatexParser.ItemizeContext ctx);
	/**
	 * Visit a parse tree produced by {@link LatexParser#item}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitItem(LatexParser.ItemContext ctx);
	/**
	 * Visit a parse tree produced by {@link LatexParser#code}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCode(LatexParser.CodeContext ctx);
	/**
	 * Visit a parse tree produced by {@link LatexParser#table}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTable(LatexParser.TableContext ctx);
	/**
	 * Visit a parse tree produced by {@link LatexParser#quote}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitQuote(LatexParser.QuoteContext ctx);
	/**
	 * Visit a parse tree produced by {@link LatexParser#color}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitColor(LatexParser.ColorContext ctx);
}