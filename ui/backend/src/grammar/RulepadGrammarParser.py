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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3-")
        buf.write("\u02b4\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\3\2\7\2\u0096\n")
        buf.write("\2\f\2\16\2\u0099\13\2\3\2\5\2\u009c\n\2\3\2\5\2\u009f")
        buf.write("\n\2\3\2\7\2\u00a2\n\2\f\2\16\2\u00a5\13\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\5\3\u00bd\n\3\3\4\3\4\3\4\3\4\6")
        buf.write("\4\u00c3\n\4\r\4\16\4\u00c4\3\4\3\4\3\5\3\5\3\6\3\6\3")
        buf.write("\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3")
        buf.write("\r\3\16\3\16\5\16\u00dd\n\16\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\5\24\u00f1\n\24\3\24\5\24\u00f4\n\24\3\25\3")
        buf.write("\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u00ff\n\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\7\26\u0107\n\26\f\26\16")
        buf.write("\26\u010a\13\26\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\5\35\u012d\n\35\5\35\u012f\n\35\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\35\7\35\u0137\n\35\f\35\16\35\u013a")
        buf.write("\13\35\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3")
        buf.write("\37\3 \3 \3 \3 \3 \3 \5 \u014c\n \3!\3!\3!\3!\3!\3!\5")
        buf.write("!\u0154\n!\3!\3!\3!\3!\7!\u015a\n!\f!\16!\u015d\13!\3")
        buf.write("\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'")
        buf.write("\3\'\3\'\3\'\3\'\3\'\5\'\u0175\n\'\5\'\u0177\n\'\3\'\3")
        buf.write("\'\3\'\3\'\3\'\3\'\7\'\u017f\n\'\f\'\16\'\u0182\13\'\3")
        buf.write("(\3(\3(\3)\3)\3)\5)\u018a\n)\3)\5)\u018d\n)\3*\3*\3*\3")
        buf.write("+\3+\3+\3+\3+\3+\3+\3+\5+\u019a\n+\5+\u019c\n+\3+\3+\3")
        buf.write("+\3+\3+\3+\7+\u01a4\n+\f+\16+\u01a7\13+\3,\3,\5,\u01ab")
        buf.write("\n,\3-\3-\3-\5-\u01b0\n-\3-\5-\u01b3\n-\3.\3.\3.\3/\3")
        buf.write("/\3/\3/\3/\3/\3/\3/\5/\u01c0\n/\5/\u01c2\n/\3/\3/\3/\3")
        buf.write("/\3/\3/\7/\u01ca\n/\f/\16/\u01cd\13/\3\60\3\60\3\60\3")
        buf.write("\61\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3\63\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\5\64")
        buf.write("\u01e7\n\64\5\64\u01e9\n\64\3\64\3\64\3\64\3\64\3\64\3")
        buf.write("\64\7\64\u01f1\n\64\f\64\16\64\u01f4\13\64\3\65\3\65\3")
        buf.write("\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\67\3\67\3\67")
        buf.write("\3\67\3\67\5\67\u0205\n\67\38\38\38\38\38\58\u020c\n8")
        buf.write("\38\38\38\38\78\u0212\n8\f8\168\u0215\138\39\39\39\3:")
        buf.write("\3:\3:\3;\3;\3;\3;\3;\3;\5;\u0223\n;\3;\3;\3;\3;\3;\3")
        buf.write(";\7;\u022b\n;\f;\16;\u022e\13;\3<\3<\3<\3=\3=\3=\5=\u0236")
        buf.write("\n=\3=\5=\u0239\n=\3>\3>\3>\3?\3?\3?\3?\3?\3?\3?\3?\5")
        buf.write("?\u0246\n?\5?\u0248\n?\3?\3?\3?\3?\3?\3?\7?\u0250\n?\f")
        buf.write("?\16?\u0253\13?\3@\3@\3@\3A\3A\3A\3B\3B\3B\3B\3B\3B\3")
        buf.write("B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\5B\u026d\nB\5B\u026f")
        buf.write("\nB\3B\3B\3B\3B\3B\3B\7B\u0277\nB\fB\16B\u027a\13B\3C")
        buf.write("\3C\3C\3C\3C\3D\3D\3D\3D\3D\3E\3E\3E\3E\3E\3E\3E\3E\3")
        buf.write("E\3E\3E\5E\u0291\nE\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\5")
        buf.write("F\u029e\nF\3F\3F\3F\3F\7F\u02a4\nF\fF\16F\u02a7\13F\3")
        buf.write("G\3G\3G\3H\3H\3H\3H\3I\3I\3J\3J\3J\2\16*8@LT\\fnt|\u0082")
        buf.write("\u008aK\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*")
        buf.write(",.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080")
        buf.write("\u0082\u0084\u0086\u0088\u008a\u008c\u008e\u0090\u0092")
        buf.write("\2\3\4\2\4\r\27\30\2\u02dc\2\u009b\3\2\2\2\4\u00bc\3\2")
        buf.write("\2\2\6\u00be\3\2\2\2\b\u00c8\3\2\2\2\n\u00ca\3\2\2\2\f")
        buf.write("\u00cc\3\2\2\2\16\u00ce\3\2\2\2\20\u00d0\3\2\2\2\22\u00d2")
        buf.write("\3\2\2\2\24\u00d4\3\2\2\2\26\u00d6\3\2\2\2\30\u00d8\3")
        buf.write("\2\2\2\32\u00dc\3\2\2\2\34\u00de\3\2\2\2\36\u00e1\3\2")
        buf.write("\2\2 \u00e4\3\2\2\2\"\u00e7\3\2\2\2$\u00ea\3\2\2\2&\u00f3")
        buf.write("\3\2\2\2(\u00f5\3\2\2\2*\u00fe\3\2\2\2,\u010b\3\2\2\2")
        buf.write(".\u010e\3\2\2\2\60\u0112\3\2\2\2\62\u0115\3\2\2\2\64\u0119")
        buf.write("\3\2\2\2\66\u011c\3\2\2\28\u012e\3\2\2\2:\u013b\3\2\2")
        buf.write("\2<\u0140\3\2\2\2>\u0145\3\2\2\2@\u014d\3\2\2\2B\u015e")
        buf.write("\3\2\2\2D\u0161\3\2\2\2F\u0164\3\2\2\2H\u0167\3\2\2\2")
        buf.write("J\u016a\3\2\2\2L\u0176\3\2\2\2N\u0183\3\2\2\2P\u018c\3")
        buf.write("\2\2\2R\u018e\3\2\2\2T\u019b\3\2\2\2V\u01a8\3\2\2\2X\u01b2")
        buf.write("\3\2\2\2Z\u01b4\3\2\2\2\\\u01c1\3\2\2\2^\u01ce\3\2\2\2")
        buf.write("`\u01d1\3\2\2\2b\u01d4\3\2\2\2d\u01d7\3\2\2\2f\u01e8\3")
        buf.write("\2\2\2h\u01f5\3\2\2\2j\u01fa\3\2\2\2l\u01ff\3\2\2\2n\u0206")
        buf.write("\3\2\2\2p\u0216\3\2\2\2r\u0219\3\2\2\2t\u0222\3\2\2\2")
        buf.write("v\u022f\3\2\2\2x\u0238\3\2\2\2z\u023a\3\2\2\2|\u0247\3")
        buf.write("\2\2\2~\u0254\3\2\2\2\u0080\u0257\3\2\2\2\u0082\u026e")
        buf.write("\3\2\2\2\u0084\u027b\3\2\2\2\u0086\u0280\3\2\2\2\u0088")
        buf.write("\u0285\3\2\2\2\u008a\u0292\3\2\2\2\u008c\u02a8\3\2\2\2")
        buf.write("\u008e\u02ab\3\2\2\2\u0090\u02af\3\2\2\2\u0092\u02b1\3")
        buf.write("\2\2\2\u0094\u0096\5\f\7\2\u0095\u0094\3\2\2\2\u0096\u0099")
        buf.write("\3\2\2\2\u0097\u0095\3\2\2\2\u0097\u0098\3\2\2\2\u0098")
        buf.write("\u009c\3\2\2\2\u0099\u0097\3\2\2\2\u009a\u009c\5\4\3\2")
        buf.write("\u009b\u0097\3\2\2\2\u009b\u009a\3\2\2\2\u009c\u009e\3")
        buf.write("\2\2\2\u009d\u009f\5\n\6\2\u009e\u009d\3\2\2\2\u009e\u009f")
        buf.write("\3\2\2\2\u009f\u00a3\3\2\2\2\u00a0\u00a2\7\26\2\2\u00a1")
        buf.write("\u00a0\3\2\2\2\u00a2\u00a5\3\2\2\2\u00a3\u00a1\3\2\2\2")
        buf.write("\u00a3\u00a4\3\2\2\2\u00a4\u00a6\3\2\2\2\u00a5\u00a3\3")
        buf.write("\2\2\2\u00a6\u00a7\7\2\2\3\u00a7\3\3\2\2\2\u00a8\u00a9")
        buf.write("\5\64\33\2\u00a9\u00aa\5\16\b\2\u00aa\u00ab\5\26\f\2\u00ab")
        buf.write("\u00ac\58\35\2\u00ac\u00bd\3\2\2\2\u00ad\u00ae\5F$\2\u00ae")
        buf.write("\u00af\5\16\b\2\u00af\u00b0\5\26\f\2\u00b0\u00b1\5L\'")
        buf.write("\2\u00b1\u00bd\3\2\2\2\u00b2\u00b3\5~@\2\u00b3\u00b4\5")
        buf.write("\16\b\2\u00b4\u00b5\5\26\f\2\u00b5\u00b6\5\u0082B\2\u00b6")
        buf.write("\u00bd\3\2\2\2\u00b7\u00b8\5b\62\2\u00b8\u00b9\5\16\b")
        buf.write("\2\u00b9\u00ba\5\26\f\2\u00ba\u00bb\5f\64\2\u00bb\u00bd")
        buf.write("\3\2\2\2\u00bc\u00a8\3\2\2\2\u00bc\u00ad\3\2\2\2\u00bc")
        buf.write("\u00b2\3\2\2\2\u00bc\u00b7\3\2\2\2\u00bd\5\3\2\2\2\u00be")
        buf.write("\u00c2\7\3\2\2\u00bf\u00c3\7\25\2\2\u00c0\u00c3\5\b\5")
        buf.write("\2\u00c1\u00c3\7\24\2\2\u00c2\u00bf\3\2\2\2\u00c2\u00c0")
        buf.write("\3\2\2\2\u00c2\u00c1\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4")
        buf.write("\u00c2\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c6\3\2\2\2")
        buf.write("\u00c6\u00c7\7\3\2\2\u00c7\7\3\2\2\2\u00c8\u00c9\t\2\2")
        buf.write("\2\u00c9\t\3\2\2\2\u00ca\u00cb\7\4\2\2\u00cb\13\3\2\2")
        buf.write("\2\u00cc\u00cd\7\26\2\2\u00cd\r\3\2\2\2\u00ce\u00cf\7")
        buf.write("\16\2\2\u00cf\17\3\2\2\2\u00d0\u00d1\7\17\2\2\u00d1\21")
        buf.write("\3\2\2\2\u00d2\u00d3\7\20\2\2\u00d3\23\3\2\2\2\u00d4\u00d5")
        buf.write("\7\21\2\2\u00d5\25\3\2\2\2\u00d6\u00d7\7\22\2\2\u00d7")
        buf.write("\27\3\2\2\2\u00d8\u00d9\7\23\2\2\u00d9\31\3\2\2\2\u00da")
        buf.write("\u00dd\5\22\n\2\u00db\u00dd\5\24\13\2\u00dc\u00da\3\2")
        buf.write("\2\2\u00dc\u00db\3\2\2\2\u00dd\33\3\2\2\2\u00de\u00df")
        buf.write("\7\34\2\2\u00df\u00e0\5\36\20\2\u00e0\35\3\2\2\2\u00e1")
        buf.write("\u00e2\5\6\4\2\u00e2\u00e3\7\24\2\2\u00e3\37\3\2\2\2\u00e4")
        buf.write("\u00e5\7\35\2\2\u00e5\u00e6\5\"\22\2\u00e6!\3\2\2\2\u00e7")
        buf.write("\u00e8\5\6\4\2\u00e8\u00e9\7\24\2\2\u00e9#\3\2\2\2\u00ea")
        buf.write("\u00eb\7\36\2\2\u00eb\u00ec\5&\24\2\u00ec%\3\2\2\2\u00ed")
        buf.write("\u00ee\5\6\4\2\u00ee\u00f0\7\24\2\2\u00ef\u00f1\5(\25")
        buf.write("\2\u00f0\u00ef\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1\u00f4")
        buf.write("\3\2\2\2\u00f2\u00f4\5(\25\2\u00f3\u00ed\3\2\2\2\u00f3")
        buf.write("\u00f2\3\2\2\2\u00f4\'\3\2\2\2\u00f5\u00f6\5\30\r\2\u00f6")
        buf.write("\u00f7\5*\26\2\u00f7)\3\2\2\2\u00f8\u00f9\b\26\1\2\u00f9")
        buf.write("\u00fa\7\27\2\2\u00fa\u00fb\5*\26\2\u00fb\u00fc\7\30\2")
        buf.write("\2\u00fc\u00ff\3\2\2\2\u00fd\u00ff\5N(\2\u00fe\u00f8\3")
        buf.write("\2\2\2\u00fe\u00fd\3\2\2\2\u00ff\u0108\3\2\2\2\u0100\u0101")
        buf.write("\f\5\2\2\u0101\u0102\5\32\16\2\u0102\u0103\5*\26\6\u0103")
        buf.write("\u0107\3\2\2\2\u0104\u0105\f\3\2\2\u0105\u0107\7\24\2")
        buf.write("\2\u0106\u0100\3\2\2\2\u0106\u0104\3\2\2\2\u0107\u010a")
        buf.write("\3\2\2\2\u0108\u0106\3\2\2\2\u0108\u0109\3\2\2\2\u0109")
        buf.write("+\3\2\2\2\u010a\u0108\3\2\2\2\u010b\u010c\7\37\2\2\u010c")
        buf.write("\u010d\5.\30\2\u010d-\3\2\2\2\u010e\u010f\5\20\t\2\u010f")
        buf.write("\u0110\5\6\4\2\u0110\u0111\7\24\2\2\u0111/\3\2\2\2\u0112")
        buf.write("\u0113\7 \2\2\u0113\u0114\5\62\32\2\u0114\61\3\2\2\2\u0115")
        buf.write("\u0116\5\20\t\2\u0116\u0117\5\6\4\2\u0117\u0118\7\24\2")
        buf.write("\2\u0118\63\3\2\2\2\u0119\u011a\7!\2\2\u011a\u011b\5\66")
        buf.write("\34\2\u011b\65\3\2\2\2\u011c\u011d\5\30\r\2\u011d\u011e")
        buf.write("\58\35\2\u011e\67\3\2\2\2\u011f\u0120\b\35\1\2\u0120\u0121")
        buf.write("\7\27\2\2\u0121\u0122\58\35\2\u0122\u0123\7\30\2\2\u0123")
        buf.write("\u012f\3\2\2\2\u0124\u012d\5$\23\2\u0125\u012d\5B\"\2")
        buf.write("\u0126\u012d\5V,\2\u0127\u012d\5p9\2\u0128\u012d\5\u008c")
        buf.write("G\2\u0129\u012d\5<\37\2\u012a\u012d\5:\36\2\u012b\u012d")
        buf.write("\5> \2\u012c\u0124\3\2\2\2\u012c\u0125\3\2\2\2\u012c\u0126")
        buf.write("\3\2\2\2\u012c\u0127\3\2\2\2\u012c\u0128\3\2\2\2\u012c")
        buf.write("\u0129\3\2\2\2\u012c\u012a\3\2\2\2\u012c\u012b\3\2\2\2")
        buf.write("\u012d\u012f\3\2\2\2\u012e\u011f\3\2\2\2\u012e\u012c\3")
        buf.write("\2\2\2\u012f\u0138\3\2\2\2\u0130\u0131\f\5\2\2\u0131\u0132")
        buf.write("\5\32\16\2\u0132\u0133\58\35\6\u0133\u0137\3\2\2\2\u0134")
        buf.write("\u0135\f\3\2\2\u0135\u0137\7\24\2\2\u0136\u0130\3\2\2")
        buf.write("\2\u0136\u0134\3\2\2\2\u0137\u013a\3\2\2\2\u0138\u0136")
        buf.write("\3\2\2\2\u0138\u0139\3\2\2\2\u01399\3\2\2\2\u013a\u0138")
        buf.write("\3\2\2\2\u013b\u013c\7\31\2\2\u013c\u013d\7\27\2\2\u013d")
        buf.write("\u013e\5@!\2\u013e\u013f\7\30\2\2\u013f;\3\2\2\2\u0140")
        buf.write("\u0141\7\32\2\2\u0141\u0142\7\27\2\2\u0142\u0143\5@!\2")
        buf.write("\u0143\u0144\7\30\2\2\u0144=\3\2\2\2\u0145\u014b\7\33")
        buf.write("\2\2\u0146\u014c\5$\23\2\u0147\u014c\5B\"\2\u0148\u014c")
        buf.write("\5V,\2\u0149\u014c\5p9\2\u014a\u014c\5\u008cG\2\u014b")
        buf.write("\u0146\3\2\2\2\u014b\u0147\3\2\2\2\u014b\u0148\3\2\2\2")
        buf.write("\u014b\u0149\3\2\2\2\u014b\u014a\3\2\2\2\u014c?\3\2\2")
        buf.write("\2\u014d\u0153\b!\1\2\u014e\u0154\5$\23\2\u014f\u0154")
        buf.write("\5B\"\2\u0150\u0154\5V,\2\u0151\u0154\5p9\2\u0152\u0154")
        buf.write("\5\u008cG\2\u0153\u014e\3\2\2\2\u0153\u014f\3\2\2\2\u0153")
        buf.write("\u0150\3\2\2\2\u0153\u0151\3\2\2\2\u0153\u0152\3\2\2\2")
        buf.write("\u0154\u015b\3\2\2\2\u0155\u0156\f\4\2\2\u0156\u0157\5")
        buf.write("\24\13\2\u0157\u0158\5@!\5\u0158\u015a\3\2\2\2\u0159\u0155")
        buf.write("\3\2\2\2\u015a\u015d\3\2\2\2\u015b\u0159\3\2\2\2\u015b")
        buf.write("\u015c\3\2\2\2\u015cA\3\2\2\2\u015d\u015b\3\2\2\2\u015e")
        buf.write("\u015f\7\"\2\2\u015f\u0160\5D#\2\u0160C\3\2\2\2\u0161")
        buf.write("\u0162\5\6\4\2\u0162\u0163\7\24\2\2\u0163E\3\2\2\2\u0164")
        buf.write("\u0165\7#\2\2\u0165\u0166\5J&\2\u0166G\3\2\2\2\u0167\u0168")
        buf.write("\5\20\t\2\u0168\u0169\5~@\2\u0169I\3\2\2\2\u016a\u016b")
        buf.write("\5\30\r\2\u016b\u016c\5L\'\2\u016cK\3\2\2\2\u016d\u016e")
        buf.write("\b\'\1\2\u016e\u016f\7\27\2\2\u016f\u0170\5L\'\2\u0170")
        buf.write("\u0171\7\30\2\2\u0171\u0177\3\2\2\2\u0172\u0175\5$\23")
        buf.write("\2\u0173\u0175\5V,\2\u0174\u0172\3\2\2\2\u0174\u0173\3")
        buf.write("\2\2\2\u0175\u0177\3\2\2\2\u0176\u016d\3\2\2\2\u0176\u0174")
        buf.write("\3\2\2\2\u0177\u0180\3\2\2\2\u0178\u0179\f\5\2\2\u0179")
        buf.write("\u017a\5\32\16\2\u017a\u017b\5L\'\6\u017b\u017f\3\2\2")
        buf.write("\2\u017c\u017d\f\3\2\2\u017d\u017f\7\24\2\2\u017e\u0178")
        buf.write("\3\2\2\2\u017e\u017c\3\2\2\2\u017f\u0182\3\2\2\2\u0180")
        buf.write("\u017e\3\2\2\2\u0180\u0181\3\2\2\2\u0181M\3\2\2\2\u0182")
        buf.write("\u0180\3\2\2\2\u0183\u0184\7$\2\2\u0184\u0185\5P)\2\u0185")
        buf.write("O\3\2\2\2\u0186\u0187\5\6\4\2\u0187\u0189\7\24\2\2\u0188")
        buf.write("\u018a\5R*\2\u0189\u0188\3\2\2\2\u0189\u018a\3\2\2\2\u018a")
        buf.write("\u018d\3\2\2\2\u018b\u018d\5R*\2\u018c\u0186\3\2\2\2\u018c")
        buf.write("\u018b\3\2\2\2\u018dQ\3\2\2\2\u018e\u018f\5\30\r\2\u018f")
        buf.write("\u0190\5T+\2\u0190S\3\2\2\2\u0191\u0192\b+\1\2\u0192\u0193")
        buf.write("\7\27\2\2\u0193\u0194\5T+\2\u0194\u0195\7\30\2\2\u0195")
        buf.write("\u019c\3\2\2\2\u0196\u019a\5^\60\2\u0197\u019a\5\34\17")
        buf.write("\2\u0198\u019a\5 \21\2\u0199\u0196\3\2\2\2\u0199\u0197")
        buf.write("\3\2\2\2\u0199\u0198\3\2\2\2\u019a\u019c\3\2\2\2\u019b")
        buf.write("\u0191\3\2\2\2\u019b\u0199\3\2\2\2\u019c\u01a5\3\2\2\2")
        buf.write("\u019d\u019e\f\5\2\2\u019e\u019f\5\32\16\2\u019f\u01a0")
        buf.write("\5T+\6\u01a0\u01a4\3\2\2\2\u01a1\u01a2\f\3\2\2\u01a2\u01a4")
        buf.write("\7\24\2\2\u01a3\u019d\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a4")
        buf.write("\u01a7\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a5\u01a6\3\2\2\2")
        buf.write("\u01a6U\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a8\u01aa\7$\2\2")
        buf.write("\u01a9\u01ab\5X-\2\u01aa\u01a9\3\2\2\2\u01aa\u01ab\3\2")
        buf.write("\2\2\u01abW\3\2\2\2\u01ac\u01ad\5\6\4\2\u01ad\u01af\7")
        buf.write("\24\2\2\u01ae\u01b0\5Z.\2\u01af\u01ae\3\2\2\2\u01af\u01b0")
        buf.write("\3\2\2\2\u01b0\u01b3\3\2\2\2\u01b1\u01b3\5Z.\2\u01b2\u01ac")
        buf.write("\3\2\2\2\u01b2\u01b1\3\2\2\2\u01b3Y\3\2\2\2\u01b4\u01b5")
        buf.write("\5\30\r\2\u01b5\u01b6\5\\/\2\u01b6[\3\2\2\2\u01b7\u01b8")
        buf.write("\b/\1\2\u01b8\u01b9\7\27\2\2\u01b9\u01ba\5\\/\2\u01ba")
        buf.write("\u01bb\7\30\2\2\u01bb\u01c2\3\2\2\2\u01bc\u01c0\5^\60")
        buf.write("\2\u01bd\u01c0\5\34\17\2\u01be\u01c0\5$\23\2\u01bf\u01bc")
        buf.write("\3\2\2\2\u01bf\u01bd\3\2\2\2\u01bf\u01be\3\2\2\2\u01c0")
        buf.write("\u01c2\3\2\2\2\u01c1\u01b7\3\2\2\2\u01c1\u01bf\3\2\2\2")
        buf.write("\u01c2\u01cb\3\2\2\2\u01c3\u01c4\f\5\2\2\u01c4\u01c5\5")
        buf.write("\32\16\2\u01c5\u01c6\5\\/\6\u01c6\u01ca\3\2\2\2\u01c7")
        buf.write("\u01c8\f\3\2\2\u01c8\u01ca\7\24\2\2\u01c9\u01c3\3\2\2")
        buf.write("\2\u01c9\u01c7\3\2\2\2\u01ca\u01cd\3\2\2\2\u01cb\u01c9")
        buf.write("\3\2\2\2\u01cb\u01cc\3\2\2\2\u01cc]\3\2\2\2\u01cd\u01cb")
        buf.write("\3\2\2\2\u01ce\u01cf\7%\2\2\u01cf\u01d0\5`\61\2\u01d0")
        buf.write("_\3\2\2\2\u01d1\u01d2\5\6\4\2\u01d2\u01d3\7\24\2\2\u01d3")
        buf.write("a\3\2\2\2\u01d4\u01d5\7&\2\2\u01d5\u01d6\5d\63\2\u01d6")
        buf.write("c\3\2\2\2\u01d7\u01d8\5\30\r\2\u01d8\u01d9\5f\64\2\u01d9")
        buf.write("e\3\2\2\2\u01da\u01db\b\64\1\2\u01db\u01dc\7\27\2\2\u01dc")
        buf.write("\u01dd\5f\64\2\u01dd\u01de\7\30\2\2\u01de\u01e9\3\2\2")
        buf.write("\2\u01df\u01e7\5$\23\2\u01e0\u01e7\5^\60\2\u01e1\u01e7")
        buf.write("\5p9\2\u01e2\u01e7\5\u008cG\2\u01e3\u01e7\5h\65\2\u01e4")
        buf.write("\u01e7\5j\66\2\u01e5\u01e7\5l\67\2\u01e6\u01df\3\2\2\2")
        buf.write("\u01e6\u01e0\3\2\2\2\u01e6\u01e1\3\2\2\2\u01e6\u01e2\3")
        buf.write("\2\2\2\u01e6\u01e3\3\2\2\2\u01e6\u01e4\3\2\2\2\u01e6\u01e5")
        buf.write("\3\2\2\2\u01e7\u01e9\3\2\2\2\u01e8\u01da\3\2\2\2\u01e8")
        buf.write("\u01e6\3\2\2\2\u01e9\u01f2\3\2\2\2\u01ea\u01eb\f\5\2\2")
        buf.write("\u01eb\u01ec\5\32\16\2\u01ec\u01ed\5f\64\6\u01ed\u01f1")
        buf.write("\3\2\2\2\u01ee\u01ef\f\3\2\2\u01ef\u01f1\7\24\2\2\u01f0")
        buf.write("\u01ea\3\2\2\2\u01f0\u01ee\3\2\2\2\u01f1\u01f4\3\2\2\2")
        buf.write("\u01f2\u01f0\3\2\2\2\u01f2\u01f3\3\2\2\2\u01f3g\3\2\2")
        buf.write("\2\u01f4\u01f2\3\2\2\2\u01f5\u01f6\7\31\2\2\u01f6\u01f7")
        buf.write("\7\27\2\2\u01f7\u01f8\5n8\2\u01f8\u01f9\7\30\2\2\u01f9")
        buf.write("i\3\2\2\2\u01fa\u01fb\7\32\2\2\u01fb\u01fc\7\27\2\2\u01fc")
        buf.write("\u01fd\5n8\2\u01fd\u01fe\7\30\2\2\u01fek\3\2\2\2\u01ff")
        buf.write("\u0204\7\33\2\2\u0200\u0205\5$\23\2\u0201\u0205\5^\60")
        buf.write("\2\u0202\u0205\5p9\2\u0203\u0205\5\u008cG\2\u0204\u0200")
        buf.write("\3\2\2\2\u0204\u0201\3\2\2\2\u0204\u0202\3\2\2\2\u0204")
        buf.write("\u0203\3\2\2\2\u0205m\3\2\2\2\u0206\u020b\b8\1\2\u0207")
        buf.write("\u020c\5$\23\2\u0208\u020c\5^\60\2\u0209\u020c\5p9\2\u020a")
        buf.write("\u020c\5\u008cG\2\u020b\u0207\3\2\2\2\u020b\u0208\3\2")
        buf.write("\2\2\u020b\u0209\3\2\2\2\u020b\u020a\3\2\2\2\u020c\u0213")
        buf.write("\3\2\2\2\u020d\u020e\f\4\2\2\u020e\u020f\5\24\13\2\u020f")
        buf.write("\u0210\5n8\5\u0210\u0212\3\2\2\2\u0211\u020d\3\2\2\2\u0212")
        buf.write("\u0215\3\2\2\2\u0213\u0211\3\2\2\2\u0213\u0214\3\2\2\2")
        buf.write("\u0214o\3\2\2\2\u0215\u0213\3\2\2\2\u0216\u0217\7\'\2")
        buf.write("\2\u0217\u0218\5r:\2\u0218q\3\2\2\2\u0219\u021a\5\30\r")
        buf.write("\2\u021a\u021b\5t;\2\u021bs\3\2\2\2\u021c\u021d\b;\1\2")
        buf.write("\u021d\u021e\7\27\2\2\u021e\u021f\5t;\2\u021f\u0220\7")
        buf.write("\30\2\2\u0220\u0223\3\2\2\2\u0221\u0223\5v<\2\u0222\u021c")
        buf.write("\3\2\2\2\u0222\u0221\3\2\2\2\u0223\u022c\3\2\2\2\u0224")
        buf.write("\u0225\f\5\2\2\u0225\u0226\5\32\16\2\u0226\u0227\5t;\6")
        buf.write("\u0227\u022b\3\2\2\2\u0228\u0229\f\3\2\2\u0229\u022b\7")
        buf.write("\24\2\2\u022a\u0224\3\2\2\2\u022a\u0228\3\2\2\2\u022b")
        buf.write("\u022e\3\2\2\2\u022c\u022a\3\2\2\2\u022c\u022d\3\2\2\2")
        buf.write("\u022du\3\2\2\2\u022e\u022c\3\2\2\2\u022f\u0230\7(\2\2")
        buf.write("\u0230\u0231\5x=\2\u0231w\3\2\2\2\u0232\u0233\5\6\4\2")
        buf.write("\u0233\u0235\7\24\2\2\u0234\u0236\5z>\2\u0235\u0234\3")
        buf.write("\2\2\2\u0235\u0236\3\2\2\2\u0236\u0239\3\2\2\2\u0237\u0239")
        buf.write("\5z>\2\u0238\u0232\3\2\2\2\u0238\u0237\3\2\2\2\u0239y")
        buf.write("\3\2\2\2\u023a\u023b\5\30\r\2\u023b\u023c\5|?\2\u023c")
        buf.write("{\3\2\2\2\u023d\u023e\b?\1\2\u023e\u023f\7\27\2\2\u023f")
        buf.write("\u0240\5|?\2\u0240\u0241\7\30\2\2\u0241\u0248\3\2\2\2")
        buf.write("\u0242\u0246\5^\60\2\u0243\u0246\5\34\17\2\u0244\u0246")
        buf.write("\5 \21\2\u0245\u0242\3\2\2\2\u0245\u0243\3\2\2\2\u0245")
        buf.write("\u0244\3\2\2\2\u0246\u0248\3\2\2\2\u0247\u023d\3\2\2\2")
        buf.write("\u0247\u0245\3\2\2\2\u0248\u0251\3\2\2\2\u0249\u024a\f")
        buf.write("\5\2\2\u024a\u024b\5\32\16\2\u024b\u024c\5|?\6\u024c\u0250")
        buf.write("\3\2\2\2\u024d\u024e\f\3\2\2\u024e\u0250\7\24\2\2\u024f")
        buf.write("\u0249\3\2\2\2\u024f\u024d\3\2\2\2\u0250\u0253\3\2\2\2")
        buf.write("\u0251\u024f\3\2\2\2\u0251\u0252\3\2\2\2\u0252}\3\2\2")
        buf.write("\2\u0253\u0251\3\2\2\2\u0254\u0255\7)\2\2\u0255\u0256")
        buf.write("\5\u0080A\2\u0256\177\3\2\2\2\u0257\u0258\5\30\r\2\u0258")
        buf.write("\u0259\5\u0082B\2\u0259\u0081\3\2\2\2\u025a\u025b\bB\1")
        buf.write("\2\u025b\u025c\7\27\2\2\u025c\u025d\5\u0082B\2\u025d\u025e")
        buf.write("\7\30\2\2\u025e\u026f\3\2\2\2\u025f\u026d\5$\23\2\u0260")
        buf.write("\u026d\5,\27\2\u0261\u026d\5\60\31\2\u0262\u026d\5\64")
        buf.write("\33\2\u0263\u026d\5F$\2\u0264\u026d\5b\62\2\u0265\u026d")
        buf.write("\5p9\2\u0266\u026d\5\u0090I\2\u0267\u026d\5\u0092J\2\u0268")
        buf.write("\u026d\5\u008eH\2\u0269\u026d\5\u0084C\2\u026a\u026d\5")
        buf.write("\u0086D\2\u026b\u026d\5\u0088E\2\u026c\u025f\3\2\2\2\u026c")
        buf.write("\u0260\3\2\2\2\u026c\u0261\3\2\2\2\u026c\u0262\3\2\2\2")
        buf.write("\u026c\u0263\3\2\2\2\u026c\u0264\3\2\2\2\u026c\u0265\3")
        buf.write("\2\2\2\u026c\u0266\3\2\2\2\u026c\u0267\3\2\2\2\u026c\u0268")
        buf.write("\3\2\2\2\u026c\u0269\3\2\2\2\u026c\u026a\3\2\2\2\u026c")
        buf.write("\u026b\3\2\2\2\u026d\u026f\3\2\2\2\u026e\u025a\3\2\2\2")
        buf.write("\u026e\u026c\3\2\2\2\u026f\u0278\3\2\2\2\u0270\u0271\f")
        buf.write("\5\2\2\u0271\u0272\5\32\16\2\u0272\u0273\5\u0082B\6\u0273")
        buf.write("\u0277\3\2\2\2\u0274\u0275\f\3\2\2\u0275\u0277\7\24\2")
        buf.write("\2\u0276\u0270\3\2\2\2\u0276\u0274\3\2\2\2\u0277\u027a")
        buf.write("\3\2\2\2\u0278\u0276\3\2\2\2\u0278\u0279\3\2\2\2\u0279")
        buf.write("\u0083\3\2\2\2\u027a\u0278\3\2\2\2\u027b\u027c\7\31\2")
        buf.write("\2\u027c\u027d\7\27\2\2\u027d\u027e\5\u008aF\2\u027e\u027f")
        buf.write("\7\30\2\2\u027f\u0085\3\2\2\2\u0280\u0281\7\32\2\2\u0281")
        buf.write("\u0282\7\27\2\2\u0282\u0283\5\u008aF\2\u0283\u0284\7\30")
        buf.write("\2\2\u0284\u0087\3\2\2\2\u0285\u0290\7\33\2\2\u0286\u0291")
        buf.write("\5$\23\2\u0287\u0291\5,\27\2\u0288\u0291\5\60\31\2\u0289")
        buf.write("\u0291\5\64\33\2\u028a\u0291\5F$\2\u028b\u0291\5b\62\2")
        buf.write("\u028c\u0291\5p9\2\u028d\u0291\5\u0090I\2\u028e\u0291")
        buf.write("\5\u0092J\2\u028f\u0291\5\u008eH\2\u0290\u0286\3\2\2\2")
        buf.write("\u0290\u0287\3\2\2\2\u0290\u0288\3\2\2\2\u0290\u0289\3")
        buf.write("\2\2\2\u0290\u028a\3\2\2\2\u0290\u028b\3\2\2\2\u0290\u028c")
        buf.write("\3\2\2\2\u0290\u028d\3\2\2\2\u0290\u028e\3\2\2\2\u0290")
        buf.write("\u028f\3\2\2\2\u0291\u0089\3\2\2\2\u0292\u029d\bF\1\2")
        buf.write("\u0293\u029e\5$\23\2\u0294\u029e\5,\27\2\u0295\u029e\5")
        buf.write("\60\31\2\u0296\u029e\5\64\33\2\u0297\u029e\5F$\2\u0298")
        buf.write("\u029e\5b\62\2\u0299\u029e\5p9\2\u029a\u029e\5\u0090I")
        buf.write("\2\u029b\u029e\5\u0092J\2\u029c\u029e\5\u008eH\2\u029d")
        buf.write("\u0293\3\2\2\2\u029d\u0294\3\2\2\2\u029d\u0295\3\2\2\2")
        buf.write("\u029d\u0296\3\2\2\2\u029d\u0297\3\2\2\2\u029d\u0298\3")
        buf.write("\2\2\2\u029d\u0299\3\2\2\2\u029d\u029a\3\2\2\2\u029d\u029b")
        buf.write("\3\2\2\2\u029d\u029c\3\2\2\2\u029e\u02a5\3\2\2\2\u029f")
        buf.write("\u02a0\f\4\2\2\u02a0\u02a1\5\24\13\2\u02a1\u02a2\5\u008a")
        buf.write("F\5\u02a2\u02a4\3\2\2\2\u02a3\u029f\3\2\2\2\u02a4\u02a7")
        buf.write("\3\2\2\2\u02a5\u02a3\3\2\2\2\u02a5\u02a6\3\2\2\2\u02a6")
        buf.write("\u008b\3\2\2\2\u02a7\u02a5\3\2\2\2\u02a8\u02a9\7*\2\2")
        buf.write("\u02a9\u02aa\5\u0080A\2\u02aa\u008d\3\2\2\2\u02ab\u02ac")
        buf.write("\7+\2\2\u02ac\u02ad\5\6\4\2\u02ad\u02ae\7\24\2\2\u02ae")
        buf.write("\u008f\3\2\2\2\u02af\u02b0\7,\2\2\u02b0\u0091\3\2\2\2")
        buf.write("\u02b1\u02b2\7-\2\2\u02b2\u0093\3\2\2\2>\u0097\u009b\u009e")
        buf.write("\u00a3\u00bc\u00c2\u00c4\u00dc\u00f0\u00f3\u00fe\u0106")
        buf.write("\u0108\u012c\u012e\u0136\u0138\u014b\u0153\u015b\u0174")
        buf.write("\u0176\u017e\u0180\u0189\u018c\u0199\u019b\u01a3\u01a5")
        buf.write("\u01aa\u01af\u01b2\u01bf\u01c1\u01c9\u01cb\u01e6\u01e8")
        buf.write("\u01f0\u01f2\u0204\u020b\u0213\u0222\u022a\u022c\u0235")
        buf.write("\u0238\u0245\u0247\u024f\u0251\u026c\u026e\u0276\u0278")
        buf.write("\u0290\u029d\u02a5")
        return buf.getvalue()


class RulepadGrammarParser ( Parser ):

    grammarFileName = "RulepadGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\"'", "'.'", "'='", "'>'", "'<'", "'''", 
                     "'&'", "'|'", "'['", "']'", "','", "'must '", "'of '", 
                     "'and '", "'or '", "'have '", "'with '", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'('", "')'", "'one of '", 
                     "'none of '", "'no '", "'name '", "'value '", "'annotation '", 
                     "'extension '", "'implementation '", "<INVALID>", "'return type '", 
                     "'constructor '", "'parameter '", "'type '", "<INVALID>", 
                     "'configuration file '", "'property '", "'class '", 
                     "'enclosing class '", "'overridden method '", "'bean declaration '", 
                     "'beans file'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "SPACE", "Alphabet", "NL", 
                      "LPAREN", "RPAREN", "ONE_OF", "NONE_OF", "NO", "NAME", 
                      "VALUE", "ANNOTATION", "EXTENSION", "IMPLEMENTATION", 
                      "FUNCTION", "RETURN_TYPES", "CONSTRUCTOR", "PARAMETER", 
                      "TYPES", "DeclarationStatement", "ConfigurationFile", 
                      "CONFIGURATION_PROPERTIES", "CLASSES", "ENCLOSING_CLASS", 
                      "OVERRIDDEN_FUNCTION", "BEAN_DECL", "BEANS_FILE" ]

    RULE_start = 0
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
    RULE_functionExpressionOneOf = 28
    RULE_functionExpressionNoneOf = 29
    RULE_functionExpressionNo = 30
    RULE_functionExpressionAggregateContents = 31
    RULE_returnTypes = 32
    RULE_returnTypeCondition = 33
    RULE_constructors = 34
    RULE_constructorOf = 35
    RULE_constructorCondition = 36
    RULE_constructorExpression = 37
    RULE_annotationParameters = 38
    RULE_annotationParameterCondition = 39
    RULE_annotationParameterConditionTransition = 40
    RULE_annotationParameterExpression = 41
    RULE_functionParameters = 42
    RULE_functionParameterCondition = 43
    RULE_functionParameterConditionTransition = 44
    RULE_functionParameterExpression = 45
    RULE_types = 46
    RULE_typeCondition = 47
    RULE_declarationStatements = 48
    RULE_declarationStatementCondition = 49
    RULE_declarationStatementExpression = 50
    RULE_declarationStatementExpressionOneOf = 51
    RULE_declarationStatementExpressionNoneOf = 52
    RULE_declarationStatementExpressionNo = 53
    RULE_declarationStatementExpressionAggregateContents = 54
    RULE_configurationFiles = 55
    RULE_configurationFileCondition = 56
    RULE_configurationFileExpression = 57
    RULE_configurationProperties = 58
    RULE_configurationPropertyCondition = 59
    RULE_configurationPropertyConditionTransition = 60
    RULE_configurationPropertyExpression = 61
    RULE_classes = 62
    RULE_classCondition = 63
    RULE_classExpression = 64
    RULE_classExpressionOneOf = 65
    RULE_classExpressionNoneOf = 66
    RULE_classExpressionNo = 67
    RULE_classExpressionAggregateContents = 68
    RULE_enclosingClass = 69
    RULE_overriddenFunctions = 70
    RULE_beans = 71
    RULE_beansFile = 72

    ruleNames =  [ "start", "mustClause", "combinatorialWords", "symbols", 
                   "end", "emptyLine", "must", "of", "and_", "or_", "have", 
                   "withWord", "binary", "names", "nameCondition", "values", 
                   "valueCondition", "annotations", "annotationCondition", 
                   "annotationConditionTransition", "annotationExpression", 
                   "extensions", "extensionCondition", "implementations", 
                   "implementationCondition", "functions", "functionCondition", 
                   "functionExpression", "functionExpressionOneOf", "functionExpressionNoneOf", 
                   "functionExpressionNo", "functionExpressionAggregateContents", 
                   "returnTypes", "returnTypeCondition", "constructors", 
                   "constructorOf", "constructorCondition", "constructorExpression", 
                   "annotationParameters", "annotationParameterCondition", 
                   "annotationParameterConditionTransition", "annotationParameterExpression", 
                   "functionParameters", "functionParameterCondition", "functionParameterConditionTransition", 
                   "functionParameterExpression", "types", "typeCondition", 
                   "declarationStatements", "declarationStatementCondition", 
                   "declarationStatementExpression", "declarationStatementExpressionOneOf", 
                   "declarationStatementExpressionNoneOf", "declarationStatementExpressionNo", 
                   "declarationStatementExpressionAggregateContents", "configurationFiles", 
                   "configurationFileCondition", "configurationFileExpression", 
                   "configurationProperties", "configurationPropertyCondition", 
                   "configurationPropertyConditionTransition", "configurationPropertyExpression", 
                   "classes", "classCondition", "classExpression", "classExpressionOneOf", 
                   "classExpressionNoneOf", "classExpressionNo", "classExpressionAggregateContents", 
                   "enclosingClass", "overriddenFunctions", "beans", "beansFile" ]

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
    T__16=17
    SPACE=18
    Alphabet=19
    NL=20
    LPAREN=21
    RPAREN=22
    ONE_OF=23
    NONE_OF=24
    NO=25
    NAME=26
    VALUE=27
    ANNOTATION=28
    EXTENSION=29
    IMPLEMENTATION=30
    FUNCTION=31
    RETURN_TYPES=32
    CONSTRUCTOR=33
    PARAMETER=34
    TYPES=35
    DeclarationStatement=36
    ConfigurationFile=37
    CONFIGURATION_PROPERTIES=38
    CLASSES=39
    ENCLOSING_CLASS=40
    OVERRIDDEN_FUNCTION=41
    BEAN_DECL=42
    BEANS_FILE=43

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):

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
            return RulepadGrammarParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = RulepadGrammarParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.EOF, RulepadGrammarParser.T__1, RulepadGrammarParser.NL]:
                self.state = 149
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 146
                        self.emptyLine() 
                    self.state = 151
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

                pass
            elif token in [RulepadGrammarParser.FUNCTION, RulepadGrammarParser.CONSTRUCTOR, RulepadGrammarParser.DeclarationStatement, RulepadGrammarParser.CLASSES]:
                self.state = 152
                self.mustClause()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RulepadGrammarParser.T__1:
                self.state = 155
                self.end()


            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RulepadGrammarParser.NL:
                self.state = 158
                self.match(RulepadGrammarParser.NL)
                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 164
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
            self.state = 186
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.FUNCTION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.functions()
                self.state = 167
                self.must()
                self.state = 168
                self.have()
                self.state = 169
                self.functionExpression(0)
                pass
            elif token in [RulepadGrammarParser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 171
                self.constructors()
                self.state = 172
                self.must()
                self.state = 173
                self.have()
                self.state = 174
                self.constructorExpression(0)
                pass
            elif token in [RulepadGrammarParser.CLASSES]:
                self.enterOuterAlt(localctx, 3)
                self.state = 176
                self.classes()
                self.state = 177
                self.must()
                self.state = 178
                self.have()
                self.state = 179
                self.classExpression(0)
                pass
            elif token in [RulepadGrammarParser.DeclarationStatement]:
                self.enterOuterAlt(localctx, 4)
                self.state = 181
                self.declarationStatements()
                self.state = 182
                self.must()
                self.state = 183
                self.have()
                self.state = 184
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
            self.state = 188
            self.match(RulepadGrammarParser.T__0)
            self.state = 192 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 192
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.Alphabet]:
                    self.state = 189
                    self.match(RulepadGrammarParser.Alphabet)
                    pass
                elif token in [RulepadGrammarParser.T__1, RulepadGrammarParser.T__2, RulepadGrammarParser.T__3, RulepadGrammarParser.T__4, RulepadGrammarParser.T__5, RulepadGrammarParser.T__6, RulepadGrammarParser.T__7, RulepadGrammarParser.T__8, RulepadGrammarParser.T__9, RulepadGrammarParser.T__10, RulepadGrammarParser.LPAREN, RulepadGrammarParser.RPAREN]:
                    self.state = 190
                    self.symbols()
                    pass
                elif token in [RulepadGrammarParser.SPACE]:
                    self.state = 191
                    self.match(RulepadGrammarParser.SPACE)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 194 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RulepadGrammarParser.T__1) | (1 << RulepadGrammarParser.T__2) | (1 << RulepadGrammarParser.T__3) | (1 << RulepadGrammarParser.T__4) | (1 << RulepadGrammarParser.T__5) | (1 << RulepadGrammarParser.T__6) | (1 << RulepadGrammarParser.T__7) | (1 << RulepadGrammarParser.T__8) | (1 << RulepadGrammarParser.T__9) | (1 << RulepadGrammarParser.T__10) | (1 << RulepadGrammarParser.SPACE) | (1 << RulepadGrammarParser.Alphabet) | (1 << RulepadGrammarParser.LPAREN) | (1 << RulepadGrammarParser.RPAREN))) != 0)):
                    break

            self.state = 196
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
            self.state = 198
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RulepadGrammarParser.T__1) | (1 << RulepadGrammarParser.T__2) | (1 << RulepadGrammarParser.T__3) | (1 << RulepadGrammarParser.T__4) | (1 << RulepadGrammarParser.T__5) | (1 << RulepadGrammarParser.T__6) | (1 << RulepadGrammarParser.T__7) | (1 << RulepadGrammarParser.T__8) | (1 << RulepadGrammarParser.T__9) | (1 << RulepadGrammarParser.T__10) | (1 << RulepadGrammarParser.LPAREN) | (1 << RulepadGrammarParser.RPAREN))) != 0)):
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
            self.state = 200
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
            self.state = 202
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
            self.state = 204
            self.match(RulepadGrammarParser.T__11)
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
            self.state = 206
            self.match(RulepadGrammarParser.T__12)
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
            self.state = 208
            self.match(RulepadGrammarParser.T__13)
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
            self.state = 210
            self.match(RulepadGrammarParser.T__14)
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
            self.state = 212
            self.match(RulepadGrammarParser.T__15)
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
            self.state = 214
            self.match(RulepadGrammarParser.T__16)
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
            self.state = 218
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.T__13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.and_()
                pass
            elif token in [RulepadGrammarParser.T__14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 217
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
            self.state = 220
            self.match(RulepadGrammarParser.NAME)
            self.state = 221
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
            self.state = 223
            self.combinatorialWords()
            self.state = 224
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
            self.state = 226
            self.match(RulepadGrammarParser.VALUE)
            self.state = 227
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
            self.state = 229
            self.combinatorialWords()
            self.state = 230
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
            self.state = 232
            self.match(RulepadGrammarParser.ANNOTATION)
            self.state = 233
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
            self.state = 241
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.combinatorialWords()
                self.state = 236
                self.match(RulepadGrammarParser.SPACE)
                self.state = 238
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 237
                    self.annotationConditionTransition()


                pass
            elif token in [RulepadGrammarParser.T__16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 240
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
            self.state = 243
            self.withWord()
            self.state = 244
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

        def annotationParameters(self):
            return self.getTypedRuleContext(RulepadGrammarParser.AnnotationParametersContext,0)


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
            self.state = 252
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 247
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 248
                self.annotationExpression(0)
                self.state = 249
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.PARAMETER]:
                self.state = 251
                self.annotationParameters()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 262
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 260
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.AnnotationExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_annotationExpression)
                        self.state = 254
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 255
                        localctx.op = self.binary()
                        self.state = 256
                        localctx.right = self.annotationExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.AnnotationExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_annotationExpression)
                        self.state = 258
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 259
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 264
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
            self.state = 265
            self.match(RulepadGrammarParser.EXTENSION)
            self.state = 266
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
            self.state = 268
            self.of()
            self.state = 269
            self.combinatorialWords()
            self.state = 270
            self.match(RulepadGrammarParser.SPACE)
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
            self.state = 272
            self.match(RulepadGrammarParser.IMPLEMENTATION)
            self.state = 273
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
            self.state = 275
            self.of()
            self.state = 276
            self.combinatorialWords()
            self.state = 277
            self.match(RulepadGrammarParser.SPACE)
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
            self.state = 279
            self.match(RulepadGrammarParser.FUNCTION)
            self.state = 280
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
            self.state = 282
            self.withWord()
            self.state = 283
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


        def returnTypes(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ReturnTypesContext,0)


        def functionParameters(self):
            return self.getTypedRuleContext(RulepadGrammarParser.FunctionParametersContext,0)


        def configurationFiles(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ConfigurationFilesContext,0)


        def enclosingClass(self):
            return self.getTypedRuleContext(RulepadGrammarParser.EnclosingClassContext,0)


        def functionExpressionNoneOf(self):
            return self.getTypedRuleContext(RulepadGrammarParser.FunctionExpressionNoneOfContext,0)


        def functionExpressionOneOf(self):
            return self.getTypedRuleContext(RulepadGrammarParser.FunctionExpressionOneOfContext,0)


        def functionExpressionNo(self):
            return self.getTypedRuleContext(RulepadGrammarParser.FunctionExpressionNoContext,0)


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
            self.state = 300
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 286
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 287
                self.functionExpression(0)
                self.state = 288
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.ONE_OF, RulepadGrammarParser.NONE_OF, RulepadGrammarParser.NO, RulepadGrammarParser.ANNOTATION, RulepadGrammarParser.RETURN_TYPES, RulepadGrammarParser.PARAMETER, RulepadGrammarParser.ConfigurationFile, RulepadGrammarParser.ENCLOSING_CLASS]:
                self.state = 298
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.ANNOTATION]:
                    self.state = 290
                    self.annotations()
                    pass
                elif token in [RulepadGrammarParser.RETURN_TYPES]:
                    self.state = 291
                    self.returnTypes()
                    pass
                elif token in [RulepadGrammarParser.PARAMETER]:
                    self.state = 292
                    self.functionParameters()
                    pass
                elif token in [RulepadGrammarParser.ConfigurationFile]:
                    self.state = 293
                    self.configurationFiles()
                    pass
                elif token in [RulepadGrammarParser.ENCLOSING_CLASS]:
                    self.state = 294
                    self.enclosingClass()
                    pass
                elif token in [RulepadGrammarParser.NONE_OF]:
                    self.state = 295
                    self.functionExpressionNoneOf()
                    pass
                elif token in [RulepadGrammarParser.ONE_OF]:
                    self.state = 296
                    self.functionExpressionOneOf()
                    pass
                elif token in [RulepadGrammarParser.NO]:
                    self.state = 297
                    self.functionExpressionNo()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 310
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 308
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.FunctionExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_functionExpression)
                        self.state = 302
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 303
                        localctx.op = self.binary()
                        self.state = 304
                        localctx.right = self.functionExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.FunctionExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_functionExpression)
                        self.state = 306
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 307
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 312
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FunctionExpressionOneOfContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ONE_OF(self):
            return self.getToken(RulepadGrammarParser.ONE_OF, 0)

        def LPAREN(self):
            return self.getToken(RulepadGrammarParser.LPAREN, 0)

        def functionExpressionAggregateContents(self):
            return self.getTypedRuleContext(RulepadGrammarParser.FunctionExpressionAggregateContentsContext,0)


        def RPAREN(self):
            return self.getToken(RulepadGrammarParser.RPAREN, 0)

        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_functionExpressionOneOf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionExpressionOneOf" ):
                listener.enterFunctionExpressionOneOf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionExpressionOneOf" ):
                listener.exitFunctionExpressionOneOf(self)




    def functionExpressionOneOf(self):

        localctx = RulepadGrammarParser.FunctionExpressionOneOfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_functionExpressionOneOf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.match(RulepadGrammarParser.ONE_OF)
            self.state = 314
            self.match(RulepadGrammarParser.LPAREN)
            self.state = 315
            self.functionExpressionAggregateContents(0)
            self.state = 316
            self.match(RulepadGrammarParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionExpressionNoneOfContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NONE_OF(self):
            return self.getToken(RulepadGrammarParser.NONE_OF, 0)

        def LPAREN(self):
            return self.getToken(RulepadGrammarParser.LPAREN, 0)

        def functionExpressionAggregateContents(self):
            return self.getTypedRuleContext(RulepadGrammarParser.FunctionExpressionAggregateContentsContext,0)


        def RPAREN(self):
            return self.getToken(RulepadGrammarParser.RPAREN, 0)

        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_functionExpressionNoneOf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionExpressionNoneOf" ):
                listener.enterFunctionExpressionNoneOf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionExpressionNoneOf" ):
                listener.exitFunctionExpressionNoneOf(self)




    def functionExpressionNoneOf(self):

        localctx = RulepadGrammarParser.FunctionExpressionNoneOfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_functionExpressionNoneOf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.match(RulepadGrammarParser.NONE_OF)
            self.state = 319
            self.match(RulepadGrammarParser.LPAREN)
            self.state = 320
            self.functionExpressionAggregateContents(0)
            self.state = 321
            self.match(RulepadGrammarParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionExpressionNoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NO(self):
            return self.getToken(RulepadGrammarParser.NO, 0)

        def annotations(self):
            return self.getTypedRuleContext(RulepadGrammarParser.AnnotationsContext,0)


        def returnTypes(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ReturnTypesContext,0)


        def functionParameters(self):
            return self.getTypedRuleContext(RulepadGrammarParser.FunctionParametersContext,0)


        def configurationFiles(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ConfigurationFilesContext,0)


        def enclosingClass(self):
            return self.getTypedRuleContext(RulepadGrammarParser.EnclosingClassContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_functionExpressionNo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionExpressionNo" ):
                listener.enterFunctionExpressionNo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionExpressionNo" ):
                listener.exitFunctionExpressionNo(self)




    def functionExpressionNo(self):

        localctx = RulepadGrammarParser.FunctionExpressionNoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_functionExpressionNo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.match(RulepadGrammarParser.NO)
            self.state = 329
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.ANNOTATION]:
                self.state = 324
                self.annotations()
                pass
            elif token in [RulepadGrammarParser.RETURN_TYPES]:
                self.state = 325
                self.returnTypes()
                pass
            elif token in [RulepadGrammarParser.PARAMETER]:
                self.state = 326
                self.functionParameters()
                pass
            elif token in [RulepadGrammarParser.ConfigurationFile]:
                self.state = 327
                self.configurationFiles()
                pass
            elif token in [RulepadGrammarParser.ENCLOSING_CLASS]:
                self.state = 328
                self.enclosingClass()
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


    class FunctionExpressionAggregateContentsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # FunctionExpressionAggregateContentsContext
            self.op = None # Or_Context
            self.right = None # FunctionExpressionAggregateContentsContext

        def annotations(self):
            return self.getTypedRuleContext(RulepadGrammarParser.AnnotationsContext,0)


        def returnTypes(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ReturnTypesContext,0)


        def functionParameters(self):
            return self.getTypedRuleContext(RulepadGrammarParser.FunctionParametersContext,0)


        def configurationFiles(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ConfigurationFilesContext,0)


        def enclosingClass(self):
            return self.getTypedRuleContext(RulepadGrammarParser.EnclosingClassContext,0)


        def functionExpressionAggregateContents(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RulepadGrammarParser.FunctionExpressionAggregateContentsContext)
            else:
                return self.getTypedRuleContext(RulepadGrammarParser.FunctionExpressionAggregateContentsContext,i)


        def or_(self):
            return self.getTypedRuleContext(RulepadGrammarParser.Or_Context,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_functionExpressionAggregateContents

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionExpressionAggregateContents" ):
                listener.enterFunctionExpressionAggregateContents(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionExpressionAggregateContents" ):
                listener.exitFunctionExpressionAggregateContents(self)



    def functionExpressionAggregateContents(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RulepadGrammarParser.FunctionExpressionAggregateContentsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_functionExpressionAggregateContents, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.ANNOTATION]:
                self.state = 332
                self.annotations()
                pass
            elif token in [RulepadGrammarParser.RETURN_TYPES]:
                self.state = 333
                self.returnTypes()
                pass
            elif token in [RulepadGrammarParser.PARAMETER]:
                self.state = 334
                self.functionParameters()
                pass
            elif token in [RulepadGrammarParser.ConfigurationFile]:
                self.state = 335
                self.configurationFiles()
                pass
            elif token in [RulepadGrammarParser.ENCLOSING_CLASS]:
                self.state = 336
                self.enclosingClass()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 345
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = RulepadGrammarParser.FunctionExpressionAggregateContentsContext(self, _parentctx, _parentState)
                    localctx.left = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_functionExpressionAggregateContents)
                    self.state = 339
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 340
                    localctx.op = self.or_()
                    self.state = 341
                    localctx.right = self.functionExpressionAggregateContents(3) 
                self.state = 347
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ReturnTypesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN_TYPES(self):
            return self.getToken(RulepadGrammarParser.RETURN_TYPES, 0)

        def returnTypeCondition(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ReturnTypeConditionContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_returnTypes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnTypes" ):
                listener.enterReturnTypes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnTypes" ):
                listener.exitReturnTypes(self)




    def returnTypes(self):

        localctx = RulepadGrammarParser.ReturnTypesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_returnTypes)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.match(RulepadGrammarParser.RETURN_TYPES)
            self.state = 349
            self.returnTypeCondition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnTypeConditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def combinatorialWords(self):
            return self.getTypedRuleContext(RulepadGrammarParser.CombinatorialWordsContext,0)


        def SPACE(self):
            return self.getToken(RulepadGrammarParser.SPACE, 0)

        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_returnTypeCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnTypeCondition" ):
                listener.enterReturnTypeCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnTypeCondition" ):
                listener.exitReturnTypeCondition(self)




    def returnTypeCondition(self):

        localctx = RulepadGrammarParser.ReturnTypeConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_returnTypeCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.combinatorialWords()
            self.state = 352
            self.match(RulepadGrammarParser.SPACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
        self.enterRule(localctx, 68, self.RULE_constructors)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.match(RulepadGrammarParser.CONSTRUCTOR)
            self.state = 355
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
        self.enterRule(localctx, 70, self.RULE_constructorOf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.of()
            self.state = 358
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
        self.enterRule(localctx, 72, self.RULE_constructorCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.withWord()
            self.state = 361
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
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_constructorExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 364
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 365
                self.constructorExpression(0)
                self.state = 366
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.ANNOTATION, RulepadGrammarParser.PARAMETER]:
                self.state = 370
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.ANNOTATION]:
                    self.state = 368
                    self.annotations()
                    pass
                elif token in [RulepadGrammarParser.PARAMETER]:
                    self.state = 369
                    self.functionParameters()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 382
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 380
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.ConstructorExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_constructorExpression)
                        self.state = 374
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 375
                        localctx.op = self.binary()
                        self.state = 376
                        localctx.right = self.constructorExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.ConstructorExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_constructorExpression)
                        self.state = 378
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 379
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 384
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AnnotationParametersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARAMETER(self):
            return self.getToken(RulepadGrammarParser.PARAMETER, 0)

        def annotationParameterCondition(self):
            return self.getTypedRuleContext(RulepadGrammarParser.AnnotationParameterConditionContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_annotationParameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnnotationParameters" ):
                listener.enterAnnotationParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnnotationParameters" ):
                listener.exitAnnotationParameters(self)




    def annotationParameters(self):

        localctx = RulepadGrammarParser.AnnotationParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_annotationParameters)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.match(RulepadGrammarParser.PARAMETER)
            self.state = 386
            self.annotationParameterCondition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AnnotationParameterConditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def combinatorialWords(self):
            return self.getTypedRuleContext(RulepadGrammarParser.CombinatorialWordsContext,0)


        def SPACE(self):
            return self.getToken(RulepadGrammarParser.SPACE, 0)

        def annotationParameterConditionTransition(self):
            return self.getTypedRuleContext(RulepadGrammarParser.AnnotationParameterConditionTransitionContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_annotationParameterCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnnotationParameterCondition" ):
                listener.enterAnnotationParameterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnnotationParameterCondition" ):
                listener.exitAnnotationParameterCondition(self)




    def annotationParameterCondition(self):

        localctx = RulepadGrammarParser.AnnotationParameterConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_annotationParameterCondition)
        try:
            self.state = 394
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 388
                self.combinatorialWords()
                self.state = 389
                self.match(RulepadGrammarParser.SPACE)
                self.state = 391
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                if la_ == 1:
                    self.state = 390
                    self.annotationParameterConditionTransition()


                pass
            elif token in [RulepadGrammarParser.T__16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 393
                self.annotationParameterConditionTransition()
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


    class AnnotationParameterConditionTransitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def withWord(self):
            return self.getTypedRuleContext(RulepadGrammarParser.WithWordContext,0)


        def annotationParameterExpression(self):
            return self.getTypedRuleContext(RulepadGrammarParser.AnnotationParameterExpressionContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_annotationParameterConditionTransition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnnotationParameterConditionTransition" ):
                listener.enterAnnotationParameterConditionTransition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnnotationParameterConditionTransition" ):
                listener.exitAnnotationParameterConditionTransition(self)




    def annotationParameterConditionTransition(self):

        localctx = RulepadGrammarParser.AnnotationParameterConditionTransitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_annotationParameterConditionTransition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            self.withWord()
            self.state = 397
            self.annotationParameterExpression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AnnotationParameterExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # AnnotationParameterExpressionContext
            self.op = None # BinaryContext
            self.right = None # AnnotationParameterExpressionContext

        def LPAREN(self):
            return self.getToken(RulepadGrammarParser.LPAREN, 0)

        def annotationParameterExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RulepadGrammarParser.AnnotationParameterExpressionContext)
            else:
                return self.getTypedRuleContext(RulepadGrammarParser.AnnotationParameterExpressionContext,i)


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
            return RulepadGrammarParser.RULE_annotationParameterExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnnotationParameterExpression" ):
                listener.enterAnnotationParameterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnnotationParameterExpression" ):
                listener.exitAnnotationParameterExpression(self)



    def annotationParameterExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RulepadGrammarParser.AnnotationParameterExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_annotationParameterExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 400
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 401
                self.annotationParameterExpression(0)
                self.state = 402
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.NAME, RulepadGrammarParser.VALUE, RulepadGrammarParser.TYPES]:
                self.state = 407
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.TYPES]:
                    self.state = 404
                    self.types()
                    pass
                elif token in [RulepadGrammarParser.NAME]:
                    self.state = 405
                    self.names()
                    pass
                elif token in [RulepadGrammarParser.VALUE]:
                    self.state = 406
                    self.values()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 419
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 417
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.AnnotationParameterExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_annotationParameterExpression)
                        self.state = 411
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 412
                        localctx.op = self.binary()
                        self.state = 413
                        localctx.right = self.annotationParameterExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.AnnotationParameterExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_annotationParameterExpression)
                        self.state = 415
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 416
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 421
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

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
        self.enterRule(localctx, 84, self.RULE_functionParameters)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.match(RulepadGrammarParser.PARAMETER)
            self.state = 424
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 423
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
        self.enterRule(localctx, 86, self.RULE_functionParameterCondition)
        try:
            self.state = 432
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 426
                self.combinatorialWords()
                self.state = 427
                self.match(RulepadGrammarParser.SPACE)
                self.state = 429
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                if la_ == 1:
                    self.state = 428
                    self.functionParameterConditionTransition()


                pass
            elif token in [RulepadGrammarParser.T__16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 431
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
        self.enterRule(localctx, 88, self.RULE_functionParameterConditionTransition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            self.withWord()
            self.state = 435
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
        _startState = 90
        self.enterRecursionRule(localctx, 90, self.RULE_functionParameterExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 447
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 438
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 439
                self.functionParameterExpression(0)
                self.state = 440
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.NAME, RulepadGrammarParser.ANNOTATION, RulepadGrammarParser.TYPES]:
                self.state = 445
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.TYPES]:
                    self.state = 442
                    self.types()
                    pass
                elif token in [RulepadGrammarParser.NAME]:
                    self.state = 443
                    self.names()
                    pass
                elif token in [RulepadGrammarParser.ANNOTATION]:
                    self.state = 444
                    self.annotations()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 457
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 455
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.FunctionParameterExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_functionParameterExpression)
                        self.state = 449
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 450
                        localctx.op = self.binary()
                        self.state = 451
                        localctx.right = self.functionParameterExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.FunctionParameterExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_functionParameterExpression)
                        self.state = 453
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 454
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 459
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

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
        self.enterRule(localctx, 92, self.RULE_types)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            self.match(RulepadGrammarParser.TYPES)
            self.state = 461
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
        self.enterRule(localctx, 94, self.RULE_typeCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 463
            self.combinatorialWords()
            self.state = 464
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
        self.enterRule(localctx, 96, self.RULE_declarationStatements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
            self.match(RulepadGrammarParser.DeclarationStatement)
            self.state = 467
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
        self.enterRule(localctx, 98, self.RULE_declarationStatementCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 469
            self.withWord()
            self.state = 470
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


        def enclosingClass(self):
            return self.getTypedRuleContext(RulepadGrammarParser.EnclosingClassContext,0)


        def declarationStatementExpressionOneOf(self):
            return self.getTypedRuleContext(RulepadGrammarParser.DeclarationStatementExpressionOneOfContext,0)


        def declarationStatementExpressionNoneOf(self):
            return self.getTypedRuleContext(RulepadGrammarParser.DeclarationStatementExpressionNoneOfContext,0)


        def declarationStatementExpressionNo(self):
            return self.getTypedRuleContext(RulepadGrammarParser.DeclarationStatementExpressionNoContext,0)


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
        _startState = 100
        self.enterRecursionRule(localctx, 100, self.RULE_declarationStatementExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 486
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 473
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 474
                self.declarationStatementExpression(0)
                self.state = 475
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.ONE_OF, RulepadGrammarParser.NONE_OF, RulepadGrammarParser.NO, RulepadGrammarParser.ANNOTATION, RulepadGrammarParser.TYPES, RulepadGrammarParser.ConfigurationFile, RulepadGrammarParser.ENCLOSING_CLASS]:
                self.state = 484
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.ANNOTATION]:
                    self.state = 477
                    self.annotations()
                    pass
                elif token in [RulepadGrammarParser.TYPES]:
                    self.state = 478
                    self.types()
                    pass
                elif token in [RulepadGrammarParser.ConfigurationFile]:
                    self.state = 479
                    self.configurationFiles()
                    pass
                elif token in [RulepadGrammarParser.ENCLOSING_CLASS]:
                    self.state = 480
                    self.enclosingClass()
                    pass
                elif token in [RulepadGrammarParser.ONE_OF]:
                    self.state = 481
                    self.declarationStatementExpressionOneOf()
                    pass
                elif token in [RulepadGrammarParser.NONE_OF]:
                    self.state = 482
                    self.declarationStatementExpressionNoneOf()
                    pass
                elif token in [RulepadGrammarParser.NO]:
                    self.state = 483
                    self.declarationStatementExpressionNo()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 496
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 494
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.DeclarationStatementExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_declarationStatementExpression)
                        self.state = 488
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 489
                        localctx.op = self.binary()
                        self.state = 490
                        localctx.right = self.declarationStatementExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.DeclarationStatementExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_declarationStatementExpression)
                        self.state = 492
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 493
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 498
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class DeclarationStatementExpressionOneOfContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ONE_OF(self):
            return self.getToken(RulepadGrammarParser.ONE_OF, 0)

        def LPAREN(self):
            return self.getToken(RulepadGrammarParser.LPAREN, 0)

        def declarationStatementExpressionAggregateContents(self):
            return self.getTypedRuleContext(RulepadGrammarParser.DeclarationStatementExpressionAggregateContentsContext,0)


        def RPAREN(self):
            return self.getToken(RulepadGrammarParser.RPAREN, 0)

        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_declarationStatementExpressionOneOf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclarationStatementExpressionOneOf" ):
                listener.enterDeclarationStatementExpressionOneOf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclarationStatementExpressionOneOf" ):
                listener.exitDeclarationStatementExpressionOneOf(self)




    def declarationStatementExpressionOneOf(self):

        localctx = RulepadGrammarParser.DeclarationStatementExpressionOneOfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_declarationStatementExpressionOneOf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 499
            self.match(RulepadGrammarParser.ONE_OF)
            self.state = 500
            self.match(RulepadGrammarParser.LPAREN)
            self.state = 501
            self.declarationStatementExpressionAggregateContents(0)
            self.state = 502
            self.match(RulepadGrammarParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationStatementExpressionNoneOfContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NONE_OF(self):
            return self.getToken(RulepadGrammarParser.NONE_OF, 0)

        def LPAREN(self):
            return self.getToken(RulepadGrammarParser.LPAREN, 0)

        def declarationStatementExpressionAggregateContents(self):
            return self.getTypedRuleContext(RulepadGrammarParser.DeclarationStatementExpressionAggregateContentsContext,0)


        def RPAREN(self):
            return self.getToken(RulepadGrammarParser.RPAREN, 0)

        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_declarationStatementExpressionNoneOf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclarationStatementExpressionNoneOf" ):
                listener.enterDeclarationStatementExpressionNoneOf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclarationStatementExpressionNoneOf" ):
                listener.exitDeclarationStatementExpressionNoneOf(self)




    def declarationStatementExpressionNoneOf(self):

        localctx = RulepadGrammarParser.DeclarationStatementExpressionNoneOfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_declarationStatementExpressionNoneOf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
            self.match(RulepadGrammarParser.NONE_OF)
            self.state = 505
            self.match(RulepadGrammarParser.LPAREN)
            self.state = 506
            self.declarationStatementExpressionAggregateContents(0)
            self.state = 507
            self.match(RulepadGrammarParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationStatementExpressionNoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NO(self):
            return self.getToken(RulepadGrammarParser.NO, 0)

        def annotations(self):
            return self.getTypedRuleContext(RulepadGrammarParser.AnnotationsContext,0)


        def types(self):
            return self.getTypedRuleContext(RulepadGrammarParser.TypesContext,0)


        def configurationFiles(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ConfigurationFilesContext,0)


        def enclosingClass(self):
            return self.getTypedRuleContext(RulepadGrammarParser.EnclosingClassContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_declarationStatementExpressionNo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclarationStatementExpressionNo" ):
                listener.enterDeclarationStatementExpressionNo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclarationStatementExpressionNo" ):
                listener.exitDeclarationStatementExpressionNo(self)




    def declarationStatementExpressionNo(self):

        localctx = RulepadGrammarParser.DeclarationStatementExpressionNoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_declarationStatementExpressionNo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 509
            self.match(RulepadGrammarParser.NO)
            self.state = 514
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.ANNOTATION]:
                self.state = 510
                self.annotations()
                pass
            elif token in [RulepadGrammarParser.TYPES]:
                self.state = 511
                self.types()
                pass
            elif token in [RulepadGrammarParser.ConfigurationFile]:
                self.state = 512
                self.configurationFiles()
                pass
            elif token in [RulepadGrammarParser.ENCLOSING_CLASS]:
                self.state = 513
                self.enclosingClass()
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


    class DeclarationStatementExpressionAggregateContentsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # DeclarationStatementExpressionAggregateContentsContext
            self.op = None # Or_Context
            self.right = None # DeclarationStatementExpressionAggregateContentsContext

        def annotations(self):
            return self.getTypedRuleContext(RulepadGrammarParser.AnnotationsContext,0)


        def types(self):
            return self.getTypedRuleContext(RulepadGrammarParser.TypesContext,0)


        def configurationFiles(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ConfigurationFilesContext,0)


        def enclosingClass(self):
            return self.getTypedRuleContext(RulepadGrammarParser.EnclosingClassContext,0)


        def declarationStatementExpressionAggregateContents(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RulepadGrammarParser.DeclarationStatementExpressionAggregateContentsContext)
            else:
                return self.getTypedRuleContext(RulepadGrammarParser.DeclarationStatementExpressionAggregateContentsContext,i)


        def or_(self):
            return self.getTypedRuleContext(RulepadGrammarParser.Or_Context,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_declarationStatementExpressionAggregateContents

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclarationStatementExpressionAggregateContents" ):
                listener.enterDeclarationStatementExpressionAggregateContents(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclarationStatementExpressionAggregateContents" ):
                listener.exitDeclarationStatementExpressionAggregateContents(self)



    def declarationStatementExpressionAggregateContents(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RulepadGrammarParser.DeclarationStatementExpressionAggregateContentsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 108
        self.enterRecursionRule(localctx, 108, self.RULE_declarationStatementExpressionAggregateContents, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 521
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.ANNOTATION]:
                self.state = 517
                self.annotations()
                pass
            elif token in [RulepadGrammarParser.TYPES]:
                self.state = 518
                self.types()
                pass
            elif token in [RulepadGrammarParser.ConfigurationFile]:
                self.state = 519
                self.configurationFiles()
                pass
            elif token in [RulepadGrammarParser.ENCLOSING_CLASS]:
                self.state = 520
                self.enclosingClass()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 529
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = RulepadGrammarParser.DeclarationStatementExpressionAggregateContentsContext(self, _parentctx, _parentState)
                    localctx.left = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_declarationStatementExpressionAggregateContents)
                    self.state = 523
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 524
                    localctx.op = self.or_()
                    self.state = 525
                    localctx.right = self.declarationStatementExpressionAggregateContents(3) 
                self.state = 531
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

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
        self.enterRule(localctx, 110, self.RULE_configurationFiles)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 532
            self.match(RulepadGrammarParser.ConfigurationFile)
            self.state = 533
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
        self.enterRule(localctx, 112, self.RULE_configurationFileCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 535
            self.withWord()
            self.state = 536
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
        _startState = 114
        self.enterRecursionRule(localctx, 114, self.RULE_configurationFileExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 544
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 539
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 540
                self.configurationFileExpression(0)
                self.state = 541
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.CONFIGURATION_PROPERTIES]:
                self.state = 543
                self.configurationProperties()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 554
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 552
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.ConfigurationFileExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_configurationFileExpression)
                        self.state = 546
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 547
                        localctx.op = self.binary()
                        self.state = 548
                        localctx.right = self.configurationFileExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.ConfigurationFileExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_configurationFileExpression)
                        self.state = 550
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 551
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 556
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

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
        self.enterRule(localctx, 116, self.RULE_configurationProperties)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 557
            self.match(RulepadGrammarParser.CONFIGURATION_PROPERTIES)
            self.state = 558
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
        self.enterRule(localctx, 118, self.RULE_configurationPropertyCondition)
        try:
            self.state = 566
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 560
                self.combinatorialWords()
                self.state = 561
                self.match(RulepadGrammarParser.SPACE)
                self.state = 563
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
                if la_ == 1:
                    self.state = 562
                    self.configurationPropertyConditionTransition()


                pass
            elif token in [RulepadGrammarParser.T__16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 565
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
        self.enterRule(localctx, 120, self.RULE_configurationPropertyConditionTransition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 568
            self.withWord()
            self.state = 569
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
        _startState = 122
        self.enterRecursionRule(localctx, 122, self.RULE_configurationPropertyExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 581
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 572
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 573
                self.configurationPropertyExpression(0)
                self.state = 574
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.NAME, RulepadGrammarParser.VALUE, RulepadGrammarParser.TYPES]:
                self.state = 579
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.TYPES]:
                    self.state = 576
                    self.types()
                    pass
                elif token in [RulepadGrammarParser.NAME]:
                    self.state = 577
                    self.names()
                    pass
                elif token in [RulepadGrammarParser.VALUE]:
                    self.state = 578
                    self.values()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 591
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,52,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 589
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.ConfigurationPropertyExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_configurationPropertyExpression)
                        self.state = 583
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 584
                        localctx.op = self.binary()
                        self.state = 585
                        localctx.right = self.configurationPropertyExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.ConfigurationPropertyExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_configurationPropertyExpression)
                        self.state = 587
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 588
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 593
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,52,self._ctx)

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
        self.enterRule(localctx, 124, self.RULE_classes)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 594
            self.match(RulepadGrammarParser.CLASSES)
            self.state = 595
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
        self.enterRule(localctx, 126, self.RULE_classCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 597
            self.withWord()
            self.state = 598
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


        def beansFile(self):
            return self.getTypedRuleContext(RulepadGrammarParser.BeansFileContext,0)


        def overriddenFunctions(self):
            return self.getTypedRuleContext(RulepadGrammarParser.OverriddenFunctionsContext,0)


        def classExpressionOneOf(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ClassExpressionOneOfContext,0)


        def classExpressionNoneOf(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ClassExpressionNoneOfContext,0)


        def classExpressionNo(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ClassExpressionNoContext,0)


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
        _startState = 128
        self.enterRecursionRule(localctx, 128, self.RULE_classExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 620
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 601
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 602
                self.classExpression(0)
                self.state = 603
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.ONE_OF, RulepadGrammarParser.NONE_OF, RulepadGrammarParser.NO, RulepadGrammarParser.ANNOTATION, RulepadGrammarParser.EXTENSION, RulepadGrammarParser.IMPLEMENTATION, RulepadGrammarParser.FUNCTION, RulepadGrammarParser.CONSTRUCTOR, RulepadGrammarParser.DeclarationStatement, RulepadGrammarParser.ConfigurationFile, RulepadGrammarParser.OVERRIDDEN_FUNCTION, RulepadGrammarParser.BEAN_DECL, RulepadGrammarParser.BEANS_FILE]:
                self.state = 618
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.ANNOTATION]:
                    self.state = 605
                    self.annotations()
                    pass
                elif token in [RulepadGrammarParser.EXTENSION]:
                    self.state = 606
                    self.extensions()
                    pass
                elif token in [RulepadGrammarParser.IMPLEMENTATION]:
                    self.state = 607
                    self.implementations()
                    pass
                elif token in [RulepadGrammarParser.FUNCTION]:
                    self.state = 608
                    self.functions()
                    pass
                elif token in [RulepadGrammarParser.CONSTRUCTOR]:
                    self.state = 609
                    self.constructors()
                    pass
                elif token in [RulepadGrammarParser.DeclarationStatement]:
                    self.state = 610
                    self.declarationStatements()
                    pass
                elif token in [RulepadGrammarParser.ConfigurationFile]:
                    self.state = 611
                    self.configurationFiles()
                    pass
                elif token in [RulepadGrammarParser.BEAN_DECL]:
                    self.state = 612
                    self.beans()
                    pass
                elif token in [RulepadGrammarParser.BEANS_FILE]:
                    self.state = 613
                    self.beansFile()
                    pass
                elif token in [RulepadGrammarParser.OVERRIDDEN_FUNCTION]:
                    self.state = 614
                    self.overriddenFunctions()
                    pass
                elif token in [RulepadGrammarParser.ONE_OF]:
                    self.state = 615
                    self.classExpressionOneOf()
                    pass
                elif token in [RulepadGrammarParser.NONE_OF]:
                    self.state = 616
                    self.classExpressionNoneOf()
                    pass
                elif token in [RulepadGrammarParser.NO]:
                    self.state = 617
                    self.classExpressionNo()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 630
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,56,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 628
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.ClassExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_classExpression)
                        self.state = 622
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 623
                        localctx.op = self.binary()
                        self.state = 624
                        localctx.right = self.classExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.ClassExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_classExpression)
                        self.state = 626
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 627
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 632
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,56,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ClassExpressionOneOfContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ONE_OF(self):
            return self.getToken(RulepadGrammarParser.ONE_OF, 0)

        def LPAREN(self):
            return self.getToken(RulepadGrammarParser.LPAREN, 0)

        def classExpressionAggregateContents(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ClassExpressionAggregateContentsContext,0)


        def RPAREN(self):
            return self.getToken(RulepadGrammarParser.RPAREN, 0)

        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_classExpressionOneOf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassExpressionOneOf" ):
                listener.enterClassExpressionOneOf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassExpressionOneOf" ):
                listener.exitClassExpressionOneOf(self)




    def classExpressionOneOf(self):

        localctx = RulepadGrammarParser.ClassExpressionOneOfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_classExpressionOneOf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 633
            self.match(RulepadGrammarParser.ONE_OF)
            self.state = 634
            self.match(RulepadGrammarParser.LPAREN)
            self.state = 635
            self.classExpressionAggregateContents(0)
            self.state = 636
            self.match(RulepadGrammarParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassExpressionNoneOfContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NONE_OF(self):
            return self.getToken(RulepadGrammarParser.NONE_OF, 0)

        def LPAREN(self):
            return self.getToken(RulepadGrammarParser.LPAREN, 0)

        def classExpressionAggregateContents(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ClassExpressionAggregateContentsContext,0)


        def RPAREN(self):
            return self.getToken(RulepadGrammarParser.RPAREN, 0)

        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_classExpressionNoneOf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassExpressionNoneOf" ):
                listener.enterClassExpressionNoneOf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassExpressionNoneOf" ):
                listener.exitClassExpressionNoneOf(self)




    def classExpressionNoneOf(self):

        localctx = RulepadGrammarParser.ClassExpressionNoneOfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_classExpressionNoneOf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 638
            self.match(RulepadGrammarParser.NONE_OF)
            self.state = 639
            self.match(RulepadGrammarParser.LPAREN)
            self.state = 640
            self.classExpressionAggregateContents(0)
            self.state = 641
            self.match(RulepadGrammarParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassExpressionNoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NO(self):
            return self.getToken(RulepadGrammarParser.NO, 0)

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


        def beansFile(self):
            return self.getTypedRuleContext(RulepadGrammarParser.BeansFileContext,0)


        def overriddenFunctions(self):
            return self.getTypedRuleContext(RulepadGrammarParser.OverriddenFunctionsContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_classExpressionNo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassExpressionNo" ):
                listener.enterClassExpressionNo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassExpressionNo" ):
                listener.exitClassExpressionNo(self)




    def classExpressionNo(self):

        localctx = RulepadGrammarParser.ClassExpressionNoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_classExpressionNo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 643
            self.match(RulepadGrammarParser.NO)
            self.state = 654
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.ANNOTATION]:
                self.state = 644
                self.annotations()
                pass
            elif token in [RulepadGrammarParser.EXTENSION]:
                self.state = 645
                self.extensions()
                pass
            elif token in [RulepadGrammarParser.IMPLEMENTATION]:
                self.state = 646
                self.implementations()
                pass
            elif token in [RulepadGrammarParser.FUNCTION]:
                self.state = 647
                self.functions()
                pass
            elif token in [RulepadGrammarParser.CONSTRUCTOR]:
                self.state = 648
                self.constructors()
                pass
            elif token in [RulepadGrammarParser.DeclarationStatement]:
                self.state = 649
                self.declarationStatements()
                pass
            elif token in [RulepadGrammarParser.ConfigurationFile]:
                self.state = 650
                self.configurationFiles()
                pass
            elif token in [RulepadGrammarParser.BEAN_DECL]:
                self.state = 651
                self.beans()
                pass
            elif token in [RulepadGrammarParser.BEANS_FILE]:
                self.state = 652
                self.beansFile()
                pass
            elif token in [RulepadGrammarParser.OVERRIDDEN_FUNCTION]:
                self.state = 653
                self.overriddenFunctions()
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


    class ClassExpressionAggregateContentsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # ClassExpressionAggregateContentsContext
            self.op = None # Or_Context
            self.right = None # ClassExpressionAggregateContentsContext

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


        def beansFile(self):
            return self.getTypedRuleContext(RulepadGrammarParser.BeansFileContext,0)


        def overriddenFunctions(self):
            return self.getTypedRuleContext(RulepadGrammarParser.OverriddenFunctionsContext,0)


        def classExpressionAggregateContents(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RulepadGrammarParser.ClassExpressionAggregateContentsContext)
            else:
                return self.getTypedRuleContext(RulepadGrammarParser.ClassExpressionAggregateContentsContext,i)


        def or_(self):
            return self.getTypedRuleContext(RulepadGrammarParser.Or_Context,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_classExpressionAggregateContents

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassExpressionAggregateContents" ):
                listener.enterClassExpressionAggregateContents(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassExpressionAggregateContents" ):
                listener.exitClassExpressionAggregateContents(self)



    def classExpressionAggregateContents(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RulepadGrammarParser.ClassExpressionAggregateContentsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 136
        self.enterRecursionRule(localctx, 136, self.RULE_classExpressionAggregateContents, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 667
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.ANNOTATION]:
                self.state = 657
                self.annotations()
                pass
            elif token in [RulepadGrammarParser.EXTENSION]:
                self.state = 658
                self.extensions()
                pass
            elif token in [RulepadGrammarParser.IMPLEMENTATION]:
                self.state = 659
                self.implementations()
                pass
            elif token in [RulepadGrammarParser.FUNCTION]:
                self.state = 660
                self.functions()
                pass
            elif token in [RulepadGrammarParser.CONSTRUCTOR]:
                self.state = 661
                self.constructors()
                pass
            elif token in [RulepadGrammarParser.DeclarationStatement]:
                self.state = 662
                self.declarationStatements()
                pass
            elif token in [RulepadGrammarParser.ConfigurationFile]:
                self.state = 663
                self.configurationFiles()
                pass
            elif token in [RulepadGrammarParser.BEAN_DECL]:
                self.state = 664
                self.beans()
                pass
            elif token in [RulepadGrammarParser.BEANS_FILE]:
                self.state = 665
                self.beansFile()
                pass
            elif token in [RulepadGrammarParser.OVERRIDDEN_FUNCTION]:
                self.state = 666
                self.overriddenFunctions()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 675
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,59,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = RulepadGrammarParser.ClassExpressionAggregateContentsContext(self, _parentctx, _parentState)
                    localctx.left = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_classExpressionAggregateContents)
                    self.state = 669
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 670
                    localctx.op = self.or_()
                    self.state = 671
                    localctx.right = self.classExpressionAggregateContents(3) 
                self.state = 677
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,59,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class EnclosingClassContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENCLOSING_CLASS(self):
            return self.getToken(RulepadGrammarParser.ENCLOSING_CLASS, 0)

        def classCondition(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ClassConditionContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_enclosingClass

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnclosingClass" ):
                listener.enterEnclosingClass(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnclosingClass" ):
                listener.exitEnclosingClass(self)




    def enclosingClass(self):

        localctx = RulepadGrammarParser.EnclosingClassContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_enclosingClass)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 678
            self.match(RulepadGrammarParser.ENCLOSING_CLASS)
            self.state = 679
            self.classCondition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OverriddenFunctionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OVERRIDDEN_FUNCTION(self):
            return self.getToken(RulepadGrammarParser.OVERRIDDEN_FUNCTION, 0)

        def combinatorialWords(self):
            return self.getTypedRuleContext(RulepadGrammarParser.CombinatorialWordsContext,0)


        def SPACE(self):
            return self.getToken(RulepadGrammarParser.SPACE, 0)

        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_overriddenFunctions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOverriddenFunctions" ):
                listener.enterOverriddenFunctions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOverriddenFunctions" ):
                listener.exitOverriddenFunctions(self)




    def overriddenFunctions(self):

        localctx = RulepadGrammarParser.OverriddenFunctionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_overriddenFunctions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 681
            self.match(RulepadGrammarParser.OVERRIDDEN_FUNCTION)
            self.state = 682
            self.combinatorialWords()
            self.state = 683
            self.match(RulepadGrammarParser.SPACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
        self.enterRule(localctx, 142, self.RULE_beans)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 685
            self.match(RulepadGrammarParser.BEAN_DECL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BeansFileContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEANS_FILE(self):
            return self.getToken(RulepadGrammarParser.BEANS_FILE, 0)

        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_beansFile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBeansFile" ):
                listener.enterBeansFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBeansFile" ):
                listener.exitBeansFile(self)




    def beansFile(self):

        localctx = RulepadGrammarParser.BeansFileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_beansFile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 687
            self.match(RulepadGrammarParser.BEANS_FILE)
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
        self._predicates[31] = self.functionExpressionAggregateContents_sempred
        self._predicates[37] = self.constructorExpression_sempred
        self._predicates[41] = self.annotationParameterExpression_sempred
        self._predicates[45] = self.functionParameterExpression_sempred
        self._predicates[50] = self.declarationStatementExpression_sempred
        self._predicates[54] = self.declarationStatementExpressionAggregateContents_sempred
        self._predicates[57] = self.configurationFileExpression_sempred
        self._predicates[61] = self.configurationPropertyExpression_sempred
        self._predicates[64] = self.classExpression_sempred
        self._predicates[68] = self.classExpressionAggregateContents_sempred
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
         

    def functionExpressionAggregateContents_sempred(self, localctx:FunctionExpressionAggregateContentsContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def constructorExpression_sempred(self, localctx:ConstructorExpressionContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 1)
         

    def annotationParameterExpression_sempred(self, localctx:AnnotationParameterExpressionContext, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 1)
         

    def functionParameterExpression_sempred(self, localctx:FunctionParameterExpressionContext, predIndex:int):
            if predIndex == 9:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 1)
         

    def declarationStatementExpression_sempred(self, localctx:DeclarationStatementExpressionContext, predIndex:int):
            if predIndex == 11:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 1)
         

    def declarationStatementExpressionAggregateContents_sempred(self, localctx:DeclarationStatementExpressionAggregateContentsContext, predIndex:int):
            if predIndex == 13:
                return self.precpred(self._ctx, 2)
         

    def configurationFileExpression_sempred(self, localctx:ConfigurationFileExpressionContext, predIndex:int):
            if predIndex == 14:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 1)
         

    def configurationPropertyExpression_sempred(self, localctx:ConfigurationPropertyExpressionContext, predIndex:int):
            if predIndex == 16:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 17:
                return self.precpred(self._ctx, 1)
         

    def classExpression_sempred(self, localctx:ClassExpressionContext, predIndex:int):
            if predIndex == 18:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 19:
                return self.precpred(self._ctx, 1)
         

    def classExpressionAggregateContents_sempred(self, localctx:ClassExpressionAggregateContentsContext, predIndex:int):
            if predIndex == 20:
                return self.precpred(self._ctx, 2)
         




