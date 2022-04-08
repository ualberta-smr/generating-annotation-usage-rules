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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\62")
        buf.write("\u035f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\tL\4M\t")
        buf.write("M\4N\tN\4O\tO\4P\tP\3\2\7\2\u00a2\n\2\f\2\16\2\u00a5\13")
        buf.write("\2\3\2\5\2\u00a8\n\2\3\2\5\2\u00ab\n\2\3\2\7\2\u00ae\n")
        buf.write("\2\f\2\16\2\u00b1\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\5\3\u00d8\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4")
        buf.write("\u00e1\n\4\f\4\16\4\u00e4\13\4\3\4\3\4\3\4\3\5\6\5\u00ea")
        buf.write("\n\5\r\5\16\5\u00eb\3\5\3\5\6\5\u00f0\n\5\r\5\16\5\u00f1")
        buf.write("\3\5\3\5\6\5\u00f6\n\5\r\5\16\5\u00f7\3\5\3\5\6\5\u00fc")
        buf.write("\n\5\r\5\16\5\u00fd\3\5\6\5\u0101\n\5\r\5\16\5\u0102\3")
        buf.write("\5\3\5\3\5\6\5\u0108\n\5\r\5\16\5\u0109\3\5\3\5\3\5\6")
        buf.write("\5\u010f\n\5\r\5\16\5\u0110\3\5\3\5\3\5\6\5\u0116\n\5")
        buf.write("\r\5\16\5\u0117\3\5\5\5\u011b\n\5\3\6\3\6\3\6\3\6\6\6")
        buf.write("\u0121\n\6\r\6\16\6\u0122\3\6\3\6\3\7\3\7\3\b\3\b\3\t")
        buf.write("\3\t\3\n\3\n\3\n\3\n\6\n\u0131\n\n\r\n\16\n\u0132\3\n")
        buf.write("\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20")
        buf.write("\3\20\3\21\3\21\5\21\u0145\n\21\3\22\3\22\5\22\u0149\n")
        buf.write("\22\3\23\3\23\3\23\3\24\3\24\5\24\u0150\n\24\3\25\3\25")
        buf.write("\3\25\5\25\u0155\n\25\3\25\5\25\u0158\n\25\3\26\3\26\3")
        buf.write("\26\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u0163\n\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\7\27\u016b\n\27\f\27\16\27\u016e")
        buf.write("\13\27\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\5\31\u0178")
        buf.write("\n\31\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\5\33\u0182")
        buf.write("\n\33\3\34\3\34\5\34\u0186\n\34\3\34\5\34\u0189\n\34\3")
        buf.write("\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u019f")
        buf.write("\n\37\5\37\u01a1\n\37\3\37\3\37\3\37\3\37\3\37\3\37\7")
        buf.write("\37\u01a9\n\37\f\37\16\37\u01ac\13\37\3 \3 \5 \u01b0\n")
        buf.write(" \3 \5 \u01b3\n \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3#\3#\3")
        buf.write("#\3#\3#\3#\3#\3#\5#\u01c6\n#\5#\u01c8\n#\3#\3#\3#\3#\3")
        buf.write("#\3#\7#\u01d0\n#\f#\16#\u01d3\13#\3$\3$\5$\u01d7\n$\3")
        buf.write("$\5$\u01da\n$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\5\'\u01ef\n\'\5\'\u01f1")
        buf.write("\n\'\3\'\3\'\3\'\3\'\3\'\3\'\7\'\u01f9\n\'\f\'\16\'\u01fc")
        buf.write("\13\'\3(\3(\5(\u0200\n(\3)\3)\3)\3)\3)\3)\5)\u0208\n)")
        buf.write("\3*\3*\3*\3*\3*\3*\3*\5*\u0211\n*\5*\u0213\n*\3*\3*\3")
        buf.write("*\3*\3*\3*\7*\u021b\n*\f*\16*\u021e\13*\3+\3+\5+\u0222")
        buf.write("\n+\3,\3,\3,\5,\u0227\n,\3,\5,\u022a\n,\3-\3-\3-\3.\3")
        buf.write(".\3.\3.\3.\3.\3.\3.\5.\u0237\n.\5.\u0239\n.\3.\3.\3.\3")
        buf.write(".\3.\3.\7.\u0241\n.\f.\16.\u0244\13.\3/\3/\5/\u0248\n")
        buf.write("/\3\60\3\60\3\60\3\60\3\60\3\60\5\60\u0250\n\60\3\61\3")
        buf.write("\61\5\61\u0254\n\61\3\62\3\62\3\62\3\63\3\63\5\63\u025b")
        buf.write("\n\63\3\64\3\64\3\64\3\65\3\65\5\65\u0262\n\65\3\66\3")
        buf.write("\66\3\66\3\67\3\67\5\67\u0269\n\67\3\67\5\67\u026c\n\67")
        buf.write("\38\38\38\38\58\u0272\n8\39\39\39\3:\3:\3:\3:\3:\3:\3")
        buf.write(":\3:\3:\3:\3:\3:\5:\u0283\n:\5:\u0285\n:\3:\3:\3:\3:\3")
        buf.write(":\3:\7:\u028d\n:\f:\16:\u0290\13:\3;\3;\5;\u0294\n;\3")
        buf.write("<\3<\3<\3=\3=\3=\3=\3=\3=\5=\u029f\n=\3=\3=\3=\3=\3=\3")
        buf.write("=\7=\u02a7\n=\f=\16=\u02aa\13=\3>\3>\3>\3?\3?\3?\3?\3")
        buf.write("?\3?\5?\u02b5\n?\3@\3@\3@\3@\3@\3@\3@\5@\u02be\n@\5@\u02c0")
        buf.write("\n@\3@\3@\3@\3@\3@\3@\7@\u02c8\n@\f@\16@\u02cb\13@\3A")
        buf.write("\3A\5A\u02cf\nA\3A\5A\u02d2\nA\3B\3B\3B\3B\5B\u02d8\n")
        buf.write("B\3C\3C\3C\3D\3D\3D\3D\3D\3D\3D\5D\u02e4\nD\5D\u02e6\n")
        buf.write("D\3D\3D\3D\3D\3D\3D\7D\u02ee\nD\fD\16D\u02f1\13D\3E\3")
        buf.write("E\5E\u02f5\nE\3F\3F\3F\3G\3G\5G\u02fc\nG\3G\5G\u02ff\n")
        buf.write("G\3H\3H\3H\3I\3I\3I\3J\3J\5J\u0309\nJ\3K\3K\3K\3L\3L\3")
        buf.write("L\3L\3L\3L\3L\3L\3L\3L\3L\3L\3L\3L\3L\3L\3L\3L\3L\5L\u0321")
        buf.write("\nL\5L\u0323\nL\3L\3L\3L\3L\3L\3L\7L\u032b\nL\fL\16L\u032e")
        buf.write("\13L\3M\3M\5M\u0332\nM\3M\5M\u0335\nM\3N\3N\3N\3O\3O\3")
        buf.write("O\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3")
        buf.write("P\3P\5P\u0350\nP\5P\u0352\nP\3P\3P\3P\3P\3P\3P\7P\u035a")
        buf.write("\nP\fP\16P\u035d\13P\3P\2\16,<DLRZrx~\u0086\u0096\u009e")
        buf.write("Q\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write("\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082")
        buf.write("\u0084\u0086\u0088\u008a\u008c\u008e\u0090\u0092\u0094")
        buf.write("\u0096\u0098\u009a\u009c\u009e\2\3\4\2\t\21\33\34\2\u03b4")
        buf.write("\2\u00a7\3\2\2\2\4\u00d7\3\2\2\2\6\u00d9\3\2\2\2\b\u011a")
        buf.write("\3\2\2\2\n\u011c\3\2\2\2\f\u0126\3\2\2\2\16\u0128\3\2")
        buf.write("\2\2\20\u012a\3\2\2\2\22\u012c\3\2\2\2\24\u0136\3\2\2")
        buf.write("\2\26\u0138\3\2\2\2\30\u013a\3\2\2\2\32\u013c\3\2\2\2")
        buf.write("\34\u013e\3\2\2\2\36\u0140\3\2\2\2 \u0144\3\2\2\2\"\u0146")
        buf.write("\3\2\2\2$\u014a\3\2\2\2&\u014d\3\2\2\2(\u0157\3\2\2\2")
        buf.write("*\u0159\3\2\2\2,\u0162\3\2\2\2.\u016f\3\2\2\2\60\u0172")
        buf.write("\3\2\2\2\62\u0179\3\2\2\2\64\u017c\3\2\2\2\66\u0183\3")
        buf.write("\2\2\28\u018a\3\2\2\2:\u018d\3\2\2\2<\u01a0\3\2\2\2>\u01ad")
        buf.write("\3\2\2\2@\u01b4\3\2\2\2B\u01b7\3\2\2\2D\u01c7\3\2\2\2")
        buf.write("F\u01d4\3\2\2\2H\u01db\3\2\2\2J\u01de\3\2\2\2L\u01f0\3")
        buf.write("\2\2\2N\u01fd\3\2\2\2P\u0207\3\2\2\2R\u0212\3\2\2\2T\u021f")
        buf.write("\3\2\2\2V\u0229\3\2\2\2X\u022b\3\2\2\2Z\u0238\3\2\2\2")
        buf.write("\\\u0245\3\2\2\2^\u024f\3\2\2\2`\u0251\3\2\2\2b\u0255")
        buf.write("\3\2\2\2d\u0258\3\2\2\2f\u025c\3\2\2\2h\u025f\3\2\2\2")
        buf.write("j\u0263\3\2\2\2l\u0266\3\2\2\2n\u026d\3\2\2\2p\u0273\3")
        buf.write("\2\2\2r\u0284\3\2\2\2t\u0291\3\2\2\2v\u0295\3\2\2\2x\u029e")
        buf.write("\3\2\2\2z\u02ab\3\2\2\2|\u02b4\3\2\2\2~\u02bf\3\2\2\2")
        buf.write("\u0080\u02cc\3\2\2\2\u0082\u02d3\3\2\2\2\u0084\u02d9\3")
        buf.write("\2\2\2\u0086\u02e5\3\2\2\2\u0088\u02f2\3\2\2\2\u008a\u02f6")
        buf.write("\3\2\2\2\u008c\u02f9\3\2\2\2\u008e\u0300\3\2\2\2\u0090")
        buf.write("\u0303\3\2\2\2\u0092\u0306\3\2\2\2\u0094\u030a\3\2\2\2")
        buf.write("\u0096\u0322\3\2\2\2\u0098\u032f\3\2\2\2\u009a\u0336\3")
        buf.write("\2\2\2\u009c\u0339\3\2\2\2\u009e\u0351\3\2\2\2\u00a0\u00a2")
        buf.write("\5\20\t\2\u00a1\u00a0\3\2\2\2\u00a2\u00a5\3\2\2\2\u00a3")
        buf.write("\u00a1\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a8\3\2\2\2")
        buf.write("\u00a5\u00a3\3\2\2\2\u00a6\u00a8\5\4\3\2\u00a7\u00a3\3")
        buf.write("\2\2\2\u00a7\u00a6\3\2\2\2\u00a8\u00aa\3\2\2\2\u00a9\u00ab")
        buf.write("\5\16\b\2\u00aa\u00a9\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab")
        buf.write("\u00af\3\2\2\2\u00ac\u00ae\7\32\2\2\u00ad\u00ac\3\2\2")
        buf.write("\2\u00ae\u00b1\3\2\2\2\u00af\u00ad\3\2\2\2\u00af\u00b0")
        buf.write("\3\2\2\2\u00b0\u00b2\3\2\2\2\u00b1\u00af\3\2\2\2\u00b2")
        buf.write("\u00b3\7\2\2\3\u00b3\3\3\2\2\2\u00b4\u00b5\5\66\34\2\u00b5")
        buf.write("\u00b6\5\24\13\2\u00b6\u00b7\5\34\17\2\u00b7\u00b8\5<")
        buf.write("\37\2\u00b8\u00d8\3\2\2\2\u00b9\u00ba\5> \2\u00ba\u00bb")
        buf.write("\5\24\13\2\u00bb\u00bc\5\34\17\2\u00bc\u00bd\5D#\2\u00bd")
        buf.write("\u00d8\3\2\2\2\u00be\u00bf\5F$\2\u00bf\u00c0\5\24\13\2")
        buf.write("\u00c0\u00c1\5\34\17\2\u00c1\u00c2\5L\'\2\u00c2\u00d8")
        buf.write("\3\2\2\2\u00c3\u00c4\5\u0092J\2\u00c4\u00c5\5\24\13\2")
        buf.write("\u00c5\u00c6\5\34\17\2\u00c6\u00c7\5\u0096L\2\u00c7\u00d8")
        buf.write("\3\2\2\2\u00c8\u00c9\5N(\2\u00c9\u00ca\5\24\13\2\u00ca")
        buf.write("\u00cb\5\34\17\2\u00cb\u00cc\5R*\2\u00cc\u00d8\3\2\2\2")
        buf.write("\u00cd\u00ce\5l\67\2\u00ce\u00cf\5\24\13\2\u00cf\u00d0")
        buf.write("\5\34\17\2\u00d0\u00d1\5r:\2\u00d1\u00d8\3\2\2\2\u00d2")
        buf.write("\u00d3\5\u0098M\2\u00d3\u00d4\5\24\13\2\u00d4\u00d5\5")
        buf.write("\34\17\2\u00d5\u00d6\5\u009eP\2\u00d6\u00d8\3\2\2\2\u00d7")
        buf.write("\u00b4\3\2\2\2\u00d7\u00b9\3\2\2\2\u00d7\u00be\3\2\2\2")
        buf.write("\u00d7\u00c3\3\2\2\2\u00d7\u00c8\3\2\2\2\u00d7\u00cd\3")
        buf.write("\2\2\2\u00d7\u00d2\3\2\2\2\u00d8\5\3\2\2\2\u00d9\u00e2")
        buf.write("\7\3\2\2\u00da\u00db\5\b\5\2\u00db\u00dc\7\4\2\2\u00dc")
        buf.write("\u00e1\3\2\2\2\u00dd\u00de\5\b\5\2\u00de\u00df\7\5\2\2")
        buf.write("\u00df\u00e1\3\2\2\2\u00e0\u00da\3\2\2\2\u00e0\u00dd\3")
        buf.write("\2\2\2\u00e1\u00e4\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e2\u00e3")
        buf.write("\3\2\2\2\u00e3\u00e5\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e5")
        buf.write("\u00e6\5\b\5\2\u00e6\u00e7\7\3\2\2\u00e7\7\3\2\2\2\u00e8")
        buf.write("\u00ea\7\31\2\2\u00e9\u00e8\3\2\2\2\u00ea\u00eb\3\2\2")
        buf.write("\2\u00eb\u00e9\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec\u011b")
        buf.write("\3\2\2\2\u00ed\u00ef\7\6\2\2\u00ee\u00f0\7\31\2\2\u00ef")
        buf.write("\u00ee\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1\u00ef\3\2\2\2")
        buf.write("\u00f1\u00f2\3\2\2\2\u00f2\u011b\3\2\2\2\u00f3\u00f5\7")
        buf.write("\7\2\2\u00f4\u00f6\7\31\2\2\u00f5\u00f4\3\2\2\2\u00f6")
        buf.write("\u00f7\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f7\u00f8\3\2\2\2")
        buf.write("\u00f8\u011b\3\2\2\2\u00f9\u00fb\7\b\2\2\u00fa\u00fc\7")
        buf.write("\31\2\2\u00fb\u00fa\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd")
        buf.write("\u00fb\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe\u011b\3\2\2\2")
        buf.write("\u00ff\u0101\7\31\2\2\u0100\u00ff\3\2\2\2\u0101\u0102")
        buf.write("\3\2\2\2\u0102\u0100\3\2\2\2\u0102\u0103\3\2\2\2\u0103")
        buf.write("\u0104\3\2\2\2\u0104\u011b\7\7\2\2\u0105\u0107\7\6\2\2")
        buf.write("\u0106\u0108\7\31\2\2\u0107\u0106\3\2\2\2\u0108\u0109")
        buf.write("\3\2\2\2\u0109\u0107\3\2\2\2\u0109\u010a\3\2\2\2\u010a")
        buf.write("\u010b\3\2\2\2\u010b\u011b\7\7\2\2\u010c\u010e\7\7\2\2")
        buf.write("\u010d\u010f\7\31\2\2\u010e\u010d\3\2\2\2\u010f\u0110")
        buf.write("\3\2\2\2\u0110\u010e\3\2\2\2\u0110\u0111\3\2\2\2\u0111")
        buf.write("\u0112\3\2\2\2\u0112\u011b\7\7\2\2\u0113\u0115\7\b\2\2")
        buf.write("\u0114\u0116\7\31\2\2\u0115\u0114\3\2\2\2\u0116\u0117")
        buf.write("\3\2\2\2\u0117\u0115\3\2\2\2\u0117\u0118\3\2\2\2\u0118")
        buf.write("\u0119\3\2\2\2\u0119\u011b\7\7\2\2\u011a\u00e9\3\2\2\2")
        buf.write("\u011a\u00ed\3\2\2\2\u011a\u00f3\3\2\2\2\u011a\u00f9\3")
        buf.write("\2\2\2\u011a\u0100\3\2\2\2\u011a\u0105\3\2\2\2\u011a\u010c")
        buf.write("\3\2\2\2\u011a\u0113\3\2\2\2\u011b\t\3\2\2\2\u011c\u0120")
        buf.write("\7\3\2\2\u011d\u0121\7\31\2\2\u011e\u0121\5\f\7\2\u011f")
        buf.write("\u0121\7\30\2\2\u0120\u011d\3\2\2\2\u0120\u011e\3\2\2")
        buf.write("\2\u0120\u011f\3\2\2\2\u0121\u0122\3\2\2\2\u0122\u0120")
        buf.write("\3\2\2\2\u0122\u0123\3\2\2\2\u0123\u0124\3\2\2\2\u0124")
        buf.write("\u0125\7\3\2\2\u0125\13\3\2\2\2\u0126\u0127\t\2\2\2\u0127")
        buf.write("\r\3\2\2\2\u0128\u0129\7\t\2\2\u0129\17\3\2\2\2\u012a")
        buf.write("\u012b\7\32\2\2\u012b\21\3\2\2\2\u012c\u0130\7\3\2\2\u012d")
        buf.write("\u0131\7\31\2\2\u012e\u0131\5\f\7\2\u012f\u0131\7\30\2")
        buf.write("\2\u0130\u012d\3\2\2\2\u0130\u012e\3\2\2\2\u0130\u012f")
        buf.write("\3\2\2\2\u0131\u0132\3\2\2\2\u0132\u0130\3\2\2\2\u0132")
        buf.write("\u0133\3\2\2\2\u0133\u0134\3\2\2\2\u0134\u0135\7\3\2\2")
        buf.write("\u0135\23\3\2\2\2\u0136\u0137\7\22\2\2\u0137\25\3\2\2")
        buf.write("\2\u0138\u0139\7\23\2\2\u0139\27\3\2\2\2\u013a\u013b\7")
        buf.write("\24\2\2\u013b\31\3\2\2\2\u013c\u013d\7\25\2\2\u013d\33")
        buf.write("\3\2\2\2\u013e\u013f\7\26\2\2\u013f\35\3\2\2\2\u0140\u0141")
        buf.write("\7\27\2\2\u0141\37\3\2\2\2\u0142\u0145\5\30\r\2\u0143")
        buf.write("\u0145\5\32\16\2\u0144\u0142\3\2\2\2\u0144\u0143\3\2\2")
        buf.write("\2\u0145!\3\2\2\2\u0146\u0148\7\35\2\2\u0147\u0149\5$")
        buf.write("\23\2\u0148\u0147\3\2\2\2\u0148\u0149\3\2\2\2\u0149#\3")
        buf.write("\2\2\2\u014a\u014b\5\6\4\2\u014b\u014c\7\30\2\2\u014c")
        buf.write("%\3\2\2\2\u014d\u014f\7\36\2\2\u014e\u0150\5(\25\2\u014f")
        buf.write("\u014e\3\2\2\2\u014f\u0150\3\2\2\2\u0150\'\3\2\2\2\u0151")
        buf.write("\u0152\5\n\6\2\u0152\u0154\7\30\2\2\u0153\u0155\5*\26")
        buf.write("\2\u0154\u0153\3\2\2\2\u0154\u0155\3\2\2\2\u0155\u0158")
        buf.write("\3\2\2\2\u0156\u0158\5*\26\2\u0157\u0151\3\2\2\2\u0157")
        buf.write("\u0156\3\2\2\2\u0158)\3\2\2\2\u0159\u015a\5\36\20\2\u015a")
        buf.write("\u015b\5,\27\2\u015b+\3\2\2\2\u015c\u015d\b\27\1\2\u015d")
        buf.write("\u015e\7\33\2\2\u015e\u015f\5,\27\2\u015f\u0160\7\34\2")
        buf.write("\2\u0160\u0163\3\2\2\2\u0161\u0163\5N(\2\u0162\u015c\3")
        buf.write("\2\2\2\u0162\u0161\3\2\2\2\u0163\u016c\3\2\2\2\u0164\u0165")
        buf.write("\f\5\2\2\u0165\u0166\5 \21\2\u0166\u0167\5,\27\6\u0167")
        buf.write("\u016b\3\2\2\2\u0168\u0169\f\3\2\2\u0169\u016b\7\30\2")
        buf.write("\2\u016a\u0164\3\2\2\2\u016a\u0168\3\2\2\2\u016b\u016e")
        buf.write("\3\2\2\2\u016c\u016a\3\2\2\2\u016c\u016d\3\2\2\2\u016d")
        buf.write("-\3\2\2\2\u016e\u016c\3\2\2\2\u016f\u0170\7\37\2\2\u0170")
        buf.write("\u0171\5\60\31\2\u0171/\3\2\2\2\u0172\u0177\5\26\f\2\u0173")
        buf.write("\u0174\5\n\6\2\u0174\u0175\7\30\2\2\u0175\u0178\3\2\2")
        buf.write("\2\u0176\u0178\7 \2\2\u0177\u0173\3\2\2\2\u0177\u0176")
        buf.write("\3\2\2\2\u0178\61\3\2\2\2\u0179\u017a\7!\2\2\u017a\u017b")
        buf.write("\5\64\33\2\u017b\63\3\2\2\2\u017c\u0181\5\26\f\2\u017d")
        buf.write("\u017e\5\n\6\2\u017e\u017f\7\30\2\2\u017f\u0182\3\2\2")
        buf.write("\2\u0180\u0182\7\"\2\2\u0181\u017d\3\2\2\2\u0181\u0180")
        buf.write("\3\2\2\2\u0182\65\3\2\2\2\u0183\u0185\7#\2\2\u0184\u0186")
        buf.write("\5:\36\2\u0185\u0184\3\2\2\2\u0185\u0186\3\2\2\2\u0186")
        buf.write("\u0188\3\2\2\2\u0187\u0189\58\35\2\u0188\u0187\3\2\2\2")
        buf.write("\u0188\u0189\3\2\2\2\u0189\67\3\2\2\2\u018a\u018b\5\26")
        buf.write("\f\2\u018b\u018c\5\u0092J\2\u018c9\3\2\2\2\u018d\u018e")
        buf.write("\5\36\20\2\u018e\u018f\5<\37\2\u018f;\3\2\2\2\u0190\u0191")
        buf.write("\b\37\1\2\u0191\u0192\7\33\2\2\u0192\u0193\5<\37\2\u0193")
        buf.write("\u0194\7\34\2\2\u0194\u01a1\3\2\2\2\u0195\u019f\5&\24")
        buf.write("\2\u0196\u019f\5`\61\2\u0197\u019f\5d\63\2\u0198\u019f")
        buf.write("\5\\/\2\u0199\u019f\5\"\22\2\u019a\u019f\5T+\2\u019b\u019f")
        buf.write("\5h\65\2\u019c\u019f\5\u0080A\2\u019d\u019f\5\22\n\2\u019e")
        buf.write("\u0195\3\2\2\2\u019e\u0196\3\2\2\2\u019e\u0197\3\2\2\2")
        buf.write("\u019e\u0198\3\2\2\2\u019e\u0199\3\2\2\2\u019e\u019a\3")
        buf.write("\2\2\2\u019e\u019b\3\2\2\2\u019e\u019c\3\2\2\2\u019e\u019d")
        buf.write("\3\2\2\2\u019f\u01a1\3\2\2\2\u01a0\u0190\3\2\2\2\u01a0")
        buf.write("\u019e\3\2\2\2\u01a1\u01aa\3\2\2\2\u01a2\u01a3\f\5\2\2")
        buf.write("\u01a3\u01a4\5 \21\2\u01a4\u01a5\5<\37\6\u01a5\u01a9\3")
        buf.write("\2\2\2\u01a6\u01a7\f\3\2\2\u01a7\u01a9\7\30\2\2\u01a8")
        buf.write("\u01a2\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a9\u01ac\3\2\2\2")
        buf.write("\u01aa\u01a8\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab=\3\2\2")
        buf.write("\2\u01ac\u01aa\3\2\2\2\u01ad\u01af\7$\2\2\u01ae\u01b0")
        buf.write("\5B\"\2\u01af\u01ae\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0")
        buf.write("\u01b2\3\2\2\2\u01b1\u01b3\5@!\2\u01b2\u01b1\3\2\2\2\u01b2")
        buf.write("\u01b3\3\2\2\2\u01b3?\3\2\2\2\u01b4\u01b5\5\26\f\2\u01b5")
        buf.write("\u01b6\5\u0092J\2\u01b6A\3\2\2\2\u01b7\u01b8\5\36\20\2")
        buf.write("\u01b8\u01b9\5D#\2\u01b9C\3\2\2\2\u01ba\u01bb\b#\1\2\u01bb")
        buf.write("\u01bc\7\33\2\2\u01bc\u01bd\5D#\2\u01bd\u01be\7\34\2\2")
        buf.write("\u01be\u01c8\3\2\2\2\u01bf\u01c6\5&\24\2\u01c0\u01c6\5")
        buf.write("`\61\2\u01c1\u01c6\5d\63\2\u01c2\u01c6\5\\/\2\u01c3\u01c6")
        buf.write("\5\"\22\2\u01c4\u01c6\5N(\2\u01c5\u01bf\3\2\2\2\u01c5")
        buf.write("\u01c0\3\2\2\2\u01c5\u01c1\3\2\2\2\u01c5\u01c2\3\2\2\2")
        buf.write("\u01c5\u01c3\3\2\2\2\u01c5\u01c4\3\2\2\2\u01c6\u01c8\3")
        buf.write("\2\2\2\u01c7\u01ba\3\2\2\2\u01c7\u01c5\3\2\2\2\u01c8\u01d1")
        buf.write("\3\2\2\2\u01c9\u01ca\f\5\2\2\u01ca\u01cb\5 \21\2\u01cb")
        buf.write("\u01cc\5D#\6\u01cc\u01d0\3\2\2\2\u01cd\u01ce\f\3\2\2\u01ce")
        buf.write("\u01d0\7\30\2\2\u01cf\u01c9\3\2\2\2\u01cf\u01cd\3\2\2")
        buf.write("\2\u01d0\u01d3\3\2\2\2\u01d1\u01cf\3\2\2\2\u01d1\u01d2")
        buf.write("\3\2\2\2\u01d2E\3\2\2\2\u01d3\u01d1\3\2\2\2\u01d4\u01d6")
        buf.write("\7%\2\2\u01d5\u01d7\5J&\2\u01d6\u01d5\3\2\2\2\u01d6\u01d7")
        buf.write("\3\2\2\2\u01d7\u01d9\3\2\2\2\u01d8\u01da\5H%\2\u01d9\u01d8")
        buf.write("\3\2\2\2\u01d9\u01da\3\2\2\2\u01daG\3\2\2\2\u01db\u01dc")
        buf.write("\5\26\f\2\u01dc\u01dd\5\u0092J\2\u01ddI\3\2\2\2\u01de")
        buf.write("\u01df\5\36\20\2\u01df\u01e0\5L\'\2\u01e0K\3\2\2\2\u01e1")
        buf.write("\u01e2\b\'\1\2\u01e2\u01e3\7\33\2\2\u01e3\u01e4\5L\'\2")
        buf.write("\u01e4\u01e5\7\34\2\2\u01e5\u01f1\3\2\2\2\u01e6\u01ef")
        buf.write("\5&\24\2\u01e7\u01ef\5`\61\2\u01e8\u01ef\5d\63\2\u01e9")
        buf.write("\u01ef\5N(\2\u01ea\u01ef\5h\65\2\u01eb\u01ef\5l\67\2\u01ec")
        buf.write("\u01ef\5\u0080A\2\u01ed\u01ef\5\22\n\2\u01ee\u01e6\3\2")
        buf.write("\2\2\u01ee\u01e7\3\2\2\2\u01ee\u01e8\3\2\2\2\u01ee\u01e9")
        buf.write("\3\2\2\2\u01ee\u01ea\3\2\2\2\u01ee\u01eb\3\2\2\2\u01ee")
        buf.write("\u01ec\3\2\2\2\u01ee\u01ed\3\2\2\2\u01ef\u01f1\3\2\2\2")
        buf.write("\u01f0\u01e1\3\2\2\2\u01f0\u01ee\3\2\2\2\u01f1\u01fa\3")
        buf.write("\2\2\2\u01f2\u01f3\f\5\2\2\u01f3\u01f4\5 \21\2\u01f4\u01f5")
        buf.write("\5L\'\6\u01f5\u01f9\3\2\2\2\u01f6\u01f7\f\3\2\2\u01f7")
        buf.write("\u01f9\7\30\2\2\u01f8\u01f2\3\2\2\2\u01f8\u01f6\3\2\2")
        buf.write("\2\u01f9\u01fc\3\2\2\2\u01fa\u01f8\3\2\2\2\u01fa\u01fb")
        buf.write("\3\2\2\2\u01fbM\3\2\2\2\u01fc\u01fa\3\2\2\2\u01fd\u01ff")
        buf.write("\7&\2\2\u01fe\u0200\5P)\2\u01ff\u01fe\3\2\2\2\u01ff\u0200")
        buf.write("\3\2\2\2\u0200O\3\2\2\2\u0201\u0202\5\36\20\2\u0202\u0203")
        buf.write("\5R*\2\u0203\u0208\3\2\2\2\u0204\u0205\5\n\6\2\u0205\u0206")
        buf.write("\7\30\2\2\u0206\u0208\3\2\2\2\u0207\u0201\3\2\2\2\u0207")
        buf.write("\u0204\3\2\2\2\u0208Q\3\2\2\2\u0209\u020a\b*\1\2\u020a")
        buf.write("\u020b\7\33\2\2\u020b\u020c\5R*\2\u020c\u020d\7\34\2\2")
        buf.write("\u020d\u0213\3\2\2\2\u020e\u0211\5\\/\2\u020f\u0211\5")
        buf.write("\"\22\2\u0210\u020e\3\2\2\2\u0210\u020f\3\2\2\2\u0211")
        buf.write("\u0213\3\2\2\2\u0212\u0209\3\2\2\2\u0212\u0210\3\2\2\2")
        buf.write("\u0213\u021c\3\2\2\2\u0214\u0215\f\5\2\2\u0215\u0216\5")
        buf.write(" \21\2\u0216\u0217\5R*\6\u0217\u021b\3\2\2\2\u0218\u0219")
        buf.write("\f\3\2\2\u0219\u021b\7\30\2\2\u021a\u0214\3\2\2\2\u021a")
        buf.write("\u0218\3\2\2\2\u021b\u021e\3\2\2\2\u021c\u021a\3\2\2\2")
        buf.write("\u021c\u021d\3\2\2\2\u021dS\3\2\2\2\u021e\u021c\3\2\2")
        buf.write("\2\u021f\u0221\7&\2\2\u0220\u0222\5V,\2\u0221\u0220\3")
        buf.write("\2\2\2\u0221\u0222\3\2\2\2\u0222U\3\2\2\2\u0223\u0224")
        buf.write("\5\n\6\2\u0224\u0226\7\30\2\2\u0225\u0227\5X-\2\u0226")
        buf.write("\u0225\3\2\2\2\u0226\u0227\3\2\2\2\u0227\u022a\3\2\2\2")
        buf.write("\u0228\u022a\5X-\2\u0229\u0223\3\2\2\2\u0229\u0228\3\2")
        buf.write("\2\2\u022aW\3\2\2\2\u022b\u022c\5\36\20\2\u022c\u022d")
        buf.write("\5Z.\2\u022dY\3\2\2\2\u022e\u022f\b.\1\2\u022f\u0230\7")
        buf.write("\33\2\2\u0230\u0231\5Z.\2\u0231\u0232\7\34\2\2\u0232\u0239")
        buf.write("\3\2\2\2\u0233\u0237\5\\/\2\u0234\u0237\5\"\22\2\u0235")
        buf.write("\u0237\5&\24\2\u0236\u0233\3\2\2\2\u0236\u0234\3\2\2\2")
        buf.write("\u0236\u0235\3\2\2\2\u0237\u0239\3\2\2\2\u0238\u022e\3")
        buf.write("\2\2\2\u0238\u0236\3\2\2\2\u0239\u0242\3\2\2\2\u023a\u023b")
        buf.write("\f\5\2\2\u023b\u023c\5 \21\2\u023c\u023d\5Z.\6\u023d\u0241")
        buf.write("\3\2\2\2\u023e\u023f\f\3\2\2\u023f\u0241\7\30\2\2\u0240")
        buf.write("\u023a\3\2\2\2\u0240\u023e\3\2\2\2\u0241\u0244\3\2\2\2")
        buf.write("\u0242\u0240\3\2\2\2\u0242\u0243\3\2\2\2\u0243[\3\2\2")
        buf.write("\2\u0244\u0242\3\2\2\2\u0245\u0247\7\'\2\2\u0246\u0248")
        buf.write("\5^\60\2\u0247\u0246\3\2\2\2\u0247\u0248\3\2\2\2\u0248")
        buf.write("]\3\2\2\2\u0249\u024a\5\n\6\2\u024a\u024b\7\30\2\2\u024b")
        buf.write("\u0250\3\2\2\2\u024c\u024d\5\6\4\2\u024d\u024e\7\30\2")
        buf.write("\2\u024e\u0250\3\2\2\2\u024f\u0249\3\2\2\2\u024f\u024c")
        buf.write("\3\2\2\2\u0250_\3\2\2\2\u0251\u0253\7(\2\2\u0252\u0254")
        buf.write("\5b\62\2\u0253\u0252\3\2\2\2\u0253\u0254\3\2\2\2\u0254")
        buf.write("a\3\2\2\2\u0255\u0256\5\6\4\2\u0256\u0257\7\30\2\2\u0257")
        buf.write("c\3\2\2\2\u0258\u025a\7)\2\2\u0259\u025b\5f\64\2\u025a")
        buf.write("\u0259\3\2\2\2\u025a\u025b\3\2\2\2\u025be\3\2\2\2\u025c")
        buf.write("\u025d\5\6\4\2\u025d\u025e\7\30\2\2\u025eg\3\2\2\2\u025f")
        buf.write("\u0261\7*\2\2\u0260\u0262\5j\66\2\u0261\u0260\3\2\2\2")
        buf.write("\u0261\u0262\3\2\2\2\u0262i\3\2\2\2\u0263\u0264\5\n\6")
        buf.write("\2\u0264\u0265\7\30\2\2\u0265k\3\2\2\2\u0266\u0268\7+")
        buf.write("\2\2\u0267\u0269\5p9\2\u0268\u0267\3\2\2\2\u0268\u0269")
        buf.write("\3\2\2\2\u0269\u026b\3\2\2\2\u026a\u026c\5n8\2\u026b\u026a")
        buf.write("\3\2\2\2\u026b\u026c\3\2\2\2\u026cm\3\2\2\2\u026d\u0271")
        buf.write("\5\26\f\2\u026e\u0272\5\u0092J\2\u026f\u0272\5\66\34\2")
        buf.write("\u0270\u0272\5F$\2\u0271\u026e\3\2\2\2\u0271\u026f\3\2")
        buf.write("\2\2\u0271\u0270\3\2\2\2\u0272o\3\2\2\2\u0273\u0274\5")
        buf.write("\36\20\2\u0274\u0275\5r:\2\u0275q\3\2\2\2\u0276\u0277")
        buf.write("\b:\1\2\u0277\u0278\7\33\2\2\u0278\u0279\5r:\2\u0279\u027a")
        buf.write("\7\34\2\2\u027a\u0285\3\2\2\2\u027b\u0283\5&\24\2\u027c")
        buf.write("\u0283\5`\61\2\u027d\u0283\5d\63\2\u027e\u0283\5\\/\2")
        buf.write("\u027f\u0283\5\"\22\2\u0280\u0283\5\u008cG\2\u0281\u0283")
        buf.write("\5\22\n\2\u0282\u027b\3\2\2\2\u0282\u027c\3\2\2\2\u0282")
        buf.write("\u027d\3\2\2\2\u0282\u027e\3\2\2\2\u0282\u027f\3\2\2\2")
        buf.write("\u0282\u0280\3\2\2\2\u0282\u0281\3\2\2\2\u0283\u0285\3")
        buf.write("\2\2\2\u0284\u0276\3\2\2\2\u0284\u0282\3\2\2\2\u0285\u028e")
        buf.write("\3\2\2\2\u0286\u0287\f\5\2\2\u0287\u0288\5 \21\2\u0288")
        buf.write("\u0289\5r:\6\u0289\u028d\3\2\2\2\u028a\u028b\f\3\2\2\u028b")
        buf.write("\u028d\7\30\2\2\u028c\u0286\3\2\2\2\u028c\u028a\3\2\2")
        buf.write("\2\u028d\u0290\3\2\2\2\u028e\u028c\3\2\2\2\u028e\u028f")
        buf.write("\3\2\2\2\u028fs\3\2\2\2\u0290\u028e\3\2\2\2\u0291\u0293")
        buf.write("\7,\2\2\u0292\u0294\5v<\2\u0293\u0292\3\2\2\2\u0293\u0294")
        buf.write("\3\2\2\2\u0294u\3\2\2\2\u0295\u0296\5\36\20\2\u0296\u0297")
        buf.write("\5x=\2\u0297w\3\2\2\2\u0298\u0299\b=\1\2\u0299\u029a\7")
        buf.write("\33\2\2\u029a\u029b\5x=\2\u029b\u029c\7\34\2\2\u029c\u029f")
        buf.write("\3\2\2\2\u029d\u029f\5z>\2\u029e\u0298\3\2\2\2\u029e\u029d")
        buf.write("\3\2\2\2\u029f\u02a8\3\2\2\2\u02a0\u02a1\f\5\2\2\u02a1")
        buf.write("\u02a2\5 \21\2\u02a2\u02a3\5x=\6\u02a3\u02a7\3\2\2\2\u02a4")
        buf.write("\u02a5\f\3\2\2\u02a5\u02a7\7\30\2\2\u02a6\u02a0\3\2\2")
        buf.write("\2\u02a6\u02a4\3\2\2\2\u02a7\u02aa\3\2\2\2\u02a8\u02a6")
        buf.write("\3\2\2\2\u02a8\u02a9\3\2\2\2\u02a9y\3\2\2\2\u02aa\u02a8")
        buf.write("\3\2\2\2\u02ab\u02ac\7-\2\2\u02ac\u02ad\5|?\2\u02ad{\3")
        buf.write("\2\2\2\u02ae\u02af\5\36\20\2\u02af\u02b0\5~@\2\u02b0\u02b5")
        buf.write("\3\2\2\2\u02b1\u02b2\5\n\6\2\u02b2\u02b3\7\30\2\2\u02b3")
        buf.write("\u02b5\3\2\2\2\u02b4\u02ae\3\2\2\2\u02b4\u02b1\3\2\2\2")
        buf.write("\u02b5}\3\2\2\2\u02b6\u02b7\b@\1\2\u02b7\u02b8\7\33\2")
        buf.write("\2\u02b8\u02b9\5~@\2\u02b9\u02ba\7\34\2\2\u02ba\u02c0")
        buf.write("\3\2\2\2\u02bb\u02be\5\\/\2\u02bc\u02be\5\"\22\2\u02bd")
        buf.write("\u02bb\3\2\2\2\u02bd\u02bc\3\2\2\2\u02be\u02c0\3\2\2\2")
        buf.write("\u02bf\u02b6\3\2\2\2\u02bf\u02bd\3\2\2\2\u02c0\u02c9\3")
        buf.write("\2\2\2\u02c1\u02c2\f\5\2\2\u02c2\u02c3\5 \21\2\u02c3\u02c4")
        buf.write("\5~@\6\u02c4\u02c8\3\2\2\2\u02c5\u02c6\f\3\2\2\u02c6\u02c8")
        buf.write("\7\30\2\2\u02c7\u02c1\3\2\2\2\u02c7\u02c5\3\2\2\2\u02c8")
        buf.write("\u02cb\3\2\2\2\u02c9\u02c7\3\2\2\2\u02c9\u02ca\3\2\2\2")
        buf.write("\u02ca\177\3\2\2\2\u02cb\u02c9\3\2\2\2\u02cc\u02ce\7.")
        buf.write("\2\2\u02cd\u02cf\5\u0084C\2\u02ce\u02cd\3\2\2\2\u02ce")
        buf.write("\u02cf\3\2\2\2\u02cf\u02d1\3\2\2\2\u02d0\u02d2\5\u0082")
        buf.write("B\2\u02d1\u02d0\3\2\2\2\u02d1\u02d2\3\2\2\2\u02d2\u0081")
        buf.write("\3\2\2\2\u02d3\u02d7\5\26\f\2\u02d4\u02d8\5\66\34\2\u02d5")
        buf.write("\u02d8\5F$\2\u02d6\u02d8\5F$\2\u02d7\u02d4\3\2\2\2\u02d7")
        buf.write("\u02d5\3\2\2\2\u02d7\u02d6\3\2\2\2\u02d8\u0083\3\2\2\2")
        buf.write("\u02d9\u02da\5\36\20\2\u02da\u02db\5\u0086D\2\u02db\u0085")
        buf.write("\3\2\2\2\u02dc\u02dd\bD\1\2\u02dd\u02de\7\33\2\2\u02de")
        buf.write("\u02df\5\u0086D\2\u02df\u02e0\7\34\2\2\u02e0\u02e6\3\2")
        buf.write("\2\2\u02e1\u02e4\5\22\n\2\u02e2\u02e4\5\u0088E\2\u02e3")
        buf.write("\u02e1\3\2\2\2\u02e3\u02e2\3\2\2\2\u02e4\u02e6\3\2\2\2")
        buf.write("\u02e5\u02dc\3\2\2\2\u02e5\u02e3\3\2\2\2\u02e6\u02ef\3")
        buf.write("\2\2\2\u02e7\u02e8\f\5\2\2\u02e8\u02e9\5 \21\2\u02e9\u02ea")
        buf.write("\5\u0086D\6\u02ea\u02ee\3\2\2\2\u02eb\u02ec\f\3\2\2\u02ec")
        buf.write("\u02ee\7\30\2\2\u02ed\u02e7\3\2\2\2\u02ed\u02eb\3\2\2")
        buf.write("\2\u02ee\u02f1\3\2\2\2\u02ef\u02ed\3\2\2\2\u02ef\u02f0")
        buf.write("\3\2\2\2\u02f0\u0087\3\2\2\2\u02f1\u02ef\3\2\2\2\u02f2")
        buf.write("\u02f4\7/\2\2\u02f3\u02f5\5\u008aF\2\u02f4\u02f3\3\2\2")
        buf.write("\2\u02f4\u02f5\3\2\2\2\u02f5\u0089\3\2\2\2\u02f6\u02f7")
        buf.write("\5\n\6\2\u02f7\u02f8\7\30\2\2\u02f8\u008b\3\2\2\2\u02f9")
        buf.write("\u02fb\7\60\2\2\u02fa\u02fc\5\u0090I\2\u02fb\u02fa\3\2")
        buf.write("\2\2\u02fb\u02fc\3\2\2\2\u02fc\u02fe\3\2\2\2\u02fd\u02ff")
        buf.write("\5\u008eH\2\u02fe\u02fd\3\2\2\2\u02fe\u02ff\3\2\2\2\u02ff")
        buf.write("\u008d\3\2\2\2\u0300\u0301\5\26\f\2\u0301\u0302\5l\67")
        buf.write("\2\u0302\u008f\3\2\2\2\u0303\u0304\5\n\6\2\u0304\u0305")
        buf.write("\7\30\2\2\u0305\u0091\3\2\2\2\u0306\u0308\7\61\2\2\u0307")
        buf.write("\u0309\5\u0094K\2\u0308\u0307\3\2\2\2\u0308\u0309\3\2")
        buf.write("\2\2\u0309\u0093\3\2\2\2\u030a\u030b\5\36\20\2\u030b\u030c")
        buf.write("\5\u0096L\2\u030c\u0095\3\2\2\2\u030d\u030e\bL\1\2\u030e")
        buf.write("\u030f\7\33\2\2\u030f\u0310\5\u0096L\2\u0310\u0311\7\34")
        buf.write("\2\2\u0311\u0323\3\2\2\2\u0312\u0321\5&\24\2\u0313\u0321")
        buf.write("\5`\61\2\u0314\u0321\5d\63\2\u0315\u0321\5\"\22\2\u0316")
        buf.write("\u0321\5.\30\2\u0317\u0321\5\62\32\2\u0318\u0321\5\66")
        buf.write("\34\2\u0319\u0321\5> \2\u031a\u0321\5F$\2\u031b\u0321")
        buf.write("\5l\67\2\u031c\u0321\5h\65\2\u031d\u0321\5\22\n\2\u031e")
        buf.write("\u0321\5\u0098M\2\u031f\u0321\5t;\2\u0320\u0312\3\2\2")
        buf.write("\2\u0320\u0313\3\2\2\2\u0320\u0314\3\2\2\2\u0320\u0315")
        buf.write("\3\2\2\2\u0320\u0316\3\2\2\2\u0320\u0317\3\2\2\2\u0320")
        buf.write("\u0318\3\2\2\2\u0320\u0319\3\2\2\2\u0320\u031a\3\2\2\2")
        buf.write("\u0320\u031b\3\2\2\2\u0320\u031c\3\2\2\2\u0320\u031d\3")
        buf.write("\2\2\2\u0320\u031e\3\2\2\2\u0320\u031f\3\2\2\2\u0321\u0323")
        buf.write("\3\2\2\2\u0322\u030d\3\2\2\2\u0322\u0320\3\2\2\2\u0323")
        buf.write("\u032c\3\2\2\2\u0324\u0325\f\5\2\2\u0325\u0326\5 \21\2")
        buf.write("\u0326\u0327\5\u0096L\6\u0327\u032b\3\2\2\2\u0328\u0329")
        buf.write("\f\3\2\2\u0329\u032b\7\30\2\2\u032a\u0324\3\2\2\2\u032a")
        buf.write("\u0328\3\2\2\2\u032b\u032e\3\2\2\2\u032c\u032a\3\2\2\2")
        buf.write("\u032c\u032d\3\2\2\2\u032d\u0097\3\2\2\2\u032e\u032c\3")
        buf.write("\2\2\2\u032f\u0331\7\62\2\2\u0330\u0332\5\u009cO\2\u0331")
        buf.write("\u0330\3\2\2\2\u0331\u0332\3\2\2\2\u0332\u0334\3\2\2\2")
        buf.write("\u0333\u0335\5\u009aN\2\u0334\u0333\3\2\2\2\u0334\u0335")
        buf.write("\3\2\2\2\u0335\u0099\3\2\2\2\u0336\u0337\5\26\f\2\u0337")
        buf.write("\u0338\5\u0092J\2\u0338\u009b\3\2\2\2\u0339\u033a\5\36")
        buf.write("\20\2\u033a\u033b\5\u009eP\2\u033b\u009d\3\2\2\2\u033c")
        buf.write("\u033d\bP\1\2\u033d\u033e\7\33\2\2\u033e\u033f\5\u009e")
        buf.write("P\2\u033f\u0340\7\34\2\2\u0340\u0352\3\2\2\2\u0341\u0350")
        buf.write("\5&\24\2\u0342\u0350\5`\61\2\u0343\u0350\5d\63\2\u0344")
        buf.write("\u0350\5\"\22\2\u0345\u0350\5.\30\2\u0346\u0350\5\62\32")
        buf.write("\2\u0347\u0350\5\66\34\2\u0348\u0350\5\u0098M\2\u0349")
        buf.write("\u0350\3\2\2\2\u034a\u0350\5> \2\u034b\u0350\5F$\2\u034c")
        buf.write("\u0350\5l\67\2\u034d\u0350\5h\65\2\u034e\u0350\5\22\n")
        buf.write("\2\u034f\u0341\3\2\2\2\u034f\u0342\3\2\2\2\u034f\u0343")
        buf.write("\3\2\2\2\u034f\u0344\3\2\2\2\u034f\u0345\3\2\2\2\u034f")
        buf.write("\u0346\3\2\2\2\u034f\u0347\3\2\2\2\u034f\u0348\3\2\2\2")
        buf.write("\u034f\u0349\3\2\2\2\u034f\u034a\3\2\2\2\u034f\u034b\3")
        buf.write("\2\2\2\u034f\u034c\3\2\2\2\u034f\u034d\3\2\2\2\u034f\u034e")
        buf.write("\3\2\2\2\u0350\u0352\3\2\2\2\u0351\u033c\3\2\2\2\u0351")
        buf.write("\u034f\3\2\2\2\u0352\u035b\3\2\2\2\u0353\u0354\f\5\2\2")
        buf.write("\u0354\u0355\5 \21\2\u0355\u0356\5\u009eP\6\u0356\u035a")
        buf.write("\3\2\2\2\u0357\u0358\f\3\2\2\u0358\u035a\7\30\2\2\u0359")
        buf.write("\u0353\3\2\2\2\u0359\u0357\3\2\2\2\u035a\u035d\3\2\2\2")
        buf.write("\u035b\u0359\3\2\2\2\u035b\u035c\3\2\2\2\u035c\u009f\3")
        buf.write("\2\2\2\u035d\u035b\3\2\2\2i\u00a3\u00a7\u00aa\u00af\u00d7")
        buf.write("\u00e0\u00e2\u00eb\u00f1\u00f7\u00fd\u0102\u0109\u0110")
        buf.write("\u0117\u011a\u0120\u0122\u0130\u0132\u0144\u0148\u014f")
        buf.write("\u0154\u0157\u0162\u016a\u016c\u0177\u0181\u0185\u0188")
        buf.write("\u019e\u01a0\u01a8\u01aa\u01af\u01b2\u01c5\u01c7\u01cf")
        buf.write("\u01d1\u01d6\u01d9\u01ee\u01f0\u01f8\u01fa\u01ff\u0207")
        buf.write("\u0210\u0212\u021a\u021c\u0221\u0226\u0229\u0236\u0238")
        buf.write("\u0240\u0242\u0247\u024f\u0253\u025a\u0261\u0268\u026b")
        buf.write("\u0271\u0282\u0284\u028c\u028e\u0293\u029e\u02a6\u02a8")
        buf.write("\u02b4\u02bd\u02bf\u02c7\u02c9\u02ce\u02d1\u02d7\u02e3")
        buf.write("\u02e5\u02ed\u02ef\u02f4\u02fb\u02fe\u0308\u0320\u0322")
        buf.write("\u032a\u032c\u0331\u0334\u034f\u0351\u0359\u035b")
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
                     "<INVALID>", "'('", "')'", "'name '", "'annotation '", 
                     "'extension '", "'Superclass'", "'implementation '", 
                     "'Interface '", "<INVALID>", "'abstract function '", 
                     "'constructor '", "'parameter '", "'type '", "'specifier '", 
                     "'visibility '", "'return value '", "<INVALID>", "'configuration file '", 
                     "'property '", "'expression statement '", "'value '", 
                     "'initial value '", "'class '", "'subclass '" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "SPACE", "Alphabet", "NL", 
                      "LPAREN", "RPAREN", "NAME", "ANNOTATION", "EXTENSION", 
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
    RULE_functionParameters = 41
    RULE_functionParameterCondition = 42
    RULE_functionParameterConditionTransition = 43
    RULE_functionParameterExpression = 44
    RULE_types = 45
    RULE_typeCondition = 46
    RULE_specifiers = 47
    RULE_specifierCondition = 48
    RULE_visibilities = 49
    RULE_visibilityCondition = 50
    RULE_returnValues = 51
    RULE_returnValueCondition = 52
    RULE_declarationStatements = 53
    RULE_declarationStatementOf = 54
    RULE_declarationStatementCondition = 55
    RULE_declarationStatementExpression = 56
    RULE_configurationFiles = 57
    RULE_configurationFileCondition = 58
    RULE_configurationFileExpression = 59
    RULE_configurationProperties = 60
    RULE_configurationPropertyCondition = 61
    RULE_configurationPropertyExpression = 62
    RULE_expressionStatements = 63
    RULE_expressionStatementOf = 64
    RULE_expressionStatementCondition = 65
    RULE_expressionStatementExpression = 66
    RULE_value = 67
    RULE_valueCondition = 68
    RULE_initialValues = 69
    RULE_initialValueOf = 70
    RULE_initialValueCondition = 71
    RULE_classes = 72
    RULE_classCondition = 73
    RULE_classExpression = 74
    RULE_subclasses = 75
    RULE_subclassOf = 76
    RULE_subclassCondition = 77
    RULE_subclassExpression = 78

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
                   "parameterExpression", "functionParameters", "functionParameterCondition", 
                   "functionParameterConditionTransition", "functionParameterExpression", 
                   "types", "typeCondition", "specifiers", "specifierCondition", 
                   "visibilities", "visibilityCondition", "returnValues", 
                   "returnValueCondition", "declarationStatements", "declarationStatementOf", 
                   "declarationStatementCondition", "declarationStatementExpression", 
                   "configurationFiles", "configurationFileCondition", "configurationFileExpression", 
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
    T__18=19
    T__19=20
    T__20=21
    SPACE=22
    Alphabet=23
    NL=24
    LPAREN=25
    RPAREN=26
    NAME=27
    ANNOTATION=28
    EXTENSION=29
    SUPERCLASS=30
    IMPLEMENTATION=31
    INTERFACE=32
    FUNCTION=33
    AbstractFunctions=34
    CONSTRUCTOR=35
    PARAMETER=36
    TYPES=37
    SPECIFIER=38
    VISIBILITY=39
    ReturnValue=40
    DeclarationStatement=41
    ConfigurationFile=42
    CONFIGURATION_PROPERTIES=43
    ExpressionStatement=44
    VALUE=45
    InitialValue=46
    CLASSES=47
    SUBCLASSES=48

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
            self.state = 165
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.EOF, RulepadGrammarParser.T__6, RulepadGrammarParser.NL]:
                self.state = 161
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 158
                        self.emptyLine() 
                    self.state = 163
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

                pass
            elif token in [RulepadGrammarParser.FUNCTION, RulepadGrammarParser.AbstractFunctions, RulepadGrammarParser.CONSTRUCTOR, RulepadGrammarParser.PARAMETER, RulepadGrammarParser.DeclarationStatement, RulepadGrammarParser.CLASSES, RulepadGrammarParser.SUBCLASSES]:
                self.state = 164
                self.mustClause()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RulepadGrammarParser.T__6:
                self.state = 167
                self.end()


            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RulepadGrammarParser.NL:
                self.state = 170
                self.match(RulepadGrammarParser.NL)
                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 176
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
            self.state = 213
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.FUNCTION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.functions()
                self.state = 179
                self.must()
                self.state = 180
                self.have()
                self.state = 181
                self.functionExpression(0)
                pass
            elif token in [RulepadGrammarParser.AbstractFunctions]:
                self.enterOuterAlt(localctx, 2)
                self.state = 183
                self.abstractFunctions()
                self.state = 184
                self.must()
                self.state = 185
                self.have()
                self.state = 186
                self.abstractFunctionExpression(0)
                pass
            elif token in [RulepadGrammarParser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 188
                self.constructors()
                self.state = 189
                self.must()
                self.state = 190
                self.have()
                self.state = 191
                self.constructorExpression(0)
                pass
            elif token in [RulepadGrammarParser.CLASSES]:
                self.enterOuterAlt(localctx, 4)
                self.state = 193
                self.classes()
                self.state = 194
                self.must()
                self.state = 195
                self.have()
                self.state = 196
                self.classExpression(0)
                pass
            elif token in [RulepadGrammarParser.PARAMETER]:
                self.enterOuterAlt(localctx, 5)
                self.state = 198
                self.parameters()
                self.state = 199
                self.must()
                self.state = 200
                self.have()
                self.state = 201
                self.parameterExpression(0)
                pass
            elif token in [RulepadGrammarParser.DeclarationStatement]:
                self.enterOuterAlt(localctx, 6)
                self.state = 203
                self.declarationStatements()
                self.state = 204
                self.must()
                self.state = 205
                self.have()
                self.state = 206
                self.declarationStatementExpression(0)
                pass
            elif token in [RulepadGrammarParser.SUBCLASSES]:
                self.enterOuterAlt(localctx, 7)
                self.state = 208
                self.subclasses()
                self.state = 209
                self.must()
                self.state = 210
                self.have()
                self.state = 211
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
            self.state = 215
            self.match(RulepadGrammarParser.T__0)
            self.state = 224
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 222
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        self.state = 216
                        self.word()
                        self.state = 217
                        self.match(RulepadGrammarParser.T__1)
                        pass

                    elif la_ == 2:
                        self.state = 219
                        self.word()
                        self.state = 220
                        self.match(RulepadGrammarParser.T__2)
                        pass

             
                self.state = 226
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 227
            self.word()
            self.state = 228
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
            self.state = 280
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 231 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 230
                    self.match(RulepadGrammarParser.Alphabet)
                    self.state = 233 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==RulepadGrammarParser.Alphabet):
                        break

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
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

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 241
                self.match(RulepadGrammarParser.T__4)
                self.state = 243 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 242
                    self.match(RulepadGrammarParser.Alphabet)
                    self.state = 245 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==RulepadGrammarParser.Alphabet):
                        break

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 247
                self.match(RulepadGrammarParser.T__5)
                self.state = 249 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 248
                    self.match(RulepadGrammarParser.Alphabet)
                    self.state = 251 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==RulepadGrammarParser.Alphabet):
                        break

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 254 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 253
                    self.match(RulepadGrammarParser.Alphabet)
                    self.state = 256 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==RulepadGrammarParser.Alphabet):
                        break

                self.state = 258
                self.match(RulepadGrammarParser.T__4)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 259
                self.match(RulepadGrammarParser.T__3)
                self.state = 261 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 260
                    self.match(RulepadGrammarParser.Alphabet)
                    self.state = 263 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==RulepadGrammarParser.Alphabet):
                        break

                self.state = 265
                self.match(RulepadGrammarParser.T__4)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 266
                self.match(RulepadGrammarParser.T__4)
                self.state = 268 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 267
                    self.match(RulepadGrammarParser.Alphabet)
                    self.state = 270 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==RulepadGrammarParser.Alphabet):
                        break

                self.state = 272
                self.match(RulepadGrammarParser.T__4)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 273
                self.match(RulepadGrammarParser.T__5)
                self.state = 275 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 274
                    self.match(RulepadGrammarParser.Alphabet)
                    self.state = 277 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==RulepadGrammarParser.Alphabet):
                        break

                self.state = 279
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
            self.state = 282
            self.match(RulepadGrammarParser.T__0)
            self.state = 286 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 286
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.Alphabet]:
                    self.state = 283
                    self.match(RulepadGrammarParser.Alphabet)
                    pass
                elif token in [RulepadGrammarParser.T__6, RulepadGrammarParser.T__7, RulepadGrammarParser.T__8, RulepadGrammarParser.T__9, RulepadGrammarParser.T__10, RulepadGrammarParser.T__11, RulepadGrammarParser.T__12, RulepadGrammarParser.T__13, RulepadGrammarParser.T__14, RulepadGrammarParser.LPAREN, RulepadGrammarParser.RPAREN]:
                    self.state = 284
                    self.symbols()
                    pass
                elif token in [RulepadGrammarParser.SPACE]:
                    self.state = 285
                    self.match(RulepadGrammarParser.SPACE)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 288 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RulepadGrammarParser.T__6) | (1 << RulepadGrammarParser.T__7) | (1 << RulepadGrammarParser.T__8) | (1 << RulepadGrammarParser.T__9) | (1 << RulepadGrammarParser.T__10) | (1 << RulepadGrammarParser.T__11) | (1 << RulepadGrammarParser.T__12) | (1 << RulepadGrammarParser.T__13) | (1 << RulepadGrammarParser.T__14) | (1 << RulepadGrammarParser.SPACE) | (1 << RulepadGrammarParser.Alphabet) | (1 << RulepadGrammarParser.LPAREN) | (1 << RulepadGrammarParser.RPAREN))) != 0)):
                    break

            self.state = 290
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
            self.state = 292
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
            self.state = 294
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
            self.state = 296
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
            self.state = 298
            self.match(RulepadGrammarParser.T__0)
            self.state = 302 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 302
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.Alphabet]:
                    self.state = 299
                    self.match(RulepadGrammarParser.Alphabet)
                    pass
                elif token in [RulepadGrammarParser.T__6, RulepadGrammarParser.T__7, RulepadGrammarParser.T__8, RulepadGrammarParser.T__9, RulepadGrammarParser.T__10, RulepadGrammarParser.T__11, RulepadGrammarParser.T__12, RulepadGrammarParser.T__13, RulepadGrammarParser.T__14, RulepadGrammarParser.LPAREN, RulepadGrammarParser.RPAREN]:
                    self.state = 300
                    self.symbols()
                    pass
                elif token in [RulepadGrammarParser.SPACE]:
                    self.state = 301
                    self.match(RulepadGrammarParser.SPACE)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 304 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RulepadGrammarParser.T__6) | (1 << RulepadGrammarParser.T__7) | (1 << RulepadGrammarParser.T__8) | (1 << RulepadGrammarParser.T__9) | (1 << RulepadGrammarParser.T__10) | (1 << RulepadGrammarParser.T__11) | (1 << RulepadGrammarParser.T__12) | (1 << RulepadGrammarParser.T__13) | (1 << RulepadGrammarParser.T__14) | (1 << RulepadGrammarParser.SPACE) | (1 << RulepadGrammarParser.Alphabet) | (1 << RulepadGrammarParser.LPAREN) | (1 << RulepadGrammarParser.RPAREN))) != 0)):
                    break

            self.state = 306
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
            self.state = 308
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
            self.state = 310
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
            self.state = 312
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
            self.state = 314
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
            self.state = 316
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
            self.state = 318
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
            self.state = 322
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.T__17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 320
                self.and_()
                pass
            elif token in [RulepadGrammarParser.T__18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 321
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
            self.state = 324
            self.match(RulepadGrammarParser.NAME)
            self.state = 326
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 325
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
            self.state = 328
            self.words()
            self.state = 329
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
        self.enterRule(localctx, 36, self.RULE_annotations)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.match(RulepadGrammarParser.ANNOTATION)
            self.state = 333
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 332
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
        self.enterRule(localctx, 38, self.RULE_annotationCondition)
        try:
            self.state = 341
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 335
                self.combinatorialWords()
                self.state = 336
                self.match(RulepadGrammarParser.SPACE)
                self.state = 338
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                if la_ == 1:
                    self.state = 337
                    self.annotationConditionTransition()


                pass
            elif token in [RulepadGrammarParser.T__20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 340
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
        self.enterRule(localctx, 40, self.RULE_annotationConditionTransition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.withWord()
            self.state = 344
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
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_annotationExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 347
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 348
                self.annotationExpression(0)
                self.state = 349
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.PARAMETER]:
                self.state = 351
                self.parameters()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 362
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 360
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.AnnotationExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_annotationExpression)
                        self.state = 354
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 355
                        localctx.op = self.binary()
                        self.state = 356
                        localctx.right = self.annotationExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.AnnotationExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_annotationExpression)
                        self.state = 358
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 359
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 364
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
        self.enterRule(localctx, 44, self.RULE_extensions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.match(RulepadGrammarParser.EXTENSION)
            self.state = 366
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
        self.enterRule(localctx, 46, self.RULE_extensionCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            self.of()
            self.state = 373
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.T__0]:
                self.state = 369
                self.combinatorialWords()
                self.state = 370
                self.match(RulepadGrammarParser.SPACE)
                pass
            elif token in [RulepadGrammarParser.SUPERCLASS]:
                self.state = 372
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
        self.enterRule(localctx, 48, self.RULE_implementations)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self.match(RulepadGrammarParser.IMPLEMENTATION)
            self.state = 376
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
        self.enterRule(localctx, 50, self.RULE_implementationCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.of()
            self.state = 383
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.T__0]:
                self.state = 379
                self.combinatorialWords()
                self.state = 380
                self.match(RulepadGrammarParser.SPACE)
                pass
            elif token in [RulepadGrammarParser.INTERFACE]:
                self.state = 382
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
            self.state = 385
            self.match(RulepadGrammarParser.FUNCTION)
            self.state = 387
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 386
                self.functionCondition()


            self.state = 390
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 389
                self.functionOf()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionOfContext(ParserRuleContext):

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
            self.state = 392
            self.of()
            self.state = 393
            self.classes()
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
        self.enterRule(localctx, 56, self.RULE_functionCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self.withWord()
            self.state = 396
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


        def specifiers(self):
            return self.getTypedRuleContext(RulepadGrammarParser.SpecifiersContext,0)


        def visibilities(self):
            return self.getTypedRuleContext(RulepadGrammarParser.VisibilitiesContext,0)


        def types(self):
            return self.getTypedRuleContext(RulepadGrammarParser.TypesContext,0)


        def names(self):
            return self.getTypedRuleContext(RulepadGrammarParser.NamesContext,0)


        def functionParameters(self):
            return self.getTypedRuleContext(RulepadGrammarParser.FunctionParametersContext,0)


        def returnValues(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ReturnValuesContext,0)


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
            self.state = 414
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 399
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 400
                self.functionExpression(0)
                self.state = 401
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.T__0, RulepadGrammarParser.NAME, RulepadGrammarParser.ANNOTATION, RulepadGrammarParser.PARAMETER, RulepadGrammarParser.TYPES, RulepadGrammarParser.SPECIFIER, RulepadGrammarParser.VISIBILITY, RulepadGrammarParser.ReturnValue, RulepadGrammarParser.ExpressionStatement]:
                self.state = 412
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.ANNOTATION]:
                    self.state = 403
                    self.annotations()
                    pass
                elif token in [RulepadGrammarParser.SPECIFIER]:
                    self.state = 404
                    self.specifiers()
                    pass
                elif token in [RulepadGrammarParser.VISIBILITY]:
                    self.state = 405
                    self.visibilities()
                    pass
                elif token in [RulepadGrammarParser.TYPES]:
                    self.state = 406
                    self.types()
                    pass
                elif token in [RulepadGrammarParser.NAME]:
                    self.state = 407
                    self.names()
                    pass
                elif token in [RulepadGrammarParser.PARAMETER]:
                    self.state = 408
                    self.functionParameters()
                    pass
                elif token in [RulepadGrammarParser.ReturnValue]:
                    self.state = 409
                    self.returnValues()
                    pass
                elif token in [RulepadGrammarParser.ExpressionStatement]:
                    self.state = 410
                    self.expressionStatements()
                    pass
                elif token in [RulepadGrammarParser.T__0]:
                    self.state = 411
                    self.comments()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 424
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 422
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.FunctionExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_functionExpression)
                        self.state = 416
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 417
                        localctx.op = self.binary()
                        self.state = 418
                        localctx.right = self.functionExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.FunctionExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_functionExpression)
                        self.state = 420
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 421
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 426
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
            self.state = 427
            self.match(RulepadGrammarParser.AbstractFunctions)
            self.state = 429
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 428
                self.abstractFunctionCondition()


            self.state = 432
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 431
                self.abstractFunctionOf()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AbstractFunctionOfContext(ParserRuleContext):

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
            self.state = 434
            self.of()
            self.state = 435
            self.classes()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AbstractFunctionConditionContext(ParserRuleContext):

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
            self.state = 437
            self.withWord()
            self.state = 438
            self.abstractFunctionExpression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AbstractFunctionExpressionContext(ParserRuleContext):

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
            self.state = 453
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 441
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 442
                self.abstractFunctionExpression(0)
                self.state = 443
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.NAME, RulepadGrammarParser.ANNOTATION, RulepadGrammarParser.PARAMETER, RulepadGrammarParser.TYPES, RulepadGrammarParser.SPECIFIER, RulepadGrammarParser.VISIBILITY]:
                self.state = 451
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.ANNOTATION]:
                    self.state = 445
                    self.annotations()
                    pass
                elif token in [RulepadGrammarParser.SPECIFIER]:
                    self.state = 446
                    self.specifiers()
                    pass
                elif token in [RulepadGrammarParser.VISIBILITY]:
                    self.state = 447
                    self.visibilities()
                    pass
                elif token in [RulepadGrammarParser.TYPES]:
                    self.state = 448
                    self.types()
                    pass
                elif token in [RulepadGrammarParser.NAME]:
                    self.state = 449
                    self.names()
                    pass
                elif token in [RulepadGrammarParser.PARAMETER]:
                    self.state = 450
                    self.parameters()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 463
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 461
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.AbstractFunctionExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_abstractFunctionExpression)
                        self.state = 455
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 456
                        localctx.op = self.binary()
                        self.state = 457
                        localctx.right = self.abstractFunctionExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.AbstractFunctionExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_abstractFunctionExpression)
                        self.state = 459
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 460
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 465
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
            self.state = 466
            self.match(RulepadGrammarParser.CONSTRUCTOR)
            self.state = 468
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 467
                self.constructorCondition()


            self.state = 471
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.state = 470
                self.constructorOf()


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
            self.state = 473
            self.of()
            self.state = 474
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
            self.state = 476
            self.withWord()
            self.state = 477
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
            self.state = 494
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 480
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 481
                self.constructorExpression(0)
                self.state = 482
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.T__0, RulepadGrammarParser.ANNOTATION, RulepadGrammarParser.PARAMETER, RulepadGrammarParser.SPECIFIER, RulepadGrammarParser.VISIBILITY, RulepadGrammarParser.ReturnValue, RulepadGrammarParser.DeclarationStatement, RulepadGrammarParser.ExpressionStatement]:
                self.state = 492
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.ANNOTATION]:
                    self.state = 484
                    self.annotations()
                    pass
                elif token in [RulepadGrammarParser.SPECIFIER]:
                    self.state = 485
                    self.specifiers()
                    pass
                elif token in [RulepadGrammarParser.VISIBILITY]:
                    self.state = 486
                    self.visibilities()
                    pass
                elif token in [RulepadGrammarParser.PARAMETER]:
                    self.state = 487
                    self.parameters()
                    pass
                elif token in [RulepadGrammarParser.ReturnValue]:
                    self.state = 488
                    self.returnValues()
                    pass
                elif token in [RulepadGrammarParser.DeclarationStatement]:
                    self.state = 489
                    self.declarationStatements()
                    pass
                elif token in [RulepadGrammarParser.ExpressionStatement]:
                    self.state = 490
                    self.expressionStatements()
                    pass
                elif token in [RulepadGrammarParser.T__0]:
                    self.state = 491
                    self.comments()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 504
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 502
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.ConstructorExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_constructorExpression)
                        self.state = 496
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 497
                        localctx.op = self.binary()
                        self.state = 498
                        localctx.right = self.constructorExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.ConstructorExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_constructorExpression)
                        self.state = 500
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 501
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 506
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
            self.state = 507
            self.match(RulepadGrammarParser.PARAMETER)
            self.state = 509
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.state = 508
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

        def withWord(self):
            return self.getTypedRuleContext(RulepadGrammarParser.WithWordContext,0)


        def parameterExpression(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ParameterExpressionContext,0)


        def combinatorialWords(self):
            return self.getTypedRuleContext(RulepadGrammarParser.CombinatorialWordsContext,0)


        def SPACE(self):
            return self.getToken(RulepadGrammarParser.SPACE, 0)

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
            self.state = 517
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.T__20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 511
                self.withWord()
                self.state = 512
                self.parameterExpression(0)
                pass
            elif token in [RulepadGrammarParser.T__0]:
                self.enterOuterAlt(localctx, 2)
                self.state = 514
                self.combinatorialWords()
                self.state = 515
                self.match(RulepadGrammarParser.SPACE)
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
            self.state = 528
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 520
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 521
                self.parameterExpression(0)
                self.state = 522
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.NAME, RulepadGrammarParser.TYPES]:
                self.state = 526
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.TYPES]:
                    self.state = 524
                    self.types()
                    pass
                elif token in [RulepadGrammarParser.NAME]:
                    self.state = 525
                    self.names()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 538
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,53,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 536
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.ParameterExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_parameterExpression)
                        self.state = 530
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 531
                        localctx.op = self.binary()
                        self.state = 532
                        localctx.right = self.parameterExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.ParameterExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_parameterExpression)
                        self.state = 534
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 535
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 540
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,53,self._ctx)

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
        self.enterRule(localctx, 82, self.RULE_functionParameters)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 541
            self.match(RulepadGrammarParser.PARAMETER)
            self.state = 543
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.state = 542
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
        self.enterRule(localctx, 84, self.RULE_functionParameterCondition)
        try:
            self.state = 551
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 545
                self.combinatorialWords()
                self.state = 546
                self.match(RulepadGrammarParser.SPACE)
                self.state = 548
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
                if la_ == 1:
                    self.state = 547
                    self.functionParameterConditionTransition()


                pass
            elif token in [RulepadGrammarParser.T__20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 550
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
        self.enterRule(localctx, 86, self.RULE_functionParameterConditionTransition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 553
            self.withWord()
            self.state = 554
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
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_functionParameterExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 566
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 557
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 558
                self.functionParameterExpression(0)
                self.state = 559
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.NAME, RulepadGrammarParser.ANNOTATION, RulepadGrammarParser.TYPES]:
                self.state = 564
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.TYPES]:
                    self.state = 561
                    self.types()
                    pass
                elif token in [RulepadGrammarParser.NAME]:
                    self.state = 562
                    self.names()
                    pass
                elif token in [RulepadGrammarParser.ANNOTATION]:
                    self.state = 563
                    self.annotations()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 576
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,60,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 574
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.FunctionParameterExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_functionParameterExpression)
                        self.state = 568
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 569
                        localctx.op = self.binary()
                        self.state = 570
                        localctx.right = self.functionParameterExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.FunctionParameterExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_functionParameterExpression)
                        self.state = 572
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 573
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 578
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,60,self._ctx)

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
        self.enterRule(localctx, 90, self.RULE_types)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 579
            self.match(RulepadGrammarParser.TYPES)
            self.state = 581
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
            if la_ == 1:
                self.state = 580
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
        self.enterRule(localctx, 92, self.RULE_typeCondition)
        try:
            self.state = 589
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,62,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 583
                self.combinatorialWords()
                self.state = 584
                self.match(RulepadGrammarParser.SPACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 586
                self.words()
                self.state = 587
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
        self.enterRule(localctx, 94, self.RULE_specifiers)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 591
            self.match(RulepadGrammarParser.SPECIFIER)
            self.state = 593
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                self.state = 592
                self.specifierCondition()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SpecifierConditionContext(ParserRuleContext):

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
        self.enterRule(localctx, 96, self.RULE_specifierCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 595
            self.words()
            self.state = 596
            self.match(RulepadGrammarParser.SPACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VisibilitiesContext(ParserRuleContext):

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
        self.enterRule(localctx, 98, self.RULE_visibilities)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 598
            self.match(RulepadGrammarParser.VISIBILITY)
            self.state = 600
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
            if la_ == 1:
                self.state = 599
                self.visibilityCondition()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VisibilityConditionContext(ParserRuleContext):

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
        self.enterRule(localctx, 100, self.RULE_visibilityCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 602
            self.words()
            self.state = 603
            self.match(RulepadGrammarParser.SPACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnValuesContext(ParserRuleContext):

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
        self.enterRule(localctx, 102, self.RULE_returnValues)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 605
            self.match(RulepadGrammarParser.ReturnValue)
            self.state = 607
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
            if la_ == 1:
                self.state = 606
                self.returnValueCondition()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnValueConditionContext(ParserRuleContext):

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
        self.enterRule(localctx, 104, self.RULE_returnValueCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 609
            self.combinatorialWords()
            self.state = 610
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
        self.enterRule(localctx, 106, self.RULE_declarationStatements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 612
            self.match(RulepadGrammarParser.DeclarationStatement)
            self.state = 614
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,66,self._ctx)
            if la_ == 1:
                self.state = 613
                self.declarationStatementCondition()


            self.state = 617
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,67,self._ctx)
            if la_ == 1:
                self.state = 616
                self.declarationStatementOf()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationStatementOfContext(ParserRuleContext):

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
        self.enterRule(localctx, 108, self.RULE_declarationStatementOf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 619
            self.of()
            self.state = 623
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.CLASSES]:
                self.state = 620
                self.classes()
                pass
            elif token in [RulepadGrammarParser.FUNCTION]:
                self.state = 621
                self.functions()
                pass
            elif token in [RulepadGrammarParser.CONSTRUCTOR]:
                self.state = 622
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
        self.enterRule(localctx, 110, self.RULE_declarationStatementCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 625
            self.withWord()
            self.state = 626
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
        _startState = 112
        self.enterRecursionRule(localctx, 112, self.RULE_declarationStatementExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 642
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 629
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 630
                self.declarationStatementExpression(0)
                self.state = 631
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.T__0, RulepadGrammarParser.NAME, RulepadGrammarParser.ANNOTATION, RulepadGrammarParser.TYPES, RulepadGrammarParser.SPECIFIER, RulepadGrammarParser.VISIBILITY, RulepadGrammarParser.InitialValue]:
                self.state = 640
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.ANNOTATION]:
                    self.state = 633
                    self.annotations()
                    pass
                elif token in [RulepadGrammarParser.SPECIFIER]:
                    self.state = 634
                    self.specifiers()
                    pass
                elif token in [RulepadGrammarParser.VISIBILITY]:
                    self.state = 635
                    self.visibilities()
                    pass
                elif token in [RulepadGrammarParser.TYPES]:
                    self.state = 636
                    self.types()
                    pass
                elif token in [RulepadGrammarParser.NAME]:
                    self.state = 637
                    self.names()
                    pass
                elif token in [RulepadGrammarParser.InitialValue]:
                    self.state = 638
                    self.initialValues()
                    pass
                elif token in [RulepadGrammarParser.T__0]:
                    self.state = 639
                    self.comments()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 652
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,72,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 650
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,71,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.DeclarationStatementExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_declarationStatementExpression)
                        self.state = 644
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 645
                        localctx.op = self.binary()
                        self.state = 646
                        localctx.right = self.declarationStatementExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.DeclarationStatementExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_declarationStatementExpression)
                        self.state = 648
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 649
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 654
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,72,self._ctx)

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
        self.enterRule(localctx, 114, self.RULE_configurationFiles)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 655
            self.match(RulepadGrammarParser.ConfigurationFile)
            self.state = 657
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,73,self._ctx)
            if la_ == 1:
                self.state = 656
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
        self.enterRule(localctx, 116, self.RULE_configurationFileCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 659
            self.withWord()
            self.state = 660
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
        _startState = 118
        self.enterRecursionRule(localctx, 118, self.RULE_configurationFileExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 668
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 663
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 664
                self.configurationFileExpression(0)
                self.state = 665
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.CONFIGURATION_PROPERTIES]:
                self.state = 667
                self.configurationProperties()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 678
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,76,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 676
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,75,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.ConfigurationFileExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_configurationFileExpression)
                        self.state = 670
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 671
                        localctx.op = self.binary()
                        self.state = 672
                        localctx.right = self.configurationFileExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.ConfigurationFileExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_configurationFileExpression)
                        self.state = 674
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 675
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 680
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,76,self._ctx)

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
        self.enterRule(localctx, 120, self.RULE_configurationProperties)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 681
            self.match(RulepadGrammarParser.CONFIGURATION_PROPERTIES)
            self.state = 682
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

        def withWord(self):
            return self.getTypedRuleContext(RulepadGrammarParser.WithWordContext,0)


        def configurationPropertyExpression(self):
            return self.getTypedRuleContext(RulepadGrammarParser.ConfigurationPropertyExpressionContext,0)


        def combinatorialWords(self):
            return self.getTypedRuleContext(RulepadGrammarParser.CombinatorialWordsContext,0)


        def SPACE(self):
            return self.getToken(RulepadGrammarParser.SPACE, 0)

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
        self.enterRule(localctx, 122, self.RULE_configurationPropertyCondition)
        try:
            self.state = 690
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.T__20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 684
                self.withWord()
                self.state = 685
                self.configurationPropertyExpression(0)
                pass
            elif token in [RulepadGrammarParser.T__0]:
                self.enterOuterAlt(localctx, 2)
                self.state = 687
                self.combinatorialWords()
                self.state = 688
                self.match(RulepadGrammarParser.SPACE)
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
        _startState = 124
        self.enterRecursionRule(localctx, 124, self.RULE_configurationPropertyExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 701
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 693
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 694
                self.configurationPropertyExpression(0)
                self.state = 695
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.NAME, RulepadGrammarParser.TYPES]:
                self.state = 699
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.TYPES]:
                    self.state = 697
                    self.types()
                    pass
                elif token in [RulepadGrammarParser.NAME]:
                    self.state = 698
                    self.names()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 711
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,81,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 709
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,80,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.ConfigurationPropertyExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_configurationPropertyExpression)
                        self.state = 703
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 704
                        localctx.op = self.binary()
                        self.state = 705
                        localctx.right = self.configurationPropertyExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.ConfigurationPropertyExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_configurationPropertyExpression)
                        self.state = 707
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 708
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 713
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,81,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExpressionStatementsContext(ParserRuleContext):

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
        self.enterRule(localctx, 126, self.RULE_expressionStatements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 714
            self.match(RulepadGrammarParser.ExpressionStatement)
            self.state = 716
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,82,self._ctx)
            if la_ == 1:
                self.state = 715
                self.expressionStatementCondition()


            self.state = 719
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,83,self._ctx)
            if la_ == 1:
                self.state = 718
                self.expressionStatementOf()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionStatementOfContext(ParserRuleContext):

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
        self.enterRule(localctx, 128, self.RULE_expressionStatementOf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 721
            self.of()
            self.state = 725
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,84,self._ctx)
            if la_ == 1:
                self.state = 722
                self.functions()
                pass

            elif la_ == 2:
                self.state = 723
                self.constructors()
                pass

            elif la_ == 3:
                self.state = 724
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
        self.enterRule(localctx, 130, self.RULE_expressionStatementCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 727
            self.withWord()
            self.state = 728
            self.expressionStatementExpression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionStatementExpressionContext(ParserRuleContext):

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
        _startState = 132
        self.enterRecursionRule(localctx, 132, self.RULE_expressionStatementExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 739
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 731
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 732
                self.expressionStatementExpression(0)
                self.state = 733
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.T__0, RulepadGrammarParser.VALUE]:
                self.state = 737
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.T__0]:
                    self.state = 735
                    self.comments()
                    pass
                elif token in [RulepadGrammarParser.VALUE]:
                    self.state = 736
                    self.value()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 749
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,88,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 747
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,87,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.ExpressionStatementExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressionStatementExpression)
                        self.state = 741
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 742
                        localctx.op = self.binary()
                        self.state = 743
                        localctx.right = self.expressionStatementExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.ExpressionStatementExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressionStatementExpression)
                        self.state = 745
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 746
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 751
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,88,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ValueContext(ParserRuleContext):

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
        self.enterRule(localctx, 134, self.RULE_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 752
            self.match(RulepadGrammarParser.VALUE)
            self.state = 754
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,89,self._ctx)
            if la_ == 1:
                self.state = 753
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
        self.enterRule(localctx, 136, self.RULE_valueCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 756
            self.combinatorialWords()
            self.state = 757
            self.match(RulepadGrammarParser.SPACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitialValuesContext(ParserRuleContext):

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
        self.enterRule(localctx, 138, self.RULE_initialValues)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 759
            self.match(RulepadGrammarParser.InitialValue)
            self.state = 761
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,90,self._ctx)
            if la_ == 1:
                self.state = 760
                self.initialValueCondition()


            self.state = 764
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,91,self._ctx)
            if la_ == 1:
                self.state = 763
                self.initialValueOf()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitialValueOfContext(ParserRuleContext):

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
        self.enterRule(localctx, 140, self.RULE_initialValueOf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 766
            self.of()
            self.state = 767
            self.declarationStatements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitialValueConditionContext(ParserRuleContext):

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
        self.enterRule(localctx, 142, self.RULE_initialValueCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 769
            self.combinatorialWords()
            self.state = 770
            self.match(RulepadGrammarParser.SPACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
        self.enterRule(localctx, 144, self.RULE_classes)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 772
            self.match(RulepadGrammarParser.CLASSES)
            self.state = 774
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,92,self._ctx)
            if la_ == 1:
                self.state = 773
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
        self.enterRule(localctx, 146, self.RULE_classCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 776
            self.withWord()
            self.state = 777
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
        _startState = 148
        self.enterRecursionRule(localctx, 148, self.RULE_classExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 800
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 780
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 781
                self.classExpression(0)
                self.state = 782
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.T__0, RulepadGrammarParser.NAME, RulepadGrammarParser.ANNOTATION, RulepadGrammarParser.EXTENSION, RulepadGrammarParser.IMPLEMENTATION, RulepadGrammarParser.FUNCTION, RulepadGrammarParser.AbstractFunctions, RulepadGrammarParser.CONSTRUCTOR, RulepadGrammarParser.SPECIFIER, RulepadGrammarParser.VISIBILITY, RulepadGrammarParser.ReturnValue, RulepadGrammarParser.DeclarationStatement, RulepadGrammarParser.ConfigurationFile, RulepadGrammarParser.SUBCLASSES]:
                self.state = 798
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.ANNOTATION]:
                    self.state = 784
                    self.annotations()
                    pass
                elif token in [RulepadGrammarParser.SPECIFIER]:
                    self.state = 785
                    self.specifiers()
                    pass
                elif token in [RulepadGrammarParser.VISIBILITY]:
                    self.state = 786
                    self.visibilities()
                    pass
                elif token in [RulepadGrammarParser.NAME]:
                    self.state = 787
                    self.names()
                    pass
                elif token in [RulepadGrammarParser.EXTENSION]:
                    self.state = 788
                    self.extensions()
                    pass
                elif token in [RulepadGrammarParser.IMPLEMENTATION]:
                    self.state = 789
                    self.implementations()
                    pass
                elif token in [RulepadGrammarParser.FUNCTION]:
                    self.state = 790
                    self.functions()
                    pass
                elif token in [RulepadGrammarParser.AbstractFunctions]:
                    self.state = 791
                    self.abstractFunctions()
                    pass
                elif token in [RulepadGrammarParser.CONSTRUCTOR]:
                    self.state = 792
                    self.constructors()
                    pass
                elif token in [RulepadGrammarParser.DeclarationStatement]:
                    self.state = 793
                    self.declarationStatements()
                    pass
                elif token in [RulepadGrammarParser.ReturnValue]:
                    self.state = 794
                    self.returnValues()
                    pass
                elif token in [RulepadGrammarParser.T__0]:
                    self.state = 795
                    self.comments()
                    pass
                elif token in [RulepadGrammarParser.SUBCLASSES]:
                    self.state = 796
                    self.subclasses()
                    pass
                elif token in [RulepadGrammarParser.ConfigurationFile]:
                    self.state = 797
                    self.configurationFiles()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 810
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,96,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 808
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,95,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.ClassExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_classExpression)
                        self.state = 802
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 803
                        localctx.op = self.binary()
                        self.state = 804
                        localctx.right = self.classExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.ClassExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_classExpression)
                        self.state = 806
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 807
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 812
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,96,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class SubclassesContext(ParserRuleContext):

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
        self.enterRule(localctx, 150, self.RULE_subclasses)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 813
            self.match(RulepadGrammarParser.SUBCLASSES)
            self.state = 815
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,97,self._ctx)
            if la_ == 1:
                self.state = 814
                self.subclassCondition()


            self.state = 818
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,98,self._ctx)
            if la_ == 1:
                self.state = 817
                self.subclassOf()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubclassOfContext(ParserRuleContext):

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
        self.enterRule(localctx, 152, self.RULE_subclassOf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 820
            self.of()
            self.state = 821
            self.classes()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubclassConditionContext(ParserRuleContext):

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
        self.enterRule(localctx, 154, self.RULE_subclassCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 823
            self.withWord()
            self.state = 824
            self.subclassExpression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubclassExpressionContext(ParserRuleContext):

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
        _startState = 156
        self.enterRecursionRule(localctx, 156, self.RULE_subclassExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 847
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,100,self._ctx)
            if la_ == 1:
                self.state = 827
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 828
                self.subclassExpression(0)
                self.state = 829
                self.match(RulepadGrammarParser.RPAREN)
                pass

            elif la_ == 2:
                self.state = 845
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,99,self._ctx)
                if la_ == 1:
                    self.state = 831
                    self.annotations()
                    pass

                elif la_ == 2:
                    self.state = 832
                    self.specifiers()
                    pass

                elif la_ == 3:
                    self.state = 833
                    self.visibilities()
                    pass

                elif la_ == 4:
                    self.state = 834
                    self.names()
                    pass

                elif la_ == 5:
                    self.state = 835
                    self.extensions()
                    pass

                elif la_ == 6:
                    self.state = 836
                    self.implementations()
                    pass

                elif la_ == 7:
                    self.state = 837
                    self.functions()
                    pass

                elif la_ == 8:
                    self.state = 838
                    self.subclasses()
                    pass

                elif la_ == 9:
                    pass

                elif la_ == 10:
                    self.state = 840
                    self.abstractFunctions()
                    pass

                elif la_ == 11:
                    self.state = 841
                    self.constructors()
                    pass

                elif la_ == 12:
                    self.state = 842
                    self.declarationStatements()
                    pass

                elif la_ == 13:
                    self.state = 843
                    self.returnValues()
                    pass

                elif la_ == 14:
                    self.state = 844
                    self.comments()
                    pass


                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 857
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,102,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 855
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,101,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.SubclassExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_subclassExpression)
                        self.state = 849
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 850
                        localctx.op = self.binary()
                        self.state = 851
                        localctx.right = self.subclassExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.SubclassExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_subclassExpression)
                        self.state = 853
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 854
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 859
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,102,self._ctx)

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
        self._predicates[44] = self.functionParameterExpression_sempred
        self._predicates[56] = self.declarationStatementExpression_sempred
        self._predicates[59] = self.configurationFileExpression_sempred
        self._predicates[62] = self.configurationPropertyExpression_sempred
        self._predicates[66] = self.expressionStatementExpression_sempred
        self._predicates[74] = self.classExpression_sempred
        self._predicates[78] = self.subclassExpression_sempred
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
         

    def functionParameterExpression_sempred(self, localctx:FunctionParameterExpressionContext, predIndex:int):
            if predIndex == 10:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 1)
         

    def declarationStatementExpression_sempred(self, localctx:DeclarationStatementExpressionContext, predIndex:int):
            if predIndex == 12:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 1)
         

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
         

    def expressionStatementExpression_sempred(self, localctx:ExpressionStatementExpressionContext, predIndex:int):
            if predIndex == 18:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 19:
                return self.precpred(self._ctx, 1)
         

    def classExpression_sempred(self, localctx:ClassExpressionContext, predIndex:int):
            if predIndex == 20:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 21:
                return self.precpred(self._ctx, 1)
         

    def subclassExpression_sempred(self, localctx:SubclassExpressionContext, predIndex:int):
            if predIndex == 22:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 23:
                return self.precpred(self._ctx, 1)
         




