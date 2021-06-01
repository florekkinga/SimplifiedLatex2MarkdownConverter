// Generated from /home/kinga/uni/sem6/tkik/Latex2MarkdownConverter/Grammar/LatexParser.g4 by ANTLR 4.9.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class LatexParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		DOCUMENT_START=1, DOCUMENT_END=2, TEXT=3, LINE_END=4, WHITESPACE=5, COMMAND_CLOSE=6, 
		BOLD_OPEN=7, ITALICS_OPEN=8, HEADER1=9, HEADER2=10, HEADER3=11, ENUM_START=12, 
		ENUM_END=13, LIST_START=14, LIST_END=15, ITEM=16, CODE_START=17, CODE_END=18, 
		TABLE_START=19, TABLE_ALIGN=20, CELL_SEPARATOR=21, HLINE=22, TABLE_END=23, 
		QUOTE_START=24, COLOR_START=25, COLOR_MID=26;
	public static final int
		RULE_latexDocument = 0, RULE_documentContent = 1, RULE_text = 2, RULE_latexElement = 3, 
		RULE_elementContent = 4, RULE_latexNestedElement = 5, RULE_bold = 6, RULE_italics = 7, 
		RULE_header1 = 8, RULE_header2 = 9, RULE_header3 = 10, RULE_numbered_list = 11, 
		RULE_itemize = 12, RULE_item = 13, RULE_code = 14, RULE_table = 15, RULE_quote = 16, 
		RULE_color = 17;
	private static String[] makeRuleNames() {
		return new String[] {
			"latexDocument", "documentContent", "text", "latexElement", "elementContent", 
			"latexNestedElement", "bold", "italics", "header1", "header2", "header3", 
			"numbered_list", "itemize", "item", "code", "table", "quote", "color"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'\\begin{document}'", "'\\end{document}'", null, "'\\\\'", null, 
			"'}'", "'\\textbf{'", "'\\textit{'", "'\\section{'", "'\\subsection{'", 
			"'\\subsubsection{'", "'\\begin{enumerate}'", "'\\end{enumerate}'", "'\\begin{itemize}'", 
			"'\\end{itemize}'", "'\\item'", "'\\begin{verbatim}'", "'\\end{verbatim}'", 
			null, null, "'&'", "'\\hline'", null, "'\\say{'", "'\\textcolor{'", "'}{'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "DOCUMENT_START", "DOCUMENT_END", "TEXT", "LINE_END", "WHITESPACE", 
			"COMMAND_CLOSE", "BOLD_OPEN", "ITALICS_OPEN", "HEADER1", "HEADER2", "HEADER3", 
			"ENUM_START", "ENUM_END", "LIST_START", "LIST_END", "ITEM", "CODE_START", 
			"CODE_END", "TABLE_START", "TABLE_ALIGN", "CELL_SEPARATOR", "HLINE", 
			"TABLE_END", "QUOTE_START", "COLOR_START", "COLOR_MID"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "LatexParser.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public LatexParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class LatexDocumentContext extends ParserRuleContext {
		public TerminalNode DOCUMENT_START() { return getToken(LatexParser.DOCUMENT_START, 0); }
		public DocumentContentContext documentContent() {
			return getRuleContext(DocumentContentContext.class,0);
		}
		public TerminalNode DOCUMENT_END() { return getToken(LatexParser.DOCUMENT_END, 0); }
		public LatexDocumentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_latexDocument; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LatexParserListener ) ((LatexParserListener)listener).enterLatexDocument(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LatexParserListener ) ((LatexParserListener)listener).exitLatexDocument(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LatexParserVisitor ) return ((LatexParserVisitor<? extends T>)visitor).visitLatexDocument(this);
			else return visitor.visitChildren(this);
		}
	}

	public final LatexDocumentContext latexDocument() throws RecognitionException {
		LatexDocumentContext _localctx = new LatexDocumentContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_latexDocument);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(36);
			match(DOCUMENT_START);
			setState(37);
			documentContent();
			setState(38);
			match(DOCUMENT_END);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DocumentContentContext extends ParserRuleContext {
		public List<TextContext> text() {
			return getRuleContexts(TextContext.class);
		}
		public TextContext text(int i) {
			return getRuleContext(TextContext.class,i);
		}
		public List<LatexElementContext> latexElement() {
			return getRuleContexts(LatexElementContext.class);
		}
		public LatexElementContext latexElement(int i) {
			return getRuleContext(LatexElementContext.class,i);
		}
		public DocumentContentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_documentContent; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LatexParserListener ) ((LatexParserListener)listener).enterDocumentContent(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LatexParserListener ) ((LatexParserListener)listener).exitDocumentContent(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LatexParserVisitor ) return ((LatexParserVisitor<? extends T>)visitor).visitDocumentContent(this);
			else return visitor.visitChildren(this);
		}
	}

	public final DocumentContentContext documentContent() throws RecognitionException {
		DocumentContentContext _localctx = new DocumentContentContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_documentContent);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(43);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << TEXT) | (1L << LINE_END) | (1L << WHITESPACE))) != 0)) {
				{
				{
				setState(40);
				text();
				}
				}
				setState(45);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(55);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << BOLD_OPEN) | (1L << ITALICS_OPEN) | (1L << HEADER1) | (1L << HEADER2) | (1L << HEADER3) | (1L << ENUM_START) | (1L << LIST_START) | (1L << CODE_START) | (1L << TABLE_START) | (1L << QUOTE_START) | (1L << COLOR_START))) != 0)) {
				{
				{
				setState(46);
				latexElement();
				setState(50);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << TEXT) | (1L << LINE_END) | (1L << WHITESPACE))) != 0)) {
					{
					{
					setState(47);
					text();
					}
					}
					setState(52);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				}
				setState(57);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TextContext extends ParserRuleContext {
		public TerminalNode TEXT() { return getToken(LatexParser.TEXT, 0); }
		public TerminalNode WHITESPACE() { return getToken(LatexParser.WHITESPACE, 0); }
		public TerminalNode LINE_END() { return getToken(LatexParser.LINE_END, 0); }
		public TextContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_text; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LatexParserListener ) ((LatexParserListener)listener).enterText(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LatexParserListener ) ((LatexParserListener)listener).exitText(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LatexParserVisitor ) return ((LatexParserVisitor<? extends T>)visitor).visitText(this);
			else return visitor.visitChildren(this);
		}
	}

	public final TextContext text() throws RecognitionException {
		TextContext _localctx = new TextContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_text);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(58);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << TEXT) | (1L << LINE_END) | (1L << WHITESPACE))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LatexElementContext extends ParserRuleContext {
		public BoldContext bold() {
			return getRuleContext(BoldContext.class,0);
		}
		public ItalicsContext italics() {
			return getRuleContext(ItalicsContext.class,0);
		}
		public Header1Context header1() {
			return getRuleContext(Header1Context.class,0);
		}
		public Header2Context header2() {
			return getRuleContext(Header2Context.class,0);
		}
		public Header3Context header3() {
			return getRuleContext(Header3Context.class,0);
		}
		public Numbered_listContext numbered_list() {
			return getRuleContext(Numbered_listContext.class,0);
		}
		public ItemizeContext itemize() {
			return getRuleContext(ItemizeContext.class,0);
		}
		public CodeContext code() {
			return getRuleContext(CodeContext.class,0);
		}
		public TableContext table() {
			return getRuleContext(TableContext.class,0);
		}
		public QuoteContext quote() {
			return getRuleContext(QuoteContext.class,0);
		}
		public ColorContext color() {
			return getRuleContext(ColorContext.class,0);
		}
		public LatexElementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_latexElement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LatexParserListener ) ((LatexParserListener)listener).enterLatexElement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LatexParserListener ) ((LatexParserListener)listener).exitLatexElement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LatexParserVisitor ) return ((LatexParserVisitor<? extends T>)visitor).visitLatexElement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final LatexElementContext latexElement() throws RecognitionException {
		LatexElementContext _localctx = new LatexElementContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_latexElement);
		try {
			setState(71);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BOLD_OPEN:
				enterOuterAlt(_localctx, 1);
				{
				setState(60);
				bold();
				}
				break;
			case ITALICS_OPEN:
				enterOuterAlt(_localctx, 2);
				{
				setState(61);
				italics();
				}
				break;
			case HEADER1:
				enterOuterAlt(_localctx, 3);
				{
				setState(62);
				header1();
				}
				break;
			case HEADER2:
				enterOuterAlt(_localctx, 4);
				{
				setState(63);
				header2();
				}
				break;
			case HEADER3:
				enterOuterAlt(_localctx, 5);
				{
				setState(64);
				header3();
				}
				break;
			case ENUM_START:
				enterOuterAlt(_localctx, 6);
				{
				setState(65);
				numbered_list();
				}
				break;
			case LIST_START:
				enterOuterAlt(_localctx, 7);
				{
				setState(66);
				itemize();
				}
				break;
			case CODE_START:
				enterOuterAlt(_localctx, 8);
				{
				setState(67);
				code();
				}
				break;
			case TABLE_START:
				enterOuterAlt(_localctx, 9);
				{
				setState(68);
				table();
				}
				break;
			case QUOTE_START:
				enterOuterAlt(_localctx, 10);
				{
				setState(69);
				quote();
				}
				break;
			case COLOR_START:
				enterOuterAlt(_localctx, 11);
				{
				setState(70);
				color();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ElementContentContext extends ParserRuleContext {
		public List<TextContext> text() {
			return getRuleContexts(TextContext.class);
		}
		public TextContext text(int i) {
			return getRuleContext(TextContext.class,i);
		}
		public List<LatexNestedElementContext> latexNestedElement() {
			return getRuleContexts(LatexNestedElementContext.class);
		}
		public LatexNestedElementContext latexNestedElement(int i) {
			return getRuleContext(LatexNestedElementContext.class,i);
		}
		public ElementContentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_elementContent; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LatexParserListener ) ((LatexParserListener)listener).enterElementContent(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LatexParserListener ) ((LatexParserListener)listener).exitElementContent(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LatexParserVisitor ) return ((LatexParserVisitor<? extends T>)visitor).visitElementContent(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ElementContentContext elementContent() throws RecognitionException {
		ElementContentContext _localctx = new ElementContentContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_elementContent);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(76);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << TEXT) | (1L << LINE_END) | (1L << WHITESPACE))) != 0)) {
				{
				{
				setState(73);
				text();
				}
				}
				setState(78);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(88);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << BOLD_OPEN) | (1L << ITALICS_OPEN) | (1L << ENUM_START) | (1L << LIST_START) | (1L << CODE_START) | (1L << QUOTE_START) | (1L << COLOR_START))) != 0)) {
				{
				{
				setState(79);
				latexNestedElement();
				setState(83);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << TEXT) | (1L << LINE_END) | (1L << WHITESPACE))) != 0)) {
					{
					{
					setState(80);
					text();
					}
					}
					setState(85);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				}
				setState(90);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LatexNestedElementContext extends ParserRuleContext {
		public BoldContext bold() {
			return getRuleContext(BoldContext.class,0);
		}
		public ItalicsContext italics() {
			return getRuleContext(ItalicsContext.class,0);
		}
		public Numbered_listContext numbered_list() {
			return getRuleContext(Numbered_listContext.class,0);
		}
		public ItemizeContext itemize() {
			return getRuleContext(ItemizeContext.class,0);
		}
		public CodeContext code() {
			return getRuleContext(CodeContext.class,0);
		}
		public QuoteContext quote() {
			return getRuleContext(QuoteContext.class,0);
		}
		public ColorContext color() {
			return getRuleContext(ColorContext.class,0);
		}
		public LatexNestedElementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_latexNestedElement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LatexParserListener ) ((LatexParserListener)listener).enterLatexNestedElement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LatexParserListener ) ((LatexParserListener)listener).exitLatexNestedElement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LatexParserVisitor ) return ((LatexParserVisitor<? extends T>)visitor).visitLatexNestedElement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final LatexNestedElementContext latexNestedElement() throws RecognitionException {
		LatexNestedElementContext _localctx = new LatexNestedElementContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_latexNestedElement);
		try {
			setState(98);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BOLD_OPEN:
				enterOuterAlt(_localctx, 1);
				{
				setState(91);
				bold();
				}
				break;
			case ITALICS_OPEN:
				enterOuterAlt(_localctx, 2);
				{
				setState(92);
				italics();
				}
				break;
			case ENUM_START:
				enterOuterAlt(_localctx, 3);
				{
				setState(93);
				numbered_list();
				}
				break;
			case LIST_START:
				enterOuterAlt(_localctx, 4);
				{
				setState(94);
				itemize();
				}
				break;
			case CODE_START:
				enterOuterAlt(_localctx, 5);
				{
				setState(95);
				code();
				}
				break;
			case QUOTE_START:
				enterOuterAlt(_localctx, 6);
				{
				setState(96);
				quote();
				}
				break;
			case COLOR_START:
				enterOuterAlt(_localctx, 7);
				{
				setState(97);
				color();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BoldContext extends ParserRuleContext {
		public TerminalNode BOLD_OPEN() { return getToken(LatexParser.BOLD_OPEN, 0); }
		public ElementContentContext elementContent() {
			return getRuleContext(ElementContentContext.class,0);
		}
		public TerminalNode COMMAND_CLOSE() { return getToken(LatexParser.COMMAND_CLOSE, 0); }
		public BoldContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bold; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LatexParserListener ) ((LatexParserListener)listener).enterBold(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LatexParserListener ) ((LatexParserListener)listener).exitBold(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LatexParserVisitor ) return ((LatexParserVisitor<? extends T>)visitor).visitBold(this);
			else return visitor.visitChildren(this);
		}
	}

	public final BoldContext bold() throws RecognitionException {
		BoldContext _localctx = new BoldContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_bold);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(100);
			match(BOLD_OPEN);
			setState(101);
			elementContent();
			setState(102);
			match(COMMAND_CLOSE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ItalicsContext extends ParserRuleContext {
		public TerminalNode ITALICS_OPEN() { return getToken(LatexParser.ITALICS_OPEN, 0); }
		public ElementContentContext elementContent() {
			return getRuleContext(ElementContentContext.class,0);
		}
		public TerminalNode COMMAND_CLOSE() { return getToken(LatexParser.COMMAND_CLOSE, 0); }
		public ItalicsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_italics; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LatexParserListener ) ((LatexParserListener)listener).enterItalics(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LatexParserListener ) ((LatexParserListener)listener).exitItalics(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LatexParserVisitor ) return ((LatexParserVisitor<? extends T>)visitor).visitItalics(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ItalicsContext italics() throws RecognitionException {
		ItalicsContext _localctx = new ItalicsContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_italics);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(104);
			match(ITALICS_OPEN);
			setState(105);
			elementContent();
			setState(106);
			match(COMMAND_CLOSE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Header1Context extends ParserRuleContext {
		public TerminalNode HEADER1() { return getToken(LatexParser.HEADER1, 0); }
		public TextContext text() {
			return getRuleContext(TextContext.class,0);
		}
		public TerminalNode COMMAND_CLOSE() { return getToken(LatexParser.COMMAND_CLOSE, 0); }
		public Header1Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_header1; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LatexParserListener ) ((LatexParserListener)listener).enterHeader1(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LatexParserListener ) ((LatexParserListener)listener).exitHeader1(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LatexParserVisitor ) return ((LatexParserVisitor<? extends T>)visitor).visitHeader1(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Header1Context header1() throws RecognitionException {
		Header1Context _localctx = new Header1Context(_ctx, getState());
		enterRule(_localctx, 16, RULE_header1);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(108);
			match(HEADER1);
			setState(109);
			text();
			setState(110);
			match(COMMAND_CLOSE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Header2Context extends ParserRuleContext {
		public TerminalNode HEADER2() { return getToken(LatexParser.HEADER2, 0); }
		public TextContext text() {
			return getRuleContext(TextContext.class,0);
		}
		public TerminalNode COMMAND_CLOSE() { return getToken(LatexParser.COMMAND_CLOSE, 0); }
		public Header2Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_header2; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LatexParserListener ) ((LatexParserListener)listener).enterHeader2(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LatexParserListener ) ((LatexParserListener)listener).exitHeader2(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LatexParserVisitor ) return ((LatexParserVisitor<? extends T>)visitor).visitHeader2(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Header2Context header2() throws RecognitionException {
		Header2Context _localctx = new Header2Context(_ctx, getState());
		enterRule(_localctx, 18, RULE_header2);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(112);
			match(HEADER2);
			setState(113);
			text();
			setState(114);
			match(COMMAND_CLOSE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Header3Context extends ParserRuleContext {
		public TerminalNode HEADER3() { return getToken(LatexParser.HEADER3, 0); }
		public TextContext text() {
			return getRuleContext(TextContext.class,0);
		}
		public TerminalNode COMMAND_CLOSE() { return getToken(LatexParser.COMMAND_CLOSE, 0); }
		public Header3Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_header3; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LatexParserListener ) ((LatexParserListener)listener).enterHeader3(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LatexParserListener ) ((LatexParserListener)listener).exitHeader3(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LatexParserVisitor ) return ((LatexParserVisitor<? extends T>)visitor).visitHeader3(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Header3Context header3() throws RecognitionException {
		Header3Context _localctx = new Header3Context(_ctx, getState());
		enterRule(_localctx, 20, RULE_header3);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(116);
			match(HEADER3);
			setState(117);
			text();
			setState(118);
			match(COMMAND_CLOSE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Numbered_listContext extends ParserRuleContext {
		public TerminalNode ENUM_START() { return getToken(LatexParser.ENUM_START, 0); }
		public TerminalNode ENUM_END() { return getToken(LatexParser.ENUM_END, 0); }
		public List<TextContext> text() {
			return getRuleContexts(TextContext.class);
		}
		public TextContext text(int i) {
			return getRuleContext(TextContext.class,i);
		}
		public List<ItemContext> item() {
			return getRuleContexts(ItemContext.class);
		}
		public ItemContext item(int i) {
			return getRuleContext(ItemContext.class,i);
		}
		public Numbered_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_numbered_list; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LatexParserListener ) ((LatexParserListener)listener).enterNumbered_list(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LatexParserListener ) ((LatexParserListener)listener).exitNumbered_list(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LatexParserVisitor ) return ((LatexParserVisitor<? extends T>)visitor).visitNumbered_list(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Numbered_listContext numbered_list() throws RecognitionException {
		Numbered_listContext _localctx = new Numbered_listContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_numbered_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(120);
			match(ENUM_START);
			setState(124);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << TEXT) | (1L << LINE_END) | (1L << WHITESPACE))) != 0)) {
				{
				{
				setState(121);
				text();
				}
				}
				setState(126);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(128); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(127);
				item();
				}
				}
				setState(130); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==ITEM );
			setState(132);
			match(ENUM_END);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ItemizeContext extends ParserRuleContext {
		public TerminalNode LIST_START() { return getToken(LatexParser.LIST_START, 0); }
		public TerminalNode LIST_END() { return getToken(LatexParser.LIST_END, 0); }
		public List<TextContext> text() {
			return getRuleContexts(TextContext.class);
		}
		public TextContext text(int i) {
			return getRuleContext(TextContext.class,i);
		}
		public List<ItemContext> item() {
			return getRuleContexts(ItemContext.class);
		}
		public ItemContext item(int i) {
			return getRuleContext(ItemContext.class,i);
		}
		public ItemizeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_itemize; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LatexParserListener ) ((LatexParserListener)listener).enterItemize(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LatexParserListener ) ((LatexParserListener)listener).exitItemize(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LatexParserVisitor ) return ((LatexParserVisitor<? extends T>)visitor).visitItemize(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ItemizeContext itemize() throws RecognitionException {
		ItemizeContext _localctx = new ItemizeContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_itemize);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(134);
			match(LIST_START);
			setState(138);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << TEXT) | (1L << LINE_END) | (1L << WHITESPACE))) != 0)) {
				{
				{
				setState(135);
				text();
				}
				}
				setState(140);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(142); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(141);
				item();
				}
				}
				setState(144); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==ITEM );
			setState(146);
			match(LIST_END);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ItemContext extends ParserRuleContext {
		public TerminalNode ITEM() { return getToken(LatexParser.ITEM, 0); }
		public ElementContentContext elementContent() {
			return getRuleContext(ElementContentContext.class,0);
		}
		public ItemContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_item; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LatexParserListener ) ((LatexParserListener)listener).enterItem(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LatexParserListener ) ((LatexParserListener)listener).exitItem(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LatexParserVisitor ) return ((LatexParserVisitor<? extends T>)visitor).visitItem(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ItemContext item() throws RecognitionException {
		ItemContext _localctx = new ItemContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_item);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(148);
			match(ITEM);
			setState(149);
			elementContent();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CodeContext extends ParserRuleContext {
		public TerminalNode CODE_START() { return getToken(LatexParser.CODE_START, 0); }
		public TextContext text() {
			return getRuleContext(TextContext.class,0);
		}
		public TerminalNode CODE_END() { return getToken(LatexParser.CODE_END, 0); }
		public CodeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_code; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LatexParserListener ) ((LatexParserListener)listener).enterCode(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LatexParserListener ) ((LatexParserListener)listener).exitCode(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LatexParserVisitor ) return ((LatexParserVisitor<? extends T>)visitor).visitCode(this);
			else return visitor.visitChildren(this);
		}
	}

	public final CodeContext code() throws RecognitionException {
		CodeContext _localctx = new CodeContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_code);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(151);
			match(CODE_START);
			setState(152);
			text();
			setState(153);
			match(CODE_END);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TableContext extends ParserRuleContext {
		public TerminalNode TABLE_START() { return getToken(LatexParser.TABLE_START, 0); }
		public TerminalNode TABLE_ALIGN() { return getToken(LatexParser.TABLE_ALIGN, 0); }
		public TerminalNode TABLE_END() { return getToken(LatexParser.TABLE_END, 0); }
		public List<TextContext> text() {
			return getRuleContexts(TextContext.class);
		}
		public TextContext text(int i) {
			return getRuleContext(TextContext.class,i);
		}
		public List<TerminalNode> LINE_END() { return getTokens(LatexParser.LINE_END); }
		public TerminalNode LINE_END(int i) {
			return getToken(LatexParser.LINE_END, i);
		}
		public List<TerminalNode> CELL_SEPARATOR() { return getTokens(LatexParser.CELL_SEPARATOR); }
		public TerminalNode CELL_SEPARATOR(int i) {
			return getToken(LatexParser.CELL_SEPARATOR, i);
		}
		public List<TerminalNode> WHITESPACE() { return getTokens(LatexParser.WHITESPACE); }
		public TerminalNode WHITESPACE(int i) {
			return getToken(LatexParser.WHITESPACE, i);
		}
		public List<TerminalNode> HLINE() { return getTokens(LatexParser.HLINE); }
		public TerminalNode HLINE(int i) {
			return getToken(LatexParser.HLINE, i);
		}
		public TableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_table; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LatexParserListener ) ((LatexParserListener)listener).enterTable(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LatexParserListener ) ((LatexParserListener)listener).exitTable(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LatexParserVisitor ) return ((LatexParserVisitor<? extends T>)visitor).visitTable(this);
			else return visitor.visitChildren(this);
		}
	}

	public final TableContext table() throws RecognitionException {
		TableContext _localctx = new TableContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_table);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(155);
			match(TABLE_START);
			setState(156);
			match(TABLE_ALIGN);
			setState(172); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(157);
				text();
				setState(162);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==CELL_SEPARATOR) {
					{
					{
					setState(158);
					match(CELL_SEPARATOR);
					setState(159);
					text();
					}
					}
					setState(164);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(165);
				match(LINE_END);
				setState(167);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
				case 1:
					{
					setState(166);
					match(WHITESPACE);
					}
					break;
				}
				setState(170);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==HLINE) {
					{
					setState(169);
					match(HLINE);
					}
				}

				}
				}
				setState(174); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << TEXT) | (1L << LINE_END) | (1L << WHITESPACE))) != 0) );
			setState(176);
			match(TABLE_END);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class QuoteContext extends ParserRuleContext {
		public TerminalNode QUOTE_START() { return getToken(LatexParser.QUOTE_START, 0); }
		public TextContext text() {
			return getRuleContext(TextContext.class,0);
		}
		public TerminalNode COMMAND_CLOSE() { return getToken(LatexParser.COMMAND_CLOSE, 0); }
		public QuoteContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_quote; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LatexParserListener ) ((LatexParserListener)listener).enterQuote(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LatexParserListener ) ((LatexParserListener)listener).exitQuote(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LatexParserVisitor ) return ((LatexParserVisitor<? extends T>)visitor).visitQuote(this);
			else return visitor.visitChildren(this);
		}
	}

	public final QuoteContext quote() throws RecognitionException {
		QuoteContext _localctx = new QuoteContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_quote);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(178);
			match(QUOTE_START);
			setState(179);
			text();
			setState(180);
			match(COMMAND_CLOSE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ColorContext extends ParserRuleContext {
		public TerminalNode COLOR_START() { return getToken(LatexParser.COLOR_START, 0); }
		public List<TextContext> text() {
			return getRuleContexts(TextContext.class);
		}
		public TextContext text(int i) {
			return getRuleContext(TextContext.class,i);
		}
		public TerminalNode COLOR_MID() { return getToken(LatexParser.COLOR_MID, 0); }
		public TerminalNode COMMAND_CLOSE() { return getToken(LatexParser.COMMAND_CLOSE, 0); }
		public ColorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_color; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LatexParserListener ) ((LatexParserListener)listener).enterColor(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LatexParserListener ) ((LatexParserListener)listener).exitColor(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LatexParserVisitor ) return ((LatexParserVisitor<? extends T>)visitor).visitColor(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ColorContext color() throws RecognitionException {
		ColorContext _localctx = new ColorContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_color);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(182);
			match(COLOR_START);
			setState(183);
			text();
			setState(184);
			match(COLOR_MID);
			setState(185);
			text();
			setState(186);
			match(COMMAND_CLOSE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\34\u00bf\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\3\2\3\2\3\2\3\2\3\3\7\3,\n\3\f\3\16\3/\13\3\3\3\3\3\7\3\63"+
		"\n\3\f\3\16\3\66\13\3\7\38\n\3\f\3\16\3;\13\3\3\4\3\4\3\5\3\5\3\5\3\5"+
		"\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5J\n\5\3\6\7\6M\n\6\f\6\16\6P\13\6\3\6"+
		"\3\6\7\6T\n\6\f\6\16\6W\13\6\7\6Y\n\6\f\6\16\6\\\13\6\3\7\3\7\3\7\3\7"+
		"\3\7\3\7\3\7\5\7e\n\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n"+
		"\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\7\r}\n\r\f\r\16\r\u0080\13"+
		"\r\3\r\6\r\u0083\n\r\r\r\16\r\u0084\3\r\3\r\3\16\3\16\7\16\u008b\n\16"+
		"\f\16\16\16\u008e\13\16\3\16\6\16\u0091\n\16\r\16\16\16\u0092\3\16\3\16"+
		"\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\7\21\u00a3"+
		"\n\21\f\21\16\21\u00a6\13\21\3\21\3\21\5\21\u00aa\n\21\3\21\5\21\u00ad"+
		"\n\21\6\21\u00af\n\21\r\21\16\21\u00b0\3\21\3\21\3\22\3\22\3\22\3\22\3"+
		"\23\3\23\3\23\3\23\3\23\3\23\3\23\2\2\24\2\4\6\b\n\f\16\20\22\24\26\30"+
		"\32\34\36 \"$\2\3\3\2\5\7\2\u00ca\2&\3\2\2\2\4-\3\2\2\2\6<\3\2\2\2\bI"+
		"\3\2\2\2\nN\3\2\2\2\fd\3\2\2\2\16f\3\2\2\2\20j\3\2\2\2\22n\3\2\2\2\24"+
		"r\3\2\2\2\26v\3\2\2\2\30z\3\2\2\2\32\u0088\3\2\2\2\34\u0096\3\2\2\2\36"+
		"\u0099\3\2\2\2 \u009d\3\2\2\2\"\u00b4\3\2\2\2$\u00b8\3\2\2\2&\'\7\3\2"+
		"\2\'(\5\4\3\2()\7\4\2\2)\3\3\2\2\2*,\5\6\4\2+*\3\2\2\2,/\3\2\2\2-+\3\2"+
		"\2\2-.\3\2\2\2.9\3\2\2\2/-\3\2\2\2\60\64\5\b\5\2\61\63\5\6\4\2\62\61\3"+
		"\2\2\2\63\66\3\2\2\2\64\62\3\2\2\2\64\65\3\2\2\2\658\3\2\2\2\66\64\3\2"+
		"\2\2\67\60\3\2\2\28;\3\2\2\29\67\3\2\2\29:\3\2\2\2:\5\3\2\2\2;9\3\2\2"+
		"\2<=\t\2\2\2=\7\3\2\2\2>J\5\16\b\2?J\5\20\t\2@J\5\22\n\2AJ\5\24\13\2B"+
		"J\5\26\f\2CJ\5\30\r\2DJ\5\32\16\2EJ\5\36\20\2FJ\5 \21\2GJ\5\"\22\2HJ\5"+
		"$\23\2I>\3\2\2\2I?\3\2\2\2I@\3\2\2\2IA\3\2\2\2IB\3\2\2\2IC\3\2\2\2ID\3"+
		"\2\2\2IE\3\2\2\2IF\3\2\2\2IG\3\2\2\2IH\3\2\2\2J\t\3\2\2\2KM\5\6\4\2LK"+
		"\3\2\2\2MP\3\2\2\2NL\3\2\2\2NO\3\2\2\2OZ\3\2\2\2PN\3\2\2\2QU\5\f\7\2R"+
		"T\5\6\4\2SR\3\2\2\2TW\3\2\2\2US\3\2\2\2UV\3\2\2\2VY\3\2\2\2WU\3\2\2\2"+
		"XQ\3\2\2\2Y\\\3\2\2\2ZX\3\2\2\2Z[\3\2\2\2[\13\3\2\2\2\\Z\3\2\2\2]e\5\16"+
		"\b\2^e\5\20\t\2_e\5\30\r\2`e\5\32\16\2ae\5\36\20\2be\5\"\22\2ce\5$\23"+
		"\2d]\3\2\2\2d^\3\2\2\2d_\3\2\2\2d`\3\2\2\2da\3\2\2\2db\3\2\2\2dc\3\2\2"+
		"\2e\r\3\2\2\2fg\7\t\2\2gh\5\n\6\2hi\7\b\2\2i\17\3\2\2\2jk\7\n\2\2kl\5"+
		"\n\6\2lm\7\b\2\2m\21\3\2\2\2no\7\13\2\2op\5\6\4\2pq\7\b\2\2q\23\3\2\2"+
		"\2rs\7\f\2\2st\5\6\4\2tu\7\b\2\2u\25\3\2\2\2vw\7\r\2\2wx\5\6\4\2xy\7\b"+
		"\2\2y\27\3\2\2\2z~\7\16\2\2{}\5\6\4\2|{\3\2\2\2}\u0080\3\2\2\2~|\3\2\2"+
		"\2~\177\3\2\2\2\177\u0082\3\2\2\2\u0080~\3\2\2\2\u0081\u0083\5\34\17\2"+
		"\u0082\u0081\3\2\2\2\u0083\u0084\3\2\2\2\u0084\u0082\3\2\2\2\u0084\u0085"+
		"\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u0087\7\17\2\2\u0087\31\3\2\2\2\u0088"+
		"\u008c\7\20\2\2\u0089\u008b\5\6\4\2\u008a\u0089\3\2\2\2\u008b\u008e\3"+
		"\2\2\2\u008c\u008a\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u0090\3\2\2\2\u008e"+
		"\u008c\3\2\2\2\u008f\u0091\5\34\17\2\u0090\u008f\3\2\2\2\u0091\u0092\3"+
		"\2\2\2\u0092\u0090\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u0094\3\2\2\2\u0094"+
		"\u0095\7\21\2\2\u0095\33\3\2\2\2\u0096\u0097\7\22\2\2\u0097\u0098\5\n"+
		"\6\2\u0098\35\3\2\2\2\u0099\u009a\7\23\2\2\u009a\u009b\5\6\4\2\u009b\u009c"+
		"\7\24\2\2\u009c\37\3\2\2\2\u009d\u009e\7\25\2\2\u009e\u00ae\7\26\2\2\u009f"+
		"\u00a4\5\6\4\2\u00a0\u00a1\7\27\2\2\u00a1\u00a3\5\6\4\2\u00a2\u00a0\3"+
		"\2\2\2\u00a3\u00a6\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5"+
		"\u00a7\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a7\u00a9\7\6\2\2\u00a8\u00aa\7\7"+
		"\2\2\u00a9\u00a8\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00ac\3\2\2\2\u00ab"+
		"\u00ad\7\30\2\2\u00ac\u00ab\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00af\3"+
		"\2\2\2\u00ae\u009f\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b0"+
		"\u00b1\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b3\7\31\2\2\u00b3!\3\2\2\2"+
		"\u00b4\u00b5\7\32\2\2\u00b5\u00b6\5\6\4\2\u00b6\u00b7\7\b\2\2\u00b7#\3"+
		"\2\2\2\u00b8\u00b9\7\33\2\2\u00b9\u00ba\5\6\4\2\u00ba\u00bb\7\34\2\2\u00bb"+
		"\u00bc\5\6\4\2\u00bc\u00bd\7\b\2\2\u00bd%\3\2\2\2\22-\649INUZd~\u0084"+
		"\u008c\u0092\u00a4\u00a9\u00ac\u00b0";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}