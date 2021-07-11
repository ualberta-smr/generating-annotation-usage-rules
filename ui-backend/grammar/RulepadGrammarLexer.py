# Generated from RulepadGrammar.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2-")
        buf.write("\u019b\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\6\24\u0099\n\24\r\24\16\24\u009a\3\25\3\25\3\26")
        buf.write("\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3")
        buf.write("!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3")
        buf.write("$\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3")
        buf.write("&\3&\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3\'")
        buf.write("\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3")
        buf.write("(\3(\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*\3")
        buf.write("*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3")
        buf.write("+\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\2\2-\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write("\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34")
        buf.write("\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-\3\2\5\4\2")
        buf.write("\13\13\"\"\7\2//\62;C\\aac|\4\2\f\f\17\17\2\u019b\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3")
        buf.write("\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2")
        buf.write("/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\3Y\3\2\2\2\5[\3\2\2\2\7^\3\2")
        buf.write("\2\2\ta\3\2\2\2\13c\3\2\2\2\rg\3\2\2\2\17l\3\2\2\2\21")
        buf.write("n\3\2\2\2\23p\3\2\2\2\25r\3\2\2\2\27t\3\2\2\2\31v\3\2")
        buf.write("\2\2\33x\3\2\2\2\35~\3\2\2\2\37\u0082\3\2\2\2!\u0087\3")
        buf.write("\2\2\2#\u008b\3\2\2\2%\u0091\3\2\2\2\'\u0098\3\2\2\2)")
        buf.write("\u009c\3\2\2\2+\u009e\3\2\2\2-\u00a0\3\2\2\2/\u00a2\3")
        buf.write("\2\2\2\61\u00a4\3\2\2\2\63\u00aa\3\2\2\2\65\u00b6\3\2")
        buf.write("\2\2\67\u00c1\3\2\2\29\u00cc\3\2\2\2;\u00dc\3\2\2\2=\u00e7")
        buf.write("\3\2\2\2?\u00f1\3\2\2\2A\u0104\3\2\2\2C\u0111\3\2\2\2")
        buf.write("E\u011c\3\2\2\2G\u0122\3\2\2\2I\u012d\3\2\2\2K\u0139\3")
        buf.write("\2\2\2M\u0147\3\2\2\2O\u015e\3\2\2\2Q\u0174\3\2\2\2S\u017b")
        buf.write("\3\2\2\2U\u018a\3\2\2\2W\u0191\3\2\2\2YZ\7$\2\2Z\4\3\2")
        buf.write("\2\2[\\\7~\2\2\\]\7~\2\2]\6\3\2\2\2^_\7(\2\2_`\7(\2\2")
        buf.write("`\b\3\2\2\2ab\7#\2\2b\n\3\2\2\2cd\7\60\2\2de\7\60\2\2")
        buf.write("ef\7\60\2\2f\f\3\2\2\2gh\7#\2\2hi\7\60\2\2ij\7\60\2\2")
        buf.write("jk\7\60\2\2k\16\3\2\2\2lm\7\60\2\2m\20\3\2\2\2no\7?\2")
        buf.write("\2o\22\3\2\2\2pq\7@\2\2q\24\3\2\2\2rs\7>\2\2s\26\3\2\2")
        buf.write("\2tu\7)\2\2u\30\3\2\2\2vw\7(\2\2w\32\3\2\2\2xy\7o\2\2")
        buf.write("yz\7w\2\2z{\7u\2\2{|\7v\2\2|}\7\"\2\2}\34\3\2\2\2~\177")
        buf.write("\7q\2\2\177\u0080\7h\2\2\u0080\u0081\7\"\2\2\u0081\36")
        buf.write("\3\2\2\2\u0082\u0083\7c\2\2\u0083\u0084\7p\2\2\u0084\u0085")
        buf.write("\7f\2\2\u0085\u0086\7\"\2\2\u0086 \3\2\2\2\u0087\u0088")
        buf.write("\7q\2\2\u0088\u0089\7t\2\2\u0089\u008a\7\"\2\2\u008a\"")
        buf.write("\3\2\2\2\u008b\u008c\7j\2\2\u008c\u008d\7c\2\2\u008d\u008e")
        buf.write("\7x\2\2\u008e\u008f\7g\2\2\u008f\u0090\7\"\2\2\u0090$")
        buf.write("\3\2\2\2\u0091\u0092\7y\2\2\u0092\u0093\7k\2\2\u0093\u0094")
        buf.write("\7v\2\2\u0094\u0095\7j\2\2\u0095\u0096\7\"\2\2\u0096&")
        buf.write("\3\2\2\2\u0097\u0099\t\2\2\2\u0098\u0097\3\2\2\2\u0099")
        buf.write("\u009a\3\2\2\2\u009a\u0098\3\2\2\2\u009a\u009b\3\2\2\2")
        buf.write("\u009b(\3\2\2\2\u009c\u009d\t\3\2\2\u009d*\3\2\2\2\u009e")
        buf.write("\u009f\t\4\2\2\u009f,\3\2\2\2\u00a0\u00a1\7*\2\2\u00a1")
        buf.write(".\3\2\2\2\u00a2\u00a3\7+\2\2\u00a3\60\3\2\2\2\u00a4\u00a5")
        buf.write("\7p\2\2\u00a5\u00a6\7c\2\2\u00a6\u00a7\7o\2\2\u00a7\u00a8")
        buf.write("\7g\2\2\u00a8\u00a9\7\"\2\2\u00a9\62\3\2\2\2\u00aa\u00ab")
        buf.write("\7c\2\2\u00ab\u00ac\7p\2\2\u00ac\u00ad\7p\2\2\u00ad\u00ae")
        buf.write("\7q\2\2\u00ae\u00af\7v\2\2\u00af\u00b0\7c\2\2\u00b0\u00b1")
        buf.write("\7v\2\2\u00b1\u00b2\7k\2\2\u00b2\u00b3\7q\2\2\u00b3\u00b4")
        buf.write("\7p\2\2\u00b4\u00b5\7\"\2\2\u00b5\64\3\2\2\2\u00b6\u00b7")
        buf.write("\7g\2\2\u00b7\u00b8\7z\2\2\u00b8\u00b9\7v\2\2\u00b9\u00ba")
        buf.write("\7g\2\2\u00ba\u00bb\7p\2\2\u00bb\u00bc\7u\2\2\u00bc\u00bd")
        buf.write("\7k\2\2\u00bd\u00be\7q\2\2\u00be\u00bf\7p\2\2\u00bf\u00c0")
        buf.write("\7\"\2\2\u00c0\66\3\2\2\2\u00c1\u00c2\7U\2\2\u00c2\u00c3")
        buf.write("\7w\2\2\u00c3\u00c4\7r\2\2\u00c4\u00c5\7g\2\2\u00c5\u00c6")
        buf.write("\7t\2\2\u00c6\u00c7\7e\2\2\u00c7\u00c8\7n\2\2\u00c8\u00c9")
        buf.write("\7c\2\2\u00c9\u00ca\7u\2\2\u00ca\u00cb\7u\2\2\u00cb8\3")
        buf.write("\2\2\2\u00cc\u00cd\7k\2\2\u00cd\u00ce\7o\2\2\u00ce\u00cf")
        buf.write("\7r\2\2\u00cf\u00d0\7n\2\2\u00d0\u00d1\7g\2\2\u00d1\u00d2")
        buf.write("\7o\2\2\u00d2\u00d3\7g\2\2\u00d3\u00d4\7p\2\2\u00d4\u00d5")
        buf.write("\7v\2\2\u00d5\u00d6\7c\2\2\u00d6\u00d7\7v\2\2\u00d7\u00d8")
        buf.write("\7k\2\2\u00d8\u00d9\7q\2\2\u00d9\u00da\7p\2\2\u00da\u00db")
        buf.write("\7\"\2\2\u00db:\3\2\2\2\u00dc\u00dd\7K\2\2\u00dd\u00de")
        buf.write("\7p\2\2\u00de\u00df\7v\2\2\u00df\u00e0\7g\2\2\u00e0\u00e1")
        buf.write("\7t\2\2\u00e1\u00e2\7h\2\2\u00e2\u00e3\7c\2\2\u00e3\u00e4")
        buf.write("\7e\2\2\u00e4\u00e5\7g\2\2\u00e5\u00e6\7\"\2\2\u00e6<")
        buf.write("\3\2\2\2\u00e7\u00e8\7h\2\2\u00e8\u00e9\7w\2\2\u00e9\u00ea")
        buf.write("\7p\2\2\u00ea\u00eb\7e\2\2\u00eb\u00ec\7v\2\2\u00ec\u00ed")
        buf.write("\7k\2\2\u00ed\u00ee\7q\2\2\u00ee\u00ef\7p\2\2\u00ef\u00f0")
        buf.write("\7\"\2\2\u00f0>\3\2\2\2\u00f1\u00f2\7c\2\2\u00f2\u00f3")
        buf.write("\7d\2\2\u00f3\u00f4\7u\2\2\u00f4\u00f5\7v\2\2\u00f5\u00f6")
        buf.write("\7t\2\2\u00f6\u00f7\7c\2\2\u00f7\u00f8\7e\2\2\u00f8\u00f9")
        buf.write("\7v\2\2\u00f9\u00fa\7\"\2\2\u00fa\u00fb\7h\2\2\u00fb\u00fc")
        buf.write("\7w\2\2\u00fc\u00fd\7p\2\2\u00fd\u00fe\7e\2\2\u00fe\u00ff")
        buf.write("\7v\2\2\u00ff\u0100\7k\2\2\u0100\u0101\7q\2\2\u0101\u0102")
        buf.write("\7p\2\2\u0102\u0103\7\"\2\2\u0103@\3\2\2\2\u0104\u0105")
        buf.write("\7e\2\2\u0105\u0106\7q\2\2\u0106\u0107\7p\2\2\u0107\u0108")
        buf.write("\7u\2\2\u0108\u0109\7v\2\2\u0109\u010a\7t\2\2\u010a\u010b")
        buf.write("\7w\2\2\u010b\u010c\7e\2\2\u010c\u010d\7v\2\2\u010d\u010e")
        buf.write("\7q\2\2\u010e\u010f\7t\2\2\u010f\u0110\7\"\2\2\u0110B")
        buf.write("\3\2\2\2\u0111\u0112\7r\2\2\u0112\u0113\7c\2\2\u0113\u0114")
        buf.write("\7t\2\2\u0114\u0115\7c\2\2\u0115\u0116\7o\2\2\u0116\u0117")
        buf.write("\7g\2\2\u0117\u0118\7v\2\2\u0118\u0119\7g\2\2\u0119\u011a")
        buf.write("\7t\2\2\u011a\u011b\7\"\2\2\u011bD\3\2\2\2\u011c\u011d")
        buf.write("\7v\2\2\u011d\u011e\7{\2\2\u011e\u011f\7r\2\2\u011f\u0120")
        buf.write("\7g\2\2\u0120\u0121\7\"\2\2\u0121F\3\2\2\2\u0122\u0123")
        buf.write("\7u\2\2\u0123\u0124\7r\2\2\u0124\u0125\7g\2\2\u0125\u0126")
        buf.write("\7e\2\2\u0126\u0127\7k\2\2\u0127\u0128\7h\2\2\u0128\u0129")
        buf.write("\7k\2\2\u0129\u012a\7g\2\2\u012a\u012b\7t\2\2\u012b\u012c")
        buf.write("\7\"\2\2\u012cH\3\2\2\2\u012d\u012e\7x\2\2\u012e\u012f")
        buf.write("\7k\2\2\u012f\u0130\7u\2\2\u0130\u0131\7k\2\2\u0131\u0132")
        buf.write("\7d\2\2\u0132\u0133\7k\2\2\u0133\u0134\7n\2\2\u0134\u0135")
        buf.write("\7k\2\2\u0135\u0136\7v\2\2\u0136\u0137\7{\2\2\u0137\u0138")
        buf.write("\7\"\2\2\u0138J\3\2\2\2\u0139\u013a\7t\2\2\u013a\u013b")
        buf.write("\7g\2\2\u013b\u013c\7v\2\2\u013c\u013d\7w\2\2\u013d\u013e")
        buf.write("\7t\2\2\u013e\u013f\7p\2\2\u013f\u0140\7\"\2\2\u0140\u0141")
        buf.write("\7x\2\2\u0141\u0142\7c\2\2\u0142\u0143\7n\2\2\u0143\u0144")
        buf.write("\7w\2\2\u0144\u0145\7g\2\2\u0145\u0146\7\"\2\2\u0146L")
        buf.write("\3\2\2\2\u0147\u0148\7f\2\2\u0148\u0149\7g\2\2\u0149\u014a")
        buf.write("\7e\2\2\u014a\u014b\7n\2\2\u014b\u014c\7c\2\2\u014c\u014d")
        buf.write("\7t\2\2\u014d\u014e\7c\2\2\u014e\u014f\7v\2\2\u014f\u0150")
        buf.write("\7k\2\2\u0150\u0151\7q\2\2\u0151\u0152\7p\2\2\u0152\u0153")
        buf.write("\7\"\2\2\u0153\u0154\7u\2\2\u0154\u0155\7v\2\2\u0155\u0156")
        buf.write("\7c\2\2\u0156\u0157\7v\2\2\u0157\u0158\7g\2\2\u0158\u0159")
        buf.write("\7o\2\2\u0159\u015a\7g\2\2\u015a\u015b\7p\2\2\u015b\u015c")
        buf.write("\7v\2\2\u015c\u015d\7\"\2\2\u015dN\3\2\2\2\u015e\u015f")
        buf.write("\7g\2\2\u015f\u0160\7z\2\2\u0160\u0161\7r\2\2\u0161\u0162")
        buf.write("\7t\2\2\u0162\u0163\7g\2\2\u0163\u0164\7u\2\2\u0164\u0165")
        buf.write("\7u\2\2\u0165\u0166\7k\2\2\u0166\u0167\7q\2\2\u0167\u0168")
        buf.write("\7p\2\2\u0168\u0169\7\"\2\2\u0169\u016a\7u\2\2\u016a\u016b")
        buf.write("\7v\2\2\u016b\u016c\7c\2\2\u016c\u016d\7v\2\2\u016d\u016e")
        buf.write("\7g\2\2\u016e\u016f\7o\2\2\u016f\u0170\7g\2\2\u0170\u0171")
        buf.write("\7p\2\2\u0171\u0172\7v\2\2\u0172\u0173\7\"\2\2\u0173P")
        buf.write("\3\2\2\2\u0174\u0175\7x\2\2\u0175\u0176\7c\2\2\u0176\u0177")
        buf.write("\7n\2\2\u0177\u0178\7w\2\2\u0178\u0179\7g\2\2\u0179\u017a")
        buf.write("\7\"\2\2\u017aR\3\2\2\2\u017b\u017c\7k\2\2\u017c\u017d")
        buf.write("\7p\2\2\u017d\u017e\7k\2\2\u017e\u017f\7v\2\2\u017f\u0180")
        buf.write("\7k\2\2\u0180\u0181\7c\2\2\u0181\u0182\7n\2\2\u0182\u0183")
        buf.write("\7\"\2\2\u0183\u0184\7x\2\2\u0184\u0185\7c\2\2\u0185\u0186")
        buf.write("\7n\2\2\u0186\u0187\7w\2\2\u0187\u0188\7g\2\2\u0188\u0189")
        buf.write("\7\"\2\2\u0189T\3\2\2\2\u018a\u018b\7e\2\2\u018b\u018c")
        buf.write("\7n\2\2\u018c\u018d\7c\2\2\u018d\u018e\7u\2\2\u018e\u018f")
        buf.write("\7u\2\2\u018f\u0190\7\"\2\2\u0190V\3\2\2\2\u0191\u0192")
        buf.write("\7u\2\2\u0192\u0193\7w\2\2\u0193\u0194\7d\2\2\u0194\u0195")
        buf.write("\7e\2\2\u0195\u0196\7n\2\2\u0196\u0197\7c\2\2\u0197\u0198")
        buf.write("\7u\2\2\u0198\u0199\7u\2\2\u0199\u019a\7\"\2\2\u019aX")
        buf.write("\3\2\2\2\4\2\u009a\2")
        return buf.getvalue()


class RulepadGrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    SPACE = 19
    Alphabet = 20
    NL = 21
    LPAREN = 22
    RPAREN = 23
    NAME = 24
    ANNOTATION = 25
    EXTENSION = 26
    SUPERCLASS = 27
    IMPLEMENTATION = 28
    INTERFACE = 29
    FUNCTION = 30
    AbstractFunctions = 31
    CONSTRUCTOR = 32
    PARAMETER = 33
    TYPES = 34
    SPECIFIER = 35
    VISIBILITY = 36
    ReturnValue = 37
    DeclarationStatement = 38
    ExpressionStatement = 39
    VALUE = 40
    InitialValue = 41
    CLASSES = 42
    SUBCLASSES = 43

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\"'", "'||'", "'&&'", "'!'", "'...'", "'!...'", "'.'", "'='", 
            "'>'", "'<'", "'''", "'&'", "'must '", "'of '", "'and '", "'or '", 
            "'have '", "'with '", "'('", "')'", "'name '", "'annotation '", 
            "'extension '", "'Superclass'", "'implementation '", "'Interface '", 
            "'function '", "'abstract function '", "'constructor '", "'parameter '", 
            "'type '", "'specifier '", "'visibility '", "'return value '", 
            "'declaration statement '", "'expression statement '", "'value '", 
            "'initial value '", "'class '", "'subclass '" ]

    symbolicNames = [ "<INVALID>",
            "SPACE", "Alphabet", "NL", "LPAREN", "RPAREN", "NAME", "ANNOTATION", 
            "EXTENSION", "SUPERCLASS", "IMPLEMENTATION", "INTERFACE", "FUNCTION", 
            "AbstractFunctions", "CONSTRUCTOR", "PARAMETER", "TYPES", "SPECIFIER", 
            "VISIBILITY", "ReturnValue", "DeclarationStatement", "ExpressionStatement", 
            "VALUE", "InitialValue", "CLASSES", "SUBCLASSES" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "SPACE", "Alphabet", 
                  "NL", "LPAREN", "RPAREN", "NAME", "ANNOTATION", "EXTENSION", 
                  "SUPERCLASS", "IMPLEMENTATION", "INTERFACE", "FUNCTION", 
                  "AbstractFunctions", "CONSTRUCTOR", "PARAMETER", "TYPES", 
                  "SPECIFIER", "VISIBILITY", "ReturnValue", "DeclarationStatement", 
                  "ExpressionStatement", "VALUE", "InitialValue", "CLASSES", 
                  "SUBCLASSES" ]

    grammarFileName = "RulepadGrammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


