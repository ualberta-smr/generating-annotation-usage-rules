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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3,")
        buf.write("\u0266\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\3\2\7\2z\n\2\f\2\16\2}\13\2\3\2\5\2\u0080\n\2")
        buf.write("\3\2\5\2\u0083\n\2\3\2\7\2\u0086\n\2\f\2\16\2\u0089\13")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u00a1\n\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\7\4\u00aa\n\4\f\4\16\4\u00ad")
        buf.write("\13\4\3\4\3\4\3\4\3\5\6\5\u00b3\n\5\r\5\16\5\u00b4\3\5")
        buf.write("\3\5\6\5\u00b9\n\5\r\5\16\5\u00ba\3\5\3\5\6\5\u00bf\n")
        buf.write("\5\r\5\16\5\u00c0\3\5\3\5\6\5\u00c5\n\5\r\5\16\5\u00c6")
        buf.write("\3\5\6\5\u00ca\n\5\r\5\16\5\u00cb\3\5\3\5\3\5\6\5\u00d1")
        buf.write("\n\5\r\5\16\5\u00d2\3\5\3\5\3\5\6\5\u00d8\n\5\r\5\16\5")
        buf.write("\u00d9\3\5\3\5\3\5\6\5\u00df\n\5\r\5\16\5\u00e0\3\5\5")
        buf.write("\5\u00e4\n\5\3\6\3\6\3\6\3\6\6\6\u00ea\n\6\r\6\16\6\u00eb")
        buf.write("\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\6\n\u00fa")
        buf.write("\n\n\r\n\16\n\u00fb\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r")
        buf.write("\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\5\21\u010e\n")
        buf.write("\21\3\22\3\22\5\22\u0112\n\22\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\26\3\26\5\26\u011f\n\26\3\27\3")
        buf.write("\27\3\27\5\27\u0124\n\27\3\27\5\27\u0127\n\27\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u0132\n\31\3")
        buf.write("\31\3\31\3\31\3\31\3\31\3\31\7\31\u013a\n\31\f\31\16\31")
        buf.write("\u013d\13\31\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\5")
        buf.write("\33\u0147\n\33\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35")
        buf.write("\5\35\u0151\n\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3 \5 \u0161\n \5 \u0163\n \3 \3 \3 \3 \3")
        buf.write(" \3 \7 \u016b\n \f \16 \u016e\13 \3!\3!\3!\3\"\3\"\3\"")
        buf.write("\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\5$\u0180\n$\5$\u0182\n")
        buf.write("$\3$\3$\3$\3$\3$\3$\7$\u018a\n$\f$\16$\u018d\13$\3%\3")
        buf.write("%\3%\3&\3&\3&\5&\u0195\n&\3&\5&\u0198\n&\3\'\3\'\3\'\3")
        buf.write("(\3(\3(\3(\3(\3(\3(\3(\5(\u01a5\n(\5(\u01a7\n(\3(\3(\3")
        buf.write("(\3(\3(\3(\7(\u01af\n(\f(\16(\u01b2\13(\3)\3)\5)\u01b6")
        buf.write("\n)\3*\3*\3*\5*\u01bb\n*\3*\5*\u01be\n*\3+\3+\3+\3,\3")
        buf.write(",\3,\3,\3,\3,\3,\3,\5,\u01cb\n,\5,\u01cd\n,\3,\3,\3,\3")
        buf.write(",\3,\3,\7,\u01d5\n,\f,\16,\u01d8\13,\3-\3-\5-\u01dc\n")
        buf.write("-\3.\3.\3.\3.\3.\3.\5.\u01e4\n.\3/\3/\3/\3\60\3\60\3\60")
        buf.write("\3\61\3\61\3\61\3\61\3\61\3\61\3\61\5\61\u01f3\n\61\5")
        buf.write("\61\u01f5\n\61\3\61\3\61\3\61\3\61\3\61\3\61\7\61\u01fd")
        buf.write("\n\61\f\61\16\61\u0200\13\61\3\62\3\62\5\62\u0204\n\62")
        buf.write("\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64\5\64\u020f")
        buf.write("\n\64\3\64\3\64\3\64\3\64\3\64\3\64\7\64\u0217\n\64\f")
        buf.write("\64\16\64\u021a\13\64\3\65\3\65\3\65\3\66\3\66\3\66\5")
        buf.write("\66\u0222\n\66\3\66\5\66\u0225\n\66\3\67\3\67\3\67\38")
        buf.write("\38\38\38\38\38\38\38\58\u0232\n8\58\u0234\n8\38\38\3")
        buf.write("8\38\38\38\78\u023c\n8\f8\168\u023f\138\39\39\59\u0243")
        buf.write("\n9\3:\3:\3:\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\5")
        buf.write(";\u0255\n;\5;\u0257\n;\3;\3;\3;\3;\3;\3;\7;\u025f\n;\f")
        buf.write(";\16;\u0262\13;\3<\3<\3<\2\13\60>FNV`fnt=\2\4\6\b\n\f")
        buf.write("\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@")
        buf.write("BDFHJLNPRTVXZ\\^`bdfhjlnprtv\2\3\4\2\t\21\33\34\2\u0286")
        buf.write("\2\177\3\2\2\2\4\u00a0\3\2\2\2\6\u00a2\3\2\2\2\b\u00e3")
        buf.write("\3\2\2\2\n\u00e5\3\2\2\2\f\u00ef\3\2\2\2\16\u00f1\3\2")
        buf.write("\2\2\20\u00f3\3\2\2\2\22\u00f5\3\2\2\2\24\u00ff\3\2\2")
        buf.write("\2\26\u0101\3\2\2\2\30\u0103\3\2\2\2\32\u0105\3\2\2\2")
        buf.write("\34\u0107\3\2\2\2\36\u0109\3\2\2\2 \u010d\3\2\2\2\"\u010f")
        buf.write("\3\2\2\2$\u0113\3\2\2\2&\u0116\3\2\2\2(\u0119\3\2\2\2")
        buf.write("*\u011c\3\2\2\2,\u0126\3\2\2\2.\u0128\3\2\2\2\60\u0131")
        buf.write("\3\2\2\2\62\u013e\3\2\2\2\64\u0141\3\2\2\2\66\u0148\3")
        buf.write("\2\2\28\u014b\3\2\2\2:\u0152\3\2\2\2<\u0155\3\2\2\2>\u0162")
        buf.write("\3\2\2\2@\u016f\3\2\2\2B\u0172\3\2\2\2D\u0175\3\2\2\2")
        buf.write("F\u0181\3\2\2\2H\u018e\3\2\2\2J\u0197\3\2\2\2L\u0199\3")
        buf.write("\2\2\2N\u01a6\3\2\2\2P\u01b3\3\2\2\2R\u01bd\3\2\2\2T\u01bf")
        buf.write("\3\2\2\2V\u01cc\3\2\2\2X\u01d9\3\2\2\2Z\u01e3\3\2\2\2")
        buf.write("\\\u01e5\3\2\2\2^\u01e8\3\2\2\2`\u01f4\3\2\2\2b\u0201")
        buf.write("\3\2\2\2d\u0205\3\2\2\2f\u020e\3\2\2\2h\u021b\3\2\2\2")
        buf.write("j\u0224\3\2\2\2l\u0226\3\2\2\2n\u0233\3\2\2\2p\u0240\3")
        buf.write("\2\2\2r\u0244\3\2\2\2t\u0256\3\2\2\2v\u0263\3\2\2\2xz")
        buf.write("\5\20\t\2yx\3\2\2\2z}\3\2\2\2{y\3\2\2\2{|\3\2\2\2|\u0080")
        buf.write("\3\2\2\2}{\3\2\2\2~\u0080\5\4\3\2\177{\3\2\2\2\177~\3")
        buf.write("\2\2\2\u0080\u0082\3\2\2\2\u0081\u0083\5\16\b\2\u0082")
        buf.write("\u0081\3\2\2\2\u0082\u0083\3\2\2\2\u0083\u0087\3\2\2\2")
        buf.write("\u0084\u0086\7\32\2\2\u0085\u0084\3\2\2\2\u0086\u0089")
        buf.write("\3\2\2\2\u0087\u0085\3\2\2\2\u0087\u0088\3\2\2\2\u0088")
        buf.write("\u008a\3\2\2\2\u0089\u0087\3\2\2\2\u008a\u008b\7\2\2\3")
        buf.write("\u008b\3\3\2\2\2\u008c\u008d\5:\36\2\u008d\u008e\5\24")
        buf.write("\13\2\u008e\u008f\5\34\17\2\u008f\u0090\5> \2\u0090\u00a1")
        buf.write("\3\2\2\2\u0091\u0092\5@!\2\u0092\u0093\5\24\13\2\u0093")
        buf.write("\u0094\5\34\17\2\u0094\u0095\5F$\2\u0095\u00a1\3\2\2\2")
        buf.write("\u0096\u0097\5p9\2\u0097\u0098\5\24\13\2\u0098\u0099\5")
        buf.write("\34\17\2\u0099\u009a\5t;\2\u009a\u00a1\3\2\2\2\u009b\u009c")
        buf.write("\5\\/\2\u009c\u009d\5\24\13\2\u009d\u009e\5\34\17\2\u009e")
        buf.write("\u009f\5`\61\2\u009f\u00a1\3\2\2\2\u00a0\u008c\3\2\2\2")
        buf.write("\u00a0\u0091\3\2\2\2\u00a0\u0096\3\2\2\2\u00a0\u009b\3")
        buf.write("\2\2\2\u00a1\5\3\2\2\2\u00a2\u00ab\7\3\2\2\u00a3\u00a4")
        buf.write("\5\b\5\2\u00a4\u00a5\7\4\2\2\u00a5\u00aa\3\2\2\2\u00a6")
        buf.write("\u00a7\5\b\5\2\u00a7\u00a8\7\5\2\2\u00a8\u00aa\3\2\2\2")
        buf.write("\u00a9\u00a3\3\2\2\2\u00a9\u00a6\3\2\2\2\u00aa\u00ad\3")
        buf.write("\2\2\2\u00ab\u00a9\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00ae")
        buf.write("\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ae\u00af\5\b\5\2\u00af")
        buf.write("\u00b0\7\3\2\2\u00b0\7\3\2\2\2\u00b1\u00b3\7\31\2\2\u00b2")
        buf.write("\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b2\3\2\2\2")
        buf.write("\u00b4\u00b5\3\2\2\2\u00b5\u00e4\3\2\2\2\u00b6\u00b8\7")
        buf.write("\6\2\2\u00b7\u00b9\7\31\2\2\u00b8\u00b7\3\2\2\2\u00b9")
        buf.write("\u00ba\3\2\2\2\u00ba\u00b8\3\2\2\2\u00ba\u00bb\3\2\2\2")
        buf.write("\u00bb\u00e4\3\2\2\2\u00bc\u00be\7\7\2\2\u00bd\u00bf\7")
        buf.write("\31\2\2\u00be\u00bd\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0")
        buf.write("\u00be\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00e4\3\2\2\2")
        buf.write("\u00c2\u00c4\7\b\2\2\u00c3\u00c5\7\31\2\2\u00c4\u00c3")
        buf.write("\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c6")
        buf.write("\u00c7\3\2\2\2\u00c7\u00e4\3\2\2\2\u00c8\u00ca\7\31\2")
        buf.write("\2\u00c9\u00c8\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00c9")
        buf.write("\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd")
        buf.write("\u00e4\7\7\2\2\u00ce\u00d0\7\6\2\2\u00cf\u00d1\7\31\2")
        buf.write("\2\u00d0\u00cf\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\u00d0")
        buf.write("\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4")
        buf.write("\u00e4\7\7\2\2\u00d5\u00d7\7\7\2\2\u00d6\u00d8\7\31\2")
        buf.write("\2\u00d7\u00d6\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9\u00d7")
        buf.write("\3\2\2\2\u00d9\u00da\3\2\2\2\u00da\u00db\3\2\2\2\u00db")
        buf.write("\u00e4\7\7\2\2\u00dc\u00de\7\b\2\2\u00dd\u00df\7\31\2")
        buf.write("\2\u00de\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\u00de")
        buf.write("\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2")
        buf.write("\u00e4\7\7\2\2\u00e3\u00b2\3\2\2\2\u00e3\u00b6\3\2\2\2")
        buf.write("\u00e3\u00bc\3\2\2\2\u00e3\u00c2\3\2\2\2\u00e3\u00c9\3")
        buf.write("\2\2\2\u00e3\u00ce\3\2\2\2\u00e3\u00d5\3\2\2\2\u00e3\u00dc")
        buf.write("\3\2\2\2\u00e4\t\3\2\2\2\u00e5\u00e9\7\3\2\2\u00e6\u00ea")
        buf.write("\7\31\2\2\u00e7\u00ea\5\f\7\2\u00e8\u00ea\7\30\2\2\u00e9")
        buf.write("\u00e6\3\2\2\2\u00e9\u00e7\3\2\2\2\u00e9\u00e8\3\2\2\2")
        buf.write("\u00ea\u00eb\3\2\2\2\u00eb\u00e9\3\2\2\2\u00eb\u00ec\3")
        buf.write("\2\2\2\u00ec\u00ed\3\2\2\2\u00ed\u00ee\7\3\2\2\u00ee\13")
        buf.write("\3\2\2\2\u00ef\u00f0\t\2\2\2\u00f0\r\3\2\2\2\u00f1\u00f2")
        buf.write("\7\t\2\2\u00f2\17\3\2\2\2\u00f3\u00f4\7\32\2\2\u00f4\21")
        buf.write("\3\2\2\2\u00f5\u00f9\7\3\2\2\u00f6\u00fa\7\31\2\2\u00f7")
        buf.write("\u00fa\5\f\7\2\u00f8\u00fa\7\30\2\2\u00f9\u00f6\3\2\2")
        buf.write("\2\u00f9\u00f7\3\2\2\2\u00f9\u00f8\3\2\2\2\u00fa\u00fb")
        buf.write("\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc")
        buf.write("\u00fd\3\2\2\2\u00fd\u00fe\7\3\2\2\u00fe\23\3\2\2\2\u00ff")
        buf.write("\u0100\7\22\2\2\u0100\25\3\2\2\2\u0101\u0102\7\23\2\2")
        buf.write("\u0102\27\3\2\2\2\u0103\u0104\7\24\2\2\u0104\31\3\2\2")
        buf.write("\2\u0105\u0106\7\25\2\2\u0106\33\3\2\2\2\u0107\u0108\7")
        buf.write("\26\2\2\u0108\35\3\2\2\2\u0109\u010a\7\27\2\2\u010a\37")
        buf.write("\3\2\2\2\u010b\u010e\5\30\r\2\u010c\u010e\5\32\16\2\u010d")
        buf.write("\u010b\3\2\2\2\u010d\u010c\3\2\2\2\u010e!\3\2\2\2\u010f")
        buf.write("\u0111\7\35\2\2\u0110\u0112\5$\23\2\u0111\u0110\3\2\2")
        buf.write("\2\u0111\u0112\3\2\2\2\u0112#\3\2\2\2\u0113\u0114\5\6")
        buf.write("\4\2\u0114\u0115\7\30\2\2\u0115%\3\2\2\2\u0116\u0117\7")
        buf.write("\36\2\2\u0117\u0118\5(\25\2\u0118\'\3\2\2\2\u0119\u011a")
        buf.write("\5\6\4\2\u011a\u011b\7\30\2\2\u011b)\3\2\2\2\u011c\u011e")
        buf.write("\7\37\2\2\u011d\u011f\5,\27\2\u011e\u011d\3\2\2\2\u011e")
        buf.write("\u011f\3\2\2\2\u011f+\3\2\2\2\u0120\u0121\5\n\6\2\u0121")
        buf.write("\u0123\7\30\2\2\u0122\u0124\5.\30\2\u0123\u0122\3\2\2")
        buf.write("\2\u0123\u0124\3\2\2\2\u0124\u0127\3\2\2\2\u0125\u0127")
        buf.write("\5.\30\2\u0126\u0120\3\2\2\2\u0126\u0125\3\2\2\2\u0127")
        buf.write("-\3\2\2\2\u0128\u0129\5\36\20\2\u0129\u012a\5\60\31\2")
        buf.write("\u012a/\3\2\2\2\u012b\u012c\b\31\1\2\u012c\u012d\7\33")
        buf.write("\2\2\u012d\u012e\5\60\31\2\u012e\u012f\7\34\2\2\u012f")
        buf.write("\u0132\3\2\2\2\u0130\u0132\5H%\2\u0131\u012b\3\2\2\2\u0131")
        buf.write("\u0130\3\2\2\2\u0132\u013b\3\2\2\2\u0133\u0134\f\5\2\2")
        buf.write("\u0134\u0135\5 \21\2\u0135\u0136\5\60\31\6\u0136\u013a")
        buf.write("\3\2\2\2\u0137\u0138\f\3\2\2\u0138\u013a\7\30\2\2\u0139")
        buf.write("\u0133\3\2\2\2\u0139\u0137\3\2\2\2\u013a\u013d\3\2\2\2")
        buf.write("\u013b\u0139\3\2\2\2\u013b\u013c\3\2\2\2\u013c\61\3\2")
        buf.write("\2\2\u013d\u013b\3\2\2\2\u013e\u013f\7 \2\2\u013f\u0140")
        buf.write("\5\64\33\2\u0140\63\3\2\2\2\u0141\u0146\5\26\f\2\u0142")
        buf.write("\u0143\5\n\6\2\u0143\u0144\7\30\2\2\u0144\u0147\3\2\2")
        buf.write("\2\u0145\u0147\7!\2\2\u0146\u0142\3\2\2\2\u0146\u0145")
        buf.write("\3\2\2\2\u0147\65\3\2\2\2\u0148\u0149\7\"\2\2\u0149\u014a")
        buf.write("\58\35\2\u014a\67\3\2\2\2\u014b\u0150\5\26\f\2\u014c\u014d")
        buf.write("\5\n\6\2\u014d\u014e\7\30\2\2\u014e\u0151\3\2\2\2\u014f")
        buf.write("\u0151\7#\2\2\u0150\u014c\3\2\2\2\u0150\u014f\3\2\2\2")
        buf.write("\u01519\3\2\2\2\u0152\u0153\7$\2\2\u0153\u0154\5<\37\2")
        buf.write("\u0154;\3\2\2\2\u0155\u0156\5\36\20\2\u0156\u0157\5> ")
        buf.write("\2\u0157=\3\2\2\2\u0158\u0159\b \1\2\u0159\u015a\7\33")
        buf.write("\2\2\u015a\u015b\5> \2\u015b\u015c\7\34\2\2\u015c\u0163")
        buf.write("\3\2\2\2\u015d\u0161\5*\26\2\u015e\u0161\5X-\2\u015f\u0161")
        buf.write("\5P)\2\u0160\u015d\3\2\2\2\u0160\u015e\3\2\2\2\u0160\u015f")
        buf.write("\3\2\2\2\u0161\u0163\3\2\2\2\u0162\u0158\3\2\2\2\u0162")
        buf.write("\u0160\3\2\2\2\u0163\u016c\3\2\2\2\u0164\u0165\f\5\2\2")
        buf.write("\u0165\u0166\5 \21\2\u0166\u0167\5> \6\u0167\u016b\3\2")
        buf.write("\2\2\u0168\u0169\f\3\2\2\u0169\u016b\7\30\2\2\u016a\u0164")
        buf.write("\3\2\2\2\u016a\u0168\3\2\2\2\u016b\u016e\3\2\2\2\u016c")
        buf.write("\u016a\3\2\2\2\u016c\u016d\3\2\2\2\u016d?\3\2\2\2\u016e")
        buf.write("\u016c\3\2\2\2\u016f\u0170\7%\2\2\u0170\u0171\5D#\2\u0171")
        buf.write("A\3\2\2\2\u0172\u0173\5\26\f\2\u0173\u0174\5p9\2\u0174")
        buf.write("C\3\2\2\2\u0175\u0176\5\36\20\2\u0176\u0177\5F$\2\u0177")
        buf.write("E\3\2\2\2\u0178\u0179\b$\1\2\u0179\u017a\7\33\2\2\u017a")
        buf.write("\u017b\5F$\2\u017b\u017c\7\34\2\2\u017c\u0182\3\2\2\2")
        buf.write("\u017d\u0180\5*\26\2\u017e\u0180\5P)\2\u017f\u017d\3\2")
        buf.write("\2\2\u017f\u017e\3\2\2\2\u0180\u0182\3\2\2\2\u0181\u0178")
        buf.write("\3\2\2\2\u0181\u017f\3\2\2\2\u0182\u018b\3\2\2\2\u0183")
        buf.write("\u0184\f\5\2\2\u0184\u0185\5 \21\2\u0185\u0186\5F$\6\u0186")
        buf.write("\u018a\3\2\2\2\u0187\u0188\f\3\2\2\u0188\u018a\7\30\2")
        buf.write("\2\u0189\u0183\3\2\2\2\u0189\u0187\3\2\2\2\u018a\u018d")
        buf.write("\3\2\2\2\u018b\u0189\3\2\2\2\u018b\u018c\3\2\2\2\u018c")
        buf.write("G\3\2\2\2\u018d\u018b\3\2\2\2\u018e\u018f\7&\2\2\u018f")
        buf.write("\u0190\5J&\2\u0190I\3\2\2\2\u0191\u0192\5\n\6\2\u0192")
        buf.write("\u0194\7\30\2\2\u0193\u0195\5L\'\2\u0194\u0193\3\2\2\2")
        buf.write("\u0194\u0195\3\2\2\2\u0195\u0198\3\2\2\2\u0196\u0198\5")
        buf.write("L\'\2\u0197\u0191\3\2\2\2\u0197\u0196\3\2\2\2\u0198K\3")
        buf.write("\2\2\2\u0199\u019a\5\36\20\2\u019a\u019b\5N(\2\u019bM")
        buf.write("\3\2\2\2\u019c\u019d\b(\1\2\u019d\u019e\7\33\2\2\u019e")
        buf.write("\u019f\5N(\2\u019f\u01a0\7\34\2\2\u01a0\u01a7\3\2\2\2")
        buf.write("\u01a1\u01a5\5X-\2\u01a2\u01a5\5\"\22\2\u01a3\u01a5\5")
        buf.write("&\24\2\u01a4\u01a1\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a4\u01a3")
        buf.write("\3\2\2\2\u01a5\u01a7\3\2\2\2\u01a6\u019c\3\2\2\2\u01a6")
        buf.write("\u01a4\3\2\2\2\u01a7\u01b0\3\2\2\2\u01a8\u01a9\f\5\2\2")
        buf.write("\u01a9\u01aa\5 \21\2\u01aa\u01ab\5N(\6\u01ab\u01af\3\2")
        buf.write("\2\2\u01ac\u01ad\f\3\2\2\u01ad\u01af\7\30\2\2\u01ae\u01a8")
        buf.write("\3\2\2\2\u01ae\u01ac\3\2\2\2\u01af\u01b2\3\2\2\2\u01b0")
        buf.write("\u01ae\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1O\3\2\2\2\u01b2")
        buf.write("\u01b0\3\2\2\2\u01b3\u01b5\7&\2\2\u01b4\u01b6\5R*\2\u01b5")
        buf.write("\u01b4\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6Q\3\2\2\2\u01b7")
        buf.write("\u01b8\5\n\6\2\u01b8\u01ba\7\30\2\2\u01b9\u01bb\5T+\2")
        buf.write("\u01ba\u01b9\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb\u01be\3")
        buf.write("\2\2\2\u01bc\u01be\5T+\2\u01bd\u01b7\3\2\2\2\u01bd\u01bc")
        buf.write("\3\2\2\2\u01beS\3\2\2\2\u01bf\u01c0\5\36\20\2\u01c0\u01c1")
        buf.write("\5V,\2\u01c1U\3\2\2\2\u01c2\u01c3\b,\1\2\u01c3\u01c4\7")
        buf.write("\33\2\2\u01c4\u01c5\5V,\2\u01c5\u01c6\7\34\2\2\u01c6\u01cd")
        buf.write("\3\2\2\2\u01c7\u01cb\5X-\2\u01c8\u01cb\5\"\22\2\u01c9")
        buf.write("\u01cb\5*\26\2\u01ca\u01c7\3\2\2\2\u01ca\u01c8\3\2\2\2")
        buf.write("\u01ca\u01c9\3\2\2\2\u01cb\u01cd\3\2\2\2\u01cc\u01c2\3")
        buf.write("\2\2\2\u01cc\u01ca\3\2\2\2\u01cd\u01d6\3\2\2\2\u01ce\u01cf")
        buf.write("\f\5\2\2\u01cf\u01d0\5 \21\2\u01d0\u01d1\5V,\6\u01d1\u01d5")
        buf.write("\3\2\2\2\u01d2\u01d3\f\3\2\2\u01d3\u01d5\7\30\2\2\u01d4")
        buf.write("\u01ce\3\2\2\2\u01d4\u01d2\3\2\2\2\u01d5\u01d8\3\2\2\2")
        buf.write("\u01d6\u01d4\3\2\2\2\u01d6\u01d7\3\2\2\2\u01d7W\3\2\2")
        buf.write("\2\u01d8\u01d6\3\2\2\2\u01d9\u01db\7\'\2\2\u01da\u01dc")
        buf.write("\5Z.\2\u01db\u01da\3\2\2\2\u01db\u01dc\3\2\2\2\u01dcY")
        buf.write("\3\2\2\2\u01dd\u01de\5\n\6\2\u01de\u01df\7\30\2\2\u01df")
        buf.write("\u01e4\3\2\2\2\u01e0\u01e1\5\6\4\2\u01e1\u01e2\7\30\2")
        buf.write("\2\u01e2\u01e4\3\2\2\2\u01e3\u01dd\3\2\2\2\u01e3\u01e0")
        buf.write("\3\2\2\2\u01e4[\3\2\2\2\u01e5\u01e6\7(\2\2\u01e6\u01e7")
        buf.write("\5^\60\2\u01e7]\3\2\2\2\u01e8\u01e9\5\36\20\2\u01e9\u01ea")
        buf.write("\5`\61\2\u01ea_\3\2\2\2\u01eb\u01ec\b\61\1\2\u01ec\u01ed")
        buf.write("\7\33\2\2\u01ed\u01ee\5`\61\2\u01ee\u01ef\7\34\2\2\u01ef")
        buf.write("\u01f5\3\2\2\2\u01f0\u01f3\5*\26\2\u01f1\u01f3\5X-\2\u01f2")
        buf.write("\u01f0\3\2\2\2\u01f2\u01f1\3\2\2\2\u01f3\u01f5\3\2\2\2")
        buf.write("\u01f4\u01eb\3\2\2\2\u01f4\u01f2\3\2\2\2\u01f5\u01fe\3")
        buf.write("\2\2\2\u01f6\u01f7\f\5\2\2\u01f7\u01f8\5 \21\2\u01f8\u01f9")
        buf.write("\5`\61\6\u01f9\u01fd\3\2\2\2\u01fa\u01fb\f\3\2\2\u01fb")
        buf.write("\u01fd\7\30\2\2\u01fc\u01f6\3\2\2\2\u01fc\u01fa\3\2\2")
        buf.write("\2\u01fd\u0200\3\2\2\2\u01fe\u01fc\3\2\2\2\u01fe\u01ff")
        buf.write("\3\2\2\2\u01ffa\3\2\2\2\u0200\u01fe\3\2\2\2\u0201\u0203")
        buf.write("\7)\2\2\u0202\u0204\5d\63\2\u0203\u0202\3\2\2\2\u0203")
        buf.write("\u0204\3\2\2\2\u0204c\3\2\2\2\u0205\u0206\5\36\20\2\u0206")
        buf.write("\u0207\5f\64\2\u0207e\3\2\2\2\u0208\u0209\b\64\1\2\u0209")
        buf.write("\u020a\7\33\2\2\u020a\u020b\5f\64\2\u020b\u020c\7\34\2")
        buf.write("\2\u020c\u020f\3\2\2\2\u020d\u020f\5h\65\2\u020e\u0208")
        buf.write("\3\2\2\2\u020e\u020d\3\2\2\2\u020f\u0218\3\2\2\2\u0210")
        buf.write("\u0211\f\5\2\2\u0211\u0212\5 \21\2\u0212\u0213\5f\64\6")
        buf.write("\u0213\u0217\3\2\2\2\u0214\u0215\f\3\2\2\u0215\u0217\7")
        buf.write("\30\2\2\u0216\u0210\3\2\2\2\u0216\u0214\3\2\2\2\u0217")
        buf.write("\u021a\3\2\2\2\u0218\u0216\3\2\2\2\u0218\u0219\3\2\2\2")
        buf.write("\u0219g\3\2\2\2\u021a\u0218\3\2\2\2\u021b\u021c\7*\2\2")
        buf.write("\u021c\u021d\5j\66\2\u021di\3\2\2\2\u021e\u021f\5\n\6")
        buf.write("\2\u021f\u0221\7\30\2\2\u0220\u0222\5l\67\2\u0221\u0220")
        buf.write("\3\2\2\2\u0221\u0222\3\2\2\2\u0222\u0225\3\2\2\2\u0223")
        buf.write("\u0225\5l\67\2\u0224\u021e\3\2\2\2\u0224\u0223\3\2\2\2")
        buf.write("\u0225k\3\2\2\2\u0226\u0227\5\36\20\2\u0227\u0228\5n8")
        buf.write("\2\u0228m\3\2\2\2\u0229\u022a\b8\1\2\u022a\u022b\7\33")
        buf.write("\2\2\u022b\u022c\5n8\2\u022c\u022d\7\34\2\2\u022d\u0234")
        buf.write("\3\2\2\2\u022e\u0232\5X-\2\u022f\u0232\5\"\22\2\u0230")
        buf.write("\u0232\5&\24\2\u0231\u022e\3\2\2\2\u0231\u022f\3\2\2\2")
        buf.write("\u0231\u0230\3\2\2\2\u0232\u0234\3\2\2\2\u0233\u0229\3")
        buf.write("\2\2\2\u0233\u0231\3\2\2\2\u0234\u023d\3\2\2\2\u0235\u0236")
        buf.write("\f\5\2\2\u0236\u0237\5 \21\2\u0237\u0238\5n8\6\u0238\u023c")
        buf.write("\3\2\2\2\u0239\u023a\f\3\2\2\u023a\u023c\7\30\2\2\u023b")
        buf.write("\u0235\3\2\2\2\u023b\u0239\3\2\2\2\u023c\u023f\3\2\2\2")
        buf.write("\u023d\u023b\3\2\2\2\u023d\u023e\3\2\2\2\u023eo\3\2\2")
        buf.write("\2\u023f\u023d\3\2\2\2\u0240\u0242\7+\2\2\u0241\u0243")
        buf.write("\5r:\2\u0242\u0241\3\2\2\2\u0242\u0243\3\2\2\2\u0243q")
        buf.write("\3\2\2\2\u0244\u0245\5\36\20\2\u0245\u0246\5t;\2\u0246")
        buf.write("s\3\2\2\2\u0247\u0248\b;\1\2\u0248\u0249\7\33\2\2\u0249")
        buf.write("\u024a\5t;\2\u024a\u024b\7\34\2\2\u024b\u0257\3\2\2\2")
        buf.write("\u024c\u0255\5*\26\2\u024d\u0255\5\62\32\2\u024e\u0255")
        buf.write("\5\66\34\2\u024f\u0255\5:\36\2\u0250\u0255\5@!\2\u0251")
        buf.write("\u0255\5\\/\2\u0252\u0255\5b\62\2\u0253\u0255\5v<\2\u0254")
        buf.write("\u024c\3\2\2\2\u0254\u024d\3\2\2\2\u0254\u024e\3\2\2\2")
        buf.write("\u0254\u024f\3\2\2\2\u0254\u0250\3\2\2\2\u0254\u0251\3")
        buf.write("\2\2\2\u0254\u0252\3\2\2\2\u0254\u0253\3\2\2\2\u0255\u0257")
        buf.write("\3\2\2\2\u0256\u0247\3\2\2\2\u0256\u0254\3\2\2\2\u0257")
        buf.write("\u0260\3\2\2\2\u0258\u0259\f\5\2\2\u0259\u025a\5 \21\2")
        buf.write("\u025a\u025b\5t;\6\u025b\u025f\3\2\2\2\u025c\u025d\f\3")
        buf.write("\2\2\u025d\u025f\7\30\2\2\u025e\u0258\3\2\2\2\u025e\u025c")
        buf.write("\3\2\2\2\u025f\u0262\3\2\2\2\u0260\u025e\3\2\2\2\u0260")
        buf.write("\u0261\3\2\2\2\u0261u\3\2\2\2\u0262\u0260\3\2\2\2\u0263")
        buf.write("\u0264\7,\2\2\u0264w\3\2\2\2J{\177\u0082\u0087\u00a0\u00a9")
        buf.write("\u00ab\u00b4\u00ba\u00c0\u00c6\u00cb\u00d2\u00d9\u00e0")
        buf.write("\u00e3\u00e9\u00eb\u00f9\u00fb\u010d\u0111\u011e\u0123")
        buf.write("\u0126\u0131\u0139\u013b\u0146\u0150\u0160\u0162\u016a")
        buf.write("\u016c\u017f\u0181\u0189\u018b\u0194\u0197\u01a4\u01a6")
        buf.write("\u01ae\u01b0\u01b5\u01ba\u01bd\u01ca\u01cc\u01d4\u01d6")
        buf.write("\u01db\u01e3\u01f2\u01f4\u01fc\u01fe\u0203\u020e\u0216")
        buf.write("\u0218\u0221\u0224\u0231\u0233\u023b\u023d\u0242\u0254")
        buf.write("\u0256\u025e\u0260")
        return buf.getvalue()


class RulepadGrammarParser ( Parser ):

    grammarFileName = "RulepadGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\"'", "'||'", "'&&'", "'!'", "'...'", 
                     "'!...'", "'.'", "'='", "'>'", "'<'", "'''", "'&'", 
                     "'|'", "'['", "']'", "'must '", "'of '", "'and '", 
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
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "SPACE", "Alphabet", "NL", 
                      "LPAREN", "RPAREN", "NAME", "VALUE", "ANNOTATION", 
                      "EXTENSION", "SUPERCLASS", "IMPLEMENTATION", "INTERFACE", 
                      "FUNCTION", "CONSTRUCTOR", "PARAMETER", "TYPES", "DeclarationStatement", 
                      "ConfigurationFile", "CONFIGURATION_PROPERTIES", "CLASSES", 
                      "BEAN_DECL" ]

    RULE_inputSentence = 0
    RULE_mustClause = 1
    RULE_words = 2
    RULE_word = 3
    RULE_combinatorialWords = 4
    RULE_symbols = 5
    RULE_end = 6
    RULE_emptyLine = 7
    RULE_comments = 8
    RULE_must = 9
    RULE_of = 10
    RULE_and_ = 11
    RULE_or_ = 12
    RULE_have = 13
    RULE_withWord = 14
    RULE_binary = 15
    RULE_names = 16
    RULE_nameCondition = 17
    RULE_values = 18
    RULE_valueCondition = 19
    RULE_annotations = 20
    RULE_annotationCondition = 21
    RULE_annotationConditionTransition = 22
    RULE_annotationExpression = 23
    RULE_extensions = 24
    RULE_extensionCondition = 25
    RULE_implementations = 26
    RULE_implementationCondition = 27
    RULE_functions = 28
    RULE_functionCondition = 29
    RULE_functionExpression = 30
    RULE_constructors = 31
    RULE_constructorOf = 32
    RULE_constructorCondition = 33
    RULE_constructorExpression = 34
    RULE_parameters = 35
    RULE_parameterCondition = 36
    RULE_parameterConditionTransition = 37
    RULE_parameterExpression = 38
    RULE_functionParameters = 39
    RULE_functionParameterCondition = 40
    RULE_functionParameterConditionTransition = 41
    RULE_functionParameterExpression = 42
    RULE_types = 43
    RULE_typeCondition = 44
    RULE_declarationStatements = 45
    RULE_declarationStatementCondition = 46
    RULE_declarationStatementExpression = 47
    RULE_configurationFiles = 48
    RULE_configurationFileCondition = 49
    RULE_configurationFileExpression = 50
    RULE_configurationProperties = 51
    RULE_configurationPropertyCondition = 52
    RULE_configurationPropertyConditionTransition = 53
    RULE_configurationPropertyExpression = 54
    RULE_classes = 55
    RULE_classCondition = 56
    RULE_classExpression = 57
    RULE_beans = 58

    ruleNames =  [ "inputSentence", "mustClause", "words", "word", "combinatorialWords", 
                   "symbols", "end", "emptyLine", "comments", "must", "of", 
                   "and_", "or_", "have", "withWord", "binary", "names", 
                   "nameCondition", "values", "valueCondition", "annotations", 
                   "annotationCondition", "annotationConditionTransition", 
                   "annotationExpression", "extensions", "extensionCondition", 
                   "implementations", "implementationCondition", "functions", 
                   "functionCondition", "functionExpression", "constructors", 
                   "constructorOf", "constructorCondition", "constructorExpression", 
                   "parameters", "parameterCondition", "parameterConditionTransition", 
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
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    SPACE=22
    Alphabet=23
    NL=24
    LPAREN=25
    RPAREN=26
    NAME=27
    VALUE=28
    ANNOTATION=29
    EXTENSION=30
    SUPERCLASS=31
    IMPLEMENTATION=32
    INTERFACE=33
    FUNCTION=34
    CONSTRUCTOR=35
    PARAMETER=36
    TYPES=37
    DeclarationStatement=38
    ConfigurationFile=39
    CONFIGURATION_PROPERTIES=40
    CLASSES=41
    BEAN_DECL=42

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
            self.state = 125
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.EOF, RulepadGrammarParser.T__6, RulepadGrammarParser.NL]:
                self.state = 121
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 118
                        self.emptyLine() 
                    self.state = 123
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

                pass
            elif token in [RulepadGrammarParser.FUNCTION, RulepadGrammarParser.CONSTRUCTOR, RulepadGrammarParser.DeclarationStatement, RulepadGrammarParser.CLASSES]:
                self.state = 124
                self.mustClause()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RulepadGrammarParser.T__6:
                self.state = 127
                self.end()


            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RulepadGrammarParser.NL:
                self.state = 130
                self.match(RulepadGrammarParser.NL)
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 136
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
            self.state = 158
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.FUNCTION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.functions()
                self.state = 139
                self.must()
                self.state = 140
                self.have()
                self.state = 141
                self.functionExpression(0)
                pass
            elif token in [RulepadGrammarParser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 143
                self.constructors()
                self.state = 144
                self.must()
                self.state = 145
                self.have()
                self.state = 146
                self.constructorExpression(0)
                pass
            elif token in [RulepadGrammarParser.CLASSES]:
                self.enterOuterAlt(localctx, 3)
                self.state = 148
                self.classes()
                self.state = 149
                self.must()
                self.state = 150
                self.have()
                self.state = 151
                self.classExpression(0)
                pass
            elif token in [RulepadGrammarParser.DeclarationStatement]:
                self.enterOuterAlt(localctx, 4)
                self.state = 153
                self.declarationStatements()
                self.state = 154
                self.must()
                self.state = 155
                self.have()
                self.state = 156
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


    class WordsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def word(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RulepadGrammarParser.WordContext)
            else:
                return self.getTypedRuleContext(RulepadGrammarParser.WordContext,i)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_words

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWords" ):
                listener.enterWords(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWords" ):
                listener.exitWords(self)




    def words(self):

        localctx = RulepadGrammarParser.WordsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_words)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(RulepadGrammarParser.T__0)
            self.state = 169
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 167
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        self.state = 161
                        self.word()
                        self.state = 162
                        self.match(RulepadGrammarParser.T__1)
                        pass

                    elif la_ == 2:
                        self.state = 164
                        self.word()
                        self.state = 165
                        self.match(RulepadGrammarParser.T__2)
                        pass

             
                self.state = 171
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 172
            self.word()
            self.state = 173
            self.match(RulepadGrammarParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WordContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Alphabet(self, i:int=None):
            if i is None:
                return self.getTokens(RulepadGrammarParser.Alphabet)
            else:
                return self.getToken(RulepadGrammarParser.Alphabet, i)

        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_word

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWord" ):
                listener.enterWord(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWord" ):
                listener.exitWord(self)




    def word(self):

        localctx = RulepadGrammarParser.WordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_word)
        self._la = 0 # Token type
        try:
            self.state = 225
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 176 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 175
                    self.match(RulepadGrammarParser.Alphabet)
                    self.state = 178 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==RulepadGrammarParser.Alphabet):
                        break

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
                self.match(RulepadGrammarParser.T__3)
                self.state = 182 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 181
                    self.match(RulepadGrammarParser.Alphabet)
                    self.state = 184 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==RulepadGrammarParser.Alphabet):
                        break

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 186
                self.match(RulepadGrammarParser.T__4)
                self.state = 188 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 187
                    self.match(RulepadGrammarParser.Alphabet)
                    self.state = 190 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==RulepadGrammarParser.Alphabet):
                        break

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 192
                self.match(RulepadGrammarParser.T__5)
                self.state = 194 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 193
                    self.match(RulepadGrammarParser.Alphabet)
                    self.state = 196 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==RulepadGrammarParser.Alphabet):
                        break

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 199 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 198
                    self.match(RulepadGrammarParser.Alphabet)
                    self.state = 201 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==RulepadGrammarParser.Alphabet):
                        break

                self.state = 203
                self.match(RulepadGrammarParser.T__4)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 204
                self.match(RulepadGrammarParser.T__3)
                self.state = 206 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 205
                    self.match(RulepadGrammarParser.Alphabet)
                    self.state = 208 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==RulepadGrammarParser.Alphabet):
                        break

                self.state = 210
                self.match(RulepadGrammarParser.T__4)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 211
                self.match(RulepadGrammarParser.T__4)
                self.state = 213 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 212
                    self.match(RulepadGrammarParser.Alphabet)
                    self.state = 215 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==RulepadGrammarParser.Alphabet):
                        break

                self.state = 217
                self.match(RulepadGrammarParser.T__4)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 218
                self.match(RulepadGrammarParser.T__5)
                self.state = 220 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 219
                    self.match(RulepadGrammarParser.Alphabet)
                    self.state = 222 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==RulepadGrammarParser.Alphabet):
                        break

                self.state = 224
                self.match(RulepadGrammarParser.T__4)
                pass


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
        self.enterRule(localctx, 8, self.RULE_combinatorialWords)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.match(RulepadGrammarParser.T__0)
            self.state = 231 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 231
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.Alphabet]:
                    self.state = 228
                    self.match(RulepadGrammarParser.Alphabet)
                    pass
                elif token in [RulepadGrammarParser.T__6, RulepadGrammarParser.T__7, RulepadGrammarParser.T__8, RulepadGrammarParser.T__9, RulepadGrammarParser.T__10, RulepadGrammarParser.T__11, RulepadGrammarParser.T__12, RulepadGrammarParser.T__13, RulepadGrammarParser.T__14, RulepadGrammarParser.LPAREN, RulepadGrammarParser.RPAREN]:
                    self.state = 229
                    self.symbols()
                    pass
                elif token in [RulepadGrammarParser.SPACE]:
                    self.state = 230
                    self.match(RulepadGrammarParser.SPACE)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 233 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RulepadGrammarParser.T__6) | (1 << RulepadGrammarParser.T__7) | (1 << RulepadGrammarParser.T__8) | (1 << RulepadGrammarParser.T__9) | (1 << RulepadGrammarParser.T__10) | (1 << RulepadGrammarParser.T__11) | (1 << RulepadGrammarParser.T__12) | (1 << RulepadGrammarParser.T__13) | (1 << RulepadGrammarParser.T__14) | (1 << RulepadGrammarParser.SPACE) | (1 << RulepadGrammarParser.Alphabet) | (1 << RulepadGrammarParser.LPAREN) | (1 << RulepadGrammarParser.RPAREN))) != 0)):
                    break

            self.state = 235
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
        self.enterRule(localctx, 10, self.RULE_symbols)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RulepadGrammarParser.T__6) | (1 << RulepadGrammarParser.T__7) | (1 << RulepadGrammarParser.T__8) | (1 << RulepadGrammarParser.T__9) | (1 << RulepadGrammarParser.T__10) | (1 << RulepadGrammarParser.T__11) | (1 << RulepadGrammarParser.T__12) | (1 << RulepadGrammarParser.T__13) | (1 << RulepadGrammarParser.T__14) | (1 << RulepadGrammarParser.LPAREN) | (1 << RulepadGrammarParser.RPAREN))) != 0)):
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
        self.enterRule(localctx, 12, self.RULE_end)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(RulepadGrammarParser.T__6)
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
        self.enterRule(localctx, 14, self.RULE_emptyLine)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(RulepadGrammarParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentsContext(ParserRuleContext):

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
            return RulepadGrammarParser.RULE_comments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComments" ):
                listener.enterComments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComments" ):
                listener.exitComments(self)




    def comments(self):

        localctx = RulepadGrammarParser.CommentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_comments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(RulepadGrammarParser.T__0)
            self.state = 247 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 247
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.Alphabet]:
                    self.state = 244
                    self.match(RulepadGrammarParser.Alphabet)
                    pass
                elif token in [RulepadGrammarParser.T__6, RulepadGrammarParser.T__7, RulepadGrammarParser.T__8, RulepadGrammarParser.T__9, RulepadGrammarParser.T__10, RulepadGrammarParser.T__11, RulepadGrammarParser.T__12, RulepadGrammarParser.T__13, RulepadGrammarParser.T__14, RulepadGrammarParser.LPAREN, RulepadGrammarParser.RPAREN]:
                    self.state = 245
                    self.symbols()
                    pass
                elif token in [RulepadGrammarParser.SPACE]:
                    self.state = 246
                    self.match(RulepadGrammarParser.SPACE)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 249 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RulepadGrammarParser.T__6) | (1 << RulepadGrammarParser.T__7) | (1 << RulepadGrammarParser.T__8) | (1 << RulepadGrammarParser.T__9) | (1 << RulepadGrammarParser.T__10) | (1 << RulepadGrammarParser.T__11) | (1 << RulepadGrammarParser.T__12) | (1 << RulepadGrammarParser.T__13) | (1 << RulepadGrammarParser.T__14) | (1 << RulepadGrammarParser.SPACE) | (1 << RulepadGrammarParser.Alphabet) | (1 << RulepadGrammarParser.LPAREN) | (1 << RulepadGrammarParser.RPAREN))) != 0)):
                    break

            self.state = 251
            self.match(RulepadGrammarParser.T__0)
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
        self.enterRule(localctx, 18, self.RULE_must)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(RulepadGrammarParser.T__15)
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
        self.enterRule(localctx, 20, self.RULE_of)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.match(RulepadGrammarParser.T__16)
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
        self.enterRule(localctx, 22, self.RULE_and_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(RulepadGrammarParser.T__17)
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
        self.enterRule(localctx, 24, self.RULE_or_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(RulepadGrammarParser.T__18)
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
        self.enterRule(localctx, 26, self.RULE_have)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(RulepadGrammarParser.T__19)
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
        self.enterRule(localctx, 28, self.RULE_withWord)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.match(RulepadGrammarParser.T__20)
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
        self.enterRule(localctx, 30, self.RULE_binary)
        try:
            self.state = 267
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.T__17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.and_()
                pass
            elif token in [RulepadGrammarParser.T__18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 266
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
        self.enterRule(localctx, 32, self.RULE_names)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(RulepadGrammarParser.NAME)
            self.state = 271
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 270
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

        def words(self):
            return self.getTypedRuleContext(RulepadGrammarParser.WordsContext,0)


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
        self.enterRule(localctx, 34, self.RULE_nameCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.words()
            self.state = 274
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
        self.enterRule(localctx, 36, self.RULE_values)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(RulepadGrammarParser.VALUE)
            self.state = 277
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

        def words(self):
            return self.getTypedRuleContext(RulepadGrammarParser.WordsContext,0)


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
        self.enterRule(localctx, 38, self.RULE_valueCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.words()
            self.state = 280
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
        self.enterRule(localctx, 40, self.RULE_annotations)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.match(RulepadGrammarParser.ANNOTATION)
            self.state = 284
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 283
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
        self.enterRule(localctx, 42, self.RULE_annotationCondition)
        try:
            self.state = 292
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 286
                self.combinatorialWords()
                self.state = 287
                self.match(RulepadGrammarParser.SPACE)
                self.state = 289
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                if la_ == 1:
                    self.state = 288
                    self.annotationConditionTransition()


                pass
            elif token in [RulepadGrammarParser.T__20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 291
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
        self.enterRule(localctx, 44, self.RULE_annotationConditionTransition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.withWord()
            self.state = 295
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
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_annotationExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 298
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 299
                self.annotationExpression(0)
                self.state = 300
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.PARAMETER]:
                self.state = 302
                self.parameters()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 313
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 311
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.AnnotationExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_annotationExpression)
                        self.state = 305
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 306
                        localctx.op = self.binary()
                        self.state = 307
                        localctx.right = self.annotationExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.AnnotationExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_annotationExpression)
                        self.state = 309
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 310
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 315
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

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
        self.enterRule(localctx, 48, self.RULE_extensions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.match(RulepadGrammarParser.EXTENSION)
            self.state = 317
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
        self.enterRule(localctx, 50, self.RULE_extensionCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.of()
            self.state = 324
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.T__0]:
                self.state = 320
                self.combinatorialWords()
                self.state = 321
                self.match(RulepadGrammarParser.SPACE)
                pass
            elif token in [RulepadGrammarParser.SUPERCLASS]:
                self.state = 323
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
        self.enterRule(localctx, 52, self.RULE_implementations)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.match(RulepadGrammarParser.IMPLEMENTATION)
            self.state = 327
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
        self.enterRule(localctx, 54, self.RULE_implementationCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.of()
            self.state = 334
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.T__0]:
                self.state = 330
                self.combinatorialWords()
                self.state = 331
                self.match(RulepadGrammarParser.SPACE)
                pass
            elif token in [RulepadGrammarParser.INTERFACE]:
                self.state = 333
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
        self.enterRule(localctx, 56, self.RULE_functions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.match(RulepadGrammarParser.FUNCTION)
            self.state = 337
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
        self.enterRule(localctx, 58, self.RULE_functionCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.withWord()
            self.state = 340
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
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_functionExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 343
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 344
                self.functionExpression(0)
                self.state = 345
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.ANNOTATION, RulepadGrammarParser.PARAMETER, RulepadGrammarParser.TYPES]:
                self.state = 350
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.ANNOTATION]:
                    self.state = 347
                    self.annotations()
                    pass
                elif token in [RulepadGrammarParser.TYPES]:
                    self.state = 348
                    self.types()
                    pass
                elif token in [RulepadGrammarParser.PARAMETER]:
                    self.state = 349
                    self.functionParameters()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 362
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 360
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.FunctionExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_functionExpression)
                        self.state = 354
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 355
                        localctx.op = self.binary()
                        self.state = 356
                        localctx.right = self.functionExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.FunctionExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_functionExpression)
                        self.state = 358
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 359
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 364
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

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
        self.enterRule(localctx, 62, self.RULE_constructors)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.match(RulepadGrammarParser.CONSTRUCTOR)
            self.state = 366
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
        self.enterRule(localctx, 64, self.RULE_constructorOf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            self.of()
            self.state = 369
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
        self.enterRule(localctx, 66, self.RULE_constructorCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.withWord()
            self.state = 372
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
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_constructorExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 375
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 376
                self.constructorExpression(0)
                self.state = 377
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.ANNOTATION, RulepadGrammarParser.PARAMETER]:
                self.state = 381
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.ANNOTATION]:
                    self.state = 379
                    self.annotations()
                    pass
                elif token in [RulepadGrammarParser.PARAMETER]:
                    self.state = 380
                    self.functionParameters()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 393
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 391
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.ConstructorExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_constructorExpression)
                        self.state = 385
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 386
                        localctx.op = self.binary()
                        self.state = 387
                        localctx.right = self.constructorExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.ConstructorExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_constructorExpression)
                        self.state = 389
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 390
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 395
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

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
        self.enterRule(localctx, 70, self.RULE_parameters)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            self.match(RulepadGrammarParser.PARAMETER)
            self.state = 397
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
        self.enterRule(localctx, 72, self.RULE_parameterCondition)
        try:
            self.state = 405
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 399
                self.combinatorialWords()
                self.state = 400
                self.match(RulepadGrammarParser.SPACE)
                self.state = 402
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
                if la_ == 1:
                    self.state = 401
                    self.parameterConditionTransition()


                pass
            elif token in [RulepadGrammarParser.T__20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 404
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
        self.enterRule(localctx, 74, self.RULE_parameterConditionTransition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.withWord()
            self.state = 408
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
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_parameterExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 411
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 412
                self.parameterExpression(0)
                self.state = 413
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.NAME, RulepadGrammarParser.VALUE, RulepadGrammarParser.TYPES]:
                self.state = 418
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.TYPES]:
                    self.state = 415
                    self.types()
                    pass
                elif token in [RulepadGrammarParser.NAME]:
                    self.state = 416
                    self.names()
                    pass
                elif token in [RulepadGrammarParser.VALUE]:
                    self.state = 417
                    self.values()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 430
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 428
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.ParameterExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_parameterExpression)
                        self.state = 422
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 423
                        localctx.op = self.binary()
                        self.state = 424
                        localctx.right = self.parameterExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.ParameterExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_parameterExpression)
                        self.state = 426
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 427
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 432
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

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
        self.enterRule(localctx, 78, self.RULE_functionParameters)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 433
            self.match(RulepadGrammarParser.PARAMETER)
            self.state = 435
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.state = 434
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
        self.enterRule(localctx, 80, self.RULE_functionParameterCondition)
        try:
            self.state = 443
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 437
                self.combinatorialWords()
                self.state = 438
                self.match(RulepadGrammarParser.SPACE)
                self.state = 440
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
                if la_ == 1:
                    self.state = 439
                    self.functionParameterConditionTransition()


                pass
            elif token in [RulepadGrammarParser.T__20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 442
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
        self.enterRule(localctx, 82, self.RULE_functionParameterConditionTransition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            self.withWord()
            self.state = 446
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
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_functionParameterExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 458
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 449
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 450
                self.functionParameterExpression(0)
                self.state = 451
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.NAME, RulepadGrammarParser.ANNOTATION, RulepadGrammarParser.TYPES]:
                self.state = 456
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.TYPES]:
                    self.state = 453
                    self.types()
                    pass
                elif token in [RulepadGrammarParser.NAME]:
                    self.state = 454
                    self.names()
                    pass
                elif token in [RulepadGrammarParser.ANNOTATION]:
                    self.state = 455
                    self.annotations()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 468
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,50,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 466
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.FunctionParameterExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_functionParameterExpression)
                        self.state = 460
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 461
                        localctx.op = self.binary()
                        self.state = 462
                        localctx.right = self.functionParameterExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.FunctionParameterExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_functionParameterExpression)
                        self.state = 464
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 465
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 470
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,50,self._ctx)

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
        self.enterRule(localctx, 86, self.RULE_types)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            self.match(RulepadGrammarParser.TYPES)
            self.state = 473
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.state = 472
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

        def words(self):
            return self.getTypedRuleContext(RulepadGrammarParser.WordsContext,0)


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
        self.enterRule(localctx, 88, self.RULE_typeCondition)
        try:
            self.state = 481
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 475
                self.combinatorialWords()
                self.state = 476
                self.match(RulepadGrammarParser.SPACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 478
                self.words()
                self.state = 479
                self.match(RulepadGrammarParser.SPACE)
                pass


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
        self.enterRule(localctx, 90, self.RULE_declarationStatements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 483
            self.match(RulepadGrammarParser.DeclarationStatement)
            self.state = 484
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
        self.enterRule(localctx, 92, self.RULE_declarationStatementCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 486
            self.withWord()
            self.state = 487
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
        _startState = 94
        self.enterRecursionRule(localctx, 94, self.RULE_declarationStatementExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 490
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 491
                self.declarationStatementExpression(0)
                self.state = 492
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.ANNOTATION, RulepadGrammarParser.TYPES]:
                self.state = 496
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.ANNOTATION]:
                    self.state = 494
                    self.annotations()
                    pass
                elif token in [RulepadGrammarParser.TYPES]:
                    self.state = 495
                    self.types()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 508
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,56,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 506
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.DeclarationStatementExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_declarationStatementExpression)
                        self.state = 500
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 501
                        localctx.op = self.binary()
                        self.state = 502
                        localctx.right = self.declarationStatementExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.DeclarationStatementExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_declarationStatementExpression)
                        self.state = 504
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 505
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 510
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,56,self._ctx)

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
        self.enterRule(localctx, 96, self.RULE_configurationFiles)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 511
            self.match(RulepadGrammarParser.ConfigurationFile)
            self.state = 513
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.state = 512
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
        self.enterRule(localctx, 98, self.RULE_configurationFileCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 515
            self.withWord()
            self.state = 516
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
        _startState = 100
        self.enterRecursionRule(localctx, 100, self.RULE_configurationFileExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 524
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 519
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 520
                self.configurationFileExpression(0)
                self.state = 521
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.CONFIGURATION_PROPERTIES]:
                self.state = 523
                self.configurationProperties()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 534
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,60,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 532
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.ConfigurationFileExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_configurationFileExpression)
                        self.state = 526
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 527
                        localctx.op = self.binary()
                        self.state = 528
                        localctx.right = self.configurationFileExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.ConfigurationFileExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_configurationFileExpression)
                        self.state = 530
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 531
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 536
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,60,self._ctx)

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
        self.enterRule(localctx, 102, self.RULE_configurationProperties)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 537
            self.match(RulepadGrammarParser.CONFIGURATION_PROPERTIES)
            self.state = 538
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
        self.enterRule(localctx, 104, self.RULE_configurationPropertyCondition)
        try:
            self.state = 546
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 540
                self.combinatorialWords()
                self.state = 541
                self.match(RulepadGrammarParser.SPACE)
                self.state = 543
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
                if la_ == 1:
                    self.state = 542
                    self.configurationPropertyConditionTransition()


                pass
            elif token in [RulepadGrammarParser.T__20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 545
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
        self.enterRule(localctx, 106, self.RULE_configurationPropertyConditionTransition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 548
            self.withWord()
            self.state = 549
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
        _startState = 108
        self.enterRecursionRule(localctx, 108, self.RULE_configurationPropertyExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 561
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 552
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 553
                self.configurationPropertyExpression(0)
                self.state = 554
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.NAME, RulepadGrammarParser.VALUE, RulepadGrammarParser.TYPES]:
                self.state = 559
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.TYPES]:
                    self.state = 556
                    self.types()
                    pass
                elif token in [RulepadGrammarParser.NAME]:
                    self.state = 557
                    self.names()
                    pass
                elif token in [RulepadGrammarParser.VALUE]:
                    self.state = 558
                    self.values()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 571
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,66,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 569
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.ConfigurationPropertyExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_configurationPropertyExpression)
                        self.state = 563
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 564
                        localctx.op = self.binary()
                        self.state = 565
                        localctx.right = self.configurationPropertyExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.ConfigurationPropertyExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_configurationPropertyExpression)
                        self.state = 567
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 568
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 573
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,66,self._ctx)

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
        self.enterRule(localctx, 110, self.RULE_classes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 574
            self.match(RulepadGrammarParser.CLASSES)
            self.state = 576
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RulepadGrammarParser.T__20:
                self.state = 575
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
        self.enterRule(localctx, 112, self.RULE_classCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 578
            self.withWord()
            self.state = 579
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
        _startState = 114
        self.enterRecursionRule(localctx, 114, self.RULE_classExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 596
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 582
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 583
                self.classExpression(0)
                self.state = 584
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.ANNOTATION, RulepadGrammarParser.EXTENSION, RulepadGrammarParser.IMPLEMENTATION, RulepadGrammarParser.FUNCTION, RulepadGrammarParser.CONSTRUCTOR, RulepadGrammarParser.DeclarationStatement, RulepadGrammarParser.ConfigurationFile, RulepadGrammarParser.BEAN_DECL]:
                self.state = 594
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.ANNOTATION]:
                    self.state = 586
                    self.annotations()
                    pass
                elif token in [RulepadGrammarParser.EXTENSION]:
                    self.state = 587
                    self.extensions()
                    pass
                elif token in [RulepadGrammarParser.IMPLEMENTATION]:
                    self.state = 588
                    self.implementations()
                    pass
                elif token in [RulepadGrammarParser.FUNCTION]:
                    self.state = 589
                    self.functions()
                    pass
                elif token in [RulepadGrammarParser.CONSTRUCTOR]:
                    self.state = 590
                    self.constructors()
                    pass
                elif token in [RulepadGrammarParser.DeclarationStatement]:
                    self.state = 591
                    self.declarationStatements()
                    pass
                elif token in [RulepadGrammarParser.ConfigurationFile]:
                    self.state = 592
                    self.configurationFiles()
                    pass
                elif token in [RulepadGrammarParser.BEAN_DECL]:
                    self.state = 593
                    self.beans()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 606
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,71,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 604
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,70,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.ClassExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_classExpression)
                        self.state = 598
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 599
                        localctx.op = self.binary()
                        self.state = 600
                        localctx.right = self.classExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.ClassExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_classExpression)
                        self.state = 602
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 603
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 608
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,71,self._ctx)

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
        self.enterRule(localctx, 116, self.RULE_beans)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 609
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
        self._predicates[23] = self.annotationExpression_sempred
        self._predicates[30] = self.functionExpression_sempred
        self._predicates[34] = self.constructorExpression_sempred
        self._predicates[38] = self.parameterExpression_sempred
        self._predicates[42] = self.functionParameterExpression_sempred
        self._predicates[47] = self.declarationStatementExpression_sempred
        self._predicates[50] = self.configurationFileExpression_sempred
        self._predicates[54] = self.configurationPropertyExpression_sempred
        self._predicates[57] = self.classExpression_sempred
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
         




