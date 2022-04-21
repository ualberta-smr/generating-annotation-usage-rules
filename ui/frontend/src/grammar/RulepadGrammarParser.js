// Generated from ../violation-detection/src/main/antlr4/ca/ualberta/grammar/RulepadGrammar.g4 by ANTLR 4.9
// jshint ignore: start
import antlr4 from 'antlr4';
import RulepadGrammarListener from './RulepadGrammarListener.js';

const serializedATN = ["\u0003\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786",
    "\u5964\u0003\'\u020b\u0004\u0002\t\u0002\u0004\u0003\t\u0003\u0004\u0004",
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
    "9\t9\u0003\u0002\u0007\u0002t\n\u0002\f\u0002\u000e\u0002w\u000b\u0002",
    "\u0003\u0002\u0005\u0002z\n\u0002\u0003\u0002\u0005\u0002}\n\u0002\u0003",
    "\u0002\u0007\u0002\u0080\n\u0002\f\u0002\u000e\u0002\u0083\u000b\u0002",
    "\u0003\u0002\u0003\u0002\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003",
    "\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003",
    "\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003",
    "\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0005\u0003\u009b\n",
    "\u0003\u0003\u0004\u0003\u0004\u0003\u0004\u0003\u0004\u0006\u0004\u00a1",
    "\n\u0004\r\u0004\u000e\u0004\u00a2\u0003\u0004\u0003\u0004\u0003\u0005",
    "\u0003\u0005\u0003\u0006\u0003\u0006\u0003\u0007\u0003\u0007\u0003\b",
    "\u0003\b\u0003\t\u0003\t\u0003\n\u0003\n\u0003\u000b\u0003\u000b\u0003",
    "\f\u0003\f\u0003\r\u0003\r\u0003\u000e\u0003\u000e\u0005\u000e\u00bb",
    "\n\u000e\u0003\u000f\u0003\u000f\u0003\u000f\u0003\u0010\u0003\u0010",
    "\u0003\u0010\u0003\u0011\u0003\u0011\u0003\u0011\u0003\u0012\u0003\u0012",
    "\u0003\u0012\u0003\u0013\u0003\u0013\u0003\u0013\u0003\u0014\u0003\u0014",
    "\u0003\u0014\u0005\u0014\u00cf\n\u0014\u0003\u0014\u0005\u0014\u00d2",
    "\n\u0014\u0003\u0015\u0003\u0015\u0003\u0015\u0003\u0016\u0003\u0016",
    "\u0003\u0016\u0003\u0016\u0003\u0016\u0003\u0016\u0005\u0016\u00dd\n",
    "\u0016\u0003\u0016\u0003\u0016\u0003\u0016\u0003\u0016\u0003\u0016\u0003",
    "\u0016\u0007\u0016\u00e5\n\u0016\f\u0016\u000e\u0016\u00e8\u000b\u0016",
    "\u0003\u0017\u0003\u0017\u0003\u0017\u0003\u0018\u0003\u0018\u0003\u0018",
    "\u0003\u0018\u0003\u0018\u0005\u0018\u00f2\n\u0018\u0003\u0019\u0003",
    "\u0019\u0003\u0019\u0003\u001a\u0003\u001a\u0003\u001a\u0003\u001a\u0003",
    "\u001a\u0005\u001a\u00fc\n\u001a\u0003\u001b\u0003\u001b\u0003\u001b",
    "\u0003\u001c\u0003\u001c\u0003\u001c\u0003\u001d\u0003\u001d\u0003\u001d",
    "\u0003\u001d\u0003\u001d\u0003\u001d\u0003\u001d\u0003\u001d\u0003\u001d",
    "\u0005\u001d\u010d\n\u001d\u0005\u001d\u010f\n\u001d\u0003\u001d\u0003",
    "\u001d\u0003\u001d\u0003\u001d\u0003\u001d\u0003\u001d\u0007\u001d\u0117",
    "\n\u001d\f\u001d\u000e\u001d\u011a\u000b\u001d\u0003\u001e\u0003\u001e",
    "\u0003\u001e\u0003\u001f\u0003\u001f\u0003\u001f\u0003 \u0003 \u0003",
    " \u0003!\u0003!\u0003!\u0003!\u0003!\u0003!\u0003!\u0005!\u012c\n!\u0005",
    "!\u012e\n!\u0003!\u0003!\u0003!\u0003!\u0003!\u0003!\u0007!\u0136\n",
    "!\f!\u000e!\u0139\u000b!\u0003\"\u0003\"\u0003\"\u0003#\u0003#\u0003",
    "#\u0005#\u0141\n#\u0003#\u0005#\u0144\n#\u0003$\u0003$\u0003$\u0003",
    "%\u0003%\u0003%\u0003%\u0003%\u0003%\u0003%\u0003%\u0005%\u0151\n%\u0005",
    "%\u0153\n%\u0003%\u0003%\u0003%\u0003%\u0003%\u0003%\u0007%\u015b\n",
    "%\f%\u000e%\u015e\u000b%\u0003&\u0003&\u0005&\u0162\n&\u0003\'\u0003",
    "\'\u0003\'\u0005\'\u0167\n\'\u0003\'\u0005\'\u016a\n\'\u0003(\u0003",
    "(\u0003(\u0003)\u0003)\u0003)\u0003)\u0003)\u0003)\u0003)\u0003)\u0005",
    ")\u0177\n)\u0005)\u0179\n)\u0003)\u0003)\u0003)\u0003)\u0003)\u0003",
    ")\u0007)\u0181\n)\f)\u000e)\u0184\u000b)\u0003*\u0003*\u0003*\u0003",
    "+\u0003+\u0003+\u0003,\u0003,\u0003,\u0003-\u0003-\u0003-\u0003.\u0003",
    ".\u0003.\u0003.\u0003.\u0003.\u0003.\u0003.\u0005.\u019a\n.\u0005.\u019c",
    "\n.\u0003.\u0003.\u0003.\u0003.\u0003.\u0003.\u0007.\u01a4\n.\f.\u000e",
    ".\u01a7\u000b.\u0003/\u0003/\u0003/\u00030\u00030\u00030\u00031\u0003",
    "1\u00031\u00031\u00031\u00031\u00051\u01b5\n1\u00031\u00031\u00031\u0003",
    "1\u00031\u00031\u00071\u01bd\n1\f1\u000e1\u01c0\u000b1\u00032\u0003",
    "2\u00032\u00033\u00033\u00033\u00053\u01c8\n3\u00033\u00053\u01cb\n",
    "3\u00034\u00034\u00034\u00035\u00035\u00035\u00035\u00035\u00035\u0003",
    "5\u00035\u00055\u01d8\n5\u00055\u01da\n5\u00035\u00035\u00035\u0003",
    "5\u00035\u00035\u00075\u01e2\n5\f5\u000e5\u01e5\u000b5\u00036\u0003",
    "6\u00036\u00037\u00037\u00037\u00038\u00038\u00038\u00038\u00038\u0003",
    "8\u00038\u00038\u00038\u00038\u00038\u00038\u00038\u00058\u01fa\n8\u0005",
    "8\u01fc\n8\u00038\u00038\u00038\u00038\u00038\u00038\u00078\u0204\n",
    "8\f8\u000e8\u0207\u000b8\u00039\u00039\u00039\u0002\u000b*8@HPZ`hn:",
    "\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c",
    "\u001e \"$&(*,.02468:<>@BDFHJLNPRTVXZ\\^`bdfhjlnp\u0002\u0003\u0004",
    "\u0002\u0004\f\u0016\u0017\u0002\u0216\u0002y\u0003\u0002\u0002\u0002",
    "\u0004\u009a\u0003\u0002\u0002\u0002\u0006\u009c\u0003\u0002\u0002\u0002",
    "\b\u00a6\u0003\u0002\u0002\u0002\n\u00a8\u0003\u0002\u0002\u0002\f\u00aa",
    "\u0003\u0002\u0002\u0002\u000e\u00ac\u0003\u0002\u0002\u0002\u0010\u00ae",
    "\u0003\u0002\u0002\u0002\u0012\u00b0\u0003\u0002\u0002\u0002\u0014\u00b2",
    "\u0003\u0002\u0002\u0002\u0016\u00b4\u0003\u0002\u0002\u0002\u0018\u00b6",
    "\u0003\u0002\u0002\u0002\u001a\u00ba\u0003\u0002\u0002\u0002\u001c\u00bc",
    "\u0003\u0002\u0002\u0002\u001e\u00bf\u0003\u0002\u0002\u0002 \u00c2",
    "\u0003\u0002\u0002\u0002\"\u00c5\u0003\u0002\u0002\u0002$\u00c8\u0003",
    "\u0002\u0002\u0002&\u00d1\u0003\u0002\u0002\u0002(\u00d3\u0003\u0002",
    "\u0002\u0002*\u00dc\u0003\u0002\u0002\u0002,\u00e9\u0003\u0002\u0002",
    "\u0002.\u00ec\u0003\u0002\u0002\u00020\u00f3\u0003\u0002\u0002\u0002",
    "2\u00f6\u0003\u0002\u0002\u00024\u00fd\u0003\u0002\u0002\u00026\u0100",
    "\u0003\u0002\u0002\u00028\u010e\u0003\u0002\u0002\u0002:\u011b\u0003",
    "\u0002\u0002\u0002<\u011e\u0003\u0002\u0002\u0002>\u0121\u0003\u0002",
    "\u0002\u0002@\u012d\u0003\u0002\u0002\u0002B\u013a\u0003\u0002\u0002",
    "\u0002D\u0143\u0003\u0002\u0002\u0002F\u0145\u0003\u0002\u0002\u0002",
    "H\u0152\u0003\u0002\u0002\u0002J\u015f\u0003\u0002\u0002\u0002L\u0169",
    "\u0003\u0002\u0002\u0002N\u016b\u0003\u0002\u0002\u0002P\u0178\u0003",
    "\u0002\u0002\u0002R\u0185\u0003\u0002\u0002\u0002T\u0188\u0003\u0002",
    "\u0002\u0002V\u018b\u0003\u0002\u0002\u0002X\u018e\u0003\u0002\u0002",
    "\u0002Z\u019b\u0003\u0002\u0002\u0002\\\u01a8\u0003\u0002\u0002\u0002",
    "^\u01ab\u0003\u0002\u0002\u0002`\u01b4\u0003\u0002\u0002\u0002b\u01c1",
    "\u0003\u0002\u0002\u0002d\u01ca\u0003\u0002\u0002\u0002f\u01cc\u0003",
    "\u0002\u0002\u0002h\u01d9\u0003\u0002\u0002\u0002j\u01e6\u0003\u0002",
    "\u0002\u0002l\u01e9\u0003\u0002\u0002\u0002n\u01fb\u0003\u0002\u0002",
    "\u0002p\u0208\u0003\u0002\u0002\u0002rt\u0005\f\u0007\u0002sr\u0003",
    "\u0002\u0002\u0002tw\u0003\u0002\u0002\u0002us\u0003\u0002\u0002\u0002",
    "uv\u0003\u0002\u0002\u0002vz\u0003\u0002\u0002\u0002wu\u0003\u0002\u0002",
    "\u0002xz\u0005\u0004\u0003\u0002yu\u0003\u0002\u0002\u0002yx\u0003\u0002",
    "\u0002\u0002z|\u0003\u0002\u0002\u0002{}\u0005\n\u0006\u0002|{\u0003",
    "\u0002\u0002\u0002|}\u0003\u0002\u0002\u0002}\u0081\u0003\u0002\u0002",
    "\u0002~\u0080\u0007\u0015\u0002\u0002\u007f~\u0003\u0002\u0002\u0002",
    "\u0080\u0083\u0003\u0002\u0002\u0002\u0081\u007f\u0003\u0002\u0002\u0002",
    "\u0081\u0082\u0003\u0002\u0002\u0002\u0082\u0084\u0003\u0002\u0002\u0002",
    "\u0083\u0081\u0003\u0002\u0002\u0002\u0084\u0085\u0007\u0002\u0002\u0003",
    "\u0085\u0003\u0003\u0002\u0002\u0002\u0086\u0087\u00054\u001b\u0002",
    "\u0087\u0088\u0005\u000e\b\u0002\u0088\u0089\u0005\u0016\f\u0002\u0089",
    "\u008a\u00058\u001d\u0002\u008a\u009b\u0003\u0002\u0002\u0002\u008b",
    "\u008c\u0005:\u001e\u0002\u008c\u008d\u0005\u000e\b\u0002\u008d\u008e",
    "\u0005\u0016\f\u0002\u008e\u008f\u0005@!\u0002\u008f\u009b\u0003\u0002",
    "\u0002\u0002\u0090\u0091\u0005j6\u0002\u0091\u0092\u0005\u000e\b\u0002",
    "\u0092\u0093\u0005\u0016\f\u0002\u0093\u0094\u0005n8\u0002\u0094\u009b",
    "\u0003\u0002\u0002\u0002\u0095\u0096\u0005V,\u0002\u0096\u0097\u0005",
    "\u000e\b\u0002\u0097\u0098\u0005\u0016\f\u0002\u0098\u0099\u0005Z.\u0002",
    "\u0099\u009b\u0003\u0002\u0002\u0002\u009a\u0086\u0003\u0002\u0002\u0002",
    "\u009a\u008b\u0003\u0002\u0002\u0002\u009a\u0090\u0003\u0002\u0002\u0002",
    "\u009a\u0095\u0003\u0002\u0002\u0002\u009b\u0005\u0003\u0002\u0002\u0002",
    "\u009c\u00a0\u0007\u0003\u0002\u0002\u009d\u00a1\u0007\u0014\u0002\u0002",
    "\u009e\u00a1\u0005\b\u0005\u0002\u009f\u00a1\u0007\u0013\u0002\u0002",
    "\u00a0\u009d\u0003\u0002\u0002\u0002\u00a0\u009e\u0003\u0002\u0002\u0002",
    "\u00a0\u009f\u0003\u0002\u0002\u0002\u00a1\u00a2\u0003\u0002\u0002\u0002",
    "\u00a2\u00a0\u0003\u0002\u0002\u0002\u00a2\u00a3\u0003\u0002\u0002\u0002",
    "\u00a3\u00a4\u0003\u0002\u0002\u0002\u00a4\u00a5\u0007\u0003\u0002\u0002",
    "\u00a5\u0007\u0003\u0002\u0002\u0002\u00a6\u00a7\t\u0002\u0002\u0002",
    "\u00a7\t\u0003\u0002\u0002\u0002\u00a8\u00a9\u0007\u0004\u0002\u0002",
    "\u00a9\u000b\u0003\u0002\u0002\u0002\u00aa\u00ab\u0007\u0015\u0002\u0002",
    "\u00ab\r\u0003\u0002\u0002\u0002\u00ac\u00ad\u0007\r\u0002\u0002\u00ad",
    "\u000f\u0003\u0002\u0002\u0002\u00ae\u00af\u0007\u000e\u0002\u0002\u00af",
    "\u0011\u0003\u0002\u0002\u0002\u00b0\u00b1\u0007\u000f\u0002\u0002\u00b1",
    "\u0013\u0003\u0002\u0002\u0002\u00b2\u00b3\u0007\u0010\u0002\u0002\u00b3",
    "\u0015\u0003\u0002\u0002\u0002\u00b4\u00b5\u0007\u0011\u0002\u0002\u00b5",
    "\u0017\u0003\u0002\u0002\u0002\u00b6\u00b7\u0007\u0012\u0002\u0002\u00b7",
    "\u0019\u0003\u0002\u0002\u0002\u00b8\u00bb\u0005\u0012\n\u0002\u00b9",
    "\u00bb\u0005\u0014\u000b\u0002\u00ba\u00b8\u0003\u0002\u0002\u0002\u00ba",
    "\u00b9\u0003\u0002\u0002\u0002\u00bb\u001b\u0003\u0002\u0002\u0002\u00bc",
    "\u00bd\u0007\u0018\u0002\u0002\u00bd\u00be\u0005\u001e\u0010\u0002\u00be",
    "\u001d\u0003\u0002\u0002\u0002\u00bf\u00c0\u0005\u0006\u0004\u0002\u00c0",
    "\u00c1\u0007\u0013\u0002\u0002\u00c1\u001f\u0003\u0002\u0002\u0002\u00c2",
    "\u00c3\u0007\u0019\u0002\u0002\u00c3\u00c4\u0005\"\u0012\u0002\u00c4",
    "!\u0003\u0002\u0002\u0002\u00c5\u00c6\u0005\u0006\u0004\u0002\u00c6",
    "\u00c7\u0007\u0013\u0002\u0002\u00c7#\u0003\u0002\u0002\u0002\u00c8",
    "\u00c9\u0007\u001a\u0002\u0002\u00c9\u00ca\u0005&\u0014\u0002\u00ca",
    "%\u0003\u0002\u0002\u0002\u00cb\u00cc\u0005\u0006\u0004\u0002\u00cc",
    "\u00ce\u0007\u0013\u0002\u0002\u00cd\u00cf\u0005(\u0015\u0002\u00ce",
    "\u00cd\u0003\u0002\u0002\u0002\u00ce\u00cf\u0003\u0002\u0002\u0002\u00cf",
    "\u00d2\u0003\u0002\u0002\u0002\u00d0\u00d2\u0005(\u0015\u0002\u00d1",
    "\u00cb\u0003\u0002\u0002\u0002\u00d1\u00d0\u0003\u0002\u0002\u0002\u00d2",
    "\'\u0003\u0002\u0002\u0002\u00d3\u00d4\u0005\u0018\r\u0002\u00d4\u00d5",
    "\u0005*\u0016\u0002\u00d5)\u0003\u0002\u0002\u0002\u00d6\u00d7\b\u0016",
    "\u0001\u0002\u00d7\u00d8\u0007\u0016\u0002\u0002\u00d8\u00d9\u0005*",
    "\u0016\u0002\u00d9\u00da\u0007\u0017\u0002\u0002\u00da\u00dd\u0003\u0002",
    "\u0002\u0002\u00db\u00dd\u0005B\"\u0002\u00dc\u00d6\u0003\u0002\u0002",
    "\u0002\u00dc\u00db\u0003\u0002\u0002\u0002\u00dd\u00e6\u0003\u0002\u0002",
    "\u0002\u00de\u00df\f\u0005\u0002\u0002\u00df\u00e0\u0005\u001a\u000e",
    "\u0002\u00e0\u00e1\u0005*\u0016\u0006\u00e1\u00e5\u0003\u0002\u0002",
    "\u0002\u00e2\u00e3\f\u0003\u0002\u0002\u00e3\u00e5\u0007\u0013\u0002",
    "\u0002\u00e4\u00de\u0003\u0002\u0002\u0002\u00e4\u00e2\u0003\u0002\u0002",
    "\u0002\u00e5\u00e8\u0003\u0002\u0002\u0002\u00e6\u00e4\u0003\u0002\u0002",
    "\u0002\u00e6\u00e7\u0003\u0002\u0002\u0002\u00e7+\u0003\u0002\u0002",
    "\u0002\u00e8\u00e6\u0003\u0002\u0002\u0002\u00e9\u00ea\u0007\u001b\u0002",
    "\u0002\u00ea\u00eb\u0005.\u0018\u0002\u00eb-\u0003\u0002\u0002\u0002",
    "\u00ec\u00f1\u0005\u0010\t\u0002\u00ed\u00ee\u0005\u0006\u0004\u0002",
    "\u00ee\u00ef\u0007\u0013\u0002\u0002\u00ef\u00f2\u0003\u0002\u0002\u0002",
    "\u00f0\u00f2\u0007\u001c\u0002\u0002\u00f1\u00ed\u0003\u0002\u0002\u0002",
    "\u00f1\u00f0\u0003\u0002\u0002\u0002\u00f2/\u0003\u0002\u0002\u0002",
    "\u00f3\u00f4\u0007\u001d\u0002\u0002\u00f4\u00f5\u00052\u001a\u0002",
    "\u00f51\u0003\u0002\u0002\u0002\u00f6\u00fb\u0005\u0010\t\u0002\u00f7",
    "\u00f8\u0005\u0006\u0004\u0002\u00f8\u00f9\u0007\u0013\u0002\u0002\u00f9",
    "\u00fc\u0003\u0002\u0002\u0002\u00fa\u00fc\u0007\u001e\u0002\u0002\u00fb",
    "\u00f7\u0003\u0002\u0002\u0002\u00fb\u00fa\u0003\u0002\u0002\u0002\u00fc",
    "3\u0003\u0002\u0002\u0002\u00fd\u00fe\u0007\u001f\u0002\u0002\u00fe",
    "\u00ff\u00056\u001c\u0002\u00ff5\u0003\u0002\u0002\u0002\u0100\u0101",
    "\u0005\u0018\r\u0002\u0101\u0102\u00058\u001d\u0002\u01027\u0003\u0002",
    "\u0002\u0002\u0103\u0104\b\u001d\u0001\u0002\u0104\u0105\u0007\u0016",
    "\u0002\u0002\u0105\u0106\u00058\u001d\u0002\u0106\u0107\u0007\u0017",
    "\u0002\u0002\u0107\u010f\u0003\u0002\u0002\u0002\u0108\u010d\u0005$",
    "\u0013\u0002\u0109\u010d\u0005R*\u0002\u010a\u010d\u0005J&\u0002\u010b",
    "\u010d\u0005\\/\u0002\u010c\u0108\u0003\u0002\u0002\u0002\u010c\u0109",
    "\u0003\u0002\u0002\u0002\u010c\u010a\u0003\u0002\u0002\u0002\u010c\u010b",
    "\u0003\u0002\u0002\u0002\u010d\u010f\u0003\u0002\u0002\u0002\u010e\u0103",
    "\u0003\u0002\u0002\u0002\u010e\u010c\u0003\u0002\u0002\u0002\u010f\u0118",
    "\u0003\u0002\u0002\u0002\u0110\u0111\f\u0005\u0002\u0002\u0111\u0112",
    "\u0005\u001a\u000e\u0002\u0112\u0113\u00058\u001d\u0006\u0113\u0117",
    "\u0003\u0002\u0002\u0002\u0114\u0115\f\u0003\u0002\u0002\u0115\u0117",
    "\u0007\u0013\u0002\u0002\u0116\u0110\u0003\u0002\u0002\u0002\u0116\u0114",
    "\u0003\u0002\u0002\u0002\u0117\u011a\u0003\u0002\u0002\u0002\u0118\u0116",
    "\u0003\u0002\u0002\u0002\u0118\u0119\u0003\u0002\u0002\u0002\u01199",
    "\u0003\u0002\u0002\u0002\u011a\u0118\u0003\u0002\u0002\u0002\u011b\u011c",
    "\u0007 \u0002\u0002\u011c\u011d\u0005> \u0002\u011d;\u0003\u0002\u0002",
    "\u0002\u011e\u011f\u0005\u0010\t\u0002\u011f\u0120\u0005j6\u0002\u0120",
    "=\u0003\u0002\u0002\u0002\u0121\u0122\u0005\u0018\r\u0002\u0122\u0123",
    "\u0005@!\u0002\u0123?\u0003\u0002\u0002\u0002\u0124\u0125\b!\u0001\u0002",
    "\u0125\u0126\u0007\u0016\u0002\u0002\u0126\u0127\u0005@!\u0002\u0127",
    "\u0128\u0007\u0017\u0002\u0002\u0128\u012e\u0003\u0002\u0002\u0002\u0129",
    "\u012c\u0005$\u0013\u0002\u012a\u012c\u0005J&\u0002\u012b\u0129\u0003",
    "\u0002\u0002\u0002\u012b\u012a\u0003\u0002\u0002\u0002\u012c\u012e\u0003",
    "\u0002\u0002\u0002\u012d\u0124\u0003\u0002\u0002\u0002\u012d\u012b\u0003",
    "\u0002\u0002\u0002\u012e\u0137\u0003\u0002\u0002\u0002\u012f\u0130\f",
    "\u0005\u0002\u0002\u0130\u0131\u0005\u001a\u000e\u0002\u0131\u0132\u0005",
    "@!\u0006\u0132\u0136\u0003\u0002\u0002\u0002\u0133\u0134\f\u0003\u0002",
    "\u0002\u0134\u0136\u0007\u0013\u0002\u0002\u0135\u012f\u0003\u0002\u0002",
    "\u0002\u0135\u0133\u0003\u0002\u0002\u0002\u0136\u0139\u0003\u0002\u0002",
    "\u0002\u0137\u0135\u0003\u0002\u0002\u0002\u0137\u0138\u0003\u0002\u0002",
    "\u0002\u0138A\u0003\u0002\u0002\u0002\u0139\u0137\u0003\u0002\u0002",
    "\u0002\u013a\u013b\u0007!\u0002\u0002\u013b\u013c\u0005D#\u0002\u013c",
    "C\u0003\u0002\u0002\u0002\u013d\u013e\u0005\u0006\u0004\u0002\u013e",
    "\u0140\u0007\u0013\u0002\u0002\u013f\u0141\u0005F$\u0002\u0140\u013f",
    "\u0003\u0002\u0002\u0002\u0140\u0141\u0003\u0002\u0002\u0002\u0141\u0144",
    "\u0003\u0002\u0002\u0002\u0142\u0144\u0005F$\u0002\u0143\u013d\u0003",
    "\u0002\u0002\u0002\u0143\u0142\u0003\u0002\u0002\u0002\u0144E\u0003",
    "\u0002\u0002\u0002\u0145\u0146\u0005\u0018\r\u0002\u0146\u0147\u0005",
    "H%\u0002\u0147G\u0003\u0002\u0002\u0002\u0148\u0149\b%\u0001\u0002\u0149",
    "\u014a\u0007\u0016\u0002\u0002\u014a\u014b\u0005H%\u0002\u014b\u014c",
    "\u0007\u0017\u0002\u0002\u014c\u0153\u0003\u0002\u0002\u0002\u014d\u0151",
    "\u0005R*\u0002\u014e\u0151\u0005\u001c\u000f\u0002\u014f\u0151\u0005",
    " \u0011\u0002\u0150\u014d\u0003\u0002\u0002\u0002\u0150\u014e\u0003",
    "\u0002\u0002\u0002\u0150\u014f\u0003\u0002\u0002\u0002\u0151\u0153\u0003",
    "\u0002\u0002\u0002\u0152\u0148\u0003\u0002\u0002\u0002\u0152\u0150\u0003",
    "\u0002\u0002\u0002\u0153\u015c\u0003\u0002\u0002\u0002\u0154\u0155\f",
    "\u0005\u0002\u0002\u0155\u0156\u0005\u001a\u000e\u0002\u0156\u0157\u0005",
    "H%\u0006\u0157\u015b\u0003\u0002\u0002\u0002\u0158\u0159\f\u0003\u0002",
    "\u0002\u0159\u015b\u0007\u0013\u0002\u0002\u015a\u0154\u0003\u0002\u0002",
    "\u0002\u015a\u0158\u0003\u0002\u0002\u0002\u015b\u015e\u0003\u0002\u0002",
    "\u0002\u015c\u015a\u0003\u0002\u0002\u0002\u015c\u015d\u0003\u0002\u0002",
    "\u0002\u015dI\u0003\u0002\u0002\u0002\u015e\u015c\u0003\u0002\u0002",
    "\u0002\u015f\u0161\u0007!\u0002\u0002\u0160\u0162\u0005L\'\u0002\u0161",
    "\u0160\u0003\u0002\u0002\u0002\u0161\u0162\u0003\u0002\u0002\u0002\u0162",
    "K\u0003\u0002\u0002\u0002\u0163\u0164\u0005\u0006\u0004\u0002\u0164",
    "\u0166\u0007\u0013\u0002\u0002\u0165\u0167\u0005N(\u0002\u0166\u0165",
    "\u0003\u0002\u0002\u0002\u0166\u0167\u0003\u0002\u0002\u0002\u0167\u016a",
    "\u0003\u0002\u0002\u0002\u0168\u016a\u0005N(\u0002\u0169\u0163\u0003",
    "\u0002\u0002\u0002\u0169\u0168\u0003\u0002\u0002\u0002\u016aM\u0003",
    "\u0002\u0002\u0002\u016b\u016c\u0005\u0018\r\u0002\u016c\u016d\u0005",
    "P)\u0002\u016dO\u0003\u0002\u0002\u0002\u016e\u016f\b)\u0001\u0002\u016f",
    "\u0170\u0007\u0016\u0002\u0002\u0170\u0171\u0005P)\u0002\u0171\u0172",
    "\u0007\u0017\u0002\u0002\u0172\u0179\u0003\u0002\u0002\u0002\u0173\u0177",
    "\u0005R*\u0002\u0174\u0177\u0005\u001c\u000f\u0002\u0175\u0177\u0005",
    "$\u0013\u0002\u0176\u0173\u0003\u0002\u0002\u0002\u0176\u0174\u0003",
    "\u0002\u0002\u0002\u0176\u0175\u0003\u0002\u0002\u0002\u0177\u0179\u0003",
    "\u0002\u0002\u0002\u0178\u016e\u0003\u0002\u0002\u0002\u0178\u0176\u0003",
    "\u0002\u0002\u0002\u0179\u0182\u0003\u0002\u0002\u0002\u017a\u017b\f",
    "\u0005\u0002\u0002\u017b\u017c\u0005\u001a\u000e\u0002\u017c\u017d\u0005",
    "P)\u0006\u017d\u0181\u0003\u0002\u0002\u0002\u017e\u017f\f\u0003\u0002",
    "\u0002\u017f\u0181\u0007\u0013\u0002\u0002\u0180\u017a\u0003\u0002\u0002",
    "\u0002\u0180\u017e\u0003\u0002\u0002\u0002\u0181\u0184\u0003\u0002\u0002",
    "\u0002\u0182\u0180\u0003\u0002\u0002\u0002\u0182\u0183\u0003\u0002\u0002",
    "\u0002\u0183Q\u0003\u0002\u0002\u0002\u0184\u0182\u0003\u0002\u0002",
    "\u0002\u0185\u0186\u0007\"\u0002\u0002\u0186\u0187\u0005T+\u0002\u0187",
    "S\u0003\u0002\u0002\u0002\u0188\u0189\u0005\u0006\u0004\u0002\u0189",
    "\u018a\u0007\u0013\u0002\u0002\u018aU\u0003\u0002\u0002\u0002\u018b",
    "\u018c\u0007#\u0002\u0002\u018c\u018d\u0005X-\u0002\u018dW\u0003\u0002",
    "\u0002\u0002\u018e\u018f\u0005\u0018\r\u0002\u018f\u0190\u0005Z.\u0002",
    "\u0190Y\u0003\u0002\u0002\u0002\u0191\u0192\b.\u0001\u0002\u0192\u0193",
    "\u0007\u0016\u0002\u0002\u0193\u0194\u0005Z.\u0002\u0194\u0195\u0007",
    "\u0017\u0002\u0002\u0195\u019c\u0003\u0002\u0002\u0002\u0196\u019a\u0005",
    "$\u0013\u0002\u0197\u019a\u0005R*\u0002\u0198\u019a\u0005\\/\u0002\u0199",
    "\u0196\u0003\u0002\u0002\u0002\u0199\u0197\u0003\u0002\u0002\u0002\u0199",
    "\u0198\u0003\u0002\u0002\u0002\u019a\u019c\u0003\u0002\u0002\u0002\u019b",
    "\u0191\u0003\u0002\u0002\u0002\u019b\u0199\u0003\u0002\u0002\u0002\u019c",
    "\u01a5\u0003\u0002\u0002\u0002\u019d\u019e\f\u0005\u0002\u0002\u019e",
    "\u019f\u0005\u001a\u000e\u0002\u019f\u01a0\u0005Z.\u0006\u01a0\u01a4",
    "\u0003\u0002\u0002\u0002\u01a1\u01a2\f\u0003\u0002\u0002\u01a2\u01a4",
    "\u0007\u0013\u0002\u0002\u01a3\u019d\u0003\u0002\u0002\u0002\u01a3\u01a1",
    "\u0003\u0002\u0002\u0002\u01a4\u01a7\u0003\u0002\u0002\u0002\u01a5\u01a3",
    "\u0003\u0002\u0002\u0002\u01a5\u01a6\u0003\u0002\u0002\u0002\u01a6[",
    "\u0003\u0002\u0002\u0002\u01a7\u01a5\u0003\u0002\u0002\u0002\u01a8\u01a9",
    "\u0007$\u0002\u0002\u01a9\u01aa\u0005^0\u0002\u01aa]\u0003\u0002\u0002",
    "\u0002\u01ab\u01ac\u0005\u0018\r\u0002\u01ac\u01ad\u0005`1\u0002\u01ad",
    "_\u0003\u0002\u0002\u0002\u01ae\u01af\b1\u0001\u0002\u01af\u01b0\u0007",
    "\u0016\u0002\u0002\u01b0\u01b1\u0005`1\u0002\u01b1\u01b2\u0007\u0017",
    "\u0002\u0002\u01b2\u01b5\u0003\u0002\u0002\u0002\u01b3\u01b5\u0005b",
    "2\u0002\u01b4\u01ae\u0003\u0002\u0002\u0002\u01b4\u01b3\u0003\u0002",
    "\u0002\u0002\u01b5\u01be\u0003\u0002\u0002\u0002\u01b6\u01b7\f\u0005",
    "\u0002\u0002\u01b7\u01b8\u0005\u001a\u000e\u0002\u01b8\u01b9\u0005`",
    "1\u0006\u01b9\u01bd\u0003\u0002\u0002\u0002\u01ba\u01bb\f\u0003\u0002",
    "\u0002\u01bb\u01bd\u0007\u0013\u0002\u0002\u01bc\u01b6\u0003\u0002\u0002",
    "\u0002\u01bc\u01ba\u0003\u0002\u0002\u0002\u01bd\u01c0\u0003\u0002\u0002",
    "\u0002\u01be\u01bc\u0003\u0002\u0002\u0002\u01be\u01bf\u0003\u0002\u0002",
    "\u0002\u01bfa\u0003\u0002\u0002\u0002\u01c0\u01be\u0003\u0002\u0002",
    "\u0002\u01c1\u01c2\u0007%\u0002\u0002\u01c2\u01c3\u0005d3\u0002\u01c3",
    "c\u0003\u0002\u0002\u0002\u01c4\u01c5\u0005\u0006\u0004\u0002\u01c5",
    "\u01c7\u0007\u0013\u0002\u0002\u01c6\u01c8\u0005f4\u0002\u01c7\u01c6",
    "\u0003\u0002\u0002\u0002\u01c7\u01c8\u0003\u0002\u0002\u0002\u01c8\u01cb",
    "\u0003\u0002\u0002\u0002\u01c9\u01cb\u0005f4\u0002\u01ca\u01c4\u0003",
    "\u0002\u0002\u0002\u01ca\u01c9\u0003\u0002\u0002\u0002\u01cbe\u0003",
    "\u0002\u0002\u0002\u01cc\u01cd\u0005\u0018\r\u0002\u01cd\u01ce\u0005",
    "h5\u0002\u01ceg\u0003\u0002\u0002\u0002\u01cf\u01d0\b5\u0001\u0002\u01d0",
    "\u01d1\u0007\u0016\u0002\u0002\u01d1\u01d2\u0005h5\u0002\u01d2\u01d3",
    "\u0007\u0017\u0002\u0002\u01d3\u01da\u0003\u0002\u0002\u0002\u01d4\u01d8",
    "\u0005R*\u0002\u01d5\u01d8\u0005\u001c\u000f\u0002\u01d6\u01d8\u0005",
    " \u0011\u0002\u01d7\u01d4\u0003\u0002\u0002\u0002\u01d7\u01d5\u0003",
    "\u0002\u0002\u0002\u01d7\u01d6\u0003\u0002\u0002\u0002\u01d8\u01da\u0003",
    "\u0002\u0002\u0002\u01d9\u01cf\u0003\u0002\u0002\u0002\u01d9\u01d7\u0003",
    "\u0002\u0002\u0002\u01da\u01e3\u0003\u0002\u0002\u0002\u01db\u01dc\f",
    "\u0005\u0002\u0002\u01dc\u01dd\u0005\u001a\u000e\u0002\u01dd\u01de\u0005",
    "h5\u0006\u01de\u01e2\u0003\u0002\u0002\u0002\u01df\u01e0\f\u0003\u0002",
    "\u0002\u01e0\u01e2\u0007\u0013\u0002\u0002\u01e1\u01db\u0003\u0002\u0002",
    "\u0002\u01e1\u01df\u0003\u0002\u0002\u0002\u01e2\u01e5\u0003\u0002\u0002",
    "\u0002\u01e3\u01e1\u0003\u0002\u0002\u0002\u01e3\u01e4\u0003\u0002\u0002",
    "\u0002\u01e4i\u0003\u0002\u0002\u0002\u01e5\u01e3\u0003\u0002\u0002",
    "\u0002\u01e6\u01e7\u0007&\u0002\u0002\u01e7\u01e8\u0005l7\u0002\u01e8",
    "k\u0003\u0002\u0002\u0002\u01e9\u01ea\u0005\u0018\r\u0002\u01ea\u01eb",
    "\u0005n8\u0002\u01ebm\u0003\u0002\u0002\u0002\u01ec\u01ed\b8\u0001\u0002",
    "\u01ed\u01ee\u0007\u0016\u0002\u0002\u01ee\u01ef\u0005n8\u0002\u01ef",
    "\u01f0\u0007\u0017\u0002\u0002\u01f0\u01fc\u0003\u0002\u0002\u0002\u01f1",
    "\u01fa\u0005$\u0013\u0002\u01f2\u01fa\u0005,\u0017\u0002\u01f3\u01fa",
    "\u00050\u0019\u0002\u01f4\u01fa\u00054\u001b\u0002\u01f5\u01fa\u0005",
    ":\u001e\u0002\u01f6\u01fa\u0005V,\u0002\u01f7\u01fa\u0005\\/\u0002\u01f8",
    "\u01fa\u0005p9\u0002\u01f9\u01f1\u0003\u0002\u0002\u0002\u01f9\u01f2",
    "\u0003\u0002\u0002\u0002\u01f9\u01f3\u0003\u0002\u0002\u0002\u01f9\u01f4",
    "\u0003\u0002\u0002\u0002\u01f9\u01f5\u0003\u0002\u0002\u0002\u01f9\u01f6",
    "\u0003\u0002\u0002\u0002\u01f9\u01f7\u0003\u0002\u0002\u0002\u01f9\u01f8",
    "\u0003\u0002\u0002\u0002\u01fa\u01fc\u0003\u0002\u0002\u0002\u01fb\u01ec",
    "\u0003\u0002\u0002\u0002\u01fb\u01f9\u0003\u0002\u0002\u0002\u01fc\u0205",
    "\u0003\u0002\u0002\u0002\u01fd\u01fe\f\u0005\u0002\u0002\u01fe\u01ff",
    "\u0005\u001a\u000e\u0002\u01ff\u0200\u0005n8\u0006\u0200\u0204\u0003",
    "\u0002\u0002\u0002\u0201\u0202\f\u0003\u0002\u0002\u0202\u0204\u0007",
    "\u0013\u0002\u0002\u0203\u01fd\u0003\u0002\u0002\u0002\u0203\u0201\u0003",
    "\u0002\u0002\u0002\u0204\u0207\u0003\u0002\u0002\u0002\u0205\u0203\u0003",
    "\u0002\u0002\u0002\u0205\u0206\u0003\u0002\u0002\u0002\u0206o\u0003",
    "\u0002\u0002\u0002\u0207\u0205\u0003\u0002\u0002\u0002\u0208\u0209\u0007",
    "\'\u0002\u0002\u0209q\u0003\u0002\u0002\u00027uy|\u0081\u009a\u00a0",
    "\u00a2\u00ba\u00ce\u00d1\u00dc\u00e4\u00e6\u00f1\u00fb\u010c\u010e\u0116",
    "\u0118\u012b\u012d\u0135\u0137\u0140\u0143\u0150\u0152\u015a\u015c\u0161",
    "\u0166\u0169\u0176\u0178\u0180\u0182\u0199\u019b\u01a3\u01a5\u01b4\u01bc",
    "\u01be\u01c7\u01ca\u01d7\u01d9\u01e1\u01e3\u01f9\u01fb\u0203\u0205"].join("");


const atn = new antlr4.atn.ATNDeserializer().deserialize(serializedATN);

const decisionsToDFA = atn.decisionToState.map( (ds, index) => new antlr4.dfa.DFA(ds, index) );

const sharedContextCache = new antlr4.PredictionContextCache();

export default class RulepadGrammarParser extends antlr4.Parser {

    static grammarFileName = "RulepadGrammar.g4";
    static literalNames = [ null, "'\"'", "'.'", "'='", "'>'", "'<'", "'''", 
                            "'&'", "'|'", "'['", "']'", "'must '", "'of '", 
                            "'and '", "'or '", "'have '", "'with '", null, 
                            null, null, "'('", "')'", "'name '", "'value '", 
                            "'annotation '", "'extension '", "'Superclass'", 
                            "'implementation '", "'Interface '", null, "'constructor '", 
                            "'parameter '", "'type '", null, "'configuration file '", 
                            "'property '", "'class '", "'bean declaration '" ];
    static symbolicNames = [ null, null, null, null, null, null, null, null, 
                             null, null, null, null, null, null, null, null, 
                             null, "SPACE", "Alphabet", "NL", "LPAREN", 
                             "RPAREN", "NAME", "VALUE", "ANNOTATION", "EXTENSION", 
                             "SUPERCLASS", "IMPLEMENTATION", "INTERFACE", 
                             "FUNCTION", "CONSTRUCTOR", "PARAMETER", "TYPES", 
                             "DeclarationStatement", "ConfigurationFile", 
                             "CONFIGURATION_PROPERTIES", "CLASSES", "BEAN_DECL" ];
    static ruleNames = [ "inputSentence", "mustClause", "combinatorialWords", 
                         "symbols", "end", "emptyLine", "must", "of", "and_", 
                         "or_", "have", "withWord", "binary", "names", "nameCondition", 
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
    	case 20:
    	    		return this.annotationExpression_sempred(localctx, predIndex);
    	case 27:
    	    		return this.functionExpression_sempred(localctx, predIndex);
    	case 31:
    	    		return this.constructorExpression_sempred(localctx, predIndex);
    	case 35:
    	    		return this.parameterExpression_sempred(localctx, predIndex);
    	case 39:
    	    		return this.functionParameterExpression_sempred(localctx, predIndex);
    	case 44:
    	    		return this.declarationStatementExpression_sempred(localctx, predIndex);
    	case 47:
    	    		return this.configurationFileExpression_sempred(localctx, predIndex);
    	case 51:
    	    		return this.configurationPropertyExpression_sempred(localctx, predIndex);
    	case 54:
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
	        this.state = 119;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.EOF:
	        case RulepadGrammarParser.T__1:
	        case RulepadGrammarParser.NL:
	            this.state = 115;
	            this._errHandler.sync(this);
	            let _alt = this._interp.adaptivePredict(this._input,0,this._ctx)
	            while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
	                if(_alt===1) {
	                    this.state = 112;
	                    this.emptyLine(); 
	                }
	                this.state = 117;
	                this._errHandler.sync(this);
	                _alt = this._interp.adaptivePredict(this._input,0,this._ctx);
	            }

	            break;
	        case RulepadGrammarParser.FUNCTION:
	        case RulepadGrammarParser.CONSTRUCTOR:
	        case RulepadGrammarParser.DeclarationStatement:
	        case RulepadGrammarParser.CLASSES:
	            this.state = 118;
	            this.mustClause();
	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	        this.state = 122;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        if(_la===RulepadGrammarParser.T__1) {
	            this.state = 121;
	            this.end();
	        }

	        this.state = 127;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        while(_la===RulepadGrammarParser.NL) {
	            this.state = 124;
	            this.match(RulepadGrammarParser.NL);
	            this.state = 129;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	        }
	        this.state = 130;
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
	        this.state = 152;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.FUNCTION:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 132;
	            this.functions();
	            this.state = 133;
	            this.must();
	            this.state = 134;
	            this.have();
	            this.state = 135;
	            this.functionExpression(0);
	            break;
	        case RulepadGrammarParser.CONSTRUCTOR:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 137;
	            this.constructors();
	            this.state = 138;
	            this.must();
	            this.state = 139;
	            this.have();
	            this.state = 140;
	            this.constructorExpression(0);
	            break;
	        case RulepadGrammarParser.CLASSES:
	            this.enterOuterAlt(localctx, 3);
	            this.state = 142;
	            this.classes();
	            this.state = 143;
	            this.must();
	            this.state = 144;
	            this.have();
	            this.state = 145;
	            this.classExpression(0);
	            break;
	        case RulepadGrammarParser.DeclarationStatement:
	            this.enterOuterAlt(localctx, 4);
	            this.state = 147;
	            this.declarationStatements();
	            this.state = 148;
	            this.must();
	            this.state = 149;
	            this.have();
	            this.state = 150;
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



	combinatorialWords() {
	    let localctx = new CombinatorialWordsContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 4, RulepadGrammarParser.RULE_combinatorialWords);
	    var _la = 0; // Token type
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 154;
	        this.match(RulepadGrammarParser.T__0);
	        this.state = 158; 
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        do {
	            this.state = 158;
	            this._errHandler.sync(this);
	            switch(this._input.LA(1)) {
	            case RulepadGrammarParser.Alphabet:
	                this.state = 155;
	                this.match(RulepadGrammarParser.Alphabet);
	                break;
	            case RulepadGrammarParser.T__1:
	            case RulepadGrammarParser.T__2:
	            case RulepadGrammarParser.T__3:
	            case RulepadGrammarParser.T__4:
	            case RulepadGrammarParser.T__5:
	            case RulepadGrammarParser.T__6:
	            case RulepadGrammarParser.T__7:
	            case RulepadGrammarParser.T__8:
	            case RulepadGrammarParser.T__9:
	            case RulepadGrammarParser.LPAREN:
	            case RulepadGrammarParser.RPAREN:
	                this.state = 156;
	                this.symbols();
	                break;
	            case RulepadGrammarParser.SPACE:
	                this.state = 157;
	                this.match(RulepadGrammarParser.SPACE);
	                break;
	            default:
	                throw new antlr4.error.NoViableAltException(this);
	            }
	            this.state = 160; 
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	        } while((((_la) & ~0x1f) == 0 && ((1 << _la) & ((1 << RulepadGrammarParser.T__1) | (1 << RulepadGrammarParser.T__2) | (1 << RulepadGrammarParser.T__3) | (1 << RulepadGrammarParser.T__4) | (1 << RulepadGrammarParser.T__5) | (1 << RulepadGrammarParser.T__6) | (1 << RulepadGrammarParser.T__7) | (1 << RulepadGrammarParser.T__8) | (1 << RulepadGrammarParser.T__9) | (1 << RulepadGrammarParser.SPACE) | (1 << RulepadGrammarParser.Alphabet) | (1 << RulepadGrammarParser.LPAREN) | (1 << RulepadGrammarParser.RPAREN))) !== 0));
	        this.state = 162;
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
	    this.enterRule(localctx, 6, RulepadGrammarParser.RULE_symbols);
	    var _la = 0; // Token type
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 164;
	        _la = this._input.LA(1);
	        if(!((((_la) & ~0x1f) == 0 && ((1 << _la) & ((1 << RulepadGrammarParser.T__1) | (1 << RulepadGrammarParser.T__2) | (1 << RulepadGrammarParser.T__3) | (1 << RulepadGrammarParser.T__4) | (1 << RulepadGrammarParser.T__5) | (1 << RulepadGrammarParser.T__6) | (1 << RulepadGrammarParser.T__7) | (1 << RulepadGrammarParser.T__8) | (1 << RulepadGrammarParser.T__9) | (1 << RulepadGrammarParser.LPAREN) | (1 << RulepadGrammarParser.RPAREN))) !== 0))) {
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
	    this.enterRule(localctx, 8, RulepadGrammarParser.RULE_end);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 166;
	        this.match(RulepadGrammarParser.T__1);
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
	    this.enterRule(localctx, 10, RulepadGrammarParser.RULE_emptyLine);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 168;
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



	must() {
	    let localctx = new MustContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 12, RulepadGrammarParser.RULE_must);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 170;
	        this.match(RulepadGrammarParser.T__10);
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
	    this.enterRule(localctx, 14, RulepadGrammarParser.RULE_of);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 172;
	        this.match(RulepadGrammarParser.T__11);
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
	    this.enterRule(localctx, 16, RulepadGrammarParser.RULE_and_);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 174;
	        this.match(RulepadGrammarParser.T__12);
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
	    this.enterRule(localctx, 18, RulepadGrammarParser.RULE_or_);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 176;
	        this.match(RulepadGrammarParser.T__13);
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
	    this.enterRule(localctx, 20, RulepadGrammarParser.RULE_have);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 178;
	        this.match(RulepadGrammarParser.T__14);
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
	    this.enterRule(localctx, 22, RulepadGrammarParser.RULE_withWord);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 180;
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



	binary() {
	    let localctx = new BinaryContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 24, RulepadGrammarParser.RULE_binary);
	    try {
	        this.state = 184;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.T__12:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 182;
	            this.and_();
	            break;
	        case RulepadGrammarParser.T__13:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 183;
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
	    this.enterRule(localctx, 26, RulepadGrammarParser.RULE_names);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 186;
	        this.match(RulepadGrammarParser.NAME);
	        this.state = 187;
	        this.nameCondition();
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
	    this.enterRule(localctx, 28, RulepadGrammarParser.RULE_nameCondition);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 189;
	        this.combinatorialWords();
	        this.state = 190;
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
	    this.enterRule(localctx, 30, RulepadGrammarParser.RULE_values);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 192;
	        this.match(RulepadGrammarParser.VALUE);
	        this.state = 193;
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
	    this.enterRule(localctx, 32, RulepadGrammarParser.RULE_valueCondition);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 195;
	        this.combinatorialWords();
	        this.state = 196;
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
	    this.enterRule(localctx, 34, RulepadGrammarParser.RULE_annotations);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 198;
	        this.match(RulepadGrammarParser.ANNOTATION);
	        this.state = 199;
	        this.annotationCondition();
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
	    this.enterRule(localctx, 36, RulepadGrammarParser.RULE_annotationCondition);
	    try {
	        this.state = 207;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.T__0:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 201;
	            this.combinatorialWords();
	            this.state = 202;
	            this.match(RulepadGrammarParser.SPACE);
	            this.state = 204;
	            this._errHandler.sync(this);
	            var la_ = this._interp.adaptivePredict(this._input,8,this._ctx);
	            if(la_===1) {
	                this.state = 203;
	                this.annotationConditionTransition();

	            }
	            break;
	        case RulepadGrammarParser.T__15:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 206;
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
	    this.enterRule(localctx, 38, RulepadGrammarParser.RULE_annotationConditionTransition);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 209;
	        this.withWord();
	        this.state = 210;
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
	    const _startState = 40;
	    this.enterRecursionRule(localctx, 40, RulepadGrammarParser.RULE_annotationExpression, _p);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 218;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.LPAREN:
	            this.state = 213;
	            this.match(RulepadGrammarParser.LPAREN);
	            this.state = 214;
	            this.annotationExpression(0);
	            this.state = 215;
	            this.match(RulepadGrammarParser.RPAREN);
	            break;
	        case RulepadGrammarParser.PARAMETER:
	            this.state = 217;
	            this.parameters();
	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	        this._ctx.stop = this._input.LT(-1);
	        this.state = 228;
	        this._errHandler.sync(this);
	        let _alt = this._interp.adaptivePredict(this._input,12,this._ctx)
	        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
	            if(_alt===1) {
	                if(this._parseListeners!==null) {
	                    this.triggerExitRuleEvent();
	                }
	                _prevctx = localctx;
	                this.state = 226;
	                this._errHandler.sync(this);
	                var la_ = this._interp.adaptivePredict(this._input,11,this._ctx);
	                switch(la_) {
	                case 1:
	                    localctx = new AnnotationExpressionContext(this, _parentctx, _parentState);
	                    localctx.left = _prevctx;
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_annotationExpression);
	                    this.state = 220;
	                    if (!( this.precpred(this._ctx, 3))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 3)");
	                    }
	                    this.state = 221;
	                    localctx.op = this.binary();
	                    this.state = 222;
	                    localctx.right = this.annotationExpression(4);
	                    break;

	                case 2:
	                    localctx = new AnnotationExpressionContext(this, _parentctx, _parentState);
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_annotationExpression);
	                    this.state = 224;
	                    if (!( this.precpred(this._ctx, 1))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 1)");
	                    }
	                    this.state = 225;
	                    this.match(RulepadGrammarParser.SPACE);
	                    break;

	                } 
	            }
	            this.state = 230;
	            this._errHandler.sync(this);
	            _alt = this._interp.adaptivePredict(this._input,12,this._ctx);
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
	    this.enterRule(localctx, 42, RulepadGrammarParser.RULE_extensions);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 231;
	        this.match(RulepadGrammarParser.EXTENSION);
	        this.state = 232;
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
	    this.enterRule(localctx, 44, RulepadGrammarParser.RULE_extensionCondition);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 234;
	        this.of();
	        this.state = 239;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.T__0:
	            this.state = 235;
	            this.combinatorialWords();
	            this.state = 236;
	            this.match(RulepadGrammarParser.SPACE);
	            break;
	        case RulepadGrammarParser.SUPERCLASS:
	            this.state = 238;
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
	    this.enterRule(localctx, 46, RulepadGrammarParser.RULE_implementations);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 241;
	        this.match(RulepadGrammarParser.IMPLEMENTATION);
	        this.state = 242;
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
	    this.enterRule(localctx, 48, RulepadGrammarParser.RULE_implementationCondition);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 244;
	        this.of();
	        this.state = 249;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.T__0:
	            this.state = 245;
	            this.combinatorialWords();
	            this.state = 246;
	            this.match(RulepadGrammarParser.SPACE);
	            break;
	        case RulepadGrammarParser.INTERFACE:
	            this.state = 248;
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
	    this.enterRule(localctx, 50, RulepadGrammarParser.RULE_functions);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 251;
	        this.match(RulepadGrammarParser.FUNCTION);
	        this.state = 252;
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
	    this.enterRule(localctx, 52, RulepadGrammarParser.RULE_functionCondition);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 254;
	        this.withWord();
	        this.state = 255;
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
	    const _startState = 54;
	    this.enterRecursionRule(localctx, 54, RulepadGrammarParser.RULE_functionExpression, _p);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 268;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.LPAREN:
	            this.state = 258;
	            this.match(RulepadGrammarParser.LPAREN);
	            this.state = 259;
	            this.functionExpression(0);
	            this.state = 260;
	            this.match(RulepadGrammarParser.RPAREN);
	            break;
	        case RulepadGrammarParser.ANNOTATION:
	        case RulepadGrammarParser.PARAMETER:
	        case RulepadGrammarParser.TYPES:
	        case RulepadGrammarParser.ConfigurationFile:
	            this.state = 266;
	            this._errHandler.sync(this);
	            switch(this._input.LA(1)) {
	            case RulepadGrammarParser.ANNOTATION:
	                this.state = 262;
	                this.annotations();
	                break;
	            case RulepadGrammarParser.TYPES:
	                this.state = 263;
	                this.types();
	                break;
	            case RulepadGrammarParser.PARAMETER:
	                this.state = 264;
	                this.functionParameters();
	                break;
	            case RulepadGrammarParser.ConfigurationFile:
	                this.state = 265;
	                this.configurationFiles();
	                break;
	            default:
	                throw new antlr4.error.NoViableAltException(this);
	            }
	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	        this._ctx.stop = this._input.LT(-1);
	        this.state = 278;
	        this._errHandler.sync(this);
	        let _alt = this._interp.adaptivePredict(this._input,18,this._ctx)
	        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
	            if(_alt===1) {
	                if(this._parseListeners!==null) {
	                    this.triggerExitRuleEvent();
	                }
	                _prevctx = localctx;
	                this.state = 276;
	                this._errHandler.sync(this);
	                var la_ = this._interp.adaptivePredict(this._input,17,this._ctx);
	                switch(la_) {
	                case 1:
	                    localctx = new FunctionExpressionContext(this, _parentctx, _parentState);
	                    localctx.left = _prevctx;
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_functionExpression);
	                    this.state = 270;
	                    if (!( this.precpred(this._ctx, 3))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 3)");
	                    }
	                    this.state = 271;
	                    localctx.op = this.binary();
	                    this.state = 272;
	                    localctx.right = this.functionExpression(4);
	                    break;

	                case 2:
	                    localctx = new FunctionExpressionContext(this, _parentctx, _parentState);
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_functionExpression);
	                    this.state = 274;
	                    if (!( this.precpred(this._ctx, 1))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 1)");
	                    }
	                    this.state = 275;
	                    this.match(RulepadGrammarParser.SPACE);
	                    break;

	                } 
	            }
	            this.state = 280;
	            this._errHandler.sync(this);
	            _alt = this._interp.adaptivePredict(this._input,18,this._ctx);
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
	    this.enterRule(localctx, 56, RulepadGrammarParser.RULE_constructors);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 281;
	        this.match(RulepadGrammarParser.CONSTRUCTOR);
	        this.state = 282;
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
	    this.enterRule(localctx, 58, RulepadGrammarParser.RULE_constructorOf);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 284;
	        this.of();
	        this.state = 285;
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
	    this.enterRule(localctx, 60, RulepadGrammarParser.RULE_constructorCondition);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 287;
	        this.withWord();
	        this.state = 288;
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
	    const _startState = 62;
	    this.enterRecursionRule(localctx, 62, RulepadGrammarParser.RULE_constructorExpression, _p);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 299;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.LPAREN:
	            this.state = 291;
	            this.match(RulepadGrammarParser.LPAREN);
	            this.state = 292;
	            this.constructorExpression(0);
	            this.state = 293;
	            this.match(RulepadGrammarParser.RPAREN);
	            break;
	        case RulepadGrammarParser.ANNOTATION:
	        case RulepadGrammarParser.PARAMETER:
	            this.state = 297;
	            this._errHandler.sync(this);
	            switch(this._input.LA(1)) {
	            case RulepadGrammarParser.ANNOTATION:
	                this.state = 295;
	                this.annotations();
	                break;
	            case RulepadGrammarParser.PARAMETER:
	                this.state = 296;
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
	        this.state = 309;
	        this._errHandler.sync(this);
	        let _alt = this._interp.adaptivePredict(this._input,22,this._ctx)
	        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
	            if(_alt===1) {
	                if(this._parseListeners!==null) {
	                    this.triggerExitRuleEvent();
	                }
	                _prevctx = localctx;
	                this.state = 307;
	                this._errHandler.sync(this);
	                var la_ = this._interp.adaptivePredict(this._input,21,this._ctx);
	                switch(la_) {
	                case 1:
	                    localctx = new ConstructorExpressionContext(this, _parentctx, _parentState);
	                    localctx.left = _prevctx;
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_constructorExpression);
	                    this.state = 301;
	                    if (!( this.precpred(this._ctx, 3))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 3)");
	                    }
	                    this.state = 302;
	                    localctx.op = this.binary();
	                    this.state = 303;
	                    localctx.right = this.constructorExpression(4);
	                    break;

	                case 2:
	                    localctx = new ConstructorExpressionContext(this, _parentctx, _parentState);
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_constructorExpression);
	                    this.state = 305;
	                    if (!( this.precpred(this._ctx, 1))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 1)");
	                    }
	                    this.state = 306;
	                    this.match(RulepadGrammarParser.SPACE);
	                    break;

	                } 
	            }
	            this.state = 311;
	            this._errHandler.sync(this);
	            _alt = this._interp.adaptivePredict(this._input,22,this._ctx);
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
	    this.enterRule(localctx, 64, RulepadGrammarParser.RULE_parameters);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 312;
	        this.match(RulepadGrammarParser.PARAMETER);
	        this.state = 313;
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
	    this.enterRule(localctx, 66, RulepadGrammarParser.RULE_parameterCondition);
	    try {
	        this.state = 321;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.T__0:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 315;
	            this.combinatorialWords();
	            this.state = 316;
	            this.match(RulepadGrammarParser.SPACE);
	            this.state = 318;
	            this._errHandler.sync(this);
	            var la_ = this._interp.adaptivePredict(this._input,23,this._ctx);
	            if(la_===1) {
	                this.state = 317;
	                this.parameterConditionTransition();

	            }
	            break;
	        case RulepadGrammarParser.T__15:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 320;
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
	    this.enterRule(localctx, 68, RulepadGrammarParser.RULE_parameterConditionTransition);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 323;
	        this.withWord();
	        this.state = 324;
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
	    const _startState = 70;
	    this.enterRecursionRule(localctx, 70, RulepadGrammarParser.RULE_parameterExpression, _p);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 336;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.LPAREN:
	            this.state = 327;
	            this.match(RulepadGrammarParser.LPAREN);
	            this.state = 328;
	            this.parameterExpression(0);
	            this.state = 329;
	            this.match(RulepadGrammarParser.RPAREN);
	            break;
	        case RulepadGrammarParser.NAME:
	        case RulepadGrammarParser.VALUE:
	        case RulepadGrammarParser.TYPES:
	            this.state = 334;
	            this._errHandler.sync(this);
	            switch(this._input.LA(1)) {
	            case RulepadGrammarParser.TYPES:
	                this.state = 331;
	                this.types();
	                break;
	            case RulepadGrammarParser.NAME:
	                this.state = 332;
	                this.names();
	                break;
	            case RulepadGrammarParser.VALUE:
	                this.state = 333;
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
	        this.state = 346;
	        this._errHandler.sync(this);
	        let _alt = this._interp.adaptivePredict(this._input,28,this._ctx)
	        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
	            if(_alt===1) {
	                if(this._parseListeners!==null) {
	                    this.triggerExitRuleEvent();
	                }
	                _prevctx = localctx;
	                this.state = 344;
	                this._errHandler.sync(this);
	                var la_ = this._interp.adaptivePredict(this._input,27,this._ctx);
	                switch(la_) {
	                case 1:
	                    localctx = new ParameterExpressionContext(this, _parentctx, _parentState);
	                    localctx.left = _prevctx;
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_parameterExpression);
	                    this.state = 338;
	                    if (!( this.precpred(this._ctx, 3))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 3)");
	                    }
	                    this.state = 339;
	                    localctx.op = this.binary();
	                    this.state = 340;
	                    localctx.right = this.parameterExpression(4);
	                    break;

	                case 2:
	                    localctx = new ParameterExpressionContext(this, _parentctx, _parentState);
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_parameterExpression);
	                    this.state = 342;
	                    if (!( this.precpred(this._ctx, 1))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 1)");
	                    }
	                    this.state = 343;
	                    this.match(RulepadGrammarParser.SPACE);
	                    break;

	                } 
	            }
	            this.state = 348;
	            this._errHandler.sync(this);
	            _alt = this._interp.adaptivePredict(this._input,28,this._ctx);
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
	        this.state = 349;
	        this.match(RulepadGrammarParser.PARAMETER);
	        this.state = 351;
	        this._errHandler.sync(this);
	        var la_ = this._interp.adaptivePredict(this._input,29,this._ctx);
	        if(la_===1) {
	            this.state = 350;
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
	        this.state = 359;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.T__0:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 353;
	            this.combinatorialWords();
	            this.state = 354;
	            this.match(RulepadGrammarParser.SPACE);
	            this.state = 356;
	            this._errHandler.sync(this);
	            var la_ = this._interp.adaptivePredict(this._input,30,this._ctx);
	            if(la_===1) {
	                this.state = 355;
	                this.functionParameterConditionTransition();

	            }
	            break;
	        case RulepadGrammarParser.T__15:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 358;
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
	        this.state = 361;
	        this.withWord();
	        this.state = 362;
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
	        this.state = 374;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.LPAREN:
	            this.state = 365;
	            this.match(RulepadGrammarParser.LPAREN);
	            this.state = 366;
	            this.functionParameterExpression(0);
	            this.state = 367;
	            this.match(RulepadGrammarParser.RPAREN);
	            break;
	        case RulepadGrammarParser.NAME:
	        case RulepadGrammarParser.ANNOTATION:
	        case RulepadGrammarParser.TYPES:
	            this.state = 372;
	            this._errHandler.sync(this);
	            switch(this._input.LA(1)) {
	            case RulepadGrammarParser.TYPES:
	                this.state = 369;
	                this.types();
	                break;
	            case RulepadGrammarParser.NAME:
	                this.state = 370;
	                this.names();
	                break;
	            case RulepadGrammarParser.ANNOTATION:
	                this.state = 371;
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
	        this.state = 384;
	        this._errHandler.sync(this);
	        let _alt = this._interp.adaptivePredict(this._input,35,this._ctx)
	        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
	            if(_alt===1) {
	                if(this._parseListeners!==null) {
	                    this.triggerExitRuleEvent();
	                }
	                _prevctx = localctx;
	                this.state = 382;
	                this._errHandler.sync(this);
	                var la_ = this._interp.adaptivePredict(this._input,34,this._ctx);
	                switch(la_) {
	                case 1:
	                    localctx = new FunctionParameterExpressionContext(this, _parentctx, _parentState);
	                    localctx.left = _prevctx;
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_functionParameterExpression);
	                    this.state = 376;
	                    if (!( this.precpred(this._ctx, 3))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 3)");
	                    }
	                    this.state = 377;
	                    localctx.op = this.binary();
	                    this.state = 378;
	                    localctx.right = this.functionParameterExpression(4);
	                    break;

	                case 2:
	                    localctx = new FunctionParameterExpressionContext(this, _parentctx, _parentState);
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_functionParameterExpression);
	                    this.state = 380;
	                    if (!( this.precpred(this._ctx, 1))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 1)");
	                    }
	                    this.state = 381;
	                    this.match(RulepadGrammarParser.SPACE);
	                    break;

	                } 
	            }
	            this.state = 386;
	            this._errHandler.sync(this);
	            _alt = this._interp.adaptivePredict(this._input,35,this._ctx);
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
	        this.state = 387;
	        this.match(RulepadGrammarParser.TYPES);
	        this.state = 388;
	        this.typeCondition();
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
	        this.enterOuterAlt(localctx, 1);
	        this.state = 390;
	        this.combinatorialWords();
	        this.state = 391;
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



	declarationStatements() {
	    let localctx = new DeclarationStatementsContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 84, RulepadGrammarParser.RULE_declarationStatements);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 393;
	        this.match(RulepadGrammarParser.DeclarationStatement);
	        this.state = 394;
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
	        this.state = 396;
	        this.withWord();
	        this.state = 397;
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
	        this.state = 409;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.LPAREN:
	            this.state = 400;
	            this.match(RulepadGrammarParser.LPAREN);
	            this.state = 401;
	            this.declarationStatementExpression(0);
	            this.state = 402;
	            this.match(RulepadGrammarParser.RPAREN);
	            break;
	        case RulepadGrammarParser.ANNOTATION:
	        case RulepadGrammarParser.TYPES:
	        case RulepadGrammarParser.ConfigurationFile:
	            this.state = 407;
	            this._errHandler.sync(this);
	            switch(this._input.LA(1)) {
	            case RulepadGrammarParser.ANNOTATION:
	                this.state = 404;
	                this.annotations();
	                break;
	            case RulepadGrammarParser.TYPES:
	                this.state = 405;
	                this.types();
	                break;
	            case RulepadGrammarParser.ConfigurationFile:
	                this.state = 406;
	                this.configurationFiles();
	                break;
	            default:
	                throw new antlr4.error.NoViableAltException(this);
	            }
	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	        this._ctx.stop = this._input.LT(-1);
	        this.state = 419;
	        this._errHandler.sync(this);
	        let _alt = this._interp.adaptivePredict(this._input,39,this._ctx)
	        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
	            if(_alt===1) {
	                if(this._parseListeners!==null) {
	                    this.triggerExitRuleEvent();
	                }
	                _prevctx = localctx;
	                this.state = 417;
	                this._errHandler.sync(this);
	                var la_ = this._interp.adaptivePredict(this._input,38,this._ctx);
	                switch(la_) {
	                case 1:
	                    localctx = new DeclarationStatementExpressionContext(this, _parentctx, _parentState);
	                    localctx.left = _prevctx;
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_declarationStatementExpression);
	                    this.state = 411;
	                    if (!( this.precpred(this._ctx, 3))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 3)");
	                    }
	                    this.state = 412;
	                    localctx.op = this.binary();
	                    this.state = 413;
	                    localctx.right = this.declarationStatementExpression(4);
	                    break;

	                case 2:
	                    localctx = new DeclarationStatementExpressionContext(this, _parentctx, _parentState);
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_declarationStatementExpression);
	                    this.state = 415;
	                    if (!( this.precpred(this._ctx, 1))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 1)");
	                    }
	                    this.state = 416;
	                    this.match(RulepadGrammarParser.SPACE);
	                    break;

	                } 
	            }
	            this.state = 421;
	            this._errHandler.sync(this);
	            _alt = this._interp.adaptivePredict(this._input,39,this._ctx);
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
	        this.state = 422;
	        this.match(RulepadGrammarParser.ConfigurationFile);
	        this.state = 423;
	        this.configurationFileCondition();
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
	        this.state = 425;
	        this.withWord();
	        this.state = 426;
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
	        this.state = 434;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.LPAREN:
	            this.state = 429;
	            this.match(RulepadGrammarParser.LPAREN);
	            this.state = 430;
	            this.configurationFileExpression(0);
	            this.state = 431;
	            this.match(RulepadGrammarParser.RPAREN);
	            break;
	        case RulepadGrammarParser.CONFIGURATION_PROPERTIES:
	            this.state = 433;
	            this.configurationProperties();
	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	        this._ctx.stop = this._input.LT(-1);
	        this.state = 444;
	        this._errHandler.sync(this);
	        let _alt = this._interp.adaptivePredict(this._input,42,this._ctx)
	        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
	            if(_alt===1) {
	                if(this._parseListeners!==null) {
	                    this.triggerExitRuleEvent();
	                }
	                _prevctx = localctx;
	                this.state = 442;
	                this._errHandler.sync(this);
	                var la_ = this._interp.adaptivePredict(this._input,41,this._ctx);
	                switch(la_) {
	                case 1:
	                    localctx = new ConfigurationFileExpressionContext(this, _parentctx, _parentState);
	                    localctx.left = _prevctx;
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_configurationFileExpression);
	                    this.state = 436;
	                    if (!( this.precpred(this._ctx, 3))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 3)");
	                    }
	                    this.state = 437;
	                    localctx.op = this.binary();
	                    this.state = 438;
	                    localctx.right = this.configurationFileExpression(4);
	                    break;

	                case 2:
	                    localctx = new ConfigurationFileExpressionContext(this, _parentctx, _parentState);
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_configurationFileExpression);
	                    this.state = 440;
	                    if (!( this.precpred(this._ctx, 1))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 1)");
	                    }
	                    this.state = 441;
	                    this.match(RulepadGrammarParser.SPACE);
	                    break;

	                } 
	            }
	            this.state = 446;
	            this._errHandler.sync(this);
	            _alt = this._interp.adaptivePredict(this._input,42,this._ctx);
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
	        this.state = 447;
	        this.match(RulepadGrammarParser.CONFIGURATION_PROPERTIES);
	        this.state = 448;
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
	        this.state = 456;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.T__0:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 450;
	            this.combinatorialWords();
	            this.state = 451;
	            this.match(RulepadGrammarParser.SPACE);
	            this.state = 453;
	            this._errHandler.sync(this);
	            var la_ = this._interp.adaptivePredict(this._input,43,this._ctx);
	            if(la_===1) {
	                this.state = 452;
	                this.configurationPropertyConditionTransition();

	            }
	            break;
	        case RulepadGrammarParser.T__15:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 455;
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
	    this.enterRule(localctx, 100, RulepadGrammarParser.RULE_configurationPropertyConditionTransition);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 458;
	        this.withWord();
	        this.state = 459;
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
	    const _startState = 102;
	    this.enterRecursionRule(localctx, 102, RulepadGrammarParser.RULE_configurationPropertyExpression, _p);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 471;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.LPAREN:
	            this.state = 462;
	            this.match(RulepadGrammarParser.LPAREN);
	            this.state = 463;
	            this.configurationPropertyExpression(0);
	            this.state = 464;
	            this.match(RulepadGrammarParser.RPAREN);
	            break;
	        case RulepadGrammarParser.NAME:
	        case RulepadGrammarParser.VALUE:
	        case RulepadGrammarParser.TYPES:
	            this.state = 469;
	            this._errHandler.sync(this);
	            switch(this._input.LA(1)) {
	            case RulepadGrammarParser.TYPES:
	                this.state = 466;
	                this.types();
	                break;
	            case RulepadGrammarParser.NAME:
	                this.state = 467;
	                this.names();
	                break;
	            case RulepadGrammarParser.VALUE:
	                this.state = 468;
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
	        this.state = 481;
	        this._errHandler.sync(this);
	        let _alt = this._interp.adaptivePredict(this._input,48,this._ctx)
	        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
	            if(_alt===1) {
	                if(this._parseListeners!==null) {
	                    this.triggerExitRuleEvent();
	                }
	                _prevctx = localctx;
	                this.state = 479;
	                this._errHandler.sync(this);
	                var la_ = this._interp.adaptivePredict(this._input,47,this._ctx);
	                switch(la_) {
	                case 1:
	                    localctx = new ConfigurationPropertyExpressionContext(this, _parentctx, _parentState);
	                    localctx.left = _prevctx;
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_configurationPropertyExpression);
	                    this.state = 473;
	                    if (!( this.precpred(this._ctx, 3))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 3)");
	                    }
	                    this.state = 474;
	                    localctx.op = this.binary();
	                    this.state = 475;
	                    localctx.right = this.configurationPropertyExpression(4);
	                    break;

	                case 2:
	                    localctx = new ConfigurationPropertyExpressionContext(this, _parentctx, _parentState);
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_configurationPropertyExpression);
	                    this.state = 477;
	                    if (!( this.precpred(this._ctx, 1))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 1)");
	                    }
	                    this.state = 478;
	                    this.match(RulepadGrammarParser.SPACE);
	                    break;

	                } 
	            }
	            this.state = 483;
	            this._errHandler.sync(this);
	            _alt = this._interp.adaptivePredict(this._input,48,this._ctx);
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
	    this.enterRule(localctx, 104, RulepadGrammarParser.RULE_classes);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 484;
	        this.match(RulepadGrammarParser.CLASSES);
	        this.state = 485;
	        this.classCondition();
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
	    this.enterRule(localctx, 106, RulepadGrammarParser.RULE_classCondition);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 487;
	        this.withWord();
	        this.state = 488;
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
	    const _startState = 108;
	    this.enterRecursionRule(localctx, 108, RulepadGrammarParser.RULE_classExpression, _p);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 505;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case RulepadGrammarParser.LPAREN:
	            this.state = 491;
	            this.match(RulepadGrammarParser.LPAREN);
	            this.state = 492;
	            this.classExpression(0);
	            this.state = 493;
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
	            this.state = 503;
	            this._errHandler.sync(this);
	            switch(this._input.LA(1)) {
	            case RulepadGrammarParser.ANNOTATION:
	                this.state = 495;
	                this.annotations();
	                break;
	            case RulepadGrammarParser.EXTENSION:
	                this.state = 496;
	                this.extensions();
	                break;
	            case RulepadGrammarParser.IMPLEMENTATION:
	                this.state = 497;
	                this.implementations();
	                break;
	            case RulepadGrammarParser.FUNCTION:
	                this.state = 498;
	                this.functions();
	                break;
	            case RulepadGrammarParser.CONSTRUCTOR:
	                this.state = 499;
	                this.constructors();
	                break;
	            case RulepadGrammarParser.DeclarationStatement:
	                this.state = 500;
	                this.declarationStatements();
	                break;
	            case RulepadGrammarParser.ConfigurationFile:
	                this.state = 501;
	                this.configurationFiles();
	                break;
	            case RulepadGrammarParser.BEAN_DECL:
	                this.state = 502;
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
	        this.state = 515;
	        this._errHandler.sync(this);
	        let _alt = this._interp.adaptivePredict(this._input,52,this._ctx)
	        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
	            if(_alt===1) {
	                if(this._parseListeners!==null) {
	                    this.triggerExitRuleEvent();
	                }
	                _prevctx = localctx;
	                this.state = 513;
	                this._errHandler.sync(this);
	                var la_ = this._interp.adaptivePredict(this._input,51,this._ctx);
	                switch(la_) {
	                case 1:
	                    localctx = new ClassExpressionContext(this, _parentctx, _parentState);
	                    localctx.left = _prevctx;
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_classExpression);
	                    this.state = 507;
	                    if (!( this.precpred(this._ctx, 3))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 3)");
	                    }
	                    this.state = 508;
	                    localctx.op = this.binary();
	                    this.state = 509;
	                    localctx.right = this.classExpression(4);
	                    break;

	                case 2:
	                    localctx = new ClassExpressionContext(this, _parentctx, _parentState);
	                    this.pushNewRecursionContext(localctx, _startState, RulepadGrammarParser.RULE_classExpression);
	                    this.state = 511;
	                    if (!( this.precpred(this._ctx, 1))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 1)");
	                    }
	                    this.state = 512;
	                    this.match(RulepadGrammarParser.SPACE);
	                    break;

	                } 
	            }
	            this.state = 517;
	            this._errHandler.sync(this);
	            _alt = this._interp.adaptivePredict(this._input,52,this._ctx);
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
	    this.enterRule(localctx, 110, RulepadGrammarParser.RULE_beans);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 518;
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
RulepadGrammarParser.SPACE = 17;
RulepadGrammarParser.Alphabet = 18;
RulepadGrammarParser.NL = 19;
RulepadGrammarParser.LPAREN = 20;
RulepadGrammarParser.RPAREN = 21;
RulepadGrammarParser.NAME = 22;
RulepadGrammarParser.VALUE = 23;
RulepadGrammarParser.ANNOTATION = 24;
RulepadGrammarParser.EXTENSION = 25;
RulepadGrammarParser.SUPERCLASS = 26;
RulepadGrammarParser.IMPLEMENTATION = 27;
RulepadGrammarParser.INTERFACE = 28;
RulepadGrammarParser.FUNCTION = 29;
RulepadGrammarParser.CONSTRUCTOR = 30;
RulepadGrammarParser.PARAMETER = 31;
RulepadGrammarParser.TYPES = 32;
RulepadGrammarParser.DeclarationStatement = 33;
RulepadGrammarParser.ConfigurationFile = 34;
RulepadGrammarParser.CONFIGURATION_PROPERTIES = 35;
RulepadGrammarParser.CLASSES = 36;
RulepadGrammarParser.BEAN_DECL = 37;

RulepadGrammarParser.RULE_inputSentence = 0;
RulepadGrammarParser.RULE_mustClause = 1;
RulepadGrammarParser.RULE_combinatorialWords = 2;
RulepadGrammarParser.RULE_symbols = 3;
RulepadGrammarParser.RULE_end = 4;
RulepadGrammarParser.RULE_emptyLine = 5;
RulepadGrammarParser.RULE_must = 6;
RulepadGrammarParser.RULE_of = 7;
RulepadGrammarParser.RULE_and_ = 8;
RulepadGrammarParser.RULE_or_ = 9;
RulepadGrammarParser.RULE_have = 10;
RulepadGrammarParser.RULE_withWord = 11;
RulepadGrammarParser.RULE_binary = 12;
RulepadGrammarParser.RULE_names = 13;
RulepadGrammarParser.RULE_nameCondition = 14;
RulepadGrammarParser.RULE_values = 15;
RulepadGrammarParser.RULE_valueCondition = 16;
RulepadGrammarParser.RULE_annotations = 17;
RulepadGrammarParser.RULE_annotationCondition = 18;
RulepadGrammarParser.RULE_annotationConditionTransition = 19;
RulepadGrammarParser.RULE_annotationExpression = 20;
RulepadGrammarParser.RULE_extensions = 21;
RulepadGrammarParser.RULE_extensionCondition = 22;
RulepadGrammarParser.RULE_implementations = 23;
RulepadGrammarParser.RULE_implementationCondition = 24;
RulepadGrammarParser.RULE_functions = 25;
RulepadGrammarParser.RULE_functionCondition = 26;
RulepadGrammarParser.RULE_functionExpression = 27;
RulepadGrammarParser.RULE_constructors = 28;
RulepadGrammarParser.RULE_constructorOf = 29;
RulepadGrammarParser.RULE_constructorCondition = 30;
RulepadGrammarParser.RULE_constructorExpression = 31;
RulepadGrammarParser.RULE_parameters = 32;
RulepadGrammarParser.RULE_parameterCondition = 33;
RulepadGrammarParser.RULE_parameterConditionTransition = 34;
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
RulepadGrammarParser.RULE_configurationPropertyConditionTransition = 50;
RulepadGrammarParser.RULE_configurationPropertyExpression = 51;
RulepadGrammarParser.RULE_classes = 52;
RulepadGrammarParser.RULE_classCondition = 53;
RulepadGrammarParser.RULE_classExpression = 54;
RulepadGrammarParser.RULE_beans = 55;

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

	combinatorialWords() {
	    return this.getTypedRuleContext(CombinatorialWordsContext,0);
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

	combinatorialWords() {
	    return this.getTypedRuleContext(CombinatorialWordsContext,0);
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

	configurationFiles() {
	    return this.getTypedRuleContext(ConfigurationFilesContext,0);
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

	configurationFiles() {
	    return this.getTypedRuleContext(ConfigurationFilesContext,0);
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
RulepadGrammarParser.CombinatorialWordsContext = CombinatorialWordsContext; 
RulepadGrammarParser.SymbolsContext = SymbolsContext; 
RulepadGrammarParser.EndContext = EndContext; 
RulepadGrammarParser.EmptyLineContext = EmptyLineContext; 
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
