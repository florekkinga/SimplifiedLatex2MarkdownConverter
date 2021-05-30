// Generated from /home/kinga/uni/sem6/tkik/Latex2MarkdownConverter/LatexLexer.g4 by ANTLR 4.9.1
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
		ENUM_END=13, LIST_START=14, LIST_END=15, ITEM=16, CODE_START=17, CODE_END=18;
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
			"ENUM_END", "LIST_START", "LIST_END", "ITEM", "CODE_START", "CODE_END"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'\\begin{document}'", "'\\end{document}'", null, "'\\\\'", null, 
			"'}'", "'\\textbf{'", "'\\textit{'", "'\\section{'", "'\\subsection{'", 
			"'\\subsubsection{'", "'\\begin{enumerate}'", "'\\end{enumerate}'", "'\\begin{itemize}'", 
			"'\\end{itemize}'", "'\\item'", "'\\begin{verbatim}'", "'\\end{verbatim}'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "DOCUMENT_START", "DOCUMENT_END", "TEXT", "LINE_END", "WHITESPACE", 
			"COMMAND_CLOSE", "BOLD_OPEN", "ITALICS_OPEN", "HEADER1", "HEADER2", "HEADER3", 
			"ENUM_START", "ENUM_END", "LIST_START", "LIST_END", "ITEM", "CODE_START", 
			"CODE_END"
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\24\u00f9\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3"+
		"\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\4\6\4I\n\4\r\4\16\4J\3\5\3\5\3\5\3\6\3\6\5\6R\n\6\3\6\6\6U\n\6"+
		"\r\6\16\6V\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t"+
		"\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13"+
		"\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3"+
		"\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r"+
		"\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3"+
		"\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3"+
		"\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3"+
		"\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3"+
		"\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3"+
		"\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3"+
		"\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\2\2\24\3\3\5\4\7"+
		"\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22"+
		"#\23%\24\3\2\4\4\2^^\177\177\4\2\13\13\"\"\2\u00fc\2\3\3\2\2\2\2\5\3\2"+
		"\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21"+
		"\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2"+
		"\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\3\'\3"+
		"\2\2\2\58\3\2\2\2\7H\3\2\2\2\tL\3\2\2\2\13T\3\2\2\2\rX\3\2\2\2\17Z\3\2"+
		"\2\2\21c\3\2\2\2\23l\3\2\2\2\25v\3\2\2\2\27\u0083\3\2\2\2\31\u0093\3\2"+
		"\2\2\33\u00a5\3\2\2\2\35\u00b5\3\2\2\2\37\u00c5\3\2\2\2!\u00d3\3\2\2\2"+
		"#\u00d9\3\2\2\2%\u00ea\3\2\2\2\'(\7^\2\2()\7d\2\2)*\7g\2\2*+\7i\2\2+,"+
		"\7k\2\2,-\7p\2\2-.\7}\2\2./\7f\2\2/\60\7q\2\2\60\61\7e\2\2\61\62\7w\2"+
		"\2\62\63\7o\2\2\63\64\7g\2\2\64\65\7p\2\2\65\66\7v\2\2\66\67\7\177\2\2"+
		"\67\4\3\2\2\289\7^\2\29:\7g\2\2:;\7p\2\2;<\7f\2\2<=\7}\2\2=>\7f\2\2>?"+
		"\7q\2\2?@\7e\2\2@A\7w\2\2AB\7o\2\2BC\7g\2\2CD\7p\2\2DE\7v\2\2EF\7\177"+
		"\2\2F\6\3\2\2\2GI\n\2\2\2HG\3\2\2\2IJ\3\2\2\2JH\3\2\2\2JK\3\2\2\2K\b\3"+
		"\2\2\2LM\7^\2\2MN\7^\2\2N\n\3\2\2\2OU\t\3\2\2PR\7\17\2\2QP\3\2\2\2QR\3"+
		"\2\2\2RS\3\2\2\2SU\7\f\2\2TO\3\2\2\2TQ\3\2\2\2UV\3\2\2\2VT\3\2\2\2VW\3"+
		"\2\2\2W\f\3\2\2\2XY\7\177\2\2Y\16\3\2\2\2Z[\7^\2\2[\\\7v\2\2\\]\7g\2\2"+
		"]^\7z\2\2^_\7v\2\2_`\7d\2\2`a\7h\2\2ab\7}\2\2b\20\3\2\2\2cd\7^\2\2de\7"+
		"v\2\2ef\7g\2\2fg\7z\2\2gh\7v\2\2hi\7k\2\2ij\7v\2\2jk\7}\2\2k\22\3\2\2"+
		"\2lm\7^\2\2mn\7u\2\2no\7g\2\2op\7e\2\2pq\7v\2\2qr\7k\2\2rs\7q\2\2st\7"+
		"p\2\2tu\7}\2\2u\24\3\2\2\2vw\7^\2\2wx\7u\2\2xy\7w\2\2yz\7d\2\2z{\7u\2"+
		"\2{|\7g\2\2|}\7e\2\2}~\7v\2\2~\177\7k\2\2\177\u0080\7q\2\2\u0080\u0081"+
		"\7p\2\2\u0081\u0082\7}\2\2\u0082\26\3\2\2\2\u0083\u0084\7^\2\2\u0084\u0085"+
		"\7u\2\2\u0085\u0086\7w\2\2\u0086\u0087\7d\2\2\u0087\u0088\7u\2\2\u0088"+
		"\u0089\7w\2\2\u0089\u008a\7d\2\2\u008a\u008b\7u\2\2\u008b\u008c\7g\2\2"+
		"\u008c\u008d\7e\2\2\u008d\u008e\7v\2\2\u008e\u008f\7k\2\2\u008f\u0090"+
		"\7q\2\2\u0090\u0091\7p\2\2\u0091\u0092\7}\2\2\u0092\30\3\2\2\2\u0093\u0094"+
		"\7^\2\2\u0094\u0095\7d\2\2\u0095\u0096\7g\2\2\u0096\u0097\7i\2\2\u0097"+
		"\u0098\7k\2\2\u0098\u0099\7p\2\2\u0099\u009a\7}\2\2\u009a\u009b\7g\2\2"+
		"\u009b\u009c\7p\2\2\u009c\u009d\7w\2\2\u009d\u009e\7o\2\2\u009e\u009f"+
		"\7g\2\2\u009f\u00a0\7t\2\2\u00a0\u00a1\7c\2\2\u00a1\u00a2\7v\2\2\u00a2"+
		"\u00a3\7g\2\2\u00a3\u00a4\7\177\2\2\u00a4\32\3\2\2\2\u00a5\u00a6\7^\2"+
		"\2\u00a6\u00a7\7g\2\2\u00a7\u00a8\7p\2\2\u00a8\u00a9\7f\2\2\u00a9\u00aa"+
		"\7}\2\2\u00aa\u00ab\7g\2\2\u00ab\u00ac\7p\2\2\u00ac\u00ad\7w\2\2\u00ad"+
		"\u00ae\7o\2\2\u00ae\u00af\7g\2\2\u00af\u00b0\7t\2\2\u00b0\u00b1\7c\2\2"+
		"\u00b1\u00b2\7v\2\2\u00b2\u00b3\7g\2\2\u00b3\u00b4\7\177\2\2\u00b4\34"+
		"\3\2\2\2\u00b5\u00b6\7^\2\2\u00b6\u00b7\7d\2\2\u00b7\u00b8\7g\2\2\u00b8"+
		"\u00b9\7i\2\2\u00b9\u00ba\7k\2\2\u00ba\u00bb\7p\2\2\u00bb\u00bc\7}\2\2"+
		"\u00bc\u00bd\7k\2\2\u00bd\u00be\7v\2\2\u00be\u00bf\7g\2\2\u00bf\u00c0"+
		"\7o\2\2\u00c0\u00c1\7k\2\2\u00c1\u00c2\7|\2\2\u00c2\u00c3\7g\2\2\u00c3"+
		"\u00c4\7\177\2\2\u00c4\36\3\2\2\2\u00c5\u00c6\7^\2\2\u00c6\u00c7\7g\2"+
		"\2\u00c7\u00c8\7p\2\2\u00c8\u00c9\7f\2\2\u00c9\u00ca\7}\2\2\u00ca\u00cb"+
		"\7k\2\2\u00cb\u00cc\7v\2\2\u00cc\u00cd\7g\2\2\u00cd\u00ce\7o\2\2\u00ce"+
		"\u00cf\7k\2\2\u00cf\u00d0\7|\2\2\u00d0\u00d1\7g\2\2\u00d1\u00d2\7\177"+
		"\2\2\u00d2 \3\2\2\2\u00d3\u00d4\7^\2\2\u00d4\u00d5\7k\2\2\u00d5\u00d6"+
		"\7v\2\2\u00d6\u00d7\7g\2\2\u00d7\u00d8\7o\2\2\u00d8\"\3\2\2\2\u00d9\u00da"+
		"\7^\2\2\u00da\u00db\7d\2\2\u00db\u00dc\7g\2\2\u00dc\u00dd\7i\2\2\u00dd"+
		"\u00de\7k\2\2\u00de\u00df\7p\2\2\u00df\u00e0\7}\2\2\u00e0\u00e1\7x\2\2"+
		"\u00e1\u00e2\7g\2\2\u00e2\u00e3\7t\2\2\u00e3\u00e4\7d\2\2\u00e4\u00e5"+
		"\7c\2\2\u00e5\u00e6\7v\2\2\u00e6\u00e7\7k\2\2\u00e7\u00e8\7o\2\2\u00e8"+
		"\u00e9\7\177\2\2\u00e9$\3\2\2\2\u00ea\u00eb\7^\2\2\u00eb\u00ec\7g\2\2"+
		"\u00ec\u00ed\7p\2\2\u00ed\u00ee\7f\2\2\u00ee\u00ef\7}\2\2\u00ef\u00f0"+
		"\7x\2\2\u00f0\u00f1\7g\2\2\u00f1\u00f2\7t\2\2\u00f2\u00f3\7d\2\2\u00f3"+
		"\u00f4\7c\2\2\u00f4\u00f5\7v\2\2\u00f5\u00f6\7k\2\2\u00f6\u00f7\7o\2\2"+
		"\u00f7\u00f8\7\177\2\2\u00f8&\3\2\2\2\7\2JQTV\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}