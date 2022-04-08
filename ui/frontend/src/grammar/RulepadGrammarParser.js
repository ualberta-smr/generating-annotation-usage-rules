// Generated from ../violation-detection/src/main/antlr4/ca/ualberta/grammar/RulepadGrammar.g4 by ANTLR 4.9
// jshint ignore: start
import antlr4 from 'antlr4';
import RulepadGrammarListener from './RulepadGrammarListener.js';

const serializedATN = ["\u0003\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786",
    "\u5964\u0003+\u0251\u0004\u0002\t\u0002\u0004\u0003\t\u0003\u0004\u0004",
    "\t\u0004\u0004\u0005\t\u0005\u0004\u0006\t\u0006\u0004\u0007\t\u0007",
    "\u0004\b\t\b\u0004\t\t\t\u0004\n\t\n\u0004\u000b\t\u000b\u0004\f\t\f",
    "\u0004\r\t\r\u0004\u000e\t\u000e\u0004\u000f\t\u000f\u0004\u0010\t\u0010",
    "\u0004\u0011\t\u0011\u0004\u0012\t\u0012\u0004\u0013\t\u0013\u0004\u0014",
    "\t\u0014\u0004\u0015\t\u0015\u0004\u0016\t\u0016\u0004\u0017\t\u0017",
    "\u0004\u0018\t\u0018\u0004\u0019\t\u0019\u0004\u001a\t\u001a\u0004\u001b",
    "\t\u001b\u0004\u001c\t\u001c\u0004\u001d\t\u001d\u0004\u001e\t\u001e",
    "\u0004\u001f\t\u001f\u0004 \t \u0004!\t!\u0004\"\t\"\u0004#\t#\u0004",
    "$\t$\u0004%\t%\u0004&\t&\u0004\'\t\'\u0004(\t(\u0004)\t)\u0004*\t*\u0004",
    "+\t+\u0004,\t,\u0004-\t-\u0004.\t.\u0004/\t/\u00040\t0\u00041\t1\u0004",
    "2\t2\u00043\t3\u00044\t4\u00045\t5\u00046\t6\u00047\t7\u00048\t8\u0003",
    "\u0002\u0007\u0002r\n\u0002\f\u0002\u000e\u0002u\u000b\u0002\u0003\u0002",
    "\u0005\u0002x\n\u0002\u0003\u0002\u0005\u0002{\n\u0002\u0003\u0002\u0007",
    "\u0002~\n\u0002\f\u0002\u000e\u0002\u0081\u000b\u0002\u0003\u0002\u0003",
    "\u0002\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003",
    "\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003",
    "\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003",
    "\u0003\u0003\u0003\u0003\u0003\u0005\u0003\u0099\n\u0003\u0003\u0004",
    "\u0003\u0004\u0003\u0004\u0003\u0004\u0003\u0004\u0003\u0004\u0003\u0004",
    "\u0007\u0004\u00a2\n\u0004\f\u0004\u000e\u0004\u00a5\u000b\u0004\u0003",
    "\u0004\u0003\u0004\u0003\u0004\u0003\u0005\u0006\u0005\u00ab\n\u0005",
    "\r\u0005\u000e\u0005\u00ac\u0003\u0005\u0003\u0005\u0006\u0005\u00b1",
    "\n\u0005\r\u0005\u000e\u0005\u00b2\u0003\u0005\u0003\u0005\u0006\u0005",
    "\u00b7\n\u0005\r\u0005\u000e\u0005\u00b8\u0003\u0005\u0003\u0005\u0006",
    "\u0005\u00bd\n\u0005\r\u0005\u000e\u0005\u00be\u0003\u0005\u0006\u0005",
    "\u00c2\n\u0005\r\u0005\u000e\u0005\u00c3\u0003\u0005\u0003\u0005\u0003",
    "\u0005\u0006\u0005\u00c9\n\u0005\r\u0005\u000e\u0005\u00ca\u0003\u0005",
    "\u0003\u0005\u0003\u0005\u0006\u0005\u00d0\n\u0005\r\u0005\u000e\u0005",
    "\u00d1\u0003\u0005\u0003\u0005\u0003\u0005\u0006\u0005\u00d7\n\u0005",
    "\r\u0005\u000e\u0005\u00d8\u0003\u0005\u0005\u0005\u00dc\n\u0005\u0003",
    "\u0006\u0003\u0006\u0003\u0006\u0003\u0006\u0006\u0006\u00e2\n\u0006",
    "\r\u0006\u000e\u0006\u00e3\u0003\u0006\u0003\u0006\u0003\u0007\u0003",
    "\u0007\u0003\b\u0003\b\u0003\t\u0003\t\u0003\n\u0003\n\u0003\n\u0003",
    "\n\u0006\n\u00f2\n\n\r\n\u000e\n\u00f3\u0003\n\u0003\n\u0003\u000b\u0003",
    "\u000b\u0003\f\u0003\f\u0003\r\u0003\r\u0003\u000e\u0003\u000e\u0003",
    "\u000f\u0003\u000f\u0003\u0010\u0003\u0010\u0003\u0011\u0003\u0011\u0005",
    "\u0011\u0106\n\u0011\u0003\u0012\u0003\u0012\u0005\u0012\u010a\n\u0012",
    "\u0003\u0013\u0003\u0013\u0003\u0013\u0003\u0014\u0003\u0014\u0005\u0014",
    "\u0111\n\u0014\u0003\u0015\u0003\u0015\u0003\u0015\u0005\u0015\u0116",
    "\n\u0015\u0003\u0015\u0005\u0015\u0119\n\u0015\u0003\u0016\u0003\u0016",
    "\u0003\u0016\u0003\u0017\u0003\u0017\u0003\u0017\u0003\u0017\u0003\u0017",
    "\u0003\u0017\u0005\u0017\u0124\n\u0017\u0003\u0017\u0003\u0017\u0003",
    "\u0017\u0003\u0017\u0003\u0017\u0003\u0017\u0007\u0017\u012c\n\u0017",
    "\f\u0017\u000e\u0017\u012f\u000b\u0017\u0003\u0018\u0003\u0018\u0003",
    "\u0018\u0003\u0019\u0003\u0019\u0003\u0019\u0003\u0019\u0003\u0019\u0005",
    "\u0019\u0139\n\u0019\u0003\u001a\u0003\u001a\u0003\u001a\u0003\u001b",
    "\u0003\u001b\u0003\u001b\u0003\u001b\u0003\u001b\u0005\u001b\u0143\n",
    "\u001b\u0003\u001c\u0003\u001c\u0003\u001c\u0003\u001d\u0003\u001d\u0003",
    "\u001d\u0003\u001e\u0003\u001e\u0003\u001e\u0003\u001e\u0003\u001e\u0003",
    "\u001e\u0003\u001e\u0003\u001e\u0005\u001e\u0153\n\u001e\u0005\u001e",
    "\u0155\n\u001e\u0003\u001e\u0003\u001e\u0003\u001e\u0003\u001e\u0003",
    "\u001e\u0003\u001e\u0007\u001e\u015d\n\u001e\f\u001e\u000e\u001e\u0160",
    "\u000b\u001e\u0003\u001f\u0003\u001f\u0003\u001f\u0003 \u0003 \u0003",
    " \u0003!\u0003!\u0003!\u0003\"\u0003\"\u0003\"\u0003\"\u0003\"\u0003",
    "\"\u0003\"\u0005\"\u0172\n\"\u0005\"\u0174\n\"\u0003\"\u0003\"\u0003",
    "\"\u0003\"\u0003\"\u0003\"\u0007\"\u017c\n\"\f\"\u000e\"\u017f\u000b",
    "\"\u0003#\u0003#\u0005#\u0183\n#\u0003$\u0003$\u0003$\u0003$\u0003$",
    "\u0003$\u0005$\u018b\n$\u0003%\u0003%\u0003%\u0003%\u0003%\u0003%\u0003",
    "%\u0005%\u0194\n%\u0005%\u0196\n%\u0003%\u0003%\u0003%\u0003%\u0003",
    "%\u0003%\u0007%\u019e\n%\f%\u000e%\u01a1\u000b%\u0003&\u0003&\u0005",
    "&\u01a5\n&\u0003\'\u0003\'\u0003\'\u0005\'\u01aa\n\'\u0003\'\u0005\'",
    "\u01ad\n\'\u0003(\u0003(\u0003(\u0003)\u0003)\u0003)\u0003)\u0003)\u0003",
    ")\u0003)\u0003)\u0005)\u01ba\n)\u0005)\u01bc\n)\u0003)\u0003)\u0003",
    ")\u0003)\u0003)\u0003)\u0007)\u01c4\n)\f)\u000e)\u01c7\u000b)\u0003",
    "*\u0003*\u0005*\u01cb\n*\u0003+\u0003+\u0003+\u0003+\u0003+\u0003+\u0005",
    "+\u01d3\n+\u0003,\u0003,\u0003,\u0003-\u0003-\u0003-\u0003.\u0003.\u0003",
    ".\u0003.\u0003.\u0003.\u0003.\u0005.\u01e2\n.\u0005.\u01e4\n.\u0003",
    ".\u0003.\u0003.\u0003.\u0003.\u0003.\u0007.\u01ec\n.\f.\u000e.\u01ef",
    "\u000b.\u0003/\u0003/\u0005/\u01f3\n/\u00030\u00030\u00030\u00031\u0003",
    "1\u00031\u00031\u00031\u00031\u00051\u01fe\n1\u00031\u00031\u00031\u0003",
    "1\u00031\u00031\u00071\u0206\n1\f1\u000e1\u0209\u000b1\u00032\u0003",
    "2\u00032\u00033\u00033\u00033\u00033\u00033\u00033\u00053\u0214\n3\u0003",
    "4\u00034\u00034\u00034\u00034\u00034\u00034\u00054\u021d\n4\u00054\u021f",
    "\n4\u00034\u00034\u00034\u00034\u00034\u00034\u00074\u0227\n4\f4\u000e",
    "4\u022a\u000b4\u00035\u00035\u00055\u022e\n5\u00036\u00036\u00036\u0003",
    "7\u00037\u00037\u00037\u00037\u00037\u00037\u00037\u00037\u00037\u0003",
    "7\u00037\u00037\u00057\u0240\n7\u00057\u0242\n7\u00037\u00037\u0003",
    "7\u00037\u00037\u00037\u00077\u024a\n7\f7\u000e7\u024d\u000b7\u0003",
    "8\u00038\u00038\u0002\u000b,:BHPZ`fl9\u0002\u0004\u0006\b\n\f\u000e",
    "\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \"$&(*,.02468:<>@B",
    "DFHJLNPRTVXZ\\^`bdfhjln\u0002\u0003\u0004\u0002\t\u0011\u001b\u001c",
    "\u0002\u0272\u0002w\u0003\u0002\u0002\u0002\u0004\u0098\u0003\u0002",
    "\u0002\u0002\u0006\u009a\u0003\u0002\u0002\u0002\b\u00db\u0003\u0002",
    "\u0002\u0002\n\u00dd\u0003\u0002\u0002\u0002\f\u00e7\u0003\u0002\u0002",
    "\u0002\u000e\u00e9\u0003\u0002\u0002\u0002\u0010\u00eb\u0003\u0002\u0002",
    "\u0002\u0012\u00ed\u0003\u0002\u0002\u0002\u0014\u00f7\u0003\u0002\u0002",
    "\u0002\u0016\u00f9\u0003\u0002\u0002\u0002\u0018\u00fb\u0003\u0002\u0002",
    "\u0002\u001a\u00fd\u0003\u0002\u0002\u0002\u001c\u00ff\u0003\u0002\u0002",
    "\u0002\u001e\u0101\u0003\u0002\u0002\u0002 \u0105\u0003\u0002\u0002",
    "\u0002\"\u0107\u0003\u0002\u0002\u0002$\u010b\u0003\u0002\u0002\u0002",
    "&\u010e\u0003\u0002\u0002\u0002(\u0118\u0003\u0002\u0002\u0002*\u011a",
    "\u0003\u0002\u0002\u0002,\u0123\u0003\u0002\u0002\u0002.\u0130\u0003",
    "\u0002\u0002\u00020\u0133\u0003\u0002\u0002\u00022\u013a\u0003\u0002",
    "\u0002\u00024\u013d\u0003\u0002\u0002\u00026\u0144\u0003\u0002\u0002",
    "\u00028\u0147\u0003\u0002\u0002\u0002:\u0154\u0003\u0002\u0002\u0002",
    "<\u0161\u0003\u0002\u0002\u0002>\u0164\u0003\u0002\u0002\u0002@\u0167",
    "\u0003\u0002\u0002\u0002B\u0173\u0003\u0002\u0002\u0002D\u0180\u0003",
    "\u0002\u0002\u0002F\u018a\u0003\u0002\u0002\u0002H\u0195\u0003\u0002",
    "\u0002\u0002J\u01a2\u0003\u0002\u0002\u0002L\u01ac\u0003\u0002\u0002",
    "\u0002N\u01ae\u0003\u0002\u0002\u0002P\u01bb\u0003\u0002\u0002\u0002",
    "R\u01c8\u0003\u0002\u0002\u0002T\u01d2\u0003\u0002\u0002\u0002V\u01d4",
    "\u0003\u0002\u0002\u0002X\u01d7\u0003\u0002\u0002\u0002Z\u01e3\u0003",
    "\u0002\u0002\u0002\\\u01f0\u0003\u0002\u0002\u0002^\u01f4\u0003\u0002",
    "\u0002\u0002`\u01fd\u0003\u0002\u0002\u0002b\u020a\u0003\u0002\u0002",
    "\u0002d\u0213\u0003\u0002\u0002\u0002f\u021e\u0003\u0002\u0002\u0002",
    "h\u022b\u0003\u0002\u0002\u0002j\u022f\u0003\u0002\u0002\u0002l\u0241",
    "\u0003\u0002\u0002\u0002n\u024e\u0003\u0002\u0002\u0002pr\u0005\u0010",
    "\t\u0002qp\u0003\u0002\u0002\u0002ru\u0003\u0002\u0002\u0002sq\u0003",
    "\u0002\u0002\u0002st\u0003\u0002\u0002\u0002tx\u0003\u0002\u0002\u0002",
    "us\u0003\u0002\u0002\u0002vx\u0005\u0004\u0003\u0002ws\u0003\u0002\u0002",
    "\u0002wv\u0003\u0002\u0002\u0002xz\u0003\u0002\u0002\u0002y{\u0005\u000e",
    "\b\u0002zy\u0003\u0002\u0002\u0002z{\u0003\u0002\u0002\u0002{\u007f",
    "\u0003\u0002\u0002\u0002|~\u0007\u001a\u0002\u0002}|\u0003\u0002\u0002",
    "\u0002~\u0081\u0003\u0002\u0002\u0002\u007f}\u0003\u0002\u0002\u0002",
    "\u007f\u0080\u0003\u0002\u0002\u0002\u0080\u0082\u0003\u0002\u0002\u0002",
    "\u0081\u007f\u0003\u0002\u0002\u0002\u0082\u0083\u0007\u0002\u0002\u0003",
    "\u0083\u0003\u0003\u0002\u0002\u0002\u0084\u0085\u00056\u001c\u0002",
    "\u0085\u0086\u0005\u0014\u000b\u0002\u0086\u0087\u0005\u001c\u000f\u0002",
    "\u0087\u0088\u0005:\u001e\u0002\u0088\u0099\u0003\u0002\u0002\u0002",
    "\u0089\u008a\u0005<\u001f\u0002\u008a\u008b\u0005\u0014\u000b\u0002",
    "\u008b\u008c\u0005\u001c\u000f\u0002\u008c\u008d\u0005B\"\u0002\u008d",
    "\u0099\u0003\u0002\u0002\u0002\u008e\u008f\u0005h5\u0002\u008f\u0090",
    "\u0005\u0014\u000b\u0002\u0090\u0091\u0005\u001c\u000f\u0002\u0091\u0092",
    "\u0005l7\u0002\u0092\u0099\u0003\u0002\u0002\u0002\u0093\u0094\u0005",
    "V,\u0002\u0094\u0095\u0005\u0014\u000b\u0002\u0095\u0096\u0005\u001c",
    "\u000f\u0002\u0096\u0097\u0005Z.\u0002\u0097\u0099\u0003\u0002\u0002",
    "\u0002\u0098\u0084\u0003\u0002\u0002\u0002\u0098\u0089\u0003\u0002\u0002",
    "\u0002\u0098\u008e\u0003\u0002\u0002\u0002\u0098\u0093\u0003\u0002\u0002",
    "\u0002\u0099\u0005\u0003\u0002\u0002\u0002\u009a\u00a3\u0007\u0003\u0002",
    "\u0002\u009b\u009c\u0005\b\u0005\u0002\u009c\u009d\u0007\u0004\u0002",
    "\u0002\u009d\u00a2\u0003\u0002\u0002\u0002\u009e\u009f\u0005\b\u0005",
    "\u0002\u009f\u00a0\u0007\u0005\u0002\u0002\u00a0\u00a2\u0003\u0002\u0002",
    "\u0002\u00a1\u009b\u0003\u0002\u0002\u0002\u00a1\u009e\u0003\u0002\u0002",
    "\u0002\u00a2\u00a5\u0003\u0002\u0002\u0002\u00a3\u00a1\u0003\u0002\u0002",
    "\u0002\u00a3\u00a4\u0003\u0002\u0002\u0002\u00a4\u00a6\u0003\u0002\u0002",
    "\u0002\u00a5\u00a3\u0003\u0002\u0002\u0002\u00a6\u00a7\u0005\b\u0005",
    "\u0002\u00a7\u00a8\u0007\u0003\u0002\u0002\u00a8\u0007\u0003\u0002\u0002",
    "\u0002\u00a9\u00ab\u0007\u0019\u0002\u0002\u00aa\u00a9\u0003\u0002\u0002",
    "\u0002\u00ab\u00ac\u0003\u0002\u0002\u0002\u00ac\u00aa\u0003\u0002\u0002",
    "\u0002\u00ac\u00ad\u0003\u0002\u0002\u0002\u00ad\u00dc\u0003\u0002\u0002",
    "\u0002\u00ae\u00b0\u0007\u0006\u0002\u0002\u00af\u00b1\u0007\u0019\u0002",
    "\u0002\u00b0\u00af\u0003\u0002\u0002\u0002\u00b1\u00b2\u0003\u0002\u0002",
    "\u0002\u00b2\u00b0\u0003\u0002\u0002\u0002\u00b2\u00b3\u0003\u0002\u0002",
    "\u0002\u00b3\u00dc\u0003\u0002\u0002\u0002\u00b4\u00b6\u0007\u0007\u0002",
    "\u0002\u00b5\u00b7\u0007\u0019\u0002\u0002\u00b6\u00b5\u0003\u0002\u0002",
    "\u0002\u00b7\u00b8\u0003\u0002\u0002\u0002\u00b8\u00b6\u0003\u0002\u0002",
    "\u0002\u00b8\u00b9\u0003\u0002\u0002\u0002\u00b9\u00dc\u0003\u0002\u0002",
    "\u0002\u00ba\u00bc\u0007\b\u0002\u0002\u00bb\u00bd\u0007\u0019\u0002",
    "\u0002\u00bc\u00bb\u0003\u0002\u0002\u0002\u00bd\u00be\u0003\u0002\u0002",
    "\u0002\u00be\u00bc\u0003\u0002\u0002\u0002\u00be\u00bf\u0003\u0002\u0002",
    "\u0002\u00bf\u00dc\u0003\u0002\u0002\u0002\u00c0\u00c2\u0007\u0019\u0002",
    "\u0002\u00c1\u00c0\u0003\u0002\u0002\u0002\u00c2\u00c3\u0003\u0002\u0002",
    "\u0002\u00c3\u00c1\u0003\u0002\u0002\u0002\u00c3\u00c4\u0003\u0002\u0002",
    "\u0002\u00c4\u00c5\u0003\u0002\u0002\u0002\u00c5\u00dc\u0007\u0007\u0002",
    "\u0002\u00c6\u00c8\u0007\u0006\u0002\u0002\u00c7\u00c9\u0007\u0019\u0002",
    "\u0002\u00c8\u00c7\u0003\u0002\u0002\u0002\u00c9\u00ca\u0003\u0002\u0002",
    "\u0002\u00ca\u00c8\u0003\u0002\u0002\u0002\u00ca\u00cb\u0003\u0002\u0002",
    "\u0002\u00cb\u00cc\u0003\u0002\u0002\u0002\u00cc\u00dc\u0007\u0007\u0002",
    "\u0002\u00cd\u00cf\u0007\u0007\u0002\u0002\u00ce\u00d0\u0007\u0019\u0002",
    "\u0002\u00cf\u00ce\u0003\u0002\u0002\u0002\u00d0\u00d1\u0003\u0002\u0002",
    "\u0002\u00d1\u00cf\u0003\u0002\u0002\u0002\u00d1\u00d2\u0003\u0002\u0002",
    "\u0002\u00d2\u00d3\u0003\u0002\u0002\u0002\u00d3\u00dc\u0007\u0007\u0002",
    "\u0002\u00d4\u00d6\u0007\b\u0002\u0002\u00d5\u00d7\u0007\u0019\u0002",
    "\u0002\u00d6\u00d5\u0003\u0002\u0002\u0002\u00d7\u00d8\u0003\u0002\u0002",
    "\u0002\u00d8\u00d6\u0003\u0002\u0002\u0002\u00d8\u00d9\u0003\u0002\u0002",
    "\u0002\u00d9\u00da\u0003\u0002\u0002\u0002\u00da\u00dc\u0007\u0007\u0002",
    "\u0002\u00db\u00aa\u0003\u0002\u0002\u0002\u00db\u00ae\u0003\u0002\u0002",
    "\u0002\u00db\u00b4\u0003\u0002\u0002\u0002\u00db\u00ba\u0003\u0002\u0002",
    "\u0002\u00db\u00c1\u0003\u0002\u0002\u0002\u00db\u00c6\u0003\u0002\u0002",
    "\u0002\u00db\u00cd\u0003\u0002\u0002\u0002\u00db\u00d4\u0003\u0002\u0002",
    "\u0002\u00dc\t\u0003\u0002\u0002\u0002\u00dd\u00e1\u0007\u0003\u0002",
    "\u0002\u00de\u00e2\u0007\u0019\u0002\u0002\u00df\u00e2\u0005\f\u0007",
    "\u0002\u00e0\u00e2\u0007\u0018\u0002\u0002\u00e1\u00de\u0003\u0002\u0002",
    "\u0002\u00e1\u00df\u0003\u0002\u0002\u0002\u00e1\u00e0\u0003\u0002\u0002",
    "\u0002\u00e2\u00e3\u0003\u0002\u0002\u0002\u00e3\u00e1\u0003\u0002\u0002",
    "\u0002\u00e3\u00e4\u0003\u0002\u0002\u0002\u00e4\u00e5\u0003\u0002\u0002",
    "\u0002\u00e5\u00e6\u0007\u0003\u0002\u0002\u00e6\u000b\u0003\u0002\u0002",
    "\u0002\u00e7\u00e8\t\u0002\u0002\u0002\u00e8\r\u0003\u0002\u0002\u0002",
    "\u00e9\u00ea\u0007\t\u0002\u0002\u00ea\u000f\u0003\u0002\u0002\u0002",
    "\u00eb\u00ec\u0007\u001a\u0002\u0002\u00ec\u0011\u0003\u0002\u0002\u0002",
    "\u00ed\u00f1\u0007\u0003\u0002\u0002\u00ee\u00f2\u0007\u0019\u0002\u0002",
    "\u00ef\u00f2\u0005\f\u0007\u0002\u00f0\u00f2\u0007\u0018\u0002\u0002",
    "\u00f1\u00ee\u0003\u0002\u0002\u0002\u00f1\u00ef\u0003\u0002\u0002\u0002",
    "\u00f1\u00f0\u0003\u0002\u0002\u0002\u00f2\u00f3\u0003\u0002\u0002\u0002",
    "\u00f3\u00f1\u0003\u0002\u0002\u0002\u00f3\u00f4\u0003\u0002\u0002\u0002",
    "\u00f4\u00f5\u0003\u0002\u0002\u0002\u00f5\u00f6\u0007\u0003\u0002\u0002",
    "\u00f6\u0013\u0003\u0002\u0002\u0002\u00f7\u00f8\u0007\u0012\u0002\u0002",
    "\u00f8\u0015\u0003\u0002\u0002\u0002\u00f9\u00fa\u0007\u0013\u0002\u0002",
    "\u00fa\u0017\u0003\u0002\u0002\u0002\u00fb\u00fc\u0007\u0014\u0002\u0002",
    "\u00fc\u0019\u0003\u0002\u0002\u0002\u00fd\u00fe\u0007\u0015\u0002\u0002",
    "\u00fe\u001b\u0003\u0002\u0002\u0002\u00ff\u0100\u0007\u0016\u0002\u0002",
    "\u0100\u001d\u0003\u0002\u0002\u0002\u0101\u0102\u0007\u0017\u0002\u0002",
    "\u0102\u001f\u0003\u0002\u0002\u0002\u0103\u0106\u0005\u0018\r\u0002",
    "\u0104\u0106\u0005\u001a\u000e\u0002\u0105\u0103\u0003\u0002\u0002\u0002",
    "\u0105\u0104\u0003\u0002\u0002\u0002\u0106!\u0003\u0002\u0002\u0002",
    "\u0107\u0109\u0007\u001d\u0002\u0002\u0108\u010a\u0005$\u0013\u0002",
    "\u0109\u0108\u0003\u0002\u0002\u0002\u0109\u010a\u0003\u0002\u0002\u0002",
    "\u010a#\u0003\u0002\u0002\u0002\u010b\u010c\u0005\u0006\u0004\u0002",
    "\u010c\u010d\u0007\u0018\u0002\u0002\u010d%\u0003\u0002\u0002\u0002",
    "\u010e\u0110\u0007\u001e\u0002\u0002\u010f\u0111\u0005(\u0015\u0002",
    "\u0110\u010f\u0003\u0002\u0002\u0002\u0110\u0111\u0003\u0002\u0002\u0002",
    "\u0111\'\u0003\u0002\u0002\u0002\u0112\u0113\u0005\n\u0006\u0002\u0113",
    "\u0115\u0007\u0018\u0002\u0002\u0114\u0116\u0005*\u0016\u0002\u0115",
    "\u0114\u0003\u0002\u0002\u0002\u0115\u0116\u0003\u0002\u0002\u0002\u0116",
    "\u0119\u0003\u0002\u0002\u0002\u0117\u0119\u0005*\u0016\u0002\u0118",
    "\u0112\u0003\u0002\u0002\u0002\u0118\u0117\u0003\u0002\u0002\u0002\u0119",
    ")\u0003\u0002\u0002\u0002\u011a\u011b\u0005\u001e\u0010\u0002\u011b",
    "\u011c\u0005,\u0017\u0002\u011c+\u0003\u0002\u0002\u0002\u011d\u011e",
    "\b\u0017\u0001\u0002\u011e\u011f\u0007\u001b\u0002\u0002\u011f\u0120",
    "\u0005,\u0017\u0002\u0120\u0121\u0007\u001c\u0002\u0002\u0121\u0124",
    "\u0003\u0002\u0002\u0002\u0122\u0124\u0005D#\u0002\u0123\u011d\u0003",
    "\u0002\u0002\u0002\u0123\u0122\u0003\u0002\u0002\u0002\u0124\u012d\u0003",
    "\u0002\u0002\u0002\u0125\u0126\f\u0005\u0002\u0002\u0126\u0127\u0005",
    " \u0011\u0002\u0127\u0128\u0005,\u0017\u0006\u0128\u012c\u0003\u0002",
    "\u0002\u0002\u0129\u012a\f\u0003\u0002\u0002\u012a\u012c\u0007\u0018",
    "\u0002\u0002\u012b\u0125\u0003\u0002\u0002\u0002\u012b\u0129\u0003\u0002",
    "\u0002\u0002\u012c\u012f\u0003\u0002\u0002\u0002\u012d\u012b\u0003\u0002",
    "\u0002\u0002\u012d\u012e\u0003\u0002\u0002\u0002\u012e-\u0003\u0002",
    "\u0002\u0002\u012f\u012d\u0003\u0002\u0002\u0002\u0130\u0131\u0007\u001f",
    "\u0002\u0002\u0131\u0132\u00050\u0019\u0002\u0132/\u0003\u0002\u0002",
    "\u0002\u0133\u0138\u0005\u0016\f\u0002\u0134\u0135\u0005\n\u0006\u0002",
    "\u0135\u0136\u0007\u0018\u0002\u0002\u0136\u0139\u0003\u0002\u0002\u0002",
    "\u0137\u0139\u0007 \u0002\u0002\u0138\u0134\u0003\u0002\u0002\u0002",
    "\u0138\u0137\u0003\u0002\u0002\u0002\u01391\u0003\u0002\u0002\u0002",
    "\u013a\u013b\u0007!\u0002\u0002\u013b\u013c\u00054\u001b\u0002\u013c",
    "3\u0003\u0002\u0002\u0002\u013d\u0142\u0005\u0016\f\u0002\u013e\u013f",
    "\u0005\n\u0006\u0002\u013f\u0140\u0007\u0018\u0002\u0002\u0140\u0143",
    "\u0003\u0002\u0002\u0002\u0141\u0143\u0007\"\u0002\u0002\u0142\u013e",
    "\u0003\u0002\u0002\u0002\u0142\u0141\u0003\u0002\u0002\u0002\u01435",
    "\u0003\u0002\u0002\u0002\u0144\u0145\u0007#\u0002\u0002\u0145\u0146",
    "\u00058\u001d\u0002\u01467\u0003\u0002\u0002\u0002\u0147\u0148\u0005",
    "\u001e\u0010\u0002\u0148\u0149\u0005:\u001e\u0002\u01499\u0003\u0002",
    "\u0002\u0002\u014a\u014b\b\u001e\u0001\u0002\u014b\u014c\u0007\u001b",
    "\u0002\u0002\u014c\u014d\u0005:\u001e\u0002\u014d\u014e\u0007\u001c",
    "\u0002\u0002\u014e\u0155\u0003\u0002\u0002\u0002\u014f\u0153\u0005&",
    "\u0014\u0002\u0150\u0153\u0005R*\u0002\u0151\u0153\u0005J&\u0002\u0152",
    "\u014f\u0003\u0002\u0002\u0002\u0152\u0150\u0003\u0002\u0002\u0002\u0152",
    "\u0151\u0003\u0002\u0002\u0002\u0153\u0155\u0003\u0002\u0002\u0002\u0154",
    "\u014a\u0003\u0002\u0002\u0002\u0154\u0152\u0003\u0002\u0002\u0002\u0155",
    "\u015e\u0003\u0002\u0002\u0002\u0156\u0157\f\u0005\u0002\u0002\u0157",
    "\u0158\u0005 \u0011\u0002\u0158\u0159\u0005:\u001e\u0006\u0159\u015d",
    "\u0003\u0002\u0002\u0002\u015a\u015b\f\u0003\u0002\u0002\u015b\u015d",
    "\u0007\u0018\u0002\u0002\u015c\u0156\u0003\u0002\u0002\u0002\u015c\u015a",
    "\u0003\u0002\u0002\u0002\u015d\u0160\u0003\u0002\u0002\u0002\u015e\u015c",
    "\u0003\u0002\u0002\u0002\u015e\u015f\u0003\u0002\u0002\u0002\u015f;",
    "\u0003\u0002\u0002\u0002\u0160\u015e\u0003\u0002\u0002\u0002\u0161\u0162",
    "\u0007$\u0002\u0002\u0162\u0163\u0005@!\u0002\u0163=\u0003\u0002\u0002",
    "\u0002\u0164\u0165\u0005\u0016\f\u0002\u0165\u0166\u0005h5\u0002\u0166",
    "?\u0003\u0002\u0002\u0002\u0167\u0168\u0005\u001e\u0010\u0002\u0168",
    "\u0169\u0005B\"\u0002\u0169A\u0003\u0002\u0002\u0002\u016a\u016b\b\"",
    "\u0001\u0002\u016b\u016c\u0007\u001b\u0002\u0002\u016c\u016d\u0005B",
    "\"\u0002\u016d\u016e\u0007\u001c\u0002\u0002\u016e\u0174\u0003\u0002",
    "\u0002\u0002\u016f\u0172\u0005&\u0014\u0002\u0170\u0172\u0005J&\u0002",
    "\u0171\u016f\u0003\u0002\u0002\u0002\u0171\u0170\u0003\u0002\u0002\u0002",
    "\u0172\u0174\u0003\u0002\u0002\u0002\u0173\u016a\u0003\u0002\u0002\u0002",
    "\u0173\u0171\u0003\u0002\u0002\u0002\u0174\u017d\u0003\u0002\u0002\u0002",
    "\u0175\u0176\f\u0005\u0002\u0002\u0176\u0177\u0005 \u0011\u0002\u0177",
    "\u0178\u0005B\"\u0006\u0178\u017c\u0003\u0002\u0002\u0002\u0179\u017a",
    "\f\u0003\u0002\u0002\u017a\u017c\u0007\u0018\u0002\u0002\u017b\u0175",
    "\u0003\u0002\u0002\u0002\u017b\u0179\u0003\u0002\u0002\u0002\u017c\u017f",
    "\u0003\u0002\u0002\u0002\u017d\u017b\u0003\u0002\u0002\u0002\u017d\u017e",
    "\u0003\u0002\u0002\u0002\u017eC\u0003\u0002\u0002\u0002\u017f\u017d",
    "\u0003\u0002\u0002\u0002\u0180\u0182\u0007%\u0002\u0002\u0181\u0183",
    "\u0005F$\u0002\u0182\u0181\u0003\u0002\u0002\u0002\u0182\u0183\u0003",
    "\u0002\u0002\u0002\u0183E\u0003\u0002\u0002\u0002\u0184\u0185\u0005",
    "\u001e\u0010\u0002\u0185\u0186\u0005H%\u0002\u0186\u018b\u0003\u0002",
    "\u0002\u0002\u0187\u0188\u0005\n\u0006\u0002\u0188\u0189\u0007\u0018",
    "\u0002\u0002\u0189\u018b\u0003\u0002\u0002\u0002\u018a\u0184\u0003\u0002",
    "\u0002\u0002\u018a\u0187\u0003\u0002\u0002\u0002\u018bG\u0003\u0002",
    "\u0002\u0002\u018c\u018d\b%\u0001\u0002\u018d\u018e\u0007\u001b\u0002",
    "\u0002\u018e\u018f\u0005H%\u0002\u018f\u0190\u0007\u001c\u0002\u0002",
    "\u0190\u0196\u0003\u0002\u0002\u0002\u0191\u0194\u0005R*\u0002\u0192",
    "\u0194\u0005\"\u0012\u0002\u0193\u0191\u0003\u0002\u0002\u0002\u0193",
    "\u0192\u0003\u0002\u0002\u0002\u0194\u0196\u0003\u0002\u0002\u0002\u0195",
    "\u018c\u0003\u0002\u0002\u0002\u0195\u0193\u0003\u0002\u0002\u0002\u0196",
    "\u019f\u0003\u0002\u0002\u0002\u0197\u0198\f\u0005\u0002\u0002\u0198",
    "\u0199\u0005 \u0011\u0002\u0199\u019a\u0005H%\u0006\u019a\u019e\u0003",
    "\u0002\u0002\u0002\u019b\u019c\f\u0003\u0002\u0002\u019c\u019e\u0007",
    "\u0018\u0002\u0002\u019d\u0197\u0003\u0002\u0002\u0002\u019d\u019b\u0003",
    "\u0002\u0002\u0002\u019e\u01a1\u0003\u0002\u0002\u0002\u019f\u019d\u0003",
    "\u0002\u0002\u0002\u019f\u01a0\u0003\u0002\u0002\u0002\u01a0I\u0003",
    "\u0002\u0002\u0002\u01a1\u019f\u0003\u0002\u0002\u0002\u01a2\u01a4\u0007",
    "%\u0002\u0002\u01a3\u01a5\u0005L\'\u0002\u01a4\u01a3\u0003\u0002\u0002",
    "\u0002\u01a4\u01a5\u0003\u0002\u0002\u0002\u01a5K\u0003\u0002\u0002",
    "\u0002\u01a6\u01a7\u0005\n\u0006\u0002\u01a7\u01a9\u0007\u0018\u0002",
    "\u0002\u01a8\u01aa\u0005N(\u0002\u01a9\u01a8\u0003\u0002\u0002\u0002",
    "\u01a9\u01aa\u0003\u0002\u0002\u0002\u01aa\u01ad\u0003\u0002\u0002\u0002",
    "\u01ab\u01ad\u0005N(\u0002\u01ac\u01a6\u0003\u0002\u0002\u0002\u01ac",
    "\u01ab\u0003\u0002\u0002\u0002\u01adM\u0003\u0002\u0002\u0002\u01ae",
    "\u01af\u0005\u001e\u0010\u0002\u01af\u01b0\u0005P)\u0002\u01b0O\u0003",
    "\u0002\u0002\u0002\u01b1\u01b2\b)\u0001\u0002\u01b2\u01b3\u0007\u001b",
    "\u0002\u0002\u01b3\u01b4\u0005P)\u0002\u01b4\u01b5\u0007\u001c\u0002",
    "\u0002\u01b5\u01bc\u0003\u0002\u0002\u0002\u01b6\u01ba\u0005R*\u0002",
    "\u01b7\u01ba\u0005\"\u0012\u0002\u01b8\u01ba\u0005&\u0014\u0002\u01b9",
    "\u01b6\u0003\u0002\u0002\u0002\u01b9\u01b7\u0003\u0002\u0002\u0002\u01b9",
    "\u01b8\u0003\u0002\u0002\u0002\u01ba\u01bc\u0003\u0002\u0002\u0002\u01bb",
    "\u01b1\u0003\u0002\u0002\u0002\u01bb\u01b9\u0003\u0002\u0002\u0002\u01bc",
    "\u01c5\u0003\u0002\u0002\u0002\u01bd\u01be\f\u0005\u0002\u0002\u01be",
    "\u01bf\u0005 \u0011\u0002\u01bf\u01c0\u0005P)\u0006\u01c0\u01c4\u0003",
    "\u0002\u0002\u0002\u01c1\u01c2\f\u0003\u0002\u0002\u01c2\u01c4\u0007",
    "\u0018\u0002\u0002\u01c3\u01bd\u0003\u0002\u0002\u0002\u01c3\u01c1\u0003",
    "\u0002\u0002\u0002\u01c4\u01c7\u0003\u0002\u0002\u0002\u01c5\u01c3\u0003",
    "\u0002\u0002\u0002\u01c5\u01c6\u0003\u0002\u0002\u0002\u01c6Q\u0003",
    "\u0002\u0002\u0002\u01c7\u01c5\u0003\u0002\u0002\u0002\u01c8\u01ca\u0007",
    "&\u0002\u0002\u01c9\u01cb\u0005T+\u0002\u01ca\u01c9\u0003\u0002\u0002",
    "\u0002\u01ca\u01cb\u0003\u0002\u0002\u0002\u01cbS\u0003\u0002\u0002",
    "\u0002\u01cc\u01cd\u0005\n\u0006\u0002\u01cd\u01ce\u0007\u0018\u0002",
    "\u0002\u01ce\u01d3\u0003\u0002\u0002\u0002\u01cf\u01d0\u0005\u0006\u0004",
    "\u0002\u01d0\u01d1\u0007\u0018\u0002\u0002\u01d1\u01d3\u0003\u0002\u0002",
    "\u0002\u01d2\u01cc\u0003\u0002\u0002\u0002\u01d2\u01cf\u0003\u0002\u0002",
    "\u0002\u01d3U\u0003\u0002\u0002\u0002\u01d4\u01d5\u0007\'\u0002\u0002",
    "\u01d5\u01d6\u0005X-\u0002\u01d6W\u0003\u0002\u0002\u0002\u01d7\u01d8",
    "\u0005\u001e\u0010\u0002\u01d8\u01d9\u0005Z.\u0002\u01d9Y\u0003\u0002",
    "\u0002\u0002\u01da\u01db\b.\u0001\u0002\u01db\u01dc\u0007\u001b\u0002",
    "\u0002\u01dc\u01dd\u0005Z.\u0002\u01dd\u01de\u0007\u001c\u0002\u0002",
    "\u01de\u01e4\u0003\u0002\u0002\u0002\u01df\u01e2\u0005&\u0014\u0002",
    "\u01e0\u01e2\u0005R*\u0002\u01e1\u01df\u0003\u0002\u0002\u0002\u01e1",
    "\u01e0\u0003\u0002\u0002\u0002\u01e2\u01e4\u0003\u0002\u0002\u0002\u01e3",
    "\u01da\u0003\u0002\u0002\u0002\u01e3\u01e1\u0003\u0002\u0002\u0002\u01e4",
    "\u01ed\u0003\u0002\u0002\u0002\u01e5\u01e6\f\u0005\u0002\u0002\u01e6",
    "\u01e7\u0005 \u0011\u0002\u01e7\u01e8\u0005Z.\u0006\u01e8\u01ec\u0003",
    "\u0002\u0002\u0002\u01e9\u01ea\f\u0003\u0002\u0002\u01ea\u01ec\u0007",
    "\u0018\u0002\u0002\u01eb\u01e5\u0003\u0002\u0002\u0002\u01eb\u01e9\u0003",
    "\u0002\u0002\u0002\u01ec\u01ef\u0003\u0002\u0002\u0002\u01ed\u01eb\u0003",
    "\u0002\u0002\u0002\u01ed\u01ee\u0003\u0002\u0002\u0002\u01ee[\u0003",
    "\u0002\u0002\u0002\u01ef\u01ed\u0003\u0002\u0002\u0002\u01f0\u01f2\u0007",
    "(\u0002\u0002\u01f1\u01f3\u0005^0\u0002\u01f2\u01f1\u0003\u0002\u0002",
    "\u0002\u01f2\u01f3\u0003\u0002\u0002\u0002\u01f3]\u0003\u0002\u0002",
    "\u0002\u01f4\u01f5\u0005\u001e\u0010\u0002\u01f5\u01f6\u0005`1\u0002",
    "\u01f6_\u0003\u0002\u0002\u0002\u01f7\u01f8\b1\u0001\u0002\u01f8\u01f9",
    "\u0007\u001b\u0002\u0002\u01f9\u01fa\u0005`1\u0002\u01fa\u01fb\u0007",
    "\u001c\u0002\u0002\u01fb\u01fe\u0003\u0002\u0002\u0002\u01fc\u01fe\u0005",
    "b2\u0002\u01fd\u01f7\u0003\u0002\u0002\u0002\u01fd\u01fc\u0003\u0002",
    "\u0002\u0002\u01fe\u0207\u0003\u0002\u0002\u0002\u01ff\u0200\f\u0005",
    "\u0002\u0002\u0200\u0201\u0005 \u0011\u0002\u0201\u0202\u0005`1\u0006",
    "\u0202\u0206\u0003\u0002\u0002\u0002\u0203\u0204\f\u0003\u0002\u0002",
    "\u0204\u0206\u0007\u0018\u0002\u0002\u0205\u01ff\u0003\u0002\u0002\u0002",
    "\u0205\u0203\u0003\u0002\u0002\u0002\u0206\u0209\u0003\u0002\u0002\u0002",
    "\u0207\u0205\u0003\u0002\u0002\u0002\u0207\u0208\u0003\u0002\u0002\u0002",
    "\u0208a\u0003\u0002\u0002\u0002\u0209\u0207\u0003\u0002\u0002\u0002",
    "\u020a\u020b\u0007)\u0002\u0002\u020b\u020c\u0005d3\u0002\u020cc\u0003",
    "\u0002\u0002\u0002\u020d\u020e\u0005\u001e\u0010\u0002\u020e\u020f\u0005",
    "f4\u0002\u020f\u0214\u0003\u0002\u0002\u0002\u0210\u0211\u0005\n\u0006",
    "\u0002\u0211\u0212\u0007\u0018\u0002\u0002\u0212\u0214\u0003\u0002\u0002",
    "\u0002\u0213\u020d\u0003\u0002\u0002\u0002\u0213\u0210\u0003\u0002\u0002",
    "\u0002\u0214e\u0003\u0002\u0002\u0002\u0215\u0216\b4\u0001\u0002\u0216",
    "\u0217\u0007\u001b\u0002\u0002\u0217\u0218\u0005f4\u0002\u0218\u0219",
    "\u0007\u001c\u0002\u0002\u0219\u021f\u0003\u0002\u0002\u0002\u021a\u021d",
    "\u0005R*\u0002\u021b\u021d\u0005\"\u0012\u0002\u021c\u021a\u0003\u0002",
    "\u0002\u0002\u021c\u021b\u0003\u0002\u0002\u0002\u021d\u021f\u0003\u0002",
    "\u0002\u0002\u021e\u0215\u0003\u0002\u0002\u0002\u021e\u021c\u0003\u0002",
    "\u0002\u0002\u021f\u0228\u0003\u0002\u0002\u0002\u0220\u0221\f\u0005",
    "\u0002\u0002\u0221\u0222\u0005 \u0011\u0002\u0222\u0223\u0005f4\u0006",
    "\u0223\u0227\u0003\u0002\u0002\u0002\u0224\u0225\f\u0003\u0002\u0002",
    "\u0225\u0227\u0007\u0018\u0002\u0002\u0226\u0220\u0003\u0002\u0002\u0002",
    "\u0226\u0224\u0003\u0002\u0002\u0002\u0227\u022a\u0003\u0002\u0002\u0002",
    "\u0228\u0226\u0003\u0002\u0002\u0002\u0228\u0229\u0003\u0002\u0002\u0002",
    "\u0229g\u0003\u0002\u0002\u0002\u022a\u0228\u0003\u0002\u0002\u0002",
    "\u022b\u022d\u0007*\u0002\u0002\u022c\u022e\u0005j6\u0002\u022d\u022c",
    "\u0003\u0002\u0002\u0002\u022d\u022e\u0003\u0002\u0002\u0002\u022ei",
    "\u0003\u0002\u0002\u0002\u022f\u0230\u0005\u001e\u0010\u0002\u0230\u0231",
    "\u0005l7\u0002\u0231k\u0003\u0002\u0002\u0002\u0232\u0233\b7\u0001\u0002",
    "\u0233\u0234\u0007\u001b\u0002\u0002\u0234\u0235\u0005l7\u0002\u0235",
    "\u0236\u0007\u001c\u0002\u0002\u0236\u0242\u0003\u0002\u0002\u0002\u0237",
    "\u0240\u0005&\u0014\u0002\u0238\u0240\u0005.\u0018\u0002\u0239\u0240",
    "\u00052\u001a\u0002\u023a\u0240\u00056\u001c\u0002\u023b\u0240\u0005",
    "<\u001f\u0002\u023c\u0240\u0005V,\u0002\u023d\u0240\u0005\\/\u0002\u023e",
    "\u0240\u0005n8\u0002\u023f\u0237\u0003\u0002\u0002\u0002\u023f\u0238",
    "\u0003\u0002\u0002\u0002\u023f\u0239\u0003\u0002\u0002\u0002\u023f\u023a",
    "\u0003\u0002\u0002\u0002\u023f\u023b\u0003\u0002\u0002\u0002\u023f\u023c",
    "\u0003\u0002\u0002\u0002\u023f\u023d\u0003\u0002\u0002\u0002\u023f\u023e",
    "\u0003\u0002\u0002\u0002\u0240\u0242\u0003\u0002\u0002\u0002\u0241\u0232",
    "\u0003\u0002\u0002\u0002\u0241\u023f\u0003\u0002\u0002\u0002\u0242\u024b",
    "\u0003\u0002\u0002\u0002\u0243\u0244\f\u0005\u0002\u0002\u0244\u0245",
    "\u0005 \u0011\u0002\u0245\u0246\u0005l7\u0006\u0246\u024a\u0003\u0002",
    "\u0002\u0002\u0247\u0248\f\u0003\u0002\u0002\u0248\u024a\u0007\u0018",
    "\u0002\u0002\u0249\u0243\u0003\u0002\u0002\u0002\u0249\u0247\u0003\u0002",
    "\u0002\u0002\u024a\u024d\u0003\u0002\u0002\u0002\u024b\u0249\u0003\u0002",
    "\u0002\u0002\u024b\u024c\u0003\u0002\u0002\u0002\u024cm\u0003\u0002",
    "\u0002\u0002\u024d\u024b\u0003\u0002\u0002\u0002\u024e\u024f\u0007+",
    "\u0002\u0002\u024fo\u0003\u0002\u0002\u0002Iswz\u007f\u0098\u00a1\u00a3",
    "\u00ac\u00b2\u00b8\u00be\u00c3\u00ca\u00d1\u00d8\u00db\u00e1\u00e3\u00f1",
    "\u00f3\u0105\u0109\u0110\u0115\u0118\u0123\u012b\u012d\u0138\u0142\u0152",
    "\u0154\u015c\u015e\u0171\u0173\u017b\u017d\u0182\u018a\u0193\u0195\u019d",
    "\u019f\u01a4\u01a9\u01ac\u01b9\u01bb\u01c3\u01c5\u01ca\u01d2\u01e1\u01e3",
    "\u01eb\u01ed\u01f2\u01fd\u0205\u0207\u0213\u021c\u021e\u0226\u0228\u022d",
    "\u023f\u0241\u0249\u024b"].join("");


const atn = new antlr4.atn.ATNDeserializer().deserialize(serializedATN);

const decisionsToDFA = atn.decisionToState.map( (ds, index) => new antlr4.dfa.DFA(ds, index) );

const sharedContextCache = new antlr4.PredictionContextCache();

export default class RulepadGrammarParser extends antlr4.Parser {

    static grammarFileName = "RulepadGrammar.g4";
    static literalNames = [ null, "'\"'", "'||'", "'&&'", "'!'", "'...'", 
                            "'!...'", "'.'", "'='", "'>'", "'<'", "'''", 
                            "'&'", "'|'", "'['", "']'", "'must '", "'of '", 
                            "'and '", "'or '", "'have '", "'with '", null, 
                            null, null, "'('", "')'", "'name '", "'annotation '", 
                            "'extension '", "'Superclass'", "'implementation '", 
                            "'Interface '", null, "'constructor '", "'parameter '", 
                            "'type '", null, "'configuration file '", "'property '", 
                            "'class '", "'bean declaration '" ];
    static symbolicNames = [ null, null, null, null, null, null, null, null, 
                             null, null, null, null, null, null, null, null, 
                             null, null, null, null, null, null, "SPACE", 
                             "Alphabet", "NL", "LPAREN", "RPAREN", "NAME", 
                             "ANNOTATION", "EXTENSION", "SUPERCLASS", "IMPLEMENTATION", 
                             "INTERFACE", "FUNCTION", "CONSTRUCTOR", "PARAMETER", 
                             "TYPES", "DeclarationStatement", "ConfigurationFile", 
                             "CONFIGURATION_PROPERTIES", "CLASSES", "BEAN_DECL" ];
    static ruleNames = [ "inputSentence", "mustClause", "words", "word", 
                         "combinatorialWords", "symbols", "end", "emptyLine", 
                         "comments", "must", "of", "and_", "or_", "have", 
                         "withWord", "binary", "names", "nameCondition", 
                         "annotations", "annotationCondition", "annotationConditionTransition", 
                         "annotationExpression", "extensions", "extensionCondition", 
                         "implementations", "implementationCondition", "functions", 
                         "functionCondition", "functionExpression", "constructors", 
                         "constructorOf", "constructorCondition", "constructorExpression", 
                         "parameters", "parameterCondition", "parameterExpression", 
                         "functionParameters", "functionParameterCondition", 
                         "functionParameterConditionTransition", "functionParameterExpression", 
                         "types", "typeCondition", "declarationStatements", 
                         "declarationStatementCondition", "declarationStatementExpression", 
                         "configurationFiles", "configurationFileCondition", 
                         "configurationFileExpression", "configurationProperties", 
                         "configurationPropertyCondition", "configurationPropertyExpression", 
                         "classes", "classCondition", "classExpression", 
                         "beans" ];

    constructor(input) {
        super(input);
        this._interp = new antlr4.atn.ParserATNSimulator(this, atn, decisionsToDFA, sharedContextCache);
        this.ruleNames = RulepadGrammarParser.ruleNames;
        this.literalNames = RulepadGrammarParser.literalNames;
        this.symbolicNames = RulepadGrammarParser.symbolicNames;
    }

    get atn() {
        return atn;
    }

    sempred(localctx, ruleIndex, predIndex) {
    	switch(ruleIndex) {
    	case 21:
    	    		return this.annotationExpression_sempred(localctx, predIndex);
    	case 28:
    	    		return this.functionExpression_sempred(localctx, predIndex);
    	case 32:
    	    		return this.constructorExpression_sempred(localctx, predIndex);
    	case 35:
    	    		return this.parameterExpression_sempred(localctx, predIndex);
    	case 39:
    	    		return this.functionParameterExpression_sempred(localctx, predIndex);
    	case 44:
    	    		return this.declarationStatementExpression_sempred(localctx, predIndex);
    	case 47:
    	    		return this.configurationFileExpression_sempred(localctx, predIndex);
    	case 50:
    	    		return this.configurationPropertyExpression_sempred(localctx, predIndex);
    	case 53:
    	    		return this.classExpression_sempred(localctx, predIndex);
        default:
            throw "No predicate with index:" + ruleIndex;
       }
    }

    annotationExpression_sempred(localctx, predIndex) {
    	switch(predIndex) {
    		case 0:
    			return this.precpred(this._ctx, 3);
    		case 1:
    			return this.precpred(this._ctx, 1);
    		default:
    			throw "No predicate with index:" + predIndex;
    	}
    };

    functionExpression_sempred(localctx, predIndex) {
    	switch(predIndex) {
    		case 2:
    			return this.precpred(this._ctx, 3);
    		case 3:
    			return this.precpred(this._ctx, 1);
    		default:
    			throw "No predicate with index:" + predIndex;
    	}
    };

    constructorExpression_sempred(localctx, predIndex) {
    	switch(predIndex) {
    		case 4:
    			return this.precpred(this._ctx, 3);
    		case 5:
    			return this.precpred(this._ctx, 1);
    		default:
    			throw "No predicate with index:" + predIndex;
    	}
    };

    parameterExpression_sempred(localctx, predIndex) {
    	switch(predIndex) {
    		case 6:
    			return this.precpred(this._ctx, 3);
    		case 7:
    			return this.precpred(this._ctx, 1);
    		default:
    			throw "No predicate with index:" + predIndex;
    	}
    };

    functionParameterExpression_sempred(localctx, predIndex) {
    	switch(predIndex) {
    		case 8:
    			return this.precpred(this._ctx, 3);
    		case 9:
    			return this.precpred(this._ctx, 1);
    		default:
    			throw "No predicate with index:" + predIndex;
    	}
    };

    declarationStatementExpression_sempred(localctx, predIndex) {
    	switch(predIndex) {
    		case 10:
    			return this.precpred(this._ctx, 3);
    		case 11:
    			return this.precpred(this._ctx, 1);
    		default:
    			throw "No predicate with index:" + predIndex;
    	}
    };

    configurationFileExpression_sempred(localctx, predIndex) {
    	switch(predIndex) {
    		case 12:
    			return this.precpred(this._ctx, 3);
    		case 13:
    			return this.precpred(this._ctx, 1);
    		default:
    			throw "No predicate with index:" + predIndex;
    	}
    };

    configurationPropertyExpression_sempred(localctx, predIndex) {
    	switch(predIndex) {
    		case 14:
    			return this.precpred(this._ctx, 3);
    		case 15:
    			return this.precpred(this._ctx, 1);
    		default:
    			throw "No predicate with index:" + predIndex;
    	}
    };

    classExpression_sempred(localctx, predIndex) {
    	switch(predIndex) {
    		case 16:
    			return this.precpred(this._ctx, 3);
    		case 17:
    			return this.precpred(this._ctx, 1);
    		default:
    			throw "No predicate with index:" + predIndex;
    	}
    };




	inputSentence() {
	    let localctx = new InputSentenceContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 0, RulepadGrammarParser.RULE_inputSentence);
	    var _la = 0; // Token type
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 117;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.EOF:
	        case RulepadGrammarParser.T__6:
	        case RulepadGrammarParser.NL:
	            this.state = 113;
	            this._errHandler.sync(this);
	            let _alt = this._interp.adaptivePredict(this._input,0,this._ctx)
	            while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
	                if(_alt===1) {
	                    this.state = 110;
	                    this.emptyLine(); 
	                }
	                this.state = 115;
	                this._errHandler.sync(this);
	                _alt = this._interp.adaptivePredict(this._input,0,this._ctx);
	            }

	            break;
	        case RulepadGrammarParser.FUNCTION:
	        case RulepadGrammarParser.CONSTRUCTOR:
	        case RulepadGrammarParser.DeclarationStatement:
	        case RulepadGrammarParser.CLASSES:
	            this.state = 116;
	            this.mustClause();
	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	        this.state = 120;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        if(_la===RulepadGrammarParser.T__6) {
	            this.state = 119;
	            this.end();
	        }

	        this.state = 125;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        while(_la===RulepadGrammarParser.NL) {
	            this.state = 122;
	            this.match(RulepadGrammarParser.NL);
	            this.state = 127;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	        }
	        this.state = 128;
	        this.match(RulepadGrammarParser.EOF);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	mustClause() {
	    let localctx = new MustClauseContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 2, RulepadGrammarParser.RULE_mustClause);
	    try {
	        this.state = 150;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.FUNCTION:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 130;
	            this.functions();
	            this.state = 131;
	            this.must();
	            this.state = 132;
	            this.have();
	            this.state = 133;
	            this.functionExpression(0);
	            break;
	        case RulepadGrammarParser.CONSTRUCTOR:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 135;
	            this.constructors();
	            this.state = 136;
	            this.must();
	            this.state = 137;
	            this.have();
	            this.state = 138;
	            this.constructorExpression(0);
	            break;
	        case RulepadGrammarParser.CLASSES:
	            this.enterOuterAlt(localctx, 3);
	            this.state = 140;
	            this.classes();
	            this.state = 141;
	            this.must();
	            this.state = 142;
	            this.have();
	            this.state = 143;
	            this.classExpression(0);
	            break;
	        case RulepadGrammarParser.DeclarationStatement:
	            this.enterOuterAlt(localctx, 4);
	            this.state = 145;
	            this.declarationStatements();
	            this.state = 146;
	            this.must();
	            this.state = 147;
	            this.have();
	            this.state = 148;
	            this.declarationStatementExpression(0);
	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	words() {
	    let localctx = new WordsContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 4, RulepadGrammarParser.RULE_words);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 152;
	        this.match(RulepadGrammarParser.T__0);
	        this.state = 161;
	        this._errHandler.sync(this);
	        let _alt = this._interp.adaptivePredict(this._input,6,this._ctx)
	        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
	            if(_alt===1) {
	                this.state = 159;
	                this._errHandler.sync(this);
	                var la_ = this._interp.adaptivePredict(this._input,5,this._ctx);
	                switch(la_) {
	                case 1:
	                    this.state = 153;
	                    this.word();
	                    this.state = 154;
	                    this.match(RulepadGrammarParser.T__1);
	                    break;

	                case 2:
	                    this.state = 156;
	                    this.word();
	                    this.state = 157;
	                    this.match(RulepadGrammarParser.T__2);
	                    break;

	                } 
	            }
	            this.state = 163;
	            this._errHandler.sync(this);
	            _alt = this._interp.adaptivePredict(this._input,6,this._ctx);
	        }

	        this.state = 164;
	        this.word();
	        this.state = 165;
	        this.match(RulepadGrammarParser.T__0);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	word() {
	    let localctx = new WordContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 6, RulepadGrammarParser.RULE_word);
	    var _la = 0; // Token type
	    try {
	        this.state = 217;
	        this._errHandler.sync(this);
	        var la_ = this._interp.adaptivePredict(this._input,15,this._ctx);
	        switch(la_) {
	        case 1:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 168; 
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            do {
	                this.state = 167;
	                this.match(RulepadGrammarParser.Alphabet);
	                this.state = 170; 
	                this._errHandler.sync(this);
	                _la = this._input.LA(1);
	            } while(_la===RulepadGrammarParser.Alphabet);
	            break;

	        case 2:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 172;
	            this.match(RulepadGrammarParser.T__3);
	            this.state = 174; 
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            do {
	                this.state = 173;
	                this.match(RulepadGrammarParser.Alphabet);
	                this.state = 176; 
	                this._errHandler.sync(this);
	                _la = this._input.LA(1);
	            } while(_la===RulepadGrammarParser.Alphabet);
	            break;

	        case 3:
	            this.enterOuterAlt(localctx, 3);
	            this.state = 178;
	            this.match(RulepadGrammarParser.T__4);
	            this.state = 180; 
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            do {
	                this.state = 179;
	                this.match(RulepadGrammarParser.Alphabet);
	                this.state = 182; 
	                this._errHandler.sync(this);
	                _la = this._input.LA(1);
	            } while(_la===RulepadGrammarParser.Alphabet);
	            break;

	        case 4:
	            this.enterOuterAlt(localctx, 4);
	            this.state = 184;
	            this.match(RulepadGrammarParser.T__5);
	            this.state = 186; 
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            do {
	                this.state = 185;
	                this.match(RulepadGrammarParser.Alphabet);
	                this.state = 188; 
	                this._errHandler.sync(this);
	                _la = this._input.LA(1);
	            } while(_la===RulepadGrammarParser.Alphabet);
	            break;

	        case 5:
	            this.enterOuterAlt(localctx, 5);
	            this.state = 191; 
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            do {
	                this.state = 190;
	                this.match(RulepadGrammarParser.Alphabet);
	                this.state = 193; 
	                this._errHandler.sync(this);
	                _la = this._input.LA(1);
	            } while(_la===RulepadGrammarParser.Alphabet);
	            this.state = 195;
	            this.match(RulepadGrammarParser.T__4);
	            break;

	        case 6:
	            this.enterOuterAlt(localctx, 6);
	            this.state = 196;
	            this.match(RulepadGrammarParser.T__3);
	            this.state = 198; 
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            do {
	                this.state = 197;
	                this.match(RulepadGrammarParser.Alphabet);
	                this.state = 200; 
	                this._errHandler.sync(this);
	                _la = this._input.LA(1);
	            } while(_la===RulepadGrammarParser.Alphabet);
	            this.state = 202;
	            this.match(RulepadGrammarParser.T__4);
	            break;

	        case 7:
	            this.enterOuterAlt(localctx, 7);
	            this.state = 203;
	            this.match(RulepadGrammarParser.T__4);
	            this.state = 205; 
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            do {
	                this.state = 204;
	                this.match(RulepadGrammarParser.Alphabet);
	                this.state = 207; 
	                this._errHandler.sync(this);
	                _la = this._input.LA(1);
	            } while(_la===RulepadGrammarParser.Alphabet);
	            this.state = 209;
	            this.match(RulepadGrammarParser.T__4);
	            break;

	        case 8:
	            this.enterOuterAlt(localctx, 8);
	            this.state = 210;
	            this.match(RulepadGrammarParser.T__5);
	            this.state = 212; 
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            do {
	                this.state = 211;
	                this.match(RulepadGrammarParser.Alphabet);
	                this.state = 214; 
	                this._errHandler.sync(this);
	                _la = this._input.LA(1);
	            } while(_la===RulepadGrammarParser.Alphabet);
	            this.state = 216;
	            this.match(RulepadGrammarParser.T__4);
	            break;

	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	combinatorialWords() {
	    let localctx = new CombinatorialWordsContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 8, RulepadGrammarParser.RULE_combinatorialWords);
	    var _la = 0; // Token type
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 219;
	        this.match(RulepadGrammarParser.T__0);
	        this.state = 223; 
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        do {
	            this.state = 223;
	            this._errHandler.sync(this);
	            switch(this._input.LA(1)) {
	            case RulepadGrammarParser.Alphabet:
	                this.state = 220;
	                this.match(RulepadGrammarParser.Alphabet);
	                break;
	            case RulepadGrammarParser.T__6:
	            case RulepadGrammarParser.T__7:
	            case RulepadGrammarParser.T__8:
	            case RulepadGrammarParser.T__9:
	            case RulepadGrammarParser.T__10:
	            case RulepadGrammarParser.T__11:
	            case RulepadGrammarParser.T__12:
	            case RulepadGrammarParser.T__13:
	            case RulepadGrammarParser.T__14:
	            case RulepadGrammarParser.LPAREN:
	            case RulepadGrammarParser.RPAREN:
	                this.state = 221;
	                this.symbols();
	                break;
	            case RulepadGrammarParser.SPACE:
	                this.state = 222;
	                this.match(RulepadGrammarParser.SPACE);
	                break;
	            default:
	                throw new antlr4.error.NoViableAltException(this);
	            }
	            this.state = 225; 
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	        } while((((_la) & ~0x1f) == 0 && ((1 << _la) & ((1 << RulepadGrammarParser.T__6) | (1 << RulepadGrammarParser.T__7) | (1 << RulepadGrammarParser.T__8) | (1 << RulepadGrammarParser.T__9) | (1 << RulepadGrammarParser.T__10) | (1 << RulepadGrammarParser.T__11) | (1 << RulepadGrammarParser.T__12) | (1 << RulepadGrammarParser.T__13) | (1 << RulepadGrammarParser.T__14) | (1 << RulepadGrammarParser.SPACE) | (1 << RulepadGrammarParser.Alphabet) | (1 << RulepadGrammarParser.LPAREN) | (1 << RulepadGrammarParser.RPAREN))) !== 0));
	        this.state = 227;
	        this.match(RulepadGrammarParser.T__0);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	symbols() {
	    let localctx = new SymbolsContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 10, RulepadGrammarParser.RULE_symbols);
	    var _la = 0; // Token type
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 229;
	        _la = this._input.LA(1);
	        if(!((((_la) & ~0x1f) == 0 && ((1 << _la) & ((1 << RulepadGrammarParser.T__6) | (1 << RulepadGrammarParser.T__7) | (1 << RulepadGrammarParser.T__8) | (1 << RulepadGrammarParser.T__9) | (1 << RulepadGrammarParser.T__10) | (1 << RulepadGrammarParser.T__11) | (1 << RulepadGrammarParser.T__12) | (1 << RulepadGrammarParser.T__13) | (1 << RulepadGrammarParser.T__14) | (1 << RulepadGrammarParser.LPAREN) | (1 << RulepadGrammarParser.RPAREN))) !== 0))) {
	        this._errHandler.recoverInline(this);
	        }
	        else {
	        	this._errHandler.reportMatch(this);
	            this.consume();
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	end() {
	    let localctx = new EndContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 12, RulepadGrammarParser.RULE_end);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 231;
	        this.match(RulepadGrammarParser.T__6);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	emptyLine() {
	    let localctx = new EmptyLineContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 14, RulepadGrammarParser.RULE_emptyLine);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 233;
	        this.match(RulepadGrammarParser.NL);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	comments() {
	    let localctx = new CommentsContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 16, RulepadGrammarParser.RULE_comments);
	    var _la = 0; // Token type
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 235;
	        this.match(RulepadGrammarParser.T__0);
	        this.state = 239; 
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        do {
	            this.state = 239;
	            this._errHandler.sync(this);
	            switch(this._input.LA(1)) {
	            case RulepadGrammarParser.Alphabet:
	                this.state = 236;
	                this.match(RulepadGrammarParser.Alphabet);
	                break;
	            case RulepadGrammarParser.T__6:
	            case RulepadGrammarParser.T__7:
	            case RulepadGrammarParser.T__8:
	            case RulepadGrammarParser.T__9:
	            case RulepadGrammarParser.T__10:
	            case RulepadGrammarParser.T__11:
	            case RulepadGrammarParser.T__12:
	            case RulepadGrammarParser.T__13:
	            case RulepadGrammarParser.T__14:
	            case RulepadGrammarParser.LPAREN:
	            case RulepadGrammarParser.RPAREN:
	                this.state = 237;
	                this.symbols();
	                break;
	            case RulepadGrammarParser.SPACE:
	                this.state = 238;
	                this.match(RulepadGrammarParser.SPACE);
	                break;
	            default:
	                throw new antlr4.error.NoViableAltException(this);
	            }
	            this.state = 241; 
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	        } while((((_la) & ~0x1f) == 0 && ((1 << _la) & ((1 << RulepadGrammarParser.T__6) | (1 << RulepadGrammarParser.T__7) | (1 << RulepadGrammarParser.T__8) | (1 << RulepadGrammarParser.T__9) | (1 << RulepadGrammarParser.T__10) | (1 << RulepadGrammarParser.T__11) | (1 << RulepadGrammarParser.T__12) | (1 << RulepadGrammarParser.T__13) | (1 << RulepadGrammarParser.T__14) | (1 << RulepadGrammarParser.SPACE) | (1 << RulepadGrammarParser.Alphabet) | (1 << RulepadGrammarParser.LPAREN) | (1 << RulepadGrammarParser.RPAREN))) !== 0));
	        this.state = 243;
	        this.match(RulepadGrammarParser.T__0);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	must() {
	    let localctx = new MustContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 18, RulepadGrammarParser.RULE_must);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 245;
	        this.match(RulepadGrammarParser.T__15);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	of() {
	    let localctx = new OfContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 20, RulepadGrammarParser.RULE_of);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 247;
	        this.match(RulepadGrammarParser.T__16);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	and_() {
	    let localctx = new And_Context(this, this._ctx, this.state);
	    this.enterRule(localctx, 22, RulepadGrammarParser.RULE_and_);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 249;
	        this.match(RulepadGrammarParser.T__17);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	or_() {
	    let localctx = new Or_Context(this, this._ctx, this.state);
	    this.enterRule(localctx, 24, RulepadGrammarParser.RULE_or_);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 251;
	        this.match(RulepadGrammarParser.T__18);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	have() {
	    let localctx = new HaveContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 26, RulepadGrammarParser.RULE_have);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 253;
	        this.match(RulepadGrammarParser.T__19);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	withWord() {
	    let localctx = new WithWordContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 28, RulepadGrammarParser.RULE_withWord);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 255;
	        this.match(RulepadGrammarParser.T__20);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	binary() {
	    let localctx = new BinaryContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 30, RulepadGrammarParser.RULE_binary);
	    try {
	        this.state = 259;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.T__17:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 257;
	            this.and_();
	            break;
	        case RulepadGrammarParser.T__18:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 258;
	            this.or_();
	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	names() {
	    let localctx = new NamesContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 32, RulepadGrammarParser.RULE_names);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 261;
	        this.match(RulepadGrammarParser.NAME);
	        this.state = 263;
	        this._errHandler.sync(this);
	        var la_ = this._interp.adaptivePredict(this._input,21,this._ctx);
	        if(la_===1) {
	            this.state = 262;
	            this.nameCondition();

	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	nameCondition() {
	    let localctx = new NameConditionContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 34, RulepadGrammarParser.RULE_nameCondition);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 265;
	        this.words();
	        this.state = 266;
	        this.match(RulepadGrammarParser.SPACE);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	annotations() {
	    let localctx = new AnnotationsContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 36, RulepadGrammarParser.RULE_annotations);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 268;
	        this.match(RulepadGrammarParser.ANNOTATION);
	        this.state = 270;
	        this._errHandler.sync(this);
	        var la_ = this._interp.adaptivePredict(this._input,22,this._ctx);
	        if(la_===1) {
	            this.state = 269;
	            this.annotationCondition();

	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	annotationCondition() {
	    let localctx = new AnnotationConditionContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 38, RulepadGrammarParser.RULE_annotationCondition);
	    try {
	        this.state = 278;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.T__0:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 272;
	            this.combinatorialWords();
	            this.state = 273;
	            this.match(RulepadGrammarParser.SPACE);
	            this.state = 275;
	            this._errHandler.sync(this);
	            var la_ = this._interp.adaptivePredict(this._input,23,this._ctx);
	            if(la_===1) {
	                this.state = 274;
	                this.annotationConditionTransition();

	            }
	            break;
	        case RulepadGrammarParser.T__20:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 277;
	            this.annotationConditionTransition();
	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	annotationConditionTransition() {
	    let localctx = new AnnotationConditionTransitionContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 40, RulepadGrammarParser.RULE_annotationConditionTransition);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 280;
	        this.withWord();
	        this.state = 281;
	        this.annotationExpression(0);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	annotationExpression(_p) {
		if(_p===undefined) {
		    _p = 0;
		}
	    const _parentctx = this._ctx;
	    const _parentState = this.state;
	    let localctx = new AnnotationExpressionContext(this, this._ctx, _parentState);
	    let _prevctx = localctx;
	    const _startState = 42;
	    this.enterRecursionRule(localctx, 42, RulepadGrammarParser.RULE_annotationExpression, _p);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 289;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.LPAREN:
	            this.state = 284;
	            this.match(RulepadGrammarParser.LPAREN);
	            this.state = 285;
	            this.annotationExpression(0);
	            this.state = 286;
	            this.match(RulepadGrammarParser.RPAREN);
	            break;
	        case RulepadGrammarParser.PARAMETER:
	            this.state = 288;
	            this.parameters();
	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	        this._ctx.stop = this._input.LT(-1);
	        this.state = 299;
	        this._errHandler.sync(this);
	        let _alt = this._interp.adaptivePredict(this._input,27,this._ctx)
	        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
	            if(_alt===1) {
	                if(this._parseListeners!==null) {
	                    this.triggerExitRuleEvent();
	                }
	                _prevctx = localctx;
	                this.state = 297;
	                this._errHandler.sync(this);
	                var la_ = this._interp.adaptivePredict(this._input,26,this._ctx);
	                switch(la_) {
	                case 1:
	                    localctx = new AnnotationExpressionContext(this, _parentctx, _parentState);
	                    localctx.left = _prevctx;
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_annotationExpression);
	                    this.state = 291;
	                    if (!( this.precpred(this._ctx, 3))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 3)");
	                    }
	                    this.state = 292;
	                    localctx.op = this.binary();
	                    this.state = 293;
	                    localctx.right = this.annotationExpression(4);
	                    break;

	                case 2:
	                    localctx = new AnnotationExpressionContext(this, _parentctx, _parentState);
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_annotationExpression);
	                    this.state = 295;
	                    if (!( this.precpred(this._ctx, 1))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 1)");
	                    }
	                    this.state = 296;
	                    this.match(RulepadGrammarParser.SPACE);
	                    break;

	                } 
	            }
	            this.state = 301;
	            this._errHandler.sync(this);
	            _alt = this._interp.adaptivePredict(this._input,27,this._ctx);
	        }

	    } catch( error) {
	        if(error instanceof antlr4.error.RecognitionException) {
		        localctx.exception = error;
		        this._errHandler.reportError(this, error);
		        this._errHandler.recover(this, error);
		    } else {
		    	throw error;
		    }
	    } finally {
	        this.unrollRecursionContexts(_parentctx)
	    }
	    return localctx;
	}



	extensions() {
	    let localctx = new ExtensionsContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 44, RulepadGrammarParser.RULE_extensions);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 302;
	        this.match(RulepadGrammarParser.EXTENSION);
	        this.state = 303;
	        this.extensionCondition();
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	extensionCondition() {
	    let localctx = new ExtensionConditionContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 46, RulepadGrammarParser.RULE_extensionCondition);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 305;
	        this.of();
	        this.state = 310;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.T__0:
	            this.state = 306;
	            this.combinatorialWords();
	            this.state = 307;
	            this.match(RulepadGrammarParser.SPACE);
	            break;
	        case RulepadGrammarParser.SUPERCLASS:
	            this.state = 309;
	            this.match(RulepadGrammarParser.SUPERCLASS);
	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	implementations() {
	    let localctx = new ImplementationsContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 48, RulepadGrammarParser.RULE_implementations);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 312;
	        this.match(RulepadGrammarParser.IMPLEMENTATION);
	        this.state = 313;
	        this.implementationCondition();
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	implementationCondition() {
	    let localctx = new ImplementationConditionContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 50, RulepadGrammarParser.RULE_implementationCondition);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 315;
	        this.of();
	        this.state = 320;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.T__0:
	            this.state = 316;
	            this.combinatorialWords();
	            this.state = 317;
	            this.match(RulepadGrammarParser.SPACE);
	            break;
	        case RulepadGrammarParser.INTERFACE:
	            this.state = 319;
	            this.match(RulepadGrammarParser.INTERFACE);
	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	functions() {
	    let localctx = new FunctionsContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 52, RulepadGrammarParser.RULE_functions);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 322;
	        this.match(RulepadGrammarParser.FUNCTION);
	        this.state = 323;
	        this.functionCondition();
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	functionCondition() {
	    let localctx = new FunctionConditionContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 54, RulepadGrammarParser.RULE_functionCondition);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 325;
	        this.withWord();
	        this.state = 326;
	        this.functionExpression(0);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	functionExpression(_p) {
		if(_p===undefined) {
		    _p = 0;
		}
	    const _parentctx = this._ctx;
	    const _parentState = this.state;
	    let localctx = new FunctionExpressionContext(this, this._ctx, _parentState);
	    let _prevctx = localctx;
	    const _startState = 56;
	    this.enterRecursionRule(localctx, 56, RulepadGrammarParser.RULE_functionExpression, _p);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 338;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.LPAREN:
	            this.state = 329;
	            this.match(RulepadGrammarParser.LPAREN);
	            this.state = 330;
	            this.functionExpression(0);
	            this.state = 331;
	            this.match(RulepadGrammarParser.RPAREN);
	            break;
	        case RulepadGrammarParser.ANNOTATION:
	        case RulepadGrammarParser.PARAMETER:
	        case RulepadGrammarParser.TYPES:
	            this.state = 336;
	            this._errHandler.sync(this);
	            switch(this._input.LA(1)) {
	            case RulepadGrammarParser.ANNOTATION:
	                this.state = 333;
	                this.annotations();
	                break;
	            case RulepadGrammarParser.TYPES:
	                this.state = 334;
	                this.types();
	                break;
	            case RulepadGrammarParser.PARAMETER:
	                this.state = 335;
	                this.functionParameters();
	                break;
	            default:
	                throw new antlr4.error.NoViableAltException(this);
	            }
	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	        this._ctx.stop = this._input.LT(-1);
	        this.state = 348;
	        this._errHandler.sync(this);
	        let _alt = this._interp.adaptivePredict(this._input,33,this._ctx)
	        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
	            if(_alt===1) {
	                if(this._parseListeners!==null) {
	                    this.triggerExitRuleEvent();
	                }
	                _prevctx = localctx;
	                this.state = 346;
	                this._errHandler.sync(this);
	                var la_ = this._interp.adaptivePredict(this._input,32,this._ctx);
	                switch(la_) {
	                case 1:
	                    localctx = new FunctionExpressionContext(this, _parentctx, _parentState);
	                    localctx.left = _prevctx;
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_functionExpression);
	                    this.state = 340;
	                    if (!( this.precpred(this._ctx, 3))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 3)");
	                    }
	                    this.state = 341;
	                    localctx.op = this.binary();
	                    this.state = 342;
	                    localctx.right = this.functionExpression(4);
	                    break;

	                case 2:
	                    localctx = new FunctionExpressionContext(this, _parentctx, _parentState);
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_functionExpression);
	                    this.state = 344;
	                    if (!( this.precpred(this._ctx, 1))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 1)");
	                    }
	                    this.state = 345;
	                    this.match(RulepadGrammarParser.SPACE);
	                    break;

	                } 
	            }
	            this.state = 350;
	            this._errHandler.sync(this);
	            _alt = this._interp.adaptivePredict(this._input,33,this._ctx);
	        }

	    } catch( error) {
	        if(error instanceof antlr4.error.RecognitionException) {
		        localctx.exception = error;
		        this._errHandler.reportError(this, error);
		        this._errHandler.recover(this, error);
		    } else {
		    	throw error;
		    }
	    } finally {
	        this.unrollRecursionContexts(_parentctx)
	    }
	    return localctx;
	}



	constructors() {
	    let localctx = new ConstructorsContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 58, RulepadGrammarParser.RULE_constructors);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 351;
	        this.match(RulepadGrammarParser.CONSTRUCTOR);
	        this.state = 352;
	        this.constructorCondition();
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	constructorOf() {
	    let localctx = new ConstructorOfContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 60, RulepadGrammarParser.RULE_constructorOf);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 354;
	        this.of();
	        this.state = 355;
	        this.classes();
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	constructorCondition() {
	    let localctx = new ConstructorConditionContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 62, RulepadGrammarParser.RULE_constructorCondition);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 357;
	        this.withWord();
	        this.state = 358;
	        this.constructorExpression(0);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	constructorExpression(_p) {
		if(_p===undefined) {
		    _p = 0;
		}
	    const _parentctx = this._ctx;
	    const _parentState = this.state;
	    let localctx = new ConstructorExpressionContext(this, this._ctx, _parentState);
	    let _prevctx = localctx;
	    const _startState = 64;
	    this.enterRecursionRule(localctx, 64, RulepadGrammarParser.RULE_constructorExpression, _p);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 369;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.LPAREN:
	            this.state = 361;
	            this.match(RulepadGrammarParser.LPAREN);
	            this.state = 362;
	            this.constructorExpression(0);
	            this.state = 363;
	            this.match(RulepadGrammarParser.RPAREN);
	            break;
	        case RulepadGrammarParser.ANNOTATION:
	        case RulepadGrammarParser.PARAMETER:
	            this.state = 367;
	            this._errHandler.sync(this);
	            switch(this._input.LA(1)) {
	            case RulepadGrammarParser.ANNOTATION:
	                this.state = 365;
	                this.annotations();
	                break;
	            case RulepadGrammarParser.PARAMETER:
	                this.state = 366;
	                this.functionParameters();
	                break;
	            default:
	                throw new antlr4.error.NoViableAltException(this);
	            }
	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	        this._ctx.stop = this._input.LT(-1);
	        this.state = 379;
	        this._errHandler.sync(this);
	        let _alt = this._interp.adaptivePredict(this._input,37,this._ctx)
	        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
	            if(_alt===1) {
	                if(this._parseListeners!==null) {
	                    this.triggerExitRuleEvent();
	                }
	                _prevctx = localctx;
	                this.state = 377;
	                this._errHandler.sync(this);
	                var la_ = this._interp.adaptivePredict(this._input,36,this._ctx);
	                switch(la_) {
	                case 1:
	                    localctx = new ConstructorExpressionContext(this, _parentctx, _parentState);
	                    localctx.left = _prevctx;
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_constructorExpression);
	                    this.state = 371;
	                    if (!( this.precpred(this._ctx, 3))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 3)");
	                    }
	                    this.state = 372;
	                    localctx.op = this.binary();
	                    this.state = 373;
	                    localctx.right = this.constructorExpression(4);
	                    break;

	                case 2:
	                    localctx = new ConstructorExpressionContext(this, _parentctx, _parentState);
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_constructorExpression);
	                    this.state = 375;
	                    if (!( this.precpred(this._ctx, 1))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 1)");
	                    }
	                    this.state = 376;
	                    this.match(RulepadGrammarParser.SPACE);
	                    break;

	                } 
	            }
	            this.state = 381;
	            this._errHandler.sync(this);
	            _alt = this._interp.adaptivePredict(this._input,37,this._ctx);
	        }

	    } catch( error) {
	        if(error instanceof antlr4.error.RecognitionException) {
		        localctx.exception = error;
		        this._errHandler.reportError(this, error);
		        this._errHandler.recover(this, error);
		    } else {
		    	throw error;
		    }
	    } finally {
	        this.unrollRecursionContexts(_parentctx)
	    }
	    return localctx;
	}



	parameters() {
	    let localctx = new ParametersContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 66, RulepadGrammarParser.RULE_parameters);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 382;
	        this.match(RulepadGrammarParser.PARAMETER);
	        this.state = 384;
	        this._errHandler.sync(this);
	        var la_ = this._interp.adaptivePredict(this._input,38,this._ctx);
	        if(la_===1) {
	            this.state = 383;
	            this.parameterCondition();

	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	parameterCondition() {
	    let localctx = new ParameterConditionContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 68, RulepadGrammarParser.RULE_parameterCondition);
	    try {
	        this.state = 392;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.T__20:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 386;
	            this.withWord();
	            this.state = 387;
	            this.parameterExpression(0);
	            break;
	        case RulepadGrammarParser.T__0:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 389;
	            this.combinatorialWords();
	            this.state = 390;
	            this.match(RulepadGrammarParser.SPACE);
	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	parameterExpression(_p) {
		if(_p===undefined) {
		    _p = 0;
		}
	    const _parentctx = this._ctx;
	    const _parentState = this.state;
	    let localctx = new ParameterExpressionContext(this, this._ctx, _parentState);
	    let _prevctx = localctx;
	    const _startState = 70;
	    this.enterRecursionRule(localctx, 70, RulepadGrammarParser.RULE_parameterExpression, _p);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 403;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.LPAREN:
	            this.state = 395;
	            this.match(RulepadGrammarParser.LPAREN);
	            this.state = 396;
	            this.parameterExpression(0);
	            this.state = 397;
	            this.match(RulepadGrammarParser.RPAREN);
	            break;
	        case RulepadGrammarParser.NAME:
	        case RulepadGrammarParser.TYPES:
	            this.state = 401;
	            this._errHandler.sync(this);
	            switch(this._input.LA(1)) {
	            case RulepadGrammarParser.TYPES:
	                this.state = 399;
	                this.types();
	                break;
	            case RulepadGrammarParser.NAME:
	                this.state = 400;
	                this.names();
	                break;
	            default:
	                throw new antlr4.error.NoViableAltException(this);
	            }
	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	        this._ctx.stop = this._input.LT(-1);
	        this.state = 413;
	        this._errHandler.sync(this);
	        let _alt = this._interp.adaptivePredict(this._input,43,this._ctx)
	        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
	            if(_alt===1) {
	                if(this._parseListeners!==null) {
	                    this.triggerExitRuleEvent();
	                }
	                _prevctx = localctx;
	                this.state = 411;
	                this._errHandler.sync(this);
	                var la_ = this._interp.adaptivePredict(this._input,42,this._ctx);
	                switch(la_) {
	                case 1:
	                    localctx = new ParameterExpressionContext(this, _parentctx, _parentState);
	                    localctx.left = _prevctx;
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_parameterExpression);
	                    this.state = 405;
	                    if (!( this.precpred(this._ctx, 3))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 3)");
	                    }
	                    this.state = 406;
	                    localctx.op = this.binary();
	                    this.state = 407;
	                    localctx.right = this.parameterExpression(4);
	                    break;

	                case 2:
	                    localctx = new ParameterExpressionContext(this, _parentctx, _parentState);
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_parameterExpression);
	                    this.state = 409;
	                    if (!( this.precpred(this._ctx, 1))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 1)");
	                    }
	                    this.state = 410;
	                    this.match(RulepadGrammarParser.SPACE);
	                    break;

	                } 
	            }
	            this.state = 415;
	            this._errHandler.sync(this);
	            _alt = this._interp.adaptivePredict(this._input,43,this._ctx);
	        }

	    } catch( error) {
	        if(error instanceof antlr4.error.RecognitionException) {
		        localctx.exception = error;
		        this._errHandler.reportError(this, error);
		        this._errHandler.recover(this, error);
		    } else {
		    	throw error;
		    }
	    } finally {
	        this.unrollRecursionContexts(_parentctx)
	    }
	    return localctx;
	}



	functionParameters() {
	    let localctx = new FunctionParametersContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 72, RulepadGrammarParser.RULE_functionParameters);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 416;
	        this.match(RulepadGrammarParser.PARAMETER);
	        this.state = 418;
	        this._errHandler.sync(this);
	        var la_ = this._interp.adaptivePredict(this._input,44,this._ctx);
	        if(la_===1) {
	            this.state = 417;
	            this.functionParameterCondition();

	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	functionParameterCondition() {
	    let localctx = new FunctionParameterConditionContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 74, RulepadGrammarParser.RULE_functionParameterCondition);
	    try {
	        this.state = 426;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.T__0:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 420;
	            this.combinatorialWords();
	            this.state = 421;
	            this.match(RulepadGrammarParser.SPACE);
	            this.state = 423;
	            this._errHandler.sync(this);
	            var la_ = this._interp.adaptivePredict(this._input,45,this._ctx);
	            if(la_===1) {
	                this.state = 422;
	                this.functionParameterConditionTransition();

	            }
	            break;
	        case RulepadGrammarParser.T__20:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 425;
	            this.functionParameterConditionTransition();
	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	functionParameterConditionTransition() {
	    let localctx = new FunctionParameterConditionTransitionContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 76, RulepadGrammarParser.RULE_functionParameterConditionTransition);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 428;
	        this.withWord();
	        this.state = 429;
	        this.functionParameterExpression(0);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	functionParameterExpression(_p) {
		if(_p===undefined) {
		    _p = 0;
		}
	    const _parentctx = this._ctx;
	    const _parentState = this.state;
	    let localctx = new FunctionParameterExpressionContext(this, this._ctx, _parentState);
	    let _prevctx = localctx;
	    const _startState = 78;
	    this.enterRecursionRule(localctx, 78, RulepadGrammarParser.RULE_functionParameterExpression, _p);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 441;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.LPAREN:
	            this.state = 432;
	            this.match(RulepadGrammarParser.LPAREN);
	            this.state = 433;
	            this.functionParameterExpression(0);
	            this.state = 434;
	            this.match(RulepadGrammarParser.RPAREN);
	            break;
	        case RulepadGrammarParser.NAME:
	        case RulepadGrammarParser.ANNOTATION:
	        case RulepadGrammarParser.TYPES:
	            this.state = 439;
	            this._errHandler.sync(this);
	            switch(this._input.LA(1)) {
	            case RulepadGrammarParser.TYPES:
	                this.state = 436;
	                this.types();
	                break;
	            case RulepadGrammarParser.NAME:
	                this.state = 437;
	                this.names();
	                break;
	            case RulepadGrammarParser.ANNOTATION:
	                this.state = 438;
	                this.annotations();
	                break;
	            default:
	                throw new antlr4.error.NoViableAltException(this);
	            }
	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	        this._ctx.stop = this._input.LT(-1);
	        this.state = 451;
	        this._errHandler.sync(this);
	        let _alt = this._interp.adaptivePredict(this._input,50,this._ctx)
	        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
	            if(_alt===1) {
	                if(this._parseListeners!==null) {
	                    this.triggerExitRuleEvent();
	                }
	                _prevctx = localctx;
	                this.state = 449;
	                this._errHandler.sync(this);
	                var la_ = this._interp.adaptivePredict(this._input,49,this._ctx);
	                switch(la_) {
	                case 1:
	                    localctx = new FunctionParameterExpressionContext(this, _parentctx, _parentState);
	                    localctx.left = _prevctx;
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_functionParameterExpression);
	                    this.state = 443;
	                    if (!( this.precpred(this._ctx, 3))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 3)");
	                    }
	                    this.state = 444;
	                    localctx.op = this.binary();
	                    this.state = 445;
	                    localctx.right = this.functionParameterExpression(4);
	                    break;

	                case 2:
	                    localctx = new FunctionParameterExpressionContext(this, _parentctx, _parentState);
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_functionParameterExpression);
	                    this.state = 447;
	                    if (!( this.precpred(this._ctx, 1))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 1)");
	                    }
	                    this.state = 448;
	                    this.match(RulepadGrammarParser.SPACE);
	                    break;

	                } 
	            }
	            this.state = 453;
	            this._errHandler.sync(this);
	            _alt = this._interp.adaptivePredict(this._input,50,this._ctx);
	        }

	    } catch( error) {
	        if(error instanceof antlr4.error.RecognitionException) {
		        localctx.exception = error;
		        this._errHandler.reportError(this, error);
		        this._errHandler.recover(this, error);
		    } else {
		    	throw error;
		    }
	    } finally {
	        this.unrollRecursionContexts(_parentctx)
	    }
	    return localctx;
	}



	types() {
	    let localctx = new TypesContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 80, RulepadGrammarParser.RULE_types);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 454;
	        this.match(RulepadGrammarParser.TYPES);
	        this.state = 456;
	        this._errHandler.sync(this);
	        var la_ = this._interp.adaptivePredict(this._input,51,this._ctx);
	        if(la_===1) {
	            this.state = 455;
	            this.typeCondition();

	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	typeCondition() {
	    let localctx = new TypeConditionContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 82, RulepadGrammarParser.RULE_typeCondition);
	    try {
	        this.state = 464;
	        this._errHandler.sync(this);
	        var la_ = this._interp.adaptivePredict(this._input,52,this._ctx);
	        switch(la_) {
	        case 1:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 458;
	            this.combinatorialWords();
	            this.state = 459;
	            this.match(RulepadGrammarParser.SPACE);
	            break;

	        case 2:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 461;
	            this.words();
	            this.state = 462;
	            this.match(RulepadGrammarParser.SPACE);
	            break;

	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	declarationStatements() {
	    let localctx = new DeclarationStatementsContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 84, RulepadGrammarParser.RULE_declarationStatements);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 466;
	        this.match(RulepadGrammarParser.DeclarationStatement);
	        this.state = 467;
	        this.declarationStatementCondition();
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	declarationStatementCondition() {
	    let localctx = new DeclarationStatementConditionContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 86, RulepadGrammarParser.RULE_declarationStatementCondition);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 469;
	        this.withWord();
	        this.state = 470;
	        this.declarationStatementExpression(0);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	declarationStatementExpression(_p) {
		if(_p===undefined) {
		    _p = 0;
		}
	    const _parentctx = this._ctx;
	    const _parentState = this.state;
	    let localctx = new DeclarationStatementExpressionContext(this, this._ctx, _parentState);
	    let _prevctx = localctx;
	    const _startState = 88;
	    this.enterRecursionRule(localctx, 88, RulepadGrammarParser.RULE_declarationStatementExpression, _p);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 481;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.LPAREN:
	            this.state = 473;
	            this.match(RulepadGrammarParser.LPAREN);
	            this.state = 474;
	            this.declarationStatementExpression(0);
	            this.state = 475;
	            this.match(RulepadGrammarParser.RPAREN);
	            break;
	        case RulepadGrammarParser.ANNOTATION:
	        case RulepadGrammarParser.TYPES:
	            this.state = 479;
	            this._errHandler.sync(this);
	            switch(this._input.LA(1)) {
	            case RulepadGrammarParser.ANNOTATION:
	                this.state = 477;
	                this.annotations();
	                break;
	            case RulepadGrammarParser.TYPES:
	                this.state = 478;
	                this.types();
	                break;
	            default:
	                throw new antlr4.error.NoViableAltException(this);
	            }
	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	        this._ctx.stop = this._input.LT(-1);
	        this.state = 491;
	        this._errHandler.sync(this);
	        let _alt = this._interp.adaptivePredict(this._input,56,this._ctx)
	        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
	            if(_alt===1) {
	                if(this._parseListeners!==null) {
	                    this.triggerExitRuleEvent();
	                }
	                _prevctx = localctx;
	                this.state = 489;
	                this._errHandler.sync(this);
	                var la_ = this._interp.adaptivePredict(this._input,55,this._ctx);
	                switch(la_) {
	                case 1:
	                    localctx = new DeclarationStatementExpressionContext(this, _parentctx, _parentState);
	                    localctx.left = _prevctx;
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_declarationStatementExpression);
	                    this.state = 483;
	                    if (!( this.precpred(this._ctx, 3))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 3)");
	                    }
	                    this.state = 484;
	                    localctx.op = this.binary();
	                    this.state = 485;
	                    localctx.right = this.declarationStatementExpression(4);
	                    break;

	                case 2:
	                    localctx = new DeclarationStatementExpressionContext(this, _parentctx, _parentState);
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_declarationStatementExpression);
	                    this.state = 487;
	                    if (!( this.precpred(this._ctx, 1))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 1)");
	                    }
	                    this.state = 488;
	                    this.match(RulepadGrammarParser.SPACE);
	                    break;

	                } 
	            }
	            this.state = 493;
	            this._errHandler.sync(this);
	            _alt = this._interp.adaptivePredict(this._input,56,this._ctx);
	        }

	    } catch( error) {
	        if(error instanceof antlr4.error.RecognitionException) {
		        localctx.exception = error;
		        this._errHandler.reportError(this, error);
		        this._errHandler.recover(this, error);
		    } else {
		    	throw error;
		    }
	    } finally {
	        this.unrollRecursionContexts(_parentctx)
	    }
	    return localctx;
	}



	configurationFiles() {
	    let localctx = new ConfigurationFilesContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 90, RulepadGrammarParser.RULE_configurationFiles);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 494;
	        this.match(RulepadGrammarParser.ConfigurationFile);
	        this.state = 496;
	        this._errHandler.sync(this);
	        var la_ = this._interp.adaptivePredict(this._input,57,this._ctx);
	        if(la_===1) {
	            this.state = 495;
	            this.configurationFileCondition();

	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	configurationFileCondition() {
	    let localctx = new ConfigurationFileConditionContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 92, RulepadGrammarParser.RULE_configurationFileCondition);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 498;
	        this.withWord();
	        this.state = 499;
	        this.configurationFileExpression(0);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	configurationFileExpression(_p) {
		if(_p===undefined) {
		    _p = 0;
		}
	    const _parentctx = this._ctx;
	    const _parentState = this.state;
	    let localctx = new ConfigurationFileExpressionContext(this, this._ctx, _parentState);
	    let _prevctx = localctx;
	    const _startState = 94;
	    this.enterRecursionRule(localctx, 94, RulepadGrammarParser.RULE_configurationFileExpression, _p);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 507;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.LPAREN:
	            this.state = 502;
	            this.match(RulepadGrammarParser.LPAREN);
	            this.state = 503;
	            this.configurationFileExpression(0);
	            this.state = 504;
	            this.match(RulepadGrammarParser.RPAREN);
	            break;
	        case RulepadGrammarParser.CONFIGURATION_PROPERTIES:
	            this.state = 506;
	            this.configurationProperties();
	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	        this._ctx.stop = this._input.LT(-1);
	        this.state = 517;
	        this._errHandler.sync(this);
	        let _alt = this._interp.adaptivePredict(this._input,60,this._ctx)
	        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
	            if(_alt===1) {
	                if(this._parseListeners!==null) {
	                    this.triggerExitRuleEvent();
	                }
	                _prevctx = localctx;
	                this.state = 515;
	                this._errHandler.sync(this);
	                var la_ = this._interp.adaptivePredict(this._input,59,this._ctx);
	                switch(la_) {
	                case 1:
	                    localctx = new ConfigurationFileExpressionContext(this, _parentctx, _parentState);
	                    localctx.left = _prevctx;
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_configurationFileExpression);
	                    this.state = 509;
	                    if (!( this.precpred(this._ctx, 3))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 3)");
	                    }
	                    this.state = 510;
	                    localctx.op = this.binary();
	                    this.state = 511;
	                    localctx.right = this.configurationFileExpression(4);
	                    break;

	                case 2:
	                    localctx = new ConfigurationFileExpressionContext(this, _parentctx, _parentState);
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_configurationFileExpression);
	                    this.state = 513;
	                    if (!( this.precpred(this._ctx, 1))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 1)");
	                    }
	                    this.state = 514;
	                    this.match(RulepadGrammarParser.SPACE);
	                    break;

	                } 
	            }
	            this.state = 519;
	            this._errHandler.sync(this);
	            _alt = this._interp.adaptivePredict(this._input,60,this._ctx);
	        }

	    } catch( error) {
	        if(error instanceof antlr4.error.RecognitionException) {
		        localctx.exception = error;
		        this._errHandler.reportError(this, error);
		        this._errHandler.recover(this, error);
		    } else {
		    	throw error;
		    }
	    } finally {
	        this.unrollRecursionContexts(_parentctx)
	    }
	    return localctx;
	}



	configurationProperties() {
	    let localctx = new ConfigurationPropertiesContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 96, RulepadGrammarParser.RULE_configurationProperties);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 520;
	        this.match(RulepadGrammarParser.CONFIGURATION_PROPERTIES);
	        this.state = 521;
	        this.configurationPropertyCondition();
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	configurationPropertyCondition() {
	    let localctx = new ConfigurationPropertyConditionContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 98, RulepadGrammarParser.RULE_configurationPropertyCondition);
	    try {
	        this.state = 529;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.T__20:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 523;
	            this.withWord();
	            this.state = 524;
	            this.configurationPropertyExpression(0);
	            break;
	        case RulepadGrammarParser.T__0:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 526;
	            this.combinatorialWords();
	            this.state = 527;
	            this.match(RulepadGrammarParser.SPACE);
	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	configurationPropertyExpression(_p) {
		if(_p===undefined) {
		    _p = 0;
		}
	    const _parentctx = this._ctx;
	    const _parentState = this.state;
	    let localctx = new ConfigurationPropertyExpressionContext(this, this._ctx, _parentState);
	    let _prevctx = localctx;
	    const _startState = 100;
	    this.enterRecursionRule(localctx, 100, RulepadGrammarParser.RULE_configurationPropertyExpression, _p);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 540;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.LPAREN:
	            this.state = 532;
	            this.match(RulepadGrammarParser.LPAREN);
	            this.state = 533;
	            this.configurationPropertyExpression(0);
	            this.state = 534;
	            this.match(RulepadGrammarParser.RPAREN);
	            break;
	        case RulepadGrammarParser.NAME:
	        case RulepadGrammarParser.TYPES:
	            this.state = 538;
	            this._errHandler.sync(this);
	            switch(this._input.LA(1)) {
	            case RulepadGrammarParser.TYPES:
	                this.state = 536;
	                this.types();
	                break;
	            case RulepadGrammarParser.NAME:
	                this.state = 537;
	                this.names();
	                break;
	            default:
	                throw new antlr4.error.NoViableAltException(this);
	            }
	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	        this._ctx.stop = this._input.LT(-1);
	        this.state = 550;
	        this._errHandler.sync(this);
	        let _alt = this._interp.adaptivePredict(this._input,65,this._ctx)
	        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
	            if(_alt===1) {
	                if(this._parseListeners!==null) {
	                    this.triggerExitRuleEvent();
	                }
	                _prevctx = localctx;
	                this.state = 548;
	                this._errHandler.sync(this);
	                var la_ = this._interp.adaptivePredict(this._input,64,this._ctx);
	                switch(la_) {
	                case 1:
	                    localctx = new ConfigurationPropertyExpressionContext(this, _parentctx, _parentState);
	                    localctx.left = _prevctx;
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_configurationPropertyExpression);
	                    this.state = 542;
	                    if (!( this.precpred(this._ctx, 3))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 3)");
	                    }
	                    this.state = 543;
	                    localctx.op = this.binary();
	                    this.state = 544;
	                    localctx.right = this.configurationPropertyExpression(4);
	                    break;

	                case 2:
	                    localctx = new ConfigurationPropertyExpressionContext(this, _parentctx, _parentState);
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_configurationPropertyExpression);
	                    this.state = 546;
	                    if (!( this.precpred(this._ctx, 1))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 1)");
	                    }
	                    this.state = 547;
	                    this.match(RulepadGrammarParser.SPACE);
	                    break;

	                } 
	            }
	            this.state = 552;
	            this._errHandler.sync(this);
	            _alt = this._interp.adaptivePredict(this._input,65,this._ctx);
	        }

	    } catch( error) {
	        if(error instanceof antlr4.error.RecognitionException) {
		        localctx.exception = error;
		        this._errHandler.reportError(this, error);
		        this._errHandler.recover(this, error);
		    } else {
		    	throw error;
		    }
	    } finally {
	        this.unrollRecursionContexts(_parentctx)
	    }
	    return localctx;
	}



	classes() {
	    let localctx = new ClassesContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 102, RulepadGrammarParser.RULE_classes);
	    var _la = 0; // Token type
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 553;
	        this.match(RulepadGrammarParser.CLASSES);
	        this.state = 555;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        if(_la===RulepadGrammarParser.T__20) {
	            this.state = 554;
	            this.classCondition();
	        }

	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	classCondition() {
	    let localctx = new ClassConditionContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 104, RulepadGrammarParser.RULE_classCondition);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 557;
	        this.withWord();
	        this.state = 558;
	        this.classExpression(0);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	classExpression(_p) {
		if(_p===undefined) {
		    _p = 0;
		}
	    const _parentctx = this._ctx;
	    const _parentState = this.state;
	    let localctx = new ClassExpressionContext(this, this._ctx, _parentState);
	    let _prevctx = localctx;
	    const _startState = 106;
	    this.enterRecursionRule(localctx, 106, RulepadGrammarParser.RULE_classExpression, _p);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 575;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.LPAREN:
	            this.state = 561;
	            this.match(RulepadGrammarParser.LPAREN);
	            this.state = 562;
	            this.classExpression(0);
	            this.state = 563;
	            this.match(RulepadGrammarParser.RPAREN);
	            break;
	        case RulepadGrammarParser.ANNOTATION:
	        case RulepadGrammarParser.EXTENSION:
	        case RulepadGrammarParser.IMPLEMENTATION:
	        case RulepadGrammarParser.FUNCTION:
	        case RulepadGrammarParser.CONSTRUCTOR:
	        case RulepadGrammarParser.DeclarationStatement:
	        case RulepadGrammarParser.ConfigurationFile:
	        case RulepadGrammarParser.BEAN_DECL:
	            this.state = 573;
	            this._errHandler.sync(this);
	            switch(this._input.LA(1)) {
	            case RulepadGrammarParser.ANNOTATION:
	                this.state = 565;
	                this.annotations();
	                break;
	            case RulepadGrammarParser.EXTENSION:
	                this.state = 566;
	                this.extensions();
	                break;
	            case RulepadGrammarParser.IMPLEMENTATION:
	                this.state = 567;
	                this.implementations();
	                break;
	            case RulepadGrammarParser.FUNCTION:
	                this.state = 568;
	                this.functions();
	                break;
	            case RulepadGrammarParser.CONSTRUCTOR:
	                this.state = 569;
	                this.constructors();
	                break;
	            case RulepadGrammarParser.DeclarationStatement:
	                this.state = 570;
	                this.declarationStatements();
	                break;
	            case RulepadGrammarParser.ConfigurationFile:
	                this.state = 571;
	                this.configurationFiles();
	                break;
	            case RulepadGrammarParser.BEAN_DECL:
	                this.state = 572;
	                this.beans();
	                break;
	            default:
	                throw new antlr4.error.NoViableAltException(this);
	            }
	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	        this._ctx.stop = this._input.LT(-1);
	        this.state = 585;
	        this._errHandler.sync(this);
	        let _alt = this._interp.adaptivePredict(this._input,70,this._ctx)
	        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
	            if(_alt===1) {
	                if(this._parseListeners!==null) {
	                    this.triggerExitRuleEvent();
	                }
	                _prevctx = localctx;
	                this.state = 583;
	                this._errHandler.sync(this);
	                var la_ = this._interp.adaptivePredict(this._input,69,this._ctx);
	                switch(la_) {
	                case 1:
	                    localctx = new ClassExpressionContext(this, _parentctx, _parentState);
	                    localctx.left = _prevctx;
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_classExpression);
	                    this.state = 577;
	                    if (!( this.precpred(this._ctx, 3))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 3)");
	                    }
	                    this.state = 578;
	                    localctx.op = this.binary();
	                    this.state = 579;
	                    localctx.right = this.classExpression(4);
	                    break;

	                case 2:
	                    localctx = new ClassExpressionContext(this, _parentctx, _parentState);
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_classExpression);
	                    this.state = 581;
	                    if (!( this.precpred(this._ctx, 1))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 1)");
	                    }
	                    this.state = 582;
	                    this.match(RulepadGrammarParser.SPACE);
	                    break;

	                } 
	            }
	            this.state = 587;
	            this._errHandler.sync(this);
	            _alt = this._interp.adaptivePredict(this._input,70,this._ctx);
	        }

	    } catch( error) {
	        if(error instanceof antlr4.error.RecognitionException) {
		        localctx.exception = error;
		        this._errHandler.reportError(this, error);
		        this._errHandler.recover(this, error);
		    } else {
		    	throw error;
		    }
	    } finally {
	        this.unrollRecursionContexts(_parentctx)
	    }
	    return localctx;
	}



	beans() {
	    let localctx = new BeansContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 108, RulepadGrammarParser.RULE_beans);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 588;
	        this.match(RulepadGrammarParser.BEAN_DECL);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


}

RulepadGrammarParser.EOF = antlr4.Token.EOF;
RulepadGrammarParser.T__0 = 1;
RulepadGrammarParser.T__1 = 2;
RulepadGrammarParser.T__2 = 3;
RulepadGrammarParser.T__3 = 4;
RulepadGrammarParser.T__4 = 5;
RulepadGrammarParser.T__5 = 6;
RulepadGrammarParser.T__6 = 7;
RulepadGrammarParser.T__7 = 8;
RulepadGrammarParser.T__8 = 9;
RulepadGrammarParser.T__9 = 10;
RulepadGrammarParser.T__10 = 11;
RulepadGrammarParser.T__11 = 12;
RulepadGrammarParser.T__12 = 13;
RulepadGrammarParser.T__13 = 14;
RulepadGrammarParser.T__14 = 15;
RulepadGrammarParser.T__15 = 16;
RulepadGrammarParser.T__16 = 17;
RulepadGrammarParser.T__17 = 18;
RulepadGrammarParser.T__18 = 19;
RulepadGrammarParser.T__19 = 20;
RulepadGrammarParser.T__20 = 21;
RulepadGrammarParser.SPACE = 22;
RulepadGrammarParser.Alphabet = 23;
RulepadGrammarParser.NL = 24;
RulepadGrammarParser.LPAREN = 25;
RulepadGrammarParser.RPAREN = 26;
RulepadGrammarParser.NAME = 27;
RulepadGrammarParser.ANNOTATION = 28;
RulepadGrammarParser.EXTENSION = 29;
RulepadGrammarParser.SUPERCLASS = 30;
RulepadGrammarParser.IMPLEMENTATION = 31;
RulepadGrammarParser.INTERFACE = 32;
RulepadGrammarParser.FUNCTION = 33;
RulepadGrammarParser.CONSTRUCTOR = 34;
RulepadGrammarParser.PARAMETER = 35;
RulepadGrammarParser.TYPES = 36;
RulepadGrammarParser.DeclarationStatement = 37;
RulepadGrammarParser.ConfigurationFile = 38;
RulepadGrammarParser.CONFIGURATION_PROPERTIES = 39;
RulepadGrammarParser.CLASSES = 40;
RulepadGrammarParser.BEAN_DECL = 41;

RulepadGrammarParser.RULE_inputSentence = 0;
RulepadGrammarParser.RULE_mustClause = 1;
RulepadGrammarParser.RULE_words = 2;
RulepadGrammarParser.RULE_word = 3;
RulepadGrammarParser.RULE_combinatorialWords = 4;
RulepadGrammarParser.RULE_symbols = 5;
RulepadGrammarParser.RULE_end = 6;
RulepadGrammarParser.RULE_emptyLine = 7;
RulepadGrammarParser.RULE_comments = 8;
RulepadGrammarParser.RULE_must = 9;
RulepadGrammarParser.RULE_of = 10;
RulepadGrammarParser.RULE_and_ = 11;
RulepadGrammarParser.RULE_or_ = 12;
RulepadGrammarParser.RULE_have = 13;
RulepadGrammarParser.RULE_withWord = 14;
RulepadGrammarParser.RULE_binary = 15;
RulepadGrammarParser.RULE_names = 16;
RulepadGrammarParser.RULE_nameCondition = 17;
RulepadGrammarParser.RULE_annotations = 18;
RulepadGrammarParser.RULE_annotationCondition = 19;
RulepadGrammarParser.RULE_annotationConditionTransition = 20;
RulepadGrammarParser.RULE_annotationExpression = 21;
RulepadGrammarParser.RULE_extensions = 22;
RulepadGrammarParser.RULE_extensionCondition = 23;
RulepadGrammarParser.RULE_implementations = 24;
RulepadGrammarParser.RULE_implementationCondition = 25;
RulepadGrammarParser.RULE_functions = 26;
RulepadGrammarParser.RULE_functionCondition = 27;
RulepadGrammarParser.RULE_functionExpression = 28;
RulepadGrammarParser.RULE_constructors = 29;
RulepadGrammarParser.RULE_constructorOf = 30;
RulepadGrammarParser.RULE_constructorCondition = 31;
RulepadGrammarParser.RULE_constructorExpression = 32;
RulepadGrammarParser.RULE_parameters = 33;
RulepadGrammarParser.RULE_parameterCondition = 34;
RulepadGrammarParser.RULE_parameterExpression = 35;
RulepadGrammarParser.RULE_functionParameters = 36;
RulepadGrammarParser.RULE_functionParameterCondition = 37;
RulepadGrammarParser.RULE_functionParameterConditionTransition = 38;
RulepadGrammarParser.RULE_functionParameterExpression = 39;
RulepadGrammarParser.RULE_types = 40;
RulepadGrammarParser.RULE_typeCondition = 41;
RulepadGrammarParser.RULE_declarationStatements = 42;
RulepadGrammarParser.RULE_declarationStatementCondition = 43;
RulepadGrammarParser.RULE_declarationStatementExpression = 44;
RulepadGrammarParser.RULE_configurationFiles = 45;
RulepadGrammarParser.RULE_configurationFileCondition = 46;
RulepadGrammarParser.RULE_configurationFileExpression = 47;
RulepadGrammarParser.RULE_configurationProperties = 48;
RulepadGrammarParser.RULE_configurationPropertyCondition = 49;
RulepadGrammarParser.RULE_configurationPropertyExpression = 50;
RulepadGrammarParser.RULE_classes = 51;
RulepadGrammarParser.RULE_classCondition = 52;
RulepadGrammarParser.RULE_classExpression = 53;
RulepadGrammarParser.RULE_beans = 54;

class InputSentenceContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_inputSentence;
    }

	EOF() {
	    return this.getToken(RulepadGrammarParser.EOF, 0);
	};

	mustClause() {
	    return this.getTypedRuleContext(MustClauseContext,0);
	};

	end() {
	    return this.getTypedRuleContext(EndContext,0);
	};

	NL = function(i) {
		if(i===undefined) {
			i = null;
		}
	    if(i===null) {
	        return this.getTokens(RulepadGrammarParser.NL);
	    } else {
	        return this.getToken(RulepadGrammarParser.NL, i);
	    }
	};


	emptyLine = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(EmptyLineContext);
	    } else {
	        return this.getTypedRuleContext(EmptyLineContext,i);
	    }
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterInputSentence(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitInputSentence(this);
		}
	}


}



class MustClauseContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_mustClause;
    }

	functions() {
	    return this.getTypedRuleContext(FunctionsContext,0);
	};

	must() {
	    return this.getTypedRuleContext(MustContext,0);
	};

	have() {
	    return this.getTypedRuleContext(HaveContext,0);
	};

	functionExpression() {
	    return this.getTypedRuleContext(FunctionExpressionContext,0);
	};

	constructors() {
	    return this.getTypedRuleContext(ConstructorsContext,0);
	};

	constructorExpression() {
	    return this.getTypedRuleContext(ConstructorExpressionContext,0);
	};

	classes() {
	    return this.getTypedRuleContext(ClassesContext,0);
	};

	classExpression() {
	    return this.getTypedRuleContext(ClassExpressionContext,0);
	};

	declarationStatements() {
	    return this.getTypedRuleContext(DeclarationStatementsContext,0);
	};

	declarationStatementExpression() {
	    return this.getTypedRuleContext(DeclarationStatementExpressionContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterMustClause(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitMustClause(this);
		}
	}


}



class WordsContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_words;
    }

	word = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(WordContext);
	    } else {
	        return this.getTypedRuleContext(WordContext,i);
	    }
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterWords(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitWords(this);
		}
	}


}



class WordContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_word;
    }

	Alphabet = function(i) {
		if(i===undefined) {
			i = null;
		}
	    if(i===null) {
	        return this.getTokens(RulepadGrammarParser.Alphabet);
	    } else {
	        return this.getToken(RulepadGrammarParser.Alphabet, i);
	    }
	};


	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterWord(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitWord(this);
		}
	}


}



class CombinatorialWordsContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_combinatorialWords;
    }

	Alphabet = function(i) {
		if(i===undefined) {
			i = null;
		}
	    if(i===null) {
	        return this.getTokens(RulepadGrammarParser.Alphabet);
	    } else {
	        return this.getToken(RulepadGrammarParser.Alphabet, i);
	    }
	};


	symbols = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(SymbolsContext);
	    } else {
	        return this.getTypedRuleContext(SymbolsContext,i);
	    }
	};

	SPACE = function(i) {
		if(i===undefined) {
			i = null;
		}
	    if(i===null) {
	        return this.getTokens(RulepadGrammarParser.SPACE);
	    } else {
	        return this.getToken(RulepadGrammarParser.SPACE, i);
	    }
	};


	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterCombinatorialWords(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitCombinatorialWords(this);
		}
	}


}



class SymbolsContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_symbols;
    }

	LPAREN() {
	    return this.getToken(RulepadGrammarParser.LPAREN, 0);
	};

	RPAREN() {
	    return this.getToken(RulepadGrammarParser.RPAREN, 0);
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterSymbols(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitSymbols(this);
		}
	}


}



class EndContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_end;
    }


	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterEnd(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitEnd(this);
		}
	}


}



class EmptyLineContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_emptyLine;
    }

	NL() {
	    return this.getToken(RulepadGrammarParser.NL, 0);
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterEmptyLine(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitEmptyLine(this);
		}
	}


}



class CommentsContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_comments;
    }

	Alphabet = function(i) {
		if(i===undefined) {
			i = null;
		}
	    if(i===null) {
	        return this.getTokens(RulepadGrammarParser.Alphabet);
	    } else {
	        return this.getToken(RulepadGrammarParser.Alphabet, i);
	    }
	};


	symbols = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(SymbolsContext);
	    } else {
	        return this.getTypedRuleContext(SymbolsContext,i);
	    }
	};

	SPACE = function(i) {
		if(i===undefined) {
			i = null;
		}
	    if(i===null) {
	        return this.getTokens(RulepadGrammarParser.SPACE);
	    } else {
	        return this.getToken(RulepadGrammarParser.SPACE, i);
	    }
	};


	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterComments(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitComments(this);
		}
	}


}



class MustContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_must;
    }


	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterMust(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitMust(this);
		}
	}


}



class OfContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_of;
    }


	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterOf(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitOf(this);
		}
	}


}



class And_Context extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_and_;
    }


	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterAnd_(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitAnd_(this);
		}
	}


}



class Or_Context extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_or_;
    }


	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterOr_(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitOr_(this);
		}
	}


}



class HaveContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_have;
    }


	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterHave(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitHave(this);
		}
	}


}



class WithWordContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_withWord;
    }


	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterWithWord(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitWithWord(this);
		}
	}


}



class BinaryContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_binary;
    }

	and_() {
	    return this.getTypedRuleContext(And_Context,0);
	};

	or_() {
	    return this.getTypedRuleContext(Or_Context,0);
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterBinary(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitBinary(this);
		}
	}


}



class NamesContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_names;
    }

	NAME() {
	    return this.getToken(RulepadGrammarParser.NAME, 0);
	};

	nameCondition() {
	    return this.getTypedRuleContext(NameConditionContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterNames(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitNames(this);
		}
	}


}



class NameConditionContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_nameCondition;
    }

	words() {
	    return this.getTypedRuleContext(WordsContext,0);
	};

	SPACE() {
	    return this.getToken(RulepadGrammarParser.SPACE, 0);
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterNameCondition(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitNameCondition(this);
		}
	}


}



class AnnotationsContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_annotations;
    }

	ANNOTATION() {
	    return this.getToken(RulepadGrammarParser.ANNOTATION, 0);
	};

	annotationCondition() {
	    return this.getTypedRuleContext(AnnotationConditionContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterAnnotations(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitAnnotations(this);
		}
	}


}



class AnnotationConditionContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_annotationCondition;
    }

	combinatorialWords() {
	    return this.getTypedRuleContext(CombinatorialWordsContext,0);
	};

	SPACE() {
	    return this.getToken(RulepadGrammarParser.SPACE, 0);
	};

	annotationConditionTransition() {
	    return this.getTypedRuleContext(AnnotationConditionTransitionContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterAnnotationCondition(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitAnnotationCondition(this);
		}
	}


}



class AnnotationConditionTransitionContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_annotationConditionTransition;
    }

	withWord() {
	    return this.getTypedRuleContext(WithWordContext,0);
	};

	annotationExpression() {
	    return this.getTypedRuleContext(AnnotationExpressionContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterAnnotationConditionTransition(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitAnnotationConditionTransition(this);
		}
	}


}



class AnnotationExpressionContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_annotationExpression;
        this.left = null; // AnnotationExpressionContext
        this.op = null; // BinaryContext
        this.right = null; // AnnotationExpressionContext
    }

	LPAREN() {
	    return this.getToken(RulepadGrammarParser.LPAREN, 0);
	};

	annotationExpression = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(AnnotationExpressionContext);
	    } else {
	        return this.getTypedRuleContext(AnnotationExpressionContext,i);
	    }
	};

	RPAREN() {
	    return this.getToken(RulepadGrammarParser.RPAREN, 0);
	};

	parameters() {
	    return this.getTypedRuleContext(ParametersContext,0);
	};

	binary() {
	    return this.getTypedRuleContext(BinaryContext,0);
	};

	SPACE() {
	    return this.getToken(RulepadGrammarParser.SPACE, 0);
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterAnnotationExpression(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitAnnotationExpression(this);
		}
	}


}



class ExtensionsContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_extensions;
    }

	EXTENSION() {
	    return this.getToken(RulepadGrammarParser.EXTENSION, 0);
	};

	extensionCondition() {
	    return this.getTypedRuleContext(ExtensionConditionContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterExtensions(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitExtensions(this);
		}
	}


}



class ExtensionConditionContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_extensionCondition;
    }

	of() {
	    return this.getTypedRuleContext(OfContext,0);
	};

	combinatorialWords() {
	    return this.getTypedRuleContext(CombinatorialWordsContext,0);
	};

	SPACE() {
	    return this.getToken(RulepadGrammarParser.SPACE, 0);
	};

	SUPERCLASS() {
	    return this.getToken(RulepadGrammarParser.SUPERCLASS, 0);
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterExtensionCondition(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitExtensionCondition(this);
		}
	}


}



class ImplementationsContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_implementations;
    }

	IMPLEMENTATION() {
	    return this.getToken(RulepadGrammarParser.IMPLEMENTATION, 0);
	};

	implementationCondition() {
	    return this.getTypedRuleContext(ImplementationConditionContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterImplementations(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitImplementations(this);
		}
	}


}



class ImplementationConditionContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_implementationCondition;
    }

	of() {
	    return this.getTypedRuleContext(OfContext,0);
	};

	combinatorialWords() {
	    return this.getTypedRuleContext(CombinatorialWordsContext,0);
	};

	SPACE() {
	    return this.getToken(RulepadGrammarParser.SPACE, 0);
	};

	INTERFACE() {
	    return this.getToken(RulepadGrammarParser.INTERFACE, 0);
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterImplementationCondition(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitImplementationCondition(this);
		}
	}


}



class FunctionsContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_functions;
    }

	FUNCTION() {
	    return this.getToken(RulepadGrammarParser.FUNCTION, 0);
	};

	functionCondition() {
	    return this.getTypedRuleContext(FunctionConditionContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterFunctions(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitFunctions(this);
		}
	}


}



class FunctionConditionContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_functionCondition;
    }

	withWord() {
	    return this.getTypedRuleContext(WithWordContext,0);
	};

	functionExpression() {
	    return this.getTypedRuleContext(FunctionExpressionContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterFunctionCondition(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitFunctionCondition(this);
		}
	}


}



class FunctionExpressionContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_functionExpression;
        this.left = null; // FunctionExpressionContext
        this.op = null; // BinaryContext
        this.right = null; // FunctionExpressionContext
    }

	LPAREN() {
	    return this.getToken(RulepadGrammarParser.LPAREN, 0);
	};

	functionExpression = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(FunctionExpressionContext);
	    } else {
	        return this.getTypedRuleContext(FunctionExpressionContext,i);
	    }
	};

	RPAREN() {
	    return this.getToken(RulepadGrammarParser.RPAREN, 0);
	};

	annotations() {
	    return this.getTypedRuleContext(AnnotationsContext,0);
	};

	types() {
	    return this.getTypedRuleContext(TypesContext,0);
	};

	functionParameters() {
	    return this.getTypedRuleContext(FunctionParametersContext,0);
	};

	binary() {
	    return this.getTypedRuleContext(BinaryContext,0);
	};

	SPACE() {
	    return this.getToken(RulepadGrammarParser.SPACE, 0);
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterFunctionExpression(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitFunctionExpression(this);
		}
	}


}



class ConstructorsContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_constructors;
    }

	CONSTRUCTOR() {
	    return this.getToken(RulepadGrammarParser.CONSTRUCTOR, 0);
	};

	constructorCondition() {
	    return this.getTypedRuleContext(ConstructorConditionContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterConstructors(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitConstructors(this);
		}
	}


}



class ConstructorOfContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_constructorOf;
    }

	of() {
	    return this.getTypedRuleContext(OfContext,0);
	};

	classes() {
	    return this.getTypedRuleContext(ClassesContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterConstructorOf(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitConstructorOf(this);
		}
	}


}



class ConstructorConditionContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_constructorCondition;
    }

	withWord() {
	    return this.getTypedRuleContext(WithWordContext,0);
	};

	constructorExpression() {
	    return this.getTypedRuleContext(ConstructorExpressionContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterConstructorCondition(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitConstructorCondition(this);
		}
	}


}



class ConstructorExpressionContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_constructorExpression;
        this.left = null; // ConstructorExpressionContext
        this.op = null; // BinaryContext
        this.right = null; // ConstructorExpressionContext
    }

	LPAREN() {
	    return this.getToken(RulepadGrammarParser.LPAREN, 0);
	};

	constructorExpression = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(ConstructorExpressionContext);
	    } else {
	        return this.getTypedRuleContext(ConstructorExpressionContext,i);
	    }
	};

	RPAREN() {
	    return this.getToken(RulepadGrammarParser.RPAREN, 0);
	};

	annotations() {
	    return this.getTypedRuleContext(AnnotationsContext,0);
	};

	functionParameters() {
	    return this.getTypedRuleContext(FunctionParametersContext,0);
	};

	binary() {
	    return this.getTypedRuleContext(BinaryContext,0);
	};

	SPACE() {
	    return this.getToken(RulepadGrammarParser.SPACE, 0);
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterConstructorExpression(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitConstructorExpression(this);
		}
	}


}



class ParametersContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_parameters;
    }

	PARAMETER() {
	    return this.getToken(RulepadGrammarParser.PARAMETER, 0);
	};

	parameterCondition() {
	    return this.getTypedRuleContext(ParameterConditionContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterParameters(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitParameters(this);
		}
	}


}



class ParameterConditionContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_parameterCondition;
    }

	withWord() {
	    return this.getTypedRuleContext(WithWordContext,0);
	};

	parameterExpression() {
	    return this.getTypedRuleContext(ParameterExpressionContext,0);
	};

	combinatorialWords() {
	    return this.getTypedRuleContext(CombinatorialWordsContext,0);
	};

	SPACE() {
	    return this.getToken(RulepadGrammarParser.SPACE, 0);
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterParameterCondition(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitParameterCondition(this);
		}
	}


}



class ParameterExpressionContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_parameterExpression;
        this.left = null; // ParameterExpressionContext
        this.op = null; // BinaryContext
        this.right = null; // ParameterExpressionContext
    }

	LPAREN() {
	    return this.getToken(RulepadGrammarParser.LPAREN, 0);
	};

	parameterExpression = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(ParameterExpressionContext);
	    } else {
	        return this.getTypedRuleContext(ParameterExpressionContext,i);
	    }
	};

	RPAREN() {
	    return this.getToken(RulepadGrammarParser.RPAREN, 0);
	};

	types() {
	    return this.getTypedRuleContext(TypesContext,0);
	};

	names() {
	    return this.getTypedRuleContext(NamesContext,0);
	};

	binary() {
	    return this.getTypedRuleContext(BinaryContext,0);
	};

	SPACE() {
	    return this.getToken(RulepadGrammarParser.SPACE, 0);
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterParameterExpression(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitParameterExpression(this);
		}
	}


}



class FunctionParametersContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_functionParameters;
    }

	PARAMETER() {
	    return this.getToken(RulepadGrammarParser.PARAMETER, 0);
	};

	functionParameterCondition() {
	    return this.getTypedRuleContext(FunctionParameterConditionContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterFunctionParameters(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitFunctionParameters(this);
		}
	}


}



class FunctionParameterConditionContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_functionParameterCondition;
    }

	combinatorialWords() {
	    return this.getTypedRuleContext(CombinatorialWordsContext,0);
	};

	SPACE() {
	    return this.getToken(RulepadGrammarParser.SPACE, 0);
	};

	functionParameterConditionTransition() {
	    return this.getTypedRuleContext(FunctionParameterConditionTransitionContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterFunctionParameterCondition(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitFunctionParameterCondition(this);
		}
	}


}



class FunctionParameterConditionTransitionContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_functionParameterConditionTransition;
    }

	withWord() {
	    return this.getTypedRuleContext(WithWordContext,0);
	};

	functionParameterExpression() {
	    return this.getTypedRuleContext(FunctionParameterExpressionContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterFunctionParameterConditionTransition(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitFunctionParameterConditionTransition(this);
		}
	}


}



class FunctionParameterExpressionContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_functionParameterExpression;
        this.left = null; // FunctionParameterExpressionContext
        this.op = null; // BinaryContext
        this.right = null; // FunctionParameterExpressionContext
    }

	LPAREN() {
	    return this.getToken(RulepadGrammarParser.LPAREN, 0);
	};

	functionParameterExpression = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(FunctionParameterExpressionContext);
	    } else {
	        return this.getTypedRuleContext(FunctionParameterExpressionContext,i);
	    }
	};

	RPAREN() {
	    return this.getToken(RulepadGrammarParser.RPAREN, 0);
	};

	types() {
	    return this.getTypedRuleContext(TypesContext,0);
	};

	names() {
	    return this.getTypedRuleContext(NamesContext,0);
	};

	annotations() {
	    return this.getTypedRuleContext(AnnotationsContext,0);
	};

	binary() {
	    return this.getTypedRuleContext(BinaryContext,0);
	};

	SPACE() {
	    return this.getToken(RulepadGrammarParser.SPACE, 0);
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterFunctionParameterExpression(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitFunctionParameterExpression(this);
		}
	}


}



class TypesContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_types;
    }

	TYPES() {
	    return this.getToken(RulepadGrammarParser.TYPES, 0);
	};

	typeCondition() {
	    return this.getTypedRuleContext(TypeConditionContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterTypes(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitTypes(this);
		}
	}


}



class TypeConditionContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_typeCondition;
    }

	combinatorialWords() {
	    return this.getTypedRuleContext(CombinatorialWordsContext,0);
	};

	SPACE() {
	    return this.getToken(RulepadGrammarParser.SPACE, 0);
	};

	words() {
	    return this.getTypedRuleContext(WordsContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterTypeCondition(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitTypeCondition(this);
		}
	}


}



class DeclarationStatementsContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_declarationStatements;
    }

	DeclarationStatement() {
	    return this.getToken(RulepadGrammarParser.DeclarationStatement, 0);
	};

	declarationStatementCondition() {
	    return this.getTypedRuleContext(DeclarationStatementConditionContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterDeclarationStatements(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitDeclarationStatements(this);
		}
	}


}



class DeclarationStatementConditionContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_declarationStatementCondition;
    }

	withWord() {
	    return this.getTypedRuleContext(WithWordContext,0);
	};

	declarationStatementExpression() {
	    return this.getTypedRuleContext(DeclarationStatementExpressionContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterDeclarationStatementCondition(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitDeclarationStatementCondition(this);
		}
	}


}



class DeclarationStatementExpressionContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_declarationStatementExpression;
        this.left = null; // DeclarationStatementExpressionContext
        this.op = null; // BinaryContext
        this.right = null; // DeclarationStatementExpressionContext
    }

	LPAREN() {
	    return this.getToken(RulepadGrammarParser.LPAREN, 0);
	};

	declarationStatementExpression = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(DeclarationStatementExpressionContext);
	    } else {
	        return this.getTypedRuleContext(DeclarationStatementExpressionContext,i);
	    }
	};

	RPAREN() {
	    return this.getToken(RulepadGrammarParser.RPAREN, 0);
	};

	annotations() {
	    return this.getTypedRuleContext(AnnotationsContext,0);
	};

	types() {
	    return this.getTypedRuleContext(TypesContext,0);
	};

	binary() {
	    return this.getTypedRuleContext(BinaryContext,0);
	};

	SPACE() {
	    return this.getToken(RulepadGrammarParser.SPACE, 0);
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterDeclarationStatementExpression(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitDeclarationStatementExpression(this);
		}
	}


}



class ConfigurationFilesContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_configurationFiles;
    }

	ConfigurationFile() {
	    return this.getToken(RulepadGrammarParser.ConfigurationFile, 0);
	};

	configurationFileCondition() {
	    return this.getTypedRuleContext(ConfigurationFileConditionContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterConfigurationFiles(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitConfigurationFiles(this);
		}
	}


}



class ConfigurationFileConditionContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_configurationFileCondition;
    }

	withWord() {
	    return this.getTypedRuleContext(WithWordContext,0);
	};

	configurationFileExpression() {
	    return this.getTypedRuleContext(ConfigurationFileExpressionContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterConfigurationFileCondition(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitConfigurationFileCondition(this);
		}
	}


}



class ConfigurationFileExpressionContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_configurationFileExpression;
        this.left = null; // ConfigurationFileExpressionContext
        this.op = null; // BinaryContext
        this.right = null; // ConfigurationFileExpressionContext
    }

	LPAREN() {
	    return this.getToken(RulepadGrammarParser.LPAREN, 0);
	};

	configurationFileExpression = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(ConfigurationFileExpressionContext);
	    } else {
	        return this.getTypedRuleContext(ConfigurationFileExpressionContext,i);
	    }
	};

	RPAREN() {
	    return this.getToken(RulepadGrammarParser.RPAREN, 0);
	};

	configurationProperties() {
	    return this.getTypedRuleContext(ConfigurationPropertiesContext,0);
	};

	binary() {
	    return this.getTypedRuleContext(BinaryContext,0);
	};

	SPACE() {
	    return this.getToken(RulepadGrammarParser.SPACE, 0);
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterConfigurationFileExpression(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitConfigurationFileExpression(this);
		}
	}


}



class ConfigurationPropertiesContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_configurationProperties;
    }

	CONFIGURATION_PROPERTIES() {
	    return this.getToken(RulepadGrammarParser.CONFIGURATION_PROPERTIES, 0);
	};

	configurationPropertyCondition() {
	    return this.getTypedRuleContext(ConfigurationPropertyConditionContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterConfigurationProperties(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitConfigurationProperties(this);
		}
	}


}



class ConfigurationPropertyConditionContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_configurationPropertyCondition;
    }

	withWord() {
	    return this.getTypedRuleContext(WithWordContext,0);
	};

	configurationPropertyExpression() {
	    return this.getTypedRuleContext(ConfigurationPropertyExpressionContext,0);
	};

	combinatorialWords() {
	    return this.getTypedRuleContext(CombinatorialWordsContext,0);
	};

	SPACE() {
	    return this.getToken(RulepadGrammarParser.SPACE, 0);
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterConfigurationPropertyCondition(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitConfigurationPropertyCondition(this);
		}
	}


}



class ConfigurationPropertyExpressionContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_configurationPropertyExpression;
        this.left = null; // ConfigurationPropertyExpressionContext
        this.op = null; // BinaryContext
        this.right = null; // ConfigurationPropertyExpressionContext
    }

	LPAREN() {
	    return this.getToken(RulepadGrammarParser.LPAREN, 0);
	};

	configurationPropertyExpression = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(ConfigurationPropertyExpressionContext);
	    } else {
	        return this.getTypedRuleContext(ConfigurationPropertyExpressionContext,i);
	    }
	};

	RPAREN() {
	    return this.getToken(RulepadGrammarParser.RPAREN, 0);
	};

	types() {
	    return this.getTypedRuleContext(TypesContext,0);
	};

	names() {
	    return this.getTypedRuleContext(NamesContext,0);
	};

	binary() {
	    return this.getTypedRuleContext(BinaryContext,0);
	};

	SPACE() {
	    return this.getToken(RulepadGrammarParser.SPACE, 0);
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterConfigurationPropertyExpression(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitConfigurationPropertyExpression(this);
		}
	}


}



class ClassesContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_classes;
    }

	CLASSES() {
	    return this.getToken(RulepadGrammarParser.CLASSES, 0);
	};

	classCondition() {
	    return this.getTypedRuleContext(ClassConditionContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterClasses(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitClasses(this);
		}
	}


}



class ClassConditionContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_classCondition;
    }

	withWord() {
	    return this.getTypedRuleContext(WithWordContext,0);
	};

	classExpression() {
	    return this.getTypedRuleContext(ClassExpressionContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterClassCondition(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitClassCondition(this);
		}
	}


}



class ClassExpressionContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_classExpression;
        this.left = null; // ClassExpressionContext
        this.op = null; // BinaryContext
        this.right = null; // ClassExpressionContext
    }

	LPAREN() {
	    return this.getToken(RulepadGrammarParser.LPAREN, 0);
	};

	classExpression = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(ClassExpressionContext);
	    } else {
	        return this.getTypedRuleContext(ClassExpressionContext,i);
	    }
	};

	RPAREN() {
	    return this.getToken(RulepadGrammarParser.RPAREN, 0);
	};

	annotations() {
	    return this.getTypedRuleContext(AnnotationsContext,0);
	};

	extensions() {
	    return this.getTypedRuleContext(ExtensionsContext,0);
	};

	implementations() {
	    return this.getTypedRuleContext(ImplementationsContext,0);
	};

	functions() {
	    return this.getTypedRuleContext(FunctionsContext,0);
	};

	constructors() {
	    return this.getTypedRuleContext(ConstructorsContext,0);
	};

	declarationStatements() {
	    return this.getTypedRuleContext(DeclarationStatementsContext,0);
	};

	configurationFiles() {
	    return this.getTypedRuleContext(ConfigurationFilesContext,0);
	};

	beans() {
	    return this.getTypedRuleContext(BeansContext,0);
	};

	binary() {
	    return this.getTypedRuleContext(BinaryContext,0);
	};

	SPACE() {
	    return this.getToken(RulepadGrammarParser.SPACE, 0);
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterClassExpression(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitClassExpression(this);
		}
	}


}



class BeansContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_beans;
    }

	BEAN_DECL() {
	    return this.getToken(RulepadGrammarParser.BEAN_DECL, 0);
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterBeans(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitBeans(this);
		}
	}


}




RulepadGrammarParser.InputSentenceContext = InputSentenceContext; 
RulepadGrammarParser.MustClauseContext = MustClauseContext; 
RulepadGrammarParser.WordsContext = WordsContext; 
RulepadGrammarParser.WordContext = WordContext; 
RulepadGrammarParser.CombinatorialWordsContext = CombinatorialWordsContext; 
RulepadGrammarParser.SymbolsContext = SymbolsContext; 
RulepadGrammarParser.EndContext = EndContext; 
RulepadGrammarParser.EmptyLineContext = EmptyLineContext; 
RulepadGrammarParser.CommentsContext = CommentsContext; 
RulepadGrammarParser.MustContext = MustContext; 
RulepadGrammarParser.OfContext = OfContext; 
RulepadGrammarParser.And_Context = And_Context; 
RulepadGrammarParser.Or_Context = Or_Context; 
RulepadGrammarParser.HaveContext = HaveContext; 
RulepadGrammarParser.WithWordContext = WithWordContext; 
RulepadGrammarParser.BinaryContext = BinaryContext; 
RulepadGrammarParser.NamesContext = NamesContext; 
RulepadGrammarParser.NameConditionContext = NameConditionContext; 
RulepadGrammarParser.AnnotationsContext = AnnotationsContext; 
RulepadGrammarParser.AnnotationConditionContext = AnnotationConditionContext; 
RulepadGrammarParser.AnnotationConditionTransitionContext = AnnotationConditionTransitionContext; 
RulepadGrammarParser.AnnotationExpressionContext = AnnotationExpressionContext; 
RulepadGrammarParser.ExtensionsContext = ExtensionsContext; 
RulepadGrammarParser.ExtensionConditionContext = ExtensionConditionContext; 
RulepadGrammarParser.ImplementationsContext = ImplementationsContext; 
RulepadGrammarParser.ImplementationConditionContext = ImplementationConditionContext; 
RulepadGrammarParser.FunctionsContext = FunctionsContext; 
RulepadGrammarParser.FunctionConditionContext = FunctionConditionContext; 
RulepadGrammarParser.FunctionExpressionContext = FunctionExpressionContext; 
RulepadGrammarParser.ConstructorsContext = ConstructorsContext; 
RulepadGrammarParser.ConstructorOfContext = ConstructorOfContext; 
RulepadGrammarParser.ConstructorConditionContext = ConstructorConditionContext; 
RulepadGrammarParser.ConstructorExpressionContext = ConstructorExpressionContext; 
RulepadGrammarParser.ParametersContext = ParametersContext; 
RulepadGrammarParser.ParameterConditionContext = ParameterConditionContext; 
RulepadGrammarParser.ParameterExpressionContext = ParameterExpressionContext; 
RulepadGrammarParser.FunctionParametersContext = FunctionParametersContext; 
RulepadGrammarParser.FunctionParameterConditionContext = FunctionParameterConditionContext; 
RulepadGrammarParser.FunctionParameterConditionTransitionContext = FunctionParameterConditionTransitionContext; 
RulepadGrammarParser.FunctionParameterExpressionContext = FunctionParameterExpressionContext; 
RulepadGrammarParser.TypesContext = TypesContext; 
RulepadGrammarParser.TypeConditionContext = TypeConditionContext; 
RulepadGrammarParser.DeclarationStatementsContext = DeclarationStatementsContext; 
RulepadGrammarParser.DeclarationStatementConditionContext = DeclarationStatementConditionContext; 
RulepadGrammarParser.DeclarationStatementExpressionContext = DeclarationStatementExpressionContext; 
RulepadGrammarParser.ConfigurationFilesContext = ConfigurationFilesContext; 
RulepadGrammarParser.ConfigurationFileConditionContext = ConfigurationFileConditionContext; 
RulepadGrammarParser.ConfigurationFileExpressionContext = ConfigurationFileExpressionContext; 
RulepadGrammarParser.ConfigurationPropertiesContext = ConfigurationPropertiesContext; 
RulepadGrammarParser.ConfigurationPropertyConditionContext = ConfigurationPropertyConditionContext; 
RulepadGrammarParser.ConfigurationPropertyExpressionContext = ConfigurationPropertyExpressionContext; 
RulepadGrammarParser.ClassesContext = ClassesContext; 
RulepadGrammarParser.ClassConditionContext = ClassConditionContext; 
RulepadGrammarParser.ClassExpressionContext = ClassExpressionContext; 
RulepadGrammarParser.BeansContext = BeansContext; 
