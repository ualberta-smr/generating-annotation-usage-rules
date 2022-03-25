# Generated from ../violation-detection/src/main/antlr4/ca/ualberta/grammar/RulepadGrammar.g4 by ANTLR 4.9
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2/")
        buf.write("\u01c4\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3")
        buf.write("\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13")
        buf.write("\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\24\6\24\u009d\n\24\r\24\16\24\u009e")
        buf.write("\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3")
        buf.write("!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3")
        buf.write("$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3")
        buf.write("&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'")
        buf.write("\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\5\'\u0168")
        buf.write("\n\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3")
        buf.write("(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\3")
        buf.write("*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3")
        buf.write("+\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3")
        buf.write(",\3,\3,\3,\3-\3-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(".\3.\3.\2\2/\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26")
        buf.write("+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#")
        buf.write("E$G%I&K\'M(O)Q*S+U,W-Y.[/\3\2\5\4\2\13\13\"\"\7\2//\62")
        buf.write(";C\\aac|\4\2\f\f\17\17\2\u01c5\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3")
        buf.write("\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2")
        buf.write("\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3")
        buf.write("\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2")
        buf.write("\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3")
        buf.write("\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E")
        buf.write("\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2")
        buf.write("O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2")
        buf.write("\2Y\3\2\2\2\2[\3\2\2\2\3]\3\2\2\2\5_\3\2\2\2\7b\3\2\2")
        buf.write("\2\te\3\2\2\2\13g\3\2\2\2\rk\3\2\2\2\17p\3\2\2\2\21r\3")
        buf.write("\2\2\2\23t\3\2\2\2\25v\3\2\2\2\27x\3\2\2\2\31z\3\2\2\2")
        buf.write("\33|\3\2\2\2\35\u0082\3\2\2\2\37\u0086\3\2\2\2!\u008b")
        buf.write("\3\2\2\2#\u008f\3\2\2\2%\u0095\3\2\2\2\'\u009c\3\2\2\2")
        buf.write(")\u00a0\3\2\2\2+\u00a2\3\2\2\2-\u00a4\3\2\2\2/\u00a6\3")
        buf.write("\2\2\2\61\u00a8\3\2\2\2\63\u00ae\3\2\2\2\65\u00ba\3\2")
        buf.write("\2\2\67\u00c5\3\2\2\29\u00d0\3\2\2\2;\u00e0\3\2\2\2=\u00eb")
        buf.write("\3\2\2\2?\u00f5\3\2\2\2A\u0108\3\2\2\2C\u0115\3\2\2\2")
        buf.write("E\u0120\3\2\2\2G\u0126\3\2\2\2I\u0131\3\2\2\2K\u013d\3")
        buf.write("\2\2\2M\u0167\3\2\2\2O\u0169\3\2\2\2Q\u017d\3\2\2\2S\u0187")
        buf.write("\3\2\2\2U\u019d\3\2\2\2W\u01a4\3\2\2\2Y\u01b3\3\2\2\2")
        buf.write("[\u01ba\3\2\2\2]^\7$\2\2^\4\3\2\2\2_`\7~\2\2`a\7~\2\2")
        buf.write("a\6\3\2\2\2bc\7(\2\2cd\7(\2\2d\b\3\2\2\2ef\7#\2\2f\n\3")
        buf.write("\2\2\2gh\7\60\2\2hi\7\60\2\2ij\7\60\2\2j\f\3\2\2\2kl\7")
        buf.write("#\2\2lm\7\60\2\2mn\7\60\2\2no\7\60\2\2o\16\3\2\2\2pq\7")
        buf.write("\60\2\2q\20\3\2\2\2rs\7?\2\2s\22\3\2\2\2tu\7@\2\2u\24")
        buf.write("\3\2\2\2vw\7>\2\2w\26\3\2\2\2xy\7)\2\2y\30\3\2\2\2z{\7")
        buf.write("(\2\2{\32\3\2\2\2|}\7o\2\2}~\7w\2\2~\177\7u\2\2\177\u0080")
        buf.write("\7v\2\2\u0080\u0081\7\"\2\2\u0081\34\3\2\2\2\u0082\u0083")
        buf.write("\7q\2\2\u0083\u0084\7h\2\2\u0084\u0085\7\"\2\2\u0085\36")
        buf.write("\3\2\2\2\u0086\u0087\7c\2\2\u0087\u0088\7p\2\2\u0088\u0089")
        buf.write("\7f\2\2\u0089\u008a\7\"\2\2\u008a \3\2\2\2\u008b\u008c")
        buf.write("\7q\2\2\u008c\u008d\7t\2\2\u008d\u008e\7\"\2\2\u008e\"")
        buf.write("\3\2\2\2\u008f\u0090\7j\2\2\u0090\u0091\7c\2\2\u0091\u0092")
        buf.write("\7x\2\2\u0092\u0093\7g\2\2\u0093\u0094\7\"\2\2\u0094$")
        buf.write("\3\2\2\2\u0095\u0096\7y\2\2\u0096\u0097\7k\2\2\u0097\u0098")
        buf.write("\7v\2\2\u0098\u0099\7j\2\2\u0099\u009a\7\"\2\2\u009a&")
        buf.write("\3\2\2\2\u009b\u009d\t\2\2\2\u009c\u009b\3\2\2\2\u009d")
        buf.write("\u009e\3\2\2\2\u009e\u009c\3\2\2\2\u009e\u009f\3\2\2\2")
        buf.write("\u009f(\3\2\2\2\u00a0\u00a1\t\3\2\2\u00a1*\3\2\2\2\u00a2")
        buf.write("\u00a3\t\4\2\2\u00a3,\3\2\2\2\u00a4\u00a5\7*\2\2\u00a5")
        buf.write(".\3\2\2\2\u00a6\u00a7\7+\2\2\u00a7\60\3\2\2\2\u00a8\u00a9")
        buf.write("\7p\2\2\u00a9\u00aa\7c\2\2\u00aa\u00ab\7o\2\2\u00ab\u00ac")
        buf.write("\7g\2\2\u00ac\u00ad\7\"\2\2\u00ad\62\3\2\2\2\u00ae\u00af")
        buf.write("\7c\2\2\u00af\u00b0\7p\2\2\u00b0\u00b1\7p\2\2\u00b1\u00b2")
        buf.write("\7q\2\2\u00b2\u00b3\7v\2\2\u00b3\u00b4\7c\2\2\u00b4\u00b5")
        buf.write("\7v\2\2\u00b5\u00b6\7k\2\2\u00b6\u00b7\7q\2\2\u00b7\u00b8")
        buf.write("\7p\2\2\u00b8\u00b9\7\"\2\2\u00b9\64\3\2\2\2\u00ba\u00bb")
        buf.write("\7g\2\2\u00bb\u00bc\7z\2\2\u00bc\u00bd\7v\2\2\u00bd\u00be")
        buf.write("\7g\2\2\u00be\u00bf\7p\2\2\u00bf\u00c0\7u\2\2\u00c0\u00c1")
        buf.write("\7k\2\2\u00c1\u00c2\7q\2\2\u00c2\u00c3\7p\2\2\u00c3\u00c4")
        buf.write("\7\"\2\2\u00c4\66\3\2\2\2\u00c5\u00c6\7U\2\2\u00c6\u00c7")
        buf.write("\7w\2\2\u00c7\u00c8\7r\2\2\u00c8\u00c9\7g\2\2\u00c9\u00ca")
        buf.write("\7t\2\2\u00ca\u00cb\7e\2\2\u00cb\u00cc\7n\2\2\u00cc\u00cd")
        buf.write("\7c\2\2\u00cd\u00ce\7u\2\2\u00ce\u00cf\7u\2\2\u00cf8\3")
        buf.write("\2\2\2\u00d0\u00d1\7k\2\2\u00d1\u00d2\7o\2\2\u00d2\u00d3")
        buf.write("\7r\2\2\u00d3\u00d4\7n\2\2\u00d4\u00d5\7g\2\2\u00d5\u00d6")
        buf.write("\7o\2\2\u00d6\u00d7\7g\2\2\u00d7\u00d8\7p\2\2\u00d8\u00d9")
        buf.write("\7v\2\2\u00d9\u00da\7c\2\2\u00da\u00db\7v\2\2\u00db\u00dc")
        buf.write("\7k\2\2\u00dc\u00dd\7q\2\2\u00dd\u00de\7p\2\2\u00de\u00df")
        buf.write("\7\"\2\2\u00df:\3\2\2\2\u00e0\u00e1\7K\2\2\u00e1\u00e2")
        buf.write("\7p\2\2\u00e2\u00e3\7v\2\2\u00e3\u00e4\7g\2\2\u00e4\u00e5")
        buf.write("\7t\2\2\u00e5\u00e6\7h\2\2\u00e6\u00e7\7c\2\2\u00e7\u00e8")
        buf.write("\7e\2\2\u00e8\u00e9\7g\2\2\u00e9\u00ea\7\"\2\2\u00ea<")
        buf.write("\3\2\2\2\u00eb\u00ec\7h\2\2\u00ec\u00ed\7w\2\2\u00ed\u00ee")
        buf.write("\7p\2\2\u00ee\u00ef\7e\2\2\u00ef\u00f0\7v\2\2\u00f0\u00f1")
        buf.write("\7k\2\2\u00f1\u00f2\7q\2\2\u00f2\u00f3\7p\2\2\u00f3\u00f4")
        buf.write("\7\"\2\2\u00f4>\3\2\2\2\u00f5\u00f6\7c\2\2\u00f6\u00f7")
        buf.write("\7d\2\2\u00f7\u00f8\7u\2\2\u00f8\u00f9\7v\2\2\u00f9\u00fa")
        buf.write("\7t\2\2\u00fa\u00fb\7c\2\2\u00fb\u00fc\7e\2\2\u00fc\u00fd")
        buf.write("\7v\2\2\u00fd\u00fe\7\"\2\2\u00fe\u00ff\7h\2\2\u00ff\u0100")
        buf.write("\7w\2\2\u0100\u0101\7p\2\2\u0101\u0102\7e\2\2\u0102\u0103")
        buf.write("\7v\2\2\u0103\u0104\7k\2\2\u0104\u0105\7q\2\2\u0105\u0106")
        buf.write("\7p\2\2\u0106\u0107\7\"\2\2\u0107@\3\2\2\2\u0108\u0109")
        buf.write("\7e\2\2\u0109\u010a\7q\2\2\u010a\u010b\7p\2\2\u010b\u010c")
        buf.write("\7u\2\2\u010c\u010d\7v\2\2\u010d\u010e\7t\2\2\u010e\u010f")
        buf.write("\7w\2\2\u010f\u0110\7e\2\2\u0110\u0111\7v\2\2\u0111\u0112")
        buf.write("\7q\2\2\u0112\u0113\7t\2\2\u0113\u0114\7\"\2\2\u0114B")
        buf.write("\3\2\2\2\u0115\u0116\7r\2\2\u0116\u0117\7c\2\2\u0117\u0118")
        buf.write("\7t\2\2\u0118\u0119\7c\2\2\u0119\u011a\7o\2\2\u011a\u011b")
        buf.write("\7g\2\2\u011b\u011c\7v\2\2\u011c\u011d\7g\2\2\u011d\u011e")
        buf.write("\7t\2\2\u011e\u011f\7\"\2\2\u011fD\3\2\2\2\u0120\u0121")
        buf.write("\7v\2\2\u0121\u0122\7{\2\2\u0122\u0123\7r\2\2\u0123\u0124")
        buf.write("\7g\2\2\u0124\u0125\7\"\2\2\u0125F\3\2\2\2\u0126\u0127")
        buf.write("\7u\2\2\u0127\u0128\7r\2\2\u0128\u0129\7g\2\2\u0129\u012a")
        buf.write("\7e\2\2\u012a\u012b\7k\2\2\u012b\u012c\7h\2\2\u012c\u012d")
        buf.write("\7k\2\2\u012d\u012e\7g\2\2\u012e\u012f\7t\2\2\u012f\u0130")
        buf.write("\7\"\2\2\u0130H\3\2\2\2\u0131\u0132\7x\2\2\u0132\u0133")
        buf.write("\7k\2\2\u0133\u0134\7u\2\2\u0134\u0135\7k\2\2\u0135\u0136")
        buf.write("\7d\2\2\u0136\u0137\7k\2\2\u0137\u0138\7n\2\2\u0138\u0139")
        buf.write("\7k\2\2\u0139\u013a\7v\2\2\u013a\u013b\7{\2\2\u013b\u013c")
        buf.write("\7\"\2\2\u013cJ\3\2\2\2\u013d\u013e\7t\2\2\u013e\u013f")
        buf.write("\7g\2\2\u013f\u0140\7v\2\2\u0140\u0141\7w\2\2\u0141\u0142")
        buf.write("\7t\2\2\u0142\u0143\7p\2\2\u0143\u0144\7\"\2\2\u0144\u0145")
        buf.write("\7x\2\2\u0145\u0146\7c\2\2\u0146\u0147\7n\2\2\u0147\u0148")
        buf.write("\7w\2\2\u0148\u0149\7g\2\2\u0149\u014a\7\"\2\2\u014aL")
        buf.write("\3\2\2\2\u014b\u014c\7f\2\2\u014c\u014d\7g\2\2\u014d\u014e")
        buf.write("\7e\2\2\u014e\u014f\7n\2\2\u014f\u0150\7c\2\2\u0150\u0151")
        buf.write("\7t\2\2\u0151\u0152\7c\2\2\u0152\u0153\7v\2\2\u0153\u0154")
        buf.write("\7k\2\2\u0154\u0155\7q\2\2\u0155\u0156\7p\2\2\u0156\u0157")
        buf.write("\7\"\2\2\u0157\u0158\7u\2\2\u0158\u0159\7v\2\2\u0159\u015a")
        buf.write("\7c\2\2\u015a\u015b\7v\2\2\u015b\u015c\7g\2\2\u015c\u015d")
        buf.write("\7o\2\2\u015d\u015e\7g\2\2\u015e\u015f\7p\2\2\u015f\u0160")
        buf.write("\7v\2\2\u0160\u0168\7\"\2\2\u0161\u0162\7h\2\2\u0162\u0163")
        buf.write("\7k\2\2\u0163\u0164\7g\2\2\u0164\u0165\7n\2\2\u0165\u0166")
        buf.write("\7f\2\2\u0166\u0168\7\"\2\2\u0167\u014b\3\2\2\2\u0167")
        buf.write("\u0161\3\2\2\2\u0168N\3\2\2\2\u0169\u016a\7e\2\2\u016a")
        buf.write("\u016b\7q\2\2\u016b\u016c\7p\2\2\u016c\u016d\7h\2\2\u016d")
        buf.write("\u016e\7k\2\2\u016e\u016f\7i\2\2\u016f\u0170\7w\2\2\u0170")
        buf.write("\u0171\7t\2\2\u0171\u0172\7c\2\2\u0172\u0173\7v\2\2\u0173")
        buf.write("\u0174\7k\2\2\u0174\u0175\7q\2\2\u0175\u0176\7p\2\2\u0176")
        buf.write("\u0177\7\"\2\2\u0177\u0178\7h\2\2\u0178\u0179\7k\2\2\u0179")
        buf.write("\u017a\7n\2\2\u017a\u017b\7g\2\2\u017b\u017c\7\"\2\2\u017c")
        buf.write("P\3\2\2\2\u017d\u017e\7r\2\2\u017e\u017f\7t\2\2\u017f")
        buf.write("\u0180\7q\2\2\u0180\u0181\7r\2\2\u0181\u0182\7g\2\2\u0182")
        buf.write("\u0183\7t\2\2\u0183\u0184\7v\2\2\u0184\u0185\7{\2\2\u0185")
        buf.write("\u0186\7\"\2\2\u0186R\3\2\2\2\u0187\u0188\7g\2\2\u0188")
        buf.write("\u0189\7z\2\2\u0189\u018a\7r\2\2\u018a\u018b\7t\2\2\u018b")
        buf.write("\u018c\7g\2\2\u018c\u018d\7u\2\2\u018d\u018e\7u\2\2\u018e")
        buf.write("\u018f\7k\2\2\u018f\u0190\7q\2\2\u0190\u0191\7p\2\2\u0191")
        buf.write("\u0192\7\"\2\2\u0192\u0193\7u\2\2\u0193\u0194\7v\2\2\u0194")
        buf.write("\u0195\7c\2\2\u0195\u0196\7v\2\2\u0196\u0197\7g\2\2\u0197")
        buf.write("\u0198\7o\2\2\u0198\u0199\7g\2\2\u0199\u019a\7p\2\2\u019a")
        buf.write("\u019b\7v\2\2\u019b\u019c\7\"\2\2\u019cT\3\2\2\2\u019d")
        buf.write("\u019e\7x\2\2\u019e\u019f\7c\2\2\u019f\u01a0\7n\2\2\u01a0")
        buf.write("\u01a1\7w\2\2\u01a1\u01a2\7g\2\2\u01a2\u01a3\7\"\2\2\u01a3")
        buf.write("V\3\2\2\2\u01a4\u01a5\7k\2\2\u01a5\u01a6\7p\2\2\u01a6")
        buf.write("\u01a7\7k\2\2\u01a7\u01a8\7v\2\2\u01a8\u01a9\7k\2\2\u01a9")
        buf.write("\u01aa\7c\2\2\u01aa\u01ab\7n\2\2\u01ab\u01ac\7\"\2\2\u01ac")
        buf.write("\u01ad\7x\2\2\u01ad\u01ae\7c\2\2\u01ae\u01af\7n\2\2\u01af")
        buf.write("\u01b0\7w\2\2\u01b0\u01b1\7g\2\2\u01b1\u01b2\7\"\2\2\u01b2")
        buf.write("X\3\2\2\2\u01b3\u01b4\7e\2\2\u01b4\u01b5\7n\2\2\u01b5")
        buf.write("\u01b6\7c\2\2\u01b6\u01b7\7u\2\2\u01b7\u01b8\7u\2\2\u01b8")
        buf.write("\u01b9\7\"\2\2\u01b9Z\3\2\2\2\u01ba\u01bb\7u\2\2\u01bb")
        buf.write("\u01bc\7w\2\2\u01bc\u01bd\7d\2\2\u01bd\u01be\7e\2\2\u01be")
        buf.write("\u01bf\7n\2\2\u01bf\u01c0\7c\2\2\u01c0\u01c1\7u\2\2\u01c1")
        buf.write("\u01c2\7u\2\2\u01c2\u01c3\7\"\2\2\u01c3\\\3\2\2\2\5\2")
        buf.write("\u009e\u0167\2")
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
    ConfigurationFile = 39
    CONFIGURATION_PROPERTIES = 40
    ExpressionStatement = 41
    VALUE = 42
    InitialValue = 43
    CLASSES = 44
    SUBCLASSES = 45

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\"'", "'||'", "'&&'", "'!'", "'...'", "'!...'", "'.'", "'='", 
            "'>'", "'<'", "'''", "'&'", "'must '", "'of '", "'and '", "'or '", 
            "'have '", "'with '", "'('", "')'", "'name '", "'annotation '", 
            "'extension '", "'Superclass'", "'implementation '", "'Interface '", 
            "'function '", "'abstract function '", "'constructor '", "'parameter '", 
            "'type '", "'specifier '", "'visibility '", "'return value '", 
            "'configuration file '", "'property '", "'expression statement '", 
            "'value '", "'initial value '", "'class '", "'subclass '" ]

    symbolicNames = [ "<INVALID>",
            "SPACE", "Alphabet", "NL", "LPAREN", "RPAREN", "NAME", "ANNOTATION", 
            "EXTENSION", "SUPERCLASS", "IMPLEMENTATION", "INTERFACE", "FUNCTION", 
            "AbstractFunctions", "CONSTRUCTOR", "PARAMETER", "TYPES", "SPECIFIER", 
            "VISIBILITY", "ReturnValue", "DeclarationStatement", "ConfigurationFile", 
            "CONFIGURATION_PROPERTIES", "ExpressionStatement", "VALUE", 
            "InitialValue", "CLASSES", "SUBCLASSES" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "SPACE", "Alphabet", 
                  "NL", "LPAREN", "RPAREN", "NAME", "ANNOTATION", "EXTENSION", 
                  "SUPERCLASS", "IMPLEMENTATION", "INTERFACE", "FUNCTION", 
                  "AbstractFunctions", "CONSTRUCTOR", "PARAMETER", "TYPES", 
                  "SPECIFIER", "VISIBILITY", "ReturnValue", "DeclarationStatement", 
                  "ConfigurationFile", "CONFIGURATION_PROPERTIES", "ExpressionStatement", 
                  "VALUE", "InitialValue", "CLASSES", "SUBCLASSES" ]

    grammarFileName = "RulepadGrammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


