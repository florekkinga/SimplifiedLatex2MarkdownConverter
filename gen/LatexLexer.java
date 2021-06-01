// Generated from /home/kinga/uni/sem6/tkik/Latex2MarkdownConverter/Grammar/LatexLexer.g4 by ANTLR 4.9.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class LatexLexer extends Lexer {
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
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"DOCUMENT_START", "DOCUMENT_END", "TEXT", "LINE_END", "WHITESPACE", "COMMAND_CLOSE", 
			"BOLD_OPEN", "ITALICS_OPEN", "HEADER1", "HEADER2", "HEADER3", "ENUM_START", 
			"ENUM_END", "LIST_START", "LIST_END", "ITEM", "CODE_START", "CODE_END", 
			"TABLE_START", "TABLE_ALIGN", "CELL_SEPARATOR", "HLINE", "TABLE_END", 
			"QUOTE_START", "COLOR_START", "COLOR_MID"
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


	public LatexLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "LatexLexer.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\34\u017a\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31"+
		"\t\31\4\32\t\32\4\33\t\33\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2"+
		"\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\4\6\4Y\n\4\r\4\16\4Z\3\5\3\5\3\5\3\6\3\6\5\6b\n\6\3\6"+
		"\6\6e\n\6\r\6\16\6f\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3"+
		"\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n"+
		"\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f"+
		"\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3"+
		"\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3"+
		"\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3"+
		"\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3"+
		"\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3"+
		"\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3"+
		"\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3"+
		"\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3"+
		"\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3"+
		"\24\5\24\u011a\n\24\3\24\5\24\u011d\n\24\3\24\3\24\3\24\3\24\3\24\3\24"+
		"\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\5\25\u0131"+
		"\n\25\3\25\3\25\5\25\u0135\n\25\6\25\u0137\n\25\r\25\16\25\u0138\3\25"+
		"\3\25\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\5\30\u0147\n\30"+
		"\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30"+
		"\3\30\5\30\u0158\n\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30"+
		"\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32"+
		"\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\2\2\34\3\3\5\4\7\5\t\6\13"+
		"\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'"+
		"\25)\26+\27-\30/\31\61\32\63\33\65\34\3\2\5\5\2((^^\177\177\4\2\13\13"+
		"\"\"\5\2eenntt\2\u0184\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2"+
		"\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25"+
		"\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2"+
		"\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2"+
		"\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\3\67\3"+
		"\2\2\2\5H\3\2\2\2\7X\3\2\2\2\t\\\3\2\2\2\13d\3\2\2\2\rh\3\2\2\2\17j\3"+
		"\2\2\2\21s\3\2\2\2\23|\3\2\2\2\25\u0086\3\2\2\2\27\u0093\3\2\2\2\31\u00a3"+
		"\3\2\2\2\33\u00b5\3\2\2\2\35\u00c5\3\2\2\2\37\u00d5\3\2\2\2!\u00e3\3\2"+
		"\2\2#\u00e9\3\2\2\2%\u00fa\3\2\2\2\'\u0109\3\2\2\2)\u012e\3\2\2\2+\u013c"+
		"\3\2\2\2-\u013e\3\2\2\2/\u0146\3\2\2\2\61\u0165\3\2\2\2\63\u016b\3\2\2"+
		"\2\65\u0177\3\2\2\2\678\7^\2\289\7d\2\29:\7g\2\2:;\7i\2\2;<\7k\2\2<=\7"+
		"p\2\2=>\7}\2\2>?\7f\2\2?@\7q\2\2@A\7e\2\2AB\7w\2\2BC\7o\2\2CD\7g\2\2D"+
		"E\7p\2\2EF\7v\2\2FG\7\177\2\2G\4\3\2\2\2HI\7^\2\2IJ\7g\2\2JK\7p\2\2KL"+
		"\7f\2\2LM\7}\2\2MN\7f\2\2NO\7q\2\2OP\7e\2\2PQ\7w\2\2QR\7o\2\2RS\7g\2\2"+
		"ST\7p\2\2TU\7v\2\2UV\7\177\2\2V\6\3\2\2\2WY\n\2\2\2XW\3\2\2\2YZ\3\2\2"+
		"\2ZX\3\2\2\2Z[\3\2\2\2[\b\3\2\2\2\\]\7^\2\2]^\7^\2\2^\n\3\2\2\2_e\t\3"+
		"\2\2`b\7\17\2\2a`\3\2\2\2ab\3\2\2\2bc\3\2\2\2ce\7\f\2\2d_\3\2\2\2da\3"+
		"\2\2\2ef\3\2\2\2fd\3\2\2\2fg\3\2\2\2g\f\3\2\2\2hi\7\177\2\2i\16\3\2\2"+
		"\2jk\7^\2\2kl\7v\2\2lm\7g\2\2mn\7z\2\2no\7v\2\2op\7d\2\2pq\7h\2\2qr\7"+
		"}\2\2r\20\3\2\2\2st\7^\2\2tu\7v\2\2uv\7g\2\2vw\7z\2\2wx\7v\2\2xy\7k\2"+
		"\2yz\7v\2\2z{\7}\2\2{\22\3\2\2\2|}\7^\2\2}~\7u\2\2~\177\7g\2\2\177\u0080"+
		"\7e\2\2\u0080\u0081\7v\2\2\u0081\u0082\7k\2\2\u0082\u0083\7q\2\2\u0083"+
		"\u0084\7p\2\2\u0084\u0085\7}\2\2\u0085\24\3\2\2\2\u0086\u0087\7^\2\2\u0087"+
		"\u0088\7u\2\2\u0088\u0089\7w\2\2\u0089\u008a\7d\2\2\u008a\u008b\7u\2\2"+
		"\u008b\u008c\7g\2\2\u008c\u008d\7e\2\2\u008d\u008e\7v\2\2\u008e\u008f"+
		"\7k\2\2\u008f\u0090\7q\2\2\u0090\u0091\7p\2\2\u0091\u0092\7}\2\2\u0092"+
		"\26\3\2\2\2\u0093\u0094\7^\2\2\u0094\u0095\7u\2\2\u0095\u0096\7w\2\2\u0096"+
		"\u0097\7d\2\2\u0097\u0098\7u\2\2\u0098\u0099\7w\2\2\u0099\u009a\7d\2\2"+
		"\u009a\u009b\7u\2\2\u009b\u009c\7g\2\2\u009c\u009d\7e\2\2\u009d\u009e"+
		"\7v\2\2\u009e\u009f\7k\2\2\u009f\u00a0\7q\2\2\u00a0\u00a1\7p\2\2\u00a1"+
		"\u00a2\7}\2\2\u00a2\30\3\2\2\2\u00a3\u00a4\7^\2\2\u00a4\u00a5\7d\2\2\u00a5"+
		"\u00a6\7g\2\2\u00a6\u00a7\7i\2\2\u00a7\u00a8\7k\2\2\u00a8\u00a9\7p\2\2"+
		"\u00a9\u00aa\7}\2\2\u00aa\u00ab\7g\2\2\u00ab\u00ac\7p\2\2\u00ac\u00ad"+
		"\7w\2\2\u00ad\u00ae\7o\2\2\u00ae\u00af\7g\2\2\u00af\u00b0\7t\2\2\u00b0"+
		"\u00b1\7c\2\2\u00b1\u00b2\7v\2\2\u00b2\u00b3\7g\2\2\u00b3\u00b4\7\177"+
		"\2\2\u00b4\32\3\2\2\2\u00b5\u00b6\7^\2\2\u00b6\u00b7\7g\2\2\u00b7\u00b8"+
		"\7p\2\2\u00b8\u00b9\7f\2\2\u00b9\u00ba\7}\2\2\u00ba\u00bb\7g\2\2\u00bb"+
		"\u00bc\7p\2\2\u00bc\u00bd\7w\2\2\u00bd\u00be\7o\2\2\u00be\u00bf\7g\2\2"+
		"\u00bf\u00c0\7t\2\2\u00c0\u00c1\7c\2\2\u00c1\u00c2\7v\2\2\u00c2\u00c3"+
		"\7g\2\2\u00c3\u00c4\7\177\2\2\u00c4\34\3\2\2\2\u00c5\u00c6\7^\2\2\u00c6"+
		"\u00c7\7d\2\2\u00c7\u00c8\7g\2\2\u00c8\u00c9\7i\2\2\u00c9\u00ca\7k\2\2"+
		"\u00ca\u00cb\7p\2\2\u00cb\u00cc\7}\2\2\u00cc\u00cd\7k\2\2\u00cd\u00ce"+
		"\7v\2\2\u00ce\u00cf\7g\2\2\u00cf\u00d0\7o\2\2\u00d0\u00d1\7k\2\2\u00d1"+
		"\u00d2\7|\2\2\u00d2\u00d3\7g\2\2\u00d3\u00d4\7\177\2\2\u00d4\36\3\2\2"+
		"\2\u00d5\u00d6\7^\2\2\u00d6\u00d7\7g\2\2\u00d7\u00d8\7p\2\2\u00d8\u00d9"+
		"\7f\2\2\u00d9\u00da\7}\2\2\u00da\u00db\7k\2\2\u00db\u00dc\7v\2\2\u00dc"+
		"\u00dd\7g\2\2\u00dd\u00de\7o\2\2\u00de\u00df\7k\2\2\u00df\u00e0\7|\2\2"+
		"\u00e0\u00e1\7g\2\2\u00e1\u00e2\7\177\2\2\u00e2 \3\2\2\2\u00e3\u00e4\7"+
		"^\2\2\u00e4\u00e5\7k\2\2\u00e5\u00e6\7v\2\2\u00e6\u00e7\7g\2\2\u00e7\u00e8"+
		"\7o\2\2\u00e8\"\3\2\2\2\u00e9\u00ea\7^\2\2\u00ea\u00eb\7d\2\2\u00eb\u00ec"+
		"\7g\2\2\u00ec\u00ed\7i\2\2\u00ed\u00ee\7k\2\2\u00ee\u00ef\7p\2\2\u00ef"+
		"\u00f0\7}\2\2\u00f0\u00f1\7x\2\2\u00f1\u00f2\7g\2\2\u00f2\u00f3\7t\2\2"+
		"\u00f3\u00f4\7d\2\2\u00f4\u00f5\7c\2\2\u00f5\u00f6\7v\2\2\u00f6\u00f7"+
		"\7k\2\2\u00f7\u00f8\7o\2\2\u00f8\u00f9\7\177\2\2\u00f9$\3\2\2\2\u00fa"+
		"\u00fb\7^\2\2\u00fb\u00fc\7g\2\2\u00fc\u00fd\7p\2\2\u00fd\u00fe\7f\2\2"+
		"\u00fe\u00ff\7}\2\2\u00ff\u0100\7x\2\2\u0100\u0101\7g\2\2\u0101\u0102"+
		"\7t\2\2\u0102\u0103\7d\2\2\u0103\u0104\7c\2\2\u0104\u0105\7v\2\2\u0105"+
		"\u0106\7k\2\2\u0106\u0107\7o\2\2\u0107\u0108\7\177\2\2\u0108&\3\2\2\2"+
		"\u0109\u010a\7^\2\2\u010a\u010b\7d\2\2\u010b\u010c\7g\2\2\u010c\u010d"+
		"\7i\2\2\u010d\u010e\7k\2\2\u010e\u010f\7p\2\2\u010f\u0110\7}\2\2\u0110"+
		"\u0111\7v\2\2\u0111\u0112\7c\2\2\u0112\u0113\7d\2\2\u0113\u0114\7n\2\2"+
		"\u0114\u0115\7g\2\2\u0115\u0116\7\177\2\2\u0116\u0119\3\2\2\2\u0117\u0118"+
		"\7]\2\2\u0118\u011a\7_\2\2\u0119\u0117\3\2\2\2\u0119\u011a\3\2\2\2\u011a"+
		"\u011c\3\2\2\2\u011b\u011d\5\13\6\2\u011c\u011b\3\2\2\2\u011c\u011d\3"+
		"\2\2\2\u011d\u011e\3\2\2\2\u011e\u011f\7^\2\2\u011f\u0120\7d\2\2\u0120"+
		"\u0121\7g\2\2\u0121\u0122\7i\2\2\u0122\u0123\7k\2\2\u0123\u0124\7p\2\2"+
		"\u0124\u0125\7}\2\2\u0125\u0126\7v\2\2\u0126\u0127\7c\2\2\u0127\u0128"+
		"\7d\2\2\u0128\u0129\7w\2\2\u0129\u012a\7n\2\2\u012a\u012b\7c\2\2\u012b"+
		"\u012c\7t\2\2\u012c\u012d\7\177\2\2\u012d(\3\2\2\2\u012e\u0136\7}\2\2"+
		"\u012f\u0131\7~\2\2\u0130\u012f\3\2\2\2\u0130\u0131\3\2\2\2\u0131\u0132"+
		"\3\2\2\2\u0132\u0134\t\4\2\2\u0133\u0135\7~\2\2\u0134\u0133\3\2\2\2\u0134"+
		"\u0135\3\2\2\2\u0135\u0137\3\2\2\2\u0136\u0130\3\2\2\2\u0137\u0138\3\2"+
		"\2\2\u0138\u0136\3\2\2\2\u0138\u0139\3\2\2\2\u0139\u013a\3\2\2\2\u013a"+
		"\u013b\5\r\7\2\u013b*\3\2\2\2\u013c\u013d\7(\2\2\u013d,\3\2\2\2\u013e"+
		"\u013f\7^\2\2\u013f\u0140\7j\2\2\u0140\u0141\7n\2\2\u0141\u0142\7k\2\2"+
		"\u0142\u0143\7p\2\2\u0143\u0144\7g\2\2\u0144.\3\2\2\2\u0145\u0147\5\13"+
		"\6\2\u0146\u0145\3\2\2\2\u0146\u0147\3\2\2\2\u0147\u0148\3\2\2\2\u0148"+
		"\u0149\7^\2\2\u0149\u014a\7g\2\2\u014a\u014b\7p\2\2\u014b\u014c\7f\2\2"+
		"\u014c\u014d\7}\2\2\u014d\u014e\7v\2\2\u014e\u014f\7c\2\2\u014f\u0150"+
		"\7d\2\2\u0150\u0151\7w\2\2\u0151\u0152\7n\2\2\u0152\u0153\7c\2\2\u0153"+
		"\u0154\7t\2\2\u0154\u0155\7\177\2\2\u0155\u0157\3\2\2\2\u0156\u0158\5"+
		"\13\6\2\u0157\u0156\3\2\2\2\u0157\u0158\3\2\2\2\u0158\u0159\3\2\2\2\u0159"+
		"\u015a\7^\2\2\u015a\u015b\7g\2\2\u015b\u015c\7p\2\2\u015c\u015d\7f\2\2"+
		"\u015d\u015e\7}\2\2\u015e\u015f\7v\2\2\u015f\u0160\7c\2\2\u0160\u0161"+
		"\7d\2\2\u0161\u0162\7n\2\2\u0162\u0163\7g\2\2\u0163\u0164\7\177\2\2\u0164"+
		"\60\3\2\2\2\u0165\u0166\7^\2\2\u0166\u0167\7u\2\2\u0167\u0168\7c\2\2\u0168"+
		"\u0169\7{\2\2\u0169\u016a\7}\2\2\u016a\62\3\2\2\2\u016b\u016c\7^\2\2\u016c"+
		"\u016d\7v\2\2\u016d\u016e\7g\2\2\u016e\u016f\7z\2\2\u016f\u0170\7v\2\2"+
		"\u0170\u0171\7e\2\2\u0171\u0172\7q\2\2\u0172\u0173\7n\2\2\u0173\u0174"+
		"\7q\2\2\u0174\u0175\7t\2\2\u0175\u0176\7}\2\2\u0176\64\3\2\2\2\u0177\u0178"+
		"\7\177\2\2\u0178\u0179\7}\2\2\u0179\66\3\2\2\2\16\2Zadf\u0119\u011c\u0130"+
		"\u0134\u0138\u0146\u0157\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}