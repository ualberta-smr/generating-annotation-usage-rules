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
        buf.write("\u02a6\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\3\2\7\2\u0092\n\2\f\2\16\2\u0095")
        buf.write("\13\2\3\2\5\2\u0098\n\2\3\2\5\2\u009b\n\2\3\2\7\2\u009e")
        buf.write("\n\2\f\2\16\2\u00a1\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\5\3\u00b9\n\3\3\4\3\4\3\4\3\4\6\4\u00bf\n\4\r\4\16")
        buf.write("\4\u00c0\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3")
        buf.write("\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\5\16\u00d9")
        buf.write("\n\16\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\5\24\u00ed\n")
        buf.write("\24\3\24\5\24\u00f0\n\24\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\5\26\u00fb\n\26\3\26\3\26\3\26\3\26\3")
        buf.write("\26\3\26\7\26\u0103\n\26\f\26\16\26\u0106\13\26\3\27\3")
        buf.write("\27\3\27\3\30\3\30\3\30\3\30\3\30\5\30\u0110\n\30\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\32\3\32\5\32\u011a\n\32\3")
        buf.write("\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u012e\n\35\5")
        buf.write("\35\u0130\n\35\3\35\3\35\3\35\3\35\3\35\3\35\7\35\u0138")
        buf.write("\n\35\f\35\16\35\u013b\13\35\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \5 \u014c\n \3")
        buf.write("!\3!\3!\3!\3!\5!\u0153\n!\3!\3!\3!\3!\7!\u0159\n!\f!\16")
        buf.write("!\u015c\13!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&")
        buf.write("\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\5\'\u0174\n\'\5\'\u0176")
        buf.write("\n\'\3\'\3\'\3\'\3\'\3\'\3\'\7\'\u017e\n\'\f\'\16\'\u0181")
        buf.write("\13\'\3(\3(\3(\3)\3)\3)\5)\u0189\n)\3)\5)\u018c\n)\3*")
        buf.write("\3*\3*\3+\3+\3+\3+\3+\3+\3+\3+\5+\u0199\n+\5+\u019b\n")
        buf.write("+\3+\3+\3+\3+\3+\3+\7+\u01a3\n+\f+\16+\u01a6\13+\3,\3")
        buf.write(",\5,\u01aa\n,\3-\3-\3-\5-\u01af\n-\3-\5-\u01b2\n-\3.\3")
        buf.write(".\3.\3/\3/\3/\3/\3/\3/\3/\3/\5/\u01bf\n/\5/\u01c1\n/\3")
        buf.write("/\3/\3/\3/\3/\3/\7/\u01c9\n/\f/\16/\u01cc\13/\3\60\3\60")
        buf.write("\3\60\3\61\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3\63\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\5\64")
        buf.write("\u01e5\n\64\5\64\u01e7\n\64\3\64\3\64\3\64\3\64\3\64\3")
        buf.write("\64\7\64\u01ef\n\64\f\64\16\64\u01f2\13\64\3\65\3\65\3")
        buf.write("\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\67\3\67\3\67")
        buf.write("\3\67\5\67\u0202\n\67\38\38\38\38\58\u0208\n8\38\38\3")
        buf.write("8\38\78\u020e\n8\f8\168\u0211\138\39\39\39\3:\3:\3:\3")
        buf.write(";\3;\3;\3;\3;\3;\5;\u021f\n;\3;\3;\3;\3;\3;\3;\7;\u0227")
        buf.write("\n;\f;\16;\u022a\13;\3<\3<\3<\3=\3=\3=\5=\u0232\n=\3=")
        buf.write("\5=\u0235\n=\3>\3>\3>\3?\3?\3?\3?\3?\3?\3?\3?\5?\u0242")
        buf.write("\n?\5?\u0244\n?\3?\3?\3?\3?\3?\3?\7?\u024c\n?\f?\16?\u024f")
        buf.write("\13?\3@\3@\3@\3A\3A\3A\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3")
        buf.write("B\3B\3B\3B\3B\3B\3B\5B\u0268\nB\5B\u026a\nB\3B\3B\3B\3")
        buf.write("B\3B\3B\7B\u0272\nB\fB\16B\u0275\13B\3C\3C\3C\3C\3C\3")
        buf.write("D\3D\3D\3D\3D\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\5E\u028b\n")
        buf.write("E\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\5F\u0297\nF\3F\3F\3F\3")
        buf.write("F\7F\u029d\nF\fF\16F\u02a0\13F\3G\3G\3H\3H\3H\2\16*8@")
        buf.write("LT\\fnt|\u0082\u008aI\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfh")
        buf.write("jlnprtvxz|~\u0080\u0082\u0084\u0086\u0088\u008a\u008c")
        buf.write("\u008e\2\3\4\2\4\f\26\27\2\u02c9\2\u0097\3\2\2\2\4\u00b8")
        buf.write("\3\2\2\2\6\u00ba\3\2\2\2\b\u00c4\3\2\2\2\n\u00c6\3\2\2")
        buf.write("\2\f\u00c8\3\2\2\2\16\u00ca\3\2\2\2\20\u00cc\3\2\2\2\22")
        buf.write("\u00ce\3\2\2\2\24\u00d0\3\2\2\2\26\u00d2\3\2\2\2\30\u00d4")
        buf.write("\3\2\2\2\32\u00d8\3\2\2\2\34\u00da\3\2\2\2\36\u00dd\3")
        buf.write("\2\2\2 \u00e0\3\2\2\2\"\u00e3\3\2\2\2$\u00e6\3\2\2\2&")
        buf.write("\u00ef\3\2\2\2(\u00f1\3\2\2\2*\u00fa\3\2\2\2,\u0107\3")
        buf.write("\2\2\2.\u010a\3\2\2\2\60\u0111\3\2\2\2\62\u0114\3\2\2")
        buf.write("\2\64\u011b\3\2\2\2\66\u011e\3\2\2\28\u012f\3\2\2\2:\u013c")
        buf.write("\3\2\2\2<\u0141\3\2\2\2>\u0146\3\2\2\2@\u014d\3\2\2\2")
        buf.write("B\u015d\3\2\2\2D\u0160\3\2\2\2F\u0163\3\2\2\2H\u0166\3")
        buf.write("\2\2\2J\u0169\3\2\2\2L\u0175\3\2\2\2N\u0182\3\2\2\2P\u018b")
        buf.write("\3\2\2\2R\u018d\3\2\2\2T\u019a\3\2\2\2V\u01a7\3\2\2\2")
        buf.write("X\u01b1\3\2\2\2Z\u01b3\3\2\2\2\\\u01c0\3\2\2\2^\u01cd")
        buf.write("\3\2\2\2`\u01d0\3\2\2\2b\u01d3\3\2\2\2d\u01d6\3\2\2\2")
        buf.write("f\u01e6\3\2\2\2h\u01f3\3\2\2\2j\u01f8\3\2\2\2l\u01fd\3")
        buf.write("\2\2\2n\u0203\3\2\2\2p\u0212\3\2\2\2r\u0215\3\2\2\2t\u021e")
        buf.write("\3\2\2\2v\u022b\3\2\2\2x\u0234\3\2\2\2z\u0236\3\2\2\2")
        buf.write("|\u0243\3\2\2\2~\u0250\3\2\2\2\u0080\u0253\3\2\2\2\u0082")
        buf.write("\u0269\3\2\2\2\u0084\u0276\3\2\2\2\u0086\u027b\3\2\2\2")
        buf.write("\u0088\u0280\3\2\2\2\u008a\u028c\3\2\2\2\u008c\u02a1\3")
        buf.write("\2\2\2\u008e\u02a3\3\2\2\2\u0090\u0092\5\f\7\2\u0091\u0090")
        buf.write("\3\2\2\2\u0092\u0095\3\2\2\2\u0093\u0091\3\2\2\2\u0093")
        buf.write("\u0094\3\2\2\2\u0094\u0098\3\2\2\2\u0095\u0093\3\2\2\2")
        buf.write("\u0096\u0098\5\4\3\2\u0097\u0093\3\2\2\2\u0097\u0096\3")
        buf.write("\2\2\2\u0098\u009a\3\2\2\2\u0099\u009b\5\n\6\2\u009a\u0099")
        buf.write("\3\2\2\2\u009a\u009b\3\2\2\2\u009b\u009f\3\2\2\2\u009c")
        buf.write("\u009e\7\25\2\2\u009d\u009c\3\2\2\2\u009e\u00a1\3\2\2")
        buf.write("\2\u009f\u009d\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u00a2")
        buf.write("\3\2\2\2\u00a1\u009f\3\2\2\2\u00a2\u00a3\7\2\2\3\u00a3")
        buf.write("\3\3\2\2\2\u00a4\u00a5\5\64\33\2\u00a5\u00a6\5\16\b\2")
        buf.write("\u00a6\u00a7\5\26\f\2\u00a7\u00a8\58\35\2\u00a8\u00b9")
        buf.write("\3\2\2\2\u00a9\u00aa\5F$\2\u00aa\u00ab\5\16\b\2\u00ab")
        buf.write("\u00ac\5\26\f\2\u00ac\u00ad\5L\'\2\u00ad\u00b9\3\2\2\2")
        buf.write("\u00ae\u00af\5~@\2\u00af\u00b0\5\16\b\2\u00b0\u00b1\5")
        buf.write("\26\f\2\u00b1\u00b2\5\u0082B\2\u00b2\u00b9\3\2\2\2\u00b3")
        buf.write("\u00b4\5b\62\2\u00b4\u00b5\5\16\b\2\u00b5\u00b6\5\26\f")
        buf.write("\2\u00b6\u00b7\5f\64\2\u00b7\u00b9\3\2\2\2\u00b8\u00a4")
        buf.write("\3\2\2\2\u00b8\u00a9\3\2\2\2\u00b8\u00ae\3\2\2\2\u00b8")
        buf.write("\u00b3\3\2\2\2\u00b9\5\3\2\2\2\u00ba\u00be\7\3\2\2\u00bb")
        buf.write("\u00bf\7\24\2\2\u00bc\u00bf\5\b\5\2\u00bd\u00bf\7\23\2")
        buf.write("\2\u00be\u00bb\3\2\2\2\u00be\u00bc\3\2\2\2\u00be\u00bd")
        buf.write("\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\u00be\3\2\2\2\u00c0")
        buf.write("\u00c1\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c3\7\3\2\2")
        buf.write("\u00c3\7\3\2\2\2\u00c4\u00c5\t\2\2\2\u00c5\t\3\2\2\2\u00c6")
        buf.write("\u00c7\7\4\2\2\u00c7\13\3\2\2\2\u00c8\u00c9\7\25\2\2\u00c9")
        buf.write("\r\3\2\2\2\u00ca\u00cb\7\r\2\2\u00cb\17\3\2\2\2\u00cc")
        buf.write("\u00cd\7\16\2\2\u00cd\21\3\2\2\2\u00ce\u00cf\7\17\2\2")
        buf.write("\u00cf\23\3\2\2\2\u00d0\u00d1\7\20\2\2\u00d1\25\3\2\2")
        buf.write("\2\u00d2\u00d3\7\21\2\2\u00d3\27\3\2\2\2\u00d4\u00d5\7")
        buf.write("\22\2\2\u00d5\31\3\2\2\2\u00d6\u00d9\5\22\n\2\u00d7\u00d9")
        buf.write("\5\24\13\2\u00d8\u00d6\3\2\2\2\u00d8\u00d7\3\2\2\2\u00d9")
        buf.write("\33\3\2\2\2\u00da\u00db\7\33\2\2\u00db\u00dc\5\36\20\2")
        buf.write("\u00dc\35\3\2\2\2\u00dd\u00de\5\6\4\2\u00de\u00df\7\23")
        buf.write("\2\2\u00df\37\3\2\2\2\u00e0\u00e1\7\34\2\2\u00e1\u00e2")
        buf.write("\5\"\22\2\u00e2!\3\2\2\2\u00e3\u00e4\5\6\4\2\u00e4\u00e5")
        buf.write("\7\23\2\2\u00e5#\3\2\2\2\u00e6\u00e7\7\35\2\2\u00e7\u00e8")
        buf.write("\5&\24\2\u00e8%\3\2\2\2\u00e9\u00ea\5\6\4\2\u00ea\u00ec")
        buf.write("\7\23\2\2\u00eb\u00ed\5(\25\2\u00ec\u00eb\3\2\2\2\u00ec")
        buf.write("\u00ed\3\2\2\2\u00ed\u00f0\3\2\2\2\u00ee\u00f0\5(\25\2")
        buf.write("\u00ef\u00e9\3\2\2\2\u00ef\u00ee\3\2\2\2\u00f0\'\3\2\2")
        buf.write("\2\u00f1\u00f2\5\30\r\2\u00f2\u00f3\5*\26\2\u00f3)\3\2")
        buf.write("\2\2\u00f4\u00f5\b\26\1\2\u00f5\u00f6\7\26\2\2\u00f6\u00f7")
        buf.write("\5*\26\2\u00f7\u00f8\7\27\2\2\u00f8\u00fb\3\2\2\2\u00f9")
        buf.write("\u00fb\5N(\2\u00fa\u00f4\3\2\2\2\u00fa\u00f9\3\2\2\2\u00fb")
        buf.write("\u0104\3\2\2\2\u00fc\u00fd\f\5\2\2\u00fd\u00fe\5\32\16")
        buf.write("\2\u00fe\u00ff\5*\26\6\u00ff\u0103\3\2\2\2\u0100\u0101")
        buf.write("\f\3\2\2\u0101\u0103\7\23\2\2\u0102\u00fc\3\2\2\2\u0102")
        buf.write("\u0100\3\2\2\2\u0103\u0106\3\2\2\2\u0104\u0102\3\2\2\2")
        buf.write("\u0104\u0105\3\2\2\2\u0105+\3\2\2\2\u0106\u0104\3\2\2")
        buf.write("\2\u0107\u0108\7\36\2\2\u0108\u0109\5.\30\2\u0109-\3\2")
        buf.write("\2\2\u010a\u010f\5\20\t\2\u010b\u010c\5\6\4\2\u010c\u010d")
        buf.write("\7\23\2\2\u010d\u0110\3\2\2\2\u010e\u0110\7\37\2\2\u010f")
        buf.write("\u010b\3\2\2\2\u010f\u010e\3\2\2\2\u0110/\3\2\2\2\u0111")
        buf.write("\u0112\7 \2\2\u0112\u0113\5\62\32\2\u0113\61\3\2\2\2\u0114")
        buf.write("\u0119\5\20\t\2\u0115\u0116\5\6\4\2\u0116\u0117\7\23\2")
        buf.write("\2\u0117\u011a\3\2\2\2\u0118\u011a\7!\2\2\u0119\u0115")
        buf.write("\3\2\2\2\u0119\u0118\3\2\2\2\u011a\63\3\2\2\2\u011b\u011c")
        buf.write("\7\"\2\2\u011c\u011d\5\66\34\2\u011d\65\3\2\2\2\u011e")
        buf.write("\u011f\5\30\r\2\u011f\u0120\58\35\2\u0120\67\3\2\2\2\u0121")
        buf.write("\u0122\b\35\1\2\u0122\u0123\7\26\2\2\u0123\u0124\58\35")
        buf.write("\2\u0124\u0125\7\27\2\2\u0125\u0130\3\2\2\2\u0126\u012e")
        buf.write("\5$\23\2\u0127\u012e\5B\"\2\u0128\u012e\5V,\2\u0129\u012e")
        buf.write("\5p9\2\u012a\u012e\5<\37\2\u012b\u012e\5:\36\2\u012c\u012e")
        buf.write("\5> \2\u012d\u0126\3\2\2\2\u012d\u0127\3\2\2\2\u012d\u0128")
        buf.write("\3\2\2\2\u012d\u0129\3\2\2\2\u012d\u012a\3\2\2\2\u012d")
        buf.write("\u012b\3\2\2\2\u012d\u012c\3\2\2\2\u012e\u0130\3\2\2\2")
        buf.write("\u012f\u0121\3\2\2\2\u012f\u012d\3\2\2\2\u0130\u0139\3")
        buf.write("\2\2\2\u0131\u0132\f\5\2\2\u0132\u0133\5\32\16\2\u0133")
        buf.write("\u0134\58\35\6\u0134\u0138\3\2\2\2\u0135\u0136\f\3\2\2")
        buf.write("\u0136\u0138\7\23\2\2\u0137\u0131\3\2\2\2\u0137\u0135")
        buf.write("\3\2\2\2\u0138\u013b\3\2\2\2\u0139\u0137\3\2\2\2\u0139")
        buf.write("\u013a\3\2\2\2\u013a9\3\2\2\2\u013b\u0139\3\2\2\2\u013c")
        buf.write("\u013d\7\30\2\2\u013d\u013e\7\26\2\2\u013e\u013f\5@!\2")
        buf.write("\u013f\u0140\7\27\2\2\u0140;\3\2\2\2\u0141\u0142\7\31")
        buf.write("\2\2\u0142\u0143\7\26\2\2\u0143\u0144\5@!\2\u0144\u0145")
        buf.write("\7\27\2\2\u0145=\3\2\2\2\u0146\u014b\7\32\2\2\u0147\u014c")
        buf.write("\5$\23\2\u0148\u014c\5B\"\2\u0149\u014c\5V,\2\u014a\u014c")
        buf.write("\5p9\2\u014b\u0147\3\2\2\2\u014b\u0148\3\2\2\2\u014b\u0149")
        buf.write("\3\2\2\2\u014b\u014a\3\2\2\2\u014c?\3\2\2\2\u014d\u0152")
        buf.write("\b!\1\2\u014e\u0153\5$\23\2\u014f\u0153\5B\"\2\u0150\u0153")
        buf.write("\5V,\2\u0151\u0153\5p9\2\u0152\u014e\3\2\2\2\u0152\u014f")
        buf.write("\3\2\2\2\u0152\u0150\3\2\2\2\u0152\u0151\3\2\2\2\u0153")
        buf.write("\u015a\3\2\2\2\u0154\u0155\f\4\2\2\u0155\u0156\5\24\13")
        buf.write("\2\u0156\u0157\5@!\5\u0157\u0159\3\2\2\2\u0158\u0154\3")
        buf.write("\2\2\2\u0159\u015c\3\2\2\2\u015a\u0158\3\2\2\2\u015a\u015b")
        buf.write("\3\2\2\2\u015bA\3\2\2\2\u015c\u015a\3\2\2\2\u015d\u015e")
        buf.write("\7#\2\2\u015e\u015f\5D#\2\u015fC\3\2\2\2\u0160\u0161\5")
        buf.write("\6\4\2\u0161\u0162\7\23\2\2\u0162E\3\2\2\2\u0163\u0164")
        buf.write("\7$\2\2\u0164\u0165\5J&\2\u0165G\3\2\2\2\u0166\u0167\5")
        buf.write("\20\t\2\u0167\u0168\5~@\2\u0168I\3\2\2\2\u0169\u016a\5")
        buf.write("\30\r\2\u016a\u016b\5L\'\2\u016bK\3\2\2\2\u016c\u016d")
        buf.write("\b\'\1\2\u016d\u016e\7\26\2\2\u016e\u016f\5L\'\2\u016f")
        buf.write("\u0170\7\27\2\2\u0170\u0176\3\2\2\2\u0171\u0174\5$\23")
        buf.write("\2\u0172\u0174\5V,\2\u0173\u0171\3\2\2\2\u0173\u0172\3")
        buf.write("\2\2\2\u0174\u0176\3\2\2\2\u0175\u016c\3\2\2\2\u0175\u0173")
        buf.write("\3\2\2\2\u0176\u017f\3\2\2\2\u0177\u0178\f\5\2\2\u0178")
        buf.write("\u0179\5\32\16\2\u0179\u017a\5L\'\6\u017a\u017e\3\2\2")
        buf.write("\2\u017b\u017c\f\3\2\2\u017c\u017e\7\23\2\2\u017d\u0177")
        buf.write("\3\2\2\2\u017d\u017b\3\2\2\2\u017e\u0181\3\2\2\2\u017f")
        buf.write("\u017d\3\2\2\2\u017f\u0180\3\2\2\2\u0180M\3\2\2\2\u0181")
        buf.write("\u017f\3\2\2\2\u0182\u0183\7%\2\2\u0183\u0184\5P)\2\u0184")
        buf.write("O\3\2\2\2\u0185\u0186\5\6\4\2\u0186\u0188\7\23\2\2\u0187")
        buf.write("\u0189\5R*\2\u0188\u0187\3\2\2\2\u0188\u0189\3\2\2\2\u0189")
        buf.write("\u018c\3\2\2\2\u018a\u018c\5R*\2\u018b\u0185\3\2\2\2\u018b")
        buf.write("\u018a\3\2\2\2\u018cQ\3\2\2\2\u018d\u018e\5\30\r\2\u018e")
        buf.write("\u018f\5T+\2\u018fS\3\2\2\2\u0190\u0191\b+\1\2\u0191\u0192")
        buf.write("\7\26\2\2\u0192\u0193\5T+\2\u0193\u0194\7\27\2\2\u0194")
        buf.write("\u019b\3\2\2\2\u0195\u0199\5^\60\2\u0196\u0199\5\34\17")
        buf.write("\2\u0197\u0199\5 \21\2\u0198\u0195\3\2\2\2\u0198\u0196")
        buf.write("\3\2\2\2\u0198\u0197\3\2\2\2\u0199\u019b\3\2\2\2\u019a")
        buf.write("\u0190\3\2\2\2\u019a\u0198\3\2\2\2\u019b\u01a4\3\2\2\2")
        buf.write("\u019c\u019d\f\5\2\2\u019d\u019e\5\32\16\2\u019e\u019f")
        buf.write("\5T+\6\u019f\u01a3\3\2\2\2\u01a0\u01a1\f\3\2\2\u01a1\u01a3")
        buf.write("\7\23\2\2\u01a2\u019c\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a3")
        buf.write("\u01a6\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a4\u01a5\3\2\2\2")
        buf.write("\u01a5U\3\2\2\2\u01a6\u01a4\3\2\2\2\u01a7\u01a9\7%\2\2")
        buf.write("\u01a8\u01aa\5X-\2\u01a9\u01a8\3\2\2\2\u01a9\u01aa\3\2")
        buf.write("\2\2\u01aaW\3\2\2\2\u01ab\u01ac\5\6\4\2\u01ac\u01ae\7")
        buf.write("\23\2\2\u01ad\u01af\5Z.\2\u01ae\u01ad\3\2\2\2\u01ae\u01af")
        buf.write("\3\2\2\2\u01af\u01b2\3\2\2\2\u01b0\u01b2\5Z.\2\u01b1\u01ab")
        buf.write("\3\2\2\2\u01b1\u01b0\3\2\2\2\u01b2Y\3\2\2\2\u01b3\u01b4")
        buf.write("\5\30\r\2\u01b4\u01b5\5\\/\2\u01b5[\3\2\2\2\u01b6\u01b7")
        buf.write("\b/\1\2\u01b7\u01b8\7\26\2\2\u01b8\u01b9\5\\/\2\u01b9")
        buf.write("\u01ba\7\27\2\2\u01ba\u01c1\3\2\2\2\u01bb\u01bf\5^\60")
        buf.write("\2\u01bc\u01bf\5\34\17\2\u01bd\u01bf\5$\23\2\u01be\u01bb")
        buf.write("\3\2\2\2\u01be\u01bc\3\2\2\2\u01be\u01bd\3\2\2\2\u01bf")
        buf.write("\u01c1\3\2\2\2\u01c0\u01b6\3\2\2\2\u01c0\u01be\3\2\2\2")
        buf.write("\u01c1\u01ca\3\2\2\2\u01c2\u01c3\f\5\2\2\u01c3\u01c4\5")
        buf.write("\32\16\2\u01c4\u01c5\5\\/\6\u01c5\u01c9\3\2\2\2\u01c6")
        buf.write("\u01c7\f\3\2\2\u01c7\u01c9\7\23\2\2\u01c8\u01c2\3\2\2")
        buf.write("\2\u01c8\u01c6\3\2\2\2\u01c9\u01cc\3\2\2\2\u01ca\u01c8")
        buf.write("\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb]\3\2\2\2\u01cc\u01ca")
        buf.write("\3\2\2\2\u01cd\u01ce\7&\2\2\u01ce\u01cf\5`\61\2\u01cf")
        buf.write("_\3\2\2\2\u01d0\u01d1\5\6\4\2\u01d1\u01d2\7\23\2\2\u01d2")
        buf.write("a\3\2\2\2\u01d3\u01d4\7\'\2\2\u01d4\u01d5\5d\63\2\u01d5")
        buf.write("c\3\2\2\2\u01d6\u01d7\5\30\r\2\u01d7\u01d8\5f\64\2\u01d8")
        buf.write("e\3\2\2\2\u01d9\u01da\b\64\1\2\u01da\u01db\7\26\2\2\u01db")
        buf.write("\u01dc\5f\64\2\u01dc\u01dd\7\27\2\2\u01dd\u01e7\3\2\2")
        buf.write("\2\u01de\u01e5\5$\23\2\u01df\u01e5\5^\60\2\u01e0\u01e5")
        buf.write("\5p9\2\u01e1\u01e5\5h\65\2\u01e2\u01e5\5j\66\2\u01e3\u01e5")
        buf.write("\5l\67\2\u01e4\u01de\3\2\2\2\u01e4\u01df\3\2\2\2\u01e4")
        buf.write("\u01e0\3\2\2\2\u01e4\u01e1\3\2\2\2\u01e4\u01e2\3\2\2\2")
        buf.write("\u01e4\u01e3\3\2\2\2\u01e5\u01e7\3\2\2\2\u01e6\u01d9\3")
        buf.write("\2\2\2\u01e6\u01e4\3\2\2\2\u01e7\u01f0\3\2\2\2\u01e8\u01e9")
        buf.write("\f\5\2\2\u01e9\u01ea\5\32\16\2\u01ea\u01eb\5f\64\6\u01eb")
        buf.write("\u01ef\3\2\2\2\u01ec\u01ed\f\3\2\2\u01ed\u01ef\7\23\2")
        buf.write("\2\u01ee\u01e8\3\2\2\2\u01ee\u01ec\3\2\2\2\u01ef\u01f2")
        buf.write("\3\2\2\2\u01f0\u01ee\3\2\2\2\u01f0\u01f1\3\2\2\2\u01f1")
        buf.write("g\3\2\2\2\u01f2\u01f0\3\2\2\2\u01f3\u01f4\7\30\2\2\u01f4")
        buf.write("\u01f5\7\26\2\2\u01f5\u01f6\5n8\2\u01f6\u01f7\7\27\2\2")
        buf.write("\u01f7i\3\2\2\2\u01f8\u01f9\7\31\2\2\u01f9\u01fa\7\26")
        buf.write("\2\2\u01fa\u01fb\5n8\2\u01fb\u01fc\7\27\2\2\u01fck\3\2")
        buf.write("\2\2\u01fd\u0201\7\32\2\2\u01fe\u0202\5$\23\2\u01ff\u0202")
        buf.write("\5^\60\2\u0200\u0202\5p9\2\u0201\u01fe\3\2\2\2\u0201\u01ff")
        buf.write("\3\2\2\2\u0201\u0200\3\2\2\2\u0202m\3\2\2\2\u0203\u0207")
        buf.write("\b8\1\2\u0204\u0208\5$\23\2\u0205\u0208\5^\60\2\u0206")
        buf.write("\u0208\5p9\2\u0207\u0204\3\2\2\2\u0207\u0205\3\2\2\2\u0207")
        buf.write("\u0206\3\2\2\2\u0208\u020f\3\2\2\2\u0209\u020a\f\4\2\2")
        buf.write("\u020a\u020b\5\24\13\2\u020b\u020c\5n8\5\u020c\u020e\3")
        buf.write("\2\2\2\u020d\u0209\3\2\2\2\u020e\u0211\3\2\2\2\u020f\u020d")
        buf.write("\3\2\2\2\u020f\u0210\3\2\2\2\u0210o\3\2\2\2\u0211\u020f")
        buf.write("\3\2\2\2\u0212\u0213\7(\2\2\u0213\u0214\5r:\2\u0214q\3")
        buf.write("\2\2\2\u0215\u0216\5\30\r\2\u0216\u0217\5t;\2\u0217s\3")
        buf.write("\2\2\2\u0218\u0219\b;\1\2\u0219\u021a\7\26\2\2\u021a\u021b")
        buf.write("\5t;\2\u021b\u021c\7\27\2\2\u021c\u021f\3\2\2\2\u021d")
        buf.write("\u021f\5v<\2\u021e\u0218\3\2\2\2\u021e\u021d\3\2\2\2\u021f")
        buf.write("\u0228\3\2\2\2\u0220\u0221\f\5\2\2\u0221\u0222\5\32\16")
        buf.write("\2\u0222\u0223\5t;\6\u0223\u0227\3\2\2\2\u0224\u0225\f")
        buf.write("\3\2\2\u0225\u0227\7\23\2\2\u0226\u0220\3\2\2\2\u0226")
        buf.write("\u0224\3\2\2\2\u0227\u022a\3\2\2\2\u0228\u0226\3\2\2\2")
        buf.write("\u0228\u0229\3\2\2\2\u0229u\3\2\2\2\u022a\u0228\3\2\2")
        buf.write("\2\u022b\u022c\7)\2\2\u022c\u022d\5x=\2\u022dw\3\2\2\2")
        buf.write("\u022e\u022f\5\6\4\2\u022f\u0231\7\23\2\2\u0230\u0232")
        buf.write("\5z>\2\u0231\u0230\3\2\2\2\u0231\u0232\3\2\2\2\u0232\u0235")
        buf.write("\3\2\2\2\u0233\u0235\5z>\2\u0234\u022e\3\2\2\2\u0234\u0233")
        buf.write("\3\2\2\2\u0235y\3\2\2\2\u0236\u0237\5\30\r\2\u0237\u0238")
        buf.write("\5|?\2\u0238{\3\2\2\2\u0239\u023a\b?\1\2\u023a\u023b\7")
        buf.write("\26\2\2\u023b\u023c\5|?\2\u023c\u023d\7\27\2\2\u023d\u0244")
        buf.write("\3\2\2\2\u023e\u0242\5^\60\2\u023f\u0242\5\34\17\2\u0240")
        buf.write("\u0242\5 \21\2\u0241\u023e\3\2\2\2\u0241\u023f\3\2\2\2")
        buf.write("\u0241\u0240\3\2\2\2\u0242\u0244\3\2\2\2\u0243\u0239\3")
        buf.write("\2\2\2\u0243\u0241\3\2\2\2\u0244\u024d\3\2\2\2\u0245\u0246")
        buf.write("\f\5\2\2\u0246\u0247\5\32\16\2\u0247\u0248\5|?\6\u0248")
        buf.write("\u024c\3\2\2\2\u0249\u024a\f\3\2\2\u024a\u024c\7\23\2")
        buf.write("\2\u024b\u0245\3\2\2\2\u024b\u0249\3\2\2\2\u024c\u024f")
        buf.write("\3\2\2\2\u024d\u024b\3\2\2\2\u024d\u024e\3\2\2\2\u024e")
        buf.write("}\3\2\2\2\u024f\u024d\3\2\2\2\u0250\u0251\7*\2\2\u0251")
        buf.write("\u0252\5\u0080A\2\u0252\177\3\2\2\2\u0253\u0254\5\30\r")
        buf.write("\2\u0254\u0255\5\u0082B\2\u0255\u0081\3\2\2\2\u0256\u0257")
        buf.write("\bB\1\2\u0257\u0258\7\26\2\2\u0258\u0259\5\u0082B\2\u0259")
        buf.write("\u025a\7\27\2\2\u025a\u026a\3\2\2\2\u025b\u0268\5$\23")
        buf.write("\2\u025c\u0268\5,\27\2\u025d\u0268\5\60\31\2\u025e\u0268")
        buf.write("\5\64\33\2\u025f\u0268\5F$\2\u0260\u0268\5b\62\2\u0261")
        buf.write("\u0268\5p9\2\u0262\u0268\5\u008cG\2\u0263\u0268\5\u008e")
        buf.write("H\2\u0264\u0268\5\u0084C\2\u0265\u0268\5\u0086D\2\u0266")
        buf.write("\u0268\5\u0088E\2\u0267\u025b\3\2\2\2\u0267\u025c\3\2")
        buf.write("\2\2\u0267\u025d\3\2\2\2\u0267\u025e\3\2\2\2\u0267\u025f")
        buf.write("\3\2\2\2\u0267\u0260\3\2\2\2\u0267\u0261\3\2\2\2\u0267")
        buf.write("\u0262\3\2\2\2\u0267\u0263\3\2\2\2\u0267\u0264\3\2\2\2")
        buf.write("\u0267\u0265\3\2\2\2\u0267\u0266\3\2\2\2\u0268\u026a\3")
        buf.write("\2\2\2\u0269\u0256\3\2\2\2\u0269\u0267\3\2\2\2\u026a\u0273")
        buf.write("\3\2\2\2\u026b\u026c\f\5\2\2\u026c\u026d\5\32\16\2\u026d")
        buf.write("\u026e\5\u0082B\6\u026e\u0272\3\2\2\2\u026f\u0270\f\3")
        buf.write("\2\2\u0270\u0272\7\23\2\2\u0271\u026b\3\2\2\2\u0271\u026f")
        buf.write("\3\2\2\2\u0272\u0275\3\2\2\2\u0273\u0271\3\2\2\2\u0273")
        buf.write("\u0274\3\2\2\2\u0274\u0083\3\2\2\2\u0275\u0273\3\2\2\2")
        buf.write("\u0276\u0277\7\30\2\2\u0277\u0278\7\26\2\2\u0278\u0279")
        buf.write("\5\u008aF\2\u0279\u027a\7\27\2\2\u027a\u0085\3\2\2\2\u027b")
        buf.write("\u027c\7\31\2\2\u027c\u027d\7\26\2\2\u027d\u027e\5\u008a")
        buf.write("F\2\u027e\u027f\7\27\2\2\u027f\u0087\3\2\2\2\u0280\u028a")
        buf.write("\7\32\2\2\u0281\u028b\5$\23\2\u0282\u028b\5,\27\2\u0283")
        buf.write("\u028b\5\60\31\2\u0284\u028b\5\64\33\2\u0285\u028b\5F")
        buf.write("$\2\u0286\u028b\5b\62\2\u0287\u028b\5p9\2\u0288\u028b")
        buf.write("\5\u008cG\2\u0289\u028b\5\u008eH\2\u028a\u0281\3\2\2\2")
        buf.write("\u028a\u0282\3\2\2\2\u028a\u0283\3\2\2\2\u028a\u0284\3")
        buf.write("\2\2\2\u028a\u0285\3\2\2\2\u028a\u0286\3\2\2\2\u028a\u0287")
        buf.write("\3\2\2\2\u028a\u0288\3\2\2\2\u028a\u0289\3\2\2\2\u028b")
        buf.write("\u0089\3\2\2\2\u028c\u0296\bF\1\2\u028d\u0297\5$\23\2")
        buf.write("\u028e\u0297\5,\27\2\u028f\u0297\5\60\31\2\u0290\u0297")
        buf.write("\5\64\33\2\u0291\u0297\5F$\2\u0292\u0297\5b\62\2\u0293")
        buf.write("\u0297\5p9\2\u0294\u0297\5\u008cG\2\u0295\u0297\5\u008e")
        buf.write("H\2\u0296\u028d\3\2\2\2\u0296\u028e\3\2\2\2\u0296\u028f")
        buf.write("\3\2\2\2\u0296\u0290\3\2\2\2\u0296\u0291\3\2\2\2\u0296")
        buf.write("\u0292\3\2\2\2\u0296\u0293\3\2\2\2\u0296\u0294\3\2\2\2")
        buf.write("\u0296\u0295\3\2\2\2\u0297\u029e\3\2\2\2\u0298\u0299\f")
        buf.write("\4\2\2\u0299\u029a\5\24\13\2\u029a\u029b\5\u008aF\5\u029b")
        buf.write("\u029d\3\2\2\2\u029c\u0298\3\2\2\2\u029d\u02a0\3\2\2\2")
        buf.write("\u029e\u029c\3\2\2\2\u029e\u029f\3\2\2\2\u029f\u008b\3")
        buf.write("\2\2\2\u02a0\u029e\3\2\2\2\u02a1\u02a2\7+\2\2\u02a2\u008d")
        buf.write("\3\2\2\2\u02a3\u02a4\7,\2\2\u02a4\u008f\3\2\2\2@\u0093")
        buf.write("\u0097\u009a\u009f\u00b8\u00be\u00c0\u00d8\u00ec\u00ef")
        buf.write("\u00fa\u0102\u0104\u010f\u0119\u012d\u012f\u0137\u0139")
        buf.write("\u014b\u0152\u015a\u0173\u0175\u017d\u017f\u0188\u018b")
        buf.write("\u0198\u019a\u01a2\u01a4\u01a9\u01ae\u01b1\u01be\u01c0")
        buf.write("\u01c8\u01ca\u01e4\u01e6\u01ee\u01f0\u0201\u0207\u020f")
        buf.write("\u021e\u0226\u0228\u0231\u0234\u0241\u0243\u024b\u024d")
        buf.write("\u0267\u0269\u0271\u0273\u028a\u0296\u029e")
        return buf.getvalue()


class RulepadGrammarParser ( Parser ):

    grammarFileName = "RulepadGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\"'", "'.'", "'='", "'>'", "'<'", "'''", 
                     "'&'", "'|'", "'['", "']'", "'must '", "'of '", "'and '", 
                     "'or '", "'have '", "'with '", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'('", "')'", "'one of '", "'none of '", 
                     "'no '", "'name '", "'value '", "'annotation '", "'extension '", 
                     "'Superclass'", "'implementation '", "'Interface '", 
                     "<INVALID>", "'return type '", "'constructor '", "'parameter '", 
                     "'type '", "<INVALID>", "'configuration file '", "'property '", 
                     "'class '", "'bean declaration '", "'beans file'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "SPACE", "Alphabet", "NL", "LPAREN", 
                      "RPAREN", "ONE_OF", "NONE_OF", "NO", "NAME", "VALUE", 
                      "ANNOTATION", "EXTENSION", "SUPERCLASS", "IMPLEMENTATION", 
                      "INTERFACE", "FUNCTION", "RETURN_TYPES", "CONSTRUCTOR", 
                      "PARAMETER", "TYPES", "DeclarationStatement", "ConfigurationFile", 
                      "CONFIGURATION_PROPERTIES", "CLASSES", "BEAN_DECL", 
                      "BEANS_FILE" ]

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
    RULE_parameters = 38
    RULE_parameterCondition = 39
    RULE_parameterConditionTransition = 40
    RULE_parameterExpression = 41
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
    RULE_beans = 69
    RULE_beansFile = 70

    ruleNames =  [ "inputSentence", "mustClause", "combinatorialWords", 
                   "symbols", "end", "emptyLine", "must", "of", "and_", 
                   "or_", "have", "withWord", "binary", "names", "nameCondition", 
                   "values", "valueCondition", "annotations", "annotationCondition", 
                   "annotationConditionTransition", "annotationExpression", 
                   "extensions", "extensionCondition", "implementations", 
                   "implementationCondition", "functions", "functionCondition", 
                   "functionExpression", "functionExpressionOneOf", "functionExpressionNoneOf", 
                   "functionExpressionNo", "functionExpressionAggregateContents", 
                   "returnTypes", "returnTypeCondition", "constructors", 
                   "constructorOf", "constructorCondition", "constructorExpression", 
                   "parameters", "parameterCondition", "parameterConditionTransition", 
                   "parameterExpression", "functionParameters", "functionParameterCondition", 
                   "functionParameterConditionTransition", "functionParameterExpression", 
                   "types", "typeCondition", "declarationStatements", "declarationStatementCondition", 
                   "declarationStatementExpression", "declarationStatementExpressionOneOf", 
                   "declarationStatementExpressionNoneOf", "declarationStatementExpressionNo", 
                   "declarationStatementExpressionAggregateContents", "configurationFiles", 
                   "configurationFileCondition", "configurationFileExpression", 
                   "configurationProperties", "configurationPropertyCondition", 
                   "configurationPropertyConditionTransition", "configurationPropertyExpression", 
                   "classes", "classCondition", "classExpression", "classExpressionOneOf", 
                   "classExpressionNoneOf", "classExpressionNo", "classExpressionAggregateContents", 
                   "beans", "beansFile" ]

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
    ONE_OF=22
    NONE_OF=23
    NO=24
    NAME=25
    VALUE=26
    ANNOTATION=27
    EXTENSION=28
    SUPERCLASS=29
    IMPLEMENTATION=30
    INTERFACE=31
    FUNCTION=32
    RETURN_TYPES=33
    CONSTRUCTOR=34
    PARAMETER=35
    TYPES=36
    DeclarationStatement=37
    ConfigurationFile=38
    CONFIGURATION_PROPERTIES=39
    CLASSES=40
    BEAN_DECL=41
    BEANS_FILE=42

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
            self.state = 149
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.EOF, RulepadGrammarParser.T__1, RulepadGrammarParser.NL]:
                self.state = 145
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 142
                        self.emptyLine() 
                    self.state = 147
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

                pass
            elif token in [RulepadGrammarParser.FUNCTION, RulepadGrammarParser.CONSTRUCTOR, RulepadGrammarParser.DeclarationStatement, RulepadGrammarParser.CLASSES]:
                self.state = 148
                self.mustClause()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RulepadGrammarParser.T__1:
                self.state = 151
                self.end()


            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RulepadGrammarParser.NL:
                self.state = 154
                self.match(RulepadGrammarParser.NL)
                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 160
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
            self.state = 182
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.FUNCTION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.functions()
                self.state = 163
                self.must()
                self.state = 164
                self.have()
                self.state = 165
                self.functionExpression(0)
                pass
            elif token in [RulepadGrammarParser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 167
                self.constructors()
                self.state = 168
                self.must()
                self.state = 169
                self.have()
                self.state = 170
                self.constructorExpression(0)
                pass
            elif token in [RulepadGrammarParser.CLASSES]:
                self.enterOuterAlt(localctx, 3)
                self.state = 172
                self.classes()
                self.state = 173
                self.must()
                self.state = 174
                self.have()
                self.state = 175
                self.classExpression(0)
                pass
            elif token in [RulepadGrammarParser.DeclarationStatement]:
                self.enterOuterAlt(localctx, 4)
                self.state = 177
                self.declarationStatements()
                self.state = 178
                self.must()
                self.state = 179
                self.have()
                self.state = 180
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
            self.state = 184
            self.match(RulepadGrammarParser.T__0)
            self.state = 188 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 188
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.Alphabet]:
                    self.state = 185
                    self.match(RulepadGrammarParser.Alphabet)
                    pass
                elif token in [RulepadGrammarParser.T__1, RulepadGrammarParser.T__2, RulepadGrammarParser.T__3, RulepadGrammarParser.T__4, RulepadGrammarParser.T__5, RulepadGrammarParser.T__6, RulepadGrammarParser.T__7, RulepadGrammarParser.T__8, RulepadGrammarParser.T__9, RulepadGrammarParser.LPAREN, RulepadGrammarParser.RPAREN]:
                    self.state = 186
                    self.symbols()
                    pass
                elif token in [RulepadGrammarParser.SPACE]:
                    self.state = 187
                    self.match(RulepadGrammarParser.SPACE)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 190 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RulepadGrammarParser.T__1) | (1 << RulepadGrammarParser.T__2) | (1 << RulepadGrammarParser.T__3) | (1 << RulepadGrammarParser.T__4) | (1 << RulepadGrammarParser.T__5) | (1 << RulepadGrammarParser.T__6) | (1 << RulepadGrammarParser.T__7) | (1 << RulepadGrammarParser.T__8) | (1 << RulepadGrammarParser.T__9) | (1 << RulepadGrammarParser.SPACE) | (1 << RulepadGrammarParser.Alphabet) | (1 << RulepadGrammarParser.LPAREN) | (1 << RulepadGrammarParser.RPAREN))) != 0)):
                    break

            self.state = 192
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
            self.state = 194
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
            self.state = 196
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
            self.state = 198
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
            self.state = 200
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
            self.state = 202
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
            self.state = 204
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
            self.state = 206
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
            self.state = 208
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
            self.state = 210
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
            self.state = 214
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.T__12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self.and_()
                pass
            elif token in [RulepadGrammarParser.T__13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 213
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
            self.state = 216
            self.match(RulepadGrammarParser.NAME)
            self.state = 217
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
            self.state = 219
            self.combinatorialWords()
            self.state = 220
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
            self.state = 222
            self.match(RulepadGrammarParser.VALUE)
            self.state = 223
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
            self.state = 225
            self.combinatorialWords()
            self.state = 226
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
            self.state = 228
            self.match(RulepadGrammarParser.ANNOTATION)
            self.state = 229
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
            self.state = 237
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.combinatorialWords()
                self.state = 232
                self.match(RulepadGrammarParser.SPACE)
                self.state = 234
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 233
                    self.annotationConditionTransition()


                pass
            elif token in [RulepadGrammarParser.T__15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
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
            self.state = 239
            self.withWord()
            self.state = 240
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
            self.state = 248
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 243
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 244
                self.annotationExpression(0)
                self.state = 245
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.PARAMETER]:
                self.state = 247
                self.parameters()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 258
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 256
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.AnnotationExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_annotationExpression)
                        self.state = 250
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 251
                        localctx.op = self.binary()
                        self.state = 252
                        localctx.right = self.annotationExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.AnnotationExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_annotationExpression)
                        self.state = 254
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 255
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 260
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
            self.state = 261
            self.match(RulepadGrammarParser.EXTENSION)
            self.state = 262
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
            self.state = 264
            self.of()
            self.state = 269
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.T__0]:
                self.state = 265
                self.combinatorialWords()
                self.state = 266
                self.match(RulepadGrammarParser.SPACE)
                pass
            elif token in [RulepadGrammarParser.SUPERCLASS]:
                self.state = 268
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
            self.state = 271
            self.match(RulepadGrammarParser.IMPLEMENTATION)
            self.state = 272
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
            self.state = 274
            self.of()
            self.state = 279
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.T__0]:
                self.state = 275
                self.combinatorialWords()
                self.state = 276
                self.match(RulepadGrammarParser.SPACE)
                pass
            elif token in [RulepadGrammarParser.INTERFACE]:
                self.state = 278
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
            self.state = 281
            self.match(RulepadGrammarParser.FUNCTION)
            self.state = 282
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
            self.state = 284
            self.withWord()
            self.state = 285
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
            self.state = 301
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 288
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 289
                self.functionExpression(0)
                self.state = 290
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.ONE_OF, RulepadGrammarParser.NONE_OF, RulepadGrammarParser.NO, RulepadGrammarParser.ANNOTATION, RulepadGrammarParser.RETURN_TYPES, RulepadGrammarParser.PARAMETER, RulepadGrammarParser.ConfigurationFile]:
                self.state = 299
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.ANNOTATION]:
                    self.state = 292
                    self.annotations()
                    pass
                elif token in [RulepadGrammarParser.RETURN_TYPES]:
                    self.state = 293
                    self.returnTypes()
                    pass
                elif token in [RulepadGrammarParser.PARAMETER]:
                    self.state = 294
                    self.functionParameters()
                    pass
                elif token in [RulepadGrammarParser.ConfigurationFile]:
                    self.state = 295
                    self.configurationFiles()
                    pass
                elif token in [RulepadGrammarParser.NONE_OF]:
                    self.state = 296
                    self.functionExpressionNoneOf()
                    pass
                elif token in [RulepadGrammarParser.ONE_OF]:
                    self.state = 297
                    self.functionExpressionOneOf()
                    pass
                elif token in [RulepadGrammarParser.NO]:
                    self.state = 298
                    self.functionExpressionNo()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 311
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 309
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.FunctionExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_functionExpression)
                        self.state = 303
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 304
                        localctx.op = self.binary()
                        self.state = 305
                        localctx.right = self.functionExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.FunctionExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_functionExpression)
                        self.state = 307
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 308
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 313
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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
            self.state = 314
            self.match(RulepadGrammarParser.ONE_OF)
            self.state = 315
            self.match(RulepadGrammarParser.LPAREN)
            self.state = 316
            self.functionExpressionAggregateContents(0)
            self.state = 317
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
            self.state = 319
            self.match(RulepadGrammarParser.NONE_OF)
            self.state = 320
            self.match(RulepadGrammarParser.LPAREN)
            self.state = 321
            self.functionExpressionAggregateContents(0)
            self.state = 322
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
            self.state = 324
            self.match(RulepadGrammarParser.NO)
            self.state = 329
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.ANNOTATION]:
                self.state = 325
                self.annotations()
                pass
            elif token in [RulepadGrammarParser.RETURN_TYPES]:
                self.state = 326
                self.returnTypes()
                pass
            elif token in [RulepadGrammarParser.PARAMETER]:
                self.state = 327
                self.functionParameters()
                pass
            elif token in [RulepadGrammarParser.ConfigurationFile]:
                self.state = 328
                self.configurationFiles()
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
            self.state = 336
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
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 344
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = RulepadGrammarParser.FunctionExpressionAggregateContentsContext(self, _parentctx, _parentState)
                    localctx.left = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_functionExpressionAggregateContents)
                    self.state = 338
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 339
                    localctx.op = self.or_()
                    self.state = 340
                    localctx.right = self.functionExpressionAggregateContents(3) 
                self.state = 346
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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
            self.state = 347
            self.match(RulepadGrammarParser.RETURN_TYPES)
            self.state = 348
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
            self.state = 350
            self.combinatorialWords()
            self.state = 351
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
            self.state = 353
            self.match(RulepadGrammarParser.CONSTRUCTOR)
            self.state = 354
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
            self.state = 356
            self.of()
            self.state = 357
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
            self.state = 359
            self.withWord()
            self.state = 360
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
            self.state = 371
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 363
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 364
                self.constructorExpression(0)
                self.state = 365
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.ANNOTATION, RulepadGrammarParser.PARAMETER]:
                self.state = 369
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.ANNOTATION]:
                    self.state = 367
                    self.annotations()
                    pass
                elif token in [RulepadGrammarParser.PARAMETER]:
                    self.state = 368
                    self.functionParameters()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 381
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 379
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.ConstructorExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_constructorExpression)
                        self.state = 373
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 374
                        localctx.op = self.binary()
                        self.state = 375
                        localctx.right = self.constructorExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.ConstructorExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_constructorExpression)
                        self.state = 377
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 378
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 383
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

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
            self.state = 384
            self.match(RulepadGrammarParser.PARAMETER)
            self.state = 385
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
        self.enterRule(localctx, 78, self.RULE_parameterCondition)
        try:
            self.state = 393
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 387
                self.combinatorialWords()
                self.state = 388
                self.match(RulepadGrammarParser.SPACE)
                self.state = 390
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                if la_ == 1:
                    self.state = 389
                    self.parameterConditionTransition()


                pass
            elif token in [RulepadGrammarParser.T__15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 392
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
        self.enterRule(localctx, 80, self.RULE_parameterConditionTransition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self.withWord()
            self.state = 396
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
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_parameterExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 399
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 400
                self.parameterExpression(0)
                self.state = 401
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.NAME, RulepadGrammarParser.VALUE, RulepadGrammarParser.TYPES]:
                self.state = 406
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.TYPES]:
                    self.state = 403
                    self.types()
                    pass
                elif token in [RulepadGrammarParser.NAME]:
                    self.state = 404
                    self.names()
                    pass
                elif token in [RulepadGrammarParser.VALUE]:
                    self.state = 405
                    self.values()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 418
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 416
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.ParameterExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_parameterExpression)
                        self.state = 410
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 411
                        localctx.op = self.binary()
                        self.state = 412
                        localctx.right = self.parameterExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.ParameterExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_parameterExpression)
                        self.state = 414
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 415
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 420
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

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
            self.state = 421
            self.match(RulepadGrammarParser.PARAMETER)
            self.state = 423
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 422
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
            self.state = 431
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 425
                self.combinatorialWords()
                self.state = 426
                self.match(RulepadGrammarParser.SPACE)
                self.state = 428
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
                if la_ == 1:
                    self.state = 427
                    self.functionParameterConditionTransition()


                pass
            elif token in [RulepadGrammarParser.T__15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 430
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
            self.state = 433
            self.withWord()
            self.state = 434
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
            self.state = 446
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 437
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 438
                self.functionParameterExpression(0)
                self.state = 439
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.NAME, RulepadGrammarParser.ANNOTATION, RulepadGrammarParser.TYPES]:
                self.state = 444
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.TYPES]:
                    self.state = 441
                    self.types()
                    pass
                elif token in [RulepadGrammarParser.NAME]:
                    self.state = 442
                    self.names()
                    pass
                elif token in [RulepadGrammarParser.ANNOTATION]:
                    self.state = 443
                    self.annotations()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 456
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 454
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.FunctionParameterExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_functionParameterExpression)
                        self.state = 448
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 449
                        localctx.op = self.binary()
                        self.state = 450
                        localctx.right = self.functionParameterExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.FunctionParameterExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_functionParameterExpression)
                        self.state = 452
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 453
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 458
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

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
            self.state = 459
            self.match(RulepadGrammarParser.TYPES)
            self.state = 460
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
            self.state = 462
            self.combinatorialWords()
            self.state = 463
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
            self.state = 465
            self.match(RulepadGrammarParser.DeclarationStatement)
            self.state = 466
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
            self.state = 468
            self.withWord()
            self.state = 469
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
            self.state = 484
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 472
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 473
                self.declarationStatementExpression(0)
                self.state = 474
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.ONE_OF, RulepadGrammarParser.NONE_OF, RulepadGrammarParser.NO, RulepadGrammarParser.ANNOTATION, RulepadGrammarParser.TYPES, RulepadGrammarParser.ConfigurationFile]:
                self.state = 482
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.ANNOTATION]:
                    self.state = 476
                    self.annotations()
                    pass
                elif token in [RulepadGrammarParser.TYPES]:
                    self.state = 477
                    self.types()
                    pass
                elif token in [RulepadGrammarParser.ConfigurationFile]:
                    self.state = 478
                    self.configurationFiles()
                    pass
                elif token in [RulepadGrammarParser.ONE_OF]:
                    self.state = 479
                    self.declarationStatementExpressionOneOf()
                    pass
                elif token in [RulepadGrammarParser.NONE_OF]:
                    self.state = 480
                    self.declarationStatementExpressionNoneOf()
                    pass
                elif token in [RulepadGrammarParser.NO]:
                    self.state = 481
                    self.declarationStatementExpressionNo()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 494
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 492
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.DeclarationStatementExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_declarationStatementExpression)
                        self.state = 486
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 487
                        localctx.op = self.binary()
                        self.state = 488
                        localctx.right = self.declarationStatementExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.DeclarationStatementExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_declarationStatementExpression)
                        self.state = 490
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 491
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 496
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

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
            self.state = 497
            self.match(RulepadGrammarParser.ONE_OF)
            self.state = 498
            self.match(RulepadGrammarParser.LPAREN)
            self.state = 499
            self.declarationStatementExpressionAggregateContents(0)
            self.state = 500
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
            self.state = 502
            self.match(RulepadGrammarParser.NONE_OF)
            self.state = 503
            self.match(RulepadGrammarParser.LPAREN)
            self.state = 504
            self.declarationStatementExpressionAggregateContents(0)
            self.state = 505
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
            self.state = 507
            self.match(RulepadGrammarParser.NO)
            self.state = 511
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.ANNOTATION]:
                self.state = 508
                self.annotations()
                pass
            elif token in [RulepadGrammarParser.TYPES]:
                self.state = 509
                self.types()
                pass
            elif token in [RulepadGrammarParser.ConfigurationFile]:
                self.state = 510
                self.configurationFiles()
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
            self.state = 517
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.ANNOTATION]:
                self.state = 514
                self.annotations()
                pass
            elif token in [RulepadGrammarParser.TYPES]:
                self.state = 515
                self.types()
                pass
            elif token in [RulepadGrammarParser.ConfigurationFile]:
                self.state = 516
                self.configurationFiles()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 525
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = RulepadGrammarParser.DeclarationStatementExpressionAggregateContentsContext(self, _parentctx, _parentState)
                    localctx.left = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_declarationStatementExpressionAggregateContents)
                    self.state = 519
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 520
                    localctx.op = self.or_()
                    self.state = 521
                    localctx.right = self.declarationStatementExpressionAggregateContents(3) 
                self.state = 527
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

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
            self.state = 528
            self.match(RulepadGrammarParser.ConfigurationFile)
            self.state = 529
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
            self.state = 531
            self.withWord()
            self.state = 532
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
            self.state = 540
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 535
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 536
                self.configurationFileExpression(0)
                self.state = 537
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.CONFIGURATION_PROPERTIES]:
                self.state = 539
                self.configurationProperties()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 550
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,48,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 548
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.ConfigurationFileExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_configurationFileExpression)
                        self.state = 542
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 543
                        localctx.op = self.binary()
                        self.state = 544
                        localctx.right = self.configurationFileExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.ConfigurationFileExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_configurationFileExpression)
                        self.state = 546
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 547
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 552
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,48,self._ctx)

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
            self.state = 553
            self.match(RulepadGrammarParser.CONFIGURATION_PROPERTIES)
            self.state = 554
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
            self.state = 562
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 556
                self.combinatorialWords()
                self.state = 557
                self.match(RulepadGrammarParser.SPACE)
                self.state = 559
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
                if la_ == 1:
                    self.state = 558
                    self.configurationPropertyConditionTransition()


                pass
            elif token in [RulepadGrammarParser.T__15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 561
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
            self.state = 564
            self.withWord()
            self.state = 565
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
            self.state = 577
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 568
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 569
                self.configurationPropertyExpression(0)
                self.state = 570
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.NAME, RulepadGrammarParser.VALUE, RulepadGrammarParser.TYPES]:
                self.state = 575
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.TYPES]:
                    self.state = 572
                    self.types()
                    pass
                elif token in [RulepadGrammarParser.NAME]:
                    self.state = 573
                    self.names()
                    pass
                elif token in [RulepadGrammarParser.VALUE]:
                    self.state = 574
                    self.values()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 587
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,54,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 585
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.ConfigurationPropertyExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_configurationPropertyExpression)
                        self.state = 579
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 580
                        localctx.op = self.binary()
                        self.state = 581
                        localctx.right = self.configurationPropertyExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.ConfigurationPropertyExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_configurationPropertyExpression)
                        self.state = 583
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 584
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 589
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,54,self._ctx)

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
            self.state = 590
            self.match(RulepadGrammarParser.CLASSES)
            self.state = 591
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
            self.state = 593
            self.withWord()
            self.state = 594
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
            self.state = 615
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 597
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 598
                self.classExpression(0)
                self.state = 599
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.ONE_OF, RulepadGrammarParser.NONE_OF, RulepadGrammarParser.NO, RulepadGrammarParser.ANNOTATION, RulepadGrammarParser.EXTENSION, RulepadGrammarParser.IMPLEMENTATION, RulepadGrammarParser.FUNCTION, RulepadGrammarParser.CONSTRUCTOR, RulepadGrammarParser.DeclarationStatement, RulepadGrammarParser.ConfigurationFile, RulepadGrammarParser.BEAN_DECL, RulepadGrammarParser.BEANS_FILE]:
                self.state = 613
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.ANNOTATION]:
                    self.state = 601
                    self.annotations()
                    pass
                elif token in [RulepadGrammarParser.EXTENSION]:
                    self.state = 602
                    self.extensions()
                    pass
                elif token in [RulepadGrammarParser.IMPLEMENTATION]:
                    self.state = 603
                    self.implementations()
                    pass
                elif token in [RulepadGrammarParser.FUNCTION]:
                    self.state = 604
                    self.functions()
                    pass
                elif token in [RulepadGrammarParser.CONSTRUCTOR]:
                    self.state = 605
                    self.constructors()
                    pass
                elif token in [RulepadGrammarParser.DeclarationStatement]:
                    self.state = 606
                    self.declarationStatements()
                    pass
                elif token in [RulepadGrammarParser.ConfigurationFile]:
                    self.state = 607
                    self.configurationFiles()
                    pass
                elif token in [RulepadGrammarParser.BEAN_DECL]:
                    self.state = 608
                    self.beans()
                    pass
                elif token in [RulepadGrammarParser.BEANS_FILE]:
                    self.state = 609
                    self.beansFile()
                    pass
                elif token in [RulepadGrammarParser.ONE_OF]:
                    self.state = 610
                    self.classExpressionOneOf()
                    pass
                elif token in [RulepadGrammarParser.NONE_OF]:
                    self.state = 611
                    self.classExpressionNoneOf()
                    pass
                elif token in [RulepadGrammarParser.NO]:
                    self.state = 612
                    self.classExpressionNo()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 625
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,58,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 623
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.ClassExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_classExpression)
                        self.state = 617
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 618
                        localctx.op = self.binary()
                        self.state = 619
                        localctx.right = self.classExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.ClassExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_classExpression)
                        self.state = 621
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 622
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 627
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,58,self._ctx)

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
            self.state = 628
            self.match(RulepadGrammarParser.ONE_OF)
            self.state = 629
            self.match(RulepadGrammarParser.LPAREN)
            self.state = 630
            self.classExpressionAggregateContents(0)
            self.state = 631
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
            self.state = 633
            self.match(RulepadGrammarParser.NONE_OF)
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
            self.state = 638
            self.match(RulepadGrammarParser.NO)
            self.state = 648
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.ANNOTATION]:
                self.state = 639
                self.annotations()
                pass
            elif token in [RulepadGrammarParser.EXTENSION]:
                self.state = 640
                self.extensions()
                pass
            elif token in [RulepadGrammarParser.IMPLEMENTATION]:
                self.state = 641
                self.implementations()
                pass
            elif token in [RulepadGrammarParser.FUNCTION]:
                self.state = 642
                self.functions()
                pass
            elif token in [RulepadGrammarParser.CONSTRUCTOR]:
                self.state = 643
                self.constructors()
                pass
            elif token in [RulepadGrammarParser.DeclarationStatement]:
                self.state = 644
                self.declarationStatements()
                pass
            elif token in [RulepadGrammarParser.ConfigurationFile]:
                self.state = 645
                self.configurationFiles()
                pass
            elif token in [RulepadGrammarParser.BEAN_DECL]:
                self.state = 646
                self.beans()
                pass
            elif token in [RulepadGrammarParser.BEANS_FILE]:
                self.state = 647
                self.beansFile()
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
            self.state = 660
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.ANNOTATION]:
                self.state = 651
                self.annotations()
                pass
            elif token in [RulepadGrammarParser.EXTENSION]:
                self.state = 652
                self.extensions()
                pass
            elif token in [RulepadGrammarParser.IMPLEMENTATION]:
                self.state = 653
                self.implementations()
                pass
            elif token in [RulepadGrammarParser.FUNCTION]:
                self.state = 654
                self.functions()
                pass
            elif token in [RulepadGrammarParser.CONSTRUCTOR]:
                self.state = 655
                self.constructors()
                pass
            elif token in [RulepadGrammarParser.DeclarationStatement]:
                self.state = 656
                self.declarationStatements()
                pass
            elif token in [RulepadGrammarParser.ConfigurationFile]:
                self.state = 657
                self.configurationFiles()
                pass
            elif token in [RulepadGrammarParser.BEAN_DECL]:
                self.state = 658
                self.beans()
                pass
            elif token in [RulepadGrammarParser.BEANS_FILE]:
                self.state = 659
                self.beansFile()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 668
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,61,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = RulepadGrammarParser.ClassExpressionAggregateContentsContext(self, _parentctx, _parentState)
                    localctx.left = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_classExpressionAggregateContents)
                    self.state = 662
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 663
                    localctx.op = self.or_()
                    self.state = 664
                    localctx.right = self.classExpressionAggregateContents(3) 
                self.state = 670
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,61,self._ctx)

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
        self.enterRule(localctx, 138, self.RULE_beans)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 671
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
        self.enterRule(localctx, 140, self.RULE_beansFile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 673
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
        self._predicates[41] = self.parameterExpression_sempred
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
         

    def parameterExpression_sempred(self, localctx:ParameterExpressionContext, predIndex:int):
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
         




