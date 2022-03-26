# Generated from ../violation-detection/src/main/antlr4/ca/ualberta/grammar/RulepadGrammar.g4 by ANTLR 4.9
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\62")
        buf.write("\u01d0\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\3\2\3\2\3\3\3\3\3\3\3\4")
        buf.write("\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16")
        buf.write("\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\27\6\27\u00a9\n\27\r\27\16\27\u00aa")
        buf.write("\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 ")
        buf.write("\3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3")
        buf.write("#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3")
        buf.write("$\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3")
        buf.write("%\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3)\3)\3")
        buf.write(")\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3")
        buf.write("*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3")
        buf.write("*\3*\3*\3*\5*\u0174\n*\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3")
        buf.write("+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3,\3,\3")
        buf.write(",\3,\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3")
        buf.write("-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3.\3/\3/\3/\3/\3/\3")
        buf.write("/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\2\2\62\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26")
        buf.write("+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#")
        buf.write("E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62\3\2\5\4\2\13\13")
        buf.write("\"\"\7\2//\62;C\\aac|\4\2\f\f\17\17\2\u01d1\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3")
        buf.write("\2\2\2\2a\3\2\2\2\3c\3\2\2\2\5e\3\2\2\2\7h\3\2\2\2\tk")
        buf.write("\3\2\2\2\13m\3\2\2\2\rq\3\2\2\2\17v\3\2\2\2\21x\3\2\2")
        buf.write("\2\23z\3\2\2\2\25|\3\2\2\2\27~\3\2\2\2\31\u0080\3\2\2")
        buf.write("\2\33\u0082\3\2\2\2\35\u0084\3\2\2\2\37\u0086\3\2\2\2")
        buf.write("!\u0088\3\2\2\2#\u008e\3\2\2\2%\u0092\3\2\2\2\'\u0097")
        buf.write("\3\2\2\2)\u009b\3\2\2\2+\u00a1\3\2\2\2-\u00a8\3\2\2\2")
        buf.write("/\u00ac\3\2\2\2\61\u00ae\3\2\2\2\63\u00b0\3\2\2\2\65\u00b2")
        buf.write("\3\2\2\2\67\u00b4\3\2\2\29\u00ba\3\2\2\2;\u00c6\3\2\2")
        buf.write("\2=\u00d1\3\2\2\2?\u00dc\3\2\2\2A\u00ec\3\2\2\2C\u00f7")
        buf.write("\3\2\2\2E\u0101\3\2\2\2G\u0114\3\2\2\2I\u0121\3\2\2\2")
        buf.write("K\u012c\3\2\2\2M\u0132\3\2\2\2O\u013d\3\2\2\2Q\u0149\3")
        buf.write("\2\2\2S\u0173\3\2\2\2U\u0175\3\2\2\2W\u0189\3\2\2\2Y\u0193")
        buf.write("\3\2\2\2[\u01a9\3\2\2\2]\u01b0\3\2\2\2_\u01bf\3\2\2\2")
        buf.write("a\u01c6\3\2\2\2cd\7$\2\2d\4\3\2\2\2ef\7~\2\2fg\7~\2\2")
        buf.write("g\6\3\2\2\2hi\7(\2\2ij\7(\2\2j\b\3\2\2\2kl\7#\2\2l\n\3")
        buf.write("\2\2\2mn\7\60\2\2no\7\60\2\2op\7\60\2\2p\f\3\2\2\2qr\7")
        buf.write("#\2\2rs\7\60\2\2st\7\60\2\2tu\7\60\2\2u\16\3\2\2\2vw\7")
        buf.write("\60\2\2w\20\3\2\2\2xy\7?\2\2y\22\3\2\2\2z{\7@\2\2{\24")
        buf.write("\3\2\2\2|}\7>\2\2}\26\3\2\2\2~\177\7)\2\2\177\30\3\2\2")
        buf.write("\2\u0080\u0081\7(\2\2\u0081\32\3\2\2\2\u0082\u0083\7~")
        buf.write("\2\2\u0083\34\3\2\2\2\u0084\u0085\7]\2\2\u0085\36\3\2")
        buf.write("\2\2\u0086\u0087\7_\2\2\u0087 \3\2\2\2\u0088\u0089\7o")
        buf.write("\2\2\u0089\u008a\7w\2\2\u008a\u008b\7u\2\2\u008b\u008c")
        buf.write("\7v\2\2\u008c\u008d\7\"\2\2\u008d\"\3\2\2\2\u008e\u008f")
        buf.write("\7q\2\2\u008f\u0090\7h\2\2\u0090\u0091\7\"\2\2\u0091$")
        buf.write("\3\2\2\2\u0092\u0093\7c\2\2\u0093\u0094\7p\2\2\u0094\u0095")
        buf.write("\7f\2\2\u0095\u0096\7\"\2\2\u0096&\3\2\2\2\u0097\u0098")
        buf.write("\7q\2\2\u0098\u0099\7t\2\2\u0099\u009a\7\"\2\2\u009a(")
        buf.write("\3\2\2\2\u009b\u009c\7j\2\2\u009c\u009d\7c\2\2\u009d\u009e")
        buf.write("\7x\2\2\u009e\u009f\7g\2\2\u009f\u00a0\7\"\2\2\u00a0*")
        buf.write("\3\2\2\2\u00a1\u00a2\7y\2\2\u00a2\u00a3\7k\2\2\u00a3\u00a4")
        buf.write("\7v\2\2\u00a4\u00a5\7j\2\2\u00a5\u00a6\7\"\2\2\u00a6,")
        buf.write("\3\2\2\2\u00a7\u00a9\t\2\2\2\u00a8\u00a7\3\2\2\2\u00a9")
        buf.write("\u00aa\3\2\2\2\u00aa\u00a8\3\2\2\2\u00aa\u00ab\3\2\2\2")
        buf.write("\u00ab.\3\2\2\2\u00ac\u00ad\t\3\2\2\u00ad\60\3\2\2\2\u00ae")
        buf.write("\u00af\t\4\2\2\u00af\62\3\2\2\2\u00b0\u00b1\7*\2\2\u00b1")
        buf.write("\64\3\2\2\2\u00b2\u00b3\7+\2\2\u00b3\66\3\2\2\2\u00b4")
        buf.write("\u00b5\7p\2\2\u00b5\u00b6\7c\2\2\u00b6\u00b7\7o\2\2\u00b7")
        buf.write("\u00b8\7g\2\2\u00b8\u00b9\7\"\2\2\u00b98\3\2\2\2\u00ba")
        buf.write("\u00bb\7c\2\2\u00bb\u00bc\7p\2\2\u00bc\u00bd\7p\2\2\u00bd")
        buf.write("\u00be\7q\2\2\u00be\u00bf\7v\2\2\u00bf\u00c0\7c\2\2\u00c0")
        buf.write("\u00c1\7v\2\2\u00c1\u00c2\7k\2\2\u00c2\u00c3\7q\2\2\u00c3")
        buf.write("\u00c4\7p\2\2\u00c4\u00c5\7\"\2\2\u00c5:\3\2\2\2\u00c6")
        buf.write("\u00c7\7g\2\2\u00c7\u00c8\7z\2\2\u00c8\u00c9\7v\2\2\u00c9")
        buf.write("\u00ca\7g\2\2\u00ca\u00cb\7p\2\2\u00cb\u00cc\7u\2\2\u00cc")
        buf.write("\u00cd\7k\2\2\u00cd\u00ce\7q\2\2\u00ce\u00cf\7p\2\2\u00cf")
        buf.write("\u00d0\7\"\2\2\u00d0<\3\2\2\2\u00d1\u00d2\7U\2\2\u00d2")
        buf.write("\u00d3\7w\2\2\u00d3\u00d4\7r\2\2\u00d4\u00d5\7g\2\2\u00d5")
        buf.write("\u00d6\7t\2\2\u00d6\u00d7\7e\2\2\u00d7\u00d8\7n\2\2\u00d8")
        buf.write("\u00d9\7c\2\2\u00d9\u00da\7u\2\2\u00da\u00db\7u\2\2\u00db")
        buf.write(">\3\2\2\2\u00dc\u00dd\7k\2\2\u00dd\u00de\7o\2\2\u00de")
        buf.write("\u00df\7r\2\2\u00df\u00e0\7n\2\2\u00e0\u00e1\7g\2\2\u00e1")
        buf.write("\u00e2\7o\2\2\u00e2\u00e3\7g\2\2\u00e3\u00e4\7p\2\2\u00e4")
        buf.write("\u00e5\7v\2\2\u00e5\u00e6\7c\2\2\u00e6\u00e7\7v\2\2\u00e7")
        buf.write("\u00e8\7k\2\2\u00e8\u00e9\7q\2\2\u00e9\u00ea\7p\2\2\u00ea")
        buf.write("\u00eb\7\"\2\2\u00eb@\3\2\2\2\u00ec\u00ed\7K\2\2\u00ed")
        buf.write("\u00ee\7p\2\2\u00ee\u00ef\7v\2\2\u00ef\u00f0\7g\2\2\u00f0")
        buf.write("\u00f1\7t\2\2\u00f1\u00f2\7h\2\2\u00f2\u00f3\7c\2\2\u00f3")
        buf.write("\u00f4\7e\2\2\u00f4\u00f5\7g\2\2\u00f5\u00f6\7\"\2\2\u00f6")
        buf.write("B\3\2\2\2\u00f7\u00f8\7h\2\2\u00f8\u00f9\7w\2\2\u00f9")
        buf.write("\u00fa\7p\2\2\u00fa\u00fb\7e\2\2\u00fb\u00fc\7v\2\2\u00fc")
        buf.write("\u00fd\7k\2\2\u00fd\u00fe\7q\2\2\u00fe\u00ff\7p\2\2\u00ff")
        buf.write("\u0100\7\"\2\2\u0100D\3\2\2\2\u0101\u0102\7c\2\2\u0102")
        buf.write("\u0103\7d\2\2\u0103\u0104\7u\2\2\u0104\u0105\7v\2\2\u0105")
        buf.write("\u0106\7t\2\2\u0106\u0107\7c\2\2\u0107\u0108\7e\2\2\u0108")
        buf.write("\u0109\7v\2\2\u0109\u010a\7\"\2\2\u010a\u010b\7h\2\2\u010b")
        buf.write("\u010c\7w\2\2\u010c\u010d\7p\2\2\u010d\u010e\7e\2\2\u010e")
        buf.write("\u010f\7v\2\2\u010f\u0110\7k\2\2\u0110\u0111\7q\2\2\u0111")
        buf.write("\u0112\7p\2\2\u0112\u0113\7\"\2\2\u0113F\3\2\2\2\u0114")
        buf.write("\u0115\7e\2\2\u0115\u0116\7q\2\2\u0116\u0117\7p\2\2\u0117")
        buf.write("\u0118\7u\2\2\u0118\u0119\7v\2\2\u0119\u011a\7t\2\2\u011a")
        buf.write("\u011b\7w\2\2\u011b\u011c\7e\2\2\u011c\u011d\7v\2\2\u011d")
        buf.write("\u011e\7q\2\2\u011e\u011f\7t\2\2\u011f\u0120\7\"\2\2\u0120")
        buf.write("H\3\2\2\2\u0121\u0122\7r\2\2\u0122\u0123\7c\2\2\u0123")
        buf.write("\u0124\7t\2\2\u0124\u0125\7c\2\2\u0125\u0126\7o\2\2\u0126")
        buf.write("\u0127\7g\2\2\u0127\u0128\7v\2\2\u0128\u0129\7g\2\2\u0129")
        buf.write("\u012a\7t\2\2\u012a\u012b\7\"\2\2\u012bJ\3\2\2\2\u012c")
        buf.write("\u012d\7v\2\2\u012d\u012e\7{\2\2\u012e\u012f\7r\2\2\u012f")
        buf.write("\u0130\7g\2\2\u0130\u0131\7\"\2\2\u0131L\3\2\2\2\u0132")
        buf.write("\u0133\7u\2\2\u0133\u0134\7r\2\2\u0134\u0135\7g\2\2\u0135")
        buf.write("\u0136\7e\2\2\u0136\u0137\7k\2\2\u0137\u0138\7h\2\2\u0138")
        buf.write("\u0139\7k\2\2\u0139\u013a\7g\2\2\u013a\u013b\7t\2\2\u013b")
        buf.write("\u013c\7\"\2\2\u013cN\3\2\2\2\u013d\u013e\7x\2\2\u013e")
        buf.write("\u013f\7k\2\2\u013f\u0140\7u\2\2\u0140\u0141\7k\2\2\u0141")
        buf.write("\u0142\7d\2\2\u0142\u0143\7k\2\2\u0143\u0144\7n\2\2\u0144")
        buf.write("\u0145\7k\2\2\u0145\u0146\7v\2\2\u0146\u0147\7{\2\2\u0147")
        buf.write("\u0148\7\"\2\2\u0148P\3\2\2\2\u0149\u014a\7t\2\2\u014a")
        buf.write("\u014b\7g\2\2\u014b\u014c\7v\2\2\u014c\u014d\7w\2\2\u014d")
        buf.write("\u014e\7t\2\2\u014e\u014f\7p\2\2\u014f\u0150\7\"\2\2\u0150")
        buf.write("\u0151\7x\2\2\u0151\u0152\7c\2\2\u0152\u0153\7n\2\2\u0153")
        buf.write("\u0154\7w\2\2\u0154\u0155\7g\2\2\u0155\u0156\7\"\2\2\u0156")
        buf.write("R\3\2\2\2\u0157\u0158\7f\2\2\u0158\u0159\7g\2\2\u0159")
        buf.write("\u015a\7e\2\2\u015a\u015b\7n\2\2\u015b\u015c\7c\2\2\u015c")
        buf.write("\u015d\7t\2\2\u015d\u015e\7c\2\2\u015e\u015f\7v\2\2\u015f")
        buf.write("\u0160\7k\2\2\u0160\u0161\7q\2\2\u0161\u0162\7p\2\2\u0162")
        buf.write("\u0163\7\"\2\2\u0163\u0164\7u\2\2\u0164\u0165\7v\2\2\u0165")
        buf.write("\u0166\7c\2\2\u0166\u0167\7v\2\2\u0167\u0168\7g\2\2\u0168")
        buf.write("\u0169\7o\2\2\u0169\u016a\7g\2\2\u016a\u016b\7p\2\2\u016b")
        buf.write("\u016c\7v\2\2\u016c\u0174\7\"\2\2\u016d\u016e\7h\2\2\u016e")
        buf.write("\u016f\7k\2\2\u016f\u0170\7g\2\2\u0170\u0171\7n\2\2\u0171")
        buf.write("\u0172\7f\2\2\u0172\u0174\7\"\2\2\u0173\u0157\3\2\2\2")
        buf.write("\u0173\u016d\3\2\2\2\u0174T\3\2\2\2\u0175\u0176\7e\2\2")
        buf.write("\u0176\u0177\7q\2\2\u0177\u0178\7p\2\2\u0178\u0179\7h")
        buf.write("\2\2\u0179\u017a\7k\2\2\u017a\u017b\7i\2\2\u017b\u017c")
        buf.write("\7w\2\2\u017c\u017d\7t\2\2\u017d\u017e\7c\2\2\u017e\u017f")
        buf.write("\7v\2\2\u017f\u0180\7k\2\2\u0180\u0181\7q\2\2\u0181\u0182")
        buf.write("\7p\2\2\u0182\u0183\7\"\2\2\u0183\u0184\7h\2\2\u0184\u0185")
        buf.write("\7k\2\2\u0185\u0186\7n\2\2\u0186\u0187\7g\2\2\u0187\u0188")
        buf.write("\7\"\2\2\u0188V\3\2\2\2\u0189\u018a\7r\2\2\u018a\u018b")
        buf.write("\7t\2\2\u018b\u018c\7q\2\2\u018c\u018d\7r\2\2\u018d\u018e")
        buf.write("\7g\2\2\u018e\u018f\7t\2\2\u018f\u0190\7v\2\2\u0190\u0191")
        buf.write("\7{\2\2\u0191\u0192\7\"\2\2\u0192X\3\2\2\2\u0193\u0194")
        buf.write("\7g\2\2\u0194\u0195\7z\2\2\u0195\u0196\7r\2\2\u0196\u0197")
        buf.write("\7t\2\2\u0197\u0198\7g\2\2\u0198\u0199\7u\2\2\u0199\u019a")
        buf.write("\7u\2\2\u019a\u019b\7k\2\2\u019b\u019c\7q\2\2\u019c\u019d")
        buf.write("\7p\2\2\u019d\u019e\7\"\2\2\u019e\u019f\7u\2\2\u019f\u01a0")
        buf.write("\7v\2\2\u01a0\u01a1\7c\2\2\u01a1\u01a2\7v\2\2\u01a2\u01a3")
        buf.write("\7g\2\2\u01a3\u01a4\7o\2\2\u01a4\u01a5\7g\2\2\u01a5\u01a6")
        buf.write("\7p\2\2\u01a6\u01a7\7v\2\2\u01a7\u01a8\7\"\2\2\u01a8Z")
        buf.write("\3\2\2\2\u01a9\u01aa\7x\2\2\u01aa\u01ab\7c\2\2\u01ab\u01ac")
        buf.write("\7n\2\2\u01ac\u01ad\7w\2\2\u01ad\u01ae\7g\2\2\u01ae\u01af")
        buf.write("\7\"\2\2\u01af\\\3\2\2\2\u01b0\u01b1\7k\2\2\u01b1\u01b2")
        buf.write("\7p\2\2\u01b2\u01b3\7k\2\2\u01b3\u01b4\7v\2\2\u01b4\u01b5")
        buf.write("\7k\2\2\u01b5\u01b6\7c\2\2\u01b6\u01b7\7n\2\2\u01b7\u01b8")
        buf.write("\7\"\2\2\u01b8\u01b9\7x\2\2\u01b9\u01ba\7c\2\2\u01ba\u01bb")
        buf.write("\7n\2\2\u01bb\u01bc\7w\2\2\u01bc\u01bd\7g\2\2\u01bd\u01be")
        buf.write("\7\"\2\2\u01be^\3\2\2\2\u01bf\u01c0\7e\2\2\u01c0\u01c1")
        buf.write("\7n\2\2\u01c1\u01c2\7c\2\2\u01c2\u01c3\7u\2\2\u01c3\u01c4")
        buf.write("\7u\2\2\u01c4\u01c5\7\"\2\2\u01c5`\3\2\2\2\u01c6\u01c7")
        buf.write("\7u\2\2\u01c7\u01c8\7w\2\2\u01c8\u01c9\7d\2\2\u01c9\u01ca")
        buf.write("\7e\2\2\u01ca\u01cb\7n\2\2\u01cb\u01cc\7c\2\2\u01cc\u01cd")
        buf.write("\7u\2\2\u01cd\u01ce\7u\2\2\u01ce\u01cf\7\"\2\2\u01cfb")
        buf.write("\3\2\2\2\5\2\u00aa\u0173\2")
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
    T__18 = 19
    T__19 = 20
    T__20 = 21
    SPACE = 22
    Alphabet = 23
    NL = 24
    LPAREN = 25
    RPAREN = 26
    NAME = 27
    ANNOTATION = 28
    EXTENSION = 29
    SUPERCLASS = 30
    IMPLEMENTATION = 31
    INTERFACE = 32
    FUNCTION = 33
    AbstractFunctions = 34
    CONSTRUCTOR = 35
    PARAMETER = 36
    TYPES = 37
    SPECIFIER = 38
    VISIBILITY = 39
    ReturnValue = 40
    DeclarationStatement = 41
    ConfigurationFile = 42
    CONFIGURATION_PROPERTIES = 43
    ExpressionStatement = 44
    VALUE = 45
    InitialValue = 46
    CLASSES = 47
    SUBCLASSES = 48

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\"'", "'||'", "'&&'", "'!'", "'...'", "'!...'", "'.'", "'='", 
            "'>'", "'<'", "'''", "'&'", "'|'", "'['", "']'", "'must '", 
            "'of '", "'and '", "'or '", "'have '", "'with '", "'('", "')'", 
            "'name '", "'annotation '", "'extension '", "'Superclass'", 
            "'implementation '", "'Interface '", "'function '", "'abstract function '", 
            "'constructor '", "'parameter '", "'type '", "'specifier '", 
            "'visibility '", "'return value '", "'configuration file '", 
            "'property '", "'expression statement '", "'value '", "'initial value '", 
            "'class '", "'subclass '" ]

    symbolicNames = [ "<INVALID>",
            "SPACE", "Alphabet", "NL", "LPAREN", "RPAREN", "NAME", "ANNOTATION", 
            "EXTENSION", "SUPERCLASS", "IMPLEMENTATION", "INTERFACE", "FUNCTION", 
            "AbstractFunctions", "CONSTRUCTOR", "PARAMETER", "TYPES", "SPECIFIER", 
            "VISIBILITY", "ReturnValue", "DeclarationStatement", "ConfigurationFile", 
            "CONFIGURATION_PROPERTIES", "ExpressionStatement", "VALUE", 
            "InitialValue", "CLASSES", "SUBCLASSES" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "SPACE", "Alphabet", "NL", "LPAREN", "RPAREN", 
                  "NAME", "ANNOTATION", "EXTENSION", "SUPERCLASS", "IMPLEMENTATION", 
                  "INTERFACE", "FUNCTION", "AbstractFunctions", "CONSTRUCTOR", 
                  "PARAMETER", "TYPES", "SPECIFIER", "VISIBILITY", "ReturnValue", 
                  "DeclarationStatement", "ConfigurationFile", "CONFIGURATION_PROPERTIES", 
                  "ExpressionStatement", "VALUE", "InitialValue", "CLASSES", 
                  "SUBCLASSES" ]

    grammarFileName = "RulepadGrammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


