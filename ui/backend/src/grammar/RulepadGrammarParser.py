# Generated from ../violation-detection/src/main/antlr4/ca/ualberta/grammar/RulepadGrammar.g4 by ANTLR 4.9
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\'")
        buf.write("\u020b\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\3\2\7\2t\n")
        buf.write("\2\f\2\16\2w\13\2\3\2\5\2z\n\2\3\2\5\2}\n\2\3\2\7\2\u0080")
        buf.write("\n\2\f\2\16\2\u0083\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\5\3\u009b\n\3\3\4\3\4\3\4\3\4\6\4\u00a1\n\4\r\4\16")
        buf.write("\4\u00a2\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3")
        buf.write("\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\5\16\u00bb")
        buf.write("\n\16\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\5\24\u00cf\n")
        buf.write("\24\3\24\5\24\u00d2\n\24\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\5\26\u00dd\n\26\3\26\3\26\3\26\3\26\3")
        buf.write("\26\3\26\7\26\u00e5\n\26\f\26\16\26\u00e8\13\26\3\27\3")
        buf.write("\27\3\27\3\30\3\30\3\30\3\30\3\30\5\30\u00f2\n\30\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\32\3\32\5\32\u00fc\n\32\3")
        buf.write("\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\5\35\u010d\n\35\5\35\u010f\n\35\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\7\35\u0117\n\35\f\35\16\35")
        buf.write("\u011a\13\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3")
        buf.write("!\3!\3!\3!\3!\3!\3!\5!\u012c\n!\5!\u012e\n!\3!\3!\3!\3")
        buf.write("!\3!\3!\7!\u0136\n!\f!\16!\u0139\13!\3\"\3\"\3\"\3#\3")
        buf.write("#\3#\5#\u0141\n#\3#\5#\u0144\n#\3$\3$\3$\3%\3%\3%\3%\3")
        buf.write("%\3%\3%\3%\5%\u0151\n%\5%\u0153\n%\3%\3%\3%\3%\3%\3%\7")
        buf.write("%\u015b\n%\f%\16%\u015e\13%\3&\3&\5&\u0162\n&\3\'\3\'")
        buf.write("\3\'\5\'\u0167\n\'\3\'\5\'\u016a\n\'\3(\3(\3(\3)\3)\3")
        buf.write(")\3)\3)\3)\3)\3)\5)\u0177\n)\5)\u0179\n)\3)\3)\3)\3)\3")
        buf.write(")\3)\7)\u0181\n)\f)\16)\u0184\13)\3*\3*\3*\3+\3+\3+\3")
        buf.write(",\3,\3,\3-\3-\3-\3.\3.\3.\3.\3.\3.\3.\3.\5.\u019a\n.\5")
        buf.write(".\u019c\n.\3.\3.\3.\3.\3.\3.\7.\u01a4\n.\f.\16.\u01a7")
        buf.write("\13.\3/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\5\61\u01b5\n\61\3\61\3\61\3\61\3\61\3\61\3\61\7")
        buf.write("\61\u01bd\n\61\f\61\16\61\u01c0\13\61\3\62\3\62\3\62\3")
        buf.write("\63\3\63\3\63\5\63\u01c8\n\63\3\63\5\63\u01cb\n\63\3\64")
        buf.write("\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\5\65")
        buf.write("\u01d8\n\65\5\65\u01da\n\65\3\65\3\65\3\65\3\65\3\65\3")
        buf.write("\65\7\65\u01e2\n\65\f\65\16\65\u01e5\13\65\3\66\3\66\3")
        buf.write("\66\3\67\3\67\3\67\38\38\38\38\38\38\38\38\38\38\38\3")
        buf.write("8\38\58\u01fa\n8\58\u01fc\n8\38\38\38\38\38\38\78\u0204")
        buf.write("\n8\f8\168\u0207\138\39\39\39\2\13*8@HPZ`hn:\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<")
        buf.write(">@BDFHJLNPRTVXZ\\^`bdfhjlnp\2\3\4\2\4\f\26\27\2\u0216")
        buf.write("\2y\3\2\2\2\4\u009a\3\2\2\2\6\u009c\3\2\2\2\b\u00a6\3")
        buf.write("\2\2\2\n\u00a8\3\2\2\2\f\u00aa\3\2\2\2\16\u00ac\3\2\2")
        buf.write("\2\20\u00ae\3\2\2\2\22\u00b0\3\2\2\2\24\u00b2\3\2\2\2")
        buf.write("\26\u00b4\3\2\2\2\30\u00b6\3\2\2\2\32\u00ba\3\2\2\2\34")
        buf.write("\u00bc\3\2\2\2\36\u00bf\3\2\2\2 \u00c2\3\2\2\2\"\u00c5")
        buf.write("\3\2\2\2$\u00c8\3\2\2\2&\u00d1\3\2\2\2(\u00d3\3\2\2\2")
        buf.write("*\u00dc\3\2\2\2,\u00e9\3\2\2\2.\u00ec\3\2\2\2\60\u00f3")
        buf.write("\3\2\2\2\62\u00f6\3\2\2\2\64\u00fd\3\2\2\2\66\u0100\3")
        buf.write("\2\2\28\u010e\3\2\2\2:\u011b\3\2\2\2<\u011e\3\2\2\2>\u0121")
        buf.write("\3\2\2\2@\u012d\3\2\2\2B\u013a\3\2\2\2D\u0143\3\2\2\2")
        buf.write("F\u0145\3\2\2\2H\u0152\3\2\2\2J\u015f\3\2\2\2L\u0169\3")
        buf.write("\2\2\2N\u016b\3\2\2\2P\u0178\3\2\2\2R\u0185\3\2\2\2T\u0188")
        buf.write("\3\2\2\2V\u018b\3\2\2\2X\u018e\3\2\2\2Z\u019b\3\2\2\2")
        buf.write("\\\u01a8\3\2\2\2^\u01ab\3\2\2\2`\u01b4\3\2\2\2b\u01c1")
        buf.write("\3\2\2\2d\u01ca\3\2\2\2f\u01cc\3\2\2\2h\u01d9\3\2\2\2")
        buf.write("j\u01e6\3\2\2\2l\u01e9\3\2\2\2n\u01fb\3\2\2\2p\u0208\3")
        buf.write("\2\2\2rt\5\f\7\2sr\3\2\2\2tw\3\2\2\2us\3\2\2\2uv\3\2\2")
        buf.write("\2vz\3\2\2\2wu\3\2\2\2xz\5\4\3\2yu\3\2\2\2yx\3\2\2\2z")
        buf.write("|\3\2\2\2{}\5\n\6\2|{\3\2\2\2|}\3\2\2\2}\u0081\3\2\2\2")
        buf.write("~\u0080\7\25\2\2\177~\3\2\2\2\u0080\u0083\3\2\2\2\u0081")
        buf.write("\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0084\3\2\2\2\u0083")
        buf.write("\u0081\3\2\2\2\u0084\u0085\7\2\2\3\u0085\3\3\2\2\2\u0086")
        buf.write("\u0087\5\64\33\2\u0087\u0088\5\16\b\2\u0088\u0089\5\26")
        buf.write("\f\2\u0089\u008a\58\35\2\u008a\u009b\3\2\2\2\u008b\u008c")
        buf.write("\5:\36\2\u008c\u008d\5\16\b\2\u008d\u008e\5\26\f\2\u008e")
        buf.write("\u008f\5@!\2\u008f\u009b\3\2\2\2\u0090\u0091\5j\66\2\u0091")
        buf.write("\u0092\5\16\b\2\u0092\u0093\5\26\f\2\u0093\u0094\5n8\2")
        buf.write("\u0094\u009b\3\2\2\2\u0095\u0096\5V,\2\u0096\u0097\5\16")
        buf.write("\b\2\u0097\u0098\5\26\f\2\u0098\u0099\5Z.\2\u0099\u009b")
        buf.write("\3\2\2\2\u009a\u0086\3\2\2\2\u009a\u008b\3\2\2\2\u009a")
        buf.write("\u0090\3\2\2\2\u009a\u0095\3\2\2\2\u009b\5\3\2\2\2\u009c")
        buf.write("\u00a0\7\3\2\2\u009d\u00a1\7\24\2\2\u009e\u00a1\5\b\5")
        buf.write("\2\u009f\u00a1\7\23\2\2\u00a0\u009d\3\2\2\2\u00a0\u009e")
        buf.write("\3\2\2\2\u00a0\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2")
        buf.write("\u00a0\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00a4\3\2\2\2")
        buf.write("\u00a4\u00a5\7\3\2\2\u00a5\7\3\2\2\2\u00a6\u00a7\t\2\2")
        buf.write("\2\u00a7\t\3\2\2\2\u00a8\u00a9\7\4\2\2\u00a9\13\3\2\2")
        buf.write("\2\u00aa\u00ab\7\25\2\2\u00ab\r\3\2\2\2\u00ac\u00ad\7")
        buf.write("\r\2\2\u00ad\17\3\2\2\2\u00ae\u00af\7\16\2\2\u00af\21")
        buf.write("\3\2\2\2\u00b0\u00b1\7\17\2\2\u00b1\23\3\2\2\2\u00b2\u00b3")
        buf.write("\7\20\2\2\u00b3\25\3\2\2\2\u00b4\u00b5\7\21\2\2\u00b5")
        buf.write("\27\3\2\2\2\u00b6\u00b7\7\22\2\2\u00b7\31\3\2\2\2\u00b8")
        buf.write("\u00bb\5\22\n\2\u00b9\u00bb\5\24\13\2\u00ba\u00b8\3\2")
        buf.write("\2\2\u00ba\u00b9\3\2\2\2\u00bb\33\3\2\2\2\u00bc\u00bd")
        buf.write("\7\30\2\2\u00bd\u00be\5\36\20\2\u00be\35\3\2\2\2\u00bf")
        buf.write("\u00c0\5\6\4\2\u00c0\u00c1\7\23\2\2\u00c1\37\3\2\2\2\u00c2")
        buf.write("\u00c3\7\31\2\2\u00c3\u00c4\5\"\22\2\u00c4!\3\2\2\2\u00c5")
        buf.write("\u00c6\5\6\4\2\u00c6\u00c7\7\23\2\2\u00c7#\3\2\2\2\u00c8")
        buf.write("\u00c9\7\32\2\2\u00c9\u00ca\5&\24\2\u00ca%\3\2\2\2\u00cb")
        buf.write("\u00cc\5\6\4\2\u00cc\u00ce\7\23\2\2\u00cd\u00cf\5(\25")
        buf.write("\2\u00ce\u00cd\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00d2")
        buf.write("\3\2\2\2\u00d0\u00d2\5(\25\2\u00d1\u00cb\3\2\2\2\u00d1")
        buf.write("\u00d0\3\2\2\2\u00d2\'\3\2\2\2\u00d3\u00d4\5\30\r\2\u00d4")
        buf.write("\u00d5\5*\26\2\u00d5)\3\2\2\2\u00d6\u00d7\b\26\1\2\u00d7")
        buf.write("\u00d8\7\26\2\2\u00d8\u00d9\5*\26\2\u00d9\u00da\7\27\2")
        buf.write("\2\u00da\u00dd\3\2\2\2\u00db\u00dd\5B\"\2\u00dc\u00d6")
        buf.write("\3\2\2\2\u00dc\u00db\3\2\2\2\u00dd\u00e6\3\2\2\2\u00de")
        buf.write("\u00df\f\5\2\2\u00df\u00e0\5\32\16\2\u00e0\u00e1\5*\26")
        buf.write("\6\u00e1\u00e5\3\2\2\2\u00e2\u00e3\f\3\2\2\u00e3\u00e5")
        buf.write("\7\23\2\2\u00e4\u00de\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e5")
        buf.write("\u00e8\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e6\u00e7\3\2\2\2")
        buf.write("\u00e7+\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e9\u00ea\7\33\2")
        buf.write("\2\u00ea\u00eb\5.\30\2\u00eb-\3\2\2\2\u00ec\u00f1\5\20")
        buf.write("\t\2\u00ed\u00ee\5\6\4\2\u00ee\u00ef\7\23\2\2\u00ef\u00f2")
        buf.write("\3\2\2\2\u00f0\u00f2\7\34\2\2\u00f1\u00ed\3\2\2\2\u00f1")
        buf.write("\u00f0\3\2\2\2\u00f2/\3\2\2\2\u00f3\u00f4\7\35\2\2\u00f4")
        buf.write("\u00f5\5\62\32\2\u00f5\61\3\2\2\2\u00f6\u00fb\5\20\t\2")
        buf.write("\u00f7\u00f8\5\6\4\2\u00f8\u00f9\7\23\2\2\u00f9\u00fc")
        buf.write("\3\2\2\2\u00fa\u00fc\7\36\2\2\u00fb\u00f7\3\2\2\2\u00fb")
        buf.write("\u00fa\3\2\2\2\u00fc\63\3\2\2\2\u00fd\u00fe\7\37\2\2\u00fe")
        buf.write("\u00ff\5\66\34\2\u00ff\65\3\2\2\2\u0100\u0101\5\30\r\2")
        buf.write("\u0101\u0102\58\35\2\u0102\67\3\2\2\2\u0103\u0104\b\35")
        buf.write("\1\2\u0104\u0105\7\26\2\2\u0105\u0106\58\35\2\u0106\u0107")
        buf.write("\7\27\2\2\u0107\u010f\3\2\2\2\u0108\u010d\5$\23\2\u0109")
        buf.write("\u010d\5R*\2\u010a\u010d\5J&\2\u010b\u010d\5\\/\2\u010c")
        buf.write("\u0108\3\2\2\2\u010c\u0109\3\2\2\2\u010c\u010a\3\2\2\2")
        buf.write("\u010c\u010b\3\2\2\2\u010d\u010f\3\2\2\2\u010e\u0103\3")
        buf.write("\2\2\2\u010e\u010c\3\2\2\2\u010f\u0118\3\2\2\2\u0110\u0111")
        buf.write("\f\5\2\2\u0111\u0112\5\32\16\2\u0112\u0113\58\35\6\u0113")
        buf.write("\u0117\3\2\2\2\u0114\u0115\f\3\2\2\u0115\u0117\7\23\2")
        buf.write("\2\u0116\u0110\3\2\2\2\u0116\u0114\3\2\2\2\u0117\u011a")
        buf.write("\3\2\2\2\u0118\u0116\3\2\2\2\u0118\u0119\3\2\2\2\u0119")
        buf.write("9\3\2\2\2\u011a\u0118\3\2\2\2\u011b\u011c\7 \2\2\u011c")
        buf.write("\u011d\5> \2\u011d;\3\2\2\2\u011e\u011f\5\20\t\2\u011f")
        buf.write("\u0120\5j\66\2\u0120=\3\2\2\2\u0121\u0122\5\30\r\2\u0122")
        buf.write("\u0123\5@!\2\u0123?\3\2\2\2\u0124\u0125\b!\1\2\u0125\u0126")
        buf.write("\7\26\2\2\u0126\u0127\5@!\2\u0127\u0128\7\27\2\2\u0128")
        buf.write("\u012e\3\2\2\2\u0129\u012c\5$\23\2\u012a\u012c\5J&\2\u012b")
        buf.write("\u0129\3\2\2\2\u012b\u012a\3\2\2\2\u012c\u012e\3\2\2\2")
        buf.write("\u012d\u0124\3\2\2\2\u012d\u012b\3\2\2\2\u012e\u0137\3")
        buf.write("\2\2\2\u012f\u0130\f\5\2\2\u0130\u0131\5\32\16\2\u0131")
        buf.write("\u0132\5@!\6\u0132\u0136\3\2\2\2\u0133\u0134\f\3\2\2\u0134")
        buf.write("\u0136\7\23\2\2\u0135\u012f\3\2\2\2\u0135\u0133\3\2\2")
        buf.write("\2\u0136\u0139\3\2\2\2\u0137\u0135\3\2\2\2\u0137\u0138")
        buf.write("\3\2\2\2\u0138A\3\2\2\2\u0139\u0137\3\2\2\2\u013a\u013b")
        buf.write("\7!\2\2\u013b\u013c\5D#\2\u013cC\3\2\2\2\u013d\u013e\5")
        buf.write("\6\4\2\u013e\u0140\7\23\2\2\u013f\u0141\5F$\2\u0140\u013f")
        buf.write("\3\2\2\2\u0140\u0141\3\2\2\2\u0141\u0144\3\2\2\2\u0142")
        buf.write("\u0144\5F$\2\u0143\u013d\3\2\2\2\u0143\u0142\3\2\2\2\u0144")
        buf.write("E\3\2\2\2\u0145\u0146\5\30\r\2\u0146\u0147\5H%\2\u0147")
        buf.write("G\3\2\2\2\u0148\u0149\b%\1\2\u0149\u014a\7\26\2\2\u014a")
        buf.write("\u014b\5H%\2\u014b\u014c\7\27\2\2\u014c\u0153\3\2\2\2")
        buf.write("\u014d\u0151\5R*\2\u014e\u0151\5\34\17\2\u014f\u0151\5")
        buf.write(" \21\2\u0150\u014d\3\2\2\2\u0150\u014e\3\2\2\2\u0150\u014f")
        buf.write("\3\2\2\2\u0151\u0153\3\2\2\2\u0152\u0148\3\2\2\2\u0152")
        buf.write("\u0150\3\2\2\2\u0153\u015c\3\2\2\2\u0154\u0155\f\5\2\2")
        buf.write("\u0155\u0156\5\32\16\2\u0156\u0157\5H%\6\u0157\u015b\3")
        buf.write("\2\2\2\u0158\u0159\f\3\2\2\u0159\u015b\7\23\2\2\u015a")
        buf.write("\u0154\3\2\2\2\u015a\u0158\3\2\2\2\u015b\u015e\3\2\2\2")
        buf.write("\u015c\u015a\3\2\2\2\u015c\u015d\3\2\2\2\u015dI\3\2\2")
        buf.write("\2\u015e\u015c\3\2\2\2\u015f\u0161\7!\2\2\u0160\u0162")
        buf.write("\5L\'\2\u0161\u0160\3\2\2\2\u0161\u0162\3\2\2\2\u0162")
        buf.write("K\3\2\2\2\u0163\u0164\5\6\4\2\u0164\u0166\7\23\2\2\u0165")
        buf.write("\u0167\5N(\2\u0166\u0165\3\2\2\2\u0166\u0167\3\2\2\2\u0167")
        buf.write("\u016a\3\2\2\2\u0168\u016a\5N(\2\u0169\u0163\3\2\2\2\u0169")
        buf.write("\u0168\3\2\2\2\u016aM\3\2\2\2\u016b\u016c\5\30\r\2\u016c")
        buf.write("\u016d\5P)\2\u016dO\3\2\2\2\u016e\u016f\b)\1\2\u016f\u0170")
        buf.write("\7\26\2\2\u0170\u0171\5P)\2\u0171\u0172\7\27\2\2\u0172")
        buf.write("\u0179\3\2\2\2\u0173\u0177\5R*\2\u0174\u0177\5\34\17\2")
        buf.write("\u0175\u0177\5$\23\2\u0176\u0173\3\2\2\2\u0176\u0174\3")
        buf.write("\2\2\2\u0176\u0175\3\2\2\2\u0177\u0179\3\2\2\2\u0178\u016e")
        buf.write("\3\2\2\2\u0178\u0176\3\2\2\2\u0179\u0182\3\2\2\2\u017a")
        buf.write("\u017b\f\5\2\2\u017b\u017c\5\32\16\2\u017c\u017d\5P)\6")
        buf.write("\u017d\u0181\3\2\2\2\u017e\u017f\f\3\2\2\u017f\u0181\7")
        buf.write("\23\2\2\u0180\u017a\3\2\2\2\u0180\u017e\3\2\2\2\u0181")
        buf.write("\u0184\3\2\2\2\u0182\u0180\3\2\2\2\u0182\u0183\3\2\2\2")
        buf.write("\u0183Q\3\2\2\2\u0184\u0182\3\2\2\2\u0185\u0186\7\"\2")
        buf.write("\2\u0186\u0187\5T+\2\u0187S\3\2\2\2\u0188\u0189\5\6\4")
        buf.write("\2\u0189\u018a\7\23\2\2\u018aU\3\2\2\2\u018b\u018c\7#")
        buf.write("\2\2\u018c\u018d\5X-\2\u018dW\3\2\2\2\u018e\u018f\5\30")
        buf.write("\r\2\u018f\u0190\5Z.\2\u0190Y\3\2\2\2\u0191\u0192\b.\1")
        buf.write("\2\u0192\u0193\7\26\2\2\u0193\u0194\5Z.\2\u0194\u0195")
        buf.write("\7\27\2\2\u0195\u019c\3\2\2\2\u0196\u019a\5$\23\2\u0197")
        buf.write("\u019a\5R*\2\u0198\u019a\5\\/\2\u0199\u0196\3\2\2\2\u0199")
        buf.write("\u0197\3\2\2\2\u0199\u0198\3\2\2\2\u019a\u019c\3\2\2\2")
        buf.write("\u019b\u0191\3\2\2\2\u019b\u0199\3\2\2\2\u019c\u01a5\3")
        buf.write("\2\2\2\u019d\u019e\f\5\2\2\u019e\u019f\5\32\16\2\u019f")
        buf.write("\u01a0\5Z.\6\u01a0\u01a4\3\2\2\2\u01a1\u01a2\f\3\2\2\u01a2")
        buf.write("\u01a4\7\23\2\2\u01a3\u019d\3\2\2\2\u01a3\u01a1\3\2\2")
        buf.write("\2\u01a4\u01a7\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a5\u01a6")
        buf.write("\3\2\2\2\u01a6[\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a8\u01a9")
        buf.write("\7$\2\2\u01a9\u01aa\5^\60\2\u01aa]\3\2\2\2\u01ab\u01ac")
        buf.write("\5\30\r\2\u01ac\u01ad\5`\61\2\u01ad_\3\2\2\2\u01ae\u01af")
        buf.write("\b\61\1\2\u01af\u01b0\7\26\2\2\u01b0\u01b1\5`\61\2\u01b1")
        buf.write("\u01b2\7\27\2\2\u01b2\u01b5\3\2\2\2\u01b3\u01b5\5b\62")
        buf.write("\2\u01b4\u01ae\3\2\2\2\u01b4\u01b3\3\2\2\2\u01b5\u01be")
        buf.write("\3\2\2\2\u01b6\u01b7\f\5\2\2\u01b7\u01b8\5\32\16\2\u01b8")
        buf.write("\u01b9\5`\61\6\u01b9\u01bd\3\2\2\2\u01ba\u01bb\f\3\2\2")
        buf.write("\u01bb\u01bd\7\23\2\2\u01bc\u01b6\3\2\2\2\u01bc\u01ba")
        buf.write("\3\2\2\2\u01bd\u01c0\3\2\2\2\u01be\u01bc\3\2\2\2\u01be")
        buf.write("\u01bf\3\2\2\2\u01bfa\3\2\2\2\u01c0\u01be\3\2\2\2\u01c1")
        buf.write("\u01c2\7%\2\2\u01c2\u01c3\5d\63\2\u01c3c\3\2\2\2\u01c4")
        buf.write("\u01c5\5\6\4\2\u01c5\u01c7\7\23\2\2\u01c6\u01c8\5f\64")
        buf.write("\2\u01c7\u01c6\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8\u01cb")
        buf.write("\3\2\2\2\u01c9\u01cb\5f\64\2\u01ca\u01c4\3\2\2\2\u01ca")
        buf.write("\u01c9\3\2\2\2\u01cbe\3\2\2\2\u01cc\u01cd\5\30\r\2\u01cd")
        buf.write("\u01ce\5h\65\2\u01ceg\3\2\2\2\u01cf\u01d0\b\65\1\2\u01d0")
        buf.write("\u01d1\7\26\2\2\u01d1\u01d2\5h\65\2\u01d2\u01d3\7\27\2")
        buf.write("\2\u01d3\u01da\3\2\2\2\u01d4\u01d8\5R*\2\u01d5\u01d8\5")
        buf.write("\34\17\2\u01d6\u01d8\5 \21\2\u01d7\u01d4\3\2\2\2\u01d7")
        buf.write("\u01d5\3\2\2\2\u01d7\u01d6\3\2\2\2\u01d8\u01da\3\2\2\2")
        buf.write("\u01d9\u01cf\3\2\2\2\u01d9\u01d7\3\2\2\2\u01da\u01e3\3")
        buf.write("\2\2\2\u01db\u01dc\f\5\2\2\u01dc\u01dd\5\32\16\2\u01dd")
        buf.write("\u01de\5h\65\6\u01de\u01e2\3\2\2\2\u01df\u01e0\f\3\2\2")
        buf.write("\u01e0\u01e2\7\23\2\2\u01e1\u01db\3\2\2\2\u01e1\u01df")
        buf.write("\3\2\2\2\u01e2\u01e5\3\2\2\2\u01e3\u01e1\3\2\2\2\u01e3")
        buf.write("\u01e4\3\2\2\2\u01e4i\3\2\2\2\u01e5\u01e3\3\2\2\2\u01e6")
        buf.write("\u01e7\7&\2\2\u01e7\u01e8\5l\67\2\u01e8k\3\2\2\2\u01e9")
        buf.write("\u01ea\5\30\r\2\u01ea\u01eb\5n8\2\u01ebm\3\2\2\2\u01ec")
        buf.write("\u01ed\b8\1\2\u01ed\u01ee\7\26\2\2\u01ee\u01ef\5n8\2\u01ef")
        buf.write("\u01f0\7\27\2\2\u01f0\u01fc\3\2\2\2\u01f1\u01fa\5$\23")
        buf.write("\2\u01f2\u01fa\5,\27\2\u01f3\u01fa\5\60\31\2\u01f4\u01fa")
        buf.write("\5\64\33\2\u01f5\u01fa\5:\36\2\u01f6\u01fa\5V,\2\u01f7")
        buf.write("\u01fa\5\\/\2\u01f8\u01fa\5p9\2\u01f9\u01f1\3\2\2\2\u01f9")
        buf.write("\u01f2\3\2\2\2\u01f9\u01f3\3\2\2\2\u01f9\u01f4\3\2\2\2")
        buf.write("\u01f9\u01f5\3\2\2\2\u01f9\u01f6\3\2\2\2\u01f9\u01f7\3")
        buf.write("\2\2\2\u01f9\u01f8\3\2\2\2\u01fa\u01fc\3\2\2\2\u01fb\u01ec")
        buf.write("\3\2\2\2\u01fb\u01f9\3\2\2\2\u01fc\u0205\3\2\2\2\u01fd")
        buf.write("\u01fe\f\5\2\2\u01fe\u01ff\5\32\16\2\u01ff\u0200\5n8\6")
        buf.write("\u0200\u0204\3\2\2\2\u0201\u0202\f\3\2\2\u0202\u0204\7")
        buf.write("\23\2\2\u0203\u01fd\3\2\2\2\u0203\u0201\3\2\2\2\u0204")
        buf.write("\u0207\3\2\2\2\u0205\u0203\3\2\2\2\u0205\u0206\3\2\2\2")
        buf.write("\u0206o\3\2\2\2\u0207\u0205\3\2\2\2\u0208\u0209\7\'\2")
        buf.write("\2\u0209q\3\2\2\2\67uy|\u0081\u009a\u00a0\u00a2\u00ba")
        buf.write("\u00ce\u00d1\u00dc\u00e4\u00e6\u00f1\u00fb\u010c\u010e")
        buf.write("\u0116\u0118\u012b\u012d\u0135\u0137\u0140\u0143\u0150")
        buf.write("\u0152\u015a\u015c\u0161\u0166\u0169\u0176\u0178\u0180")
        buf.write("\u0182\u0199\u019b\u01a3\u01a5\u01b4\u01bc\u01be\u01c7")
        buf.write("\u01ca\u01d7\u01d9\u01e1\u01e3\u01f9\u01fb\u0203\u0205")
        return buf.getvalue()


class RulepadGrammarParser ( Parser ):

    grammarFileName = "RulepadGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\"'", "'.'", "'='", "'>'", "'<'", "'''", 
                     "'&'", "'|'", "'['", "']'", "'must '", "'of '", "'and '", 
                     "'or '", "'have '", "'with '", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'('", "')'", "'name '", "'value '", "'annotation '", 
                     "'extension '", "'Superclass'", "'implementation '", 
                     "'Interface '", "<INVALID>", "'constructor '", "'parameter '", 
                     "'type '", "<INVALID>", "'configuration file '", "'property '", 
                     "'class '", "'bean declaration '" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "SPACE", "Alphabet", "NL", "LPAREN", 
                      "RPAREN", "NAME", "VALUE", "ANNOTATION", "EXTENSION", 
                      "SUPERCLASS", "IMPLEMENTATION", "INTERFACE", "FUNCTION", 
                      "CONSTRUCTOR", "PARAMETER", "TYPES", "DeclarationStatement", 
                      "ConfigurationFile", "CONFIGURATION_PROPERTIES", "CLASSES", 
                      "BEAN_DECL" ]

    RULE_inputSentence = 0
    RULE_mustClause = 1
    RULE_combinatorialWords = 2
    RULE_symbols = 3
    RULE_end = 4
    RULE_emptyLine = 5
    RULE_must = 6
    RULE_of = 7
    RULE_and_ = 8
    RULE_or_ = 9
    RULE_have = 10
    RULE_withWord = 11
    RULE_binary = 12
    RULE_names = 13
    RULE_nameCondition = 14
    RULE_values = 15
    RULE_valueCondition = 16
    RULE_annotations = 17
    RULE_annotationCondition = 18
    RULE_annotationConditionTransition = 19
    RULE_annotationExpression = 20
    RULE_extensions = 21
    RULE_extensionCondition = 22
    RULE_implementations = 23
    RULE_implementationCondition = 24
    RULE_functions = 25
    RULE_functionCondition = 26
    RULE_functionExpression = 27
    RULE_constructors = 28
    RULE_constructorOf = 29
    RULE_constructorCondition = 30
    RULE_constructorExpression = 31
    RULE_parameters = 32
    RULE_parameterCondition = 33
    RULE_parameterConditionTransition = 34
    RULE_parameterExpression = 35
    RULE_functionParameters = 36
    RULE_functionParameterCondition = 37
    RULE_functionParameterConditionTransition = 38
    RULE_functionParameterExpression = 39
    RULE_types = 40
    RULE_typeCondition = 41
    RULE_declarationStatements = 42
    RULE_declarationStatementCondition = 43
    RULE_declarationStatementExpression = 44
    RULE_configurationFiles = 45
    RULE_configurationFileCondition = 46
    RULE_configurationFileExpression = 47
    RULE_configurationProperties = 48
    RULE_configurationPropertyCondition = 49
    RULE_configurationPropertyConditionTransition = 50
    RULE_configurationPropertyExpression = 51
    RULE_classes = 52
    RULE_classCondition = 53
    RULE_classExpression = 54
    RULE_beans = 55

    ruleNames =  [ "inputSentence", "mustClause", "combinatorialWords", 
                   "symbols", "end", "emptyLine", "must", "of", "and_", 
                   "or_", "have", "withWord", "binary", "names", "nameCondition", 
                   "values", "valueCondition", "annotations", "annotationCondition", 
                   "annotationConditionTransition", "annotationExpression", 
                   "extensions", "extensionCondition", "implementations", 
                   "implementationCondition", "functions", "functionCondition", 
                   "functionExpression", "constructors", "constructorOf", 
                   "constructorCondition", "constructorExpression", "parameters", 
                   "parameterCondition", "parameterConditionTransition", 
                   "parameterExpression", "functionParameters", "functionParameterCondition", 
                   "functionParameterConditionTransition", "functionParameterExpression", 
                   "types", "typeCondition", "declarationStatements", "declarationStatementCondition", 
                   "declarationStatementExpression", "configurationFiles", 
                   "configurationFileCondition", "configurationFileExpression", 
                   "configurationProperties", "configurationPropertyCondition", 
                   "configurationPropertyConditionTransition", "configurationPropertyExpression", 
                   "classes", "classCondition", "classExpression", "beans" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    SPACE=17
    Alphabet=18
    NL=19
    LPAREN=20
    RPAREN=21
    NAME=22
    VALUE=23
    ANNOTATION=24
    EXTENSION=25
    SUPERCLASS=26
    IMPLEMENTATION=27
    INTERFACE=28
    FUNCTION=29
    CONSTRUCTOR=30
    PARAMETER=31
    TYPES=32
    DeclarationStatement=33
    ConfigurationFile=34
    CONFIGURATION_PROPERTIES=35
    CLASSES=36
    BEAN_DECL=37

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class InputSentenceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(RulepadGrammarParser.EOF, 0)

        def mustClause(self):
            return self.getTypedRuleContext(RulepadGrammarParser.MustClauseContext,0)


        def end(self):
            return self.getTypedRuleContext(RulepadGrammarParser.EndContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(RulepadGrammarParser.NL)
            else:
                return self.getToken(RulepadGrammarParser.NL, i)

        def emptyLine(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RulepadGrammarParser.EmptyLineContext)
            else:
                return self.getTypedRuleContext(RulepadGrammarParser.EmptyLineContext,i)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_inputSentence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInputSentence" ):
                listener.enterInputSentence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInputSentence" ):
                listener.exitInputSentence(self)




    def inputSentence(self):

        localctx = RulepadGrammarParser.InputSentenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_inputSentence)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.EOF, RulepadGrammarParser.T__1, RulepadGrammarParser.NL]:
                self.state = 115
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 112
                        self.emptyLine() 
                    self.state = 117
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

                pass
            elif token in [RulepadGrammarParser.FUNCTION, RulepadGrammarParser.CONSTRUCTOR, RulepadGrammarParser.DeclarationStatement, RulepadGrammarParser.CLASSES]:
                self.state = 118
                self.mustClause()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RulepadGrammarParser.T__1:
                self.state = 121
                self.end()


            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RulepadGrammarParser.NL:
                self.state = 124
                self.match(RulepadGrammarParser.NL)
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 130
            self.match(RulepadGrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MustClauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functions(self):
            return self.getTypedRuleContext(RulepadGrammarParser.FunctionsContext,0)


        def must(self):
            return self.getTypedRuleContext(RulepadGrammarParser.MustContext,0)


        def have(self):
            return self.getTypedRuleContext(RulepadGrammarParser.HaveContext,0)


        def functionExpression(self):
            return self.getTypedRuleContext(RulepadGrammarParser.FunctionExpressionContext,0)


        def constructors(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ConstructorsContext,0)


        def constructorExpression(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ConstructorExpressionContext,0)


        def classes(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ClassesContext,0)


        def classExpression(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ClassExpressionContext,0)


        def declarationStatements(self):
            return self.getTypedRuleContext(RulepadGrammarParser.DeclarationStatementsContext,0)


        def declarationStatementExpression(self):
            return self.getTypedRuleContext(RulepadGrammarParser.DeclarationStatementExpressionContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_mustClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMustClause" ):
                listener.enterMustClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMustClause" ):
                listener.exitMustClause(self)




    def mustClause(self):

        localctx = RulepadGrammarParser.MustClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_mustClause)
        try:
            self.state = 152
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.FUNCTION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.functions()
                self.state = 133
                self.must()
                self.state = 134
                self.have()
                self.state = 135
                self.functionExpression(0)
                pass
            elif token in [RulepadGrammarParser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.constructors()
                self.state = 138
                self.must()
                self.state = 139
                self.have()
                self.state = 140
                self.constructorExpression(0)
                pass
            elif token in [RulepadGrammarParser.CLASSES]:
                self.enterOuterAlt(localctx, 3)
                self.state = 142
                self.classes()
                self.state = 143
                self.must()
                self.state = 144
                self.have()
                self.state = 145
                self.classExpression(0)
                pass
            elif token in [RulepadGrammarParser.DeclarationStatement]:
                self.enterOuterAlt(localctx, 4)
                self.state = 147
                self.declarationStatements()
                self.state = 148
                self.must()
                self.state = 149
                self.have()
                self.state = 150
                self.declarationStatementExpression(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CombinatorialWordsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Alphabet(self, i:int=None):
            if i is None:
                return self.getTokens(RulepadGrammarParser.Alphabet)
            else:
                return self.getToken(RulepadGrammarParser.Alphabet, i)

        def symbols(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RulepadGrammarParser.SymbolsContext)
            else:
                return self.getTypedRuleContext(RulepadGrammarParser.SymbolsContext,i)


        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(RulepadGrammarParser.SPACE)
            else:
                return self.getToken(RulepadGrammarParser.SPACE, i)

        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_combinatorialWords

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCombinatorialWords" ):
                listener.enterCombinatorialWords(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCombinatorialWords" ):
                listener.exitCombinatorialWords(self)




    def combinatorialWords(self):

        localctx = RulepadGrammarParser.CombinatorialWordsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_combinatorialWords)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(RulepadGrammarParser.T__0)
            self.state = 158 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 158
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.Alphabet]:
                    self.state = 155
                    self.match(RulepadGrammarParser.Alphabet)
                    pass
                elif token in [RulepadGrammarParser.T__1, RulepadGrammarParser.T__2, RulepadGrammarParser.T__3, RulepadGrammarParser.T__4, RulepadGrammarParser.T__5, RulepadGrammarParser.T__6, RulepadGrammarParser.T__7, RulepadGrammarParser.T__8, RulepadGrammarParser.T__9, RulepadGrammarParser.LPAREN, RulepadGrammarParser.RPAREN]:
                    self.state = 156
                    self.symbols()
                    pass
                elif token in [RulepadGrammarParser.SPACE]:
                    self.state = 157
                    self.match(RulepadGrammarParser.SPACE)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 160 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RulepadGrammarParser.T__1) | (1 << RulepadGrammarParser.T__2) | (1 << RulepadGrammarParser.T__3) | (1 << RulepadGrammarParser.T__4) | (1 << RulepadGrammarParser.T__5) | (1 << RulepadGrammarParser.T__6) | (1 << RulepadGrammarParser.T__7) | (1 << RulepadGrammarParser.T__8) | (1 << RulepadGrammarParser.T__9) | (1 << RulepadGrammarParser.SPACE) | (1 << RulepadGrammarParser.Alphabet) | (1 << RulepadGrammarParser.LPAREN) | (1 << RulepadGrammarParser.RPAREN))) != 0)):
                    break

            self.state = 162
            self.match(RulepadGrammarParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SymbolsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(RulepadGrammarParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(RulepadGrammarParser.RPAREN, 0)

        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_symbols

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSymbols" ):
                listener.enterSymbols(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSymbols" ):
                listener.exitSymbols(self)




    def symbols(self):

        localctx = RulepadGrammarParser.SymbolsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_symbols)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RulepadGrammarParser.T__1) | (1 << RulepadGrammarParser.T__2) | (1 << RulepadGrammarParser.T__3) | (1 << RulepadGrammarParser.T__4) | (1 << RulepadGrammarParser.T__5) | (1 << RulepadGrammarParser.T__6) | (1 << RulepadGrammarParser.T__7) | (1 << RulepadGrammarParser.T__8) | (1 << RulepadGrammarParser.T__9) | (1 << RulepadGrammarParser.LPAREN) | (1 << RulepadGrammarParser.RPAREN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EndContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_end

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnd" ):
                listener.enterEnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnd" ):
                listener.exitEnd(self)




    def end(self):

        localctx = RulepadGrammarParser.EndContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_end)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(RulepadGrammarParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EmptyLineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NL(self):
            return self.getToken(RulepadGrammarParser.NL, 0)

        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_emptyLine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyLine" ):
                listener.enterEmptyLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyLine" ):
                listener.exitEmptyLine(self)




    def emptyLine(self):

        localctx = RulepadGrammarParser.EmptyLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_emptyLine)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(RulepadGrammarParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MustContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_must

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMust" ):
                listener.enterMust(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMust" ):
                listener.exitMust(self)




    def must(self):

        localctx = RulepadGrammarParser.MustContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_must)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(RulepadGrammarParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OfContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_of

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOf" ):
                listener.enterOf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOf" ):
                listener.exitOf(self)




    def of(self):

        localctx = RulepadGrammarParser.OfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_of)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(RulepadGrammarParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class And_Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_and_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd_" ):
                listener.enterAnd_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd_" ):
                listener.exitAnd_(self)




    def and_(self):

        localctx = RulepadGrammarParser.And_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_and_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(RulepadGrammarParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Or_Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_or_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOr_" ):
                listener.enterOr_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOr_" ):
                listener.exitOr_(self)




    def or_(self):

        localctx = RulepadGrammarParser.Or_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_or_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(RulepadGrammarParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HaveContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_have

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHave" ):
                listener.enterHave(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHave" ):
                listener.exitHave(self)




    def have(self):

        localctx = RulepadGrammarParser.HaveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_have)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(RulepadGrammarParser.T__14)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WithWordContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_withWord

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWithWord" ):
                listener.enterWithWord(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWithWord" ):
                listener.exitWithWord(self)




    def withWord(self):

        localctx = RulepadGrammarParser.WithWordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_withWord)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(RulepadGrammarParser.T__15)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BinaryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def and_(self):
            return self.getTypedRuleContext(RulepadGrammarParser.And_Context,0)


        def or_(self):
            return self.getTypedRuleContext(RulepadGrammarParser.Or_Context,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_binary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinary" ):
                listener.enterBinary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinary" ):
                listener.exitBinary(self)




    def binary(self):

        localctx = RulepadGrammarParser.BinaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_binary)
        try:
            self.state = 184
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.T__12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.and_()
                pass
            elif token in [RulepadGrammarParser.T__13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 183
                self.or_()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NamesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(RulepadGrammarParser.NAME, 0)

        def nameCondition(self):
            return self.getTypedRuleContext(RulepadGrammarParser.NameConditionContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_names

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNames" ):
                listener.enterNames(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNames" ):
                listener.exitNames(self)




    def names(self):

        localctx = RulepadGrammarParser.NamesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_names)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(RulepadGrammarParser.NAME)
            self.state = 187
            self.nameCondition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameConditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def combinatorialWords(self):
            return self.getTypedRuleContext(RulepadGrammarParser.CombinatorialWordsContext,0)


        def SPACE(self):
            return self.getToken(RulepadGrammarParser.SPACE, 0)

        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_nameCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNameCondition" ):
                listener.enterNameCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNameCondition" ):
                listener.exitNameCondition(self)




    def nameCondition(self):

        localctx = RulepadGrammarParser.NameConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_nameCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.combinatorialWords()
            self.state = 190
            self.match(RulepadGrammarParser.SPACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValuesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VALUE(self):
            return self.getToken(RulepadGrammarParser.VALUE, 0)

        def valueCondition(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ValueConditionContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_values

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValues" ):
                listener.enterValues(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValues" ):
                listener.exitValues(self)




    def values(self):

        localctx = RulepadGrammarParser.ValuesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_values)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(RulepadGrammarParser.VALUE)
            self.state = 193
            self.valueCondition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueConditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def combinatorialWords(self):
            return self.getTypedRuleContext(RulepadGrammarParser.CombinatorialWordsContext,0)


        def SPACE(self):
            return self.getToken(RulepadGrammarParser.SPACE, 0)

        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_valueCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValueCondition" ):
                listener.enterValueCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValueCondition" ):
                listener.exitValueCondition(self)




    def valueCondition(self):

        localctx = RulepadGrammarParser.ValueConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_valueCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.combinatorialWords()
            self.state = 196
            self.match(RulepadGrammarParser.SPACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AnnotationsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ANNOTATION(self):
            return self.getToken(RulepadGrammarParser.ANNOTATION, 0)

        def annotationCondition(self):
            return self.getTypedRuleContext(RulepadGrammarParser.AnnotationConditionContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_annotations

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnnotations" ):
                listener.enterAnnotations(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnnotations" ):
                listener.exitAnnotations(self)




    def annotations(self):

        localctx = RulepadGrammarParser.AnnotationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_annotations)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(RulepadGrammarParser.ANNOTATION)
            self.state = 199
            self.annotationCondition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AnnotationConditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def combinatorialWords(self):
            return self.getTypedRuleContext(RulepadGrammarParser.CombinatorialWordsContext,0)


        def SPACE(self):
            return self.getToken(RulepadGrammarParser.SPACE, 0)

        def annotationConditionTransition(self):
            return self.getTypedRuleContext(RulepadGrammarParser.AnnotationConditionTransitionContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_annotationCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnnotationCondition" ):
                listener.enterAnnotationCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnnotationCondition" ):
                listener.exitAnnotationCondition(self)




    def annotationCondition(self):

        localctx = RulepadGrammarParser.AnnotationConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_annotationCondition)
        try:
            self.state = 207
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 201
                self.combinatorialWords()
                self.state = 202
                self.match(RulepadGrammarParser.SPACE)
                self.state = 204
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 203
                    self.annotationConditionTransition()


                pass
            elif token in [RulepadGrammarParser.T__15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
                self.annotationConditionTransition()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AnnotationConditionTransitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def withWord(self):
            return self.getTypedRuleContext(RulepadGrammarParser.WithWordContext,0)


        def annotationExpression(self):
            return self.getTypedRuleContext(RulepadGrammarParser.AnnotationExpressionContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_annotationConditionTransition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnnotationConditionTransition" ):
                listener.enterAnnotationConditionTransition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnnotationConditionTransition" ):
                listener.exitAnnotationConditionTransition(self)




    def annotationConditionTransition(self):

        localctx = RulepadGrammarParser.AnnotationConditionTransitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_annotationConditionTransition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.withWord()
            self.state = 210
            self.annotationExpression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AnnotationExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # AnnotationExpressionContext
            self.op = None # BinaryContext
            self.right = None # AnnotationExpressionContext

        def LPAREN(self):
            return self.getToken(RulepadGrammarParser.LPAREN, 0)

        def annotationExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RulepadGrammarParser.AnnotationExpressionContext)
            else:
                return self.getTypedRuleContext(RulepadGrammarParser.AnnotationExpressionContext,i)


        def RPAREN(self):
            return self.getToken(RulepadGrammarParser.RPAREN, 0)

        def parameters(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ParametersContext,0)


        def binary(self):
            return self.getTypedRuleContext(RulepadGrammarParser.BinaryContext,0)


        def SPACE(self):
            return self.getToken(RulepadGrammarParser.SPACE, 0)

        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_annotationExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnnotationExpression" ):
                listener.enterAnnotationExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnnotationExpression" ):
                listener.exitAnnotationExpression(self)



    def annotationExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RulepadGrammarParser.AnnotationExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_annotationExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 213
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 214
                self.annotationExpression(0)
                self.state = 215
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.PARAMETER]:
                self.state = 217
                self.parameters()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 228
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 226
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.AnnotationExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_annotationExpression)
                        self.state = 220
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 221
                        localctx.op = self.binary()
                        self.state = 222
                        localctx.right = self.annotationExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.AnnotationExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_annotationExpression)
                        self.state = 224
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 225
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 230
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExtensionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXTENSION(self):
            return self.getToken(RulepadGrammarParser.EXTENSION, 0)

        def extensionCondition(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ExtensionConditionContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_extensions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExtensions" ):
                listener.enterExtensions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExtensions" ):
                listener.exitExtensions(self)




    def extensions(self):

        localctx = RulepadGrammarParser.ExtensionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_extensions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(RulepadGrammarParser.EXTENSION)
            self.state = 232
            self.extensionCondition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExtensionConditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def of(self):
            return self.getTypedRuleContext(RulepadGrammarParser.OfContext,0)


        def combinatorialWords(self):
            return self.getTypedRuleContext(RulepadGrammarParser.CombinatorialWordsContext,0)


        def SPACE(self):
            return self.getToken(RulepadGrammarParser.SPACE, 0)

        def SUPERCLASS(self):
            return self.getToken(RulepadGrammarParser.SUPERCLASS, 0)

        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_extensionCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExtensionCondition" ):
                listener.enterExtensionCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExtensionCondition" ):
                listener.exitExtensionCondition(self)




    def extensionCondition(self):

        localctx = RulepadGrammarParser.ExtensionConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_extensionCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.of()
            self.state = 239
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.T__0]:
                self.state = 235
                self.combinatorialWords()
                self.state = 236
                self.match(RulepadGrammarParser.SPACE)
                pass
            elif token in [RulepadGrammarParser.SUPERCLASS]:
                self.state = 238
                self.match(RulepadGrammarParser.SUPERCLASS)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImplementationsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPLEMENTATION(self):
            return self.getToken(RulepadGrammarParser.IMPLEMENTATION, 0)

        def implementationCondition(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ImplementationConditionContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_implementations

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImplementations" ):
                listener.enterImplementations(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImplementations" ):
                listener.exitImplementations(self)




    def implementations(self):

        localctx = RulepadGrammarParser.ImplementationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_implementations)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(RulepadGrammarParser.IMPLEMENTATION)
            self.state = 242
            self.implementationCondition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImplementationConditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def of(self):
            return self.getTypedRuleContext(RulepadGrammarParser.OfContext,0)


        def combinatorialWords(self):
            return self.getTypedRuleContext(RulepadGrammarParser.CombinatorialWordsContext,0)


        def SPACE(self):
            return self.getToken(RulepadGrammarParser.SPACE, 0)

        def INTERFACE(self):
            return self.getToken(RulepadGrammarParser.INTERFACE, 0)

        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_implementationCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImplementationCondition" ):
                listener.enterImplementationCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImplementationCondition" ):
                listener.exitImplementationCondition(self)




    def implementationCondition(self):

        localctx = RulepadGrammarParser.ImplementationConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_implementationCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.of()
            self.state = 249
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.T__0]:
                self.state = 245
                self.combinatorialWords()
                self.state = 246
                self.match(RulepadGrammarParser.SPACE)
                pass
            elif token in [RulepadGrammarParser.INTERFACE]:
                self.state = 248
                self.match(RulepadGrammarParser.INTERFACE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(RulepadGrammarParser.FUNCTION, 0)

        def functionCondition(self):
            return self.getTypedRuleContext(RulepadGrammarParser.FunctionConditionContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_functions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctions" ):
                listener.enterFunctions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctions" ):
                listener.exitFunctions(self)




    def functions(self):

        localctx = RulepadGrammarParser.FunctionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_functions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(RulepadGrammarParser.FUNCTION)
            self.state = 252
            self.functionCondition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionConditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def withWord(self):
            return self.getTypedRuleContext(RulepadGrammarParser.WithWordContext,0)


        def functionExpression(self):
            return self.getTypedRuleContext(RulepadGrammarParser.FunctionExpressionContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_functionCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCondition" ):
                listener.enterFunctionCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCondition" ):
                listener.exitFunctionCondition(self)




    def functionCondition(self):

        localctx = RulepadGrammarParser.FunctionConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_functionCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.withWord()
            self.state = 255
            self.functionExpression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # FunctionExpressionContext
            self.op = None # BinaryContext
            self.right = None # FunctionExpressionContext

        def LPAREN(self):
            return self.getToken(RulepadGrammarParser.LPAREN, 0)

        def functionExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RulepadGrammarParser.FunctionExpressionContext)
            else:
                return self.getTypedRuleContext(RulepadGrammarParser.FunctionExpressionContext,i)


        def RPAREN(self):
            return self.getToken(RulepadGrammarParser.RPAREN, 0)

        def annotations(self):
            return self.getTypedRuleContext(RulepadGrammarParser.AnnotationsContext,0)


        def types(self):
            return self.getTypedRuleContext(RulepadGrammarParser.TypesContext,0)


        def functionParameters(self):
            return self.getTypedRuleContext(RulepadGrammarParser.FunctionParametersContext,0)


        def configurationFiles(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ConfigurationFilesContext,0)


        def binary(self):
            return self.getTypedRuleContext(RulepadGrammarParser.BinaryContext,0)


        def SPACE(self):
            return self.getToken(RulepadGrammarParser.SPACE, 0)

        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_functionExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionExpression" ):
                listener.enterFunctionExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionExpression" ):
                listener.exitFunctionExpression(self)



    def functionExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RulepadGrammarParser.FunctionExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_functionExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 258
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 259
                self.functionExpression(0)
                self.state = 260
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.ANNOTATION, RulepadGrammarParser.PARAMETER, RulepadGrammarParser.TYPES, RulepadGrammarParser.ConfigurationFile]:
                self.state = 266
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.ANNOTATION]:
                    self.state = 262
                    self.annotations()
                    pass
                elif token in [RulepadGrammarParser.TYPES]:
                    self.state = 263
                    self.types()
                    pass
                elif token in [RulepadGrammarParser.PARAMETER]:
                    self.state = 264
                    self.functionParameters()
                    pass
                elif token in [RulepadGrammarParser.ConfigurationFile]:
                    self.state = 265
                    self.configurationFiles()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 278
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 276
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.FunctionExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_functionExpression)
                        self.state = 270
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 271
                        localctx.op = self.binary()
                        self.state = 272
                        localctx.right = self.functionExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.FunctionExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_functionExpression)
                        self.state = 274
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 275
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 280
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ConstructorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTRUCTOR(self):
            return self.getToken(RulepadGrammarParser.CONSTRUCTOR, 0)

        def constructorCondition(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ConstructorConditionContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_constructors

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstructors" ):
                listener.enterConstructors(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstructors" ):
                listener.exitConstructors(self)




    def constructors(self):

        localctx = RulepadGrammarParser.ConstructorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_constructors)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(RulepadGrammarParser.CONSTRUCTOR)
            self.state = 282
            self.constructorCondition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorOfContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def of(self):
            return self.getTypedRuleContext(RulepadGrammarParser.OfContext,0)


        def classes(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ClassesContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_constructorOf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstructorOf" ):
                listener.enterConstructorOf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstructorOf" ):
                listener.exitConstructorOf(self)




    def constructorOf(self):

        localctx = RulepadGrammarParser.ConstructorOfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_constructorOf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.of()
            self.state = 285
            self.classes()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorConditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def withWord(self):
            return self.getTypedRuleContext(RulepadGrammarParser.WithWordContext,0)


        def constructorExpression(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ConstructorExpressionContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_constructorCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstructorCondition" ):
                listener.enterConstructorCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstructorCondition" ):
                listener.exitConstructorCondition(self)




    def constructorCondition(self):

        localctx = RulepadGrammarParser.ConstructorConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_constructorCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.withWord()
            self.state = 288
            self.constructorExpression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # ConstructorExpressionContext
            self.op = None # BinaryContext
            self.right = None # ConstructorExpressionContext

        def LPAREN(self):
            return self.getToken(RulepadGrammarParser.LPAREN, 0)

        def constructorExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RulepadGrammarParser.ConstructorExpressionContext)
            else:
                return self.getTypedRuleContext(RulepadGrammarParser.ConstructorExpressionContext,i)


        def RPAREN(self):
            return self.getToken(RulepadGrammarParser.RPAREN, 0)

        def annotations(self):
            return self.getTypedRuleContext(RulepadGrammarParser.AnnotationsContext,0)


        def functionParameters(self):
            return self.getTypedRuleContext(RulepadGrammarParser.FunctionParametersContext,0)


        def binary(self):
            return self.getTypedRuleContext(RulepadGrammarParser.BinaryContext,0)


        def SPACE(self):
            return self.getToken(RulepadGrammarParser.SPACE, 0)

        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_constructorExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstructorExpression" ):
                listener.enterConstructorExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstructorExpression" ):
                listener.exitConstructorExpression(self)



    def constructorExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RulepadGrammarParser.ConstructorExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_constructorExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 291
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 292
                self.constructorExpression(0)
                self.state = 293
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.ANNOTATION, RulepadGrammarParser.PARAMETER]:
                self.state = 297
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.ANNOTATION]:
                    self.state = 295
                    self.annotations()
                    pass
                elif token in [RulepadGrammarParser.PARAMETER]:
                    self.state = 296
                    self.functionParameters()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 309
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 307
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.ConstructorExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_constructorExpression)
                        self.state = 301
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 302
                        localctx.op = self.binary()
                        self.state = 303
                        localctx.right = self.constructorExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.ConstructorExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_constructorExpression)
                        self.state = 305
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 306
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 311
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ParametersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARAMETER(self):
            return self.getToken(RulepadGrammarParser.PARAMETER, 0)

        def parameterCondition(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ParameterConditionContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameters" ):
                listener.enterParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameters" ):
                listener.exitParameters(self)




    def parameters(self):

        localctx = RulepadGrammarParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_parameters)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.match(RulepadGrammarParser.PARAMETER)
            self.state = 313
            self.parameterCondition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterConditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def combinatorialWords(self):
            return self.getTypedRuleContext(RulepadGrammarParser.CombinatorialWordsContext,0)


        def SPACE(self):
            return self.getToken(RulepadGrammarParser.SPACE, 0)

        def parameterConditionTransition(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ParameterConditionTransitionContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_parameterCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterCondition" ):
                listener.enterParameterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterCondition" ):
                listener.exitParameterCondition(self)




    def parameterCondition(self):

        localctx = RulepadGrammarParser.ParameterConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_parameterCondition)
        try:
            self.state = 321
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 315
                self.combinatorialWords()
                self.state = 316
                self.match(RulepadGrammarParser.SPACE)
                self.state = 318
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                if la_ == 1:
                    self.state = 317
                    self.parameterConditionTransition()


                pass
            elif token in [RulepadGrammarParser.T__15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 320
                self.parameterConditionTransition()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterConditionTransitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def withWord(self):
            return self.getTypedRuleContext(RulepadGrammarParser.WithWordContext,0)


        def parameterExpression(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ParameterExpressionContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_parameterConditionTransition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterConditionTransition" ):
                listener.enterParameterConditionTransition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterConditionTransition" ):
                listener.exitParameterConditionTransition(self)




    def parameterConditionTransition(self):

        localctx = RulepadGrammarParser.ParameterConditionTransitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_parameterConditionTransition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.withWord()
            self.state = 324
            self.parameterExpression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # ParameterExpressionContext
            self.op = None # BinaryContext
            self.right = None # ParameterExpressionContext

        def LPAREN(self):
            return self.getToken(RulepadGrammarParser.LPAREN, 0)

        def parameterExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RulepadGrammarParser.ParameterExpressionContext)
            else:
                return self.getTypedRuleContext(RulepadGrammarParser.ParameterExpressionContext,i)


        def RPAREN(self):
            return self.getToken(RulepadGrammarParser.RPAREN, 0)

        def types(self):
            return self.getTypedRuleContext(RulepadGrammarParser.TypesContext,0)


        def names(self):
            return self.getTypedRuleContext(RulepadGrammarParser.NamesContext,0)


        def values(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ValuesContext,0)


        def binary(self):
            return self.getTypedRuleContext(RulepadGrammarParser.BinaryContext,0)


        def SPACE(self):
            return self.getToken(RulepadGrammarParser.SPACE, 0)

        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_parameterExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterExpression" ):
                listener.enterParameterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterExpression" ):
                listener.exitParameterExpression(self)



    def parameterExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RulepadGrammarParser.ParameterExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_parameterExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 327
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 328
                self.parameterExpression(0)
                self.state = 329
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.NAME, RulepadGrammarParser.VALUE, RulepadGrammarParser.TYPES]:
                self.state = 334
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.TYPES]:
                    self.state = 331
                    self.types()
                    pass
                elif token in [RulepadGrammarParser.NAME]:
                    self.state = 332
                    self.names()
                    pass
                elif token in [RulepadGrammarParser.VALUE]:
                    self.state = 333
                    self.values()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 346
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 344
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.ParameterExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_parameterExpression)
                        self.state = 338
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 339
                        localctx.op = self.binary()
                        self.state = 340
                        localctx.right = self.parameterExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.ParameterExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_parameterExpression)
                        self.state = 342
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 343
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 348
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FunctionParametersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARAMETER(self):
            return self.getToken(RulepadGrammarParser.PARAMETER, 0)

        def functionParameterCondition(self):
            return self.getTypedRuleContext(RulepadGrammarParser.FunctionParameterConditionContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_functionParameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionParameters" ):
                listener.enterFunctionParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionParameters" ):
                listener.exitFunctionParameters(self)




    def functionParameters(self):

        localctx = RulepadGrammarParser.FunctionParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_functionParameters)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.match(RulepadGrammarParser.PARAMETER)
            self.state = 351
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 350
                self.functionParameterCondition()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionParameterConditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def combinatorialWords(self):
            return self.getTypedRuleContext(RulepadGrammarParser.CombinatorialWordsContext,0)


        def SPACE(self):
            return self.getToken(RulepadGrammarParser.SPACE, 0)

        def functionParameterConditionTransition(self):
            return self.getTypedRuleContext(RulepadGrammarParser.FunctionParameterConditionTransitionContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_functionParameterCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionParameterCondition" ):
                listener.enterFunctionParameterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionParameterCondition" ):
                listener.exitFunctionParameterCondition(self)




    def functionParameterCondition(self):

        localctx = RulepadGrammarParser.FunctionParameterConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_functionParameterCondition)
        try:
            self.state = 359
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 353
                self.combinatorialWords()
                self.state = 354
                self.match(RulepadGrammarParser.SPACE)
                self.state = 356
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                if la_ == 1:
                    self.state = 355
                    self.functionParameterConditionTransition()


                pass
            elif token in [RulepadGrammarParser.T__15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 358
                self.functionParameterConditionTransition()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionParameterConditionTransitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def withWord(self):
            return self.getTypedRuleContext(RulepadGrammarParser.WithWordContext,0)


        def functionParameterExpression(self):
            return self.getTypedRuleContext(RulepadGrammarParser.FunctionParameterExpressionContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_functionParameterConditionTransition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionParameterConditionTransition" ):
                listener.enterFunctionParameterConditionTransition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionParameterConditionTransition" ):
                listener.exitFunctionParameterConditionTransition(self)




    def functionParameterConditionTransition(self):

        localctx = RulepadGrammarParser.FunctionParameterConditionTransitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_functionParameterConditionTransition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.withWord()
            self.state = 362
            self.functionParameterExpression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionParameterExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # FunctionParameterExpressionContext
            self.op = None # BinaryContext
            self.right = None # FunctionParameterExpressionContext

        def LPAREN(self):
            return self.getToken(RulepadGrammarParser.LPAREN, 0)

        def functionParameterExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RulepadGrammarParser.FunctionParameterExpressionContext)
            else:
                return self.getTypedRuleContext(RulepadGrammarParser.FunctionParameterExpressionContext,i)


        def RPAREN(self):
            return self.getToken(RulepadGrammarParser.RPAREN, 0)

        def types(self):
            return self.getTypedRuleContext(RulepadGrammarParser.TypesContext,0)


        def names(self):
            return self.getTypedRuleContext(RulepadGrammarParser.NamesContext,0)


        def annotations(self):
            return self.getTypedRuleContext(RulepadGrammarParser.AnnotationsContext,0)


        def binary(self):
            return self.getTypedRuleContext(RulepadGrammarParser.BinaryContext,0)


        def SPACE(self):
            return self.getToken(RulepadGrammarParser.SPACE, 0)

        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_functionParameterExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionParameterExpression" ):
                listener.enterFunctionParameterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionParameterExpression" ):
                listener.exitFunctionParameterExpression(self)



    def functionParameterExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RulepadGrammarParser.FunctionParameterExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_functionParameterExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 365
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 366
                self.functionParameterExpression(0)
                self.state = 367
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.NAME, RulepadGrammarParser.ANNOTATION, RulepadGrammarParser.TYPES]:
                self.state = 372
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.TYPES]:
                    self.state = 369
                    self.types()
                    pass
                elif token in [RulepadGrammarParser.NAME]:
                    self.state = 370
                    self.names()
                    pass
                elif token in [RulepadGrammarParser.ANNOTATION]:
                    self.state = 371
                    self.annotations()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 384
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 382
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.FunctionParameterExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_functionParameterExpression)
                        self.state = 376
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 377
                        localctx.op = self.binary()
                        self.state = 378
                        localctx.right = self.functionParameterExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.FunctionParameterExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_functionParameterExpression)
                        self.state = 380
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 381
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 386
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TypesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPES(self):
            return self.getToken(RulepadGrammarParser.TYPES, 0)

        def typeCondition(self):
            return self.getTypedRuleContext(RulepadGrammarParser.TypeConditionContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_types

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypes" ):
                listener.enterTypes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypes" ):
                listener.exitTypes(self)




    def types(self):

        localctx = RulepadGrammarParser.TypesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_types)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.match(RulepadGrammarParser.TYPES)
            self.state = 388
            self.typeCondition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeConditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def combinatorialWords(self):
            return self.getTypedRuleContext(RulepadGrammarParser.CombinatorialWordsContext,0)


        def SPACE(self):
            return self.getToken(RulepadGrammarParser.SPACE, 0)

        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_typeCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeCondition" ):
                listener.enterTypeCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeCondition" ):
                listener.exitTypeCondition(self)




    def typeCondition(self):

        localctx = RulepadGrammarParser.TypeConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_typeCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self.combinatorialWords()
            self.state = 391
            self.match(RulepadGrammarParser.SPACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationStatementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DeclarationStatement(self):
            return self.getToken(RulepadGrammarParser.DeclarationStatement, 0)

        def declarationStatementCondition(self):
            return self.getTypedRuleContext(RulepadGrammarParser.DeclarationStatementConditionContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_declarationStatements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclarationStatements" ):
                listener.enterDeclarationStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclarationStatements" ):
                listener.exitDeclarationStatements(self)




    def declarationStatements(self):

        localctx = RulepadGrammarParser.DeclarationStatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_declarationStatements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.match(RulepadGrammarParser.DeclarationStatement)
            self.state = 394
            self.declarationStatementCondition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationStatementConditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def withWord(self):
            return self.getTypedRuleContext(RulepadGrammarParser.WithWordContext,0)


        def declarationStatementExpression(self):
            return self.getTypedRuleContext(RulepadGrammarParser.DeclarationStatementExpressionContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_declarationStatementCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclarationStatementCondition" ):
                listener.enterDeclarationStatementCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclarationStatementCondition" ):
                listener.exitDeclarationStatementCondition(self)




    def declarationStatementCondition(self):

        localctx = RulepadGrammarParser.DeclarationStatementConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_declarationStatementCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            self.withWord()
            self.state = 397
            self.declarationStatementExpression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationStatementExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # DeclarationStatementExpressionContext
            self.op = None # BinaryContext
            self.right = None # DeclarationStatementExpressionContext

        def LPAREN(self):
            return self.getToken(RulepadGrammarParser.LPAREN, 0)

        def declarationStatementExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RulepadGrammarParser.DeclarationStatementExpressionContext)
            else:
                return self.getTypedRuleContext(RulepadGrammarParser.DeclarationStatementExpressionContext,i)


        def RPAREN(self):
            return self.getToken(RulepadGrammarParser.RPAREN, 0)

        def annotations(self):
            return self.getTypedRuleContext(RulepadGrammarParser.AnnotationsContext,0)


        def types(self):
            return self.getTypedRuleContext(RulepadGrammarParser.TypesContext,0)


        def configurationFiles(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ConfigurationFilesContext,0)


        def binary(self):
            return self.getTypedRuleContext(RulepadGrammarParser.BinaryContext,0)


        def SPACE(self):
            return self.getToken(RulepadGrammarParser.SPACE, 0)

        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_declarationStatementExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclarationStatementExpression" ):
                listener.enterDeclarationStatementExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclarationStatementExpression" ):
                listener.exitDeclarationStatementExpression(self)



    def declarationStatementExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RulepadGrammarParser.DeclarationStatementExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_declarationStatementExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 400
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 401
                self.declarationStatementExpression(0)
                self.state = 402
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.ANNOTATION, RulepadGrammarParser.TYPES, RulepadGrammarParser.ConfigurationFile]:
                self.state = 407
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.ANNOTATION]:
                    self.state = 404
                    self.annotations()
                    pass
                elif token in [RulepadGrammarParser.TYPES]:
                    self.state = 405
                    self.types()
                    pass
                elif token in [RulepadGrammarParser.ConfigurationFile]:
                    self.state = 406
                    self.configurationFiles()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 419
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 417
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.DeclarationStatementExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_declarationStatementExpression)
                        self.state = 411
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 412
                        localctx.op = self.binary()
                        self.state = 413
                        localctx.right = self.declarationStatementExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.DeclarationStatementExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_declarationStatementExpression)
                        self.state = 415
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 416
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 421
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ConfigurationFilesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ConfigurationFile(self):
            return self.getToken(RulepadGrammarParser.ConfigurationFile, 0)

        def configurationFileCondition(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ConfigurationFileConditionContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_configurationFiles

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConfigurationFiles" ):
                listener.enterConfigurationFiles(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConfigurationFiles" ):
                listener.exitConfigurationFiles(self)




    def configurationFiles(self):

        localctx = RulepadGrammarParser.ConfigurationFilesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_configurationFiles)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.match(RulepadGrammarParser.ConfigurationFile)
            self.state = 423
            self.configurationFileCondition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConfigurationFileConditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def withWord(self):
            return self.getTypedRuleContext(RulepadGrammarParser.WithWordContext,0)


        def configurationFileExpression(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ConfigurationFileExpressionContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_configurationFileCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConfigurationFileCondition" ):
                listener.enterConfigurationFileCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConfigurationFileCondition" ):
                listener.exitConfigurationFileCondition(self)




    def configurationFileCondition(self):

        localctx = RulepadGrammarParser.ConfigurationFileConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_configurationFileCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
            self.withWord()
            self.state = 426
            self.configurationFileExpression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConfigurationFileExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # ConfigurationFileExpressionContext
            self.op = None # BinaryContext
            self.right = None # ConfigurationFileExpressionContext

        def LPAREN(self):
            return self.getToken(RulepadGrammarParser.LPAREN, 0)

        def configurationFileExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RulepadGrammarParser.ConfigurationFileExpressionContext)
            else:
                return self.getTypedRuleContext(RulepadGrammarParser.ConfigurationFileExpressionContext,i)


        def RPAREN(self):
            return self.getToken(RulepadGrammarParser.RPAREN, 0)

        def configurationProperties(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ConfigurationPropertiesContext,0)


        def binary(self):
            return self.getTypedRuleContext(RulepadGrammarParser.BinaryContext,0)


        def SPACE(self):
            return self.getToken(RulepadGrammarParser.SPACE, 0)

        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_configurationFileExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConfigurationFileExpression" ):
                listener.enterConfigurationFileExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConfigurationFileExpression" ):
                listener.exitConfigurationFileExpression(self)



    def configurationFileExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RulepadGrammarParser.ConfigurationFileExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 94
        self.enterRecursionRule(localctx, 94, self.RULE_configurationFileExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 429
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 430
                self.configurationFileExpression(0)
                self.state = 431
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.CONFIGURATION_PROPERTIES]:
                self.state = 433
                self.configurationProperties()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 444
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 442
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.ConfigurationFileExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_configurationFileExpression)
                        self.state = 436
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 437
                        localctx.op = self.binary()
                        self.state = 438
                        localctx.right = self.configurationFileExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.ConfigurationFileExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_configurationFileExpression)
                        self.state = 440
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 441
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 446
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ConfigurationPropertiesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONFIGURATION_PROPERTIES(self):
            return self.getToken(RulepadGrammarParser.CONFIGURATION_PROPERTIES, 0)

        def configurationPropertyCondition(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ConfigurationPropertyConditionContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_configurationProperties

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConfigurationProperties" ):
                listener.enterConfigurationProperties(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConfigurationProperties" ):
                listener.exitConfigurationProperties(self)




    def configurationProperties(self):

        localctx = RulepadGrammarParser.ConfigurationPropertiesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_configurationProperties)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 447
            self.match(RulepadGrammarParser.CONFIGURATION_PROPERTIES)
            self.state = 448
            self.configurationPropertyCondition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConfigurationPropertyConditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def combinatorialWords(self):
            return self.getTypedRuleContext(RulepadGrammarParser.CombinatorialWordsContext,0)


        def SPACE(self):
            return self.getToken(RulepadGrammarParser.SPACE, 0)

        def configurationPropertyConditionTransition(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ConfigurationPropertyConditionTransitionContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_configurationPropertyCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConfigurationPropertyCondition" ):
                listener.enterConfigurationPropertyCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConfigurationPropertyCondition" ):
                listener.exitConfigurationPropertyCondition(self)




    def configurationPropertyCondition(self):

        localctx = RulepadGrammarParser.ConfigurationPropertyConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_configurationPropertyCondition)
        try:
            self.state = 456
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 450
                self.combinatorialWords()
                self.state = 451
                self.match(RulepadGrammarParser.SPACE)
                self.state = 453
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
                if la_ == 1:
                    self.state = 452
                    self.configurationPropertyConditionTransition()


                pass
            elif token in [RulepadGrammarParser.T__15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 455
                self.configurationPropertyConditionTransition()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConfigurationPropertyConditionTransitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def withWord(self):
            return self.getTypedRuleContext(RulepadGrammarParser.WithWordContext,0)


        def configurationPropertyExpression(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ConfigurationPropertyExpressionContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_configurationPropertyConditionTransition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConfigurationPropertyConditionTransition" ):
                listener.enterConfigurationPropertyConditionTransition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConfigurationPropertyConditionTransition" ):
                listener.exitConfigurationPropertyConditionTransition(self)




    def configurationPropertyConditionTransition(self):

        localctx = RulepadGrammarParser.ConfigurationPropertyConditionTransitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_configurationPropertyConditionTransition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 458
            self.withWord()
            self.state = 459
            self.configurationPropertyExpression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConfigurationPropertyExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # ConfigurationPropertyExpressionContext
            self.op = None # BinaryContext
            self.right = None # ConfigurationPropertyExpressionContext

        def LPAREN(self):
            return self.getToken(RulepadGrammarParser.LPAREN, 0)

        def configurationPropertyExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RulepadGrammarParser.ConfigurationPropertyExpressionContext)
            else:
                return self.getTypedRuleContext(RulepadGrammarParser.ConfigurationPropertyExpressionContext,i)


        def RPAREN(self):
            return self.getToken(RulepadGrammarParser.RPAREN, 0)

        def types(self):
            return self.getTypedRuleContext(RulepadGrammarParser.TypesContext,0)


        def names(self):
            return self.getTypedRuleContext(RulepadGrammarParser.NamesContext,0)


        def values(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ValuesContext,0)


        def binary(self):
            return self.getTypedRuleContext(RulepadGrammarParser.BinaryContext,0)


        def SPACE(self):
            return self.getToken(RulepadGrammarParser.SPACE, 0)

        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_configurationPropertyExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConfigurationPropertyExpression" ):
                listener.enterConfigurationPropertyExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConfigurationPropertyExpression" ):
                listener.exitConfigurationPropertyExpression(self)



    def configurationPropertyExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RulepadGrammarParser.ConfigurationPropertyExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 102
        self.enterRecursionRule(localctx, 102, self.RULE_configurationPropertyExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 462
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 463
                self.configurationPropertyExpression(0)
                self.state = 464
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.NAME, RulepadGrammarParser.VALUE, RulepadGrammarParser.TYPES]:
                self.state = 469
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.TYPES]:
                    self.state = 466
                    self.types()
                    pass
                elif token in [RulepadGrammarParser.NAME]:
                    self.state = 467
                    self.names()
                    pass
                elif token in [RulepadGrammarParser.VALUE]:
                    self.state = 468
                    self.values()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 481
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,48,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 479
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.ConfigurationPropertyExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_configurationPropertyExpression)
                        self.state = 473
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 474
                        localctx.op = self.binary()
                        self.state = 475
                        localctx.right = self.configurationPropertyExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.ConfigurationPropertyExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_configurationPropertyExpression)
                        self.state = 477
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 478
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 483
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,48,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ClassesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASSES(self):
            return self.getToken(RulepadGrammarParser.CLASSES, 0)

        def classCondition(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ClassConditionContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_classes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClasses" ):
                listener.enterClasses(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClasses" ):
                listener.exitClasses(self)




    def classes(self):

        localctx = RulepadGrammarParser.ClassesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_classes)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 484
            self.match(RulepadGrammarParser.CLASSES)
            self.state = 485
            self.classCondition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassConditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def withWord(self):
            return self.getTypedRuleContext(RulepadGrammarParser.WithWordContext,0)


        def classExpression(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ClassExpressionContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_classCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassCondition" ):
                listener.enterClassCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassCondition" ):
                listener.exitClassCondition(self)




    def classCondition(self):

        localctx = RulepadGrammarParser.ClassConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_classCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 487
            self.withWord()
            self.state = 488
            self.classExpression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # ClassExpressionContext
            self.op = None # BinaryContext
            self.right = None # ClassExpressionContext

        def LPAREN(self):
            return self.getToken(RulepadGrammarParser.LPAREN, 0)

        def classExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RulepadGrammarParser.ClassExpressionContext)
            else:
                return self.getTypedRuleContext(RulepadGrammarParser.ClassExpressionContext,i)


        def RPAREN(self):
            return self.getToken(RulepadGrammarParser.RPAREN, 0)

        def annotations(self):
            return self.getTypedRuleContext(RulepadGrammarParser.AnnotationsContext,0)


        def extensions(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ExtensionsContext,0)


        def implementations(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ImplementationsContext,0)


        def functions(self):
            return self.getTypedRuleContext(RulepadGrammarParser.FunctionsContext,0)


        def constructors(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ConstructorsContext,0)


        def declarationStatements(self):
            return self.getTypedRuleContext(RulepadGrammarParser.DeclarationStatementsContext,0)


        def configurationFiles(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ConfigurationFilesContext,0)


        def beans(self):
            return self.getTypedRuleContext(RulepadGrammarParser.BeansContext,0)


        def binary(self):
            return self.getTypedRuleContext(RulepadGrammarParser.BinaryContext,0)


        def SPACE(self):
            return self.getToken(RulepadGrammarParser.SPACE, 0)

        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_classExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassExpression" ):
                listener.enterClassExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassExpression" ):
                listener.exitClassExpression(self)



    def classExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RulepadGrammarParser.ClassExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 108
        self.enterRecursionRule(localctx, 108, self.RULE_classExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 505
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 491
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 492
                self.classExpression(0)
                self.state = 493
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.ANNOTATION, RulepadGrammarParser.EXTENSION, RulepadGrammarParser.IMPLEMENTATION, RulepadGrammarParser.FUNCTION, RulepadGrammarParser.CONSTRUCTOR, RulepadGrammarParser.DeclarationStatement, RulepadGrammarParser.ConfigurationFile, RulepadGrammarParser.BEAN_DECL]:
                self.state = 503
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.ANNOTATION]:
                    self.state = 495
                    self.annotations()
                    pass
                elif token in [RulepadGrammarParser.EXTENSION]:
                    self.state = 496
                    self.extensions()
                    pass
                elif token in [RulepadGrammarParser.IMPLEMENTATION]:
                    self.state = 497
                    self.implementations()
                    pass
                elif token in [RulepadGrammarParser.FUNCTION]:
                    self.state = 498
                    self.functions()
                    pass
                elif token in [RulepadGrammarParser.CONSTRUCTOR]:
                    self.state = 499
                    self.constructors()
                    pass
                elif token in [RulepadGrammarParser.DeclarationStatement]:
                    self.state = 500
                    self.declarationStatements()
                    pass
                elif token in [RulepadGrammarParser.ConfigurationFile]:
                    self.state = 501
                    self.configurationFiles()
                    pass
                elif token in [RulepadGrammarParser.BEAN_DECL]:
                    self.state = 502
                    self.beans()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 515
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,52,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 513
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.ClassExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_classExpression)
                        self.state = 507
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 508
                        localctx.op = self.binary()
                        self.state = 509
                        localctx.right = self.classExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.ClassExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_classExpression)
                        self.state = 511
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 512
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 517
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,52,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class BeansContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEAN_DECL(self):
            return self.getToken(RulepadGrammarParser.BEAN_DECL, 0)

        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_beans

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBeans" ):
                listener.enterBeans(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBeans" ):
                listener.exitBeans(self)




    def beans(self):

        localctx = RulepadGrammarParser.BeansContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_beans)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 518
            self.match(RulepadGrammarParser.BEAN_DECL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[20] = self.annotationExpression_sempred
        self._predicates[27] = self.functionExpression_sempred
        self._predicates[31] = self.constructorExpression_sempred
        self._predicates[35] = self.parameterExpression_sempred
        self._predicates[39] = self.functionParameterExpression_sempred
        self._predicates[44] = self.declarationStatementExpression_sempred
        self._predicates[47] = self.configurationFileExpression_sempred
        self._predicates[51] = self.configurationPropertyExpression_sempred
        self._predicates[54] = self.classExpression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def annotationExpression_sempred(self, localctx:AnnotationExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def functionExpression_sempred(self, localctx:FunctionExpressionContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         

    def constructorExpression_sempred(self, localctx:ConstructorExpressionContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 1)
         

    def parameterExpression_sempred(self, localctx:ParameterExpressionContext, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 1)
         

    def functionParameterExpression_sempred(self, localctx:FunctionParameterExpressionContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 1)
         

    def declarationStatementExpression_sempred(self, localctx:DeclarationStatementExpressionContext, predIndex:int):
            if predIndex == 10:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 1)
         

    def configurationFileExpression_sempred(self, localctx:ConfigurationFileExpressionContext, predIndex:int):
            if predIndex == 12:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 1)
         

    def configurationPropertyExpression_sempred(self, localctx:ConfigurationPropertyExpressionContext, predIndex:int):
            if predIndex == 14:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 1)
         

    def classExpression_sempred(self, localctx:ClassExpressionContext, predIndex:int):
            if predIndex == 16:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 17:
                return self.precpred(self._ctx, 1)
         




