// Generated from ../violation-detection/src/main/antlr4/ca/ualberta/grammar/RulepadGrammar.g4 by ANTLR 4.9
// jshint ignore: start
import antlr4 from 'antlr4';



const serializedATN = ["\u0003\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786",
    "\u5964\u0002)\u0178\b\u0001\u0004\u0002\t\u0002\u0004\u0003\t\u0003",
    "\u0004\u0004\t\u0004\u0004\u0005\t\u0005\u0004\u0006\t\u0006\u0004\u0007",
    "\t\u0007\u0004\b\t\b\u0004\t\t\t\u0004\n\t\n\u0004\u000b\t\u000b\u0004",
    "\f\t\f\u0004\r\t\r\u0004\u000e\t\u000e\u0004\u000f\t\u000f\u0004\u0010",
    "\t\u0010\u0004\u0011\t\u0011\u0004\u0012\t\u0012\u0004\u0013\t\u0013",
    "\u0004\u0014\t\u0014\u0004\u0015\t\u0015\u0004\u0016\t\u0016\u0004\u0017",
    "\t\u0017\u0004\u0018\t\u0018\u0004\u0019\t\u0019\u0004\u001a\t\u001a",
    "\u0004\u001b\t\u001b\u0004\u001c\t\u001c\u0004\u001d\t\u001d\u0004\u001e",
    "\t\u001e\u0004\u001f\t\u001f\u0004 \t \u0004!\t!\u0004\"\t\"\u0004#",
    "\t#\u0004$\t$\u0004%\t%\u0004&\t&\u0004\'\t\'\u0004(\t(\u0003\u0002",
    "\u0003\u0002\u0003\u0003\u0003\u0003\u0003\u0004\u0003\u0004\u0003\u0005",
    "\u0003\u0005\u0003\u0006\u0003\u0006\u0003\u0007\u0003\u0007\u0003\b",
    "\u0003\b\u0003\t\u0003\t\u0003\n\u0003\n\u0003\u000b\u0003\u000b\u0003",
    "\f\u0003\f\u0003\f\u0003\f\u0003\f\u0003\f\u0003\r\u0003\r\u0003\r\u0003",
    "\r\u0003\u000e\u0003\u000e\u0003\u000e\u0003\u000e\u0003\u000e\u0003",
    "\u000f\u0003\u000f\u0003\u000f\u0003\u000f\u0003\u0010\u0003\u0010\u0003",
    "\u0010\u0003\u0010\u0003\u0010\u0003\u0010\u0003\u0011\u0003\u0011\u0003",
    "\u0011\u0003\u0011\u0003\u0011\u0003\u0011\u0003\u0012\u0006\u0012\u0086",
    "\n\u0012\r\u0012\u000e\u0012\u0087\u0003\u0013\u0003\u0013\u0003\u0014",
    "\u0003\u0014\u0003\u0015\u0003\u0015\u0003\u0016\u0003\u0016\u0003\u0017",
    "\u0003\u0017\u0003\u0017\u0003\u0017\u0003\u0017\u0003\u0017\u0003\u0018",
    "\u0003\u0018\u0003\u0018\u0003\u0018\u0003\u0018\u0003\u0018\u0003\u0018",
    "\u0003\u0019\u0003\u0019\u0003\u0019\u0003\u0019\u0003\u0019\u0003\u0019",
    "\u0003\u0019\u0003\u0019\u0003\u0019\u0003\u0019\u0003\u0019\u0003\u0019",
    "\u0003\u001a\u0003\u001a\u0003\u001a\u0003\u001a\u0003\u001a\u0003\u001a",
    "\u0003\u001a\u0003\u001a\u0003\u001a\u0003\u001a\u0003\u001a\u0003\u001b",
    "\u0003\u001b\u0003\u001b\u0003\u001b\u0003\u001b\u0003\u001b\u0003\u001b",
    "\u0003\u001b\u0003\u001b\u0003\u001b\u0003\u001b\u0003\u001c\u0003\u001c",
    "\u0003\u001c\u0003\u001c\u0003\u001c\u0003\u001c\u0003\u001c\u0003\u001c",
    "\u0003\u001c\u0003\u001c\u0003\u001c\u0003\u001c\u0003\u001c\u0003\u001c",
    "\u0003\u001c\u0003\u001c\u0003\u001d\u0003\u001d\u0003\u001d\u0003\u001d",
    "\u0003\u001d\u0003\u001d\u0003\u001d\u0003\u001d\u0003\u001d\u0003\u001d",
    "\u0003\u001d\u0003\u001e\u0003\u001e\u0003\u001e\u0003\u001e\u0003\u001e",
    "\u0003\u001e\u0003\u001e\u0003\u001e\u0003\u001e\u0003\u001e\u0003\u001e",
    "\u0003\u001e\u0003\u001e\u0003\u001e\u0003\u001e\u0003\u001e\u0005\u001e",
    "\u00ec\n\u001e\u0003\u001f\u0003\u001f\u0003\u001f\u0003\u001f\u0003",
    "\u001f\u0003\u001f\u0003\u001f\u0003\u001f\u0003\u001f\u0003\u001f\u0003",
    "\u001f\u0003\u001f\u0003\u001f\u0003 \u0003 \u0003 \u0003 \u0003 \u0003",
    " \u0003 \u0003 \u0003 \u0003 \u0003 \u0003 \u0003 \u0003!\u0003!\u0003",
    "!\u0003!\u0003!\u0003!\u0003!\u0003!\u0003!\u0003!\u0003!\u0003\"\u0003",
    "\"\u0003\"\u0003\"\u0003\"\u0003\"\u0003#\u0003#\u0003#\u0003#\u0003",
    "#\u0003#\u0003#\u0003#\u0003#\u0003#\u0003#\u0003#\u0003#\u0003#\u0003",
    "#\u0003#\u0003#\u0003#\u0003#\u0003#\u0003#\u0003#\u0003#\u0003#\u0003",
    "#\u0003#\u0003#\u0003#\u0005#\u0135\n#\u0003$\u0003$\u0003$\u0003$\u0003",
    "$\u0003$\u0003$\u0003$\u0003$\u0003$\u0003$\u0003$\u0003$\u0003$\u0003",
    "$\u0003$\u0003$\u0003$\u0003$\u0003$\u0003%\u0003%\u0003%\u0003%\u0003",
    "%\u0003%\u0003%\u0003%\u0003%\u0003%\u0003&\u0003&\u0003&\u0003&\u0003",
    "&\u0003&\u0003&\u0003\'\u0003\'\u0003\'\u0003\'\u0003\'\u0003\'\u0003",
    "\'\u0003\'\u0003\'\u0003\'\u0003\'\u0003\'\u0003\'\u0003\'\u0003\'\u0003",
    "\'\u0003\'\u0003\'\u0003(\u0003(\u0003(\u0003(\u0003(\u0003(\u0003(",
    "\u0003(\u0003(\u0003(\u0003(\u0002\u0002)\u0003\u0003\u0005\u0004\u0007",
    "\u0005\t\u0006\u000b\u0007\r\b\u000f\t\u0011\n\u0013\u000b\u0015\f\u0017",
    "\r\u0019\u000e\u001b\u000f\u001d\u0010\u001f\u0011!\u0012#\u0013%\u0014",
    "\'\u0015)\u0016+\u0017-\u0018/\u00191\u001a3\u001b5\u001c7\u001d9\u001e",
    ";\u001f= ?!A\"C#E$G%I&K\'M(O)\u0003\u0002\u0005\u0004\u0002\u000b\u000b",
    "\"\"\u0007\u0002//2;C\\aac|\u0004\u0002\f\f\u000f\u000f\u0002\u017a",
    "\u0002\u0003\u0003\u0002\u0002\u0002\u0002\u0005\u0003\u0002\u0002\u0002",
    "\u0002\u0007\u0003\u0002\u0002\u0002\u0002\t\u0003\u0002\u0002\u0002",
    "\u0002\u000b\u0003\u0002\u0002\u0002\u0002\r\u0003\u0002\u0002\u0002",
    "\u0002\u000f\u0003\u0002\u0002\u0002\u0002\u0011\u0003\u0002\u0002\u0002",
    "\u0002\u0013\u0003\u0002\u0002\u0002\u0002\u0015\u0003\u0002\u0002\u0002",
    "\u0002\u0017\u0003\u0002\u0002\u0002\u0002\u0019\u0003\u0002\u0002\u0002",
    "\u0002\u001b\u0003\u0002\u0002\u0002\u0002\u001d\u0003\u0002\u0002\u0002",
    "\u0002\u001f\u0003\u0002\u0002\u0002\u0002!\u0003\u0002\u0002\u0002",
    "\u0002#\u0003\u0002\u0002\u0002\u0002%\u0003\u0002\u0002\u0002\u0002",
    "\'\u0003\u0002\u0002\u0002\u0002)\u0003\u0002\u0002\u0002\u0002+\u0003",
    "\u0002\u0002\u0002\u0002-\u0003\u0002\u0002\u0002\u0002/\u0003\u0002",
    "\u0002\u0002\u00021\u0003\u0002\u0002\u0002\u00023\u0003\u0002\u0002",
    "\u0002\u00025\u0003\u0002\u0002\u0002\u00027\u0003\u0002\u0002\u0002",
    "\u00029\u0003\u0002\u0002\u0002\u0002;\u0003\u0002\u0002\u0002\u0002",
    "=\u0003\u0002\u0002\u0002\u0002?\u0003\u0002\u0002\u0002\u0002A\u0003",
    "\u0002\u0002\u0002\u0002C\u0003\u0002\u0002\u0002\u0002E\u0003\u0002",
    "\u0002\u0002\u0002G\u0003\u0002\u0002\u0002\u0002I\u0003\u0002\u0002",
    "\u0002\u0002K\u0003\u0002\u0002\u0002\u0002M\u0003\u0002\u0002\u0002",
    "\u0002O\u0003\u0002\u0002\u0002\u0003Q\u0003\u0002\u0002\u0002\u0005",
    "S\u0003\u0002\u0002\u0002\u0007U\u0003\u0002\u0002\u0002\tW\u0003\u0002",
    "\u0002\u0002\u000bY\u0003\u0002\u0002\u0002\r[\u0003\u0002\u0002\u0002",
    "\u000f]\u0003\u0002\u0002\u0002\u0011_\u0003\u0002\u0002\u0002\u0013",
    "a\u0003\u0002\u0002\u0002\u0015c\u0003\u0002\u0002\u0002\u0017e\u0003",
    "\u0002\u0002\u0002\u0019k\u0003\u0002\u0002\u0002\u001bo\u0003\u0002",
    "\u0002\u0002\u001dt\u0003\u0002\u0002\u0002\u001fx\u0003\u0002\u0002",
    "\u0002!~\u0003\u0002\u0002\u0002#\u0085\u0003\u0002\u0002\u0002%\u0089",
    "\u0003\u0002\u0002\u0002\'\u008b\u0003\u0002\u0002\u0002)\u008d\u0003",
    "\u0002\u0002\u0002+\u008f\u0003\u0002\u0002\u0002-\u0091\u0003\u0002",
    "\u0002\u0002/\u0097\u0003\u0002\u0002\u00021\u009e\u0003\u0002\u0002",
    "\u00023\u00aa\u0003\u0002\u0002\u00025\u00b5\u0003\u0002\u0002\u0002",
    "7\u00c0\u0003\u0002\u0002\u00029\u00d0\u0003\u0002\u0002\u0002;\u00eb",
    "\u0003\u0002\u0002\u0002=\u00ed\u0003\u0002\u0002\u0002?\u00fa\u0003",
    "\u0002\u0002\u0002A\u0107\u0003\u0002\u0002\u0002C\u0112\u0003\u0002",
    "\u0002\u0002E\u0134\u0003\u0002\u0002\u0002G\u0136\u0003\u0002\u0002",
    "\u0002I\u014a\u0003\u0002\u0002\u0002K\u0154\u0003\u0002\u0002\u0002",
    "M\u015b\u0003\u0002\u0002\u0002O\u016d\u0003\u0002\u0002\u0002QR\u0007",
    "$\u0002\u0002R\u0004\u0003\u0002\u0002\u0002ST\u00070\u0002\u0002T\u0006",
    "\u0003\u0002\u0002\u0002UV\u0007?\u0002\u0002V\b\u0003\u0002\u0002\u0002",
    "WX\u0007@\u0002\u0002X\n\u0003\u0002\u0002\u0002YZ\u0007>\u0002\u0002",
    "Z\f\u0003\u0002\u0002\u0002[\\\u0007)\u0002\u0002\\\u000e\u0003\u0002",
    "\u0002\u0002]^\u0007(\u0002\u0002^\u0010\u0003\u0002\u0002\u0002_`\u0007",
    "~\u0002\u0002`\u0012\u0003\u0002\u0002\u0002ab\u0007]\u0002\u0002b\u0014",
    "\u0003\u0002\u0002\u0002cd\u0007_\u0002\u0002d\u0016\u0003\u0002\u0002",
    "\u0002ef\u0007o\u0002\u0002fg\u0007w\u0002\u0002gh\u0007u\u0002\u0002",
    "hi\u0007v\u0002\u0002ij\u0007\"\u0002\u0002j\u0018\u0003\u0002\u0002",
    "\u0002kl\u0007q\u0002\u0002lm\u0007h\u0002\u0002mn\u0007\"\u0002\u0002",
    "n\u001a\u0003\u0002\u0002\u0002op\u0007c\u0002\u0002pq\u0007p\u0002",
    "\u0002qr\u0007f\u0002\u0002rs\u0007\"\u0002\u0002s\u001c\u0003\u0002",
    "\u0002\u0002tu\u0007q\u0002\u0002uv\u0007t\u0002\u0002vw\u0007\"\u0002",
    "\u0002w\u001e\u0003\u0002\u0002\u0002xy\u0007j\u0002\u0002yz\u0007c",
    "\u0002\u0002z{\u0007x\u0002\u0002{|\u0007g\u0002\u0002|}\u0007\"\u0002",
    "\u0002} \u0003\u0002\u0002\u0002~\u007f\u0007y\u0002\u0002\u007f\u0080",
    "\u0007k\u0002\u0002\u0080\u0081\u0007v\u0002\u0002\u0081\u0082\u0007",
    "j\u0002\u0002\u0082\u0083\u0007\"\u0002\u0002\u0083\"\u0003\u0002\u0002",
    "\u0002\u0084\u0086\t\u0002\u0002\u0002\u0085\u0084\u0003\u0002\u0002",
    "\u0002\u0086\u0087\u0003\u0002\u0002\u0002\u0087\u0085\u0003\u0002\u0002",
    "\u0002\u0087\u0088\u0003\u0002\u0002\u0002\u0088$\u0003\u0002\u0002",
    "\u0002\u0089\u008a\t\u0003\u0002\u0002\u008a&\u0003\u0002\u0002\u0002",
    "\u008b\u008c\t\u0004\u0002\u0002\u008c(\u0003\u0002\u0002\u0002\u008d",
    "\u008e\u0007*\u0002\u0002\u008e*\u0003\u0002\u0002\u0002\u008f\u0090",
    "\u0007+\u0002\u0002\u0090,\u0003\u0002\u0002\u0002\u0091\u0092\u0007",
    "p\u0002\u0002\u0092\u0093\u0007c\u0002\u0002\u0093\u0094\u0007o\u0002",
    "\u0002\u0094\u0095\u0007g\u0002\u0002\u0095\u0096\u0007\"\u0002\u0002",
    "\u0096.\u0003\u0002\u0002\u0002\u0097\u0098\u0007x\u0002\u0002\u0098",
    "\u0099\u0007c\u0002\u0002\u0099\u009a\u0007n\u0002\u0002\u009a\u009b",
    "\u0007w\u0002\u0002\u009b\u009c\u0007g\u0002\u0002\u009c\u009d\u0007",
    "\"\u0002\u0002\u009d0\u0003\u0002\u0002\u0002\u009e\u009f\u0007c\u0002",
    "\u0002\u009f\u00a0\u0007p\u0002\u0002\u00a0\u00a1\u0007p\u0002\u0002",
    "\u00a1\u00a2\u0007q\u0002\u0002\u00a2\u00a3\u0007v\u0002\u0002\u00a3",
    "\u00a4\u0007c\u0002\u0002\u00a4\u00a5\u0007v\u0002\u0002\u00a5\u00a6",
    "\u0007k\u0002\u0002\u00a6\u00a7\u0007q\u0002\u0002\u00a7\u00a8\u0007",
    "p\u0002\u0002\u00a8\u00a9\u0007\"\u0002\u0002\u00a92\u0003\u0002\u0002",
    "\u0002\u00aa\u00ab\u0007g\u0002\u0002\u00ab\u00ac\u0007z\u0002\u0002",
    "\u00ac\u00ad\u0007v\u0002\u0002\u00ad\u00ae\u0007g\u0002\u0002\u00ae",
    "\u00af\u0007p\u0002\u0002\u00af\u00b0\u0007u\u0002\u0002\u00b0\u00b1",
    "\u0007k\u0002\u0002\u00b1\u00b2\u0007q\u0002\u0002\u00b2\u00b3\u0007",
    "p\u0002\u0002\u00b3\u00b4\u0007\"\u0002\u0002\u00b44\u0003\u0002\u0002",
    "\u0002\u00b5\u00b6\u0007U\u0002\u0002\u00b6\u00b7\u0007w\u0002\u0002",
    "\u00b7\u00b8\u0007r\u0002\u0002\u00b8\u00b9\u0007g\u0002\u0002\u00b9",
    "\u00ba\u0007t\u0002\u0002\u00ba\u00bb\u0007e\u0002\u0002\u00bb\u00bc",
    "\u0007n\u0002\u0002\u00bc\u00bd\u0007c\u0002\u0002\u00bd\u00be\u0007",
    "u\u0002\u0002\u00be\u00bf\u0007u\u0002\u0002\u00bf6\u0003\u0002\u0002",
    "\u0002\u00c0\u00c1\u0007k\u0002\u0002\u00c1\u00c2\u0007o\u0002\u0002",
    "\u00c2\u00c3\u0007r\u0002\u0002\u00c3\u00c4\u0007n\u0002\u0002\u00c4",
    "\u00c5\u0007g\u0002\u0002\u00c5\u00c6\u0007o\u0002\u0002\u00c6\u00c7",
    "\u0007g\u0002\u0002\u00c7\u00c8\u0007p\u0002\u0002\u00c8\u00c9\u0007",
    "v\u0002\u0002\u00c9\u00ca\u0007c\u0002\u0002\u00ca\u00cb\u0007v\u0002",
    "\u0002\u00cb\u00cc\u0007k\u0002\u0002\u00cc\u00cd\u0007q\u0002\u0002",
    "\u00cd\u00ce\u0007p\u0002\u0002\u00ce\u00cf\u0007\"\u0002\u0002\u00cf",
    "8\u0003\u0002\u0002\u0002\u00d0\u00d1\u0007K\u0002\u0002\u00d1\u00d2",
    "\u0007p\u0002\u0002\u00d2\u00d3\u0007v\u0002\u0002\u00d3\u00d4\u0007",
    "g\u0002\u0002\u00d4\u00d5\u0007t\u0002\u0002\u00d5\u00d6\u0007h\u0002",
    "\u0002\u00d6\u00d7\u0007c\u0002\u0002\u00d7\u00d8\u0007e\u0002\u0002",
    "\u00d8\u00d9\u0007g\u0002\u0002\u00d9\u00da\u0007\"\u0002\u0002\u00da",
    ":\u0003\u0002\u0002\u0002\u00db\u00dc\u0007h\u0002\u0002\u00dc\u00dd",
    "\u0007w\u0002\u0002\u00dd\u00de\u0007p\u0002\u0002\u00de\u00df\u0007",
    "e\u0002\u0002\u00df\u00e0\u0007v\u0002\u0002\u00e0\u00e1\u0007k\u0002",
    "\u0002\u00e1\u00e2\u0007q\u0002\u0002\u00e2\u00e3\u0007p\u0002\u0002",
    "\u00e3\u00ec\u0007\"\u0002\u0002\u00e4\u00e5\u0007o\u0002\u0002\u00e5",
    "\u00e6\u0007g\u0002\u0002\u00e6\u00e7\u0007v\u0002\u0002\u00e7\u00e8",
    "\u0007j\u0002\u0002\u00e8\u00e9\u0007q\u0002\u0002\u00e9\u00ea\u0007",
    "f\u0002\u0002\u00ea\u00ec\u0007\"\u0002\u0002\u00eb\u00db\u0003\u0002",
    "\u0002\u0002\u00eb\u00e4\u0003\u0002\u0002\u0002\u00ec<\u0003\u0002",
    "\u0002\u0002\u00ed\u00ee\u0007t\u0002\u0002\u00ee\u00ef\u0007g\u0002",
    "\u0002\u00ef\u00f0\u0007v\u0002\u0002\u00f0\u00f1\u0007w\u0002\u0002",
    "\u00f1\u00f2\u0007t\u0002\u0002\u00f2\u00f3\u0007p\u0002\u0002\u00f3",
    "\u00f4\u0007\"\u0002\u0002\u00f4\u00f5\u0007v\u0002\u0002\u00f5\u00f6",
    "\u0007{\u0002\u0002\u00f6\u00f7\u0007r\u0002\u0002\u00f7\u00f8\u0007",
    "g\u0002\u0002\u00f8\u00f9\u0007\"\u0002\u0002\u00f9>\u0003\u0002\u0002",
    "\u0002\u00fa\u00fb\u0007e\u0002\u0002\u00fb\u00fc\u0007q\u0002\u0002",
    "\u00fc\u00fd\u0007p\u0002\u0002\u00fd\u00fe\u0007u\u0002\u0002\u00fe",
    "\u00ff\u0007v\u0002\u0002\u00ff\u0100\u0007t\u0002\u0002\u0100\u0101",
    "\u0007w\u0002\u0002\u0101\u0102\u0007e\u0002\u0002\u0102\u0103\u0007",
    "v\u0002\u0002\u0103\u0104\u0007q\u0002\u0002\u0104\u0105\u0007t\u0002",
    "\u0002\u0105\u0106\u0007\"\u0002\u0002\u0106@\u0003\u0002\u0002\u0002",
    "\u0107\u0108\u0007r\u0002\u0002\u0108\u0109\u0007c\u0002\u0002\u0109",
    "\u010a\u0007t\u0002\u0002\u010a\u010b\u0007c\u0002\u0002\u010b\u010c",
    "\u0007o\u0002\u0002\u010c\u010d\u0007g\u0002\u0002\u010d\u010e\u0007",
    "v\u0002\u0002\u010e\u010f\u0007g\u0002\u0002\u010f\u0110\u0007t\u0002",
    "\u0002\u0110\u0111\u0007\"\u0002\u0002\u0111B\u0003\u0002\u0002\u0002",
    "\u0112\u0113\u0007v\u0002\u0002\u0113\u0114\u0007{\u0002\u0002\u0114",
    "\u0115\u0007r\u0002\u0002\u0115\u0116\u0007g\u0002\u0002\u0116\u0117",
    "\u0007\"\u0002\u0002\u0117D\u0003\u0002\u0002\u0002\u0118\u0119\u0007",
    "f\u0002\u0002\u0119\u011a\u0007g\u0002\u0002\u011a\u011b\u0007e\u0002",
    "\u0002\u011b\u011c\u0007n\u0002\u0002\u011c\u011d\u0007c\u0002\u0002",
    "\u011d\u011e\u0007t\u0002\u0002\u011e\u011f\u0007c\u0002\u0002\u011f",
    "\u0120\u0007v\u0002\u0002\u0120\u0121\u0007k\u0002\u0002\u0121\u0122",
    "\u0007q\u0002\u0002\u0122\u0123\u0007p\u0002\u0002\u0123\u0124\u0007",
    "\"\u0002\u0002\u0124\u0125\u0007u\u0002\u0002\u0125\u0126\u0007v\u0002",
    "\u0002\u0126\u0127\u0007c\u0002\u0002\u0127\u0128\u0007v\u0002\u0002",
    "\u0128\u0129\u0007g\u0002\u0002\u0129\u012a\u0007o\u0002\u0002\u012a",
    "\u012b\u0007g\u0002\u0002\u012b\u012c\u0007p\u0002\u0002\u012c\u012d",
    "\u0007v\u0002\u0002\u012d\u0135\u0007\"\u0002\u0002\u012e\u012f\u0007",
    "h\u0002\u0002\u012f\u0130\u0007k\u0002\u0002\u0130\u0131\u0007g\u0002",
    "\u0002\u0131\u0132\u0007n\u0002\u0002\u0132\u0133\u0007f\u0002\u0002",
    "\u0133\u0135\u0007\"\u0002\u0002\u0134\u0118\u0003\u0002\u0002\u0002",
    "\u0134\u012e\u0003\u0002\u0002\u0002\u0135F\u0003\u0002\u0002\u0002",
    "\u0136\u0137\u0007e\u0002\u0002\u0137\u0138\u0007q\u0002\u0002\u0138",
    "\u0139\u0007p\u0002\u0002\u0139\u013a\u0007h\u0002\u0002\u013a\u013b",
    "\u0007k\u0002\u0002\u013b\u013c\u0007i\u0002\u0002\u013c\u013d\u0007",
    "w\u0002\u0002\u013d\u013e\u0007t\u0002\u0002\u013e\u013f\u0007c\u0002",
    "\u0002\u013f\u0140\u0007v\u0002\u0002\u0140\u0141\u0007k\u0002\u0002",
    "\u0141\u0142\u0007q\u0002\u0002\u0142\u0143\u0007p\u0002\u0002\u0143",
    "\u0144\u0007\"\u0002\u0002\u0144\u0145\u0007h\u0002\u0002\u0145\u0146",
    "\u0007k\u0002\u0002\u0146\u0147\u0007n\u0002\u0002\u0147\u0148\u0007",
    "g\u0002\u0002\u0148\u0149\u0007\"\u0002\u0002\u0149H\u0003\u0002\u0002",
    "\u0002\u014a\u014b\u0007r\u0002\u0002\u014b\u014c\u0007t\u0002\u0002",
    "\u014c\u014d\u0007q\u0002\u0002\u014d\u014e\u0007r\u0002\u0002\u014e",
    "\u014f\u0007g\u0002\u0002\u014f\u0150\u0007t\u0002\u0002\u0150\u0151",
    "\u0007v\u0002\u0002\u0151\u0152\u0007{\u0002\u0002\u0152\u0153\u0007",
    "\"\u0002\u0002\u0153J\u0003\u0002\u0002\u0002\u0154\u0155\u0007e\u0002",
    "\u0002\u0155\u0156\u0007n\u0002\u0002\u0156\u0157\u0007c\u0002\u0002",
    "\u0157\u0158\u0007u\u0002\u0002\u0158\u0159\u0007u\u0002\u0002\u0159",
    "\u015a\u0007\"\u0002\u0002\u015aL\u0003\u0002\u0002\u0002\u015b\u015c",
    "\u0007d\u0002\u0002\u015c\u015d\u0007g\u0002\u0002\u015d\u015e\u0007",
    "c\u0002\u0002\u015e\u015f\u0007p\u0002\u0002\u015f\u0160\u0007\"\u0002",
    "\u0002\u0160\u0161\u0007f\u0002\u0002\u0161\u0162\u0007g\u0002\u0002",
    "\u0162\u0163\u0007e\u0002\u0002\u0163\u0164\u0007n\u0002\u0002\u0164",
    "\u0165\u0007c\u0002\u0002\u0165\u0166\u0007t\u0002\u0002\u0166\u0167",
    "\u0007c\u0002\u0002\u0167\u0168\u0007v\u0002\u0002\u0168\u0169\u0007",
    "k\u0002\u0002\u0169\u016a\u0007q\u0002\u0002\u016a\u016b\u0007p\u0002",
    "\u0002\u016b\u016c\u0007\"\u0002\u0002\u016cN\u0003\u0002\u0002\u0002",
    "\u016d\u016e\u0007d\u0002\u0002\u016e\u016f\u0007g\u0002\u0002\u016f",
    "\u0170\u0007c\u0002\u0002\u0170\u0171\u0007p\u0002\u0002\u0171\u0172",
    "\u0007u\u0002\u0002\u0172\u0173\u0007\"\u0002\u0002\u0173\u0174\u0007",
    "h\u0002\u0002\u0174\u0175\u0007k\u0002\u0002\u0175\u0176\u0007n\u0002",
    "\u0002\u0176\u0177\u0007g\u0002\u0002\u0177P\u0003\u0002\u0002\u0002",
    "\u0006\u0002\u0087\u00eb\u0134\u0002"].join("");


const atn = new antlr4.atn.ATNDeserializer().deserialize(serializedATN);

const decisionsToDFA = atn.decisionToState.map( (ds, index) => new antlr4.dfa.DFA(ds, index) );

export default class RulepadGrammarLexer extends antlr4.Lexer {

    static grammarFileName = "RulepadGrammar.g4";
    static channelNames = [ "DEFAULT_TOKEN_CHANNEL", "HIDDEN" ];
	static modeNames = [ "DEFAULT_MODE" ];
	static literalNames = [ null, "'\"'", "'.'", "'='", "'>'", "'<'", "'''", 
                         "'&'", "'|'", "'['", "']'", "'must '", "'of '", 
                         "'and '", "'or '", "'have '", "'with '", null, 
                         null, null, "'('", "')'", "'name '", "'value '", 
                         "'annotation '", "'extension '", "'Superclass'", 
                         "'implementation '", "'Interface '", null, "'return type '", 
                         "'constructor '", "'parameter '", "'type '", null, 
                         "'configuration file '", "'property '", "'class '", 
                         "'bean declaration '", "'beans file'" ];
	static symbolicNames = [ null, null, null, null, null, null, null, null, 
                          null, null, null, null, null, null, null, null, 
                          null, "SPACE", "Alphabet", "NL", "LPAREN", "RPAREN", 
                          "NAME", "VALUE", "ANNOTATION", "EXTENSION", "SUPERCLASS", 
                          "IMPLEMENTATION", "INTERFACE", "FUNCTION", "RETURN_TYPES", 
                          "CONSTRUCTOR", "PARAMETER", "TYPES", "DeclarationStatement", 
                          "ConfigurationFile", "CONFIGURATION_PROPERTIES", 
                          "CLASSES", "BEAN_DECL", "BEANS_FILE" ];
	static ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                      "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", 
                      "T__13", "T__14", "T__15", "SPACE", "Alphabet", "NL", 
                      "LPAREN", "RPAREN", "NAME", "VALUE", "ANNOTATION", 
                      "EXTENSION", "SUPERCLASS", "IMPLEMENTATION", "INTERFACE", 
                      "FUNCTION", "RETURN_TYPES", "CONSTRUCTOR", "PARAMETER", 
                      "TYPES", "DeclarationStatement", "ConfigurationFile", 
                      "CONFIGURATION_PROPERTIES", "CLASSES", "BEAN_DECL", 
                      "BEANS_FILE" ];

    constructor(input) {
        super(input)
        this._interp = new antlr4.atn.LexerATNSimulator(this, atn, decisionsToDFA, new antlr4.PredictionContextCache());
    }

    get atn() {
        return atn;
    }
}

RulepadGrammarLexer.EOF = antlr4.Token.EOF;
RulepadGrammarLexer.T__0 = 1;
RulepadGrammarLexer.T__1 = 2;
RulepadGrammarLexer.T__2 = 3;
RulepadGrammarLexer.T__3 = 4;
RulepadGrammarLexer.T__4 = 5;
RulepadGrammarLexer.T__5 = 6;
RulepadGrammarLexer.T__6 = 7;
RulepadGrammarLexer.T__7 = 8;
RulepadGrammarLexer.T__8 = 9;
RulepadGrammarLexer.T__9 = 10;
RulepadGrammarLexer.T__10 = 11;
RulepadGrammarLexer.T__11 = 12;
RulepadGrammarLexer.T__12 = 13;
RulepadGrammarLexer.T__13 = 14;
RulepadGrammarLexer.T__14 = 15;
RulepadGrammarLexer.T__15 = 16;
RulepadGrammarLexer.SPACE = 17;
RulepadGrammarLexer.Alphabet = 18;
RulepadGrammarLexer.NL = 19;
RulepadGrammarLexer.LPAREN = 20;
RulepadGrammarLexer.RPAREN = 21;
RulepadGrammarLexer.NAME = 22;
RulepadGrammarLexer.VALUE = 23;
RulepadGrammarLexer.ANNOTATION = 24;
RulepadGrammarLexer.EXTENSION = 25;
RulepadGrammarLexer.SUPERCLASS = 26;
RulepadGrammarLexer.IMPLEMENTATION = 27;
RulepadGrammarLexer.INTERFACE = 28;
RulepadGrammarLexer.FUNCTION = 29;
RulepadGrammarLexer.RETURN_TYPES = 30;
RulepadGrammarLexer.CONSTRUCTOR = 31;
RulepadGrammarLexer.PARAMETER = 32;
RulepadGrammarLexer.TYPES = 33;
RulepadGrammarLexer.DeclarationStatement = 34;
RulepadGrammarLexer.ConfigurationFile = 35;
RulepadGrammarLexer.CONFIGURATION_PROPERTIES = 36;
RulepadGrammarLexer.CLASSES = 37;
RulepadGrammarLexer.BEAN_DECL = 38;
RulepadGrammarLexer.BEANS_FILE = 39;



