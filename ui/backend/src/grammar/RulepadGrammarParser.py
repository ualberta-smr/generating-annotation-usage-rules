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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3+")
        buf.write("\u02a7\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\3\2\7\2\u0094\n\2\f\2")
        buf.write("\16\2\u0097\13\2\3\2\5\2\u009a\n\2\3\2\5\2\u009d\n\2\3")
        buf.write("\2\7\2\u00a0\n\2\f\2\16\2\u00a3\13\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\5\3\u00bb\n\3\3\4\3\4\3\4\3\4\6\4\u00c1")
        buf.write("\n\4\r\4\16\4\u00c2\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3")
        buf.write("\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16")
        buf.write("\3\16\5\16\u00db\n\16\3\17\3\17\3\17\3\20\3\20\3\20\3")
        buf.write("\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\5\24\u00ef\n\24\3\24\5\24\u00f2\n\24\3\25\3\25\3")
        buf.write("\25\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u00fd\n\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\7\26\u0105\n\26\f\26\16\26\u0108")
        buf.write("\13\26\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\31\3\31\3")
        buf.write("\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\5\35\u012a\n\35\5\35\u012c\n\35\3\35\3\35\3\35\3")
        buf.write("\35\3\35\3\35\7\35\u0134\n\35\f\35\16\35\u0137\13\35\3")
        buf.write("\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3 \3")
        buf.write(" \3 \3 \3 \5 \u0148\n \3!\3!\3!\3!\3!\5!\u014f\n!\3!\3")
        buf.write("!\3!\3!\7!\u0155\n!\f!\16!\u0158\13!\3\"\3\"\3\"\3#\3")
        buf.write("#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("\'\3\'\5\'\u0170\n\'\5\'\u0172\n\'\3\'\3\'\3\'\3\'\3\'")
        buf.write("\3\'\7\'\u017a\n\'\f\'\16\'\u017d\13\'\3(\3(\3(\3)\3)")
        buf.write("\3)\5)\u0185\n)\3)\5)\u0188\n)\3*\3*\3*\3+\3+\3+\3+\3")
        buf.write("+\3+\3+\3+\5+\u0195\n+\5+\u0197\n+\3+\3+\3+\3+\3+\3+\7")
        buf.write("+\u019f\n+\f+\16+\u01a2\13+\3,\3,\5,\u01a6\n,\3-\3-\3")
        buf.write("-\5-\u01ab\n-\3-\5-\u01ae\n-\3.\3.\3.\3/\3/\3/\3/\3/\3")
        buf.write("/\3/\3/\5/\u01bb\n/\5/\u01bd\n/\3/\3/\3/\3/\3/\3/\7/\u01c5")
        buf.write("\n/\f/\16/\u01c8\13/\3\60\3\60\3\60\3\61\3\61\3\61\3\62")
        buf.write("\3\62\3\62\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\5\64\u01e1\n\64\5\64\u01e3\n")
        buf.write("\64\3\64\3\64\3\64\3\64\3\64\3\64\7\64\u01eb\n\64\f\64")
        buf.write("\16\64\u01ee\13\64\3\65\3\65\3\65\3\65\3\65\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\67\3\67\3\67\3\67\5\67\u01fe\n\67\3")
        buf.write("8\38\38\38\58\u0204\n8\38\38\38\38\78\u020a\n8\f8\168")
        buf.write("\u020d\138\39\39\39\3:\3:\3:\3;\3;\3;\3;\3;\3;\5;\u021b")
        buf.write("\n;\3;\3;\3;\3;\3;\3;\7;\u0223\n;\f;\16;\u0226\13;\3<")
        buf.write("\3<\3<\3=\3=\3=\5=\u022e\n=\3=\5=\u0231\n=\3>\3>\3>\3")
        buf.write("?\3?\3?\3?\3?\3?\3?\3?\5?\u023e\n?\5?\u0240\n?\3?\3?\3")
        buf.write("?\3?\3?\3?\7?\u0248\n?\f?\16?\u024b\13?\3@\3@\3@\3A\3")
        buf.write("A\3A\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3")
        buf.write("B\3B\5B\u0265\nB\5B\u0267\nB\3B\3B\3B\3B\3B\3B\7B\u026f")
        buf.write("\nB\fB\16B\u0272\13B\3C\3C\3C\3C\3C\3D\3D\3D\3D\3D\3E")
        buf.write("\3E\3E\3E\3E\3E\3E\3E\3E\3E\5E\u0288\nE\3F\3F\3F\3F\3")
        buf.write("F\3F\3F\3F\3F\3F\5F\u0294\nF\3F\3F\3F\3F\7F\u029a\nF\f")
        buf.write("F\16F\u029d\13F\3G\3G\3G\3G\3H\3H\3I\3I\3I\2\16*8@LT\\")
        buf.write("fnt|\u0082\u008aJ\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjln")
        buf.write("prtvxz|~\u0080\u0082\u0084\u0086\u0088\u008a\u008c\u008e")
        buf.write("\u0090\2\3\4\2\4\f\26\27\2\u02c8\2\u0099\3\2\2\2\4\u00ba")
        buf.write("\3\2\2\2\6\u00bc\3\2\2\2\b\u00c6\3\2\2\2\n\u00c8\3\2\2")
        buf.write("\2\f\u00ca\3\2\2\2\16\u00cc\3\2\2\2\20\u00ce\3\2\2\2\22")
        buf.write("\u00d0\3\2\2\2\24\u00d2\3\2\2\2\26\u00d4\3\2\2\2\30\u00d6")
        buf.write("\3\2\2\2\32\u00da\3\2\2\2\34\u00dc\3\2\2\2\36\u00df\3")
        buf.write("\2\2\2 \u00e2\3\2\2\2\"\u00e5\3\2\2\2$\u00e8\3\2\2\2&")
        buf.write("\u00f1\3\2\2\2(\u00f3\3\2\2\2*\u00fc\3\2\2\2,\u0109\3")
        buf.write("\2\2\2.\u010c\3\2\2\2\60\u0110\3\2\2\2\62\u0113\3\2\2")
        buf.write("\2\64\u0117\3\2\2\2\66\u011a\3\2\2\28\u012b\3\2\2\2:\u0138")
        buf.write("\3\2\2\2<\u013d\3\2\2\2>\u0142\3\2\2\2@\u0149\3\2\2\2")
        buf.write("B\u0159\3\2\2\2D\u015c\3\2\2\2F\u015f\3\2\2\2H\u0162\3")
        buf.write("\2\2\2J\u0165\3\2\2\2L\u0171\3\2\2\2N\u017e\3\2\2\2P\u0187")
        buf.write("\3\2\2\2R\u0189\3\2\2\2T\u0196\3\2\2\2V\u01a3\3\2\2\2")
        buf.write("X\u01ad\3\2\2\2Z\u01af\3\2\2\2\\\u01bc\3\2\2\2^\u01c9")
        buf.write("\3\2\2\2`\u01cc\3\2\2\2b\u01cf\3\2\2\2d\u01d2\3\2\2\2")
        buf.write("f\u01e2\3\2\2\2h\u01ef\3\2\2\2j\u01f4\3\2\2\2l\u01f9\3")
        buf.write("\2\2\2n\u01ff\3\2\2\2p\u020e\3\2\2\2r\u0211\3\2\2\2t\u021a")
        buf.write("\3\2\2\2v\u0227\3\2\2\2x\u0230\3\2\2\2z\u0232\3\2\2\2")
        buf.write("|\u023f\3\2\2\2~\u024c\3\2\2\2\u0080\u024f\3\2\2\2\u0082")
        buf.write("\u0266\3\2\2\2\u0084\u0273\3\2\2\2\u0086\u0278\3\2\2\2")
        buf.write("\u0088\u027d\3\2\2\2\u008a\u0289\3\2\2\2\u008c\u029e\3")
        buf.write("\2\2\2\u008e\u02a2\3\2\2\2\u0090\u02a4\3\2\2\2\u0092\u0094")
        buf.write("\5\f\7\2\u0093\u0092\3\2\2\2\u0094\u0097\3\2\2\2\u0095")
        buf.write("\u0093\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u009a\3\2\2\2")
        buf.write("\u0097\u0095\3\2\2\2\u0098\u009a\5\4\3\2\u0099\u0095\3")
        buf.write("\2\2\2\u0099\u0098\3\2\2\2\u009a\u009c\3\2\2\2\u009b\u009d")
        buf.write("\5\n\6\2\u009c\u009b\3\2\2\2\u009c\u009d\3\2\2\2\u009d")
        buf.write("\u00a1\3\2\2\2\u009e\u00a0\7\25\2\2\u009f\u009e\3\2\2")
        buf.write("\2\u00a0\u00a3\3\2\2\2\u00a1\u009f\3\2\2\2\u00a1\u00a2")
        buf.write("\3\2\2\2\u00a2\u00a4\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a4")
        buf.write("\u00a5\7\2\2\3\u00a5\3\3\2\2\2\u00a6\u00a7\5\64\33\2\u00a7")
        buf.write("\u00a8\5\16\b\2\u00a8\u00a9\5\26\f\2\u00a9\u00aa\58\35")
        buf.write("\2\u00aa\u00bb\3\2\2\2\u00ab\u00ac\5F$\2\u00ac\u00ad\5")
        buf.write("\16\b\2\u00ad\u00ae\5\26\f\2\u00ae\u00af\5L\'\2\u00af")
        buf.write("\u00bb\3\2\2\2\u00b0\u00b1\5~@\2\u00b1\u00b2\5\16\b\2")
        buf.write("\u00b2\u00b3\5\26\f\2\u00b3\u00b4\5\u0082B\2\u00b4\u00bb")
        buf.write("\3\2\2\2\u00b5\u00b6\5b\62\2\u00b6\u00b7\5\16\b\2\u00b7")
        buf.write("\u00b8\5\26\f\2\u00b8\u00b9\5f\64\2\u00b9\u00bb\3\2\2")
        buf.write("\2\u00ba\u00a6\3\2\2\2\u00ba\u00ab\3\2\2\2\u00ba\u00b0")
        buf.write("\3\2\2\2\u00ba\u00b5\3\2\2\2\u00bb\5\3\2\2\2\u00bc\u00c0")
        buf.write("\7\3\2\2\u00bd\u00c1\7\24\2\2\u00be\u00c1\5\b\5\2\u00bf")
        buf.write("\u00c1\7\23\2\2\u00c0\u00bd\3\2\2\2\u00c0\u00be\3\2\2")
        buf.write("\2\u00c0\u00bf\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c0")
        buf.write("\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4")
        buf.write("\u00c5\7\3\2\2\u00c5\7\3\2\2\2\u00c6\u00c7\t\2\2\2\u00c7")
        buf.write("\t\3\2\2\2\u00c8\u00c9\7\4\2\2\u00c9\13\3\2\2\2\u00ca")
        buf.write("\u00cb\7\25\2\2\u00cb\r\3\2\2\2\u00cc\u00cd\7\r\2\2\u00cd")
        buf.write("\17\3\2\2\2\u00ce\u00cf\7\16\2\2\u00cf\21\3\2\2\2\u00d0")
        buf.write("\u00d1\7\17\2\2\u00d1\23\3\2\2\2\u00d2\u00d3\7\20\2\2")
        buf.write("\u00d3\25\3\2\2\2\u00d4\u00d5\7\21\2\2\u00d5\27\3\2\2")
        buf.write("\2\u00d6\u00d7\7\22\2\2\u00d7\31\3\2\2\2\u00d8\u00db\5")
        buf.write("\22\n\2\u00d9\u00db\5\24\13\2\u00da\u00d8\3\2\2\2\u00da")
        buf.write("\u00d9\3\2\2\2\u00db\33\3\2\2\2\u00dc\u00dd\7\33\2\2\u00dd")
        buf.write("\u00de\5\36\20\2\u00de\35\3\2\2\2\u00df\u00e0\5\6\4\2")
        buf.write("\u00e0\u00e1\7\23\2\2\u00e1\37\3\2\2\2\u00e2\u00e3\7\34")
        buf.write("\2\2\u00e3\u00e4\5\"\22\2\u00e4!\3\2\2\2\u00e5\u00e6\5")
        buf.write("\6\4\2\u00e6\u00e7\7\23\2\2\u00e7#\3\2\2\2\u00e8\u00e9")
        buf.write("\7\35\2\2\u00e9\u00ea\5&\24\2\u00ea%\3\2\2\2\u00eb\u00ec")
        buf.write("\5\6\4\2\u00ec\u00ee\7\23\2\2\u00ed\u00ef\5(\25\2\u00ee")
        buf.write("\u00ed\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00f2\3\2\2\2")
        buf.write("\u00f0\u00f2\5(\25\2\u00f1\u00eb\3\2\2\2\u00f1\u00f0\3")
        buf.write("\2\2\2\u00f2\'\3\2\2\2\u00f3\u00f4\5\30\r\2\u00f4\u00f5")
        buf.write("\5*\26\2\u00f5)\3\2\2\2\u00f6\u00f7\b\26\1\2\u00f7\u00f8")
        buf.write("\7\26\2\2\u00f8\u00f9\5*\26\2\u00f9\u00fa\7\27\2\2\u00fa")
        buf.write("\u00fd\3\2\2\2\u00fb\u00fd\5N(\2\u00fc\u00f6\3\2\2\2\u00fc")
        buf.write("\u00fb\3\2\2\2\u00fd\u0106\3\2\2\2\u00fe\u00ff\f\5\2\2")
        buf.write("\u00ff\u0100\5\32\16\2\u0100\u0101\5*\26\6\u0101\u0105")
        buf.write("\3\2\2\2\u0102\u0103\f\3\2\2\u0103\u0105\7\23\2\2\u0104")
        buf.write("\u00fe\3\2\2\2\u0104\u0102\3\2\2\2\u0105\u0108\3\2\2\2")
        buf.write("\u0106\u0104\3\2\2\2\u0106\u0107\3\2\2\2\u0107+\3\2\2")
        buf.write("\2\u0108\u0106\3\2\2\2\u0109\u010a\7\36\2\2\u010a\u010b")
        buf.write("\5.\30\2\u010b-\3\2\2\2\u010c\u010d\5\20\t\2\u010d\u010e")
        buf.write("\5\6\4\2\u010e\u010f\7\23\2\2\u010f/\3\2\2\2\u0110\u0111")
        buf.write("\7\37\2\2\u0111\u0112\5\62\32\2\u0112\61\3\2\2\2\u0113")
        buf.write("\u0114\5\20\t\2\u0114\u0115\5\6\4\2\u0115\u0116\7\23\2")
        buf.write("\2\u0116\63\3\2\2\2\u0117\u0118\7 \2\2\u0118\u0119\5\66")
        buf.write("\34\2\u0119\65\3\2\2\2\u011a\u011b\5\30\r\2\u011b\u011c")
        buf.write("\58\35\2\u011c\67\3\2\2\2\u011d\u011e\b\35\1\2\u011e\u011f")
        buf.write("\7\26\2\2\u011f\u0120\58\35\2\u0120\u0121\7\27\2\2\u0121")
        buf.write("\u012c\3\2\2\2\u0122\u012a\5$\23\2\u0123\u012a\5B\"\2")
        buf.write("\u0124\u012a\5V,\2\u0125\u012a\5p9\2\u0126\u012a\5<\37")
        buf.write("\2\u0127\u012a\5:\36\2\u0128\u012a\5> \2\u0129\u0122\3")
        buf.write("\2\2\2\u0129\u0123\3\2\2\2\u0129\u0124\3\2\2\2\u0129\u0125")
        buf.write("\3\2\2\2\u0129\u0126\3\2\2\2\u0129\u0127\3\2\2\2\u0129")
        buf.write("\u0128\3\2\2\2\u012a\u012c\3\2\2\2\u012b\u011d\3\2\2\2")
        buf.write("\u012b\u0129\3\2\2\2\u012c\u0135\3\2\2\2\u012d\u012e\f")
        buf.write("\5\2\2\u012e\u012f\5\32\16\2\u012f\u0130\58\35\6\u0130")
        buf.write("\u0134\3\2\2\2\u0131\u0132\f\3\2\2\u0132\u0134\7\23\2")
        buf.write("\2\u0133\u012d\3\2\2\2\u0133\u0131\3\2\2\2\u0134\u0137")
        buf.write("\3\2\2\2\u0135\u0133\3\2\2\2\u0135\u0136\3\2\2\2\u0136")
        buf.write("9\3\2\2\2\u0137\u0135\3\2\2\2\u0138\u0139\7\30\2\2\u0139")
        buf.write("\u013a\7\26\2\2\u013a\u013b\5@!\2\u013b\u013c\7\27\2\2")
        buf.write("\u013c;\3\2\2\2\u013d\u013e\7\31\2\2\u013e\u013f\7\26")
        buf.write("\2\2\u013f\u0140\5@!\2\u0140\u0141\7\27\2\2\u0141=\3\2")
        buf.write("\2\2\u0142\u0147\7\32\2\2\u0143\u0148\5$\23\2\u0144\u0148")
        buf.write("\5B\"\2\u0145\u0148\5V,\2\u0146\u0148\5p9\2\u0147\u0143")
        buf.write("\3\2\2\2\u0147\u0144\3\2\2\2\u0147\u0145\3\2\2\2\u0147")
        buf.write("\u0146\3\2\2\2\u0148?\3\2\2\2\u0149\u014e\b!\1\2\u014a")
        buf.write("\u014f\5$\23\2\u014b\u014f\5B\"\2\u014c\u014f\5V,\2\u014d")
        buf.write("\u014f\5p9\2\u014e\u014a\3\2\2\2\u014e\u014b\3\2\2\2\u014e")
        buf.write("\u014c\3\2\2\2\u014e\u014d\3\2\2\2\u014f\u0156\3\2\2\2")
        buf.write("\u0150\u0151\f\4\2\2\u0151\u0152\5\24\13\2\u0152\u0153")
        buf.write("\5@!\5\u0153\u0155\3\2\2\2\u0154\u0150\3\2\2\2\u0155\u0158")
        buf.write("\3\2\2\2\u0156\u0154\3\2\2\2\u0156\u0157\3\2\2\2\u0157")
        buf.write("A\3\2\2\2\u0158\u0156\3\2\2\2\u0159\u015a\7!\2\2\u015a")
        buf.write("\u015b\5D#\2\u015bC\3\2\2\2\u015c\u015d\5\6\4\2\u015d")
        buf.write("\u015e\7\23\2\2\u015eE\3\2\2\2\u015f\u0160\7\"\2\2\u0160")
        buf.write("\u0161\5J&\2\u0161G\3\2\2\2\u0162\u0163\5\20\t\2\u0163")
        buf.write("\u0164\5~@\2\u0164I\3\2\2\2\u0165\u0166\5\30\r\2\u0166")
        buf.write("\u0167\5L\'\2\u0167K\3\2\2\2\u0168\u0169\b\'\1\2\u0169")
        buf.write("\u016a\7\26\2\2\u016a\u016b\5L\'\2\u016b\u016c\7\27\2")
        buf.write("\2\u016c\u0172\3\2\2\2\u016d\u0170\5$\23\2\u016e\u0170")
        buf.write("\5V,\2\u016f\u016d\3\2\2\2\u016f\u016e\3\2\2\2\u0170\u0172")
        buf.write("\3\2\2\2\u0171\u0168\3\2\2\2\u0171\u016f\3\2\2\2\u0172")
        buf.write("\u017b\3\2\2\2\u0173\u0174\f\5\2\2\u0174\u0175\5\32\16")
        buf.write("\2\u0175\u0176\5L\'\6\u0176\u017a\3\2\2\2\u0177\u0178")
        buf.write("\f\3\2\2\u0178\u017a\7\23\2\2\u0179\u0173\3\2\2\2\u0179")
        buf.write("\u0177\3\2\2\2\u017a\u017d\3\2\2\2\u017b\u0179\3\2\2\2")
        buf.write("\u017b\u017c\3\2\2\2\u017cM\3\2\2\2\u017d\u017b\3\2\2")
        buf.write("\2\u017e\u017f\7#\2\2\u017f\u0180\5P)\2\u0180O\3\2\2\2")
        buf.write("\u0181\u0182\5\6\4\2\u0182\u0184\7\23\2\2\u0183\u0185")
        buf.write("\5R*\2\u0184\u0183\3\2\2\2\u0184\u0185\3\2\2\2\u0185\u0188")
        buf.write("\3\2\2\2\u0186\u0188\5R*\2\u0187\u0181\3\2\2\2\u0187\u0186")
        buf.write("\3\2\2\2\u0188Q\3\2\2\2\u0189\u018a\5\30\r\2\u018a\u018b")
        buf.write("\5T+\2\u018bS\3\2\2\2\u018c\u018d\b+\1\2\u018d\u018e\7")
        buf.write("\26\2\2\u018e\u018f\5T+\2\u018f\u0190\7\27\2\2\u0190\u0197")
        buf.write("\3\2\2\2\u0191\u0195\5^\60\2\u0192\u0195\5\34\17\2\u0193")
        buf.write("\u0195\5 \21\2\u0194\u0191\3\2\2\2\u0194\u0192\3\2\2\2")
        buf.write("\u0194\u0193\3\2\2\2\u0195\u0197\3\2\2\2\u0196\u018c\3")
        buf.write("\2\2\2\u0196\u0194\3\2\2\2\u0197\u01a0\3\2\2\2\u0198\u0199")
        buf.write("\f\5\2\2\u0199\u019a\5\32\16\2\u019a\u019b\5T+\6\u019b")
        buf.write("\u019f\3\2\2\2\u019c\u019d\f\3\2\2\u019d\u019f\7\23\2")
        buf.write("\2\u019e\u0198\3\2\2\2\u019e\u019c\3\2\2\2\u019f\u01a2")
        buf.write("\3\2\2\2\u01a0\u019e\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1")
        buf.write("U\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a3\u01a5\7#\2\2\u01a4")
        buf.write("\u01a6\5X-\2\u01a5\u01a4\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6")
        buf.write("W\3\2\2\2\u01a7\u01a8\5\6\4\2\u01a8\u01aa\7\23\2\2\u01a9")
        buf.write("\u01ab\5Z.\2\u01aa\u01a9\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab")
        buf.write("\u01ae\3\2\2\2\u01ac\u01ae\5Z.\2\u01ad\u01a7\3\2\2\2\u01ad")
        buf.write("\u01ac\3\2\2\2\u01aeY\3\2\2\2\u01af\u01b0\5\30\r\2\u01b0")
        buf.write("\u01b1\5\\/\2\u01b1[\3\2\2\2\u01b2\u01b3\b/\1\2\u01b3")
        buf.write("\u01b4\7\26\2\2\u01b4\u01b5\5\\/\2\u01b5\u01b6\7\27\2")
        buf.write("\2\u01b6\u01bd\3\2\2\2\u01b7\u01bb\5^\60\2\u01b8\u01bb")
        buf.write("\5\34\17\2\u01b9\u01bb\5$\23\2\u01ba\u01b7\3\2\2\2\u01ba")
        buf.write("\u01b8\3\2\2\2\u01ba\u01b9\3\2\2\2\u01bb\u01bd\3\2\2\2")
        buf.write("\u01bc\u01b2\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bd\u01c6\3")
        buf.write("\2\2\2\u01be\u01bf\f\5\2\2\u01bf\u01c0\5\32\16\2\u01c0")
        buf.write("\u01c1\5\\/\6\u01c1\u01c5\3\2\2\2\u01c2\u01c3\f\3\2\2")
        buf.write("\u01c3\u01c5\7\23\2\2\u01c4\u01be\3\2\2\2\u01c4\u01c2")
        buf.write("\3\2\2\2\u01c5\u01c8\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c6")
        buf.write("\u01c7\3\2\2\2\u01c7]\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c9")
        buf.write("\u01ca\7$\2\2\u01ca\u01cb\5`\61\2\u01cb_\3\2\2\2\u01cc")
        buf.write("\u01cd\5\6\4\2\u01cd\u01ce\7\23\2\2\u01cea\3\2\2\2\u01cf")
        buf.write("\u01d0\7%\2\2\u01d0\u01d1\5d\63\2\u01d1c\3\2\2\2\u01d2")
        buf.write("\u01d3\5\30\r\2\u01d3\u01d4\5f\64\2\u01d4e\3\2\2\2\u01d5")
        buf.write("\u01d6\b\64\1\2\u01d6\u01d7\7\26\2\2\u01d7\u01d8\5f\64")
        buf.write("\2\u01d8\u01d9\7\27\2\2\u01d9\u01e3\3\2\2\2\u01da\u01e1")
        buf.write("\5$\23\2\u01db\u01e1\5^\60\2\u01dc\u01e1\5p9\2\u01dd\u01e1")
        buf.write("\5h\65\2\u01de\u01e1\5j\66\2\u01df\u01e1\5l\67\2\u01e0")
        buf.write("\u01da\3\2\2\2\u01e0\u01db\3\2\2\2\u01e0\u01dc\3\2\2\2")
        buf.write("\u01e0\u01dd\3\2\2\2\u01e0\u01de\3\2\2\2\u01e0\u01df\3")
        buf.write("\2\2\2\u01e1\u01e3\3\2\2\2\u01e2\u01d5\3\2\2\2\u01e2\u01e0")
        buf.write("\3\2\2\2\u01e3\u01ec\3\2\2\2\u01e4\u01e5\f\5\2\2\u01e5")
        buf.write("\u01e6\5\32\16\2\u01e6\u01e7\5f\64\6\u01e7\u01eb\3\2\2")
        buf.write("\2\u01e8\u01e9\f\3\2\2\u01e9\u01eb\7\23\2\2\u01ea\u01e4")
        buf.write("\3\2\2\2\u01ea\u01e8\3\2\2\2\u01eb\u01ee\3\2\2\2\u01ec")
        buf.write("\u01ea\3\2\2\2\u01ec\u01ed\3\2\2\2\u01edg\3\2\2\2\u01ee")
        buf.write("\u01ec\3\2\2\2\u01ef\u01f0\7\30\2\2\u01f0\u01f1\7\26\2")
        buf.write("\2\u01f1\u01f2\5n8\2\u01f2\u01f3\7\27\2\2\u01f3i\3\2\2")
        buf.write("\2\u01f4\u01f5\7\31\2\2\u01f5\u01f6\7\26\2\2\u01f6\u01f7")
        buf.write("\5n8\2\u01f7\u01f8\7\27\2\2\u01f8k\3\2\2\2\u01f9\u01fd")
        buf.write("\7\32\2\2\u01fa\u01fe\5$\23\2\u01fb\u01fe\5^\60\2\u01fc")
        buf.write("\u01fe\5p9\2\u01fd\u01fa\3\2\2\2\u01fd\u01fb\3\2\2\2\u01fd")
        buf.write("\u01fc\3\2\2\2\u01fem\3\2\2\2\u01ff\u0203\b8\1\2\u0200")
        buf.write("\u0204\5$\23\2\u0201\u0204\5^\60\2\u0202\u0204\5p9\2\u0203")
        buf.write("\u0200\3\2\2\2\u0203\u0201\3\2\2\2\u0203\u0202\3\2\2\2")
        buf.write("\u0204\u020b\3\2\2\2\u0205\u0206\f\4\2\2\u0206\u0207\5")
        buf.write("\24\13\2\u0207\u0208\5n8\5\u0208\u020a\3\2\2\2\u0209\u0205")
        buf.write("\3\2\2\2\u020a\u020d\3\2\2\2\u020b\u0209\3\2\2\2\u020b")
        buf.write("\u020c\3\2\2\2\u020co\3\2\2\2\u020d\u020b\3\2\2\2\u020e")
        buf.write("\u020f\7&\2\2\u020f\u0210\5r:\2\u0210q\3\2\2\2\u0211\u0212")
        buf.write("\5\30\r\2\u0212\u0213\5t;\2\u0213s\3\2\2\2\u0214\u0215")
        buf.write("\b;\1\2\u0215\u0216\7\26\2\2\u0216\u0217\5t;\2\u0217\u0218")
        buf.write("\7\27\2\2\u0218\u021b\3\2\2\2\u0219\u021b\5v<\2\u021a")
        buf.write("\u0214\3\2\2\2\u021a\u0219\3\2\2\2\u021b\u0224\3\2\2\2")
        buf.write("\u021c\u021d\f\5\2\2\u021d\u021e\5\32\16\2\u021e\u021f")
        buf.write("\5t;\6\u021f\u0223\3\2\2\2\u0220\u0221\f\3\2\2\u0221\u0223")
        buf.write("\7\23\2\2\u0222\u021c\3\2\2\2\u0222\u0220\3\2\2\2\u0223")
        buf.write("\u0226\3\2\2\2\u0224\u0222\3\2\2\2\u0224\u0225\3\2\2\2")
        buf.write("\u0225u\3\2\2\2\u0226\u0224\3\2\2\2\u0227\u0228\7\'\2")
        buf.write("\2\u0228\u0229\5x=\2\u0229w\3\2\2\2\u022a\u022b\5\6\4")
        buf.write("\2\u022b\u022d\7\23\2\2\u022c\u022e\5z>\2\u022d\u022c")
        buf.write("\3\2\2\2\u022d\u022e\3\2\2\2\u022e\u0231\3\2\2\2\u022f")
        buf.write("\u0231\5z>\2\u0230\u022a\3\2\2\2\u0230\u022f\3\2\2\2\u0231")
        buf.write("y\3\2\2\2\u0232\u0233\5\30\r\2\u0233\u0234\5|?\2\u0234")
        buf.write("{\3\2\2\2\u0235\u0236\b?\1\2\u0236\u0237\7\26\2\2\u0237")
        buf.write("\u0238\5|?\2\u0238\u0239\7\27\2\2\u0239\u0240\3\2\2\2")
        buf.write("\u023a\u023e\5^\60\2\u023b\u023e\5\34\17\2\u023c\u023e")
        buf.write("\5 \21\2\u023d\u023a\3\2\2\2\u023d\u023b\3\2\2\2\u023d")
        buf.write("\u023c\3\2\2\2\u023e\u0240\3\2\2\2\u023f\u0235\3\2\2\2")
        buf.write("\u023f\u023d\3\2\2\2\u0240\u0249\3\2\2\2\u0241\u0242\f")
        buf.write("\5\2\2\u0242\u0243\5\32\16\2\u0243\u0244\5|?\6\u0244\u0248")
        buf.write("\3\2\2\2\u0245\u0246\f\3\2\2\u0246\u0248\7\23\2\2\u0247")
        buf.write("\u0241\3\2\2\2\u0247\u0245\3\2\2\2\u0248\u024b\3\2\2\2")
        buf.write("\u0249\u0247\3\2\2\2\u0249\u024a\3\2\2\2\u024a}\3\2\2")
        buf.write("\2\u024b\u0249\3\2\2\2\u024c\u024d\7(\2\2\u024d\u024e")
        buf.write("\5\u0080A\2\u024e\177\3\2\2\2\u024f\u0250\5\30\r\2\u0250")
        buf.write("\u0251\5\u0082B\2\u0251\u0081\3\2\2\2\u0252\u0253\bB\1")
        buf.write("\2\u0253\u0254\7\26\2\2\u0254\u0255\5\u0082B\2\u0255\u0256")
        buf.write("\7\27\2\2\u0256\u0267\3\2\2\2\u0257\u0265\5$\23\2\u0258")
        buf.write("\u0265\5,\27\2\u0259\u0265\5\60\31\2\u025a\u0265\5\64")
        buf.write("\33\2\u025b\u0265\5F$\2\u025c\u0265\5b\62\2\u025d\u0265")
        buf.write("\5p9\2\u025e\u0265\5\u008eH\2\u025f\u0265\5\u0090I\2\u0260")
        buf.write("\u0265\5\u008cG\2\u0261\u0265\5\u0084C\2\u0262\u0265\5")
        buf.write("\u0086D\2\u0263\u0265\5\u0088E\2\u0264\u0257\3\2\2\2\u0264")
        buf.write("\u0258\3\2\2\2\u0264\u0259\3\2\2\2\u0264\u025a\3\2\2\2")
        buf.write("\u0264\u025b\3\2\2\2\u0264\u025c\3\2\2\2\u0264\u025d\3")
        buf.write("\2\2\2\u0264\u025e\3\2\2\2\u0264\u025f\3\2\2\2\u0264\u0260")
        buf.write("\3\2\2\2\u0264\u0261\3\2\2\2\u0264\u0262\3\2\2\2\u0264")
        buf.write("\u0263\3\2\2\2\u0265\u0267\3\2\2\2\u0266\u0252\3\2\2\2")
        buf.write("\u0266\u0264\3\2\2\2\u0267\u0270\3\2\2\2\u0268\u0269\f")
        buf.write("\5\2\2\u0269\u026a\5\32\16\2\u026a\u026b\5\u0082B\6\u026b")
        buf.write("\u026f\3\2\2\2\u026c\u026d\f\3\2\2\u026d\u026f\7\23\2")
        buf.write("\2\u026e\u0268\3\2\2\2\u026e\u026c\3\2\2\2\u026f\u0272")
        buf.write("\3\2\2\2\u0270\u026e\3\2\2\2\u0270\u0271\3\2\2\2\u0271")
        buf.write("\u0083\3\2\2\2\u0272\u0270\3\2\2\2\u0273\u0274\7\30\2")
        buf.write("\2\u0274\u0275\7\26\2\2\u0275\u0276\5\u008aF\2\u0276\u0277")
        buf.write("\7\27\2\2\u0277\u0085\3\2\2\2\u0278\u0279\7\31\2\2\u0279")
        buf.write("\u027a\7\26\2\2\u027a\u027b\5\u008aF\2\u027b\u027c\7\27")
        buf.write("\2\2\u027c\u0087\3\2\2\2\u027d\u0287\7\32\2\2\u027e\u0288")
        buf.write("\5$\23\2\u027f\u0288\5,\27\2\u0280\u0288\5\60\31\2\u0281")
        buf.write("\u0288\5\64\33\2\u0282\u0288\5F$\2\u0283\u0288\5b\62\2")
        buf.write("\u0284\u0288\5p9\2\u0285\u0288\5\u008eH\2\u0286\u0288")
        buf.write("\5\u0090I\2\u0287\u027e\3\2\2\2\u0287\u027f\3\2\2\2\u0287")
        buf.write("\u0280\3\2\2\2\u0287\u0281\3\2\2\2\u0287\u0282\3\2\2\2")
        buf.write("\u0287\u0283\3\2\2\2\u0287\u0284\3\2\2\2\u0287\u0285\3")
        buf.write("\2\2\2\u0287\u0286\3\2\2\2\u0288\u0089\3\2\2\2\u0289\u0293")
        buf.write("\bF\1\2\u028a\u0294\5$\23\2\u028b\u0294\5,\27\2\u028c")
        buf.write("\u0294\5\60\31\2\u028d\u0294\5\64\33\2\u028e\u0294\5F")
        buf.write("$\2\u028f\u0294\5b\62\2\u0290\u0294\5p9\2\u0291\u0294")
        buf.write("\5\u008eH\2\u0292\u0294\5\u0090I\2\u0293\u028a\3\2\2\2")
        buf.write("\u0293\u028b\3\2\2\2\u0293\u028c\3\2\2\2\u0293\u028d\3")
        buf.write("\2\2\2\u0293\u028e\3\2\2\2\u0293\u028f\3\2\2\2\u0293\u0290")
        buf.write("\3\2\2\2\u0293\u0291\3\2\2\2\u0293\u0292\3\2\2\2\u0294")
        buf.write("\u029b\3\2\2\2\u0295\u0296\f\4\2\2\u0296\u0297\5\24\13")
        buf.write("\2\u0297\u0298\5\u008aF\5\u0298\u029a\3\2\2\2\u0299\u0295")
        buf.write("\3\2\2\2\u029a\u029d\3\2\2\2\u029b\u0299\3\2\2\2\u029b")
        buf.write("\u029c\3\2\2\2\u029c\u008b\3\2\2\2\u029d\u029b\3\2\2\2")
        buf.write("\u029e\u029f\7)\2\2\u029f\u02a0\5\6\4\2\u02a0\u02a1\7")
        buf.write("\23\2\2\u02a1\u008d\3\2\2\2\u02a2\u02a3\7*\2\2\u02a3\u008f")
        buf.write("\3\2\2\2\u02a4\u02a5\7+\2\2\u02a5\u0091\3\2\2\2>\u0095")
        buf.write("\u0099\u009c\u00a1\u00ba\u00c0\u00c2\u00da\u00ee\u00f1")
        buf.write("\u00fc\u0104\u0106\u0129\u012b\u0133\u0135\u0147\u014e")
        buf.write("\u0156\u016f\u0171\u0179\u017b\u0184\u0187\u0194\u0196")
        buf.write("\u019e\u01a0\u01a5\u01aa\u01ad\u01ba\u01bc\u01c4\u01c6")
        buf.write("\u01e0\u01e2\u01ea\u01ec\u01fd\u0203\u020b\u021a\u0222")
        buf.write("\u0224\u022d\u0230\u023d\u023f\u0247\u0249\u0264\u0266")
        buf.write("\u026e\u0270\u0287\u0293\u029b")
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
                     "'implementation '", "<INVALID>", "'return type '", 
                     "'constructor '", "'parameter '", "'type '", "<INVALID>", 
                     "'configuration file '", "'property '", "'class '", 
                     "'overridden function '", "'bean declaration '", "'beans file'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "SPACE", "Alphabet", "NL", "LPAREN", 
                      "RPAREN", "ONE_OF", "NONE_OF", "NO", "NAME", "VALUE", 
                      "ANNOTATION", "EXTENSION", "IMPLEMENTATION", "FUNCTION", 
                      "RETURN_TYPES", "CONSTRUCTOR", "PARAMETER", "TYPES", 
                      "DeclarationStatement", "ConfigurationFile", "CONFIGURATION_PROPERTIES", 
                      "CLASSES", "OVERRIDDEN_FUNCTION", "BEAN_DECL", "BEANS_FILE" ]

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
    RULE_overriddenFunctions = 69
    RULE_beans = 70
    RULE_beansFile = 71

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
                   "overriddenFunctions", "beans", "beansFile" ]

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
    IMPLEMENTATION=29
    FUNCTION=30
    RETURN_TYPES=31
    CONSTRUCTOR=32
    PARAMETER=33
    TYPES=34
    DeclarationStatement=35
    ConfigurationFile=36
    CONFIGURATION_PROPERTIES=37
    CLASSES=38
    OVERRIDDEN_FUNCTION=39
    BEAN_DECL=40
    BEANS_FILE=41

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
            self.state = 151
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.EOF, RulepadGrammarParser.T__1, RulepadGrammarParser.NL]:
                self.state = 147
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 144
                        self.emptyLine() 
                    self.state = 149
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

                pass
            elif token in [RulepadGrammarParser.FUNCTION, RulepadGrammarParser.CONSTRUCTOR, RulepadGrammarParser.DeclarationStatement, RulepadGrammarParser.CLASSES]:
                self.state = 150
                self.mustClause()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RulepadGrammarParser.T__1:
                self.state = 153
                self.end()


            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RulepadGrammarParser.NL:
                self.state = 156
                self.match(RulepadGrammarParser.NL)
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 162
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
            self.state = 184
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.FUNCTION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.functions()
                self.state = 165
                self.must()
                self.state = 166
                self.have()
                self.state = 167
                self.functionExpression(0)
                pass
            elif token in [RulepadGrammarParser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 169
                self.constructors()
                self.state = 170
                self.must()
                self.state = 171
                self.have()
                self.state = 172
                self.constructorExpression(0)
                pass
            elif token in [RulepadGrammarParser.CLASSES]:
                self.enterOuterAlt(localctx, 3)
                self.state = 174
                self.classes()
                self.state = 175
                self.must()
                self.state = 176
                self.have()
                self.state = 177
                self.classExpression(0)
                pass
            elif token in [RulepadGrammarParser.DeclarationStatement]:
                self.enterOuterAlt(localctx, 4)
                self.state = 179
                self.declarationStatements()
                self.state = 180
                self.must()
                self.state = 181
                self.have()
                self.state = 182
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
            self.state = 186
            self.match(RulepadGrammarParser.T__0)
            self.state = 190 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 190
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.Alphabet]:
                    self.state = 187
                    self.match(RulepadGrammarParser.Alphabet)
                    pass
                elif token in [RulepadGrammarParser.T__1, RulepadGrammarParser.T__2, RulepadGrammarParser.T__3, RulepadGrammarParser.T__4, RulepadGrammarParser.T__5, RulepadGrammarParser.T__6, RulepadGrammarParser.T__7, RulepadGrammarParser.T__8, RulepadGrammarParser.T__9, RulepadGrammarParser.LPAREN, RulepadGrammarParser.RPAREN]:
                    self.state = 188
                    self.symbols()
                    pass
                elif token in [RulepadGrammarParser.SPACE]:
                    self.state = 189
                    self.match(RulepadGrammarParser.SPACE)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 192 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RulepadGrammarParser.T__1) | (1 << RulepadGrammarParser.T__2) | (1 << RulepadGrammarParser.T__3) | (1 << RulepadGrammarParser.T__4) | (1 << RulepadGrammarParser.T__5) | (1 << RulepadGrammarParser.T__6) | (1 << RulepadGrammarParser.T__7) | (1 << RulepadGrammarParser.T__8) | (1 << RulepadGrammarParser.T__9) | (1 << RulepadGrammarParser.SPACE) | (1 << RulepadGrammarParser.Alphabet) | (1 << RulepadGrammarParser.LPAREN) | (1 << RulepadGrammarParser.RPAREN))) != 0)):
                    break

            self.state = 194
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
            self.state = 196
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
            self.state = 198
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
            self.state = 200
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
            self.state = 202
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
            self.state = 204
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
            self.state = 206
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
            self.state = 208
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
            self.state = 210
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
            self.state = 212
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
            self.state = 216
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.T__12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.and_()
                pass
            elif token in [RulepadGrammarParser.T__13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
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
            self.state = 218
            self.match(RulepadGrammarParser.NAME)
            self.state = 219
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
            self.state = 221
            self.combinatorialWords()
            self.state = 222
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
            self.state = 224
            self.match(RulepadGrammarParser.VALUE)
            self.state = 225
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
            self.state = 227
            self.combinatorialWords()
            self.state = 228
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
            self.state = 230
            self.match(RulepadGrammarParser.ANNOTATION)
            self.state = 231
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
            self.state = 239
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.combinatorialWords()
                self.state = 234
                self.match(RulepadGrammarParser.SPACE)
                self.state = 236
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 235
                    self.annotationConditionTransition()


                pass
            elif token in [RulepadGrammarParser.T__15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 238
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
            self.state = 241
            self.withWord()
            self.state = 242
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
            self.state = 250
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 245
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 246
                self.annotationExpression(0)
                self.state = 247
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.PARAMETER]:
                self.state = 249
                self.annotationParameters()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 260
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 258
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.AnnotationExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_annotationExpression)
                        self.state = 252
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 253
                        localctx.op = self.binary()
                        self.state = 254
                        localctx.right = self.annotationExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.AnnotationExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_annotationExpression)
                        self.state = 256
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 257
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 262
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
            self.state = 263
            self.match(RulepadGrammarParser.EXTENSION)
            self.state = 264
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
            self.state = 266
            self.of()
            self.state = 267
            self.combinatorialWords()
            self.state = 268
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
            self.state = 270
            self.match(RulepadGrammarParser.IMPLEMENTATION)
            self.state = 271
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
            self.state = 273
            self.of()
            self.state = 274
            self.combinatorialWords()
            self.state = 275
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
            self.state = 277
            self.match(RulepadGrammarParser.FUNCTION)
            self.state = 278
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
            self.state = 280
            self.withWord()
            self.state = 281
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
            self.state = 297
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 284
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 285
                self.functionExpression(0)
                self.state = 286
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.ONE_OF, RulepadGrammarParser.NONE_OF, RulepadGrammarParser.NO, RulepadGrammarParser.ANNOTATION, RulepadGrammarParser.RETURN_TYPES, RulepadGrammarParser.PARAMETER, RulepadGrammarParser.ConfigurationFile]:
                self.state = 295
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.ANNOTATION]:
                    self.state = 288
                    self.annotations()
                    pass
                elif token in [RulepadGrammarParser.RETURN_TYPES]:
                    self.state = 289
                    self.returnTypes()
                    pass
                elif token in [RulepadGrammarParser.PARAMETER]:
                    self.state = 290
                    self.functionParameters()
                    pass
                elif token in [RulepadGrammarParser.ConfigurationFile]:
                    self.state = 291
                    self.configurationFiles()
                    pass
                elif token in [RulepadGrammarParser.NONE_OF]:
                    self.state = 292
                    self.functionExpressionNoneOf()
                    pass
                elif token in [RulepadGrammarParser.ONE_OF]:
                    self.state = 293
                    self.functionExpressionOneOf()
                    pass
                elif token in [RulepadGrammarParser.NO]:
                    self.state = 294
                    self.functionExpressionNo()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 307
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 305
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.FunctionExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_functionExpression)
                        self.state = 299
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 300
                        localctx.op = self.binary()
                        self.state = 301
                        localctx.right = self.functionExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.FunctionExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_functionExpression)
                        self.state = 303
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 304
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 309
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
            self.state = 310
            self.match(RulepadGrammarParser.ONE_OF)
            self.state = 311
            self.match(RulepadGrammarParser.LPAREN)
            self.state = 312
            self.functionExpressionAggregateContents(0)
            self.state = 313
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
            self.state = 315
            self.match(RulepadGrammarParser.NONE_OF)
            self.state = 316
            self.match(RulepadGrammarParser.LPAREN)
            self.state = 317
            self.functionExpressionAggregateContents(0)
            self.state = 318
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
            self.state = 320
            self.match(RulepadGrammarParser.NO)
            self.state = 325
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.ANNOTATION]:
                self.state = 321
                self.annotations()
                pass
            elif token in [RulepadGrammarParser.RETURN_TYPES]:
                self.state = 322
                self.returnTypes()
                pass
            elif token in [RulepadGrammarParser.PARAMETER]:
                self.state = 323
                self.functionParameters()
                pass
            elif token in [RulepadGrammarParser.ConfigurationFile]:
                self.state = 324
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
            self.state = 332
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.ANNOTATION]:
                self.state = 328
                self.annotations()
                pass
            elif token in [RulepadGrammarParser.RETURN_TYPES]:
                self.state = 329
                self.returnTypes()
                pass
            elif token in [RulepadGrammarParser.PARAMETER]:
                self.state = 330
                self.functionParameters()
                pass
            elif token in [RulepadGrammarParser.ConfigurationFile]:
                self.state = 331
                self.configurationFiles()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 340
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
                    self.state = 334
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 335
                    localctx.op = self.or_()
                    self.state = 336
                    localctx.right = self.functionExpressionAggregateContents(3) 
                self.state = 342
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
            self.state = 343
            self.match(RulepadGrammarParser.RETURN_TYPES)
            self.state = 344
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
            self.state = 346
            self.combinatorialWords()
            self.state = 347
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
            self.state = 349
            self.match(RulepadGrammarParser.CONSTRUCTOR)
            self.state = 350
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
            self.state = 352
            self.of()
            self.state = 353
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
            self.state = 355
            self.withWord()
            self.state = 356
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
            self.state = 367
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 359
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 360
                self.constructorExpression(0)
                self.state = 361
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.ANNOTATION, RulepadGrammarParser.PARAMETER]:
                self.state = 365
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.ANNOTATION]:
                    self.state = 363
                    self.annotations()
                    pass
                elif token in [RulepadGrammarParser.PARAMETER]:
                    self.state = 364
                    self.functionParameters()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 377
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 375
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.ConstructorExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_constructorExpression)
                        self.state = 369
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 370
                        localctx.op = self.binary()
                        self.state = 371
                        localctx.right = self.constructorExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.ConstructorExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_constructorExpression)
                        self.state = 373
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 374
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 379
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
            self.state = 380
            self.match(RulepadGrammarParser.PARAMETER)
            self.state = 381
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
            self.state = 389
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 383
                self.combinatorialWords()
                self.state = 384
                self.match(RulepadGrammarParser.SPACE)
                self.state = 386
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                if la_ == 1:
                    self.state = 385
                    self.annotationParameterConditionTransition()


                pass
            elif token in [RulepadGrammarParser.T__15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 388
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
            self.state = 391
            self.withWord()
            self.state = 392
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
            self.state = 404
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 395
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 396
                self.annotationParameterExpression(0)
                self.state = 397
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.NAME, RulepadGrammarParser.VALUE, RulepadGrammarParser.TYPES]:
                self.state = 402
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.TYPES]:
                    self.state = 399
                    self.types()
                    pass
                elif token in [RulepadGrammarParser.NAME]:
                    self.state = 400
                    self.names()
                    pass
                elif token in [RulepadGrammarParser.VALUE]:
                    self.state = 401
                    self.values()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 414
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 412
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.AnnotationParameterExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_annotationParameterExpression)
                        self.state = 406
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 407
                        localctx.op = self.binary()
                        self.state = 408
                        localctx.right = self.annotationParameterExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.AnnotationParameterExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_annotationParameterExpression)
                        self.state = 410
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 411
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 416
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
            self.state = 417
            self.match(RulepadGrammarParser.PARAMETER)
            self.state = 419
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 418
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
            self.state = 427
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 421
                self.combinatorialWords()
                self.state = 422
                self.match(RulepadGrammarParser.SPACE)
                self.state = 424
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                if la_ == 1:
                    self.state = 423
                    self.functionParameterConditionTransition()


                pass
            elif token in [RulepadGrammarParser.T__15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 426
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
            self.state = 429
            self.withWord()
            self.state = 430
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
            self.state = 442
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 433
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 434
                self.functionParameterExpression(0)
                self.state = 435
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.NAME, RulepadGrammarParser.ANNOTATION, RulepadGrammarParser.TYPES]:
                self.state = 440
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.TYPES]:
                    self.state = 437
                    self.types()
                    pass
                elif token in [RulepadGrammarParser.NAME]:
                    self.state = 438
                    self.names()
                    pass
                elif token in [RulepadGrammarParser.ANNOTATION]:
                    self.state = 439
                    self.annotations()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 452
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 450
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.FunctionParameterExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_functionParameterExpression)
                        self.state = 444
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 445
                        localctx.op = self.binary()
                        self.state = 446
                        localctx.right = self.functionParameterExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.FunctionParameterExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_functionParameterExpression)
                        self.state = 448
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 449
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 454
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
            self.state = 455
            self.match(RulepadGrammarParser.TYPES)
            self.state = 456
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
            self.state = 458
            self.combinatorialWords()
            self.state = 459
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
            self.state = 461
            self.match(RulepadGrammarParser.DeclarationStatement)
            self.state = 462
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
            self.state = 464
            self.withWord()
            self.state = 465
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
            self.state = 480
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 468
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 469
                self.declarationStatementExpression(0)
                self.state = 470
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.ONE_OF, RulepadGrammarParser.NONE_OF, RulepadGrammarParser.NO, RulepadGrammarParser.ANNOTATION, RulepadGrammarParser.TYPES, RulepadGrammarParser.ConfigurationFile]:
                self.state = 478
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.ANNOTATION]:
                    self.state = 472
                    self.annotations()
                    pass
                elif token in [RulepadGrammarParser.TYPES]:
                    self.state = 473
                    self.types()
                    pass
                elif token in [RulepadGrammarParser.ConfigurationFile]:
                    self.state = 474
                    self.configurationFiles()
                    pass
                elif token in [RulepadGrammarParser.ONE_OF]:
                    self.state = 475
                    self.declarationStatementExpressionOneOf()
                    pass
                elif token in [RulepadGrammarParser.NONE_OF]:
                    self.state = 476
                    self.declarationStatementExpressionNoneOf()
                    pass
                elif token in [RulepadGrammarParser.NO]:
                    self.state = 477
                    self.declarationStatementExpressionNo()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 490
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 488
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.DeclarationStatementExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_declarationStatementExpression)
                        self.state = 482
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 483
                        localctx.op = self.binary()
                        self.state = 484
                        localctx.right = self.declarationStatementExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.DeclarationStatementExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_declarationStatementExpression)
                        self.state = 486
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 487
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 492
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
            self.state = 493
            self.match(RulepadGrammarParser.ONE_OF)
            self.state = 494
            self.match(RulepadGrammarParser.LPAREN)
            self.state = 495
            self.declarationStatementExpressionAggregateContents(0)
            self.state = 496
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
            self.state = 498
            self.match(RulepadGrammarParser.NONE_OF)
            self.state = 499
            self.match(RulepadGrammarParser.LPAREN)
            self.state = 500
            self.declarationStatementExpressionAggregateContents(0)
            self.state = 501
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
            self.state = 503
            self.match(RulepadGrammarParser.NO)
            self.state = 507
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.ANNOTATION]:
                self.state = 504
                self.annotations()
                pass
            elif token in [RulepadGrammarParser.TYPES]:
                self.state = 505
                self.types()
                pass
            elif token in [RulepadGrammarParser.ConfigurationFile]:
                self.state = 506
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
            self.state = 513
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
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 521
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
                    self.state = 515
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 516
                    localctx.op = self.or_()
                    self.state = 517
                    localctx.right = self.declarationStatementExpressionAggregateContents(3) 
                self.state = 523
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
            self.state = 524
            self.match(RulepadGrammarParser.ConfigurationFile)
            self.state = 525
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
            self.state = 527
            self.withWord()
            self.state = 528
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
            self.state = 536
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 531
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 532
                self.configurationFileExpression(0)
                self.state = 533
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.CONFIGURATION_PROPERTIES]:
                self.state = 535
                self.configurationProperties()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 546
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 544
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.ConfigurationFileExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_configurationFileExpression)
                        self.state = 538
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 539
                        localctx.op = self.binary()
                        self.state = 540
                        localctx.right = self.configurationFileExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.ConfigurationFileExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_configurationFileExpression)
                        self.state = 542
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 543
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 548
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
            self.state = 549
            self.match(RulepadGrammarParser.CONFIGURATION_PROPERTIES)
            self.state = 550
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
            self.state = 558
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 552
                self.combinatorialWords()
                self.state = 553
                self.match(RulepadGrammarParser.SPACE)
                self.state = 555
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
                if la_ == 1:
                    self.state = 554
                    self.configurationPropertyConditionTransition()


                pass
            elif token in [RulepadGrammarParser.T__15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 557
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
            self.state = 560
            self.withWord()
            self.state = 561
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
            self.state = 573
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 564
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 565
                self.configurationPropertyExpression(0)
                self.state = 566
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.NAME, RulepadGrammarParser.VALUE, RulepadGrammarParser.TYPES]:
                self.state = 571
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.TYPES]:
                    self.state = 568
                    self.types()
                    pass
                elif token in [RulepadGrammarParser.NAME]:
                    self.state = 569
                    self.names()
                    pass
                elif token in [RulepadGrammarParser.VALUE]:
                    self.state = 570
                    self.values()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 583
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,52,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 581
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.ConfigurationPropertyExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_configurationPropertyExpression)
                        self.state = 575
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 576
                        localctx.op = self.binary()
                        self.state = 577
                        localctx.right = self.configurationPropertyExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.ConfigurationPropertyExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_configurationPropertyExpression)
                        self.state = 579
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 580
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 585
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
            self.state = 586
            self.match(RulepadGrammarParser.CLASSES)
            self.state = 587
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
            self.state = 589
            self.withWord()
            self.state = 590
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
            self.state = 612
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.LPAREN]:
                self.state = 593
                self.match(RulepadGrammarParser.LPAREN)
                self.state = 594
                self.classExpression(0)
                self.state = 595
                self.match(RulepadGrammarParser.RPAREN)
                pass
            elif token in [RulepadGrammarParser.ONE_OF, RulepadGrammarParser.NONE_OF, RulepadGrammarParser.NO, RulepadGrammarParser.ANNOTATION, RulepadGrammarParser.EXTENSION, RulepadGrammarParser.IMPLEMENTATION, RulepadGrammarParser.FUNCTION, RulepadGrammarParser.CONSTRUCTOR, RulepadGrammarParser.DeclarationStatement, RulepadGrammarParser.ConfigurationFile, RulepadGrammarParser.OVERRIDDEN_FUNCTION, RulepadGrammarParser.BEAN_DECL, RulepadGrammarParser.BEANS_FILE]:
                self.state = 610
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RulepadGrammarParser.ANNOTATION]:
                    self.state = 597
                    self.annotations()
                    pass
                elif token in [RulepadGrammarParser.EXTENSION]:
                    self.state = 598
                    self.extensions()
                    pass
                elif token in [RulepadGrammarParser.IMPLEMENTATION]:
                    self.state = 599
                    self.implementations()
                    pass
                elif token in [RulepadGrammarParser.FUNCTION]:
                    self.state = 600
                    self.functions()
                    pass
                elif token in [RulepadGrammarParser.CONSTRUCTOR]:
                    self.state = 601
                    self.constructors()
                    pass
                elif token in [RulepadGrammarParser.DeclarationStatement]:
                    self.state = 602
                    self.declarationStatements()
                    pass
                elif token in [RulepadGrammarParser.ConfigurationFile]:
                    self.state = 603
                    self.configurationFiles()
                    pass
                elif token in [RulepadGrammarParser.BEAN_DECL]:
                    self.state = 604
                    self.beans()
                    pass
                elif token in [RulepadGrammarParser.BEANS_FILE]:
                    self.state = 605
                    self.beansFile()
                    pass
                elif token in [RulepadGrammarParser.OVERRIDDEN_FUNCTION]:
                    self.state = 606
                    self.overriddenFunctions()
                    pass
                elif token in [RulepadGrammarParser.ONE_OF]:
                    self.state = 607
                    self.classExpressionOneOf()
                    pass
                elif token in [RulepadGrammarParser.NONE_OF]:
                    self.state = 608
                    self.classExpressionNoneOf()
                    pass
                elif token in [RulepadGrammarParser.NO]:
                    self.state = 609
                    self.classExpressionNo()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 622
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,56,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 620
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
                    if la_ == 1:
                        localctx = RulepadGrammarParser.ClassExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_classExpression)
                        self.state = 614
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 615
                        localctx.op = self.binary()
                        self.state = 616
                        localctx.right = self.classExpression(4)
                        pass

                    elif la_ == 2:
                        localctx = RulepadGrammarParser.ClassExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_classExpression)
                        self.state = 618
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 619
                        self.match(RulepadGrammarParser.SPACE)
                        pass

             
                self.state = 624
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
            self.state = 625
            self.match(RulepadGrammarParser.ONE_OF)
            self.state = 626
            self.match(RulepadGrammarParser.LPAREN)
            self.state = 627
            self.classExpressionAggregateContents(0)
            self.state = 628
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
            self.state = 630
            self.match(RulepadGrammarParser.NONE_OF)
            self.state = 631
            self.match(RulepadGrammarParser.LPAREN)
            self.state = 632
            self.classExpressionAggregateContents(0)
            self.state = 633
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
            self.state = 635
            self.match(RulepadGrammarParser.NO)
            self.state = 645
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.ANNOTATION]:
                self.state = 636
                self.annotations()
                pass
            elif token in [RulepadGrammarParser.EXTENSION]:
                self.state = 637
                self.extensions()
                pass
            elif token in [RulepadGrammarParser.IMPLEMENTATION]:
                self.state = 638
                self.implementations()
                pass
            elif token in [RulepadGrammarParser.FUNCTION]:
                self.state = 639
                self.functions()
                pass
            elif token in [RulepadGrammarParser.CONSTRUCTOR]:
                self.state = 640
                self.constructors()
                pass
            elif token in [RulepadGrammarParser.DeclarationStatement]:
                self.state = 641
                self.declarationStatements()
                pass
            elif token in [RulepadGrammarParser.ConfigurationFile]:
                self.state = 642
                self.configurationFiles()
                pass
            elif token in [RulepadGrammarParser.BEAN_DECL]:
                self.state = 643
                self.beans()
                pass
            elif token in [RulepadGrammarParser.BEANS_FILE]:
                self.state = 644
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
            self.state = 657
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RulepadGrammarParser.ANNOTATION]:
                self.state = 648
                self.annotations()
                pass
            elif token in [RulepadGrammarParser.EXTENSION]:
                self.state = 649
                self.extensions()
                pass
            elif token in [RulepadGrammarParser.IMPLEMENTATION]:
                self.state = 650
                self.implementations()
                pass
            elif token in [RulepadGrammarParser.FUNCTION]:
                self.state = 651
                self.functions()
                pass
            elif token in [RulepadGrammarParser.CONSTRUCTOR]:
                self.state = 652
                self.constructors()
                pass
            elif token in [RulepadGrammarParser.DeclarationStatement]:
                self.state = 653
                self.declarationStatements()
                pass
            elif token in [RulepadGrammarParser.ConfigurationFile]:
                self.state = 654
                self.configurationFiles()
                pass
            elif token in [RulepadGrammarParser.BEAN_DECL]:
                self.state = 655
                self.beans()
                pass
            elif token in [RulepadGrammarParser.BEANS_FILE]:
                self.state = 656
                self.beansFile()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 665
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
                    self.state = 659
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 660
                    localctx.op = self.or_()
                    self.state = 661
                    localctx.right = self.classExpressionAggregateContents(3) 
                self.state = 667
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,59,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 138, self.RULE_overriddenFunctions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 668
            self.match(RulepadGrammarParser.OVERRIDDEN_FUNCTION)
            self.state = 669
            self.combinatorialWords()
            self.state = 670
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
        self.enterRule(localctx, 140, self.RULE_beans)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 672
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
        self.enterRule(localctx, 142, self.RULE_beansFile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 674
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
         




