// Generated from ../violation-detection/src/main/antlr4/ca/ualberta/grammar/RulepadGrammar.g4 by ANTLR 4.9
// jshint ignore: start
import antlr4 from 'antlr4';
import RulepadGrammarListener from './RulepadGrammarListener.js';

const serializedATN = ["\u0003\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786",
    "\u5964\u0003,\u0266\u0004\u0002\t\u0002\u0004\u0003\t\u0003\u0004\u0004",
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
    "2\t2\u00043\t3\u00044\t4\u00045\t5\u00046\t6\u00047\t7\u00048\t8\u0004",
    "9\t9\u0004:\t:\u0004;\t;\u0004<\t<\u0003\u0002\u0007\u0002z\n\u0002",
    "\f\u0002\u000e\u0002}\u000b\u0002\u0003\u0002\u0005\u0002\u0080\n\u0002",
    "\u0003\u0002\u0005\u0002\u0083\n\u0002\u0003\u0002\u0007\u0002\u0086",
    "\n\u0002\f\u0002\u000e\u0002\u0089\u000b\u0002\u0003\u0002\u0003\u0002",
    "\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003",
    "\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003",
    "\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003",
    "\u0003\u0003\u0003\u0003\u0005\u0003\u00a1\n\u0003\u0003\u0004\u0003",
    "\u0004\u0003\u0004\u0003\u0004\u0003\u0004\u0003\u0004\u0003\u0004\u0007",
    "\u0004\u00aa\n\u0004\f\u0004\u000e\u0004\u00ad\u000b\u0004\u0003\u0004",
    "\u0003\u0004\u0003\u0004\u0003\u0005\u0006\u0005\u00b3\n\u0005\r\u0005",
    "\u000e\u0005\u00b4\u0003\u0005\u0003\u0005\u0006\u0005\u00b9\n\u0005",
    "\r\u0005\u000e\u0005\u00ba\u0003\u0005\u0003\u0005\u0006\u0005\u00bf",
    "\n\u0005\r\u0005\u000e\u0005\u00c0\u0003\u0005\u0003\u0005\u0006\u0005",
    "\u00c5\n\u0005\r\u0005\u000e\u0005\u00c6\u0003\u0005\u0006\u0005\u00ca",
    "\n\u0005\r\u0005\u000e\u0005\u00cb\u0003\u0005\u0003\u0005\u0003\u0005",
    "\u0006\u0005\u00d1\n\u0005\r\u0005\u000e\u0005\u00d2\u0003\u0005\u0003",
    "\u0005\u0003\u0005\u0006\u0005\u00d8\n\u0005\r\u0005\u000e\u0005\u00d9",
    "\u0003\u0005\u0003\u0005\u0003\u0005\u0006\u0005\u00df\n\u0005\r\u0005",
    "\u000e\u0005\u00e0\u0003\u0005\u0005\u0005\u00e4\n\u0005\u0003\u0006",
    "\u0003\u0006\u0003\u0006\u0003\u0006\u0006\u0006\u00ea\n\u0006\r\u0006",
    "\u000e\u0006\u00eb\u0003\u0006\u0003\u0006\u0003\u0007\u0003\u0007\u0003",
    "\b\u0003\b\u0003\t\u0003\t\u0003\n\u0003\n\u0003\n\u0003\n\u0006\n\u00fa",
    "\n\n\r\n\u000e\n\u00fb\u0003\n\u0003\n\u0003\u000b\u0003\u000b\u0003",
    "\f\u0003\f\u0003\r\u0003\r\u0003\u000e\u0003\u000e\u0003\u000f\u0003",
    "\u000f\u0003\u0010\u0003\u0010\u0003\u0011\u0003\u0011\u0005\u0011\u010e",
    "\n\u0011\u0003\u0012\u0003\u0012\u0005\u0012\u0112\n\u0012\u0003\u0013",
    "\u0003\u0013\u0003\u0013\u0003\u0014\u0003\u0014\u0003\u0014\u0003\u0015",
    "\u0003\u0015\u0003\u0015\u0003\u0016\u0003\u0016\u0005\u0016\u011f\n",
    "\u0016\u0003\u0017\u0003\u0017\u0003\u0017\u0005\u0017\u0124\n\u0017",
    "\u0003\u0017\u0005\u0017\u0127\n\u0017\u0003\u0018\u0003\u0018\u0003",
    "\u0018\u0003\u0019\u0003\u0019\u0003\u0019\u0003\u0019\u0003\u0019\u0003",
    "\u0019\u0005\u0019\u0132\n\u0019\u0003\u0019\u0003\u0019\u0003\u0019",
    "\u0003\u0019\u0003\u0019\u0003\u0019\u0007\u0019\u013a\n\u0019\f\u0019",
    "\u000e\u0019\u013d\u000b\u0019\u0003\u001a\u0003\u001a\u0003\u001a\u0003",
    "\u001b\u0003\u001b\u0003\u001b\u0003\u001b\u0003\u001b\u0005\u001b\u0147",
    "\n\u001b\u0003\u001c\u0003\u001c\u0003\u001c\u0003\u001d\u0003\u001d",
    "\u0003\u001d\u0003\u001d\u0003\u001d\u0005\u001d\u0151\n\u001d\u0003",
    "\u001e\u0003\u001e\u0003\u001e\u0003\u001f\u0003\u001f\u0003\u001f\u0003",
    " \u0003 \u0003 \u0003 \u0003 \u0003 \u0003 \u0003 \u0005 \u0161\n \u0005",
    " \u0163\n \u0003 \u0003 \u0003 \u0003 \u0003 \u0003 \u0007 \u016b\n",
    " \f \u000e \u016e\u000b \u0003!\u0003!\u0003!\u0003\"\u0003\"\u0003",
    "\"\u0003#\u0003#\u0003#\u0003$\u0003$\u0003$\u0003$\u0003$\u0003$\u0003",
    "$\u0005$\u0180\n$\u0005$\u0182\n$\u0003$\u0003$\u0003$\u0003$\u0003",
    "$\u0003$\u0007$\u018a\n$\f$\u000e$\u018d\u000b$\u0003%\u0003%\u0003",
    "%\u0003&\u0003&\u0003&\u0005&\u0195\n&\u0003&\u0005&\u0198\n&\u0003",
    "\'\u0003\'\u0003\'\u0003(\u0003(\u0003(\u0003(\u0003(\u0003(\u0003(",
    "\u0003(\u0005(\u01a5\n(\u0005(\u01a7\n(\u0003(\u0003(\u0003(\u0003(",
    "\u0003(\u0003(\u0007(\u01af\n(\f(\u000e(\u01b2\u000b(\u0003)\u0003)",
    "\u0005)\u01b6\n)\u0003*\u0003*\u0003*\u0005*\u01bb\n*\u0003*\u0005*",
    "\u01be\n*\u0003+\u0003+\u0003+\u0003,\u0003,\u0003,\u0003,\u0003,\u0003",
    ",\u0003,\u0003,\u0005,\u01cb\n,\u0005,\u01cd\n,\u0003,\u0003,\u0003",
    ",\u0003,\u0003,\u0003,\u0007,\u01d5\n,\f,\u000e,\u01d8\u000b,\u0003",
    "-\u0003-\u0005-\u01dc\n-\u0003.\u0003.\u0003.\u0003.\u0003.\u0003.\u0005",
    ".\u01e4\n.\u0003/\u0003/\u0003/\u00030\u00030\u00030\u00031\u00031\u0003",
    "1\u00031\u00031\u00031\u00031\u00051\u01f3\n1\u00051\u01f5\n1\u0003",
    "1\u00031\u00031\u00031\u00031\u00031\u00071\u01fd\n1\f1\u000e1\u0200",
    "\u000b1\u00032\u00032\u00052\u0204\n2\u00033\u00033\u00033\u00034\u0003",
    "4\u00034\u00034\u00034\u00034\u00054\u020f\n4\u00034\u00034\u00034\u0003",
    "4\u00034\u00034\u00074\u0217\n4\f4\u000e4\u021a\u000b4\u00035\u0003",
    "5\u00035\u00036\u00036\u00036\u00056\u0222\n6\u00036\u00056\u0225\n",
    "6\u00037\u00037\u00037\u00038\u00038\u00038\u00038\u00038\u00038\u0003",
    "8\u00038\u00058\u0232\n8\u00058\u0234\n8\u00038\u00038\u00038\u0003",
    "8\u00038\u00038\u00078\u023c\n8\f8\u000e8\u023f\u000b8\u00039\u0003",
    "9\u00059\u0243\n9\u0003:\u0003:\u0003:\u0003;\u0003;\u0003;\u0003;\u0003",
    ";\u0003;\u0003;\u0003;\u0003;\u0003;\u0003;\u0003;\u0003;\u0005;\u0255",
    "\n;\u0005;\u0257\n;\u0003;\u0003;\u0003;\u0003;\u0003;\u0003;\u0007",
    ";\u025f\n;\f;\u000e;\u0262\u000b;\u0003<\u0003<\u0003<\u0002\u000b0",
    ">FNV`fnt=\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018",
    "\u001a\u001c\u001e \"$&(*,.02468:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtv\u0002",
    "\u0003\u0004\u0002\t\u0011\u001b\u001c\u0002\u0286\u0002\u007f\u0003",
    "\u0002\u0002\u0002\u0004\u00a0\u0003\u0002\u0002\u0002\u0006\u00a2\u0003",
    "\u0002\u0002\u0002\b\u00e3\u0003\u0002\u0002\u0002\n\u00e5\u0003\u0002",
    "\u0002\u0002\f\u00ef\u0003\u0002\u0002\u0002\u000e\u00f1\u0003\u0002",
    "\u0002\u0002\u0010\u00f3\u0003\u0002\u0002\u0002\u0012\u00f5\u0003\u0002",
    "\u0002\u0002\u0014\u00ff\u0003\u0002\u0002\u0002\u0016\u0101\u0003\u0002",
    "\u0002\u0002\u0018\u0103\u0003\u0002\u0002\u0002\u001a\u0105\u0003\u0002",
    "\u0002\u0002\u001c\u0107\u0003\u0002\u0002\u0002\u001e\u0109\u0003\u0002",
    "\u0002\u0002 \u010d\u0003\u0002\u0002\u0002\"\u010f\u0003\u0002\u0002",
    "\u0002$\u0113\u0003\u0002\u0002\u0002&\u0116\u0003\u0002\u0002\u0002",
    "(\u0119\u0003\u0002\u0002\u0002*\u011c\u0003\u0002\u0002\u0002,\u0126",
    "\u0003\u0002\u0002\u0002.\u0128\u0003\u0002\u0002\u00020\u0131\u0003",
    "\u0002\u0002\u00022\u013e\u0003\u0002\u0002\u00024\u0141\u0003\u0002",
    "\u0002\u00026\u0148\u0003\u0002\u0002\u00028\u014b\u0003\u0002\u0002",
    "\u0002:\u0152\u0003\u0002\u0002\u0002<\u0155\u0003\u0002\u0002\u0002",
    ">\u0162\u0003\u0002\u0002\u0002@\u016f\u0003\u0002\u0002\u0002B\u0172",
    "\u0003\u0002\u0002\u0002D\u0175\u0003\u0002\u0002\u0002F\u0181\u0003",
    "\u0002\u0002\u0002H\u018e\u0003\u0002\u0002\u0002J\u0197\u0003\u0002",
    "\u0002\u0002L\u0199\u0003\u0002\u0002\u0002N\u01a6\u0003\u0002\u0002",
    "\u0002P\u01b3\u0003\u0002\u0002\u0002R\u01bd\u0003\u0002\u0002\u0002",
    "T\u01bf\u0003\u0002\u0002\u0002V\u01cc\u0003\u0002\u0002\u0002X\u01d9",
    "\u0003\u0002\u0002\u0002Z\u01e3\u0003\u0002\u0002\u0002\\\u01e5\u0003",
    "\u0002\u0002\u0002^\u01e8\u0003\u0002\u0002\u0002`\u01f4\u0003\u0002",
    "\u0002\u0002b\u0201\u0003\u0002\u0002\u0002d\u0205\u0003\u0002\u0002",
    "\u0002f\u020e\u0003\u0002\u0002\u0002h\u021b\u0003\u0002\u0002\u0002",
    "j\u0224\u0003\u0002\u0002\u0002l\u0226\u0003\u0002\u0002\u0002n\u0233",
    "\u0003\u0002\u0002\u0002p\u0240\u0003\u0002\u0002\u0002r\u0244\u0003",
    "\u0002\u0002\u0002t\u0256\u0003\u0002\u0002\u0002v\u0263\u0003\u0002",
    "\u0002\u0002xz\u0005\u0010\t\u0002yx\u0003\u0002\u0002\u0002z}\u0003",
    "\u0002\u0002\u0002{y\u0003\u0002\u0002\u0002{|\u0003\u0002\u0002\u0002",
    "|\u0080\u0003\u0002\u0002\u0002}{\u0003\u0002\u0002\u0002~\u0080\u0005",
    "\u0004\u0003\u0002\u007f{\u0003\u0002\u0002\u0002\u007f~\u0003\u0002",
    "\u0002\u0002\u0080\u0082\u0003\u0002\u0002\u0002\u0081\u0083\u0005\u000e",
    "\b\u0002\u0082\u0081\u0003\u0002\u0002\u0002\u0082\u0083\u0003\u0002",
    "\u0002\u0002\u0083\u0087\u0003\u0002\u0002\u0002\u0084\u0086\u0007\u001a",
    "\u0002\u0002\u0085\u0084\u0003\u0002\u0002\u0002\u0086\u0089\u0003\u0002",
    "\u0002\u0002\u0087\u0085\u0003\u0002\u0002\u0002\u0087\u0088\u0003\u0002",
    "\u0002\u0002\u0088\u008a\u0003\u0002\u0002\u0002\u0089\u0087\u0003\u0002",
    "\u0002\u0002\u008a\u008b\u0007\u0002\u0002\u0003\u008b\u0003\u0003\u0002",
    "\u0002\u0002\u008c\u008d\u0005:\u001e\u0002\u008d\u008e\u0005\u0014",
    "\u000b\u0002\u008e\u008f\u0005\u001c\u000f\u0002\u008f\u0090\u0005>",
    " \u0002\u0090\u00a1\u0003\u0002\u0002\u0002\u0091\u0092\u0005@!\u0002",
    "\u0092\u0093\u0005\u0014\u000b\u0002\u0093\u0094\u0005\u001c\u000f\u0002",
    "\u0094\u0095\u0005F$\u0002\u0095\u00a1\u0003\u0002\u0002\u0002\u0096",
    "\u0097\u0005p9\u0002\u0097\u0098\u0005\u0014\u000b\u0002\u0098\u0099",
    "\u0005\u001c\u000f\u0002\u0099\u009a\u0005t;\u0002\u009a\u00a1\u0003",
    "\u0002\u0002\u0002\u009b\u009c\u0005\\/\u0002\u009c\u009d\u0005\u0014",
    "\u000b\u0002\u009d\u009e\u0005\u001c\u000f\u0002\u009e\u009f\u0005`",
    "1\u0002\u009f\u00a1\u0003\u0002\u0002\u0002\u00a0\u008c\u0003\u0002",
    "\u0002\u0002\u00a0\u0091\u0003\u0002\u0002\u0002\u00a0\u0096\u0003\u0002",
    "\u0002\u0002\u00a0\u009b\u0003\u0002\u0002\u0002\u00a1\u0005\u0003\u0002",
    "\u0002\u0002\u00a2\u00ab\u0007\u0003\u0002\u0002\u00a3\u00a4\u0005\b",
    "\u0005\u0002\u00a4\u00a5\u0007\u0004\u0002\u0002\u00a5\u00aa\u0003\u0002",
    "\u0002\u0002\u00a6\u00a7\u0005\b\u0005\u0002\u00a7\u00a8\u0007\u0005",
    "\u0002\u0002\u00a8\u00aa\u0003\u0002\u0002\u0002\u00a9\u00a3\u0003\u0002",
    "\u0002\u0002\u00a9\u00a6\u0003\u0002\u0002\u0002\u00aa\u00ad\u0003\u0002",
    "\u0002\u0002\u00ab\u00a9\u0003\u0002\u0002\u0002\u00ab\u00ac\u0003\u0002",
    "\u0002\u0002\u00ac\u00ae\u0003\u0002\u0002\u0002\u00ad\u00ab\u0003\u0002",
    "\u0002\u0002\u00ae\u00af\u0005\b\u0005\u0002\u00af\u00b0\u0007\u0003",
    "\u0002\u0002\u00b0\u0007\u0003\u0002\u0002\u0002\u00b1\u00b3\u0007\u0019",
    "\u0002\u0002\u00b2\u00b1\u0003\u0002\u0002\u0002\u00b3\u00b4\u0003\u0002",
    "\u0002\u0002\u00b4\u00b2\u0003\u0002\u0002\u0002\u00b4\u00b5\u0003\u0002",
    "\u0002\u0002\u00b5\u00e4\u0003\u0002\u0002\u0002\u00b6\u00b8\u0007\u0006",
    "\u0002\u0002\u00b7\u00b9\u0007\u0019\u0002\u0002\u00b8\u00b7\u0003\u0002",
    "\u0002\u0002\u00b9\u00ba\u0003\u0002\u0002\u0002\u00ba\u00b8\u0003\u0002",
    "\u0002\u0002\u00ba\u00bb\u0003\u0002\u0002\u0002\u00bb\u00e4\u0003\u0002",
    "\u0002\u0002\u00bc\u00be\u0007\u0007\u0002\u0002\u00bd\u00bf\u0007\u0019",
    "\u0002\u0002\u00be\u00bd\u0003\u0002\u0002\u0002\u00bf\u00c0\u0003\u0002",
    "\u0002\u0002\u00c0\u00be\u0003\u0002\u0002\u0002\u00c0\u00c1\u0003\u0002",
    "\u0002\u0002\u00c1\u00e4\u0003\u0002\u0002\u0002\u00c2\u00c4\u0007\b",
    "\u0002\u0002\u00c3\u00c5\u0007\u0019\u0002\u0002\u00c4\u00c3\u0003\u0002",
    "\u0002\u0002\u00c5\u00c6\u0003\u0002\u0002\u0002\u00c6\u00c4\u0003\u0002",
    "\u0002\u0002\u00c6\u00c7\u0003\u0002\u0002\u0002\u00c7\u00e4\u0003\u0002",
    "\u0002\u0002\u00c8\u00ca\u0007\u0019\u0002\u0002\u00c9\u00c8\u0003\u0002",
    "\u0002\u0002\u00ca\u00cb\u0003\u0002\u0002\u0002\u00cb\u00c9\u0003\u0002",
    "\u0002\u0002\u00cb\u00cc\u0003\u0002\u0002\u0002\u00cc\u00cd\u0003\u0002",
    "\u0002\u0002\u00cd\u00e4\u0007\u0007\u0002\u0002\u00ce\u00d0\u0007\u0006",
    "\u0002\u0002\u00cf\u00d1\u0007\u0019\u0002\u0002\u00d0\u00cf\u0003\u0002",
    "\u0002\u0002\u00d1\u00d2\u0003\u0002\u0002\u0002\u00d2\u00d0\u0003\u0002",
    "\u0002\u0002\u00d2\u00d3\u0003\u0002\u0002\u0002\u00d3\u00d4\u0003\u0002",
    "\u0002\u0002\u00d4\u00e4\u0007\u0007\u0002\u0002\u00d5\u00d7\u0007\u0007",
    "\u0002\u0002\u00d6\u00d8\u0007\u0019\u0002\u0002\u00d7\u00d6\u0003\u0002",
    "\u0002\u0002\u00d8\u00d9\u0003\u0002\u0002\u0002\u00d9\u00d7\u0003\u0002",
    "\u0002\u0002\u00d9\u00da\u0003\u0002\u0002\u0002\u00da\u00db\u0003\u0002",
    "\u0002\u0002\u00db\u00e4\u0007\u0007\u0002\u0002\u00dc\u00de\u0007\b",
    "\u0002\u0002\u00dd\u00df\u0007\u0019\u0002\u0002\u00de\u00dd\u0003\u0002",
    "\u0002\u0002\u00df\u00e0\u0003\u0002\u0002\u0002\u00e0\u00de\u0003\u0002",
    "\u0002\u0002\u00e0\u00e1\u0003\u0002\u0002\u0002\u00e1\u00e2\u0003\u0002",
    "\u0002\u0002\u00e2\u00e4\u0007\u0007\u0002\u0002\u00e3\u00b2\u0003\u0002",
    "\u0002\u0002\u00e3\u00b6\u0003\u0002\u0002\u0002\u00e3\u00bc\u0003\u0002",
    "\u0002\u0002\u00e3\u00c2\u0003\u0002\u0002\u0002\u00e3\u00c9\u0003\u0002",
    "\u0002\u0002\u00e3\u00ce\u0003\u0002\u0002\u0002\u00e3\u00d5\u0003\u0002",
    "\u0002\u0002\u00e3\u00dc\u0003\u0002\u0002\u0002\u00e4\t\u0003\u0002",
    "\u0002\u0002\u00e5\u00e9\u0007\u0003\u0002\u0002\u00e6\u00ea\u0007\u0019",
    "\u0002\u0002\u00e7\u00ea\u0005\f\u0007\u0002\u00e8\u00ea\u0007\u0018",
    "\u0002\u0002\u00e9\u00e6\u0003\u0002\u0002\u0002\u00e9\u00e7\u0003\u0002",
    "\u0002\u0002\u00e9\u00e8\u0003\u0002\u0002\u0002\u00ea\u00eb\u0003\u0002",
    "\u0002\u0002\u00eb\u00e9\u0003\u0002\u0002\u0002\u00eb\u00ec\u0003\u0002",
    "\u0002\u0002\u00ec\u00ed\u0003\u0002\u0002\u0002\u00ed\u00ee\u0007\u0003",
    "\u0002\u0002\u00ee\u000b\u0003\u0002\u0002\u0002\u00ef\u00f0\t\u0002",
    "\u0002\u0002\u00f0\r\u0003\u0002\u0002\u0002\u00f1\u00f2\u0007\t\u0002",
    "\u0002\u00f2\u000f\u0003\u0002\u0002\u0002\u00f3\u00f4\u0007\u001a\u0002",
    "\u0002\u00f4\u0011\u0003\u0002\u0002\u0002\u00f5\u00f9\u0007\u0003\u0002",
    "\u0002\u00f6\u00fa\u0007\u0019\u0002\u0002\u00f7\u00fa\u0005\f\u0007",
    "\u0002\u00f8\u00fa\u0007\u0018\u0002\u0002\u00f9\u00f6\u0003\u0002\u0002",
    "\u0002\u00f9\u00f7\u0003\u0002\u0002\u0002\u00f9\u00f8\u0003\u0002\u0002",
    "\u0002\u00fa\u00fb\u0003\u0002\u0002\u0002\u00fb\u00f9\u0003\u0002\u0002",
    "\u0002\u00fb\u00fc\u0003\u0002\u0002\u0002\u00fc\u00fd\u0003\u0002\u0002",
    "\u0002\u00fd\u00fe\u0007\u0003\u0002\u0002\u00fe\u0013\u0003\u0002\u0002",
    "\u0002\u00ff\u0100\u0007\u0012\u0002\u0002\u0100\u0015\u0003\u0002\u0002",
    "\u0002\u0101\u0102\u0007\u0013\u0002\u0002\u0102\u0017\u0003\u0002\u0002",
    "\u0002\u0103\u0104\u0007\u0014\u0002\u0002\u0104\u0019\u0003\u0002\u0002",
    "\u0002\u0105\u0106\u0007\u0015\u0002\u0002\u0106\u001b\u0003\u0002\u0002",
    "\u0002\u0107\u0108\u0007\u0016\u0002\u0002\u0108\u001d\u0003\u0002\u0002",
    "\u0002\u0109\u010a\u0007\u0017\u0002\u0002\u010a\u001f\u0003\u0002\u0002",
    "\u0002\u010b\u010e\u0005\u0018\r\u0002\u010c\u010e\u0005\u001a\u000e",
    "\u0002\u010d\u010b\u0003\u0002\u0002\u0002\u010d\u010c\u0003\u0002\u0002",
    "\u0002\u010e!\u0003\u0002\u0002\u0002\u010f\u0111\u0007\u001d\u0002",
    "\u0002\u0110\u0112\u0005$\u0013\u0002\u0111\u0110\u0003\u0002\u0002",
    "\u0002\u0111\u0112\u0003\u0002\u0002\u0002\u0112#\u0003\u0002\u0002",
    "\u0002\u0113\u0114\u0005\u0006\u0004\u0002\u0114\u0115\u0007\u0018\u0002",
    "\u0002\u0115%\u0003\u0002\u0002\u0002\u0116\u0117\u0007\u001e\u0002",
    "\u0002\u0117\u0118\u0005(\u0015\u0002\u0118\'\u0003\u0002\u0002\u0002",
    "\u0119\u011a\u0005\u0006\u0004\u0002\u011a\u011b\u0007\u0018\u0002\u0002",
    "\u011b)\u0003\u0002\u0002\u0002\u011c\u011e\u0007\u001f\u0002\u0002",
    "\u011d\u011f\u0005,\u0017\u0002\u011e\u011d\u0003\u0002\u0002\u0002",
    "\u011e\u011f\u0003\u0002\u0002\u0002\u011f+\u0003\u0002\u0002\u0002",
    "\u0120\u0121\u0005\n\u0006\u0002\u0121\u0123\u0007\u0018\u0002\u0002",
    "\u0122\u0124\u0005.\u0018\u0002\u0123\u0122\u0003\u0002\u0002\u0002",
    "\u0123\u0124\u0003\u0002\u0002\u0002\u0124\u0127\u0003\u0002\u0002\u0002",
    "\u0125\u0127\u0005.\u0018\u0002\u0126\u0120\u0003\u0002\u0002\u0002",
    "\u0126\u0125\u0003\u0002\u0002\u0002\u0127-\u0003\u0002\u0002\u0002",
    "\u0128\u0129\u0005\u001e\u0010\u0002\u0129\u012a\u00050\u0019\u0002",
    "\u012a/\u0003\u0002\u0002\u0002\u012b\u012c\b\u0019\u0001\u0002\u012c",
    "\u012d\u0007\u001b\u0002\u0002\u012d\u012e\u00050\u0019\u0002\u012e",
    "\u012f\u0007\u001c\u0002\u0002\u012f\u0132\u0003\u0002\u0002\u0002\u0130",
    "\u0132\u0005H%\u0002\u0131\u012b\u0003\u0002\u0002\u0002\u0131\u0130",
    "\u0003\u0002\u0002\u0002\u0132\u013b\u0003\u0002\u0002\u0002\u0133\u0134",
    "\f\u0005\u0002\u0002\u0134\u0135\u0005 \u0011\u0002\u0135\u0136\u0005",
    "0\u0019\u0006\u0136\u013a\u0003\u0002\u0002\u0002\u0137\u0138\f\u0003",
    "\u0002\u0002\u0138\u013a\u0007\u0018\u0002\u0002\u0139\u0133\u0003\u0002",
    "\u0002\u0002\u0139\u0137\u0003\u0002\u0002\u0002\u013a\u013d\u0003\u0002",
    "\u0002\u0002\u013b\u0139\u0003\u0002\u0002\u0002\u013b\u013c\u0003\u0002",
    "\u0002\u0002\u013c1\u0003\u0002\u0002\u0002\u013d\u013b\u0003\u0002",
    "\u0002\u0002\u013e\u013f\u0007 \u0002\u0002\u013f\u0140\u00054\u001b",
    "\u0002\u01403\u0003\u0002\u0002\u0002\u0141\u0146\u0005\u0016\f\u0002",
    "\u0142\u0143\u0005\n\u0006\u0002\u0143\u0144\u0007\u0018\u0002\u0002",
    "\u0144\u0147\u0003\u0002\u0002\u0002\u0145\u0147\u0007!\u0002\u0002",
    "\u0146\u0142\u0003\u0002\u0002\u0002\u0146\u0145\u0003\u0002\u0002\u0002",
    "\u01475\u0003\u0002\u0002\u0002\u0148\u0149\u0007\"\u0002\u0002\u0149",
    "\u014a\u00058\u001d\u0002\u014a7\u0003\u0002\u0002\u0002\u014b\u0150",
    "\u0005\u0016\f\u0002\u014c\u014d\u0005\n\u0006\u0002\u014d\u014e\u0007",
    "\u0018\u0002\u0002\u014e\u0151\u0003\u0002\u0002\u0002\u014f\u0151\u0007",
    "#\u0002\u0002\u0150\u014c\u0003\u0002\u0002\u0002\u0150\u014f\u0003",
    "\u0002\u0002\u0002\u01519\u0003\u0002\u0002\u0002\u0152\u0153\u0007",
    "$\u0002\u0002\u0153\u0154\u0005<\u001f\u0002\u0154;\u0003\u0002\u0002",
    "\u0002\u0155\u0156\u0005\u001e\u0010\u0002\u0156\u0157\u0005> \u0002",
    "\u0157=\u0003\u0002\u0002\u0002\u0158\u0159\b \u0001\u0002\u0159\u015a",
    "\u0007\u001b\u0002\u0002\u015a\u015b\u0005> \u0002\u015b\u015c\u0007",
    "\u001c\u0002\u0002\u015c\u0163\u0003\u0002\u0002\u0002\u015d\u0161\u0005",
    "*\u0016\u0002\u015e\u0161\u0005X-\u0002\u015f\u0161\u0005P)\u0002\u0160",
    "\u015d\u0003\u0002\u0002\u0002\u0160\u015e\u0003\u0002\u0002\u0002\u0160",
    "\u015f\u0003\u0002\u0002\u0002\u0161\u0163\u0003\u0002\u0002\u0002\u0162",
    "\u0158\u0003\u0002\u0002\u0002\u0162\u0160\u0003\u0002\u0002\u0002\u0163",
    "\u016c\u0003\u0002\u0002\u0002\u0164\u0165\f\u0005\u0002\u0002\u0165",
    "\u0166\u0005 \u0011\u0002\u0166\u0167\u0005> \u0006\u0167\u016b\u0003",
    "\u0002\u0002\u0002\u0168\u0169\f\u0003\u0002\u0002\u0169\u016b\u0007",
    "\u0018\u0002\u0002\u016a\u0164\u0003\u0002\u0002\u0002\u016a\u0168\u0003",
    "\u0002\u0002\u0002\u016b\u016e\u0003\u0002\u0002\u0002\u016c\u016a\u0003",
    "\u0002\u0002\u0002\u016c\u016d\u0003\u0002\u0002\u0002\u016d?\u0003",
    "\u0002\u0002\u0002\u016e\u016c\u0003\u0002\u0002\u0002\u016f\u0170\u0007",
    "%\u0002\u0002\u0170\u0171\u0005D#\u0002\u0171A\u0003\u0002\u0002\u0002",
    "\u0172\u0173\u0005\u0016\f\u0002\u0173\u0174\u0005p9\u0002\u0174C\u0003",
    "\u0002\u0002\u0002\u0175\u0176\u0005\u001e\u0010\u0002\u0176\u0177\u0005",
    "F$\u0002\u0177E\u0003\u0002\u0002\u0002\u0178\u0179\b$\u0001\u0002\u0179",
    "\u017a\u0007\u001b\u0002\u0002\u017a\u017b\u0005F$\u0002\u017b\u017c",
    "\u0007\u001c\u0002\u0002\u017c\u0182\u0003\u0002\u0002\u0002\u017d\u0180",
    "\u0005*\u0016\u0002\u017e\u0180\u0005P)\u0002\u017f\u017d\u0003\u0002",
    "\u0002\u0002\u017f\u017e\u0003\u0002\u0002\u0002\u0180\u0182\u0003\u0002",
    "\u0002\u0002\u0181\u0178\u0003\u0002\u0002\u0002\u0181\u017f\u0003\u0002",
    "\u0002\u0002\u0182\u018b\u0003\u0002\u0002\u0002\u0183\u0184\f\u0005",
    "\u0002\u0002\u0184\u0185\u0005 \u0011\u0002\u0185\u0186\u0005F$\u0006",
    "\u0186\u018a\u0003\u0002\u0002\u0002\u0187\u0188\f\u0003\u0002\u0002",
    "\u0188\u018a\u0007\u0018\u0002\u0002\u0189\u0183\u0003\u0002\u0002\u0002",
    "\u0189\u0187\u0003\u0002\u0002\u0002\u018a\u018d\u0003\u0002\u0002\u0002",
    "\u018b\u0189\u0003\u0002\u0002\u0002\u018b\u018c\u0003\u0002\u0002\u0002",
    "\u018cG\u0003\u0002\u0002\u0002\u018d\u018b\u0003\u0002\u0002\u0002",
    "\u018e\u018f\u0007&\u0002\u0002\u018f\u0190\u0005J&\u0002\u0190I\u0003",
    "\u0002\u0002\u0002\u0191\u0192\u0005\n\u0006\u0002\u0192\u0194\u0007",
    "\u0018\u0002\u0002\u0193\u0195\u0005L\'\u0002\u0194\u0193\u0003\u0002",
    "\u0002\u0002\u0194\u0195\u0003\u0002\u0002\u0002\u0195\u0198\u0003\u0002",
    "\u0002\u0002\u0196\u0198\u0005L\'\u0002\u0197\u0191\u0003\u0002\u0002",
    "\u0002\u0197\u0196\u0003\u0002\u0002\u0002\u0198K\u0003\u0002\u0002",
    "\u0002\u0199\u019a\u0005\u001e\u0010\u0002\u019a\u019b\u0005N(\u0002",
    "\u019bM\u0003\u0002\u0002\u0002\u019c\u019d\b(\u0001\u0002\u019d\u019e",
    "\u0007\u001b\u0002\u0002\u019e\u019f\u0005N(\u0002\u019f\u01a0\u0007",
    "\u001c\u0002\u0002\u01a0\u01a7\u0003\u0002\u0002\u0002\u01a1\u01a5\u0005",
    "X-\u0002\u01a2\u01a5\u0005\"\u0012\u0002\u01a3\u01a5\u0005&\u0014\u0002",
    "\u01a4\u01a1\u0003\u0002\u0002\u0002\u01a4\u01a2\u0003\u0002\u0002\u0002",
    "\u01a4\u01a3\u0003\u0002\u0002\u0002\u01a5\u01a7\u0003\u0002\u0002\u0002",
    "\u01a6\u019c\u0003\u0002\u0002\u0002\u01a6\u01a4\u0003\u0002\u0002\u0002",
    "\u01a7\u01b0\u0003\u0002\u0002\u0002\u01a8\u01a9\f\u0005\u0002\u0002",
    "\u01a9\u01aa\u0005 \u0011\u0002\u01aa\u01ab\u0005N(\u0006\u01ab\u01af",
    "\u0003\u0002\u0002\u0002\u01ac\u01ad\f\u0003\u0002\u0002\u01ad\u01af",
    "\u0007\u0018\u0002\u0002\u01ae\u01a8\u0003\u0002\u0002\u0002\u01ae\u01ac",
    "\u0003\u0002\u0002\u0002\u01af\u01b2\u0003\u0002\u0002\u0002\u01b0\u01ae",
    "\u0003\u0002\u0002\u0002\u01b0\u01b1\u0003\u0002\u0002\u0002\u01b1O",
    "\u0003\u0002\u0002\u0002\u01b2\u01b0\u0003\u0002\u0002\u0002\u01b3\u01b5",
    "\u0007&\u0002\u0002\u01b4\u01b6\u0005R*\u0002\u01b5\u01b4\u0003\u0002",
    "\u0002\u0002\u01b5\u01b6\u0003\u0002\u0002\u0002\u01b6Q\u0003\u0002",
    "\u0002\u0002\u01b7\u01b8\u0005\n\u0006\u0002\u01b8\u01ba\u0007\u0018",
    "\u0002\u0002\u01b9\u01bb\u0005T+\u0002\u01ba\u01b9\u0003\u0002\u0002",
    "\u0002\u01ba\u01bb\u0003\u0002\u0002\u0002\u01bb\u01be\u0003\u0002\u0002",
    "\u0002\u01bc\u01be\u0005T+\u0002\u01bd\u01b7\u0003\u0002\u0002\u0002",
    "\u01bd\u01bc\u0003\u0002\u0002\u0002\u01beS\u0003\u0002\u0002\u0002",
    "\u01bf\u01c0\u0005\u001e\u0010\u0002\u01c0\u01c1\u0005V,\u0002\u01c1",
    "U\u0003\u0002\u0002\u0002\u01c2\u01c3\b,\u0001\u0002\u01c3\u01c4\u0007",
    "\u001b\u0002\u0002\u01c4\u01c5\u0005V,\u0002\u01c5\u01c6\u0007\u001c",
    "\u0002\u0002\u01c6\u01cd\u0003\u0002\u0002\u0002\u01c7\u01cb\u0005X",
    "-\u0002\u01c8\u01cb\u0005\"\u0012\u0002\u01c9\u01cb\u0005*\u0016\u0002",
    "\u01ca\u01c7\u0003\u0002\u0002\u0002\u01ca\u01c8\u0003\u0002\u0002\u0002",
    "\u01ca\u01c9\u0003\u0002\u0002\u0002\u01cb\u01cd\u0003\u0002\u0002\u0002",
    "\u01cc\u01c2\u0003\u0002\u0002\u0002\u01cc\u01ca\u0003\u0002\u0002\u0002",
    "\u01cd\u01d6\u0003\u0002\u0002\u0002\u01ce\u01cf\f\u0005\u0002\u0002",
    "\u01cf\u01d0\u0005 \u0011\u0002\u01d0\u01d1\u0005V,\u0006\u01d1\u01d5",
    "\u0003\u0002\u0002\u0002\u01d2\u01d3\f\u0003\u0002\u0002\u01d3\u01d5",
    "\u0007\u0018\u0002\u0002\u01d4\u01ce\u0003\u0002\u0002\u0002\u01d4\u01d2",
    "\u0003\u0002\u0002\u0002\u01d5\u01d8\u0003\u0002\u0002\u0002\u01d6\u01d4",
    "\u0003\u0002\u0002\u0002\u01d6\u01d7\u0003\u0002\u0002\u0002\u01d7W",
    "\u0003\u0002\u0002\u0002\u01d8\u01d6\u0003\u0002\u0002\u0002\u01d9\u01db",
    "\u0007\'\u0002\u0002\u01da\u01dc\u0005Z.\u0002\u01db\u01da\u0003\u0002",
    "\u0002\u0002\u01db\u01dc\u0003\u0002\u0002\u0002\u01dcY\u0003\u0002",
    "\u0002\u0002\u01dd\u01de\u0005\n\u0006\u0002\u01de\u01df\u0007\u0018",
    "\u0002\u0002\u01df\u01e4\u0003\u0002\u0002\u0002\u01e0\u01e1\u0005\u0006",
    "\u0004\u0002\u01e1\u01e2\u0007\u0018\u0002\u0002\u01e2\u01e4\u0003\u0002",
    "\u0002\u0002\u01e3\u01dd\u0003\u0002\u0002\u0002\u01e3\u01e0\u0003\u0002",
    "\u0002\u0002\u01e4[\u0003\u0002\u0002\u0002\u01e5\u01e6\u0007(\u0002",
    "\u0002\u01e6\u01e7\u0005^0\u0002\u01e7]\u0003\u0002\u0002\u0002\u01e8",
    "\u01e9\u0005\u001e\u0010\u0002\u01e9\u01ea\u0005`1\u0002\u01ea_\u0003",
    "\u0002\u0002\u0002\u01eb\u01ec\b1\u0001\u0002\u01ec\u01ed\u0007\u001b",
    "\u0002\u0002\u01ed\u01ee\u0005`1\u0002\u01ee\u01ef\u0007\u001c\u0002",
    "\u0002\u01ef\u01f5\u0003\u0002\u0002\u0002\u01f0\u01f3\u0005*\u0016",
    "\u0002\u01f1\u01f3\u0005X-\u0002\u01f2\u01f0\u0003\u0002\u0002\u0002",
    "\u01f2\u01f1\u0003\u0002\u0002\u0002\u01f3\u01f5\u0003\u0002\u0002\u0002",
    "\u01f4\u01eb\u0003\u0002\u0002\u0002\u01f4\u01f2\u0003\u0002\u0002\u0002",
    "\u01f5\u01fe\u0003\u0002\u0002\u0002\u01f6\u01f7\f\u0005\u0002\u0002",
    "\u01f7\u01f8\u0005 \u0011\u0002\u01f8\u01f9\u0005`1\u0006\u01f9\u01fd",
    "\u0003\u0002\u0002\u0002\u01fa\u01fb\f\u0003\u0002\u0002\u01fb\u01fd",
    "\u0007\u0018\u0002\u0002\u01fc\u01f6\u0003\u0002\u0002\u0002\u01fc\u01fa",
    "\u0003\u0002\u0002\u0002\u01fd\u0200\u0003\u0002\u0002\u0002\u01fe\u01fc",
    "\u0003\u0002\u0002\u0002\u01fe\u01ff\u0003\u0002\u0002\u0002\u01ffa",
    "\u0003\u0002\u0002\u0002\u0200\u01fe\u0003\u0002\u0002\u0002\u0201\u0203",
    "\u0007)\u0002\u0002\u0202\u0204\u0005d3\u0002\u0203\u0202\u0003\u0002",
    "\u0002\u0002\u0203\u0204\u0003\u0002\u0002\u0002\u0204c\u0003\u0002",
    "\u0002\u0002\u0205\u0206\u0005\u001e\u0010\u0002\u0206\u0207\u0005f",
    "4\u0002\u0207e\u0003\u0002\u0002\u0002\u0208\u0209\b4\u0001\u0002\u0209",
    "\u020a\u0007\u001b\u0002\u0002\u020a\u020b\u0005f4\u0002\u020b\u020c",
    "\u0007\u001c\u0002\u0002\u020c\u020f\u0003\u0002\u0002\u0002\u020d\u020f",
    "\u0005h5\u0002\u020e\u0208\u0003\u0002\u0002\u0002\u020e\u020d\u0003",
    "\u0002\u0002\u0002\u020f\u0218\u0003\u0002\u0002\u0002\u0210\u0211\f",
    "\u0005\u0002\u0002\u0211\u0212\u0005 \u0011\u0002\u0212\u0213\u0005",
    "f4\u0006\u0213\u0217\u0003\u0002\u0002\u0002\u0214\u0215\f\u0003\u0002",
    "\u0002\u0215\u0217\u0007\u0018\u0002\u0002\u0216\u0210\u0003\u0002\u0002",
    "\u0002\u0216\u0214\u0003\u0002\u0002\u0002\u0217\u021a\u0003\u0002\u0002",
    "\u0002\u0218\u0216\u0003\u0002\u0002\u0002\u0218\u0219\u0003\u0002\u0002",
    "\u0002\u0219g\u0003\u0002\u0002\u0002\u021a\u0218\u0003\u0002\u0002",
    "\u0002\u021b\u021c\u0007*\u0002\u0002\u021c\u021d\u0005j6\u0002\u021d",
    "i\u0003\u0002\u0002\u0002\u021e\u021f\u0005\n\u0006\u0002\u021f\u0221",
    "\u0007\u0018\u0002\u0002\u0220\u0222\u0005l7\u0002\u0221\u0220\u0003",
    "\u0002\u0002\u0002\u0221\u0222\u0003\u0002\u0002\u0002\u0222\u0225\u0003",
    "\u0002\u0002\u0002\u0223\u0225\u0005l7\u0002\u0224\u021e\u0003\u0002",
    "\u0002\u0002\u0224\u0223\u0003\u0002\u0002\u0002\u0225k\u0003\u0002",
    "\u0002\u0002\u0226\u0227\u0005\u001e\u0010\u0002\u0227\u0228\u0005n",
    "8\u0002\u0228m\u0003\u0002\u0002\u0002\u0229\u022a\b8\u0001\u0002\u022a",
    "\u022b\u0007\u001b\u0002\u0002\u022b\u022c\u0005n8\u0002\u022c\u022d",
    "\u0007\u001c\u0002\u0002\u022d\u0234\u0003\u0002\u0002\u0002\u022e\u0232",
    "\u0005X-\u0002\u022f\u0232\u0005\"\u0012\u0002\u0230\u0232\u0005&\u0014",
    "\u0002\u0231\u022e\u0003\u0002\u0002\u0002\u0231\u022f\u0003\u0002\u0002",
    "\u0002\u0231\u0230\u0003\u0002\u0002\u0002\u0232\u0234\u0003\u0002\u0002",
    "\u0002\u0233\u0229\u0003\u0002\u0002\u0002\u0233\u0231\u0003\u0002\u0002",
    "\u0002\u0234\u023d\u0003\u0002\u0002\u0002\u0235\u0236\f\u0005\u0002",
    "\u0002\u0236\u0237\u0005 \u0011\u0002\u0237\u0238\u0005n8\u0006\u0238",
    "\u023c\u0003\u0002\u0002\u0002\u0239\u023a\f\u0003\u0002\u0002\u023a",
    "\u023c\u0007\u0018\u0002\u0002\u023b\u0235\u0003\u0002\u0002\u0002\u023b",
    "\u0239\u0003\u0002\u0002\u0002\u023c\u023f\u0003\u0002\u0002\u0002\u023d",
    "\u023b\u0003\u0002\u0002\u0002\u023d\u023e\u0003\u0002\u0002\u0002\u023e",
    "o\u0003\u0002\u0002\u0002\u023f\u023d\u0003\u0002\u0002\u0002\u0240",
    "\u0242\u0007+\u0002\u0002\u0241\u0243\u0005r:\u0002\u0242\u0241\u0003",
    "\u0002\u0002\u0002\u0242\u0243\u0003\u0002\u0002\u0002\u0243q\u0003",
    "\u0002\u0002\u0002\u0244\u0245\u0005\u001e\u0010\u0002\u0245\u0246\u0005",
    "t;\u0002\u0246s\u0003\u0002\u0002\u0002\u0247\u0248\b;\u0001\u0002\u0248",
    "\u0249\u0007\u001b\u0002\u0002\u0249\u024a\u0005t;\u0002\u024a\u024b",
    "\u0007\u001c\u0002\u0002\u024b\u0257\u0003\u0002\u0002\u0002\u024c\u0255",
    "\u0005*\u0016\u0002\u024d\u0255\u00052\u001a\u0002\u024e\u0255\u0005",
    "6\u001c\u0002\u024f\u0255\u0005:\u001e\u0002\u0250\u0255\u0005@!\u0002",
    "\u0251\u0255\u0005\\/\u0002\u0252\u0255\u0005b2\u0002\u0253\u0255\u0005",
    "v<\u0002\u0254\u024c\u0003\u0002\u0002\u0002\u0254\u024d\u0003\u0002",
    "\u0002\u0002\u0254\u024e\u0003\u0002\u0002\u0002\u0254\u024f\u0003\u0002",
    "\u0002\u0002\u0254\u0250\u0003\u0002\u0002\u0002\u0254\u0251\u0003\u0002",
    "\u0002\u0002\u0254\u0252\u0003\u0002\u0002\u0002\u0254\u0253\u0003\u0002",
    "\u0002\u0002\u0255\u0257\u0003\u0002\u0002\u0002\u0256\u0247\u0003\u0002",
    "\u0002\u0002\u0256\u0254\u0003\u0002\u0002\u0002\u0257\u0260\u0003\u0002",
    "\u0002\u0002\u0258\u0259\f\u0005\u0002\u0002\u0259\u025a\u0005 \u0011",
    "\u0002\u025a\u025b\u0005t;\u0006\u025b\u025f\u0003\u0002\u0002\u0002",
    "\u025c\u025d\f\u0003\u0002\u0002\u025d\u025f\u0007\u0018\u0002\u0002",
    "\u025e\u0258\u0003\u0002\u0002\u0002\u025e\u025c\u0003\u0002\u0002\u0002",
    "\u025f\u0262\u0003\u0002\u0002\u0002\u0260\u025e\u0003\u0002\u0002\u0002",
    "\u0260\u0261\u0003\u0002\u0002\u0002\u0261u\u0003\u0002\u0002\u0002",
    "\u0262\u0260\u0003\u0002\u0002\u0002\u0263\u0264\u0007,\u0002\u0002",
    "\u0264w\u0003\u0002\u0002\u0002J{\u007f\u0082\u0087\u00a0\u00a9\u00ab",
    "\u00b4\u00ba\u00c0\u00c6\u00cb\u00d2\u00d9\u00e0\u00e3\u00e9\u00eb\u00f9",
    "\u00fb\u010d\u0111\u011e\u0123\u0126\u0131\u0139\u013b\u0146\u0150\u0160",
    "\u0162\u016a\u016c\u017f\u0181\u0189\u018b\u0194\u0197\u01a4\u01a6\u01ae",
    "\u01b0\u01b5\u01ba\u01bd\u01ca\u01cc\u01d4\u01d6\u01db\u01e3\u01f2\u01f4",
    "\u01fc\u01fe\u0203\u020e\u0216\u0218\u0221\u0224\u0231\u0233\u023b\u023d",
    "\u0242\u0254\u0256\u025e\u0260"].join("");


const atn = new antlr4.atn.ATNDeserializer().deserialize(serializedATN);

const decisionsToDFA = atn.decisionToState.map( (ds, index) => new antlr4.dfa.DFA(ds, index) );

const sharedContextCache = new antlr4.PredictionContextCache();

export default class RulepadGrammarParser extends antlr4.Parser {

    static grammarFileName = "RulepadGrammar.g4";
    static literalNames = [ null, "'\"'", "'||'", "'&&'", "'!'", "'...'", 
                            "'!...'", "'.'", "'='", "'>'", "'<'", "'''", 
                            "'&'", "'|'", "'['", "']'", "'must '", "'of '", 
                            "'and '", "'or '", "'have '", "'with '", null, 
                            null, null, "'('", "')'", "'name '", "'value '", 
                            "'annotation '", "'extension '", "'Superclass'", 
                            "'implementation '", "'Interface '", null, "'constructor '", 
                            "'parameter '", "'type '", null, "'configuration file '", 
                            "'property '", "'class '", "'bean declaration '" ];
    static symbolicNames = [ null, null, null, null, null, null, null, null, 
                             null, null, null, null, null, null, null, null, 
                             null, null, null, null, null, null, "SPACE", 
                             "Alphabet", "NL", "LPAREN", "RPAREN", "NAME", 
                             "VALUE", "ANNOTATION", "EXTENSION", "SUPERCLASS", 
                             "IMPLEMENTATION", "INTERFACE", "FUNCTION", 
                             "CONSTRUCTOR", "PARAMETER", "TYPES", "DeclarationStatement", 
                             "ConfigurationFile", "CONFIGURATION_PROPERTIES", 
                             "CLASSES", "BEAN_DECL" ];
    static ruleNames = [ "inputSentence", "mustClause", "words", "word", 
                         "combinatorialWords", "symbols", "end", "emptyLine", 
                         "comments", "must", "of", "and_", "or_", "have", 
                         "withWord", "binary", "names", "nameCondition", 
                         "values", "valueCondition", "annotations", "annotationCondition", 
                         "annotationConditionTransition", "annotationExpression", 
                         "extensions", "extensionCondition", "implementations", 
                         "implementationCondition", "functions", "functionCondition", 
                         "functionExpression", "constructors", "constructorOf", 
                         "constructorCondition", "constructorExpression", 
                         "parameters", "parameterCondition", "parameterConditionTransition", 
                         "parameterExpression", "functionParameters", "functionParameterCondition", 
                         "functionParameterConditionTransition", "functionParameterExpression", 
                         "types", "typeCondition", "declarationStatements", 
                         "declarationStatementCondition", "declarationStatementExpression", 
                         "configurationFiles", "configurationFileCondition", 
                         "configurationFileExpression", "configurationProperties", 
                         "configurationPropertyCondition", "configurationPropertyConditionTransition", 
                         "configurationPropertyExpression", "classes", "classCondition", 
                         "classExpression", "beans" ];

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
    	case 23:
    	    		return this.annotationExpression_sempred(localctx, predIndex);
    	case 30:
    	    		return this.functionExpression_sempred(localctx, predIndex);
    	case 34:
    	    		return this.constructorExpression_sempred(localctx, predIndex);
    	case 38:
    	    		return this.parameterExpression_sempred(localctx, predIndex);
    	case 42:
    	    		return this.functionParameterExpression_sempred(localctx, predIndex);
    	case 47:
    	    		return this.declarationStatementExpression_sempred(localctx, predIndex);
    	case 50:
    	    		return this.configurationFileExpression_sempred(localctx, predIndex);
    	case 54:
    	    		return this.configurationPropertyExpression_sempred(localctx, predIndex);
    	case 57:
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
	        this.state = 125;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.EOF:
	        case RulepadGrammarParser.T__6:
	        case RulepadGrammarParser.NL:
	            this.state = 121;
	            this._errHandler.sync(this);
	            let _alt = this._interp.adaptivePredict(this._input,0,this._ctx)
	            while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
	                if(_alt===1) {
	                    this.state = 118;
	                    this.emptyLine(); 
	                }
	                this.state = 123;
	                this._errHandler.sync(this);
	                _alt = this._interp.adaptivePredict(this._input,0,this._ctx);
	            }

	            break;
	        case RulepadGrammarParser.FUNCTION:
	        case RulepadGrammarParser.CONSTRUCTOR:
	        case RulepadGrammarParser.DeclarationStatement:
	        case RulepadGrammarParser.CLASSES:
	            this.state = 124;
	            this.mustClause();
	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	        this.state = 128;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        if(_la===RulepadGrammarParser.T__6) {
	            this.state = 127;
	            this.end();
	        }

	        this.state = 133;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        while(_la===RulepadGrammarParser.NL) {
	            this.state = 130;
	            this.match(RulepadGrammarParser.NL);
	            this.state = 135;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	        }
	        this.state = 136;
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
	        this.state = 158;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.FUNCTION:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 138;
	            this.functions();
	            this.state = 139;
	            this.must();
	            this.state = 140;
	            this.have();
	            this.state = 141;
	            this.functionExpression(0);
	            break;
	        case RulepadGrammarParser.CONSTRUCTOR:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 143;
	            this.constructors();
	            this.state = 144;
	            this.must();
	            this.state = 145;
	            this.have();
	            this.state = 146;
	            this.constructorExpression(0);
	            break;
	        case RulepadGrammarParser.CLASSES:
	            this.enterOuterAlt(localctx, 3);
	            this.state = 148;
	            this.classes();
	            this.state = 149;
	            this.must();
	            this.state = 150;
	            this.have();
	            this.state = 151;
	            this.classExpression(0);
	            break;
	        case RulepadGrammarParser.DeclarationStatement:
	            this.enterOuterAlt(localctx, 4);
	            this.state = 153;
	            this.declarationStatements();
	            this.state = 154;
	            this.must();
	            this.state = 155;
	            this.have();
	            this.state = 156;
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
	        this.state = 160;
	        this.match(RulepadGrammarParser.T__0);
	        this.state = 169;
	        this._errHandler.sync(this);
	        let _alt = this._interp.adaptivePredict(this._input,6,this._ctx)
	        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
	            if(_alt===1) {
	                this.state = 167;
	                this._errHandler.sync(this);
	                var la_ = this._interp.adaptivePredict(this._input,5,this._ctx);
	                switch(la_) {
	                case 1:
	                    this.state = 161;
	                    this.word();
	                    this.state = 162;
	                    this.match(RulepadGrammarParser.T__1);
	                    break;

	                case 2:
	                    this.state = 164;
	                    this.word();
	                    this.state = 165;
	                    this.match(RulepadGrammarParser.T__2);
	                    break;

	                } 
	            }
	            this.state = 171;
	            this._errHandler.sync(this);
	            _alt = this._interp.adaptivePredict(this._input,6,this._ctx);
	        }

	        this.state = 172;
	        this.word();
	        this.state = 173;
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
	        this.state = 225;
	        this._errHandler.sync(this);
	        var la_ = this._interp.adaptivePredict(this._input,15,this._ctx);
	        switch(la_) {
	        case 1:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 176; 
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            do {
	                this.state = 175;
	                this.match(RulepadGrammarParser.Alphabet);
	                this.state = 178; 
	                this._errHandler.sync(this);
	                _la = this._input.LA(1);
	            } while(_la===RulepadGrammarParser.Alphabet);
	            break;

	        case 2:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 180;
	            this.match(RulepadGrammarParser.T__3);
	            this.state = 182; 
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            do {
	                this.state = 181;
	                this.match(RulepadGrammarParser.Alphabet);
	                this.state = 184; 
	                this._errHandler.sync(this);
	                _la = this._input.LA(1);
	            } while(_la===RulepadGrammarParser.Alphabet);
	            break;

	        case 3:
	            this.enterOuterAlt(localctx, 3);
	            this.state = 186;
	            this.match(RulepadGrammarParser.T__4);
	            this.state = 188; 
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            do {
	                this.state = 187;
	                this.match(RulepadGrammarParser.Alphabet);
	                this.state = 190; 
	                this._errHandler.sync(this);
	                _la = this._input.LA(1);
	            } while(_la===RulepadGrammarParser.Alphabet);
	            break;

	        case 4:
	            this.enterOuterAlt(localctx, 4);
	            this.state = 192;
	            this.match(RulepadGrammarParser.T__5);
	            this.state = 194; 
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            do {
	                this.state = 193;
	                this.match(RulepadGrammarParser.Alphabet);
	                this.state = 196; 
	                this._errHandler.sync(this);
	                _la = this._input.LA(1);
	            } while(_la===RulepadGrammarParser.Alphabet);
	            break;

	        case 5:
	            this.enterOuterAlt(localctx, 5);
	            this.state = 199; 
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            do {
	                this.state = 198;
	                this.match(RulepadGrammarParser.Alphabet);
	                this.state = 201; 
	                this._errHandler.sync(this);
	                _la = this._input.LA(1);
	            } while(_la===RulepadGrammarParser.Alphabet);
	            this.state = 203;
	            this.match(RulepadGrammarParser.T__4);
	            break;

	        case 6:
	            this.enterOuterAlt(localctx, 6);
	            this.state = 204;
	            this.match(RulepadGrammarParser.T__3);
	            this.state = 206; 
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            do {
	                this.state = 205;
	                this.match(RulepadGrammarParser.Alphabet);
	                this.state = 208; 
	                this._errHandler.sync(this);
	                _la = this._input.LA(1);
	            } while(_la===RulepadGrammarParser.Alphabet);
	            this.state = 210;
	            this.match(RulepadGrammarParser.T__4);
	            break;

	        case 7:
	            this.enterOuterAlt(localctx, 7);
	            this.state = 211;
	            this.match(RulepadGrammarParser.T__4);
	            this.state = 213; 
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            do {
	                this.state = 212;
	                this.match(RulepadGrammarParser.Alphabet);
	                this.state = 215; 
	                this._errHandler.sync(this);
	                _la = this._input.LA(1);
	            } while(_la===RulepadGrammarParser.Alphabet);
	            this.state = 217;
	            this.match(RulepadGrammarParser.T__4);
	            break;

	        case 8:
	            this.enterOuterAlt(localctx, 8);
	            this.state = 218;
	            this.match(RulepadGrammarParser.T__5);
	            this.state = 220; 
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            do {
	                this.state = 219;
	                this.match(RulepadGrammarParser.Alphabet);
	                this.state = 222; 
	                this._errHandler.sync(this);
	                _la = this._input.LA(1);
	            } while(_la===RulepadGrammarParser.Alphabet);
	            this.state = 224;
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
	        this.state = 227;
	        this.match(RulepadGrammarParser.T__0);
	        this.state = 231; 
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        do {
	            this.state = 231;
	            this._errHandler.sync(this);
	            switch(this._input.LA(1)) {
	            case RulepadGrammarParser.Alphabet:
	                this.state = 228;
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
	                this.state = 229;
	                this.symbols();
	                break;
	            case RulepadGrammarParser.SPACE:
	                this.state = 230;
	                this.match(RulepadGrammarParser.SPACE);
	                break;
	            default:
	                throw new antlr4.error.NoViableAltException(this);
	            }
	            this.state = 233; 
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	        } while((((_la) & ~0x1f) == 0 && ((1 << _la) & ((1 << RulepadGrammarParser.T__6) | (1 << RulepadGrammarParser.T__7) | (1 << RulepadGrammarParser.T__8) | (1 << RulepadGrammarParser.T__9) | (1 << RulepadGrammarParser.T__10) | (1 << RulepadGrammarParser.T__11) | (1 << RulepadGrammarParser.T__12) | (1 << RulepadGrammarParser.T__13) | (1 << RulepadGrammarParser.T__14) | (1 << RulepadGrammarParser.SPACE) | (1 << RulepadGrammarParser.Alphabet) | (1 << RulepadGrammarParser.LPAREN) | (1 << RulepadGrammarParser.RPAREN))) !== 0));
	        this.state = 235;
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
	        this.state = 237;
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
	        this.state = 239;
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
	        this.state = 241;
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
	        this.state = 243;
	        this.match(RulepadGrammarParser.T__0);
	        this.state = 247; 
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        do {
	            this.state = 247;
	            this._errHandler.sync(this);
	            switch(this._input.LA(1)) {
	            case RulepadGrammarParser.Alphabet:
	                this.state = 244;
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
	                this.state = 245;
	                this.symbols();
	                break;
	            case RulepadGrammarParser.SPACE:
	                this.state = 246;
	                this.match(RulepadGrammarParser.SPACE);
	                break;
	            default:
	                throw new antlr4.error.NoViableAltException(this);
	            }
	            this.state = 249; 
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	        } while((((_la) & ~0x1f) == 0 && ((1 << _la) & ((1 << RulepadGrammarParser.T__6) | (1 << RulepadGrammarParser.T__7) | (1 << RulepadGrammarParser.T__8) | (1 << RulepadGrammarParser.T__9) | (1 << RulepadGrammarParser.T__10) | (1 << RulepadGrammarParser.T__11) | (1 << RulepadGrammarParser.T__12) | (1 << RulepadGrammarParser.T__13) | (1 << RulepadGrammarParser.T__14) | (1 << RulepadGrammarParser.SPACE) | (1 << RulepadGrammarParser.Alphabet) | (1 << RulepadGrammarParser.LPAREN) | (1 << RulepadGrammarParser.RPAREN))) !== 0));
	        this.state = 251;
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
	        this.state = 253;
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
	        this.state = 255;
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
	        this.state = 257;
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
	        this.state = 259;
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
	        this.state = 261;
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
	        this.state = 263;
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
	        this.state = 267;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.T__17:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 265;
	            this.and_();
	            break;
	        case RulepadGrammarParser.T__18:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 266;
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
	        this.state = 269;
	        this.match(RulepadGrammarParser.NAME);
	        this.state = 271;
	        this._errHandler.sync(this);
	        var la_ = this._interp.adaptivePredict(this._input,21,this._ctx);
	        if(la_===1) {
	            this.state = 270;
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
	        this.state = 273;
	        this.words();
	        this.state = 274;
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



	values() {
	    let localctx = new ValuesContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 36, RulepadGrammarParser.RULE_values);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 276;
	        this.match(RulepadGrammarParser.VALUE);
	        this.state = 277;
	        this.valueCondition();
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



	valueCondition() {
	    let localctx = new ValueConditionContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 38, RulepadGrammarParser.RULE_valueCondition);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 279;
	        this.words();
	        this.state = 280;
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
	    this.enterRule(localctx, 40, RulepadGrammarParser.RULE_annotations);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 282;
	        this.match(RulepadGrammarParser.ANNOTATION);
	        this.state = 284;
	        this._errHandler.sync(this);
	        var la_ = this._interp.adaptivePredict(this._input,22,this._ctx);
	        if(la_===1) {
	            this.state = 283;
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
	    this.enterRule(localctx, 42, RulepadGrammarParser.RULE_annotationCondition);
	    try {
	        this.state = 292;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.T__0:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 286;
	            this.combinatorialWords();
	            this.state = 287;
	            this.match(RulepadGrammarParser.SPACE);
	            this.state = 289;
	            this._errHandler.sync(this);
	            var la_ = this._interp.adaptivePredict(this._input,23,this._ctx);
	            if(la_===1) {
	                this.state = 288;
	                this.annotationConditionTransition();

	            }
	            break;
	        case RulepadGrammarParser.T__20:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 291;
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
	    this.enterRule(localctx, 44, RulepadGrammarParser.RULE_annotationConditionTransition);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 294;
	        this.withWord();
	        this.state = 295;
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
	    const _startState = 46;
	    this.enterRecursionRule(localctx, 46, RulepadGrammarParser.RULE_annotationExpression, _p);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 303;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.LPAREN:
	            this.state = 298;
	            this.match(RulepadGrammarParser.LPAREN);
	            this.state = 299;
	            this.annotationExpression(0);
	            this.state = 300;
	            this.match(RulepadGrammarParser.RPAREN);
	            break;
	        case RulepadGrammarParser.PARAMETER:
	            this.state = 302;
	            this.parameters();
	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	        this._ctx.stop = this._input.LT(-1);
	        this.state = 313;
	        this._errHandler.sync(this);
	        let _alt = this._interp.adaptivePredict(this._input,27,this._ctx)
	        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
	            if(_alt===1) {
	                if(this._parseListeners!==null) {
	                    this.triggerExitRuleEvent();
	                }
	                _prevctx = localctx;
	                this.state = 311;
	                this._errHandler.sync(this);
	                var la_ = this._interp.adaptivePredict(this._input,26,this._ctx);
	                switch(la_) {
	                case 1:
	                    localctx = new AnnotationExpressionContext(this, _parentctx, _parentState);
	                    localctx.left = _prevctx;
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_annotationExpression);
	                    this.state = 305;
	                    if (!( this.precpred(this._ctx, 3))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 3)");
	                    }
	                    this.state = 306;
	                    localctx.op = this.binary();
	                    this.state = 307;
	                    localctx.right = this.annotationExpression(4);
	                    break;

	                case 2:
	                    localctx = new AnnotationExpressionContext(this, _parentctx, _parentState);
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_annotationExpression);
	                    this.state = 309;
	                    if (!( this.precpred(this._ctx, 1))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 1)");
	                    }
	                    this.state = 310;
	                    this.match(RulepadGrammarParser.SPACE);
	                    break;

	                } 
	            }
	            this.state = 315;
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
	    this.enterRule(localctx, 48, RulepadGrammarParser.RULE_extensions);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 316;
	        this.match(RulepadGrammarParser.EXTENSION);
	        this.state = 317;
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
	    this.enterRule(localctx, 50, RulepadGrammarParser.RULE_extensionCondition);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 319;
	        this.of();
	        this.state = 324;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.T__0:
	            this.state = 320;
	            this.combinatorialWords();
	            this.state = 321;
	            this.match(RulepadGrammarParser.SPACE);
	            break;
	        case RulepadGrammarParser.SUPERCLASS:
	            this.state = 323;
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
	    this.enterRule(localctx, 52, RulepadGrammarParser.RULE_implementations);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 326;
	        this.match(RulepadGrammarParser.IMPLEMENTATION);
	        this.state = 327;
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
	    this.enterRule(localctx, 54, RulepadGrammarParser.RULE_implementationCondition);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 329;
	        this.of();
	        this.state = 334;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.T__0:
	            this.state = 330;
	            this.combinatorialWords();
	            this.state = 331;
	            this.match(RulepadGrammarParser.SPACE);
	            break;
	        case RulepadGrammarParser.INTERFACE:
	            this.state = 333;
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
	    this.enterRule(localctx, 56, RulepadGrammarParser.RULE_functions);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 336;
	        this.match(RulepadGrammarParser.FUNCTION);
	        this.state = 337;
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
	    this.enterRule(localctx, 58, RulepadGrammarParser.RULE_functionCondition);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 339;
	        this.withWord();
	        this.state = 340;
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
	    const _startState = 60;
	    this.enterRecursionRule(localctx, 60, RulepadGrammarParser.RULE_functionExpression, _p);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 352;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.LPAREN:
	            this.state = 343;
	            this.match(RulepadGrammarParser.LPAREN);
	            this.state = 344;
	            this.functionExpression(0);
	            this.state = 345;
	            this.match(RulepadGrammarParser.RPAREN);
	            break;
	        case RulepadGrammarParser.ANNOTATION:
	        case RulepadGrammarParser.PARAMETER:
	        case RulepadGrammarParser.TYPES:
	            this.state = 350;
	            this._errHandler.sync(this);
	            switch(this._input.LA(1)) {
	            case RulepadGrammarParser.ANNOTATION:
	                this.state = 347;
	                this.annotations();
	                break;
	            case RulepadGrammarParser.TYPES:
	                this.state = 348;
	                this.types();
	                break;
	            case RulepadGrammarParser.PARAMETER:
	                this.state = 349;
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
	        this.state = 362;
	        this._errHandler.sync(this);
	        let _alt = this._interp.adaptivePredict(this._input,33,this._ctx)
	        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
	            if(_alt===1) {
	                if(this._parseListeners!==null) {
	                    this.triggerExitRuleEvent();
	                }
	                _prevctx = localctx;
	                this.state = 360;
	                this._errHandler.sync(this);
	                var la_ = this._interp.adaptivePredict(this._input,32,this._ctx);
	                switch(la_) {
	                case 1:
	                    localctx = new FunctionExpressionContext(this, _parentctx, _parentState);
	                    localctx.left = _prevctx;
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_functionExpression);
	                    this.state = 354;
	                    if (!( this.precpred(this._ctx, 3))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 3)");
	                    }
	                    this.state = 355;
	                    localctx.op = this.binary();
	                    this.state = 356;
	                    localctx.right = this.functionExpression(4);
	                    break;

	                case 2:
	                    localctx = new FunctionExpressionContext(this, _parentctx, _parentState);
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_functionExpression);
	                    this.state = 358;
	                    if (!( this.precpred(this._ctx, 1))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 1)");
	                    }
	                    this.state = 359;
	                    this.match(RulepadGrammarParser.SPACE);
	                    break;

	                } 
	            }
	            this.state = 364;
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
	    this.enterRule(localctx, 62, RulepadGrammarParser.RULE_constructors);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 365;
	        this.match(RulepadGrammarParser.CONSTRUCTOR);
	        this.state = 366;
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
	    this.enterRule(localctx, 64, RulepadGrammarParser.RULE_constructorOf);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 368;
	        this.of();
	        this.state = 369;
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
	    this.enterRule(localctx, 66, RulepadGrammarParser.RULE_constructorCondition);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 371;
	        this.withWord();
	        this.state = 372;
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
	    const _startState = 68;
	    this.enterRecursionRule(localctx, 68, RulepadGrammarParser.RULE_constructorExpression, _p);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 383;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.LPAREN:
	            this.state = 375;
	            this.match(RulepadGrammarParser.LPAREN);
	            this.state = 376;
	            this.constructorExpression(0);
	            this.state = 377;
	            this.match(RulepadGrammarParser.RPAREN);
	            break;
	        case RulepadGrammarParser.ANNOTATION:
	        case RulepadGrammarParser.PARAMETER:
	            this.state = 381;
	            this._errHandler.sync(this);
	            switch(this._input.LA(1)) {
	            case RulepadGrammarParser.ANNOTATION:
	                this.state = 379;
	                this.annotations();
	                break;
	            case RulepadGrammarParser.PARAMETER:
	                this.state = 380;
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
	        this.state = 393;
	        this._errHandler.sync(this);
	        let _alt = this._interp.adaptivePredict(this._input,37,this._ctx)
	        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
	            if(_alt===1) {
	                if(this._parseListeners!==null) {
	                    this.triggerExitRuleEvent();
	                }
	                _prevctx = localctx;
	                this.state = 391;
	                this._errHandler.sync(this);
	                var la_ = this._interp.adaptivePredict(this._input,36,this._ctx);
	                switch(la_) {
	                case 1:
	                    localctx = new ConstructorExpressionContext(this, _parentctx, _parentState);
	                    localctx.left = _prevctx;
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_constructorExpression);
	                    this.state = 385;
	                    if (!( this.precpred(this._ctx, 3))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 3)");
	                    }
	                    this.state = 386;
	                    localctx.op = this.binary();
	                    this.state = 387;
	                    localctx.right = this.constructorExpression(4);
	                    break;

	                case 2:
	                    localctx = new ConstructorExpressionContext(this, _parentctx, _parentState);
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_constructorExpression);
	                    this.state = 389;
	                    if (!( this.precpred(this._ctx, 1))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 1)");
	                    }
	                    this.state = 390;
	                    this.match(RulepadGrammarParser.SPACE);
	                    break;

	                } 
	            }
	            this.state = 395;
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
	    this.enterRule(localctx, 70, RulepadGrammarParser.RULE_parameters);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 396;
	        this.match(RulepadGrammarParser.PARAMETER);
	        this.state = 397;
	        this.parameterCondition();
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
	    this.enterRule(localctx, 72, RulepadGrammarParser.RULE_parameterCondition);
	    try {
	        this.state = 405;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.T__0:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 399;
	            this.combinatorialWords();
	            this.state = 400;
	            this.match(RulepadGrammarParser.SPACE);
	            this.state = 402;
	            this._errHandler.sync(this);
	            var la_ = this._interp.adaptivePredict(this._input,38,this._ctx);
	            if(la_===1) {
	                this.state = 401;
	                this.parameterConditionTransition();

	            }
	            break;
	        case RulepadGrammarParser.T__20:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 404;
	            this.parameterConditionTransition();
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



	parameterConditionTransition() {
	    let localctx = new ParameterConditionTransitionContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 74, RulepadGrammarParser.RULE_parameterConditionTransition);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 407;
	        this.withWord();
	        this.state = 408;
	        this.parameterExpression(0);
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
	    const _startState = 76;
	    this.enterRecursionRule(localctx, 76, RulepadGrammarParser.RULE_parameterExpression, _p);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 420;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.LPAREN:
	            this.state = 411;
	            this.match(RulepadGrammarParser.LPAREN);
	            this.state = 412;
	            this.parameterExpression(0);
	            this.state = 413;
	            this.match(RulepadGrammarParser.RPAREN);
	            break;
	        case RulepadGrammarParser.NAME:
	        case RulepadGrammarParser.VALUE:
	        case RulepadGrammarParser.TYPES:
	            this.state = 418;
	            this._errHandler.sync(this);
	            switch(this._input.LA(1)) {
	            case RulepadGrammarParser.TYPES:
	                this.state = 415;
	                this.types();
	                break;
	            case RulepadGrammarParser.NAME:
	                this.state = 416;
	                this.names();
	                break;
	            case RulepadGrammarParser.VALUE:
	                this.state = 417;
	                this.values();
	                break;
	            default:
	                throw new antlr4.error.NoViableAltException(this);
	            }
	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	        this._ctx.stop = this._input.LT(-1);
	        this.state = 430;
	        this._errHandler.sync(this);
	        let _alt = this._interp.adaptivePredict(this._input,43,this._ctx)
	        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
	            if(_alt===1) {
	                if(this._parseListeners!==null) {
	                    this.triggerExitRuleEvent();
	                }
	                _prevctx = localctx;
	                this.state = 428;
	                this._errHandler.sync(this);
	                var la_ = this._interp.adaptivePredict(this._input,42,this._ctx);
	                switch(la_) {
	                case 1:
	                    localctx = new ParameterExpressionContext(this, _parentctx, _parentState);
	                    localctx.left = _prevctx;
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_parameterExpression);
	                    this.state = 422;
	                    if (!( this.precpred(this._ctx, 3))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 3)");
	                    }
	                    this.state = 423;
	                    localctx.op = this.binary();
	                    this.state = 424;
	                    localctx.right = this.parameterExpression(4);
	                    break;

	                case 2:
	                    localctx = new ParameterExpressionContext(this, _parentctx, _parentState);
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_parameterExpression);
	                    this.state = 426;
	                    if (!( this.precpred(this._ctx, 1))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 1)");
	                    }
	                    this.state = 427;
	                    this.match(RulepadGrammarParser.SPACE);
	                    break;

	                } 
	            }
	            this.state = 432;
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
	    this.enterRule(localctx, 78, RulepadGrammarParser.RULE_functionParameters);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 433;
	        this.match(RulepadGrammarParser.PARAMETER);
	        this.state = 435;
	        this._errHandler.sync(this);
	        var la_ = this._interp.adaptivePredict(this._input,44,this._ctx);
	        if(la_===1) {
	            this.state = 434;
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
	    this.enterRule(localctx, 80, RulepadGrammarParser.RULE_functionParameterCondition);
	    try {
	        this.state = 443;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.T__0:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 437;
	            this.combinatorialWords();
	            this.state = 438;
	            this.match(RulepadGrammarParser.SPACE);
	            this.state = 440;
	            this._errHandler.sync(this);
	            var la_ = this._interp.adaptivePredict(this._input,45,this._ctx);
	            if(la_===1) {
	                this.state = 439;
	                this.functionParameterConditionTransition();

	            }
	            break;
	        case RulepadGrammarParser.T__20:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 442;
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
	    this.enterRule(localctx, 82, RulepadGrammarParser.RULE_functionParameterConditionTransition);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 445;
	        this.withWord();
	        this.state = 446;
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
	    const _startState = 84;
	    this.enterRecursionRule(localctx, 84, RulepadGrammarParser.RULE_functionParameterExpression, _p);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 458;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.LPAREN:
	            this.state = 449;
	            this.match(RulepadGrammarParser.LPAREN);
	            this.state = 450;
	            this.functionParameterExpression(0);
	            this.state = 451;
	            this.match(RulepadGrammarParser.RPAREN);
	            break;
	        case RulepadGrammarParser.NAME:
	        case RulepadGrammarParser.ANNOTATION:
	        case RulepadGrammarParser.TYPES:
	            this.state = 456;
	            this._errHandler.sync(this);
	            switch(this._input.LA(1)) {
	            case RulepadGrammarParser.TYPES:
	                this.state = 453;
	                this.types();
	                break;
	            case RulepadGrammarParser.NAME:
	                this.state = 454;
	                this.names();
	                break;
	            case RulepadGrammarParser.ANNOTATION:
	                this.state = 455;
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
	        this.state = 468;
	        this._errHandler.sync(this);
	        let _alt = this._interp.adaptivePredict(this._input,50,this._ctx)
	        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
	            if(_alt===1) {
	                if(this._parseListeners!==null) {
	                    this.triggerExitRuleEvent();
	                }
	                _prevctx = localctx;
	                this.state = 466;
	                this._errHandler.sync(this);
	                var la_ = this._interp.adaptivePredict(this._input,49,this._ctx);
	                switch(la_) {
	                case 1:
	                    localctx = new FunctionParameterExpressionContext(this, _parentctx, _parentState);
	                    localctx.left = _prevctx;
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_functionParameterExpression);
	                    this.state = 460;
	                    if (!( this.precpred(this._ctx, 3))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 3)");
	                    }
	                    this.state = 461;
	                    localctx.op = this.binary();
	                    this.state = 462;
	                    localctx.right = this.functionParameterExpression(4);
	                    break;

	                case 2:
	                    localctx = new FunctionParameterExpressionContext(this, _parentctx, _parentState);
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_functionParameterExpression);
	                    this.state = 464;
	                    if (!( this.precpred(this._ctx, 1))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 1)");
	                    }
	                    this.state = 465;
	                    this.match(RulepadGrammarParser.SPACE);
	                    break;

	                } 
	            }
	            this.state = 470;
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
	    this.enterRule(localctx, 86, RulepadGrammarParser.RULE_types);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 471;
	        this.match(RulepadGrammarParser.TYPES);
	        this.state = 473;
	        this._errHandler.sync(this);
	        var la_ = this._interp.adaptivePredict(this._input,51,this._ctx);
	        if(la_===1) {
	            this.state = 472;
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
	    this.enterRule(localctx, 88, RulepadGrammarParser.RULE_typeCondition);
	    try {
	        this.state = 481;
	        this._errHandler.sync(this);
	        var la_ = this._interp.adaptivePredict(this._input,52,this._ctx);
	        switch(la_) {
	        case 1:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 475;
	            this.combinatorialWords();
	            this.state = 476;
	            this.match(RulepadGrammarParser.SPACE);
	            break;

	        case 2:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 478;
	            this.words();
	            this.state = 479;
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
	    this.enterRule(localctx, 90, RulepadGrammarParser.RULE_declarationStatements);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 483;
	        this.match(RulepadGrammarParser.DeclarationStatement);
	        this.state = 484;
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
	    this.enterRule(localctx, 92, RulepadGrammarParser.RULE_declarationStatementCondition);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 486;
	        this.withWord();
	        this.state = 487;
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
	    const _startState = 94;
	    this.enterRecursionRule(localctx, 94, RulepadGrammarParser.RULE_declarationStatementExpression, _p);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 498;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.LPAREN:
	            this.state = 490;
	            this.match(RulepadGrammarParser.LPAREN);
	            this.state = 491;
	            this.declarationStatementExpression(0);
	            this.state = 492;
	            this.match(RulepadGrammarParser.RPAREN);
	            break;
	        case RulepadGrammarParser.ANNOTATION:
	        case RulepadGrammarParser.TYPES:
	            this.state = 496;
	            this._errHandler.sync(this);
	            switch(this._input.LA(1)) {
	            case RulepadGrammarParser.ANNOTATION:
	                this.state = 494;
	                this.annotations();
	                break;
	            case RulepadGrammarParser.TYPES:
	                this.state = 495;
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
	        this.state = 508;
	        this._errHandler.sync(this);
	        let _alt = this._interp.adaptivePredict(this._input,56,this._ctx)
	        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
	            if(_alt===1) {
	                if(this._parseListeners!==null) {
	                    this.triggerExitRuleEvent();
	                }
	                _prevctx = localctx;
	                this.state = 506;
	                this._errHandler.sync(this);
	                var la_ = this._interp.adaptivePredict(this._input,55,this._ctx);
	                switch(la_) {
	                case 1:
	                    localctx = new DeclarationStatementExpressionContext(this, _parentctx, _parentState);
	                    localctx.left = _prevctx;
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_declarationStatementExpression);
	                    this.state = 500;
	                    if (!( this.precpred(this._ctx, 3))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 3)");
	                    }
	                    this.state = 501;
	                    localctx.op = this.binary();
	                    this.state = 502;
	                    localctx.right = this.declarationStatementExpression(4);
	                    break;

	                case 2:
	                    localctx = new DeclarationStatementExpressionContext(this, _parentctx, _parentState);
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_declarationStatementExpression);
	                    this.state = 504;
	                    if (!( this.precpred(this._ctx, 1))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 1)");
	                    }
	                    this.state = 505;
	                    this.match(RulepadGrammarParser.SPACE);
	                    break;

	                } 
	            }
	            this.state = 510;
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
	    this.enterRule(localctx, 96, RulepadGrammarParser.RULE_configurationFiles);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 511;
	        this.match(RulepadGrammarParser.ConfigurationFile);
	        this.state = 513;
	        this._errHandler.sync(this);
	        var la_ = this._interp.adaptivePredict(this._input,57,this._ctx);
	        if(la_===1) {
	            this.state = 512;
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
	    this.enterRule(localctx, 98, RulepadGrammarParser.RULE_configurationFileCondition);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 515;
	        this.withWord();
	        this.state = 516;
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
	    const _startState = 100;
	    this.enterRecursionRule(localctx, 100, RulepadGrammarParser.RULE_configurationFileExpression, _p);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 524;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.LPAREN:
	            this.state = 519;
	            this.match(RulepadGrammarParser.LPAREN);
	            this.state = 520;
	            this.configurationFileExpression(0);
	            this.state = 521;
	            this.match(RulepadGrammarParser.RPAREN);
	            break;
	        case RulepadGrammarParser.CONFIGURATION_PROPERTIES:
	            this.state = 523;
	            this.configurationProperties();
	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	        this._ctx.stop = this._input.LT(-1);
	        this.state = 534;
	        this._errHandler.sync(this);
	        let _alt = this._interp.adaptivePredict(this._input,60,this._ctx)
	        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
	            if(_alt===1) {
	                if(this._parseListeners!==null) {
	                    this.triggerExitRuleEvent();
	                }
	                _prevctx = localctx;
	                this.state = 532;
	                this._errHandler.sync(this);
	                var la_ = this._interp.adaptivePredict(this._input,59,this._ctx);
	                switch(la_) {
	                case 1:
	                    localctx = new ConfigurationFileExpressionContext(this, _parentctx, _parentState);
	                    localctx.left = _prevctx;
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_configurationFileExpression);
	                    this.state = 526;
	                    if (!( this.precpred(this._ctx, 3))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 3)");
	                    }
	                    this.state = 527;
	                    localctx.op = this.binary();
	                    this.state = 528;
	                    localctx.right = this.configurationFileExpression(4);
	                    break;

	                case 2:
	                    localctx = new ConfigurationFileExpressionContext(this, _parentctx, _parentState);
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_configurationFileExpression);
	                    this.state = 530;
	                    if (!( this.precpred(this._ctx, 1))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 1)");
	                    }
	                    this.state = 531;
	                    this.match(RulepadGrammarParser.SPACE);
	                    break;

	                } 
	            }
	            this.state = 536;
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
	    this.enterRule(localctx, 102, RulepadGrammarParser.RULE_configurationProperties);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 537;
	        this.match(RulepadGrammarParser.CONFIGURATION_PROPERTIES);
	        this.state = 538;
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
	    this.enterRule(localctx, 104, RulepadGrammarParser.RULE_configurationPropertyCondition);
	    try {
	        this.state = 546;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.T__0:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 540;
	            this.combinatorialWords();
	            this.state = 541;
	            this.match(RulepadGrammarParser.SPACE);
	            this.state = 543;
	            this._errHandler.sync(this);
	            var la_ = this._interp.adaptivePredict(this._input,61,this._ctx);
	            if(la_===1) {
	                this.state = 542;
	                this.configurationPropertyConditionTransition();

	            }
	            break;
	        case RulepadGrammarParser.T__20:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 545;
	            this.configurationPropertyConditionTransition();
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



	configurationPropertyConditionTransition() {
	    let localctx = new ConfigurationPropertyConditionTransitionContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 106, RulepadGrammarParser.RULE_configurationPropertyConditionTransition);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 548;
	        this.withWord();
	        this.state = 549;
	        this.configurationPropertyExpression(0);
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
	    const _startState = 108;
	    this.enterRecursionRule(localctx, 108, RulepadGrammarParser.RULE_configurationPropertyExpression, _p);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 561;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.LPAREN:
	            this.state = 552;
	            this.match(RulepadGrammarParser.LPAREN);
	            this.state = 553;
	            this.configurationPropertyExpression(0);
	            this.state = 554;
	            this.match(RulepadGrammarParser.RPAREN);
	            break;
	        case RulepadGrammarParser.NAME:
	        case RulepadGrammarParser.VALUE:
	        case RulepadGrammarParser.TYPES:
	            this.state = 559;
	            this._errHandler.sync(this);
	            switch(this._input.LA(1)) {
	            case RulepadGrammarParser.TYPES:
	                this.state = 556;
	                this.types();
	                break;
	            case RulepadGrammarParser.NAME:
	                this.state = 557;
	                this.names();
	                break;
	            case RulepadGrammarParser.VALUE:
	                this.state = 558;
	                this.values();
	                break;
	            default:
	                throw new antlr4.error.NoViableAltException(this);
	            }
	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	        this._ctx.stop = this._input.LT(-1);
	        this.state = 571;
	        this._errHandler.sync(this);
	        let _alt = this._interp.adaptivePredict(this._input,66,this._ctx)
	        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
	            if(_alt===1) {
	                if(this._parseListeners!==null) {
	                    this.triggerExitRuleEvent();
	                }
	                _prevctx = localctx;
	                this.state = 569;
	                this._errHandler.sync(this);
	                var la_ = this._interp.adaptivePredict(this._input,65,this._ctx);
	                switch(la_) {
	                case 1:
	                    localctx = new ConfigurationPropertyExpressionContext(this, _parentctx, _parentState);
	                    localctx.left = _prevctx;
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_configurationPropertyExpression);
	                    this.state = 563;
	                    if (!( this.precpred(this._ctx, 3))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 3)");
	                    }
	                    this.state = 564;
	                    localctx.op = this.binary();
	                    this.state = 565;
	                    localctx.right = this.configurationPropertyExpression(4);
	                    break;

	                case 2:
	                    localctx = new ConfigurationPropertyExpressionContext(this, _parentctx, _parentState);
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_configurationPropertyExpression);
	                    this.state = 567;
	                    if (!( this.precpred(this._ctx, 1))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 1)");
	                    }
	                    this.state = 568;
	                    this.match(RulepadGrammarParser.SPACE);
	                    break;

	                } 
	            }
	            this.state = 573;
	            this._errHandler.sync(this);
	            _alt = this._interp.adaptivePredict(this._input,66,this._ctx);
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
	    this.enterRule(localctx, 110, RulepadGrammarParser.RULE_classes);
	    var _la = 0; // Token type
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 574;
	        this.match(RulepadGrammarParser.CLASSES);
	        this.state = 576;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        if(_la===RulepadGrammarParser.T__20) {
	            this.state = 575;
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
	    this.enterRule(localctx, 112, RulepadGrammarParser.RULE_classCondition);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 578;
	        this.withWord();
	        this.state = 579;
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
	    const _startState = 114;
	    this.enterRecursionRule(localctx, 114, RulepadGrammarParser.RULE_classExpression, _p);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 596;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.LPAREN:
	            this.state = 582;
	            this.match(RulepadGrammarParser.LPAREN);
	            this.state = 583;
	            this.classExpression(0);
	            this.state = 584;
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
	            this.state = 594;
	            this._errHandler.sync(this);
	            switch(this._input.LA(1)) {
	            case RulepadGrammarParser.ANNOTATION:
	                this.state = 586;
	                this.annotations();
	                break;
	            case RulepadGrammarParser.EXTENSION:
	                this.state = 587;
	                this.extensions();
	                break;
	            case RulepadGrammarParser.IMPLEMENTATION:
	                this.state = 588;
	                this.implementations();
	                break;
	            case RulepadGrammarParser.FUNCTION:
	                this.state = 589;
	                this.functions();
	                break;
	            case RulepadGrammarParser.CONSTRUCTOR:
	                this.state = 590;
	                this.constructors();
	                break;
	            case RulepadGrammarParser.DeclarationStatement:
	                this.state = 591;
	                this.declarationStatements();
	                break;
	            case RulepadGrammarParser.ConfigurationFile:
	                this.state = 592;
	                this.configurationFiles();
	                break;
	            case RulepadGrammarParser.BEAN_DECL:
	                this.state = 593;
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
	        this.state = 606;
	        this._errHandler.sync(this);
	        let _alt = this._interp.adaptivePredict(this._input,71,this._ctx)
	        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
	            if(_alt===1) {
	                if(this._parseListeners!==null) {
	                    this.triggerExitRuleEvent();
	                }
	                _prevctx = localctx;
	                this.state = 604;
	                this._errHandler.sync(this);
	                var la_ = this._interp.adaptivePredict(this._input,70,this._ctx);
	                switch(la_) {
	                case 1:
	                    localctx = new ClassExpressionContext(this, _parentctx, _parentState);
	                    localctx.left = _prevctx;
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_classExpression);
	                    this.state = 598;
	                    if (!( this.precpred(this._ctx, 3))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 3)");
	                    }
	                    this.state = 599;
	                    localctx.op = this.binary();
	                    this.state = 600;
	                    localctx.right = this.classExpression(4);
	                    break;

	                case 2:
	                    localctx = new ClassExpressionContext(this, _parentctx, _parentState);
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_classExpression);
	                    this.state = 602;
	                    if (!( this.precpred(this._ctx, 1))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 1)");
	                    }
	                    this.state = 603;
	                    this.match(RulepadGrammarParser.SPACE);
	                    break;

	                } 
	            }
	            this.state = 608;
	            this._errHandler.sync(this);
	            _alt = this._interp.adaptivePredict(this._input,71,this._ctx);
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
	    this.enterRule(localctx, 116, RulepadGrammarParser.RULE_beans);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 609;
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
RulepadGrammarParser.VALUE = 28;
RulepadGrammarParser.ANNOTATION = 29;
RulepadGrammarParser.EXTENSION = 30;
RulepadGrammarParser.SUPERCLASS = 31;
RulepadGrammarParser.IMPLEMENTATION = 32;
RulepadGrammarParser.INTERFACE = 33;
RulepadGrammarParser.FUNCTION = 34;
RulepadGrammarParser.CONSTRUCTOR = 35;
RulepadGrammarParser.PARAMETER = 36;
RulepadGrammarParser.TYPES = 37;
RulepadGrammarParser.DeclarationStatement = 38;
RulepadGrammarParser.ConfigurationFile = 39;
RulepadGrammarParser.CONFIGURATION_PROPERTIES = 40;
RulepadGrammarParser.CLASSES = 41;
RulepadGrammarParser.BEAN_DECL = 42;

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
RulepadGrammarParser.RULE_values = 18;
RulepadGrammarParser.RULE_valueCondition = 19;
RulepadGrammarParser.RULE_annotations = 20;
RulepadGrammarParser.RULE_annotationCondition = 21;
RulepadGrammarParser.RULE_annotationConditionTransition = 22;
RulepadGrammarParser.RULE_annotationExpression = 23;
RulepadGrammarParser.RULE_extensions = 24;
RulepadGrammarParser.RULE_extensionCondition = 25;
RulepadGrammarParser.RULE_implementations = 26;
RulepadGrammarParser.RULE_implementationCondition = 27;
RulepadGrammarParser.RULE_functions = 28;
RulepadGrammarParser.RULE_functionCondition = 29;
RulepadGrammarParser.RULE_functionExpression = 30;
RulepadGrammarParser.RULE_constructors = 31;
RulepadGrammarParser.RULE_constructorOf = 32;
RulepadGrammarParser.RULE_constructorCondition = 33;
RulepadGrammarParser.RULE_constructorExpression = 34;
RulepadGrammarParser.RULE_parameters = 35;
RulepadGrammarParser.RULE_parameterCondition = 36;
RulepadGrammarParser.RULE_parameterConditionTransition = 37;
RulepadGrammarParser.RULE_parameterExpression = 38;
RulepadGrammarParser.RULE_functionParameters = 39;
RulepadGrammarParser.RULE_functionParameterCondition = 40;
RulepadGrammarParser.RULE_functionParameterConditionTransition = 41;
RulepadGrammarParser.RULE_functionParameterExpression = 42;
RulepadGrammarParser.RULE_types = 43;
RulepadGrammarParser.RULE_typeCondition = 44;
RulepadGrammarParser.RULE_declarationStatements = 45;
RulepadGrammarParser.RULE_declarationStatementCondition = 46;
RulepadGrammarParser.RULE_declarationStatementExpression = 47;
RulepadGrammarParser.RULE_configurationFiles = 48;
RulepadGrammarParser.RULE_configurationFileCondition = 49;
RulepadGrammarParser.RULE_configurationFileExpression = 50;
RulepadGrammarParser.RULE_configurationProperties = 51;
RulepadGrammarParser.RULE_configurationPropertyCondition = 52;
RulepadGrammarParser.RULE_configurationPropertyConditionTransition = 53;
RulepadGrammarParser.RULE_configurationPropertyExpression = 54;
RulepadGrammarParser.RULE_classes = 55;
RulepadGrammarParser.RULE_classCondition = 56;
RulepadGrammarParser.RULE_classExpression = 57;
RulepadGrammarParser.RULE_beans = 58;

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



class ValuesContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_values;
    }

	VALUE() {
	    return this.getToken(RulepadGrammarParser.VALUE, 0);
	};

	valueCondition() {
	    return this.getTypedRuleContext(ValueConditionContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterValues(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitValues(this);
		}
	}


}



class ValueConditionContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_valueCondition;
    }

	words() {
	    return this.getTypedRuleContext(WordsContext,0);
	};

	SPACE() {
	    return this.getToken(RulepadGrammarParser.SPACE, 0);
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterValueCondition(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitValueCondition(this);
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

	combinatorialWords() {
	    return this.getTypedRuleContext(CombinatorialWordsContext,0);
	};

	SPACE() {
	    return this.getToken(RulepadGrammarParser.SPACE, 0);
	};

	parameterConditionTransition() {
	    return this.getTypedRuleContext(ParameterConditionTransitionContext,0);
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



class ParameterConditionTransitionContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_parameterConditionTransition;
    }

	withWord() {
	    return this.getTypedRuleContext(WithWordContext,0);
	};

	parameterExpression() {
	    return this.getTypedRuleContext(ParameterExpressionContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterParameterConditionTransition(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitParameterConditionTransition(this);
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

	values() {
	    return this.getTypedRuleContext(ValuesContext,0);
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

	combinatorialWords() {
	    return this.getTypedRuleContext(CombinatorialWordsContext,0);
	};

	SPACE() {
	    return this.getToken(RulepadGrammarParser.SPACE, 0);
	};

	configurationPropertyConditionTransition() {
	    return this.getTypedRuleContext(ConfigurationPropertyConditionTransitionContext,0);
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



class ConfigurationPropertyConditionTransitionContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = RulepadGrammarParser.RULE_configurationPropertyConditionTransition;
    }

	withWord() {
	    return this.getTypedRuleContext(WithWordContext,0);
	};

	configurationPropertyExpression() {
	    return this.getTypedRuleContext(ConfigurationPropertyExpressionContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.enterConfigurationPropertyConditionTransition(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof RulepadGrammarListener ) {
	        listener.exitConfigurationPropertyConditionTransition(this);
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

	values() {
	    return this.getTypedRuleContext(ValuesContext,0);
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
RulepadGrammarParser.ValuesContext = ValuesContext; 
RulepadGrammarParser.ValueConditionContext = ValueConditionContext; 
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
RulepadGrammarParser.ParameterConditionTransitionContext = ParameterConditionTransitionContext; 
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
RulepadGrammarParser.ConfigurationPropertyConditionTransitionContext = ConfigurationPropertyConditionTransitionContext; 
RulepadGrammarParser.ConfigurationPropertyExpressionContext = ConfigurationPropertyExpressionContext; 
RulepadGrammarParser.ClassesContext = ClassesContext; 
RulepadGrammarParser.ClassConditionContext = ClassConditionContext; 
RulepadGrammarParser.ClassExpressionContext = ClassExpressionContext; 
RulepadGrammarParser.BeansContext = BeansContext; 
