# Generated from RulepadGrammar.g4 by ANTLR 4.9.2
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
        buf.write("\u02c6\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\3\2\7\2\u008a\n\2\f\2\16\2\u008d\13\2\3\2\5\2\u0090")
        buf.write("\n\2\3\2\5\2\u0093\n\2\3\2\7\2\u0096\n\2\f\2\16\2\u0099")
        buf.write("\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u00c0")
        buf.write("\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4\u00c9\n\4\f\4\16")
        buf.write("\4\u00cc\13\4\3\4\3\4\3\4\3\5\6\5\u00d2\n\5\r\5\16\5\u00d3")
        buf.write("\3\5\3\5\6\5\u00d8\n\5\r\5\16\5\u00d9\3\5\3\5\6\5\u00de")
        buf.write("\n\5\r\5\16\5\u00df\3\5\3\5\6\5\u00e4\n\5\r\5\16\5\u00e5")
        buf.write("\3\5\6\5\u00e9\n\5\r\5\16\5\u00ea\3\5\3\5\3\5\6\5\u00f0")
        buf.write("\n\5\r\5\16\5\u00f1\3\5\3\5\3\5\6\5\u00f7\n\5\r\5\16\5")
        buf.write("\u00f8\3\5\3\5\3\5\6\5\u00fe\n\5\r\5\16\5\u00ff\3\5\5")
        buf.write("\5\u0103\n\5\3\6\3\6\3\6\3\6\6\6\u0109\n\6\r\6\16\6\u010a")
        buf.write("\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\6\n\u0119")
        buf.write("\n\n\r\n\16\n\u011a\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r")
        buf.write("\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\5\21\u012d\n")
        buf.write("\21\3\22\3\22\5\22\u0131\n\22\3\23\3\23\3\23\3\24\3\24")
        buf.write("\5\24\u0138\n\24\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3")
        buf.write("\27\3\27\3\27\3\27\5\27\u0145\n\27\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\31\3\31\5\31\u014f\n\31\3\32\3\32\5\32\u0153")
        buf.write("\n\32\3\32\5\32\u0156\n\32\3\33\3\33\3\33\3\34\3\34\3")
        buf.write("\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\5\35\u016d\n\35\5\35\u016f\n")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\3\35\7\35\u0177\n\35\f\35")
        buf.write("\16\35\u017a\13\35\3\36\3\36\5\36\u017e\n\36\3\36\5\36")
        buf.write("\u0181\n\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3!\3!\3!")
        buf.write("\3!\3!\3!\3!\3!\5!\u0194\n!\5!\u0196\n!\3!\3!\3!\3!\3")
        buf.write("!\3!\7!\u019e\n!\f!\16!\u01a1\13!\3\"\3\"\5\"\u01a5\n")
        buf.write("\"\3\"\5\"\u01a8\n\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3%\3%")
        buf.write("\3%\3%\3%\3%\3%\3%\3%\3%\5%\u01bd\n%\5%\u01bf\n%\3%\3")
        buf.write("%\3%\3%\3%\3%\7%\u01c7\n%\f%\16%\u01ca\13%\3&\3&\5&\u01ce")
        buf.write("\n&\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\5(\u01da\n(\5(\u01dc")
        buf.write("\n(\3(\3(\3(\3(\3(\3(\7(\u01e4\n(\f(\16(\u01e7\13(\3)")
        buf.write("\3)\5)\u01eb\n)\3*\3*\3*\3*\3*\3*\5*\u01f3\n*\3+\3+\5")
        buf.write("+\u01f7\n+\3,\3,\3,\3-\3-\5-\u01fe\n-\3.\3.\3.\3/\3/\5")
        buf.write("/\u0205\n/\3\60\3\60\3\60\3\61\3\61\5\61\u020c\n\61\3")
        buf.write("\61\5\61\u020f\n\61\3\62\3\62\3\62\3\62\5\62\u0215\n\62")
        buf.write("\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\5\64\u0226\n\64\5\64\u0228\n\64\3")
        buf.write("\64\3\64\3\64\3\64\3\64\3\64\7\64\u0230\n\64\f\64\16\64")
        buf.write("\u0233\13\64\3\65\3\65\5\65\u0237\n\65\3\65\5\65\u023a")
        buf.write("\n\65\3\66\3\66\3\66\3\66\5\66\u0240\n\66\3\67\3\67\3")
        buf.write("\67\38\38\38\38\38\38\38\58\u024c\n8\58\u024e\n8\38\3")
        buf.write("8\38\38\38\38\78\u0256\n8\f8\168\u0259\138\39\39\59\u025d")
        buf.write("\n9\3:\3:\3:\3;\3;\5;\u0264\n;\3;\5;\u0267\n;\3<\3<\3")
        buf.write("<\3=\3=\3=\3>\3>\5>\u0271\n>\3?\3?\3?\3@\3@\3@\3@\3@\3")
        buf.write("@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\5@\u0288\n@\5@\u028a")
        buf.write("\n@\3@\3@\3@\3@\3@\3@\7@\u0292\n@\f@\16@\u0295\13@\3A")
        buf.write("\3A\5A\u0299\nA\3A\5A\u029c\nA\3B\3B\3B\3C\3C\3C\3D\3")
        buf.write("D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\5")
        buf.write("D\u02b7\nD\5D\u02b9\nD\3D\3D\3D\3D\3D\3D\7D\u02c1\nD\f")
        buf.write("D\16D\u02c4\13D\3D\2\n8@HNfn~\u0086E\2\4\6\b\n\f\16\20")
        buf.write("\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJL")
        buf.write("NPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086\2\3")
        buf.write("\4\2\t\16\30\31\2\u0310\2\u008f\3\2\2\2\4\u00bf\3\2\2")
        buf.write("\2\6\u00c1\3\2\2\2\b\u0102\3\2\2\2\n\u0104\3\2\2\2\f\u010e")
        buf.write("\3\2\2\2\16\u0110\3\2\2\2\20\u0112\3\2\2\2\22\u0114\3")
        buf.write("\2\2\2\24\u011e\3\2\2\2\26\u0120\3\2\2\2\30\u0122\3\2")
        buf.write("\2\2\32\u0124\3\2\2\2\34\u0126\3\2\2\2\36\u0128\3\2\2")
        buf.write("\2 \u012c\3\2\2\2\"\u012e\3\2\2\2$\u0132\3\2\2\2&\u0135")
        buf.write("\3\2\2\2(\u0139\3\2\2\2*\u013c\3\2\2\2,\u013f\3\2\2\2")
        buf.write(".\u0146\3\2\2\2\60\u0149\3\2\2\2\62\u0150\3\2\2\2\64\u0157")
        buf.write("\3\2\2\2\66\u015a\3\2\2\28\u016e\3\2\2\2:\u017b\3\2\2")
        buf.write("\2<\u0182\3\2\2\2>\u0185\3\2\2\2@\u0195\3\2\2\2B\u01a2")
        buf.write("\3\2\2\2D\u01a9\3\2\2\2F\u01ac\3\2\2\2H\u01be\3\2\2\2")
        buf.write("J\u01cb\3\2\2\2L\u01cf\3\2\2\2N\u01db\3\2\2\2P\u01e8\3")
        buf.write("\2\2\2R\u01f2\3\2\2\2T\u01f4\3\2\2\2V\u01f8\3\2\2\2X\u01fb")
        buf.write("\3\2\2\2Z\u01ff\3\2\2\2\\\u0202\3\2\2\2^\u0206\3\2\2\2")
        buf.write("`\u0209\3\2\2\2b\u0210\3\2\2\2d\u0216\3\2\2\2f\u0227\3")
        buf.write("\2\2\2h\u0234\3\2\2\2j\u023b\3\2\2\2l\u0241\3\2\2\2n\u024d")
        buf.write("\3\2\2\2p\u025a\3\2\2\2r\u025e\3\2\2\2t\u0261\3\2\2\2")
        buf.write("v\u0268\3\2\2\2x\u026b\3\2\2\2z\u026e\3\2\2\2|\u0272\3")
        buf.write("\2\2\2~\u0289\3\2\2\2\u0080\u0296\3\2\2\2\u0082\u029d")
        buf.write("\3\2\2\2\u0084\u02a0\3\2\2\2\u0086\u02b8\3\2\2\2\u0088")
        buf.write("\u008a\5\20\t\2\u0089\u0088\3\2\2\2\u008a\u008d\3\2\2")
        buf.write("\2\u008b\u0089\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u0090")
        buf.write("\3\2\2\2\u008d\u008b\3\2\2\2\u008e\u0090\5\4\3\2\u008f")
        buf.write("\u008b\3\2\2\2\u008f\u008e\3\2\2\2\u0090\u0092\3\2\2\2")
        buf.write("\u0091\u0093\5\16\b\2\u0092\u0091\3\2\2\2\u0092\u0093")
        buf.write("\3\2\2\2\u0093\u0097\3\2\2\2\u0094\u0096\7\27\2\2\u0095")
        buf.write("\u0094\3\2\2\2\u0096\u0099\3\2\2\2\u0097\u0095\3\2\2\2")
        buf.write("\u0097\u0098\3\2\2\2\u0098\u009a\3\2\2\2\u0099\u0097\3")
        buf.write("\2\2\2\u009a\u009b\7\2\2\3\u009b\3\3\2\2\2\u009c\u009d")
        buf.write("\5\62\32\2\u009d\u009e\5\24\13\2\u009e\u009f\5\34\17\2")
        buf.write("\u009f\u00a0\58\35\2\u00a0\u00c0\3\2\2\2\u00a1\u00a2\5")
        buf.write(":\36\2\u00a2\u00a3\5\24\13\2\u00a3\u00a4\5\34\17\2\u00a4")
        buf.write("\u00a5\5@!\2\u00a5\u00c0\3\2\2\2\u00a6\u00a7\5B\"\2\u00a7")
        buf.write("\u00a8\5\24\13\2\u00a8\u00a9\5\34\17\2\u00a9\u00aa\5H")
        buf.write("%\2\u00aa\u00c0\3\2\2\2\u00ab\u00ac\5z>\2\u00ac\u00ad")
        buf.write("\5\24\13\2\u00ad\u00ae\5\34\17\2\u00ae\u00af\5~@\2\u00af")
        buf.write("\u00c0\3\2\2\2\u00b0\u00b1\5J&\2\u00b1\u00b2\5\24\13\2")
        buf.write("\u00b2\u00b3\5\34\17\2\u00b3\u00b4\5N(\2\u00b4\u00c0\3")
        buf.write("\2\2\2\u00b5\u00b6\5`\61\2\u00b6\u00b7\5\24\13\2\u00b7")
        buf.write("\u00b8\5\34\17\2\u00b8\u00b9\5f\64\2\u00b9\u00c0\3\2\2")
        buf.write("\2\u00ba\u00bb\5\u0080A\2\u00bb\u00bc\5\24\13\2\u00bc")
        buf.write("\u00bd\5\34\17\2\u00bd\u00be\5\u0086D\2\u00be\u00c0\3")
        buf.write("\2\2\2\u00bf\u009c\3\2\2\2\u00bf\u00a1\3\2\2\2\u00bf\u00a6")
        buf.write("\3\2\2\2\u00bf\u00ab\3\2\2\2\u00bf\u00b0\3\2\2\2\u00bf")
        buf.write("\u00b5\3\2\2\2\u00bf\u00ba\3\2\2\2\u00c0\5\3\2\2\2\u00c1")
        buf.write("\u00ca\7\3\2\2\u00c2\u00c3\5\b\5\2\u00c3\u00c4\7\4\2\2")
        buf.write("\u00c4\u00c9\3\2\2\2\u00c5\u00c6\5\b\5\2\u00c6\u00c7\7")
        buf.write("\5\2\2\u00c7\u00c9\3\2\2\2\u00c8\u00c2\3\2\2\2\u00c8\u00c5")
        buf.write("\3\2\2\2\u00c9\u00cc\3\2\2\2\u00ca\u00c8\3\2\2\2\u00ca")
        buf.write("\u00cb\3\2\2\2\u00cb\u00cd\3\2\2\2\u00cc\u00ca\3\2\2\2")
        buf.write("\u00cd\u00ce\5\b\5\2\u00ce\u00cf\7\3\2\2\u00cf\7\3\2\2")
        buf.write("\2\u00d0\u00d2\7\26\2\2\u00d1\u00d0\3\2\2\2\u00d2\u00d3")
        buf.write("\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4")
        buf.write("\u0103\3\2\2\2\u00d5\u00d7\7\6\2\2\u00d6\u00d8\7\26\2")
        buf.write("\2\u00d7\u00d6\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9\u00d7")
        buf.write("\3\2\2\2\u00d9\u00da\3\2\2\2\u00da\u0103\3\2\2\2\u00db")
        buf.write("\u00dd\7\7\2\2\u00dc\u00de\7\26\2\2\u00dd\u00dc\3\2\2")
        buf.write("\2\u00de\u00df\3\2\2\2\u00df\u00dd\3\2\2\2\u00df\u00e0")
        buf.write("\3\2\2\2\u00e0\u0103\3\2\2\2\u00e1\u00e3\7\b\2\2\u00e2")
        buf.write("\u00e4\7\26\2\2\u00e3\u00e2\3\2\2\2\u00e4\u00e5\3\2\2")
        buf.write("\2\u00e5\u00e3\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\u0103")
        buf.write("\3\2\2\2\u00e7\u00e9\7\26\2\2\u00e8\u00e7\3\2\2\2\u00e9")
        buf.write("\u00ea\3\2\2\2\u00ea\u00e8\3\2\2\2\u00ea\u00eb\3\2\2\2")
        buf.write("\u00eb\u00ec\3\2\2\2\u00ec\u0103\7\7\2\2\u00ed\u00ef\7")
        buf.write("\6\2\2\u00ee\u00f0\7\26\2\2\u00ef\u00ee\3\2\2\2\u00f0")
        buf.write("\u00f1\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f1\u00f2\3\2\2\2")
        buf.write("\u00f2\u00f3\3\2\2\2\u00f3\u0103\7\7\2\2\u00f4\u00f6\7")
        buf.write("\7\2\2\u00f5\u00f7\7\26\2\2\u00f6\u00f5\3\2\2\2\u00f7")
        buf.write("\u00f8\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f8\u00f9\3\2\2\2")
        buf.write("\u00f9\u00fa\3\2\2\2\u00fa\u0103\7\7\2\2\u00fb\u00fd\7")
        buf.write("\b\2\2\u00fc\u00fe\7\26\2\2\u00fd\u00fc\3\2\2\2\u00fe")
        buf.write("\u00ff\3\2\2\2\u00ff\u00fd\3\2\2\2\u00ff\u0100\3\2\2\2")
        buf.write("\u0100\u0101\3\2\2\2\u0101\u0103\7\7\2\2\u0102\u00d1\3")
        buf.write("\2\2\2\u0102\u00d5\3\2\2\2\u0102\u00db\3\2\2\2\u0102\u00e1")
        buf.write("\3\2\2\2\u0102\u00e8\3\2\2\2\u0102\u00ed\3\2\2\2\u0102")
        buf.write("\u00f4\3\2\2\2\u0102\u00fb\3\2\2\2\u0103\t\3\2\2\2\u0104")
        buf.write("\u0108\7\3\2\2\u0105\u0109\7\26\2\2\u0106\u0109\5\f\7")
        buf.write("\2\u0107\u0109\7\25\2\2\u0108\u0105\3\2\2\2\u0108\u0106")
        buf.write("\3\2\2\2\u0108\u0107\3\2\2\2\u0109\u010a\3\2\2\2\u010a")
        buf.write("\u0108\3\2\2\2\u010a\u010b\3\2\2\2\u010b\u010c\3\2\2\2")
        buf.write("\u010c\u010d\7\3\2\2\u010d\13\3\2\2\2\u010e\u010f\t\2")
        buf.write("\2\2\u010f\r\3\2\2\2\u0110\u0111\7\t\2\2\u0111\17\3\2")
        buf.write("\2\2\u0112\u0113\7\27\2\2\u0113\21\3\2\2\2\u0114\u0118")
        buf.write("\7\3\2\2\u0115\u0119\7\26\2\2\u0116\u0119\5\f\7\2\u0117")
        buf.write("\u0119\7\25\2\2\u0118\u0115\3\2\2\2\u0118\u0116\3\2\2")
        buf.write("\2\u0118\u0117\3\2\2\2\u0119\u011a\3\2\2\2\u011a\u0118")
        buf.write("\3\2\2\2\u011a\u011b\3\2\2\2\u011b\u011c\3\2\2\2\u011c")
        buf.write("\u011d\7\3\2\2\u011d\23\3\2\2\2\u011e\u011f\7\17\2\2\u011f")
        buf.write("\25\3\2\2\2\u0120\u0121\7\20\2\2\u0121\27\3\2\2\2\u0122")
        buf.write("\u0123\7\21\2\2\u0123\31\3\2\2\2\u0124\u0125\7\22\2\2")
        buf.write("\u0125\33\3\2\2\2\u0126\u0127\7\23\2\2\u0127\35\3\2\2")
        buf.write("\2\u0128\u0129\7\24\2\2\u0129\37\3\2\2\2\u012a\u012d\5")
        buf.write("\30\r\2\u012b\u012d\5\32\16\2\u012c\u012a\3\2\2\2\u012c")
        buf.write("\u012b\3\2\2\2\u012d!\3\2\2\2\u012e\u0130\7\32\2\2\u012f")
        buf.write("\u0131\5$\23\2\u0130\u012f\3\2\2\2\u0130\u0131\3\2\2\2")
        buf.write("\u0131#\3\2\2\2\u0132\u0133\5\6\4\2\u0133\u0134\7\25\2")
        buf.write("\2\u0134%\3\2\2\2\u0135\u0137\7\33\2\2\u0136\u0138\5(")
        buf.write("\25\2\u0137\u0136\3\2\2\2\u0137\u0138\3\2\2\2\u0138\'")
        buf.write("\3\2\2\2\u0139\u013a\5\n\6\2\u013a\u013b\7\25\2\2\u013b")
        buf.write(")\3\2\2\2\u013c\u013d\7\34\2\2\u013d\u013e\5,\27\2\u013e")
        buf.write("+\3\2\2\2\u013f\u0144\5\26\f\2\u0140\u0141\5\6\4\2\u0141")
        buf.write("\u0142\7\25\2\2\u0142\u0145\3\2\2\2\u0143\u0145\7\35\2")
        buf.write("\2\u0144\u0140\3\2\2\2\u0144\u0143\3\2\2\2\u0145-\3\2")
        buf.write("\2\2\u0146\u0147\7\36\2\2\u0147\u0148\5\60\31\2\u0148")
        buf.write("/\3\2\2\2\u0149\u014e\5\26\f\2\u014a\u014b\5\6\4\2\u014b")
        buf.write("\u014c\7\25\2\2\u014c\u014f\3\2\2\2\u014d\u014f\7\37\2")
        buf.write("\2\u014e\u014a\3\2\2\2\u014e\u014d\3\2\2\2\u014f\61\3")
        buf.write("\2\2\2\u0150\u0152\7 \2\2\u0151\u0153\5\66\34\2\u0152")
        buf.write("\u0151\3\2\2\2\u0152\u0153\3\2\2\2\u0153\u0155\3\2\2\2")
        buf.write("\u0154\u0156\5\64\33\2\u0155\u0154\3\2\2\2\u0155\u0156")
        buf.write("\3\2\2\2\u0156\63\3\2\2\2\u0157\u0158\5\26\f\2\u0158\u0159")
        buf.write("\5z>\2\u0159\65\3\2\2\2\u015a\u015b\5\36\20\2\u015b\u015c")
        buf.write("\58\35\2\u015c\67\3\2\2\2\u015d\u015e\b\35\1\2\u015e\u015f")
        buf.write("\7\30\2\2\u015f\u0160\58\35\2\u0160\u0161\7\31\2\2\u0161")
        buf.write("\u016f\3\2\2\2\u0162\u016d\5&\24\2\u0163\u016d\5T+\2\u0164")
        buf.write("\u016d\5X-\2\u0165\u016d\5P)\2\u0166\u016d\5\"\22\2\u0167")
        buf.write("\u016d\5J&\2\u0168\u016d\5\\/\2\u0169\u016d\5`\61\2\u016a")
        buf.write("\u016d\5h\65\2\u016b\u016d\5\22\n\2\u016c\u0162\3\2\2")
        buf.write("\2\u016c\u0163\3\2\2\2\u016c\u0164\3\2\2\2\u016c\u0165")
        buf.write("\3\2\2\2\u016c\u0166\3\2\2\2\u016c\u0167\3\2\2\2\u016c")
        buf.write("\u0168\3\2\2\2\u016c\u0169\3\2\2\2\u016c\u016a\3\2\2\2")
        buf.write("\u016c\u016b\3\2\2\2\u016d\u016f\3\2\2\2\u016e\u015d\3")
        buf.write("\2\2\2\u016e\u016c\3\2\2\2\u016f\u0178\3\2\2\2\u0170\u0171")
        buf.write("\f\5\2\2\u0171\u0172\5 \21\2\u0172\u0173\58\35\6\u0173")
        buf.write("\u0177\3\2\2\2\u0174\u0175\f\3\2\2\u0175\u0177\7\25\2")
        buf.write("\2\u0176\u0170\3\2\2\2\u0176\u0174\3\2\2\2\u0177\u017a")
        buf.write("\3\2\2\2\u0178\u0176\3\2\2\2\u0178\u0179\3\2\2\2\u0179")
        buf.write("9\3\2\2\2\u017a\u0178\3\2\2\2\u017b\u017d\7!\2\2\u017c")
        buf.write("\u017e\5> \2\u017d\u017c\3\2\2\2\u017d\u017e\3\2\2\2\u017e")
        buf.write("\u0180\3\2\2\2\u017f\u0181\5<\37\2\u0180\u017f\3\2\2\2")
        buf.write("\u0180\u0181\3\2\2\2\u0181;\3\2\2\2\u0182\u0183\5\26\f")
        buf.write("\2\u0183\u0184\5z>\2\u0184=\3\2\2\2\u0185\u0186\5\36\20")
        buf.write("\2\u0186\u0187\5@!\2\u0187?\3\2\2\2\u0188\u0189\b!\1\2")
        buf.write("\u0189\u018a\7\30\2\2\u018a\u018b\5@!\2\u018b\u018c\7")
        buf.write("\31\2\2\u018c\u0196\3\2\2\2\u018d\u0194\5&\24\2\u018e")
        buf.write("\u0194\5T+\2\u018f\u0194\5X-\2\u0190\u0194\5P)\2\u0191")
        buf.write("\u0194\5\"\22\2\u0192\u0194\5J&\2\u0193\u018d\3\2\2\2")
        buf.write("\u0193\u018e\3\2\2\2\u0193\u018f\3\2\2\2\u0193\u0190\3")
        buf.write("\2\2\2\u0193\u0191\3\2\2\2\u0193\u0192\3\2\2\2\u0194\u0196")
        buf.write("\3\2\2\2\u0195\u0188\3\2\2\2\u0195\u0193\3\2\2\2\u0196")
        buf.write("\u019f\3\2\2\2\u0197\u0198\f\5\2\2\u0198\u0199\5 \21\2")
        buf.write("\u0199\u019a\5@!\6\u019a\u019e\3\2\2\2\u019b\u019c\f\3")
        buf.write("\2\2\u019c\u019e\7\25\2\2\u019d\u0197\3\2\2\2\u019d\u019b")
        buf.write("\3\2\2\2\u019e\u01a1\3\2\2\2\u019f\u019d\3\2\2\2\u019f")
        buf.write("\u01a0\3\2\2\2\u01a0A\3\2\2\2\u01a1\u019f\3\2\2\2\u01a2")
        buf.write("\u01a4\7\"\2\2\u01a3\u01a5\5F$\2\u01a4\u01a3\3\2\2\2\u01a4")
        buf.write("\u01a5\3\2\2\2\u01a5\u01a7\3\2\2\2\u01a6\u01a8\5D#\2\u01a7")
        buf.write("\u01a6\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8C\3\2\2\2\u01a9")
        buf.write("\u01aa\5\26\f\2\u01aa\u01ab\5z>\2\u01abE\3\2\2\2\u01ac")
        buf.write("\u01ad\5\36\20\2\u01ad\u01ae\5H%\2\u01aeG\3\2\2\2\u01af")
        buf.write("\u01b0\b%\1\2\u01b0\u01b1\7\30\2\2\u01b1\u01b2\5H%\2\u01b2")
        buf.write("\u01b3\7\31\2\2\u01b3\u01bf\3\2\2\2\u01b4\u01bd\5&\24")
        buf.write("\2\u01b5\u01bd\5T+\2\u01b6\u01bd\5X-\2\u01b7\u01bd\5J")
        buf.write("&\2\u01b8\u01bd\5\\/\2\u01b9\u01bd\5`\61\2\u01ba\u01bd")
        buf.write("\5h\65\2\u01bb\u01bd\5\22\n\2\u01bc\u01b4\3\2\2\2\u01bc")
        buf.write("\u01b5\3\2\2\2\u01bc\u01b6\3\2\2\2\u01bc\u01b7\3\2\2\2")
        buf.write("\u01bc\u01b8\3\2\2\2\u01bc\u01b9\3\2\2\2\u01bc\u01ba\3")
        buf.write("\2\2\2\u01bc\u01bb\3\2\2\2\u01bd\u01bf\3\2\2\2\u01be\u01af")
        buf.write("\3\2\2\2\u01be\u01bc\3\2\2\2\u01bf\u01c8\3\2\2\2\u01c0")
        buf.write("\u01c1\f\5\2\2\u01c1\u01c2\5 \21\2\u01c2\u01c3\5H%\6\u01c3")
        buf.write("\u01c7\3\2\2\2\u01c4\u01c5\f\3\2\2\u01c5\u01c7\7\25\2")
        buf.write("\2\u01c6\u01c0\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c7\u01ca")
        buf.write("\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9")
        buf.write("I\3\2\2\2\u01ca\u01c8\3\2\2\2\u01cb\u01cd\7#\2\2\u01cc")
        buf.write("\u01ce\5L\'\2\u01cd\u01cc\3\2\2\2\u01cd\u01ce\3\2\2\2")
        buf.write("\u01ceK\3\2\2\2\u01cf\u01d0\5\36\20\2\u01d0\u01d1\5N(")
        buf.write("\2\u01d1M\3\2\2\2\u01d2\u01d3\b(\1\2\u01d3\u01d4\7\30")
        buf.write("\2\2\u01d4\u01d5\5N(\2\u01d5\u01d6\7\31\2\2\u01d6\u01dc")
        buf.write("\3\2\2\2\u01d7\u01da\5P)\2\u01d8\u01da\5\"\22\2\u01d9")
        buf.write("\u01d7\3\2\2\2\u01d9\u01d8\3\2\2\2\u01da\u01dc\3\2\2\2")
        buf.write("\u01db\u01d2\3\2\2\2\u01db\u01d9\3\2\2\2\u01dc\u01e5\3")
        buf.write("\2\2\2\u01dd\u01de\f\5\2\2\u01de\u01df\5 \21\2\u01df\u01e0")
        buf.write("\5N(\6\u01e0\u01e4\3\2\2\2\u01e1\u01e2\f\3\2\2\u01e2\u01e4")
        buf.write("\7\25\2\2\u01e3\u01dd\3\2\2\2\u01e3\u01e1\3\2\2\2\u01e4")
        buf.write("\u01e7\3\2\2\2\u01e5\u01e3\3\2\2\2\u01e5\u01e6\3\2\2\2")
        buf.write("\u01e6O\3\2\2\2\u01e7\u01e5\3\2\2\2\u01e8\u01ea\7$\2\2")
        buf.write("\u01e9\u01eb\5R*\2\u01ea\u01e9\3\2\2\2\u01ea\u01eb\3\2")
        buf.write("\2\2\u01ebQ\3\2\2\2\u01ec\u01ed\5\n\6\2\u01ed\u01ee\7")
        buf.write("\25\2\2\u01ee\u01f3\3\2\2\2\u01ef\u01f0\5\6\4\2\u01f0")
        buf.write("\u01f1\7\25\2\2\u01f1\u01f3\3\2\2\2\u01f2\u01ec\3\2\2")
        buf.write("\2\u01f2\u01ef\3\2\2\2\u01f3S\3\2\2\2\u01f4\u01f6\7%\2")
        buf.write("\2\u01f5\u01f7\5V,\2\u01f6\u01f5\3\2\2\2\u01f6\u01f7\3")
        buf.write("\2\2\2\u01f7U\3\2\2\2\u01f8\u01f9\5\6\4\2\u01f9\u01fa")
        buf.write("\7\25\2\2\u01faW\3\2\2\2\u01fb\u01fd\7&\2\2\u01fc\u01fe")
        buf.write("\5Z.\2\u01fd\u01fc\3\2\2\2\u01fd\u01fe\3\2\2\2\u01feY")
        buf.write("\3\2\2\2\u01ff\u0200\5\6\4\2\u0200\u0201\7\25\2\2\u0201")
        buf.write("[\3\2\2\2\u0202\u0204\7\'\2\2\u0203\u0205\5^\60\2\u0204")
        buf.write("\u0203\3\2\2\2\u0204\u0205\3\2\2\2\u0205]\3\2\2\2\u0206")
        buf.write("\u0207\5\n\6\2\u0207\u0208\7\25\2\2\u0208_\3\2\2\2\u0209")
        buf.write("\u020b\7(\2\2\u020a\u020c\5d\63\2\u020b\u020a\3\2\2\2")
        buf.write("\u020b\u020c\3\2\2\2\u020c\u020e\3\2\2\2\u020d\u020f\5")
        buf.write("b\62\2\u020e\u020d\3\2\2\2\u020e\u020f\3\2\2\2\u020fa")
        buf.write("\3\2\2\2\u0210\u0214\5\26\f\2\u0211\u0215\5z>\2\u0212")
        buf.write("\u0215\5\62\32\2\u0213\u0215\5B\"\2\u0214\u0211\3\2\2")
        buf.write("\2\u0214\u0212\3\2\2\2\u0214\u0213\3\2\2\2\u0215c\3\2")
        buf.write("\2\2\u0216\u0217\5\36\20\2\u0217\u0218\5f\64\2\u0218e")
        buf.write("\3\2\2\2\u0219\u021a\b\64\1\2\u021a\u021b\7\30\2\2\u021b")
        buf.write("\u021c\5f\64\2\u021c\u021d\7\31\2\2\u021d\u0228\3\2\2")
        buf.write("\2\u021e\u0226\5&\24\2\u021f\u0226\5T+\2\u0220\u0226\5")
        buf.write("X-\2\u0221\u0226\5P)\2\u0222\u0226\5\"\22\2\u0223\u0226")
        buf.write("\5t;\2\u0224\u0226\5\22\n\2\u0225\u021e\3\2\2\2\u0225")
        buf.write("\u021f\3\2\2\2\u0225\u0220\3\2\2\2\u0225\u0221\3\2\2\2")
        buf.write("\u0225\u0222\3\2\2\2\u0225\u0223\3\2\2\2\u0225\u0224\3")
        buf.write("\2\2\2\u0226\u0228\3\2\2\2\u0227\u0219\3\2\2\2\u0227\u0225")
        buf.write("\3\2\2\2\u0228\u0231\3\2\2\2\u0229\u022a\f\5\2\2\u022a")
        buf.write("\u022b\5 \21\2\u022b\u022c\5f\64\6\u022c\u0230\3\2\2\2")
        buf.write("\u022d\u022e\f\3\2\2\u022e\u0230\7\25\2\2\u022f\u0229")
        buf.write("\3\2\2\2\u022f\u022d\3\2\2\2\u0230\u0233\3\2\2\2\u0231")
        buf.write("\u022f\3\2\2\2\u0231\u0232\3\2\2\2\u0232g\3\2\2\2\u0233")
        buf.write("\u0231\3\2\2\2\u0234\u0236\7)\2\2\u0235\u0237\5l\67\2")
        buf.write("\u0236\u0235\3\2\2\2\u0236\u0237\3\2\2\2\u0237\u0239\3")
        buf.write("\2\2\2\u0238\u023a\5j\66\2\u0239\u0238\3\2\2\2\u0239\u023a")
        buf.write("\3\2\2\2\u023ai\3\2\2\2\u023b\u023f\5\26\f\2\u023c\u0240")
        buf.write("\5\62\32\2\u023d\u0240\5B\"\2\u023e\u0240\5B\"\2\u023f")
        buf.write("\u023c\3\2\2\2\u023f\u023d\3\2\2\2\u023f\u023e\3\2\2\2")
        buf.write("\u0240k\3\2\2\2\u0241\u0242\5\36\20\2\u0242\u0243\5n8")
        buf.write("\2\u0243m\3\2\2\2\u0244\u0245\b8\1\2\u0245\u0246\7\30")
        buf.write("\2\2\u0246\u0247\5n8\2\u0247\u0248\7\31\2\2\u0248\u024e")
        buf.write("\3\2\2\2\u0249\u024c\5\22\n\2\u024a\u024c\5p9\2\u024b")
        buf.write("\u0249\3\2\2\2\u024b\u024a\3\2\2\2\u024c\u024e\3\2\2\2")
        buf.write("\u024d\u0244\3\2\2\2\u024d\u024b\3\2\2\2\u024e\u0257\3")
        buf.write("\2\2\2\u024f\u0250\f\5\2\2\u0250\u0251\5 \21\2\u0251\u0252")
        buf.write("\5n8\6\u0252\u0256\3\2\2\2\u0253\u0254\f\3\2\2\u0254\u0256")
        buf.write("\7\25\2\2\u0255\u024f\3\2\2\2\u0255\u0253\3\2\2\2\u0256")
        buf.write("\u0259\3\2\2\2\u0257\u0255\3\2\2\2\u0257\u0258\3\2\2\2")
        buf.write("\u0258o\3\2\2\2\u0259\u0257\3\2\2\2\u025a\u025c\7*\2\2")
        buf.write("\u025b\u025d\5r:\2\u025c\u025b\3\2\2\2\u025c\u025d\3\2")
        buf.write("\2\2\u025dq\3\2\2\2\u025e\u025f\5\n\6\2\u025f\u0260\7")
        buf.write("\25\2\2\u0260s\3\2\2\2\u0261\u0263\7+\2\2\u0262\u0264")
        buf.write("\5x=\2\u0263\u0262\3\2\2\2\u0263\u0264\3\2\2\2\u0264\u0266")
        buf.write("\3\2\2\2\u0265\u0267\5v<\2\u0266\u0265\3\2\2\2\u0266\u0267")
        buf.write("\3\2\2\2\u0267u\3\2\2\2\u0268\u0269\5\26\f\2\u0269\u026a")
        buf.write("\5`\61\2\u026aw\3\2\2\2\u026b\u026c\5\n\6\2\u026c\u026d")
        buf.write("\7\25\2\2\u026dy\3\2\2\2\u026e\u0270\7,\2\2\u026f\u0271")
        buf.write("\5|?\2\u0270\u026f\3\2\2\2\u0270\u0271\3\2\2\2\u0271{")
        buf.write("\3\2\2\2\u0272\u0273\5\36\20\2\u0273\u0274\5~@\2\u0274")
        buf.write("}\3\2\2\2\u0275\u0276\b@\1\2\u0276\u0277\7\30\2\2\u0277")
        buf.write("\u0278\5~@\2\u0278\u0279\7\31\2\2\u0279\u028a\3\2\2\2")
        buf.write("\u027a\u0288\5&\24\2\u027b\u0288\5T+\2\u027c\u0288\5X")
        buf.write("-\2\u027d\u0288\5\"\22\2\u027e\u0288\5*\26\2\u027f\u0288")
        buf.write("\5.\30\2\u0280\u0288\5\62\32\2\u0281\u0288\5:\36\2\u0282")
        buf.write("\u0288\5B\"\2\u0283\u0288\5`\61\2\u0284\u0288\5\\/\2\u0285")
        buf.write("\u0288\5\22\n\2\u0286\u0288\5\u0080A\2\u0287\u027a\3\2")
        buf.write("\2\2\u0287\u027b\3\2\2\2\u0287\u027c\3\2\2\2\u0287\u027d")
        buf.write("\3\2\2\2\u0287\u027e\3\2\2\2\u0287\u027f\3\2\2\2\u0287")
        buf.write("\u0280\3\2\2\2\u0287\u0281\3\2\2\2\u0287\u0282\3\2\2\2")
        buf.write("\u0287\u0283\3\2\2\2\u0287\u0284\3\2\2\2\u0287\u0285\3")
        buf.write("\2\2\2\u0287\u0286\3\2\2\2\u0288\u028a\3\2\2\2\u0289\u0275")
        buf.write("\3\2\2\2\u0289\u0287\3\2\2\2\u028a\u0293\3\2\2\2\u028b")
        buf.write("\u028c\f\5\2\2\u028c\u028d\5 \21\2\u028d\u028e\5~@\6\u028e")
        buf.write("\u0292\3\2\2\2\u028f\u0290\f\3\2\2\u0290\u0292\7\25\2")
        buf.write("\2\u0291\u028b\3\2\2\2\u0291\u028f\3\2\2\2\u0292\u0295")
        buf.write("\3\2\2\2\u0293\u0291\3\2\2\2\u0293\u0294\3\2\2\2\u0294")
        buf.write("\177\3\2\2\2\u0295\u0293\3\2\2\2\u0296\u0298\7-\2\2\u0297")
        buf.write("\u0299\5\u0084C\2\u0298\u0297\3\2\2\2\u0298\u0299\3\2")
        buf.write("\2\2\u0299\u029b\3\2\2\2\u029a\u029c\5\u0082B\2\u029b")
        buf.write("\u029a\3\2\2\2\u029b\u029c\3\2\2\2\u029c\u0081\3\2\2\2")
        buf.write("\u029d\u029e\5\26\f\2\u029e\u029f\5z>\2\u029f\u0083\3")
        buf.write("\2\2\2\u02a0\u02a1\5\36\20\2\u02a1\u02a2\5\u0086D\2\u02a2")
        buf.write("\u0085\3\2\2\2\u02a3\u02a4\bD\1\2\u02a4\u02a5\7\30\2\2")
        buf.write("\u02a5\u02a6\5\u0086D\2\u02a6\u02a7\7\31\2\2\u02a7\u02b9")
        buf.write("\3\2\2\2\u02a8\u02b7\5&\24\2\u02a9\u02b7\5T+\2\u02aa\u02b7")
        buf.write("\5X-\2\u02ab\u02b7\5\"\22\2\u02ac\u02b7\5*\26\2\u02ad")
        buf.write("\u02b7\5.\30\2\u02ae\u02b7\5\62\32\2\u02af\u02b7\5\u0080")
        buf.write("A\2\u02b0\u02b7\3\2\2\2\u02b1\u02b7\5:\36\2\u02b2\u02b7")
        buf.write("\5B\"\2\u02b3\u02b7\5`\61\2\u02b4\u02b7\5\\/\2\u02b5\u02b7")
        buf.write("\5\22\n\2\u02b6\u02a8\3\2\2\2\u02b6\u02a9\3\2\2\2\u02b6")
        buf.write("\u02aa\3\2\2\2\u02b6\u02ab\3\2\2\2\u02b6\u02ac\3\2\2\2")
        buf.write("\u02b6\u02ad\3\2\2\2\u02b6\u02ae\3\2\2\2\u02b6\u02af\3")
        buf.write("\2\2\2\u02b6\u02b0\3\2\2\2\u02b6\u02b1\3\2\2\2\u02b6\u02b2")
        buf.write("\3\2\2\2\u02b6\u02b3\3\2\2\2\u02b6\u02b4\3\2\2\2\u02b6")
        buf.write("\u02b5\3\2\2\2\u02b7\u02b9\3\2\2\2\u02b8\u02a3\3\2\2\2")
        buf.write("\u02b8\u02b6\3\2\2\2\u02b9\u02c2\3\2\2\2\u02ba\u02bb\f")
        buf.write("\5\2\2\u02bb\u02bc\5 \21\2\u02bc\u02bd\5\u0086D\6\u02bd")
        buf.write("\u02c1\3\2\2\2\u02be\u02bf\f\3\2\2\u02bf\u02c1\7\25\2")
        buf.write("\2\u02c0\u02ba\3\2\2\2\u02c0\u02be\3\2\2\2\u02c1\u02c4")
        buf.write("\3\2\2\2\u02c2\u02c0\3\2\2\2\u02c2\u02c3\3\2\2\2\u02c3")
        buf.write("\u0087\3\2\2\2\u02c4\u02c2\3\2\2\2S\u008b\u008f\u0092")
        buf.write("\u0097\u00bf\u00c8\u00ca\u00d3\u00d9\u00df\u00e5\u00ea")
        buf.write("\u00f1\u00f8\u00ff\u0102\u0108\u010a\u0118\u011a\u012c")
        buf.write("\u0130\u0137\u0144\u014e\u0152\u0155\u016c\u016e\u0176")
        buf.write("\u0178\u017d\u0180\u0193\u0195\u019d\u019f\u01a4\u01a7")
        buf.write("\u01bc\u01be\u01c6\u01c8\u01cd\u01d9\u01db\u01e3\u01e5")
        buf.write("\u01ea\u01f2\u01f6\u01fd\u0204\u020b\u020e\u0214\u0225")
        buf.write("\u0227\u022f\u0231\u0236\u0239\u023f\u024b\u024d\u0255")
        buf.write("\u0257\u025c\u0263\u0266\u0270\u0287\u0289\u0291\u0293")
        buf.write("\u0298\u029b\u02b6\u02b8\u02c0\u02c2")
        return buf.getvalue()


class RulepadGrammarParser ( Parser ):

    grammarFileName = "RulepadGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\"'", "'||'", "'&&'", "'!'", "'...'", 
                     "'!...'", "'.'", "'='", "'>'", "'<'", "'''", "'&'", 
                     "'must '", "'of '", "'and '", "'or '", "'have '", "'with '", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'name '", "'annotation '", "'extension '", "'Superclass'", 
                     "'implementation '", "'Interface '", "'function '", 
                     "'abstract function '", "'constructor '", "'parameter '", 
                     "'type '", "'specifier '", "'visibility '", "'return value '", 
                     "'declaration statement '", "'expression statement '", 
                     "'value '", "'initial value '", "'class '", "'subclass '" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "SPACE", "Alphabet", 
                      "NL", "LPAREN", "RPAREN", "NAME", "ANNOTATION", "EXTENSION", 
                      "SUPERCLASS", "IMPLEMENTATION", "INTERFACE", "FUNCTION", 
                      "AbstractFunctions", "CONSTRUCTOR", "PARAMETER", "TYPES", 
                      "SPECIFIER", "VISIBILITY", "ReturnValue", "DeclarationStatement", 
                      "ExpressionStatement", "VALUE", "InitialValue", "CLASSES", 
                      "SUBCLASSES" ]

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
    RULE_annotations = 18
    RULE_annotationCondition = 19
    RULE_extensions = 20
    RULE_extensionCondition = 21
    RULE_implementations = 22
    RULE_implementationCondition = 23
    RULE_functions = 24
    RULE_functionOf = 25
    RULE_functionCondition = 26
    RULE_functionExpression = 27
    RULE_abstractFunctions = 28
    RULE_abstractFunctionOf = 29
    RULE_abstractFunctionCondition = 30
    RULE_abstractFunctionExpression = 31
    RULE_constructors = 32
    RULE_constructorOf = 33
    RULE_constructorCondition = 34
    RULE_constructorExpression = 35
    RULE_parameters = 36
    RULE_parameterCondition = 37
    RULE_parameterExpression = 38
    RULE_types = 39
    RULE_typeCondition = 40
    RULE_specifiers = 41
    RULE_specifierCondition = 42
    RULE_visibilities = 43
    RULE_visibilityCondition = 44
    RULE_returnValues = 45
    RULE_returnValueCondition = 46
    RULE_declarationStatements = 47
    RULE_declarationStatementOf = 48
    RULE_declarationStatementCondition = 49
    RULE_declarationStatementExpression = 50
    RULE_expressionStatements = 51
    RULE_expressionStatementOf = 52
    RULE_expressionStatementCondition = 53
    RULE_expressionStatementExpression = 54
    RULE_value = 55
    RULE_valueCondition = 56
    RULE_initialValues = 57
    RULE_initialValueOf = 58
    RULE_initialValueCondition = 59
    RULE_classes = 60
    RULE_classCondition = 61
    RULE_classExpression = 62
    RULE_subclasses = 63
    RULE_subclassOf = 64
    RULE_subclassCondition = 65
    RULE_subclassExpression = 66

    ruleNames =  [ "inputSentence", "mustClause", "words", "word", "combinatorialWords", 
                   "symbols", "end", "emptyLine", "comments", "must", "of", 
                   "and_", "or_", "have", "withWord", "binary", "names", 
                   "nameCondition", "annotations", "annotationCondition", 
                   "extensions", "extensionCondition", "implementations", 
                   "implementationCondition", "functions", "functionOf", 
                   "functionCondition", "functionExpression", "abstractFunctions", 
                   "abstractFunctionOf", "abstractFunctionCondition", "abstractFunctionExpression", 
                   "constructors", "constructorOf", "constructorCondition", 
                   "constructorExpression", "parameters", "parameterCondition", 
                   "parameterExpression", "types", "typeCondition", "specifiers", 
                   "specifierCondition", "visibilities", "visibilityCondition", 
                   "returnValues", "returnValueCondition", "declarationStatements", 
                   "declarationStatementOf", "declarationStatementCondition", 
                   "declarationStatementExpression", "expressionStatements", 
                   "expressionStatementOf", "expressionStatementCondition", 
                   "expressionStatementExpression", "value", "valueCondition", 
                   "initialValues", "initialValueOf", "initialValueCondition", 
                   "classes", "classCondition", "classExpression", "subclasses", 
                   "subclassOf", "subclassCondition", "subclassExpression" ]

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
    SPACE=19
    Alphabet=20
    NL=21
    LPAREN=22
    RPAREN=23
    NAME=24
    ANNOTATION=25
    EXTENSION=26
    SUPERCLASS=27
    IMPLEMENTATION=28
    INTERFACE=29
    FUNCTION=30
    AbstractFunctions=31
    CONSTRUCTOR=32
    PARAMETER=33
    TYPES=34
    SPECIFIER=35
    VISIBILITY=36
    ReturnValue=37
    DeclarationStatement=38
    ExpressionStatement=39
    VALUE=40
    InitialValue=41
    CLASSES=42
    SUBCLASSES=43

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class InputSentenceContext(ParserRuleContext):
        __slots__ = 'parser'

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
            self.state = 141
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.EOF, RulepadGrammarParser.T__6, RulepadGrammarParser.NL]:
                self.state = 137
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 134
                        self.emptyLine() 
                    self.state = 139
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

                pass
            elif token in [RulepadGrammarParser.FUNCTION, RulepadGrammarParser.AbstractFunctions, RulepadGrammarParser.CONSTRUCTOR, RulepadGrammarParser.PARAMETER, RulepadGrammarParser.DeclarationStatement, RulepadGrammarParser.CLASSES, RulepadGrammarParser.SUBCLASSES]:
                self.state = 140
                self.mustClause()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RulepadGrammarParser.T__6:
                self.state = 143
                self.end()


            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RulepadGrammarParser.NL:
                self.state = 146
                self.match(RulepadGrammarParser.NL)
                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 152
            self.match(RulepadGrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MustClauseContext(ParserRuleContext):
        __slots__ = 'parser'

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


        def abstractFunctions(self):
            return self.getTypedRuleContext(RulepadGrammarParser.AbstractFunctionsContext,0)


        def abstractFunctionExpression(self):
            return self.getTypedRuleContext(RulepadGrammarParser.AbstractFunctionExpressionContext,0)


        def constructors(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ConstructorsContext,0)


        def constructorExpression(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ConstructorExpressionContext,0)


        def classes(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ClassesContext,0)


        def classExpression(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ClassExpressionContext,0)


        def parameters(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ParametersContext,0)


        def parameterExpression(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ParameterExpressionContext,0)


        def declarationStatements(self):
            return self.getTypedRuleContext(RulepadGrammarParser.DeclarationStatementsContext,0)


        def declarationStatementExpression(self):
            return self.getTypedRuleContext(RulepadGrammarParser.DeclarationStatementExpressionContext,0)


        def subclasses(self):
            return self.getTypedRuleContext(RulepadGrammarParser.SubclassesContext,0)


        def subclassExpression(self):
            return self.getTypedRuleContext(RulepadGrammarParser.SubclassExpressionContext,0)


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
            self.state = 189
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.FUNCTION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.functions()
                self.state = 155
                self.must()
                self.state = 156
                self.have()
                self.state = 157
                self.functionExpression(0)
                pass
            elif token in [RulepadGrammarParser.AbstractFunctions]:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
                self.abstractFunctions()
                self.state = 160
                self.must()
                self.state = 161
                self.have()
                self.state = 162
                self.abstractFunctionExpression(0)
                pass
            elif token in [RulepadGrammarParser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 164
                self.constructors()
                self.state = 165
                self.must()
                self.state = 166
                self.have()
                self.state = 167
                self.constructorExpression(0)
                pass
            elif token in [RulepadGrammarParser.CLASSES]:
                self.enterOuterAlt(localctx, 4)
                self.state = 169
                self.classes()
                self.state = 170
                self.must()
                self.state = 171
                self.have()
                self.state = 172
                self.classExpression(0)
                pass
            elif token in [RulepadGrammarParser.PARAMETER]:
                self.enterOuterAlt(localctx, 5)
                self.state = 174
                self.parameters()
                self.state = 175
                self.must()
                self.state = 176
                self.have()
                self.state = 177
                self.parameterExpression(0)
                pass
            elif token in [RulepadGrammarParser.DeclarationStatement]:
                self.enterOuterAlt(localctx, 6)
                self.state = 179
                self.declarationStatements()
                self.state = 180
                self.must()
                self.state = 181
                self.have()
                self.state = 182
                self.declarationStatementExpression(0)
                pass
            elif token in [RulepadGrammarParser.SUBCLASSES]:
                self.enterOuterAlt(localctx, 7)
                self.state = 184
                self.subclasses()
                self.state = 185
                self.must()
                self.state = 186
                self.have()
                self.state = 187
                self.subclassExpression(0)
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
        __slots__ = 'parser'

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
            self.state = 191
            self.match(RulepadGrammarParser.T__0)
            self.state = 200
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 198
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        self.state = 192
                        self.word()
                        self.state = 193
                        self.match(RulepadGrammarParser.T__1)
                        pass

                    elif la_ == 2:
                        self.state = 195
                        self.word()
                        self.state = 196
                        self.match(RulepadGrammarParser.T__2)
                        pass

             
                self.state = 202
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 203
            self.word()
            self.state = 204
            self.match(RulepadGrammarParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WordContext(ParserRuleContext):
        __slots__ = 'parser'

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
            self.state = 256
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 207 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 206
                    self.match(RulepadGrammarParser.Alphabet)
                    self.state = 209 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==RulepadGrammarParser.Alphabet):
                        break

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 211
                self.match(RulepadGrammarParser.T__3)
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

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 217
                self.match(RulepadGrammarParser.T__4)
                self.state = 219 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 218
                    self.match(RulepadGrammarParser.Alphabet)
                    self.state = 221 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==RulepadGrammarParser.Alphabet):
                        break

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 223
                self.match(RulepadGrammarParser.T__5)
                self.state = 225 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 224
                    self.match(RulepadGrammarParser.Alphabet)
                    self.state = 227 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==RulepadGrammarParser.Alphabet):
                        break

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 230 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 229
                    self.match(RulepadGrammarParser.Alphabet)
                    self.state = 232 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==RulepadGrammarParser.Alphabet):
                        break

                self.state = 234
                self.match(RulepadGrammarParser.T__4)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 235
                self.match(RulepadGrammarParser.T__3)
                self.state = 237 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 236
                    self.match(RulepadGrammarParser.Alphabet)
                    self.state = 239 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==RulepadGrammarParser.Alphabet):
                        break

                self.state = 241
                self.match(RulepadGrammarParser.T__4)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 242
                self.match(RulepadGrammarParser.T__4)
                self.state = 244 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 243
                    self.match(RulepadGrammarParser.Alphabet)
                    self.state = 246 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==RulepadGrammarParser.Alphabet):
                        break

                self.state = 248
                self.match(RulepadGrammarParser.T__4)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 249
                self.match(RulepadGrammarParser.T__5)
                self.state = 251 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 250
                    self.match(RulepadGrammarParser.Alphabet)
                    self.state = 253 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==RulepadGrammarParser.Alphabet):
                        break

                self.state = 255
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
        __slots__ = 'parser'

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
            self.state = 258
            self.match(RulepadGrammarParser.T__0)
            self.state = 262 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 262
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.Alphabet]:
                    self.state = 259
                    self.match(RulepadGrammarParser.Alphabet)
                    pass
                elif token in [RulepadGrammarParser.T__6, RulepadGrammarParser.T__7, RulepadGrammarParser.T__8, RulepadGrammarParser.T__9, RulepadGrammarParser.T__10, RulepadGrammarParser.T__11, RulepadGrammarParser.LPAREN, RulepadGrammarParser.RPAREN]:
                    self.state = 260
                    self.symbols()
                    pass
                elif token in [RulepadGrammarParser.SPACE]:
                    self.state = 261
                    self.match(RulepadGrammarParser.SPACE)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 264 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RulepadGrammarParser.T__6) | (1 << RulepadGrammarParser.T__7) | (1 << RulepadGrammarParser.T__8) | (1 << RulepadGrammarParser.T__9) | (1 << RulepadGrammarParser.T__10) | (1 << RulepadGrammarParser.T__11) | (1 << RulepadGrammarParser.SPACE) | (1 << RulepadGrammarParser.Alphabet) | (1 << RulepadGrammarParser.LPAREN) | (1 << RulepadGrammarParser.RPAREN))) != 0)):
                    break

            self.state = 266
            self.match(RulepadGrammarParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SymbolsContext(ParserRuleContext):
        __slots__ = 'parser'

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
            self.state = 268
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RulepadGrammarParser.T__6) | (1 << RulepadGrammarParser.T__7) | (1 << RulepadGrammarParser.T__8) | (1 << RulepadGrammarParser.T__9) | (1 << RulepadGrammarParser.T__10) | (1 << RulepadGrammarParser.T__11) | (1 << RulepadGrammarParser.LPAREN) | (1 << RulepadGrammarParser.RPAREN))) != 0)):
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
        __slots__ = 'parser'

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
            self.state = 270
            self.match(RulepadGrammarParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EmptyLineContext(ParserRuleContext):
        __slots__ = 'parser'

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
            self.state = 272
            self.match(RulepadGrammarParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentsContext(ParserRuleContext):
        __slots__ = 'parser'

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
            self.state = 274
            self.match(RulepadGrammarParser.T__0)
            self.state = 278 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 278
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.Alphabet]:
                    self.state = 275
                    self.match(RulepadGrammarParser.Alphabet)
                    pass
                elif token in [RulepadGrammarParser.T__6, RulepadGrammarParser.T__7, RulepadGrammarParser.T__8, RulepadGrammarParser.T__9, RulepadGrammarParser.T__10, RulepadGrammarParser.T__11, RulepadGrammarParser.LPAREN, RulepadGrammarParser.RPAREN]:
                    self.state = 276
                    self.symbols()
                    pass
                elif token in [RulepadGrammarParser.SPACE]:
                    self.state = 277
                    self.match(RulepadGrammarParser.SPACE)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 280 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RulepadGrammarParser.T__6) | (1 << RulepadGrammarParser.T__7) | (1 << RulepadGrammarParser.T__8) | (1 << RulepadGrammarParser.T__9) | (1 << RulepadGrammarParser.T__10) | (1 << RulepadGrammarParser.T__11) | (1 << RulepadGrammarParser.SPACE) | (1 << RulepadGrammarParser.Alphabet) | (1 << RulepadGrammarParser.LPAREN) | (1 << RulepadGrammarParser.RPAREN))) != 0)):
                    break

            self.state = 282
            self.match(RulepadGrammarParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MustContext(ParserRuleContext):
        __slots__ = 'parser'

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
            self.state = 284
            self.match(RulepadGrammarParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OfContext(ParserRuleContext):
        __slots__ = 'parser'

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
            self.state = 286
            self.match(RulepadGrammarParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class And_Context(ParserRuleContext):
        __slots__ = 'parser'

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
            self.state = 288
            self.match(RulepadGrammarParser.T__14)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Or_Context(ParserRuleContext):
        __slots__ = 'parser'

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
            self.state = 290
            self.match(RulepadGrammarParser.T__15)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HaveContext(ParserRuleContext):
        __slots__ = 'parser'

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
            self.state = 292
            self.match(RulepadGrammarParser.T__16)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WithWordContext(ParserRuleContext):
        __slots__ = 'parser'

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
            self.state = 294
            self.match(RulepadGrammarParser.T__17)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BinaryContext(ParserRuleContext):
        __slots__ = 'parser'

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
            self.state = 298
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.T__14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                self.and_()
                pass
            elif token in [RulepadGrammarParser.T__15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 297
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
        __slots__ = 'parser'

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
            self.state = 300
            self.match(RulepadGrammarParser.NAME)
            self.state = 302
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 301
                self.nameCondition()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameConditionContext(ParserRuleContext):
        __slots__ = 'parser'

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
            self.state = 304
            self.words()
            self.state = 305
            self.match(RulepadGrammarParser.SPACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AnnotationsContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 36, self.RULE_annotations)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.match(RulepadGrammarParser.ANNOTATION)
            self.state = 309
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 308
                self.annotationCondition()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AnnotationConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def combinatorialWords(self):
            return self.getTypedRuleContext(RulepadGrammarParser.CombinatorialWordsContext,0)


        def SPACE(self):
            return self.getToken(RulepadGrammarParser.SPACE, 0)

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
        self.enterRule(localctx, 38, self.RULE_annotationCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.combinatorialWords()
            self.state = 312
            self.match(RulepadGrammarParser.SPACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExtensionsContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 40, self.RULE_extensions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.match(RulepadGrammarParser.EXTENSION)
            self.state = 315
            self.extensionCondition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExtensionConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def of(self):
            return self.getTypedRuleContext(RulepadGrammarParser.OfContext,0)


        def words(self):
            return self.getTypedRuleContext(RulepadGrammarParser.WordsContext,0)


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
        self.enterRule(localctx, 42, self.RULE_extensionCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.of()
            self.state = 322
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.T__0]:
                self.state = 318
                self.words()
                self.state = 319
                self.match(RulepadGrammarParser.SPACE)
                pass
            elif token in [RulepadGrammarParser.SUPERCLASS]:
                self.state = 321
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
        __slots__ = 'parser'

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
        self.enterRule(localctx, 44, self.RULE_implementations)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.match(RulepadGrammarParser.IMPLEMENTATION)
            self.state = 325
            self.implementationCondition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImplementationConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def of(self):
            return self.getTypedRuleContext(RulepadGrammarParser.OfContext,0)


        def words(self):
            return self.getTypedRuleContext(RulepadGrammarParser.WordsContext,0)


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
        self.enterRule(localctx, 46, self.RULE_implementationCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.of()
            self.state = 332
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.T__0]:
                self.state = 328
                self.words()
                self.state = 329
                self.match(RulepadGrammarParser.SPACE)
                pass
            elif token in [RulepadGrammarParser.INTERFACE]:
                self.state = 331
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(RulepadGrammarParser.FUNCTION, 0)

        def functionCondition(self):
            return self.getTypedRuleContext(RulepadGrammarParser.FunctionConditionContext,0)


        def functionOf(self):
            return self.getTypedRuleContext(RulepadGrammarParser.FunctionOfContext,0)


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
        self.enterRule(localctx, 48, self.RULE_functions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.match(RulepadGrammarParser.FUNCTION)
            self.state = 336
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 335
                self.functionCondition()


            self.state = 339
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 338
                self.functionOf()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionOfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def of(self):
            return self.getTypedRuleContext(RulepadGrammarParser.OfContext,0)


        def classes(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ClassesContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_functionOf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionOf" ):
                listener.enterFunctionOf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionOf" ):
                listener.exitFunctionOf(self)




    def functionOf(self):

        localctx = RulepadGrammarParser.FunctionOfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_functionOf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.of()
            self.state = 342
            self.classes()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionConditionContext(ParserRuleContext):
        __slots__ = 'parser'

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
            self.state = 344
            self.withWord()
            self.state = 345
            self.functionExpression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

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


        def specifiers(self):
            return self.getTypedRuleContext(RulepadGrammarParser.SpecifiersContext,0)


        def visibilities(self):
            return self.getTypedRuleContext(RulepadGrammarParser.VisibilitiesContext,0)


        def types(self):
            return self.getTypedRuleContext(RulepadGrammarParser.TypesContext,0)


        def names(self):
            return self.getTypedRuleContext(RulepadGrammarParser.NamesContext,0)


        def parameters(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ParametersContext,0)


        def returnValues(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ReturnValuesContext,0)


        def declarationStatements(self):
            return self.getTypedRuleContext(RulepadGrammarParser.DeclarationStatementsContext,0)


        def expressionStatements(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ExpressionStatementsContext,0)


        def comments(self):
            return self.getTypedRuleContext(RulepadGrammarParser.CommentsContext,0)


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
            self.state = 364
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 348
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 349
                self.functionExpression(0)
                self.state = 350
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.T__0, RulepadGrammarParser.NAME, RulepadGrammarParser.ANNOTATION, RulepadGrammarParser.PARAMETER, RulepadGrammarParser.TYPES, RulepadGrammarParser.SPECIFIER, RulepadGrammarParser.VISIBILITY, RulepadGrammarParser.ReturnValue, RulepadGrammarParser.DeclarationStatement, RulepadGrammarParser.ExpressionStatement]:
                self.state = 362
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.ANNOTATION]:
                    self.state = 352
                    self.annotations()
                    pass
                elif token in [RulepadGrammarParser.SPECIFIER]:
                    self.state = 353
                    self.specifiers()
                    pass
                elif token in [RulepadGrammarParser.VISIBILITY]:
                    self.state = 354
                    self.visibilities()
                    pass
                elif token in [RulepadGrammarParser.TYPES]:
                    self.state = 355
                    self.types()
                    pass
                elif token in [RulepadGrammarParser.NAME]:
                    self.state = 356
                    self.names()
                    pass
                elif token in [RulepadGrammarParser.PARAMETER]:
                    self.state = 357
                    self.parameters()
                    pass
                elif token in [RulepadGrammarParser.ReturnValue]:
                    self.state = 358
                    self.returnValues()
                    pass
                elif token in [RulepadGrammarParser.DeclarationStatement]:
                    self.state = 359
                    self.declarationStatements()
                    pass
                elif token in [RulepadGrammarParser.ExpressionStatement]:
                    self.state = 360
                    self.expressionStatements()
                    pass
                elif token in [RulepadGrammarParser.T__0]:
                    self.state = 361
                    self.comments()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 374
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 372
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.FunctionExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_functionExpression)
                        self.state = 366
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 367
                        localctx.op = self.binary()
                        self.state = 368
                        localctx.right = self.functionExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.FunctionExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_functionExpression)
                        self.state = 370
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 371
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 376
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AbstractFunctionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AbstractFunctions(self):
            return self.getToken(RulepadGrammarParser.AbstractFunctions, 0)

        def abstractFunctionCondition(self):
            return self.getTypedRuleContext(RulepadGrammarParser.AbstractFunctionConditionContext,0)


        def abstractFunctionOf(self):
            return self.getTypedRuleContext(RulepadGrammarParser.AbstractFunctionOfContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_abstractFunctions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAbstractFunctions" ):
                listener.enterAbstractFunctions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAbstractFunctions" ):
                listener.exitAbstractFunctions(self)




    def abstractFunctions(self):

        localctx = RulepadGrammarParser.AbstractFunctionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_abstractFunctions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self.match(RulepadGrammarParser.AbstractFunctions)
            self.state = 379
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 378
                self.abstractFunctionCondition()


            self.state = 382
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 381
                self.abstractFunctionOf()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AbstractFunctionOfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def of(self):
            return self.getTypedRuleContext(RulepadGrammarParser.OfContext,0)


        def classes(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ClassesContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_abstractFunctionOf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAbstractFunctionOf" ):
                listener.enterAbstractFunctionOf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAbstractFunctionOf" ):
                listener.exitAbstractFunctionOf(self)




    def abstractFunctionOf(self):

        localctx = RulepadGrammarParser.AbstractFunctionOfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_abstractFunctionOf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.of()
            self.state = 385
            self.classes()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AbstractFunctionConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def withWord(self):
            return self.getTypedRuleContext(RulepadGrammarParser.WithWordContext,0)


        def abstractFunctionExpression(self):
            return self.getTypedRuleContext(RulepadGrammarParser.AbstractFunctionExpressionContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_abstractFunctionCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAbstractFunctionCondition" ):
                listener.enterAbstractFunctionCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAbstractFunctionCondition" ):
                listener.exitAbstractFunctionCondition(self)




    def abstractFunctionCondition(self):

        localctx = RulepadGrammarParser.AbstractFunctionConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_abstractFunctionCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.withWord()
            self.state = 388
            self.abstractFunctionExpression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AbstractFunctionExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # AbstractFunctionExpressionContext
            self.op = None # BinaryContext
            self.right = None # AbstractFunctionExpressionContext

        def LPAREN(self):
            return self.getToken(RulepadGrammarParser.LPAREN, 0)

        def abstractFunctionExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RulepadGrammarParser.AbstractFunctionExpressionContext)
            else:
                return self.getTypedRuleContext(RulepadGrammarParser.AbstractFunctionExpressionContext,i)


        def RPAREN(self):
            return self.getToken(RulepadGrammarParser.RPAREN, 0)

        def annotations(self):
            return self.getTypedRuleContext(RulepadGrammarParser.AnnotationsContext,0)


        def specifiers(self):
            return self.getTypedRuleContext(RulepadGrammarParser.SpecifiersContext,0)


        def visibilities(self):
            return self.getTypedRuleContext(RulepadGrammarParser.VisibilitiesContext,0)


        def types(self):
            return self.getTypedRuleContext(RulepadGrammarParser.TypesContext,0)


        def names(self):
            return self.getTypedRuleContext(RulepadGrammarParser.NamesContext,0)


        def parameters(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ParametersContext,0)


        def binary(self):
            return self.getTypedRuleContext(RulepadGrammarParser.BinaryContext,0)


        def SPACE(self):
            return self.getToken(RulepadGrammarParser.SPACE, 0)

        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_abstractFunctionExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAbstractFunctionExpression" ):
                listener.enterAbstractFunctionExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAbstractFunctionExpression" ):
                listener.exitAbstractFunctionExpression(self)



    def abstractFunctionExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RulepadGrammarParser.AbstractFunctionExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_abstractFunctionExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 391
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 392
                self.abstractFunctionExpression(0)
                self.state = 393
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.NAME, RulepadGrammarParser.ANNOTATION, RulepadGrammarParser.PARAMETER, RulepadGrammarParser.TYPES, RulepadGrammarParser.SPECIFIER, RulepadGrammarParser.VISIBILITY]:
                self.state = 401
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.ANNOTATION]:
                    self.state = 395
                    self.annotations()
                    pass
                elif token in [RulepadGrammarParser.SPECIFIER]:
                    self.state = 396
                    self.specifiers()
                    pass
                elif token in [RulepadGrammarParser.VISIBILITY]:
                    self.state = 397
                    self.visibilities()
                    pass
                elif token in [RulepadGrammarParser.TYPES]:
                    self.state = 398
                    self.types()
                    pass
                elif token in [RulepadGrammarParser.NAME]:
                    self.state = 399
                    self.names()
                    pass
                elif token in [RulepadGrammarParser.PARAMETER]:
                    self.state = 400
                    self.parameters()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 413
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 411
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.AbstractFunctionExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_abstractFunctionExpression)
                        self.state = 405
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 406
                        localctx.op = self.binary()
                        self.state = 407
                        localctx.right = self.abstractFunctionExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.AbstractFunctionExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_abstractFunctionExpression)
                        self.state = 409
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 410
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 415
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ConstructorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTRUCTOR(self):
            return self.getToken(RulepadGrammarParser.CONSTRUCTOR, 0)

        def constructorCondition(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ConstructorConditionContext,0)


        def constructorOf(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ConstructorOfContext,0)


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
        self.enterRule(localctx, 64, self.RULE_constructors)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.match(RulepadGrammarParser.CONSTRUCTOR)
            self.state = 418
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 417
                self.constructorCondition()


            self.state = 421
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 420
                self.constructorOf()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorOfContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 66, self.RULE_constructorOf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            self.of()
            self.state = 424
            self.classes()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorConditionContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 68, self.RULE_constructorCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            self.withWord()
            self.state = 427
            self.constructorExpression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

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


        def specifiers(self):
            return self.getTypedRuleContext(RulepadGrammarParser.SpecifiersContext,0)


        def visibilities(self):
            return self.getTypedRuleContext(RulepadGrammarParser.VisibilitiesContext,0)


        def parameters(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ParametersContext,0)


        def returnValues(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ReturnValuesContext,0)


        def declarationStatements(self):
            return self.getTypedRuleContext(RulepadGrammarParser.DeclarationStatementsContext,0)


        def expressionStatements(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ExpressionStatementsContext,0)


        def comments(self):
            return self.getTypedRuleContext(RulepadGrammarParser.CommentsContext,0)


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
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_constructorExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 444
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 430
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 431
                self.constructorExpression(0)
                self.state = 432
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.T__0, RulepadGrammarParser.ANNOTATION, RulepadGrammarParser.PARAMETER, RulepadGrammarParser.SPECIFIER, RulepadGrammarParser.VISIBILITY, RulepadGrammarParser.ReturnValue, RulepadGrammarParser.DeclarationStatement, RulepadGrammarParser.ExpressionStatement]:
                self.state = 442
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.ANNOTATION]:
                    self.state = 434
                    self.annotations()
                    pass
                elif token in [RulepadGrammarParser.SPECIFIER]:
                    self.state = 435
                    self.specifiers()
                    pass
                elif token in [RulepadGrammarParser.VISIBILITY]:
                    self.state = 436
                    self.visibilities()
                    pass
                elif token in [RulepadGrammarParser.PARAMETER]:
                    self.state = 437
                    self.parameters()
                    pass
                elif token in [RulepadGrammarParser.ReturnValue]:
                    self.state = 438
                    self.returnValues()
                    pass
                elif token in [RulepadGrammarParser.DeclarationStatement]:
                    self.state = 439
                    self.declarationStatements()
                    pass
                elif token in [RulepadGrammarParser.ExpressionStatement]:
                    self.state = 440
                    self.expressionStatements()
                    pass
                elif token in [RulepadGrammarParser.T__0]:
                    self.state = 441
                    self.comments()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 454
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 452
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.ConstructorExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_constructorExpression)
                        self.state = 446
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 447
                        localctx.op = self.binary()
                        self.state = 448
                        localctx.right = self.constructorExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.ConstructorExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_constructorExpression)
                        self.state = 450
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 451
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 456
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 72, self.RULE_parameters)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
            self.match(RulepadGrammarParser.PARAMETER)
            self.state = 459
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.state = 458
                self.parameterCondition()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def withWord(self):
            return self.getTypedRuleContext(RulepadGrammarParser.WithWordContext,0)


        def parameterExpression(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ParameterExpressionContext,0)


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
        self.enterRule(localctx, 74, self.RULE_parameterCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 461
            self.withWord()
            self.state = 462
            self.parameterExpression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

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
            self.state = 473
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 465
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 466
                self.parameterExpression(0)
                self.state = 467
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.NAME, RulepadGrammarParser.TYPES]:
                self.state = 471
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.TYPES]:
                    self.state = 469
                    self.types()
                    pass
                elif token in [RulepadGrammarParser.NAME]:
                    self.state = 470
                    self.names()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 483
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 481
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.ParameterExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_parameterExpression)
                        self.state = 475
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 476
                        localctx.op = self.binary()
                        self.state = 477
                        localctx.right = self.parameterExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.ParameterExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_parameterExpression)
                        self.state = 479
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 480
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 485
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TypesContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 78, self.RULE_types)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 486
            self.match(RulepadGrammarParser.TYPES)
            self.state = 488
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.state = 487
                self.typeCondition()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeConditionContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 80, self.RULE_typeCondition)
        try:
            self.state = 496
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 490
                self.combinatorialWords()
                self.state = 491
                self.match(RulepadGrammarParser.SPACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 493
                self.words()
                self.state = 494
                self.match(RulepadGrammarParser.SPACE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SpecifiersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SPECIFIER(self):
            return self.getToken(RulepadGrammarParser.SPECIFIER, 0)

        def specifierCondition(self):
            return self.getTypedRuleContext(RulepadGrammarParser.SpecifierConditionContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_specifiers

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpecifiers" ):
                listener.enterSpecifiers(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpecifiers" ):
                listener.exitSpecifiers(self)




    def specifiers(self):

        localctx = RulepadGrammarParser.SpecifiersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_specifiers)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498
            self.match(RulepadGrammarParser.SPECIFIER)
            self.state = 500
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.state = 499
                self.specifierCondition()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SpecifierConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def words(self):
            return self.getTypedRuleContext(RulepadGrammarParser.WordsContext,0)


        def SPACE(self):
            return self.getToken(RulepadGrammarParser.SPACE, 0)

        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_specifierCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpecifierCondition" ):
                listener.enterSpecifierCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpecifierCondition" ):
                listener.exitSpecifierCondition(self)




    def specifierCondition(self):

        localctx = RulepadGrammarParser.SpecifierConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_specifierCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 502
            self.words()
            self.state = 503
            self.match(RulepadGrammarParser.SPACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VisibilitiesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VISIBILITY(self):
            return self.getToken(RulepadGrammarParser.VISIBILITY, 0)

        def visibilityCondition(self):
            return self.getTypedRuleContext(RulepadGrammarParser.VisibilityConditionContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_visibilities

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVisibilities" ):
                listener.enterVisibilities(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVisibilities" ):
                listener.exitVisibilities(self)




    def visibilities(self):

        localctx = RulepadGrammarParser.VisibilitiesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_visibilities)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 505
            self.match(RulepadGrammarParser.VISIBILITY)
            self.state = 507
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.state = 506
                self.visibilityCondition()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VisibilityConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def words(self):
            return self.getTypedRuleContext(RulepadGrammarParser.WordsContext,0)


        def SPACE(self):
            return self.getToken(RulepadGrammarParser.SPACE, 0)

        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_visibilityCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVisibilityCondition" ):
                listener.enterVisibilityCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVisibilityCondition" ):
                listener.exitVisibilityCondition(self)




    def visibilityCondition(self):

        localctx = RulepadGrammarParser.VisibilityConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_visibilityCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 509
            self.words()
            self.state = 510
            self.match(RulepadGrammarParser.SPACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnValuesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ReturnValue(self):
            return self.getToken(RulepadGrammarParser.ReturnValue, 0)

        def returnValueCondition(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ReturnValueConditionContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_returnValues

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnValues" ):
                listener.enterReturnValues(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnValues" ):
                listener.exitReturnValues(self)




    def returnValues(self):

        localctx = RulepadGrammarParser.ReturnValuesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_returnValues)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 512
            self.match(RulepadGrammarParser.ReturnValue)
            self.state = 514
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.state = 513
                self.returnValueCondition()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnValueConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def combinatorialWords(self):
            return self.getTypedRuleContext(RulepadGrammarParser.CombinatorialWordsContext,0)


        def SPACE(self):
            return self.getToken(RulepadGrammarParser.SPACE, 0)

        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_returnValueCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnValueCondition" ):
                listener.enterReturnValueCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnValueCondition" ):
                listener.exitReturnValueCondition(self)




    def returnValueCondition(self):

        localctx = RulepadGrammarParser.ReturnValueConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_returnValueCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 516
            self.combinatorialWords()
            self.state = 517
            self.match(RulepadGrammarParser.SPACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationStatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DeclarationStatement(self):
            return self.getToken(RulepadGrammarParser.DeclarationStatement, 0)

        def declarationStatementCondition(self):
            return self.getTypedRuleContext(RulepadGrammarParser.DeclarationStatementConditionContext,0)


        def declarationStatementOf(self):
            return self.getTypedRuleContext(RulepadGrammarParser.DeclarationStatementOfContext,0)


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
        self.enterRule(localctx, 94, self.RULE_declarationStatements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 519
            self.match(RulepadGrammarParser.DeclarationStatement)
            self.state = 521
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.state = 520
                self.declarationStatementCondition()


            self.state = 524
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.state = 523
                self.declarationStatementOf()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationStatementOfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def of(self):
            return self.getTypedRuleContext(RulepadGrammarParser.OfContext,0)


        def classes(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ClassesContext,0)


        def functions(self):
            return self.getTypedRuleContext(RulepadGrammarParser.FunctionsContext,0)


        def constructors(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ConstructorsContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_declarationStatementOf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclarationStatementOf" ):
                listener.enterDeclarationStatementOf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclarationStatementOf" ):
                listener.exitDeclarationStatementOf(self)




    def declarationStatementOf(self):

        localctx = RulepadGrammarParser.DeclarationStatementOfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_declarationStatementOf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 526
            self.of()
            self.state = 530
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.CLASSES]:
                self.state = 527
                self.classes()
                pass
            elif token in [RulepadGrammarParser.FUNCTION]:
                self.state = 528
                self.functions()
                pass
            elif token in [RulepadGrammarParser.CONSTRUCTOR]:
                self.state = 529
                self.constructors()
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


    class DeclarationStatementConditionContext(ParserRuleContext):
        __slots__ = 'parser'

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
            self.state = 532
            self.withWord()
            self.state = 533
            self.declarationStatementExpression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationStatementExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

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


        def specifiers(self):
            return self.getTypedRuleContext(RulepadGrammarParser.SpecifiersContext,0)


        def visibilities(self):
            return self.getTypedRuleContext(RulepadGrammarParser.VisibilitiesContext,0)


        def types(self):
            return self.getTypedRuleContext(RulepadGrammarParser.TypesContext,0)


        def names(self):
            return self.getTypedRuleContext(RulepadGrammarParser.NamesContext,0)


        def initialValues(self):
            return self.getTypedRuleContext(RulepadGrammarParser.InitialValuesContext,0)


        def comments(self):
            return self.getTypedRuleContext(RulepadGrammarParser.CommentsContext,0)


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
            self.state = 549
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 536
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 537
                self.declarationStatementExpression(0)
                self.state = 538
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.T__0, RulepadGrammarParser.NAME, RulepadGrammarParser.ANNOTATION, RulepadGrammarParser.TYPES, RulepadGrammarParser.SPECIFIER, RulepadGrammarParser.VISIBILITY, RulepadGrammarParser.InitialValue]:
                self.state = 547
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.ANNOTATION]:
                    self.state = 540
                    self.annotations()
                    pass
                elif token in [RulepadGrammarParser.SPECIFIER]:
                    self.state = 541
                    self.specifiers()
                    pass
                elif token in [RulepadGrammarParser.VISIBILITY]:
                    self.state = 542
                    self.visibilities()
                    pass
                elif token in [RulepadGrammarParser.TYPES]:
                    self.state = 543
                    self.types()
                    pass
                elif token in [RulepadGrammarParser.NAME]:
                    self.state = 544
                    self.names()
                    pass
                elif token in [RulepadGrammarParser.InitialValue]:
                    self.state = 545
                    self.initialValues()
                    pass
                elif token in [RulepadGrammarParser.T__0]:
                    self.state = 546
                    self.comments()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 559
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,59,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 557
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.DeclarationStatementExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_declarationStatementExpression)
                        self.state = 551
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 552
                        localctx.op = self.binary()
                        self.state = 553
                        localctx.right = self.declarationStatementExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.DeclarationStatementExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_declarationStatementExpression)
                        self.state = 555
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 556
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 561
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,59,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExpressionStatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ExpressionStatement(self):
            return self.getToken(RulepadGrammarParser.ExpressionStatement, 0)

        def expressionStatementCondition(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ExpressionStatementConditionContext,0)


        def expressionStatementOf(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ExpressionStatementOfContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_expressionStatements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionStatements" ):
                listener.enterExpressionStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionStatements" ):
                listener.exitExpressionStatements(self)




    def expressionStatements(self):

        localctx = RulepadGrammarParser.ExpressionStatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_expressionStatements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 562
            self.match(RulepadGrammarParser.ExpressionStatement)
            self.state = 564
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
            if la_ == 1:
                self.state = 563
                self.expressionStatementCondition()


            self.state = 567
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
            if la_ == 1:
                self.state = 566
                self.expressionStatementOf()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionStatementOfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def of(self):
            return self.getTypedRuleContext(RulepadGrammarParser.OfContext,0)


        def functions(self):
            return self.getTypedRuleContext(RulepadGrammarParser.FunctionsContext,0)


        def constructors(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ConstructorsContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_expressionStatementOf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionStatementOf" ):
                listener.enterExpressionStatementOf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionStatementOf" ):
                listener.exitExpressionStatementOf(self)




    def expressionStatementOf(self):

        localctx = RulepadGrammarParser.ExpressionStatementOfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_expressionStatementOf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 569
            self.of()
            self.state = 573
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,62,self._ctx)
            if la_ == 1:
                self.state = 570
                self.functions()
                pass

            elif la_ == 2:
                self.state = 571
                self.constructors()
                pass

            elif la_ == 3:
                self.state = 572
                self.constructors()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionStatementConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def withWord(self):
            return self.getTypedRuleContext(RulepadGrammarParser.WithWordContext,0)


        def expressionStatementExpression(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ExpressionStatementExpressionContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_expressionStatementCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionStatementCondition" ):
                listener.enterExpressionStatementCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionStatementCondition" ):
                listener.exitExpressionStatementCondition(self)




    def expressionStatementCondition(self):

        localctx = RulepadGrammarParser.ExpressionStatementConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_expressionStatementCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 575
            self.withWord()
            self.state = 576
            self.expressionStatementExpression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionStatementExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # ExpressionStatementExpressionContext
            self.op = None # BinaryContext
            self.right = None # ExpressionStatementExpressionContext

        def LPAREN(self):
            return self.getToken(RulepadGrammarParser.LPAREN, 0)

        def expressionStatementExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RulepadGrammarParser.ExpressionStatementExpressionContext)
            else:
                return self.getTypedRuleContext(RulepadGrammarParser.ExpressionStatementExpressionContext,i)


        def RPAREN(self):
            return self.getToken(RulepadGrammarParser.RPAREN, 0)

        def comments(self):
            return self.getTypedRuleContext(RulepadGrammarParser.CommentsContext,0)


        def value(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ValueContext,0)


        def binary(self):
            return self.getTypedRuleContext(RulepadGrammarParser.BinaryContext,0)


        def SPACE(self):
            return self.getToken(RulepadGrammarParser.SPACE, 0)

        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_expressionStatementExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionStatementExpression" ):
                listener.enterExpressionStatementExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionStatementExpression" ):
                listener.exitExpressionStatementExpression(self)



    def expressionStatementExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RulepadGrammarParser.ExpressionStatementExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 108
        self.enterRecursionRule(localctx, 108, self.RULE_expressionStatementExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 587
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 579
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 580
                self.expressionStatementExpression(0)
                self.state = 581
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.T__0, RulepadGrammarParser.VALUE]:
                self.state = 585
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.T__0]:
                    self.state = 583
                    self.comments()
                    pass
                elif token in [RulepadGrammarParser.VALUE]:
                    self.state = 584
                    self.value()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 597
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,66,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 595
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.ExpressionStatementExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressionStatementExpression)
                        self.state = 589
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 590
                        localctx.op = self.binary()
                        self.state = 591
                        localctx.right = self.expressionStatementExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.ExpressionStatementExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressionStatementExpression)
                        self.state = 593
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 594
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 599
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,66,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VALUE(self):
            return self.getToken(RulepadGrammarParser.VALUE, 0)

        def valueCondition(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ValueConditionContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = RulepadGrammarParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 600
            self.match(RulepadGrammarParser.VALUE)
            self.state = 602
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,67,self._ctx)
            if la_ == 1:
                self.state = 601
                self.valueCondition()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueConditionContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 112, self.RULE_valueCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 604
            self.combinatorialWords()
            self.state = 605
            self.match(RulepadGrammarParser.SPACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitialValuesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def InitialValue(self):
            return self.getToken(RulepadGrammarParser.InitialValue, 0)

        def initialValueCondition(self):
            return self.getTypedRuleContext(RulepadGrammarParser.InitialValueConditionContext,0)


        def initialValueOf(self):
            return self.getTypedRuleContext(RulepadGrammarParser.InitialValueOfContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_initialValues

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitialValues" ):
                listener.enterInitialValues(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitialValues" ):
                listener.exitInitialValues(self)




    def initialValues(self):

        localctx = RulepadGrammarParser.InitialValuesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_initialValues)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 607
            self.match(RulepadGrammarParser.InitialValue)
            self.state = 609
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,68,self._ctx)
            if la_ == 1:
                self.state = 608
                self.initialValueCondition()


            self.state = 612
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,69,self._ctx)
            if la_ == 1:
                self.state = 611
                self.initialValueOf()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitialValueOfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def of(self):
            return self.getTypedRuleContext(RulepadGrammarParser.OfContext,0)


        def declarationStatements(self):
            return self.getTypedRuleContext(RulepadGrammarParser.DeclarationStatementsContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_initialValueOf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitialValueOf" ):
                listener.enterInitialValueOf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitialValueOf" ):
                listener.exitInitialValueOf(self)




    def initialValueOf(self):

        localctx = RulepadGrammarParser.InitialValueOfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_initialValueOf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 614
            self.of()
            self.state = 615
            self.declarationStatements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitialValueConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def combinatorialWords(self):
            return self.getTypedRuleContext(RulepadGrammarParser.CombinatorialWordsContext,0)


        def SPACE(self):
            return self.getToken(RulepadGrammarParser.SPACE, 0)

        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_initialValueCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitialValueCondition" ):
                listener.enterInitialValueCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitialValueCondition" ):
                listener.exitInitialValueCondition(self)




    def initialValueCondition(self):

        localctx = RulepadGrammarParser.InitialValueConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_initialValueCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 617
            self.combinatorialWords()
            self.state = 618
            self.match(RulepadGrammarParser.SPACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassesContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 120, self.RULE_classes)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 620
            self.match(RulepadGrammarParser.CLASSES)
            self.state = 622
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,70,self._ctx)
            if la_ == 1:
                self.state = 621
                self.classCondition()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassConditionContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 122, self.RULE_classCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 624
            self.withWord()
            self.state = 625
            self.classExpression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

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


        def specifiers(self):
            return self.getTypedRuleContext(RulepadGrammarParser.SpecifiersContext,0)


        def visibilities(self):
            return self.getTypedRuleContext(RulepadGrammarParser.VisibilitiesContext,0)


        def names(self):
            return self.getTypedRuleContext(RulepadGrammarParser.NamesContext,0)


        def extensions(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ExtensionsContext,0)


        def implementations(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ImplementationsContext,0)


        def functions(self):
            return self.getTypedRuleContext(RulepadGrammarParser.FunctionsContext,0)


        def abstractFunctions(self):
            return self.getTypedRuleContext(RulepadGrammarParser.AbstractFunctionsContext,0)


        def constructors(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ConstructorsContext,0)


        def declarationStatements(self):
            return self.getTypedRuleContext(RulepadGrammarParser.DeclarationStatementsContext,0)


        def returnValues(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ReturnValuesContext,0)


        def comments(self):
            return self.getTypedRuleContext(RulepadGrammarParser.CommentsContext,0)


        def subclasses(self):
            return self.getTypedRuleContext(RulepadGrammarParser.SubclassesContext,0)


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
        _startState = 124
        self.enterRecursionRule(localctx, 124, self.RULE_classExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 647
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 628
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 629
                self.classExpression(0)
                self.state = 630
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.T__0, RulepadGrammarParser.NAME, RulepadGrammarParser.ANNOTATION, RulepadGrammarParser.EXTENSION, RulepadGrammarParser.IMPLEMENTATION, RulepadGrammarParser.FUNCTION, RulepadGrammarParser.AbstractFunctions, RulepadGrammarParser.CONSTRUCTOR, RulepadGrammarParser.SPECIFIER, RulepadGrammarParser.VISIBILITY, RulepadGrammarParser.ReturnValue, RulepadGrammarParser.DeclarationStatement, RulepadGrammarParser.SUBCLASSES]:
                self.state = 645
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.ANNOTATION]:
                    self.state = 632
                    self.annotations()
                    pass
                elif token in [RulepadGrammarParser.SPECIFIER]:
                    self.state = 633
                    self.specifiers()
                    pass
                elif token in [RulepadGrammarParser.VISIBILITY]:
                    self.state = 634
                    self.visibilities()
                    pass
                elif token in [RulepadGrammarParser.NAME]:
                    self.state = 635
                    self.names()
                    pass
                elif token in [RulepadGrammarParser.EXTENSION]:
                    self.state = 636
                    self.extensions()
                    pass
                elif token in [RulepadGrammarParser.IMPLEMENTATION]:
                    self.state = 637
                    self.implementations()
                    pass
                elif token in [RulepadGrammarParser.FUNCTION]:
                    self.state = 638
                    self.functions()
                    pass
                elif token in [RulepadGrammarParser.AbstractFunctions]:
                    self.state = 639
                    self.abstractFunctions()
                    pass
                elif token in [RulepadGrammarParser.CONSTRUCTOR]:
                    self.state = 640
                    self.constructors()
                    pass
                elif token in [RulepadGrammarParser.DeclarationStatement]:
                    self.state = 641
                    self.declarationStatements()
                    pass
                elif token in [RulepadGrammarParser.ReturnValue]:
                    self.state = 642
                    self.returnValues()
                    pass
                elif token in [RulepadGrammarParser.T__0]:
                    self.state = 643
                    self.comments()
                    pass
                elif token in [RulepadGrammarParser.SUBCLASSES]:
                    self.state = 644
                    self.subclasses()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 657
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,74,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 655
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,73,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.ClassExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_classExpression)
                        self.state = 649
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 650
                        localctx.op = self.binary()
                        self.state = 651
                        localctx.right = self.classExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.ClassExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_classExpression)
                        self.state = 653
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 654
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 659
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,74,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class SubclassesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUBCLASSES(self):
            return self.getToken(RulepadGrammarParser.SUBCLASSES, 0)

        def subclassCondition(self):
            return self.getTypedRuleContext(RulepadGrammarParser.SubclassConditionContext,0)


        def subclassOf(self):
            return self.getTypedRuleContext(RulepadGrammarParser.SubclassOfContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_subclasses

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubclasses" ):
                listener.enterSubclasses(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubclasses" ):
                listener.exitSubclasses(self)




    def subclasses(self):

        localctx = RulepadGrammarParser.SubclassesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_subclasses)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 660
            self.match(RulepadGrammarParser.SUBCLASSES)
            self.state = 662
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,75,self._ctx)
            if la_ == 1:
                self.state = 661
                self.subclassCondition()


            self.state = 665
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,76,self._ctx)
            if la_ == 1:
                self.state = 664
                self.subclassOf()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubclassOfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def of(self):
            return self.getTypedRuleContext(RulepadGrammarParser.OfContext,0)


        def classes(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ClassesContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_subclassOf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubclassOf" ):
                listener.enterSubclassOf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubclassOf" ):
                listener.exitSubclassOf(self)




    def subclassOf(self):

        localctx = RulepadGrammarParser.SubclassOfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_subclassOf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 667
            self.of()
            self.state = 668
            self.classes()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubclassConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def withWord(self):
            return self.getTypedRuleContext(RulepadGrammarParser.WithWordContext,0)


        def subclassExpression(self):
            return self.getTypedRuleContext(RulepadGrammarParser.SubclassExpressionContext,0)


        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_subclassCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubclassCondition" ):
                listener.enterSubclassCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubclassCondition" ):
                listener.exitSubclassCondition(self)




    def subclassCondition(self):

        localctx = RulepadGrammarParser.SubclassConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_subclassCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 670
            self.withWord()
            self.state = 671
            self.subclassExpression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubclassExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # SubclassExpressionContext
            self.op = None # BinaryContext
            self.right = None # SubclassExpressionContext

        def LPAREN(self):
            return self.getToken(RulepadGrammarParser.LPAREN, 0)

        def subclassExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RulepadGrammarParser.SubclassExpressionContext)
            else:
                return self.getTypedRuleContext(RulepadGrammarParser.SubclassExpressionContext,i)


        def RPAREN(self):
            return self.getToken(RulepadGrammarParser.RPAREN, 0)

        def annotations(self):
            return self.getTypedRuleContext(RulepadGrammarParser.AnnotationsContext,0)


        def specifiers(self):
            return self.getTypedRuleContext(RulepadGrammarParser.SpecifiersContext,0)


        def visibilities(self):
            return self.getTypedRuleContext(RulepadGrammarParser.VisibilitiesContext,0)


        def names(self):
            return self.getTypedRuleContext(RulepadGrammarParser.NamesContext,0)


        def extensions(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ExtensionsContext,0)


        def implementations(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ImplementationsContext,0)


        def functions(self):
            return self.getTypedRuleContext(RulepadGrammarParser.FunctionsContext,0)


        def subclasses(self):
            return self.getTypedRuleContext(RulepadGrammarParser.SubclassesContext,0)


        def abstractFunctions(self):
            return self.getTypedRuleContext(RulepadGrammarParser.AbstractFunctionsContext,0)


        def constructors(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ConstructorsContext,0)


        def declarationStatements(self):
            return self.getTypedRuleContext(RulepadGrammarParser.DeclarationStatementsContext,0)


        def returnValues(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ReturnValuesContext,0)


        def comments(self):
            return self.getTypedRuleContext(RulepadGrammarParser.CommentsContext,0)


        def binary(self):
            return self.getTypedRuleContext(RulepadGrammarParser.BinaryContext,0)


        def SPACE(self):
            return self.getToken(RulepadGrammarParser.SPACE, 0)

        def getRuleIndex(self):
            return RulepadGrammarParser.RULE_subclassExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubclassExpression" ):
                listener.enterSubclassExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubclassExpression" ):
                listener.exitSubclassExpression(self)



    def subclassExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RulepadGrammarParser.SubclassExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 132
        self.enterRecursionRule(localctx, 132, self.RULE_subclassExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 694
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,78,self._ctx)
            if la_ == 1:
                self.state = 674
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 675
                self.subclassExpression(0)
                self.state = 676
                self.match(RulepadGrammarParser.RPAREN)
                pass

            elif la_ == 2:
                self.state = 692
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,77,self._ctx)
                if la_ == 1:
                    self.state = 678
                    self.annotations()
                    pass

                elif la_ == 2:
                    self.state = 679
                    self.specifiers()
                    pass

                elif la_ == 3:
                    self.state = 680
                    self.visibilities()
                    pass

                elif la_ == 4:
                    self.state = 681
                    self.names()
                    pass

                elif la_ == 5:
                    self.state = 682
                    self.extensions()
                    pass

                elif la_ == 6:
                    self.state = 683
                    self.implementations()
                    pass

                elif la_ == 7:
                    self.state = 684
                    self.functions()
                    pass

                elif la_ == 8:
                    self.state = 685
                    self.subclasses()
                    pass

                elif la_ == 9:
                    pass

                elif la_ == 10:
                    self.state = 687
                    self.abstractFunctions()
                    pass

                elif la_ == 11:
                    self.state = 688
                    self.constructors()
                    pass

                elif la_ == 12:
                    self.state = 689
                    self.declarationStatements()
                    pass

                elif la_ == 13:
                    self.state = 690
                    self.returnValues()
                    pass

                elif la_ == 14:
                    self.state = 691
                    self.comments()
                    pass


                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 704
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,80,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 702
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,79,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.SubclassExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_subclassExpression)
                        self.state = 696
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 697
                        localctx.op = self.binary()
                        self.state = 698
                        localctx.right = self.subclassExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.SubclassExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_subclassExpression)
                        self.state = 700
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 701
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 706
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,80,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[27] = self.functionExpression_sempred
        self._predicates[31] = self.abstractFunctionExpression_sempred
        self._predicates[35] = self.constructorExpression_sempred
        self._predicates[38] = self.parameterExpression_sempred
        self._predicates[50] = self.declarationStatementExpression_sempred
        self._predicates[54] = self.expressionStatementExpression_sempred
        self._predicates[62] = self.classExpression_sempred
        self._predicates[66] = self.subclassExpression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def functionExpression_sempred(self, localctx:FunctionExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def abstractFunctionExpression_sempred(self, localctx:AbstractFunctionExpressionContext, predIndex:int):
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
         

    def declarationStatementExpression_sempred(self, localctx:DeclarationStatementExpressionContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 1)
         

    def expressionStatementExpression_sempred(self, localctx:ExpressionStatementExpressionContext, predIndex:int):
            if predIndex == 10:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 1)
         

    def classExpression_sempred(self, localctx:ClassExpressionContext, predIndex:int):
            if predIndex == 12:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 1)
         

    def subclassExpression_sempred(self, localctx:SubclassExpressionContext, predIndex:int):
            if predIndex == 14:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 1)
         




