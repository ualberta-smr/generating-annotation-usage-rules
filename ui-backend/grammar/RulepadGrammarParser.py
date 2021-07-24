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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3/")
        buf.write("\u0329\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\tL\3\2")
        buf.write("\7\2\u009a\n\2\f\2\16\2\u009d\13\2\3\2\5\2\u00a0\n\2\3")
        buf.write("\2\5\2\u00a3\n\2\3\2\7\2\u00a6\n\2\f\2\16\2\u00a9\13\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u00d0\n\3")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4\u00d9\n\4\f\4\16\4\u00dc")
        buf.write("\13\4\3\4\3\4\3\4\3\5\6\5\u00e2\n\5\r\5\16\5\u00e3\3\5")
        buf.write("\3\5\6\5\u00e8\n\5\r\5\16\5\u00e9\3\5\3\5\6\5\u00ee\n")
        buf.write("\5\r\5\16\5\u00ef\3\5\3\5\6\5\u00f4\n\5\r\5\16\5\u00f5")
        buf.write("\3\5\6\5\u00f9\n\5\r\5\16\5\u00fa\3\5\3\5\3\5\6\5\u0100")
        buf.write("\n\5\r\5\16\5\u0101\3\5\3\5\3\5\6\5\u0107\n\5\r\5\16\5")
        buf.write("\u0108\3\5\3\5\3\5\6\5\u010e\n\5\r\5\16\5\u010f\3\5\5")
        buf.write("\5\u0113\n\5\3\6\3\6\3\6\3\6\6\6\u0119\n\6\r\6\16\6\u011a")
        buf.write("\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\6\n\u0129")
        buf.write("\n\n\r\n\16\n\u012a\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r")
        buf.write("\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\5\21\u013d\n")
        buf.write("\21\3\22\3\22\5\22\u0141\n\22\3\23\3\23\3\23\3\24\3\24")
        buf.write("\5\24\u0148\n\24\3\25\3\25\3\25\5\25\u014d\n\25\3\25\5")
        buf.write("\25\u0150\n\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\5\27\u015b\n\27\3\27\3\27\3\27\3\27\3\27\3\27\7")
        buf.write("\27\u0163\n\27\f\27\16\27\u0166\13\27\3\30\3\30\3\30\3")
        buf.write("\31\3\31\3\31\3\31\3\31\5\31\u0170\n\31\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\5\33\u017a\n\33\3\34\3\34\5")
        buf.write("\34\u017e\n\34\3\34\5\34\u0181\n\34\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u0198\n\37\5\37\u019a")
        buf.write("\n\37\3\37\3\37\3\37\3\37\3\37\3\37\7\37\u01a2\n\37\f")
        buf.write("\37\16\37\u01a5\13\37\3 \3 \5 \u01a9\n \3 \5 \u01ac\n")
        buf.write(" \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3")
        buf.write("#\5#\u01bf\n#\5#\u01c1\n#\3#\3#\3#\3#\3#\3#\7#\u01c9\n")
        buf.write("#\f#\16#\u01cc\13#\3$\3$\5$\u01d0\n$\3$\5$\u01d3\n$\3")
        buf.write("%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3\'\3\'\5\'\u01e8\n\'\5\'\u01ea\n\'\3\'\3\'\3\'")
        buf.write("\3\'\3\'\3\'\7\'\u01f2\n\'\f\'\16\'\u01f5\13\'\3(\3(\5")
        buf.write("(\u01f9\n(\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\5*\u0205\n*\5")
        buf.write("*\u0207\n*\3*\3*\3*\3*\3*\3*\7*\u020f\n*\f*\16*\u0212")
        buf.write("\13*\3+\3+\5+\u0216\n+\3,\3,\3,\3,\3,\3,\5,\u021e\n,\3")
        buf.write("-\3-\5-\u0222\n-\3.\3.\3.\3/\3/\5/\u0229\n/\3\60\3\60")
        buf.write("\3\60\3\61\3\61\5\61\u0230\n\61\3\62\3\62\3\62\3\63\3")
        buf.write("\63\5\63\u0237\n\63\3\63\5\63\u023a\n\63\3\64\3\64\3\64")
        buf.write("\3\64\5\64\u0240\n\64\3\65\3\65\3\65\3\66\3\66\3\66\3")
        buf.write("\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\5\66\u0251")
        buf.write("\n\66\5\66\u0253\n\66\3\66\3\66\3\66\3\66\3\66\3\66\7")
        buf.write("\66\u025b\n\66\f\66\16\66\u025e\13\66\3\67\3\67\5\67\u0262")
        buf.write("\n\67\38\38\38\39\39\39\39\39\39\59\u026d\n9\39\39\39")
        buf.write("\39\39\39\79\u0275\n9\f9\169\u0278\139\3:\3:\5:\u027c")
        buf.write("\n:\3;\3;\3;\3<\3<\3<\3<\3<\3<\3<\5<\u0288\n<\5<\u028a")
        buf.write("\n<\3<\3<\3<\3<\3<\3<\7<\u0292\n<\f<\16<\u0295\13<\3=")
        buf.write("\3=\5=\u0299\n=\3=\5=\u029c\n=\3>\3>\3>\3>\5>\u02a2\n")
        buf.write(">\3?\3?\3?\3@\3@\3@\3@\3@\3@\3@\5@\u02ae\n@\5@\u02b0\n")
        buf.write("@\3@\3@\3@\3@\3@\3@\7@\u02b8\n@\f@\16@\u02bb\13@\3A\3")
        buf.write("A\5A\u02bf\nA\3B\3B\3B\3C\3C\5C\u02c6\nC\3C\5C\u02c9\n")
        buf.write("C\3D\3D\3D\3E\3E\3E\3F\3F\5F\u02d3\nF\3G\3G\3G\3H\3H\3")
        buf.write("H\3H\3H\3H\3H\3H\3H\3H\3H\3H\3H\3H\3H\3H\3H\3H\3H\5H\u02eb")
        buf.write("\nH\5H\u02ed\nH\3H\3H\3H\3H\3H\3H\7H\u02f5\nH\fH\16H\u02f8")
        buf.write("\13H\3I\3I\5I\u02fc\nI\3I\5I\u02ff\nI\3J\3J\3J\3K\3K\3")
        buf.write("K\3L\3L\3L\3L\3L\3L\3L\3L\3L\3L\3L\3L\3L\3L\3L\3L\3L\3")
        buf.write("L\3L\5L\u031a\nL\5L\u031c\nL\3L\3L\3L\3L\3L\3L\7L\u0324")
        buf.write("\nL\fL\16L\u0327\13L\3L\2\r,<DLRjpv~\u008e\u0096M\2\4")
        buf.write("\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084")
        buf.write("\u0086\u0088\u008a\u008c\u008e\u0090\u0092\u0094\u0096")
        buf.write("\2\3\4\2\t\16\30\31\2\u037a\2\u009f\3\2\2\2\4\u00cf\3")
        buf.write("\2\2\2\6\u00d1\3\2\2\2\b\u0112\3\2\2\2\n\u0114\3\2\2\2")
        buf.write("\f\u011e\3\2\2\2\16\u0120\3\2\2\2\20\u0122\3\2\2\2\22")
        buf.write("\u0124\3\2\2\2\24\u012e\3\2\2\2\26\u0130\3\2\2\2\30\u0132")
        buf.write("\3\2\2\2\32\u0134\3\2\2\2\34\u0136\3\2\2\2\36\u0138\3")
        buf.write("\2\2\2 \u013c\3\2\2\2\"\u013e\3\2\2\2$\u0142\3\2\2\2&")
        buf.write("\u0145\3\2\2\2(\u014f\3\2\2\2*\u0151\3\2\2\2,\u015a\3")
        buf.write("\2\2\2.\u0167\3\2\2\2\60\u016a\3\2\2\2\62\u0171\3\2\2")
        buf.write("\2\64\u0174\3\2\2\2\66\u017b\3\2\2\28\u0182\3\2\2\2:\u0185")
        buf.write("\3\2\2\2<\u0199\3\2\2\2>\u01a6\3\2\2\2@\u01ad\3\2\2\2")
        buf.write("B\u01b0\3\2\2\2D\u01c0\3\2\2\2F\u01cd\3\2\2\2H\u01d4\3")
        buf.write("\2\2\2J\u01d7\3\2\2\2L\u01e9\3\2\2\2N\u01f6\3\2\2\2P\u01fa")
        buf.write("\3\2\2\2R\u0206\3\2\2\2T\u0213\3\2\2\2V\u021d\3\2\2\2")
        buf.write("X\u021f\3\2\2\2Z\u0223\3\2\2\2\\\u0226\3\2\2\2^\u022a")
        buf.write("\3\2\2\2`\u022d\3\2\2\2b\u0231\3\2\2\2d\u0234\3\2\2\2")
        buf.write("f\u023b\3\2\2\2h\u0241\3\2\2\2j\u0252\3\2\2\2l\u025f\3")
        buf.write("\2\2\2n\u0263\3\2\2\2p\u026c\3\2\2\2r\u0279\3\2\2\2t\u027d")
        buf.write("\3\2\2\2v\u0289\3\2\2\2x\u0296\3\2\2\2z\u029d\3\2\2\2")
        buf.write("|\u02a3\3\2\2\2~\u02af\3\2\2\2\u0080\u02bc\3\2\2\2\u0082")
        buf.write("\u02c0\3\2\2\2\u0084\u02c3\3\2\2\2\u0086\u02ca\3\2\2\2")
        buf.write("\u0088\u02cd\3\2\2\2\u008a\u02d0\3\2\2\2\u008c\u02d4\3")
        buf.write("\2\2\2\u008e\u02ec\3\2\2\2\u0090\u02f9\3\2\2\2\u0092\u0300")
        buf.write("\3\2\2\2\u0094\u0303\3\2\2\2\u0096\u031b\3\2\2\2\u0098")
        buf.write("\u009a\5\20\t\2\u0099\u0098\3\2\2\2\u009a\u009d\3\2\2")
        buf.write("\2\u009b\u0099\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u00a0")
        buf.write("\3\2\2\2\u009d\u009b\3\2\2\2\u009e\u00a0\5\4\3\2\u009f")
        buf.write("\u009b\3\2\2\2\u009f\u009e\3\2\2\2\u00a0\u00a2\3\2\2\2")
        buf.write("\u00a1\u00a3\5\16\b\2\u00a2\u00a1\3\2\2\2\u00a2\u00a3")
        buf.write("\3\2\2\2\u00a3\u00a7\3\2\2\2\u00a4\u00a6\7\27\2\2\u00a5")
        buf.write("\u00a4\3\2\2\2\u00a6\u00a9\3\2\2\2\u00a7\u00a5\3\2\2\2")
        buf.write("\u00a7\u00a8\3\2\2\2\u00a8\u00aa\3\2\2\2\u00a9\u00a7\3")
        buf.write("\2\2\2\u00aa\u00ab\7\2\2\3\u00ab\3\3\2\2\2\u00ac\u00ad")
        buf.write("\5\66\34\2\u00ad\u00ae\5\24\13\2\u00ae\u00af\5\34\17\2")
        buf.write("\u00af\u00b0\5<\37\2\u00b0\u00d0\3\2\2\2\u00b1\u00b2\5")
        buf.write("> \2\u00b2\u00b3\5\24\13\2\u00b3\u00b4\5\34\17\2\u00b4")
        buf.write("\u00b5\5D#\2\u00b5\u00d0\3\2\2\2\u00b6\u00b7\5F$\2\u00b7")
        buf.write("\u00b8\5\24\13\2\u00b8\u00b9\5\34\17\2\u00b9\u00ba\5L")
        buf.write("\'\2\u00ba\u00d0\3\2\2\2\u00bb\u00bc\5\u008aF\2\u00bc")
        buf.write("\u00bd\5\24\13\2\u00bd\u00be\5\34\17\2\u00be\u00bf\5\u008e")
        buf.write("H\2\u00bf\u00d0\3\2\2\2\u00c0\u00c1\5N(\2\u00c1\u00c2")
        buf.write("\5\24\13\2\u00c2\u00c3\5\34\17\2\u00c3\u00c4\5R*\2\u00c4")
        buf.write("\u00d0\3\2\2\2\u00c5\u00c6\5d\63\2\u00c6\u00c7\5\24\13")
        buf.write("\2\u00c7\u00c8\5\34\17\2\u00c8\u00c9\5j\66\2\u00c9\u00d0")
        buf.write("\3\2\2\2\u00ca\u00cb\5\u0090I\2\u00cb\u00cc\5\24\13\2")
        buf.write("\u00cc\u00cd\5\34\17\2\u00cd\u00ce\5\u0096L\2\u00ce\u00d0")
        buf.write("\3\2\2\2\u00cf\u00ac\3\2\2\2\u00cf\u00b1\3\2\2\2\u00cf")
        buf.write("\u00b6\3\2\2\2\u00cf\u00bb\3\2\2\2\u00cf\u00c0\3\2\2\2")
        buf.write("\u00cf\u00c5\3\2\2\2\u00cf\u00ca\3\2\2\2\u00d0\5\3\2\2")
        buf.write("\2\u00d1\u00da\7\3\2\2\u00d2\u00d3\5\b\5\2\u00d3\u00d4")
        buf.write("\7\4\2\2\u00d4\u00d9\3\2\2\2\u00d5\u00d6\5\b\5\2\u00d6")
        buf.write("\u00d7\7\5\2\2\u00d7\u00d9\3\2\2\2\u00d8\u00d2\3\2\2\2")
        buf.write("\u00d8\u00d5\3\2\2\2\u00d9\u00dc\3\2\2\2\u00da\u00d8\3")
        buf.write("\2\2\2\u00da\u00db\3\2\2\2\u00db\u00dd\3\2\2\2\u00dc\u00da")
        buf.write("\3\2\2\2\u00dd\u00de\5\b\5\2\u00de\u00df\7\3\2\2\u00df")
        buf.write("\7\3\2\2\2\u00e0\u00e2\7\26\2\2\u00e1\u00e0\3\2\2\2\u00e2")
        buf.write("\u00e3\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e3\u00e4\3\2\2\2")
        buf.write("\u00e4\u0113\3\2\2\2\u00e5\u00e7\7\6\2\2\u00e6\u00e8\7")
        buf.write("\26\2\2\u00e7\u00e6\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9")
        buf.write("\u00e7\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea\u0113\3\2\2\2")
        buf.write("\u00eb\u00ed\7\7\2\2\u00ec\u00ee\7\26\2\2\u00ed\u00ec")
        buf.write("\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00ed\3\2\2\2\u00ef")
        buf.write("\u00f0\3\2\2\2\u00f0\u0113\3\2\2\2\u00f1\u00f3\7\b\2\2")
        buf.write("\u00f2\u00f4\7\26\2\2\u00f3\u00f2\3\2\2\2\u00f4\u00f5")
        buf.write("\3\2\2\2\u00f5\u00f3\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6")
        buf.write("\u0113\3\2\2\2\u00f7\u00f9\7\26\2\2\u00f8\u00f7\3\2\2")
        buf.write("\2\u00f9\u00fa\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fa\u00fb")
        buf.write("\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\u0113\7\7\2\2\u00fd")
        buf.write("\u00ff\7\6\2\2\u00fe\u0100\7\26\2\2\u00ff\u00fe\3\2\2")
        buf.write("\2\u0100\u0101\3\2\2\2\u0101\u00ff\3\2\2\2\u0101\u0102")
        buf.write("\3\2\2\2\u0102\u0103\3\2\2\2\u0103\u0113\7\7\2\2\u0104")
        buf.write("\u0106\7\7\2\2\u0105\u0107\7\26\2\2\u0106\u0105\3\2\2")
        buf.write("\2\u0107\u0108\3\2\2\2\u0108\u0106\3\2\2\2\u0108\u0109")
        buf.write("\3\2\2\2\u0109\u010a\3\2\2\2\u010a\u0113\7\7\2\2\u010b")
        buf.write("\u010d\7\b\2\2\u010c\u010e\7\26\2\2\u010d\u010c\3\2\2")
        buf.write("\2\u010e\u010f\3\2\2\2\u010f\u010d\3\2\2\2\u010f\u0110")
        buf.write("\3\2\2\2\u0110\u0111\3\2\2\2\u0111\u0113\7\7\2\2\u0112")
        buf.write("\u00e1\3\2\2\2\u0112\u00e5\3\2\2\2\u0112\u00eb\3\2\2\2")
        buf.write("\u0112\u00f1\3\2\2\2\u0112\u00f8\3\2\2\2\u0112\u00fd\3")
        buf.write("\2\2\2\u0112\u0104\3\2\2\2\u0112\u010b\3\2\2\2\u0113\t")
        buf.write("\3\2\2\2\u0114\u0118\7\3\2\2\u0115\u0119\7\26\2\2\u0116")
        buf.write("\u0119\5\f\7\2\u0117\u0119\7\25\2\2\u0118\u0115\3\2\2")
        buf.write("\2\u0118\u0116\3\2\2\2\u0118\u0117\3\2\2\2\u0119\u011a")
        buf.write("\3\2\2\2\u011a\u0118\3\2\2\2\u011a\u011b\3\2\2\2\u011b")
        buf.write("\u011c\3\2\2\2\u011c\u011d\7\3\2\2\u011d\13\3\2\2\2\u011e")
        buf.write("\u011f\t\2\2\2\u011f\r\3\2\2\2\u0120\u0121\7\t\2\2\u0121")
        buf.write("\17\3\2\2\2\u0122\u0123\7\27\2\2\u0123\21\3\2\2\2\u0124")
        buf.write("\u0128\7\3\2\2\u0125\u0129\7\26\2\2\u0126\u0129\5\f\7")
        buf.write("\2\u0127\u0129\7\25\2\2\u0128\u0125\3\2\2\2\u0128\u0126")
        buf.write("\3\2\2\2\u0128\u0127\3\2\2\2\u0129\u012a\3\2\2\2\u012a")
        buf.write("\u0128\3\2\2\2\u012a\u012b\3\2\2\2\u012b\u012c\3\2\2\2")
        buf.write("\u012c\u012d\7\3\2\2\u012d\23\3\2\2\2\u012e\u012f\7\17")
        buf.write("\2\2\u012f\25\3\2\2\2\u0130\u0131\7\20\2\2\u0131\27\3")
        buf.write("\2\2\2\u0132\u0133\7\21\2\2\u0133\31\3\2\2\2\u0134\u0135")
        buf.write("\7\22\2\2\u0135\33\3\2\2\2\u0136\u0137\7\23\2\2\u0137")
        buf.write("\35\3\2\2\2\u0138\u0139\7\24\2\2\u0139\37\3\2\2\2\u013a")
        buf.write("\u013d\5\30\r\2\u013b\u013d\5\32\16\2\u013c\u013a\3\2")
        buf.write("\2\2\u013c\u013b\3\2\2\2\u013d!\3\2\2\2\u013e\u0140\7")
        buf.write("\32\2\2\u013f\u0141\5$\23\2\u0140\u013f\3\2\2\2\u0140")
        buf.write("\u0141\3\2\2\2\u0141#\3\2\2\2\u0142\u0143\5\6\4\2\u0143")
        buf.write("\u0144\7\25\2\2\u0144%\3\2\2\2\u0145\u0147\7\33\2\2\u0146")
        buf.write("\u0148\5(\25\2\u0147\u0146\3\2\2\2\u0147\u0148\3\2\2\2")
        buf.write("\u0148\'\3\2\2\2\u0149\u014a\5\n\6\2\u014a\u014c\7\25")
        buf.write("\2\2\u014b\u014d\5*\26\2\u014c\u014b\3\2\2\2\u014c\u014d")
        buf.write("\3\2\2\2\u014d\u0150\3\2\2\2\u014e\u0150\5*\26\2\u014f")
        buf.write("\u0149\3\2\2\2\u014f\u014e\3\2\2\2\u0150)\3\2\2\2\u0151")
        buf.write("\u0152\5\36\20\2\u0152\u0153\5,\27\2\u0153+\3\2\2\2\u0154")
        buf.write("\u0155\b\27\1\2\u0155\u0156\7\30\2\2\u0156\u0157\5,\27")
        buf.write("\2\u0157\u0158\7\31\2\2\u0158\u015b\3\2\2\2\u0159\u015b")
        buf.write("\5N(\2\u015a\u0154\3\2\2\2\u015a\u0159\3\2\2\2\u015b\u0164")
        buf.write("\3\2\2\2\u015c\u015d\f\5\2\2\u015d\u015e\5 \21\2\u015e")
        buf.write("\u015f\5,\27\6\u015f\u0163\3\2\2\2\u0160\u0161\f\3\2\2")
        buf.write("\u0161\u0163\7\25\2\2\u0162\u015c\3\2\2\2\u0162\u0160")
        buf.write("\3\2\2\2\u0163\u0166\3\2\2\2\u0164\u0162\3\2\2\2\u0164")
        buf.write("\u0165\3\2\2\2\u0165-\3\2\2\2\u0166\u0164\3\2\2\2\u0167")
        buf.write("\u0168\7\34\2\2\u0168\u0169\5\60\31\2\u0169/\3\2\2\2\u016a")
        buf.write("\u016f\5\26\f\2\u016b\u016c\5\6\4\2\u016c\u016d\7\25\2")
        buf.write("\2\u016d\u0170\3\2\2\2\u016e\u0170\7\35\2\2\u016f\u016b")
        buf.write("\3\2\2\2\u016f\u016e\3\2\2\2\u0170\61\3\2\2\2\u0171\u0172")
        buf.write("\7\36\2\2\u0172\u0173\5\64\33\2\u0173\63\3\2\2\2\u0174")
        buf.write("\u0179\5\26\f\2\u0175\u0176\5\6\4\2\u0176\u0177\7\25\2")
        buf.write("\2\u0177\u017a\3\2\2\2\u0178\u017a\7\37\2\2\u0179\u0175")
        buf.write("\3\2\2\2\u0179\u0178\3\2\2\2\u017a\65\3\2\2\2\u017b\u017d")
        buf.write("\7 \2\2\u017c\u017e\5:\36\2\u017d\u017c\3\2\2\2\u017d")
        buf.write("\u017e\3\2\2\2\u017e\u0180\3\2\2\2\u017f\u0181\58\35\2")
        buf.write("\u0180\u017f\3\2\2\2\u0180\u0181\3\2\2\2\u0181\67\3\2")
        buf.write("\2\2\u0182\u0183\5\26\f\2\u0183\u0184\5\u008aF\2\u0184")
        buf.write("9\3\2\2\2\u0185\u0186\5\36\20\2\u0186\u0187\5<\37\2\u0187")
        buf.write(";\3\2\2\2\u0188\u0189\b\37\1\2\u0189\u018a\7\30\2\2\u018a")
        buf.write("\u018b\5<\37\2\u018b\u018c\7\31\2\2\u018c\u019a\3\2\2")
        buf.write("\2\u018d\u0198\5&\24\2\u018e\u0198\5X-\2\u018f\u0198\5")
        buf.write("\\/\2\u0190\u0198\5T+\2\u0191\u0198\5\"\22\2\u0192\u0198")
        buf.write("\5N(\2\u0193\u0198\5`\61\2\u0194\u0198\5d\63\2\u0195\u0198")
        buf.write("\5x=\2\u0196\u0198\5\22\n\2\u0197\u018d\3\2\2\2\u0197")
        buf.write("\u018e\3\2\2\2\u0197\u018f\3\2\2\2\u0197\u0190\3\2\2\2")
        buf.write("\u0197\u0191\3\2\2\2\u0197\u0192\3\2\2\2\u0197\u0193\3")
        buf.write("\2\2\2\u0197\u0194\3\2\2\2\u0197\u0195\3\2\2\2\u0197\u0196")
        buf.write("\3\2\2\2\u0198\u019a\3\2\2\2\u0199\u0188\3\2\2\2\u0199")
        buf.write("\u0197\3\2\2\2\u019a\u01a3\3\2\2\2\u019b\u019c\f\5\2\2")
        buf.write("\u019c\u019d\5 \21\2\u019d\u019e\5<\37\6\u019e\u01a2\3")
        buf.write("\2\2\2\u019f\u01a0\f\3\2\2\u01a0\u01a2\7\25\2\2\u01a1")
        buf.write("\u019b\3\2\2\2\u01a1\u019f\3\2\2\2\u01a2\u01a5\3\2\2\2")
        buf.write("\u01a3\u01a1\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4=\3\2\2")
        buf.write("\2\u01a5\u01a3\3\2\2\2\u01a6\u01a8\7!\2\2\u01a7\u01a9")
        buf.write("\5B\"\2\u01a8\u01a7\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9")
        buf.write("\u01ab\3\2\2\2\u01aa\u01ac\5@!\2\u01ab\u01aa\3\2\2\2\u01ab")
        buf.write("\u01ac\3\2\2\2\u01ac?\3\2\2\2\u01ad\u01ae\5\26\f\2\u01ae")
        buf.write("\u01af\5\u008aF\2\u01afA\3\2\2\2\u01b0\u01b1\5\36\20\2")
        buf.write("\u01b1\u01b2\5D#\2\u01b2C\3\2\2\2\u01b3\u01b4\b#\1\2\u01b4")
        buf.write("\u01b5\7\30\2\2\u01b5\u01b6\5D#\2\u01b6\u01b7\7\31\2\2")
        buf.write("\u01b7\u01c1\3\2\2\2\u01b8\u01bf\5&\24\2\u01b9\u01bf\5")
        buf.write("X-\2\u01ba\u01bf\5\\/\2\u01bb\u01bf\5T+\2\u01bc\u01bf")
        buf.write("\5\"\22\2\u01bd\u01bf\5N(\2\u01be\u01b8\3\2\2\2\u01be")
        buf.write("\u01b9\3\2\2\2\u01be\u01ba\3\2\2\2\u01be\u01bb\3\2\2\2")
        buf.write("\u01be\u01bc\3\2\2\2\u01be\u01bd\3\2\2\2\u01bf\u01c1\3")
        buf.write("\2\2\2\u01c0\u01b3\3\2\2\2\u01c0\u01be\3\2\2\2\u01c1\u01ca")
        buf.write("\3\2\2\2\u01c2\u01c3\f\5\2\2\u01c3\u01c4\5 \21\2\u01c4")
        buf.write("\u01c5\5D#\6\u01c5\u01c9\3\2\2\2\u01c6\u01c7\f\3\2\2\u01c7")
        buf.write("\u01c9\7\25\2\2\u01c8\u01c2\3\2\2\2\u01c8\u01c6\3\2\2")
        buf.write("\2\u01c9\u01cc\3\2\2\2\u01ca\u01c8\3\2\2\2\u01ca\u01cb")
        buf.write("\3\2\2\2\u01cbE\3\2\2\2\u01cc\u01ca\3\2\2\2\u01cd\u01cf")
        buf.write("\7\"\2\2\u01ce\u01d0\5J&\2\u01cf\u01ce\3\2\2\2\u01cf\u01d0")
        buf.write("\3\2\2\2\u01d0\u01d2\3\2\2\2\u01d1\u01d3\5H%\2\u01d2\u01d1")
        buf.write("\3\2\2\2\u01d2\u01d3\3\2\2\2\u01d3G\3\2\2\2\u01d4\u01d5")
        buf.write("\5\26\f\2\u01d5\u01d6\5\u008aF\2\u01d6I\3\2\2\2\u01d7")
        buf.write("\u01d8\5\36\20\2\u01d8\u01d9\5L\'\2\u01d9K\3\2\2\2\u01da")
        buf.write("\u01db\b\'\1\2\u01db\u01dc\7\30\2\2\u01dc\u01dd\5L\'\2")
        buf.write("\u01dd\u01de\7\31\2\2\u01de\u01ea\3\2\2\2\u01df\u01e8")
        buf.write("\5&\24\2\u01e0\u01e8\5X-\2\u01e1\u01e8\5\\/\2\u01e2\u01e8")
        buf.write("\5N(\2\u01e3\u01e8\5`\61\2\u01e4\u01e8\5d\63\2\u01e5\u01e8")
        buf.write("\5x=\2\u01e6\u01e8\5\22\n\2\u01e7\u01df\3\2\2\2\u01e7")
        buf.write("\u01e0\3\2\2\2\u01e7\u01e1\3\2\2\2\u01e7\u01e2\3\2\2\2")
        buf.write("\u01e7\u01e3\3\2\2\2\u01e7\u01e4\3\2\2\2\u01e7\u01e5\3")
        buf.write("\2\2\2\u01e7\u01e6\3\2\2\2\u01e8\u01ea\3\2\2\2\u01e9\u01da")
        buf.write("\3\2\2\2\u01e9\u01e7\3\2\2\2\u01ea\u01f3\3\2\2\2\u01eb")
        buf.write("\u01ec\f\5\2\2\u01ec\u01ed\5 \21\2\u01ed\u01ee\5L\'\6")
        buf.write("\u01ee\u01f2\3\2\2\2\u01ef\u01f0\f\3\2\2\u01f0\u01f2\7")
        buf.write("\25\2\2\u01f1\u01eb\3\2\2\2\u01f1\u01ef\3\2\2\2\u01f2")
        buf.write("\u01f5\3\2\2\2\u01f3\u01f1\3\2\2\2\u01f3\u01f4\3\2\2\2")
        buf.write("\u01f4M\3\2\2\2\u01f5\u01f3\3\2\2\2\u01f6\u01f8\7#\2\2")
        buf.write("\u01f7\u01f9\5P)\2\u01f8\u01f7\3\2\2\2\u01f8\u01f9\3\2")
        buf.write("\2\2\u01f9O\3\2\2\2\u01fa\u01fb\5\36\20\2\u01fb\u01fc")
        buf.write("\5R*\2\u01fcQ\3\2\2\2\u01fd\u01fe\b*\1\2\u01fe\u01ff\7")
        buf.write("\30\2\2\u01ff\u0200\5R*\2\u0200\u0201\7\31\2\2\u0201\u0207")
        buf.write("\3\2\2\2\u0202\u0205\5T+\2\u0203\u0205\5\"\22\2\u0204")
        buf.write("\u0202\3\2\2\2\u0204\u0203\3\2\2\2\u0205\u0207\3\2\2\2")
        buf.write("\u0206\u01fd\3\2\2\2\u0206\u0204\3\2\2\2\u0207\u0210\3")
        buf.write("\2\2\2\u0208\u0209\f\5\2\2\u0209\u020a\5 \21\2\u020a\u020b")
        buf.write("\5R*\6\u020b\u020f\3\2\2\2\u020c\u020d\f\3\2\2\u020d\u020f")
        buf.write("\7\25\2\2\u020e\u0208\3\2\2\2\u020e\u020c\3\2\2\2\u020f")
        buf.write("\u0212\3\2\2\2\u0210\u020e\3\2\2\2\u0210\u0211\3\2\2\2")
        buf.write("\u0211S\3\2\2\2\u0212\u0210\3\2\2\2\u0213\u0215\7$\2\2")
        buf.write("\u0214\u0216\5V,\2\u0215\u0214\3\2\2\2\u0215\u0216\3\2")
        buf.write("\2\2\u0216U\3\2\2\2\u0217\u0218\5\n\6\2\u0218\u0219\7")
        buf.write("\25\2\2\u0219\u021e\3\2\2\2\u021a\u021b\5\6\4\2\u021b")
        buf.write("\u021c\7\25\2\2\u021c\u021e\3\2\2\2\u021d\u0217\3\2\2")
        buf.write("\2\u021d\u021a\3\2\2\2\u021eW\3\2\2\2\u021f\u0221\7%\2")
        buf.write("\2\u0220\u0222\5Z.\2\u0221\u0220\3\2\2\2\u0221\u0222\3")
        buf.write("\2\2\2\u0222Y\3\2\2\2\u0223\u0224\5\6\4\2\u0224\u0225")
        buf.write("\7\25\2\2\u0225[\3\2\2\2\u0226\u0228\7&\2\2\u0227\u0229")
        buf.write("\5^\60\2\u0228\u0227\3\2\2\2\u0228\u0229\3\2\2\2\u0229")
        buf.write("]\3\2\2\2\u022a\u022b\5\6\4\2\u022b\u022c\7\25\2\2\u022c")
        buf.write("_\3\2\2\2\u022d\u022f\7\'\2\2\u022e\u0230\5b\62\2\u022f")
        buf.write("\u022e\3\2\2\2\u022f\u0230\3\2\2\2\u0230a\3\2\2\2\u0231")
        buf.write("\u0232\5\n\6\2\u0232\u0233\7\25\2\2\u0233c\3\2\2\2\u0234")
        buf.write("\u0236\7(\2\2\u0235\u0237\5h\65\2\u0236\u0235\3\2\2\2")
        buf.write("\u0236\u0237\3\2\2\2\u0237\u0239\3\2\2\2\u0238\u023a\5")
        buf.write("f\64\2\u0239\u0238\3\2\2\2\u0239\u023a\3\2\2\2\u023ae")
        buf.write("\3\2\2\2\u023b\u023f\5\26\f\2\u023c\u0240\5\u008aF\2\u023d")
        buf.write("\u0240\5\66\34\2\u023e\u0240\5F$\2\u023f\u023c\3\2\2\2")
        buf.write("\u023f\u023d\3\2\2\2\u023f\u023e\3\2\2\2\u0240g\3\2\2")
        buf.write("\2\u0241\u0242\5\36\20\2\u0242\u0243\5j\66\2\u0243i\3")
        buf.write("\2\2\2\u0244\u0245\b\66\1\2\u0245\u0246\7\30\2\2\u0246")
        buf.write("\u0247\5j\66\2\u0247\u0248\7\31\2\2\u0248\u0253\3\2\2")
        buf.write("\2\u0249\u0251\5&\24\2\u024a\u0251\5X-\2\u024b\u0251\5")
        buf.write("\\/\2\u024c\u0251\5T+\2\u024d\u0251\5\"\22\2\u024e\u0251")
        buf.write("\5\u0084C\2\u024f\u0251\5\22\n\2\u0250\u0249\3\2\2\2\u0250")
        buf.write("\u024a\3\2\2\2\u0250\u024b\3\2\2\2\u0250\u024c\3\2\2\2")
        buf.write("\u0250\u024d\3\2\2\2\u0250\u024e\3\2\2\2\u0250\u024f\3")
        buf.write("\2\2\2\u0251\u0253\3\2\2\2\u0252\u0244\3\2\2\2\u0252\u0250")
        buf.write("\3\2\2\2\u0253\u025c\3\2\2\2\u0254\u0255\f\5\2\2\u0255")
        buf.write("\u0256\5 \21\2\u0256\u0257\5j\66\6\u0257\u025b\3\2\2\2")
        buf.write("\u0258\u0259\f\3\2\2\u0259\u025b\7\25\2\2\u025a\u0254")
        buf.write("\3\2\2\2\u025a\u0258\3\2\2\2\u025b\u025e\3\2\2\2\u025c")
        buf.write("\u025a\3\2\2\2\u025c\u025d\3\2\2\2\u025dk\3\2\2\2\u025e")
        buf.write("\u025c\3\2\2\2\u025f\u0261\7)\2\2\u0260\u0262\5n8\2\u0261")
        buf.write("\u0260\3\2\2\2\u0261\u0262\3\2\2\2\u0262m\3\2\2\2\u0263")
        buf.write("\u0264\5\36\20\2\u0264\u0265\5p9\2\u0265o\3\2\2\2\u0266")
        buf.write("\u0267\b9\1\2\u0267\u0268\7\30\2\2\u0268\u0269\5p9\2\u0269")
        buf.write("\u026a\7\31\2\2\u026a\u026d\3\2\2\2\u026b\u026d\5r:\2")
        buf.write("\u026c\u0266\3\2\2\2\u026c\u026b\3\2\2\2\u026d\u0276\3")
        buf.write("\2\2\2\u026e\u026f\f\5\2\2\u026f\u0270\5 \21\2\u0270\u0271")
        buf.write("\5p9\6\u0271\u0275\3\2\2\2\u0272\u0273\f\3\2\2\u0273\u0275")
        buf.write("\7\25\2\2\u0274\u026e\3\2\2\2\u0274\u0272\3\2\2\2\u0275")
        buf.write("\u0278\3\2\2\2\u0276\u0274\3\2\2\2\u0276\u0277\3\2\2\2")
        buf.write("\u0277q\3\2\2\2\u0278\u0276\3\2\2\2\u0279\u027b\7*\2\2")
        buf.write("\u027a\u027c\5t;\2\u027b\u027a\3\2\2\2\u027b\u027c\3\2")
        buf.write("\2\2\u027cs\3\2\2\2\u027d\u027e\5\36\20\2\u027e\u027f")
        buf.write("\5v<\2\u027fu\3\2\2\2\u0280\u0281\b<\1\2\u0281\u0282\7")
        buf.write("\30\2\2\u0282\u0283\5v<\2\u0283\u0284\7\31\2\2\u0284\u028a")
        buf.write("\3\2\2\2\u0285\u0288\5T+\2\u0286\u0288\5\"\22\2\u0287")
        buf.write("\u0285\3\2\2\2\u0287\u0286\3\2\2\2\u0288\u028a\3\2\2\2")
        buf.write("\u0289\u0280\3\2\2\2\u0289\u0287\3\2\2\2\u028a\u0293\3")
        buf.write("\2\2\2\u028b\u028c\f\5\2\2\u028c\u028d\5 \21\2\u028d\u028e")
        buf.write("\5v<\6\u028e\u0292\3\2\2\2\u028f\u0290\f\3\2\2\u0290\u0292")
        buf.write("\7\25\2\2\u0291\u028b\3\2\2\2\u0291\u028f\3\2\2\2\u0292")
        buf.write("\u0295\3\2\2\2\u0293\u0291\3\2\2\2\u0293\u0294\3\2\2\2")
        buf.write("\u0294w\3\2\2\2\u0295\u0293\3\2\2\2\u0296\u0298\7+\2\2")
        buf.write("\u0297\u0299\5|?\2\u0298\u0297\3\2\2\2\u0298\u0299\3\2")
        buf.write("\2\2\u0299\u029b\3\2\2\2\u029a\u029c\5z>\2\u029b\u029a")
        buf.write("\3\2\2\2\u029b\u029c\3\2\2\2\u029cy\3\2\2\2\u029d\u02a1")
        buf.write("\5\26\f\2\u029e\u02a2\5\66\34\2\u029f\u02a2\5F$\2\u02a0")
        buf.write("\u02a2\5F$\2\u02a1\u029e\3\2\2\2\u02a1\u029f\3\2\2\2\u02a1")
        buf.write("\u02a0\3\2\2\2\u02a2{\3\2\2\2\u02a3\u02a4\5\36\20\2\u02a4")
        buf.write("\u02a5\5~@\2\u02a5}\3\2\2\2\u02a6\u02a7\b@\1\2\u02a7\u02a8")
        buf.write("\7\30\2\2\u02a8\u02a9\5~@\2\u02a9\u02aa\7\31\2\2\u02aa")
        buf.write("\u02b0\3\2\2\2\u02ab\u02ae\5\22\n\2\u02ac\u02ae\5\u0080")
        buf.write("A\2\u02ad\u02ab\3\2\2\2\u02ad\u02ac\3\2\2\2\u02ae\u02b0")
        buf.write("\3\2\2\2\u02af\u02a6\3\2\2\2\u02af\u02ad\3\2\2\2\u02b0")
        buf.write("\u02b9\3\2\2\2\u02b1\u02b2\f\5\2\2\u02b2\u02b3\5 \21\2")
        buf.write("\u02b3\u02b4\5~@\6\u02b4\u02b8\3\2\2\2\u02b5\u02b6\f\3")
        buf.write("\2\2\u02b6\u02b8\7\25\2\2\u02b7\u02b1\3\2\2\2\u02b7\u02b5")
        buf.write("\3\2\2\2\u02b8\u02bb\3\2\2\2\u02b9\u02b7\3\2\2\2\u02b9")
        buf.write("\u02ba\3\2\2\2\u02ba\177\3\2\2\2\u02bb\u02b9\3\2\2\2\u02bc")
        buf.write("\u02be\7,\2\2\u02bd\u02bf\5\u0082B\2\u02be\u02bd\3\2\2")
        buf.write("\2\u02be\u02bf\3\2\2\2\u02bf\u0081\3\2\2\2\u02c0\u02c1")
        buf.write("\5\n\6\2\u02c1\u02c2\7\25\2\2\u02c2\u0083\3\2\2\2\u02c3")
        buf.write("\u02c5\7-\2\2\u02c4\u02c6\5\u0088E\2\u02c5\u02c4\3\2\2")
        buf.write("\2\u02c5\u02c6\3\2\2\2\u02c6\u02c8\3\2\2\2\u02c7\u02c9")
        buf.write("\5\u0086D\2\u02c8\u02c7\3\2\2\2\u02c8\u02c9\3\2\2\2\u02c9")
        buf.write("\u0085\3\2\2\2\u02ca\u02cb\5\26\f\2\u02cb\u02cc\5d\63")
        buf.write("\2\u02cc\u0087\3\2\2\2\u02cd\u02ce\5\n\6\2\u02ce\u02cf")
        buf.write("\7\25\2\2\u02cf\u0089\3\2\2\2\u02d0\u02d2\7.\2\2\u02d1")
        buf.write("\u02d3\5\u008cG\2\u02d2\u02d1\3\2\2\2\u02d2\u02d3\3\2")
        buf.write("\2\2\u02d3\u008b\3\2\2\2\u02d4\u02d5\5\36\20\2\u02d5\u02d6")
        buf.write("\5\u008eH\2\u02d6\u008d\3\2\2\2\u02d7\u02d8\bH\1\2\u02d8")
        buf.write("\u02d9\7\30\2\2\u02d9\u02da\5\u008eH\2\u02da\u02db\7\31")
        buf.write("\2\2\u02db\u02ed\3\2\2\2\u02dc\u02eb\5&\24\2\u02dd\u02eb")
        buf.write("\5X-\2\u02de\u02eb\5\\/\2\u02df\u02eb\5\"\22\2\u02e0\u02eb")
        buf.write("\5.\30\2\u02e1\u02eb\5\62\32\2\u02e2\u02eb\5\66\34\2\u02e3")
        buf.write("\u02eb\5> \2\u02e4\u02eb\5F$\2\u02e5\u02eb\5d\63\2\u02e6")
        buf.write("\u02eb\5`\61\2\u02e7\u02eb\5\22\n\2\u02e8\u02eb\5\u0090")
        buf.write("I\2\u02e9\u02eb\5l\67\2\u02ea\u02dc\3\2\2\2\u02ea\u02dd")
        buf.write("\3\2\2\2\u02ea\u02de\3\2\2\2\u02ea\u02df\3\2\2\2\u02ea")
        buf.write("\u02e0\3\2\2\2\u02ea\u02e1\3\2\2\2\u02ea\u02e2\3\2\2\2")
        buf.write("\u02ea\u02e3\3\2\2\2\u02ea\u02e4\3\2\2\2\u02ea\u02e5\3")
        buf.write("\2\2\2\u02ea\u02e6\3\2\2\2\u02ea\u02e7\3\2\2\2\u02ea\u02e8")
        buf.write("\3\2\2\2\u02ea\u02e9\3\2\2\2\u02eb\u02ed\3\2\2\2\u02ec")
        buf.write("\u02d7\3\2\2\2\u02ec\u02ea\3\2\2\2\u02ed\u02f6\3\2\2\2")
        buf.write("\u02ee\u02ef\f\5\2\2\u02ef\u02f0\5 \21\2\u02f0\u02f1\5")
        buf.write("\u008eH\6\u02f1\u02f5\3\2\2\2\u02f2\u02f3\f\3\2\2\u02f3")
        buf.write("\u02f5\7\25\2\2\u02f4\u02ee\3\2\2\2\u02f4\u02f2\3\2\2")
        buf.write("\2\u02f5\u02f8\3\2\2\2\u02f6\u02f4\3\2\2\2\u02f6\u02f7")
        buf.write("\3\2\2\2\u02f7\u008f\3\2\2\2\u02f8\u02f6\3\2\2\2\u02f9")
        buf.write("\u02fb\7/\2\2\u02fa\u02fc\5\u0094K\2\u02fb\u02fa\3\2\2")
        buf.write("\2\u02fb\u02fc\3\2\2\2\u02fc\u02fe\3\2\2\2\u02fd\u02ff")
        buf.write("\5\u0092J\2\u02fe\u02fd\3\2\2\2\u02fe\u02ff\3\2\2\2\u02ff")
        buf.write("\u0091\3\2\2\2\u0300\u0301\5\26\f\2\u0301\u0302\5\u008a")
        buf.write("F\2\u0302\u0093\3\2\2\2\u0303\u0304\5\36\20\2\u0304\u0305")
        buf.write("\5\u0096L\2\u0305\u0095\3\2\2\2\u0306\u0307\bL\1\2\u0307")
        buf.write("\u0308\7\30\2\2\u0308\u0309\5\u0096L\2\u0309\u030a\7\31")
        buf.write("\2\2\u030a\u031c\3\2\2\2\u030b\u031a\5&\24\2\u030c\u031a")
        buf.write("\5X-\2\u030d\u031a\5\\/\2\u030e\u031a\5\"\22\2\u030f\u031a")
        buf.write("\5.\30\2\u0310\u031a\5\62\32\2\u0311\u031a\5\66\34\2\u0312")
        buf.write("\u031a\5\u0090I\2\u0313\u031a\3\2\2\2\u0314\u031a\5> ")
        buf.write("\2\u0315\u031a\5F$\2\u0316\u031a\5d\63\2\u0317\u031a\5")
        buf.write("`\61\2\u0318\u031a\5\22\n\2\u0319\u030b\3\2\2\2\u0319")
        buf.write("\u030c\3\2\2\2\u0319\u030d\3\2\2\2\u0319\u030e\3\2\2\2")
        buf.write("\u0319\u030f\3\2\2\2\u0319\u0310\3\2\2\2\u0319\u0311\3")
        buf.write("\2\2\2\u0319\u0312\3\2\2\2\u0319\u0313\3\2\2\2\u0319\u0314")
        buf.write("\3\2\2\2\u0319\u0315\3\2\2\2\u0319\u0316\3\2\2\2\u0319")
        buf.write("\u0317\3\2\2\2\u0319\u0318\3\2\2\2\u031a\u031c\3\2\2\2")
        buf.write("\u031b\u0306\3\2\2\2\u031b\u0319\3\2\2\2\u031c\u0325\3")
        buf.write("\2\2\2\u031d\u031e\f\5\2\2\u031e\u031f\5 \21\2\u031f\u0320")
        buf.write("\5\u0096L\6\u0320\u0324\3\2\2\2\u0321\u0322\f\3\2\2\u0322")
        buf.write("\u0324\7\25\2\2\u0323\u031d\3\2\2\2\u0323\u0321\3\2\2")
        buf.write("\2\u0324\u0327\3\2\2\2\u0325\u0323\3\2\2\2\u0325\u0326")
        buf.write("\3\2\2\2\u0326\u0097\3\2\2\2\u0327\u0325\3\2\2\2a\u009b")
        buf.write("\u009f\u00a2\u00a7\u00cf\u00d8\u00da\u00e3\u00e9\u00ef")
        buf.write("\u00f5\u00fa\u0101\u0108\u010f\u0112\u0118\u011a\u0128")
        buf.write("\u012a\u013c\u0140\u0147\u014c\u014f\u015a\u0162\u0164")
        buf.write("\u016f\u0179\u017d\u0180\u0197\u0199\u01a1\u01a3\u01a8")
        buf.write("\u01ab\u01be\u01c0\u01c8\u01ca\u01cf\u01d2\u01e7\u01e9")
        buf.write("\u01f1\u01f3\u01f8\u0204\u0206\u020e\u0210\u0215\u021d")
        buf.write("\u0221\u0228\u022f\u0236\u0239\u023f\u0250\u0252\u025a")
        buf.write("\u025c\u0261\u026c\u0274\u0276\u027b\u0287\u0289\u0291")
        buf.write("\u0293\u0298\u029b\u02a1\u02ad\u02af\u02b7\u02b9\u02be")
        buf.write("\u02c5\u02c8\u02d2\u02ea\u02ec\u02f4\u02f6\u02fb\u02fe")
        buf.write("\u0319\u031b\u0323\u0325")
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
                     "'declaration statement '", "'configuration file '", 
                     "'property '", "'expression statement '", "'value '", 
                     "'initial value '", "'class '", "'subclass '" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "SPACE", "Alphabet", 
                      "NL", "LPAREN", "RPAREN", "NAME", "ANNOTATION", "EXTENSION", 
                      "SUPERCLASS", "IMPLEMENTATION", "INTERFACE", "FUNCTION", 
                      "AbstractFunctions", "CONSTRUCTOR", "PARAMETER", "TYPES", 
                      "SPECIFIER", "VISIBILITY", "ReturnValue", "DeclarationStatement", 
                      "ConfigurationFile", "CONFIGURATION_PROPERTIES", "ExpressionStatement", 
                      "VALUE", "InitialValue", "CLASSES", "SUBCLASSES" ]

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
    RULE_annotationConditionTransition = 20
    RULE_annotationExpression = 21
    RULE_extensions = 22
    RULE_extensionCondition = 23
    RULE_implementations = 24
    RULE_implementationCondition = 25
    RULE_functions = 26
    RULE_functionOf = 27
    RULE_functionCondition = 28
    RULE_functionExpression = 29
    RULE_abstractFunctions = 30
    RULE_abstractFunctionOf = 31
    RULE_abstractFunctionCondition = 32
    RULE_abstractFunctionExpression = 33
    RULE_constructors = 34
    RULE_constructorOf = 35
    RULE_constructorCondition = 36
    RULE_constructorExpression = 37
    RULE_parameters = 38
    RULE_parameterCondition = 39
    RULE_parameterExpression = 40
    RULE_types = 41
    RULE_typeCondition = 42
    RULE_specifiers = 43
    RULE_specifierCondition = 44
    RULE_visibilities = 45
    RULE_visibilityCondition = 46
    RULE_returnValues = 47
    RULE_returnValueCondition = 48
    RULE_declarationStatements = 49
    RULE_declarationStatementOf = 50
    RULE_declarationStatementCondition = 51
    RULE_declarationStatementExpression = 52
    RULE_configurationFiles = 53
    RULE_configurationFileCondition = 54
    RULE_configurationFileExpression = 55
    RULE_configurationProperties = 56
    RULE_configurationPropertyCondition = 57
    RULE_configurationPropertyExpression = 58
    RULE_expressionStatements = 59
    RULE_expressionStatementOf = 60
    RULE_expressionStatementCondition = 61
    RULE_expressionStatementExpression = 62
    RULE_value = 63
    RULE_valueCondition = 64
    RULE_initialValues = 65
    RULE_initialValueOf = 66
    RULE_initialValueCondition = 67
    RULE_classes = 68
    RULE_classCondition = 69
    RULE_classExpression = 70
    RULE_subclasses = 71
    RULE_subclassOf = 72
    RULE_subclassCondition = 73
    RULE_subclassExpression = 74

    ruleNames =  [ "inputSentence", "mustClause", "words", "word", "combinatorialWords", 
                   "symbols", "end", "emptyLine", "comments", "must", "of", 
                   "and_", "or_", "have", "withWord", "binary", "names", 
                   "nameCondition", "annotations", "annotationCondition", 
                   "annotationConditionTransition", "annotationExpression", 
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
                   "declarationStatementExpression", "configurationFiles", 
                   "configurationFileCondition", "configurationFileExpression", 
                   "configurationProperties", "configurationPropertyCondition", 
                   "configurationPropertyExpression", "expressionStatements", 
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
    ConfigurationFile=39
    CONFIGURATION_PROPERTIES=40
    ExpressionStatement=41
    VALUE=42
    InitialValue=43
    CLASSES=44
    SUBCLASSES=45

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
            self.state = 157
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.EOF, RulepadGrammarParser.T__6, RulepadGrammarParser.NL]:
                self.state = 153
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 150
                        self.emptyLine() 
                    self.state = 155
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

                pass
            elif token in [RulepadGrammarParser.FUNCTION, RulepadGrammarParser.AbstractFunctions, RulepadGrammarParser.CONSTRUCTOR, RulepadGrammarParser.PARAMETER, RulepadGrammarParser.DeclarationStatement, RulepadGrammarParser.CLASSES, RulepadGrammarParser.SUBCLASSES]:
                self.state = 156
                self.mustClause()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RulepadGrammarParser.T__6:
                self.state = 159
                self.end()


            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RulepadGrammarParser.NL:
                self.state = 162
                self.match(RulepadGrammarParser.NL)
                self.state = 167
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 168
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
            self.state = 205
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.FUNCTION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.functions()
                self.state = 171
                self.must()
                self.state = 172
                self.have()
                self.state = 173
                self.functionExpression(0)
                pass
            elif token in [RulepadGrammarParser.AbstractFunctions]:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.abstractFunctions()
                self.state = 176
                self.must()
                self.state = 177
                self.have()
                self.state = 178
                self.abstractFunctionExpression(0)
                pass
            elif token in [RulepadGrammarParser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 180
                self.constructors()
                self.state = 181
                self.must()
                self.state = 182
                self.have()
                self.state = 183
                self.constructorExpression(0)
                pass
            elif token in [RulepadGrammarParser.CLASSES]:
                self.enterOuterAlt(localctx, 4)
                self.state = 185
                self.classes()
                self.state = 186
                self.must()
                self.state = 187
                self.have()
                self.state = 188
                self.classExpression(0)
                pass
            elif token in [RulepadGrammarParser.PARAMETER]:
                self.enterOuterAlt(localctx, 5)
                self.state = 190
                self.parameters()
                self.state = 191
                self.must()
                self.state = 192
                self.have()
                self.state = 193
                self.parameterExpression(0)
                pass
            elif token in [RulepadGrammarParser.DeclarationStatement]:
                self.enterOuterAlt(localctx, 6)
                self.state = 195
                self.declarationStatements()
                self.state = 196
                self.must()
                self.state = 197
                self.have()
                self.state = 198
                self.declarationStatementExpression(0)
                pass
            elif token in [RulepadGrammarParser.SUBCLASSES]:
                self.enterOuterAlt(localctx, 7)
                self.state = 200
                self.subclasses()
                self.state = 201
                self.must()
                self.state = 202
                self.have()
                self.state = 203
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
            self.state = 207
            self.match(RulepadGrammarParser.T__0)
            self.state = 216
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 214
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        self.state = 208
                        self.word()
                        self.state = 209
                        self.match(RulepadGrammarParser.T__1)
                        pass

                    elif la_ == 2:
                        self.state = 211
                        self.word()
                        self.state = 212
                        self.match(RulepadGrammarParser.T__2)
                        pass

             
                self.state = 218
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 219
            self.word()
            self.state = 220
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
            self.state = 272
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 223 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 222
                    self.match(RulepadGrammarParser.Alphabet)
                    self.state = 225 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==RulepadGrammarParser.Alphabet):
                        break

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 227
                self.match(RulepadGrammarParser.T__3)
                self.state = 229 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 228
                    self.match(RulepadGrammarParser.Alphabet)
                    self.state = 231 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==RulepadGrammarParser.Alphabet):
                        break

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 233
                self.match(RulepadGrammarParser.T__4)
                self.state = 235 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 234
                    self.match(RulepadGrammarParser.Alphabet)
                    self.state = 237 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==RulepadGrammarParser.Alphabet):
                        break

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 239
                self.match(RulepadGrammarParser.T__5)
                self.state = 241 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 240
                    self.match(RulepadGrammarParser.Alphabet)
                    self.state = 243 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==RulepadGrammarParser.Alphabet):
                        break

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 246 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 245
                    self.match(RulepadGrammarParser.Alphabet)
                    self.state = 248 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==RulepadGrammarParser.Alphabet):
                        break

                self.state = 250
                self.match(RulepadGrammarParser.T__4)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 251
                self.match(RulepadGrammarParser.T__3)
                self.state = 253 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 252
                    self.match(RulepadGrammarParser.Alphabet)
                    self.state = 255 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==RulepadGrammarParser.Alphabet):
                        break

                self.state = 257
                self.match(RulepadGrammarParser.T__4)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 258
                self.match(RulepadGrammarParser.T__4)
                self.state = 260 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 259
                    self.match(RulepadGrammarParser.Alphabet)
                    self.state = 262 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==RulepadGrammarParser.Alphabet):
                        break

                self.state = 264
                self.match(RulepadGrammarParser.T__4)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 265
                self.match(RulepadGrammarParser.T__5)
                self.state = 267 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 266
                    self.match(RulepadGrammarParser.Alphabet)
                    self.state = 269 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==RulepadGrammarParser.Alphabet):
                        break

                self.state = 271
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
            self.state = 284
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
            self.state = 286
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
            self.state = 288
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
            self.state = 290
            self.match(RulepadGrammarParser.T__0)
            self.state = 294 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 294
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.Alphabet]:
                    self.state = 291
                    self.match(RulepadGrammarParser.Alphabet)
                    pass
                elif token in [RulepadGrammarParser.T__6, RulepadGrammarParser.T__7, RulepadGrammarParser.T__8, RulepadGrammarParser.T__9, RulepadGrammarParser.T__10, RulepadGrammarParser.T__11, RulepadGrammarParser.LPAREN, RulepadGrammarParser.RPAREN]:
                    self.state = 292
                    self.symbols()
                    pass
                elif token in [RulepadGrammarParser.SPACE]:
                    self.state = 293
                    self.match(RulepadGrammarParser.SPACE)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 296 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RulepadGrammarParser.T__6) | (1 << RulepadGrammarParser.T__7) | (1 << RulepadGrammarParser.T__8) | (1 << RulepadGrammarParser.T__9) | (1 << RulepadGrammarParser.T__10) | (1 << RulepadGrammarParser.T__11) | (1 << RulepadGrammarParser.SPACE) | (1 << RulepadGrammarParser.Alphabet) | (1 << RulepadGrammarParser.LPAREN) | (1 << RulepadGrammarParser.RPAREN))) != 0)):
                    break

            self.state = 298
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
            self.state = 300
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
            self.state = 302
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
            self.state = 304
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
            self.state = 306
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
            self.state = 308
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
            self.state = 310
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
            self.state = 314
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.T__14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 312
                self.and_()
                pass
            elif token in [RulepadGrammarParser.T__15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 313
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
            self.state = 316
            self.match(RulepadGrammarParser.NAME)
            self.state = 318
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 317
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
            self.state = 320
            self.words()
            self.state = 321
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
            self.state = 323
            self.match(RulepadGrammarParser.ANNOTATION)
            self.state = 325
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 324
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
        self.enterRule(localctx, 38, self.RULE_annotationCondition)
        try:
            self.state = 333
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 327
                self.combinatorialWords()
                self.state = 328
                self.match(RulepadGrammarParser.SPACE)
                self.state = 330
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                if la_ == 1:
                    self.state = 329
                    self.annotationConditionTransition()


                pass
            elif token in [RulepadGrammarParser.T__17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 332
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
        __slots__ = 'parser'

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
        self.enterRule(localctx, 40, self.RULE_annotationConditionTransition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.withWord()
            self.state = 336
            self.annotationExpression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AnnotationExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

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
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_annotationExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 339
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 340
                self.annotationExpression(0)
                self.state = 341
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.PARAMETER]:
                self.state = 343
                self.parameters()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 354
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 352
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.AnnotationExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_annotationExpression)
                        self.state = 346
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 347
                        localctx.op = self.binary()
                        self.state = 348
                        localctx.right = self.annotationExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.AnnotationExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_annotationExpression)
                        self.state = 350
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 351
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 356
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
        self.enterRule(localctx, 44, self.RULE_extensions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.match(RulepadGrammarParser.EXTENSION)
            self.state = 358
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
        self.enterRule(localctx, 46, self.RULE_extensionCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.of()
            self.state = 365
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.T__0]:
                self.state = 361
                self.words()
                self.state = 362
                self.match(RulepadGrammarParser.SPACE)
                pass
            elif token in [RulepadGrammarParser.SUPERCLASS]:
                self.state = 364
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
        self.enterRule(localctx, 48, self.RULE_implementations)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.match(RulepadGrammarParser.IMPLEMENTATION)
            self.state = 368
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
        self.enterRule(localctx, 50, self.RULE_implementationCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.of()
            self.state = 375
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.T__0]:
                self.state = 371
                self.words()
                self.state = 372
                self.match(RulepadGrammarParser.SPACE)
                pass
            elif token in [RulepadGrammarParser.INTERFACE]:
                self.state = 374
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
        self.enterRule(localctx, 52, self.RULE_functions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self.match(RulepadGrammarParser.FUNCTION)
            self.state = 379
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 378
                self.functionCondition()


            self.state = 382
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 381
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
        self.enterRule(localctx, 54, self.RULE_functionOf)
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
        self.enterRule(localctx, 56, self.RULE_functionCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.withWord()
            self.state = 388
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
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_functionExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 391
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 392
                self.functionExpression(0)
                self.state = 393
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.T__0, RulepadGrammarParser.NAME, RulepadGrammarParser.ANNOTATION, RulepadGrammarParser.PARAMETER, RulepadGrammarParser.TYPES, RulepadGrammarParser.SPECIFIER, RulepadGrammarParser.VISIBILITY, RulepadGrammarParser.ReturnValue, RulepadGrammarParser.DeclarationStatement, RulepadGrammarParser.ExpressionStatement]:
                self.state = 405
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
                elif token in [RulepadGrammarParser.ReturnValue]:
                    self.state = 401
                    self.returnValues()
                    pass
                elif token in [RulepadGrammarParser.DeclarationStatement]:
                    self.state = 402
                    self.declarationStatements()
                    pass
                elif token in [RulepadGrammarParser.ExpressionStatement]:
                    self.state = 403
                    self.expressionStatements()
                    pass
                elif token in [RulepadGrammarParser.T__0]:
                    self.state = 404
                    self.comments()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 417
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 415
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.FunctionExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_functionExpression)
                        self.state = 409
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 410
                        localctx.op = self.binary()
                        self.state = 411
                        localctx.right = self.functionExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.FunctionExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_functionExpression)
                        self.state = 413
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 414
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 419
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

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
        self.enterRule(localctx, 60, self.RULE_abstractFunctions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.match(RulepadGrammarParser.AbstractFunctions)
            self.state = 422
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 421
                self.abstractFunctionCondition()


            self.state = 425
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 424
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
        self.enterRule(localctx, 62, self.RULE_abstractFunctionOf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 427
            self.of()
            self.state = 428
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
        self.enterRule(localctx, 64, self.RULE_abstractFunctionCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 430
            self.withWord()
            self.state = 431
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
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_abstractFunctionExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 446
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 434
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 435
                self.abstractFunctionExpression(0)
                self.state = 436
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.NAME, RulepadGrammarParser.ANNOTATION, RulepadGrammarParser.PARAMETER, RulepadGrammarParser.TYPES, RulepadGrammarParser.SPECIFIER, RulepadGrammarParser.VISIBILITY]:
                self.state = 444
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.ANNOTATION]:
                    self.state = 438
                    self.annotations()
                    pass
                elif token in [RulepadGrammarParser.SPECIFIER]:
                    self.state = 439
                    self.specifiers()
                    pass
                elif token in [RulepadGrammarParser.VISIBILITY]:
                    self.state = 440
                    self.visibilities()
                    pass
                elif token in [RulepadGrammarParser.TYPES]:
                    self.state = 441
                    self.types()
                    pass
                elif token in [RulepadGrammarParser.NAME]:
                    self.state = 442
                    self.names()
                    pass
                elif token in [RulepadGrammarParser.PARAMETER]:
                    self.state = 443
                    self.parameters()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 456
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 454
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.AbstractFunctionExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_abstractFunctionExpression)
                        self.state = 448
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 449
                        localctx.op = self.binary()
                        self.state = 450
                        localctx.right = self.abstractFunctionExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.AbstractFunctionExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_abstractFunctionExpression)
                        self.state = 452
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 453
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 458
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

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
        self.enterRule(localctx, 68, self.RULE_constructors)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 459
            self.match(RulepadGrammarParser.CONSTRUCTOR)
            self.state = 461
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 460
                self.constructorCondition()


            self.state = 464
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.state = 463
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
        self.enterRule(localctx, 70, self.RULE_constructorOf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
            self.of()
            self.state = 467
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
        self.enterRule(localctx, 72, self.RULE_constructorCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 469
            self.withWord()
            self.state = 470
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
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_constructorExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 487
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 473
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 474
                self.constructorExpression(0)
                self.state = 475
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.T__0, RulepadGrammarParser.ANNOTATION, RulepadGrammarParser.PARAMETER, RulepadGrammarParser.SPECIFIER, RulepadGrammarParser.VISIBILITY, RulepadGrammarParser.ReturnValue, RulepadGrammarParser.DeclarationStatement, RulepadGrammarParser.ExpressionStatement]:
                self.state = 485
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.ANNOTATION]:
                    self.state = 477
                    self.annotations()
                    pass
                elif token in [RulepadGrammarParser.SPECIFIER]:
                    self.state = 478
                    self.specifiers()
                    pass
                elif token in [RulepadGrammarParser.VISIBILITY]:
                    self.state = 479
                    self.visibilities()
                    pass
                elif token in [RulepadGrammarParser.PARAMETER]:
                    self.state = 480
                    self.parameters()
                    pass
                elif token in [RulepadGrammarParser.ReturnValue]:
                    self.state = 481
                    self.returnValues()
                    pass
                elif token in [RulepadGrammarParser.DeclarationStatement]:
                    self.state = 482
                    self.declarationStatements()
                    pass
                elif token in [RulepadGrammarParser.ExpressionStatement]:
                    self.state = 483
                    self.expressionStatements()
                    pass
                elif token in [RulepadGrammarParser.T__0]:
                    self.state = 484
                    self.comments()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 497
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 495
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.ConstructorExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_constructorExpression)
                        self.state = 489
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 490
                        localctx.op = self.binary()
                        self.state = 491
                        localctx.right = self.constructorExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.ConstructorExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_constructorExpression)
                        self.state = 493
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 494
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 499
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

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
        self.enterRule(localctx, 76, self.RULE_parameters)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 500
            self.match(RulepadGrammarParser.PARAMETER)
            self.state = 502
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.state = 501
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
        self.enterRule(localctx, 78, self.RULE_parameterCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
            self.withWord()
            self.state = 505
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
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_parameterExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 516
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 508
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 509
                self.parameterExpression(0)
                self.state = 510
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.NAME, RulepadGrammarParser.TYPES]:
                self.state = 514
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.TYPES]:
                    self.state = 512
                    self.types()
                    pass
                elif token in [RulepadGrammarParser.NAME]:
                    self.state = 513
                    self.names()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 526
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,52,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 524
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.ParameterExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_parameterExpression)
                        self.state = 518
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 519
                        localctx.op = self.binary()
                        self.state = 520
                        localctx.right = self.parameterExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.ParameterExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_parameterExpression)
                        self.state = 522
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 523
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 528
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,52,self._ctx)

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
        self.enterRule(localctx, 82, self.RULE_types)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 529
            self.match(RulepadGrammarParser.TYPES)
            self.state = 531
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.state = 530
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
        self.enterRule(localctx, 84, self.RULE_typeCondition)
        try:
            self.state = 539
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 533
                self.combinatorialWords()
                self.state = 534
                self.match(RulepadGrammarParser.SPACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 536
                self.words()
                self.state = 537
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
        self.enterRule(localctx, 86, self.RULE_specifiers)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 541
            self.match(RulepadGrammarParser.SPECIFIER)
            self.state = 543
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                self.state = 542
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
        self.enterRule(localctx, 88, self.RULE_specifierCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 545
            self.words()
            self.state = 546
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
        self.enterRule(localctx, 90, self.RULE_visibilities)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 548
            self.match(RulepadGrammarParser.VISIBILITY)
            self.state = 550
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
            if la_ == 1:
                self.state = 549
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
        self.enterRule(localctx, 92, self.RULE_visibilityCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 552
            self.words()
            self.state = 553
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
        self.enterRule(localctx, 94, self.RULE_returnValues)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 555
            self.match(RulepadGrammarParser.ReturnValue)
            self.state = 557
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.state = 556
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
        self.enterRule(localctx, 96, self.RULE_returnValueCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 559
            self.combinatorialWords()
            self.state = 560
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
        self.enterRule(localctx, 98, self.RULE_declarationStatements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 562
            self.match(RulepadGrammarParser.DeclarationStatement)
            self.state = 564
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
            if la_ == 1:
                self.state = 563
                self.declarationStatementCondition()


            self.state = 567
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
            if la_ == 1:
                self.state = 566
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
        self.enterRule(localctx, 100, self.RULE_declarationStatementOf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 569
            self.of()
            self.state = 573
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.CLASSES]:
                self.state = 570
                self.classes()
                pass
            elif token in [RulepadGrammarParser.FUNCTION]:
                self.state = 571
                self.functions()
                pass
            elif token in [RulepadGrammarParser.CONSTRUCTOR]:
                self.state = 572
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
        self.enterRule(localctx, 102, self.RULE_declarationStatementCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 575
            self.withWord()
            self.state = 576
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
        _startState = 104
        self.enterRecursionRule(localctx, 104, self.RULE_declarationStatementExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 592
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 579
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 580
                self.declarationStatementExpression(0)
                self.state = 581
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.T__0, RulepadGrammarParser.NAME, RulepadGrammarParser.ANNOTATION, RulepadGrammarParser.TYPES, RulepadGrammarParser.SPECIFIER, RulepadGrammarParser.VISIBILITY, RulepadGrammarParser.InitialValue]:
                self.state = 590
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.ANNOTATION]:
                    self.state = 583
                    self.annotations()
                    pass
                elif token in [RulepadGrammarParser.SPECIFIER]:
                    self.state = 584
                    self.specifiers()
                    pass
                elif token in [RulepadGrammarParser.VISIBILITY]:
                    self.state = 585
                    self.visibilities()
                    pass
                elif token in [RulepadGrammarParser.TYPES]:
                    self.state = 586
                    self.types()
                    pass
                elif token in [RulepadGrammarParser.NAME]:
                    self.state = 587
                    self.names()
                    pass
                elif token in [RulepadGrammarParser.InitialValue]:
                    self.state = 588
                    self.initialValues()
                    pass
                elif token in [RulepadGrammarParser.T__0]:
                    self.state = 589
                    self.comments()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 602
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,64,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 600
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.DeclarationStatementExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_declarationStatementExpression)
                        self.state = 594
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 595
                        localctx.op = self.binary()
                        self.state = 596
                        localctx.right = self.declarationStatementExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.DeclarationStatementExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_declarationStatementExpression)
                        self.state = 598
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 599
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 604
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,64,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ConfigurationFilesContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 106, self.RULE_configurationFiles)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 605
            self.match(RulepadGrammarParser.ConfigurationFile)
            self.state = 607
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
            if la_ == 1:
                self.state = 606
                self.configurationFileCondition()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConfigurationFileConditionContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 108, self.RULE_configurationFileCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 609
            self.withWord()
            self.state = 610
            self.configurationFileExpression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConfigurationFileExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

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
        _startState = 110
        self.enterRecursionRule(localctx, 110, self.RULE_configurationFileExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 618
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 613
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 614
                self.configurationFileExpression(0)
                self.state = 615
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.CONFIGURATION_PROPERTIES]:
                self.state = 617
                self.configurationProperties()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 628
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,68,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 626
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,67,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.ConfigurationFileExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_configurationFileExpression)
                        self.state = 620
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 621
                        localctx.op = self.binary()
                        self.state = 622
                        localctx.right = self.configurationFileExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.ConfigurationFileExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_configurationFileExpression)
                        self.state = 624
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 625
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 630
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,68,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ConfigurationPropertiesContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 112, self.RULE_configurationProperties)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 631
            self.match(RulepadGrammarParser.CONFIGURATION_PROPERTIES)
            self.state = 633
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,69,self._ctx)
            if la_ == 1:
                self.state = 632
                self.configurationPropertyCondition()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConfigurationPropertyConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def withWord(self):
            return self.getTypedRuleContext(RulepadGrammarParser.WithWordContext,0)


        def configurationPropertyExpression(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ConfigurationPropertyExpressionContext,0)


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
        self.enterRule(localctx, 114, self.RULE_configurationPropertyCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 635
            self.withWord()
            self.state = 636
            self.configurationPropertyExpression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConfigurationPropertyExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

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
        _startState = 116
        self.enterRecursionRule(localctx, 116, self.RULE_configurationPropertyExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 647
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 639
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 640
                self.configurationPropertyExpression(0)
                self.state = 641
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.NAME, RulepadGrammarParser.TYPES]:
                self.state = 645
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.TYPES]:
                    self.state = 643
                    self.types()
                    pass
                elif token in [RulepadGrammarParser.NAME]:
                    self.state = 644
                    self.names()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 657
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,73,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 655
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,72,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.ConfigurationPropertyExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_configurationPropertyExpression)
                        self.state = 649
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 650
                        localctx.op = self.binary()
                        self.state = 651
                        localctx.right = self.configurationPropertyExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.ConfigurationPropertyExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_configurationPropertyExpression)
                        self.state = 653
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 654
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 659
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,73,self._ctx)

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
        self.enterRule(localctx, 118, self.RULE_expressionStatements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 660
            self.match(RulepadGrammarParser.ExpressionStatement)
            self.state = 662
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,74,self._ctx)
            if la_ == 1:
                self.state = 661
                self.expressionStatementCondition()


            self.state = 665
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,75,self._ctx)
            if la_ == 1:
                self.state = 664
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
        self.enterRule(localctx, 120, self.RULE_expressionStatementOf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 667
            self.of()
            self.state = 671
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,76,self._ctx)
            if la_ == 1:
                self.state = 668
                self.functions()
                pass

            elif la_ == 2:
                self.state = 669
                self.constructors()
                pass

            elif la_ == 3:
                self.state = 670
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
        self.enterRule(localctx, 122, self.RULE_expressionStatementCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 673
            self.withWord()
            self.state = 674
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
        _startState = 124
        self.enterRecursionRule(localctx, 124, self.RULE_expressionStatementExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 685
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 677
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 678
                self.expressionStatementExpression(0)
                self.state = 679
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.T__0, RulepadGrammarParser.VALUE]:
                self.state = 683
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.T__0]:
                    self.state = 681
                    self.comments()
                    pass
                elif token in [RulepadGrammarParser.VALUE]:
                    self.state = 682
                    self.value()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 695
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,80,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 693
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,79,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.ExpressionStatementExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressionStatementExpression)
                        self.state = 687
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 688
                        localctx.op = self.binary()
                        self.state = 689
                        localctx.right = self.expressionStatementExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.ExpressionStatementExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressionStatementExpression)
                        self.state = 691
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 692
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 697
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,80,self._ctx)

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
        self.enterRule(localctx, 126, self.RULE_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 698
            self.match(RulepadGrammarParser.VALUE)
            self.state = 700
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,81,self._ctx)
            if la_ == 1:
                self.state = 699
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
        self.enterRule(localctx, 128, self.RULE_valueCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 702
            self.combinatorialWords()
            self.state = 703
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
        self.enterRule(localctx, 130, self.RULE_initialValues)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 705
            self.match(RulepadGrammarParser.InitialValue)
            self.state = 707
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,82,self._ctx)
            if la_ == 1:
                self.state = 706
                self.initialValueCondition()


            self.state = 710
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,83,self._ctx)
            if la_ == 1:
                self.state = 709
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
        self.enterRule(localctx, 132, self.RULE_initialValueOf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 712
            self.of()
            self.state = 713
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
        self.enterRule(localctx, 134, self.RULE_initialValueCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 715
            self.combinatorialWords()
            self.state = 716
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
        self.enterRule(localctx, 136, self.RULE_classes)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 718
            self.match(RulepadGrammarParser.CLASSES)
            self.state = 720
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,84,self._ctx)
            if la_ == 1:
                self.state = 719
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
        self.enterRule(localctx, 138, self.RULE_classCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 722
            self.withWord()
            self.state = 723
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


        def configurationFiles(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ConfigurationFilesContext,0)


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
        _startState = 140
        self.enterRecursionRule(localctx, 140, self.RULE_classExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 746
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 726
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 727
                self.classExpression(0)
                self.state = 728
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.T__0, RulepadGrammarParser.NAME, RulepadGrammarParser.ANNOTATION, RulepadGrammarParser.EXTENSION, RulepadGrammarParser.IMPLEMENTATION, RulepadGrammarParser.FUNCTION, RulepadGrammarParser.AbstractFunctions, RulepadGrammarParser.CONSTRUCTOR, RulepadGrammarParser.SPECIFIER, RulepadGrammarParser.VISIBILITY, RulepadGrammarParser.ReturnValue, RulepadGrammarParser.DeclarationStatement, RulepadGrammarParser.ConfigurationFile, RulepadGrammarParser.SUBCLASSES]:
                self.state = 744
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.ANNOTATION]:
                    self.state = 730
                    self.annotations()
                    pass
                elif token in [RulepadGrammarParser.SPECIFIER]:
                    self.state = 731
                    self.specifiers()
                    pass
                elif token in [RulepadGrammarParser.VISIBILITY]:
                    self.state = 732
                    self.visibilities()
                    pass
                elif token in [RulepadGrammarParser.NAME]:
                    self.state = 733
                    self.names()
                    pass
                elif token in [RulepadGrammarParser.EXTENSION]:
                    self.state = 734
                    self.extensions()
                    pass
                elif token in [RulepadGrammarParser.IMPLEMENTATION]:
                    self.state = 735
                    self.implementations()
                    pass
                elif token in [RulepadGrammarParser.FUNCTION]:
                    self.state = 736
                    self.functions()
                    pass
                elif token in [RulepadGrammarParser.AbstractFunctions]:
                    self.state = 737
                    self.abstractFunctions()
                    pass
                elif token in [RulepadGrammarParser.CONSTRUCTOR]:
                    self.state = 738
                    self.constructors()
                    pass
                elif token in [RulepadGrammarParser.DeclarationStatement]:
                    self.state = 739
                    self.declarationStatements()
                    pass
                elif token in [RulepadGrammarParser.ReturnValue]:
                    self.state = 740
                    self.returnValues()
                    pass
                elif token in [RulepadGrammarParser.T__0]:
                    self.state = 741
                    self.comments()
                    pass
                elif token in [RulepadGrammarParser.SUBCLASSES]:
                    self.state = 742
                    self.subclasses()
                    pass
                elif token in [RulepadGrammarParser.ConfigurationFile]:
                    self.state = 743
                    self.configurationFiles()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 756
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,88,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 754
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,87,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.ClassExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_classExpression)
                        self.state = 748
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 749
                        localctx.op = self.binary()
                        self.state = 750
                        localctx.right = self.classExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.ClassExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_classExpression)
                        self.state = 752
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 753
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 758
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,88,self._ctx)

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
        self.enterRule(localctx, 142, self.RULE_subclasses)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 759
            self.match(RulepadGrammarParser.SUBCLASSES)
            self.state = 761
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,89,self._ctx)
            if la_ == 1:
                self.state = 760
                self.subclassCondition()


            self.state = 764
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,90,self._ctx)
            if la_ == 1:
                self.state = 763
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
        self.enterRule(localctx, 144, self.RULE_subclassOf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 766
            self.of()
            self.state = 767
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
        self.enterRule(localctx, 146, self.RULE_subclassCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 769
            self.withWord()
            self.state = 770
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
        _startState = 148
        self.enterRecursionRule(localctx, 148, self.RULE_subclassExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 793
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,92,self._ctx)
            if la_ == 1:
                self.state = 773
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 774
                self.subclassExpression(0)
                self.state = 775
                self.match(RulepadGrammarParser.RPAREN)
                pass

            elif la_ == 2:
                self.state = 791
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,91,self._ctx)
                if la_ == 1:
                    self.state = 777
                    self.annotations()
                    pass

                elif la_ == 2:
                    self.state = 778
                    self.specifiers()
                    pass

                elif la_ == 3:
                    self.state = 779
                    self.visibilities()
                    pass

                elif la_ == 4:
                    self.state = 780
                    self.names()
                    pass

                elif la_ == 5:
                    self.state = 781
                    self.extensions()
                    pass

                elif la_ == 6:
                    self.state = 782
                    self.implementations()
                    pass

                elif la_ == 7:
                    self.state = 783
                    self.functions()
                    pass

                elif la_ == 8:
                    self.state = 784
                    self.subclasses()
                    pass

                elif la_ == 9:
                    pass

                elif la_ == 10:
                    self.state = 786
                    self.abstractFunctions()
                    pass

                elif la_ == 11:
                    self.state = 787
                    self.constructors()
                    pass

                elif la_ == 12:
                    self.state = 788
                    self.declarationStatements()
                    pass

                elif la_ == 13:
                    self.state = 789
                    self.returnValues()
                    pass

                elif la_ == 14:
                    self.state = 790
                    self.comments()
                    pass


                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 803
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,94,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 801
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,93,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.SubclassExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_subclassExpression)
                        self.state = 795
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 796
                        localctx.op = self.binary()
                        self.state = 797
                        localctx.right = self.subclassExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.SubclassExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_subclassExpression)
                        self.state = 799
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 800
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 805
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,94,self._ctx)

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
        self._predicates[21] = self.annotationExpression_sempred
        self._predicates[29] = self.functionExpression_sempred
        self._predicates[33] = self.abstractFunctionExpression_sempred
        self._predicates[37] = self.constructorExpression_sempred
        self._predicates[40] = self.parameterExpression_sempred
        self._predicates[52] = self.declarationStatementExpression_sempred
        self._predicates[55] = self.configurationFileExpression_sempred
        self._predicates[58] = self.configurationPropertyExpression_sempred
        self._predicates[62] = self.expressionStatementExpression_sempred
        self._predicates[70] = self.classExpression_sempred
        self._predicates[74] = self.subclassExpression_sempred
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
         

    def abstractFunctionExpression_sempred(self, localctx:AbstractFunctionExpressionContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 1)
         

    def constructorExpression_sempred(self, localctx:ConstructorExpressionContext, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 1)
         

    def parameterExpression_sempred(self, localctx:ParameterExpressionContext, predIndex:int):
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
         

    def expressionStatementExpression_sempred(self, localctx:ExpressionStatementExpressionContext, predIndex:int):
            if predIndex == 16:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 17:
                return self.precpred(self._ctx, 1)
         

    def classExpression_sempred(self, localctx:ClassExpressionContext, predIndex:int):
            if predIndex == 18:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 19:
                return self.precpred(self._ctx, 1)
         

    def subclassExpression_sempred(self, localctx:SubclassExpressionContext, predIndex:int):
            if predIndex == 20:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 21:
                return self.precpred(self._ctx, 1)
         




