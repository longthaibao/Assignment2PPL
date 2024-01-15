# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\66")
        buf.write("\u0183\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3f\n\3\3\4\3\4\5\4")
        buf.write("j\n\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\5\bz\n\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n")
        buf.write("\5\n\u0085\n\n\3\13\3\13\3\13\3\13\3\13\5\13\u008c\n\13")
        buf.write("\3\f\3\f\3\f\3\f\5\f\u0092\n\f\3\r\3\r\3\r\3\r\5\r\u0098")
        buf.write("\n\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\5\17")
        buf.write("\u00a3\n\17\3\20\3\20\3\20\5\20\u00a8\n\20\3\21\3\21\3")
        buf.write("\22\3\22\3\22\3\22\5\22\u00b0\n\22\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\5\24\u00b8\n\24\3\25\3\25\3\25\3\25\3\25\5")
        buf.write("\25\u00bf\n\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26")
        buf.write("\u00c8\n\26\3\27\3\27\5\27\u00cc\n\27\3\30\3\30\5\30\u00d0")
        buf.write("\n\30\3\31\3\31\5\31\u00d4\n\31\3\31\3\31\3\31\3\31\5")
        buf.write("\31\u00da\n\31\5\31\u00dc\n\31\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\5\32\u00e6\n\32\3\33\3\33\3\33\3\33\5")
        buf.write("\33\u00ec\n\33\3\33\3\33\5\33\u00f0\n\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\34\3\34\7\34\u00fa\n\34\f\34\16\34\u00fd")
        buf.write("\13\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3")
        buf.write("\35\3\35\7\35\u010a\n\35\f\35\16\35\u010d\13\35\3\35\3")
        buf.write("\35\5\35\u0111\n\35\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3")
        buf.write("!\3!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\5#\u0125\n#\3$\3$\3$")
        buf.write("\3$\3$\5$\u012c\n$\3%\3%\3%\3%\3%\5%\u0133\n%\3&\3&\3")
        buf.write("&\3&\3&\5&\u013a\n&\3\'\3\'\3\'\3\'\3\'\3\'\7\'\u0142")
        buf.write("\n\'\f\'\16\'\u0145\13\'\3(\3(\3(\3(\3(\3(\7(\u014d\n")
        buf.write("(\f(\16(\u0150\13(\3)\3)\3)\3)\3)\3)\7)\u0158\n)\f)\16")
        buf.write(")\u015b\13)\3*\3*\3*\5*\u0160\n*\3+\3+\3+\5+\u0165\n+")
        buf.write("\3,\3,\3,\3,\3,\3,\5,\u016d\n,\3-\3-\3-\3-\3-\3-\5-\u0175")
        buf.write("\n-\3.\3.\3.\3.\3.\3.\5.\u017d\n.\3/\3/\3/\3/\3/\2\5L")
        buf.write("NP\60\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.")
        buf.write("\60\62\64\668:<>@BDFHJLNPRTVXZ\\\2\b\5\2\f\f\21\21\25")
        buf.write("\25\4\2\b\b\r\r\4\2\36\36 %\4\2\13\13\20\20\3\2\31\32")
        buf.write("\3\2\33\35\2\u0184\2^\3\2\2\2\4e\3\2\2\2\6i\3\2\2\2\b")
        buf.write("k\3\2\2\2\nm\3\2\2\2\fo\3\2\2\2\16y\3\2\2\2\20{\3\2\2")
        buf.write("\2\22\u0084\3\2\2\2\24\u008b\3\2\2\2\26\u0091\3\2\2\2")
        buf.write("\30\u0093\3\2\2\2\32\u0099\3\2\2\2\34\u009e\3\2\2\2\36")
        buf.write("\u00a4\3\2\2\2 \u00a9\3\2\2\2\"\u00ab\3\2\2\2$\u00b1\3")
        buf.write("\2\2\2&\u00b7\3\2\2\2(\u00be\3\2\2\2*\u00c0\3\2\2\2,\u00cb")
        buf.write("\3\2\2\2.\u00cf\3\2\2\2\60\u00db\3\2\2\2\62\u00e5\3\2")
        buf.write("\2\2\64\u00e7\3\2\2\2\66\u00f7\3\2\2\28\u0101\3\2\2\2")
        buf.write(":\u0112\3\2\2\2<\u0114\3\2\2\2>\u0116\3\2\2\2@\u0119\3")
        buf.write("\2\2\2B\u011e\3\2\2\2D\u0124\3\2\2\2F\u012b\3\2\2\2H\u0132")
        buf.write("\3\2\2\2J\u0139\3\2\2\2L\u013b\3\2\2\2N\u0146\3\2\2\2")
        buf.write("P\u0151\3\2\2\2R\u015f\3\2\2\2T\u0164\3\2\2\2V\u016c\3")
        buf.write("\2\2\2X\u0174\3\2\2\2Z\u017c\3\2\2\2\\\u017e\3\2\2\2^")
        buf.write("_\5\4\3\2_`\7\2\2\3`\3\3\2\2\2ab\5\6\4\2bc\5\4\3\2cf\3")
        buf.write("\2\2\2df\5\6\4\2ea\3\2\2\2ed\3\2\2\2f\5\3\2\2\2gj\5\26")
        buf.write("\f\2hj\5\"\22\2ig\3\2\2\2ih\3\2\2\2j\7\3\2\2\2kl\t\2\2")
        buf.write("\2l\t\3\2\2\2mn\t\3\2\2n\13\3\2\2\2op\5\b\5\2pq\7\62\2")
        buf.write("\2qr\7)\2\2rs\5\16\b\2st\7*\2\2t\r\3\2\2\2uv\7.\2\2vw")
        buf.write("\7+\2\2wz\5\16\b\2xz\7.\2\2yu\3\2\2\2yx\3\2\2\2z\17\3")
        buf.write("\2\2\2{|\7)\2\2|}\5F$\2}~\7*\2\2~\21\3\2\2\2\177\u0080")
        buf.write("\5\20\t\2\u0080\u0081\7+\2\2\u0081\u0082\5\22\n\2\u0082")
        buf.write("\u0085\3\2\2\2\u0083\u0085\5\20\t\2\u0084\177\3\2\2\2")
        buf.write("\u0084\u0083\3\2\2\2\u0085\23\3\2\2\2\u0086\u0087\7)\2")
        buf.write("\2\u0087\u0088\5\22\n\2\u0088\u0089\7*\2\2\u0089\u008c")
        buf.write("\3\2\2\2\u008a\u008c\5\20\t\2\u008b\u0086\3\2\2\2\u008b")
        buf.write("\u008a\3\2\2\2\u008c\25\3\2\2\2\u008d\u0092\5\30\r\2\u008e")
        buf.write("\u0092\5\32\16\2\u008f\u0092\5\34\17\2\u0090\u0092\5\36")
        buf.write("\20\2\u0091\u008d\3\2\2\2\u0091\u008e\3\2\2\2\u0091\u008f")
        buf.write("\3\2\2\2\u0091\u0090\3\2\2\2\u0092\27\3\2\2\2\u0093\u0094")
        buf.write("\5\b\5\2\u0094\u0097\7\62\2\2\u0095\u0096\7\37\2\2\u0096")
        buf.write("\u0098\5 \21\2\u0097\u0095\3\2\2\2\u0097\u0098\3\2\2\2")
        buf.write("\u0098\31\3\2\2\2\u0099\u009a\7\b\2\2\u009a\u009b\7\62")
        buf.write("\2\2\u009b\u009c\7\37\2\2\u009c\u009d\5 \21\2\u009d\33")
        buf.write("\3\2\2\2\u009e\u009f\7\r\2\2\u009f\u00a2\7\62\2\2\u00a0")
        buf.write("\u00a1\7\37\2\2\u00a1\u00a3\5 \21\2\u00a2\u00a0\3\2\2")
        buf.write("\2\u00a2\u00a3\3\2\2\2\u00a3\35\3\2\2\2\u00a4\u00a7\5")
        buf.write("\f\7\2\u00a5\u00a6\7\37\2\2\u00a6\u00a8\5\24\13\2\u00a7")
        buf.write("\u00a5\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\37\3\2\2\2\u00a9")
        buf.write("\u00aa\5D#\2\u00aa!\3\2\2\2\u00ab\u00ac\7\22\2\2\u00ac")
        buf.write("\u00ad\7\62\2\2\u00ad\u00af\5$\23\2\u00ae\u00b0\5,\27")
        buf.write("\2\u00af\u00ae\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0#\3\2")
        buf.write("\2\2\u00b1\u00b2\7\'\2\2\u00b2\u00b3\5&\24\2\u00b3\u00b4")
        buf.write("\7(\2\2\u00b4%\3\2\2\2\u00b5\u00b8\5(\25\2\u00b6\u00b8")
        buf.write("\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b7\u00b6\3\2\2\2\u00b8")
        buf.write("\'\3\2\2\2\u00b9\u00ba\5*\26\2\u00ba\u00bb\7+\2\2\u00bb")
        buf.write("\u00bc\5(\25\2\u00bc\u00bf\3\2\2\2\u00bd\u00bf\5*\26\2")
        buf.write("\u00be\u00b9\3\2\2\2\u00be\u00bd\3\2\2\2\u00bf)\3\2\2")
        buf.write("\2\u00c0\u00c7\5\b\5\2\u00c1\u00c8\7\62\2\2\u00c2\u00c3")
        buf.write("\7\62\2\2\u00c3\u00c4\7)\2\2\u00c4\u00c5\5F$\2\u00c5\u00c6")
        buf.write("\7*\2\2\u00c6\u00c8\3\2\2\2\u00c7\u00c1\3\2\2\2\u00c7")
        buf.write("\u00c2\3\2\2\2\u00c8+\3\2\2\2\u00c9\u00cc\5> \2\u00ca")
        buf.write("\u00cc\5B\"\2\u00cb\u00c9\3\2\2\2\u00cb\u00ca\3\2\2\2")
        buf.write("\u00cc-\3\2\2\2\u00cd\u00d0\5\60\31\2\u00ce\u00d0\3\2")
        buf.write("\2\2\u00cf\u00cd\3\2\2\2\u00cf\u00ce\3\2\2\2\u00d0/\3")
        buf.write("\2\2\2\u00d1\u00d4\5\62\32\2\u00d2\u00d4\5\26\f\2\u00d3")
        buf.write("\u00d1\3\2\2\2\u00d3\u00d2\3\2\2\2\u00d4\u00d5\3\2\2\2")
        buf.write("\u00d5\u00d6\5\60\31\2\u00d6\u00dc\3\2\2\2\u00d7\u00da")
        buf.write("\5\62\32\2\u00d8\u00da\5\26\f\2\u00d9\u00d7\3\2\2\2\u00d9")
        buf.write("\u00d8\3\2\2\2\u00da\u00dc\3\2\2\2\u00db\u00d3\3\2\2\2")
        buf.write("\u00db\u00d9\3\2\2\2\u00dc\61\3\2\2\2\u00dd\u00e6\5\66")
        buf.write("\34\2\u00de\u00e6\5\64\33\2\u00df\u00e6\58\35\2\u00e0")
        buf.write("\u00e6\5:\36\2\u00e1\u00e6\5<\37\2\u00e2\u00e6\5> \2\u00e3")
        buf.write("\u00e6\5@!\2\u00e4\u00e6\5B\"\2\u00e5\u00dd\3\2\2\2\u00e5")
        buf.write("\u00de\3\2\2\2\u00e5\u00df\3\2\2\2\u00e5\u00e0\3\2\2\2")
        buf.write("\u00e5\u00e1\3\2\2\2\u00e5\u00e2\3\2\2\2\u00e5\u00e3\3")
        buf.write("\2\2\2\u00e5\u00e4\3\2\2\2\u00e6\63\3\2\2\2\u00e7\u00e8")
        buf.write("\7\5\2\2\u00e8\u00eb\7\62\2\2\u00e9\u00ec\5F$\2\u00ea")
        buf.write("\u00ec\3\2\2\2\u00eb\u00e9\3\2\2\2\u00eb\u00ea\3\2\2\2")
        buf.write("\u00ec\u00ef\3\2\2\2\u00ed\u00ee\7\37\2\2\u00ee\u00f0")
        buf.write("\5F$\2\u00ef\u00ed\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0\u00f1")
        buf.write("\3\2\2\2\u00f1\u00f2\7\t\2\2\u00f2\u00f3\5F$\2\u00f3\u00f4")
        buf.write("\7\16\2\2\u00f4\u00f5\5F$\2\u00f5\u00f6\5\60\31\2\u00f6")
        buf.write("\65\3\2\2\2\u00f7\u00fb\7\62\2\2\u00f8\u00fa\5F$\2\u00f9")
        buf.write("\u00f8\3\2\2\2\u00fa\u00fd\3\2\2\2\u00fb\u00f9\3\2\2\2")
        buf.write("\u00fb\u00fc\3\2\2\2\u00fc\u00fe\3\2\2\2\u00fd\u00fb\3")
        buf.write("\2\2\2\u00fe\u00ff\7\37\2\2\u00ff\u0100\5F$\2\u0100\67")
        buf.write("\3\2\2\2\u0101\u0102\7\6\2\2\u0102\u0103\5H%\2\u0103\u0104")
        buf.write("\5\62\32\2\u0104\u010b\3\2\2\2\u0105\u0106\7\17\2\2\u0106")
        buf.write("\u0107\5H%\2\u0107\u0108\5\62\32\2\u0108\u010a\3\2\2\2")
        buf.write("\u0109\u0105\3\2\2\2\u010a\u010d\3\2\2\2\u010b\u0109\3")
        buf.write("\2\2\2\u010b\u010c\3\2\2\2\u010c\u0110\3\2\2\2\u010d\u010b")
        buf.write("\3\2\2\2\u010e\u010f\7\n\2\2\u010f\u0111\5\62\32\2\u0110")
        buf.write("\u010e\3\2\2\2\u0110\u0111\3\2\2\2\u01119\3\2\2\2\u0112")
        buf.write("\u0113\7\23\2\2\u0113;\3\2\2\2\u0114\u0115\7\26\2\2\u0115")
        buf.write("=\3\2\2\2\u0116\u0117\7\4\2\2\u0117\u0118\5D#\2\u0118")
        buf.write("?\3\2\2\2\u0119\u011a\7\62\2\2\u011a\u011b\7\'\2\2\u011b")
        buf.write("\u011c\5D#\2\u011c\u011d\7(\2\2\u011dA\3\2\2\2\u011e\u011f")
        buf.write("\7\24\2\2\u011f\u0120\5.\30\2\u0120\u0121\7\27\2\2\u0121")
        buf.write("C\3\2\2\2\u0122\u0125\5F$\2\u0123\u0125\3\2\2\2\u0124")
        buf.write("\u0122\3\2\2\2\u0124\u0123\3\2\2\2\u0125E\3\2\2\2\u0126")
        buf.write("\u0127\5H%\2\u0127\u0128\7+\2\2\u0128\u0129\5F$\2\u0129")
        buf.write("\u012c\3\2\2\2\u012a\u012c\5H%\2\u012b\u0126\3\2\2\2\u012b")
        buf.write("\u012a\3\2\2\2\u012cG\3\2\2\2\u012d\u012e\5J&\2\u012e")
        buf.write("\u012f\7&\2\2\u012f\u0130\5J&\2\u0130\u0133\3\2\2\2\u0131")
        buf.write("\u0133\5J&\2\u0132\u012d\3\2\2\2\u0132\u0131\3\2\2\2\u0133")
        buf.write("I\3\2\2\2\u0134\u0135\5L\'\2\u0135\u0136\t\4\2\2\u0136")
        buf.write("\u0137\5L\'\2\u0137\u013a\3\2\2\2\u0138\u013a\5L\'\2\u0139")
        buf.write("\u0134\3\2\2\2\u0139\u0138\3\2\2\2\u013aK\3\2\2\2\u013b")
        buf.write("\u013c\b\'\1\2\u013c\u013d\5N(\2\u013d\u0143\3\2\2\2\u013e")
        buf.write("\u013f\f\4\2\2\u013f\u0140\t\5\2\2\u0140\u0142\5N(\2\u0141")
        buf.write("\u013e\3\2\2\2\u0142\u0145\3\2\2\2\u0143\u0141\3\2\2\2")
        buf.write("\u0143\u0144\3\2\2\2\u0144M\3\2\2\2\u0145\u0143\3\2\2")
        buf.write("\2\u0146\u0147\b(\1\2\u0147\u0148\5P)\2\u0148\u014e\3")
        buf.write("\2\2\2\u0149\u014a\f\4\2\2\u014a\u014b\t\6\2\2\u014b\u014d")
        buf.write("\5P)\2\u014c\u0149\3\2\2\2\u014d\u0150\3\2\2\2\u014e\u014c")
        buf.write("\3\2\2\2\u014e\u014f\3\2\2\2\u014fO\3\2\2\2\u0150\u014e")
        buf.write("\3\2\2\2\u0151\u0152\b)\1\2\u0152\u0153\5R*\2\u0153\u0159")
        buf.write("\3\2\2\2\u0154\u0155\f\4\2\2\u0155\u0156\t\7\2\2\u0156")
        buf.write("\u0158\5R*\2\u0157\u0154\3\2\2\2\u0158\u015b\3\2\2\2\u0159")
        buf.write("\u0157\3\2\2\2\u0159\u015a\3\2\2\2\u015aQ\3\2\2\2\u015b")
        buf.write("\u0159\3\2\2\2\u015c\u015d\7\7\2\2\u015d\u0160\5R*\2\u015e")
        buf.write("\u0160\5T+\2\u015f\u015c\3\2\2\2\u015f\u015e\3\2\2\2\u0160")
        buf.write("S\3\2\2\2\u0161\u0162\7\32\2\2\u0162\u0165\5T+\2\u0163")
        buf.write("\u0165\5V,\2\u0164\u0161\3\2\2\2\u0164\u0163\3\2\2\2\u0165")
        buf.write("U\3\2\2\2\u0166\u0167\7\62\2\2\u0167\u0168\7)\2\2\u0168")
        buf.write("\u0169\5F$\2\u0169\u016a\7*\2\2\u016a\u016d\3\2\2\2\u016b")
        buf.write("\u016d\5X-\2\u016c\u0166\3\2\2\2\u016c\u016b\3\2\2\2\u016d")
        buf.write("W\3\2\2\2\u016e\u016f\7\62\2\2\u016f\u0170\7\'\2\2\u0170")
        buf.write("\u0171\5D#\2\u0171\u0172\7(\2\2\u0172\u0175\3\2\2\2\u0173")
        buf.write("\u0175\5Z.\2\u0174\u016e\3\2\2\2\u0174\u0173\3\2\2\2\u0175")
        buf.write("Y\3\2\2\2\u0176\u017d\7.\2\2\u0177\u017d\7\60\2\2\u0178")
        buf.write("\u017d\7/\2\2\u0179\u017d\5\20\t\2\u017a\u017d\7\62\2")
        buf.write("\2\u017b\u017d\5\\/\2\u017c\u0176\3\2\2\2\u017c\u0177")
        buf.write("\3\2\2\2\u017c\u0178\3\2\2\2\u017c\u0179\3\2\2\2\u017c")
        buf.write("\u017a\3\2\2\2\u017c\u017b\3\2\2\2\u017d[\3\2\2\2\u017e")
        buf.write("\u017f\7\'\2\2\u017f\u0180\5H%\2\u0180\u0181\7(\2\2\u0181")
        buf.write("]\3\2\2\2&eiy\u0084\u008b\u0091\u0097\u00a2\u00a7\u00af")
        buf.write("\u00b7\u00be\u00c7\u00cb\u00cf\u00d3\u00d9\u00db\u00e5")
        buf.write("\u00eb\u00ef\u00fb\u010b\u0110\u0124\u012b\u0132\u0139")
        buf.write("\u0143\u014e\u0159\u015f\u0164\u016c\u0174\u017c")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'return'", "'for'", "'if'", 
                     "'NOT'", "'var'", "'until'", "'else'", "'and'", "'number'", 
                     "'dynamic'", "'by'", "'elif'", "'or'", "'bool'", "'func'", 
                     "'break'", "'begin'", "'string'", "'continue'", "'end'", 
                     "'array'", "'+'", "'-'", "'*'", "'/'", "'%'", "'='", 
                     "'<-'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", 
                     "'...'", "'('", "')'", "'['", "']'", "','", "':'", 
                     "';'" ]

    symbolicNames = [ "<INVALID>", "ZCODE_COMMENT", "RETURN", "FOR", "IF", 
                      "NOT", "VAR", "UNTIL", "ELSE", "AND", "NUMBER", "DYNAMIC", 
                      "BY", "ELIF", "OR", "BOOL", "FUNC", "BREAK", "BEGIN", 
                      "STRING", "CONTINUE", "END", "ARRAY", "PLUS", "MINUS", 
                      "TIMES", "DIVIDED", "MOD", "EQUAL", "ASSIGN", "COMPARE", 
                      "NOT_EQUAL", "LT", "GT", "LTOE", "GTOE", "CONCATENATION", 
                      "LEFTPAREN", "RIGHTPAREN", "LEFTBRACKET", "RIGHTBRACKET", 
                      "COMMA", "COLON", "SEMI", "NUMBER_LITERAL", "BOOLEAN_LITERAL", 
                      "STRING_LITERAL", "SIZE", "IDENTIFIER", "WS", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_decllist = 1
    RULE_decl = 2
    RULE_primitype = 3
    RULE_implitype = 4
    RULE_arraytype = 5
    RULE_sizelist = 6
    RULE_array = 7
    RULE_listofArray = 8
    RULE_arrayvalue = 9
    RULE_vardecl = 10
    RULE_vardecl1 = 11
    RULE_vardecl2 = 12
    RULE_vardecl3 = 13
    RULE_vardecl4 = 14
    RULE_initval = 15
    RULE_funcdecl = 16
    RULE_paramdecl = 17
    RULE_paramlist = 18
    RULE_paramprime = 19
    RULE_param = 20
    RULE_bodyfunc = 21
    RULE_stmtlist = 22
    RULE_stmtprime = 23
    RULE_stmt = 24
    RULE_forstmt = 25
    RULE_assignstmt = 26
    RULE_ifstmt = 27
    RULE_breakstmt = 28
    RULE_continuestmt = 29
    RULE_returnstmt = 30
    RULE_funstmt = 31
    RULE_blockstmt = 32
    RULE_exprlist = 33
    RULE_exprprime = 34
    RULE_expr0 = 35
    RULE_expr1 = 36
    RULE_expr2 = 37
    RULE_expr3 = 38
    RULE_expr4 = 39
    RULE_expr5 = 40
    RULE_expr6 = 41
    RULE_expr7 = 42
    RULE_expr8 = 43
    RULE_expr9 = 44
    RULE_expr10 = 45

    ruleNames =  [ "program", "decllist", "decl", "primitype", "implitype", 
                   "arraytype", "sizelist", "array", "listofArray", "arrayvalue", 
                   "vardecl", "vardecl1", "vardecl2", "vardecl3", "vardecl4", 
                   "initval", "funcdecl", "paramdecl", "paramlist", "paramprime", 
                   "param", "bodyfunc", "stmtlist", "stmtprime", "stmt", 
                   "forstmt", "assignstmt", "ifstmt", "breakstmt", "continuestmt", 
                   "returnstmt", "funstmt", "blockstmt", "exprlist", "exprprime", 
                   "expr0", "expr1", "expr2", "expr3", "expr4", "expr5", 
                   "expr6", "expr7", "expr8", "expr9", "expr10" ]

    EOF = Token.EOF
    ZCODE_COMMENT=1
    RETURN=2
    FOR=3
    IF=4
    NOT=5
    VAR=6
    UNTIL=7
    ELSE=8
    AND=9
    NUMBER=10
    DYNAMIC=11
    BY=12
    ELIF=13
    OR=14
    BOOL=15
    FUNC=16
    BREAK=17
    BEGIN=18
    STRING=19
    CONTINUE=20
    END=21
    ARRAY=22
    PLUS=23
    MINUS=24
    TIMES=25
    DIVIDED=26
    MOD=27
    EQUAL=28
    ASSIGN=29
    COMPARE=30
    NOT_EQUAL=31
    LT=32
    GT=33
    LTOE=34
    GTOE=35
    CONCATENATION=36
    LEFTPAREN=37
    RIGHTPAREN=38
    LEFTBRACKET=39
    RIGHTBRACKET=40
    COMMA=41
    COLON=42
    SEMI=43
    NUMBER_LITERAL=44
    BOOLEAN_LITERAL=45
    STRING_LITERAL=46
    SIZE=47
    IDENTIFIER=48
    WS=49
    ERROR_CHAR=50
    UNCLOSE_STRING=51
    ILLEGAL_ESCAPE=52

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decllist(self):
            return self.getTypedRuleContext(ZCodeParser.DecllistContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.decllist()
            self.state = 93
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecllistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(ZCodeParser.DeclContext,0)


        def decllist(self):
            return self.getTypedRuleContext(ZCodeParser.DecllistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decllist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecllist" ):
                return visitor.visitDecllist(self)
            else:
                return visitor.visitChildren(self)




    def decllist(self):

        localctx = ZCodeParser.DecllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decllist)
        try:
            self.state = 99
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.decl()
                self.state = 96
                self.decllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 98
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(ZCodeParser.VardeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(ZCodeParser.FuncdeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = ZCodeParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 103
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.VAR, ZCodeParser.NUMBER, ZCodeParser.DYNAMIC, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.vardecl()
                pass
            elif token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.funcdecl()
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


    class PrimitypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_primitype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitype" ):
                return visitor.visitPrimitype(self)
            else:
                return visitor.visitChildren(self)




    def primitype(self):

        localctx = ZCodeParser.PrimitypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_primitype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
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


    class ImplitypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_implitype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplitype" ):
                return visitor.visitImplitype(self)
            else:
                return visitor.visitChildren(self)




    def implitype(self):

        localctx = ZCodeParser.ImplitypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_implitype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.VAR or _la==ZCodeParser.DYNAMIC):
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


    class ArraytypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitype(self):
            return self.getTypedRuleContext(ZCodeParser.PrimitypeContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LEFTBRACKET(self):
            return self.getToken(ZCodeParser.LEFTBRACKET, 0)

        def sizelist(self):
            return self.getTypedRuleContext(ZCodeParser.SizelistContext,0)


        def RIGHTBRACKET(self):
            return self.getToken(ZCodeParser.RIGHTBRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arraytype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraytype" ):
                return visitor.visitArraytype(self)
            else:
                return visitor.visitChildren(self)




    def arraytype(self):

        localctx = ZCodeParser.ArraytypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_arraytype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.primitype()
            self.state = 110
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 111
            self.match(ZCodeParser.LEFTBRACKET)
            self.state = 112
            self.sizelist()
            self.state = 113
            self.match(ZCodeParser.RIGHTBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SizelistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_LITERAL(self):
            return self.getToken(ZCodeParser.NUMBER_LITERAL, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def sizelist(self):
            return self.getTypedRuleContext(ZCodeParser.SizelistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_sizelist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSizelist" ):
                return visitor.visitSizelist(self)
            else:
                return visitor.visitChildren(self)




    def sizelist(self):

        localctx = ZCodeParser.SizelistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_sizelist)
        try:
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                self.match(ZCodeParser.NUMBER_LITERAL)
                self.state = 116
                self.match(ZCodeParser.COMMA)
                self.state = 117
                self.sizelist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.match(ZCodeParser.NUMBER_LITERAL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFTBRACKET(self):
            return self.getToken(ZCodeParser.LEFTBRACKET, 0)

        def RIGHTBRACKET(self):
            return self.getToken(ZCodeParser.RIGHTBRACKET, 0)

        def exprprime(self):
            return self.getTypedRuleContext(ZCodeParser.ExprprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = ZCodeParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(ZCodeParser.LEFTBRACKET)

            self.state = 122
            self.exprprime()
            self.state = 123
            self.match(ZCodeParser.RIGHTBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListofArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def listofArray(self):
            return self.getTypedRuleContext(ZCodeParser.ListofArrayContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_listofArray

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListofArray" ):
                return visitor.visitListofArray(self)
            else:
                return visitor.visitChildren(self)




    def listofArray(self):

        localctx = ZCodeParser.ListofArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_listofArray)
        try:
            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.array()
                self.state = 126
                self.match(ZCodeParser.COMMA)
                self.state = 127
                self.listofArray()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
                self.array()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayvalueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFTBRACKET(self):
            return self.getToken(ZCodeParser.LEFTBRACKET, 0)

        def listofArray(self):
            return self.getTypedRuleContext(ZCodeParser.ListofArrayContext,0)


        def RIGHTBRACKET(self):
            return self.getToken(ZCodeParser.RIGHTBRACKET, 0)

        def array(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayvalue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayvalue" ):
                return visitor.visitArrayvalue(self)
            else:
                return visitor.visitChildren(self)




    def arrayvalue(self):

        localctx = ZCodeParser.ArrayvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_arrayvalue)
        try:
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.match(ZCodeParser.LEFTBRACKET)
                self.state = 133
                self.listofArray()
                self.state = 134
                self.match(ZCodeParser.RIGHTBRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.array()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl1(self):
            return self.getTypedRuleContext(ZCodeParser.Vardecl1Context,0)


        def vardecl2(self):
            return self.getTypedRuleContext(ZCodeParser.Vardecl2Context,0)


        def vardecl3(self):
            return self.getTypedRuleContext(ZCodeParser.Vardecl3Context,0)


        def vardecl4(self):
            return self.getTypedRuleContext(ZCodeParser.Vardecl4Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = ZCodeParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_vardecl)
        try:
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.vardecl1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.vardecl2()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 141
                self.vardecl3()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 142
                self.vardecl4()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vardecl1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitype(self):
            return self.getTypedRuleContext(ZCodeParser.PrimitypeContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def initval(self):
            return self.getTypedRuleContext(ZCodeParser.InitvalContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_vardecl1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl1" ):
                return visitor.visitVardecl1(self)
            else:
                return visitor.visitChildren(self)




    def vardecl1(self):

        localctx = ZCodeParser.Vardecl1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_vardecl1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.primitype()
            self.state = 146
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 147
                self.match(ZCodeParser.ASSIGN)
                self.state = 148
                self.initval()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vardecl2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def initval(self):
            return self.getTypedRuleContext(ZCodeParser.InitvalContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_vardecl2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl2" ):
                return visitor.visitVardecl2(self)
            else:
                return visitor.visitChildren(self)




    def vardecl2(self):

        localctx = ZCodeParser.Vardecl2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_vardecl2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(ZCodeParser.VAR)
            self.state = 152
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 153
            self.match(ZCodeParser.ASSIGN)
            self.state = 154
            self.initval()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vardecl3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def initval(self):
            return self.getTypedRuleContext(ZCodeParser.InitvalContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_vardecl3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl3" ):
                return visitor.visitVardecl3(self)
            else:
                return visitor.visitChildren(self)




    def vardecl3(self):

        localctx = ZCodeParser.Vardecl3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_vardecl3)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(ZCodeParser.DYNAMIC)
            self.state = 157
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 158
                self.match(ZCodeParser.ASSIGN)
                self.state = 159
                self.initval()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vardecl4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arraytype(self):
            return self.getTypedRuleContext(ZCodeParser.ArraytypeContext,0)


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def arrayvalue(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayvalueContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_vardecl4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl4" ):
                return visitor.visitVardecl4(self)
            else:
                return visitor.visitChildren(self)




    def vardecl4(self):

        localctx = ZCodeParser.Vardecl4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_vardecl4)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.arraytype()
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 163
                self.match(ZCodeParser.ASSIGN)
                self.state = 164
                self.arrayvalue()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitvalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprlist(self):
            return self.getTypedRuleContext(ZCodeParser.ExprlistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_initval

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitval" ):
                return visitor.visitInitval(self)
            else:
                return visitor.visitChildren(self)




    def initval(self):

        localctx = ZCodeParser.InitvalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_initval)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.exprlist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def paramdecl(self):
            return self.getTypedRuleContext(ZCodeParser.ParamdeclContext,0)


        def bodyfunc(self):
            return self.getTypedRuleContext(ZCodeParser.BodyfuncContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = ZCodeParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(ZCodeParser.FUNC)
            self.state = 170
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 171
            self.paramdecl()
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.RETURN or _la==ZCodeParser.BEGIN:
                self.state = 172
                self.bodyfunc()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFTPAREN(self):
            return self.getToken(ZCodeParser.LEFTPAREN, 0)

        def paramlist(self):
            return self.getTypedRuleContext(ZCodeParser.ParamlistContext,0)


        def RIGHTPAREN(self):
            return self.getToken(ZCodeParser.RIGHTPAREN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_paramdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamdecl" ):
                return visitor.visitParamdecl(self)
            else:
                return visitor.visitChildren(self)




    def paramdecl(self):

        localctx = ZCodeParser.ParamdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_paramdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(ZCodeParser.LEFTPAREN)
            self.state = 176
            self.paramlist()
            self.state = 177
            self.match(ZCodeParser.RIGHTPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramprime(self):
            return self.getTypedRuleContext(ZCodeParser.ParamprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




    def paramlist(self):

        localctx = ZCodeParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_paramlist)
        try:
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.paramprime()
                pass
            elif token in [ZCodeParser.RIGHTPAREN]:
                self.enterOuterAlt(localctx, 2)

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


    class ParamprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(ZCodeParser.ParamContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def paramprime(self):
            return self.getTypedRuleContext(ZCodeParser.ParamprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamprime" ):
                return visitor.visitParamprime(self)
            else:
                return visitor.visitChildren(self)




    def paramprime(self):

        localctx = ZCodeParser.ParamprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_paramprime)
        try:
            self.state = 188
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.param()
                self.state = 184
                self.match(ZCodeParser.COMMA)
                self.state = 185
                self.paramprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 187
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitype(self):
            return self.getTypedRuleContext(ZCodeParser.PrimitypeContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LEFTBRACKET(self):
            return self.getToken(ZCodeParser.LEFTBRACKET, 0)

        def exprprime(self):
            return self.getTypedRuleContext(ZCodeParser.ExprprimeContext,0)


        def RIGHTBRACKET(self):
            return self.getToken(ZCodeParser.RIGHTBRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = ZCodeParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.primitype()
            self.state = 197
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 191
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 192
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 193
                self.match(ZCodeParser.LEFTBRACKET)
                self.state = 194
                self.exprprime()
                self.state = 195
                self.match(ZCodeParser.RIGHTBRACKET)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyfuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def returnstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ReturnstmtContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(ZCodeParser.BlockstmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_bodyfunc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBodyfunc" ):
                return visitor.visitBodyfunc(self)
            else:
                return visitor.visitChildren(self)




    def bodyfunc(self):

        localctx = ZCodeParser.BodyfuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_bodyfunc)
        try:
            self.state = 201
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 199
                self.returnstmt()
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 200
                self.blockstmt()
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


    class StmtlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmtprime(self):
            return self.getTypedRuleContext(ZCodeParser.StmtprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmtlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtlist" ):
                return visitor.visitStmtlist(self)
            else:
                return visitor.visitChildren(self)




    def stmtlist(self):

        localctx = ZCodeParser.StmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_stmtlist)
        try:
            self.state = 205
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN, ZCodeParser.FOR, ZCodeParser.IF, ZCodeParser.VAR, ZCodeParser.NUMBER, ZCodeParser.DYNAMIC, ZCodeParser.BOOL, ZCodeParser.BREAK, ZCodeParser.BEGIN, ZCodeParser.STRING, ZCodeParser.CONTINUE, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self.stmtprime()
                pass
            elif token in [ZCodeParser.END]:
                self.enterOuterAlt(localctx, 2)

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


    class StmtprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmtprime(self):
            return self.getTypedRuleContext(ZCodeParser.StmtprimeContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(ZCodeParser.VardeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmtprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtprime" ):
                return visitor.visitStmtprime(self)
            else:
                return visitor.visitChildren(self)




    def stmtprime(self):

        localctx = ZCodeParser.StmtprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_stmtprime)
        try:
            self.state = 217
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.RETURN, ZCodeParser.FOR, ZCodeParser.IF, ZCodeParser.BREAK, ZCodeParser.BEGIN, ZCodeParser.CONTINUE, ZCodeParser.IDENTIFIER]:
                    self.state = 207
                    self.stmt()
                    pass
                elif token in [ZCodeParser.VAR, ZCodeParser.NUMBER, ZCodeParser.DYNAMIC, ZCodeParser.BOOL, ZCodeParser.STRING]:
                    self.state = 208
                    self.vardecl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 211
                self.stmtprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.RETURN, ZCodeParser.FOR, ZCodeParser.IF, ZCodeParser.BREAK, ZCodeParser.BEGIN, ZCodeParser.CONTINUE, ZCodeParser.IDENTIFIER]:
                    self.state = 213
                    self.stmt()
                    pass
                elif token in [ZCodeParser.VAR, ZCodeParser.NUMBER, ZCodeParser.DYNAMIC, ZCodeParser.BOOL, ZCodeParser.STRING]:
                    self.state = 214
                    self.vardecl()
                    pass
                else:
                    raise NoViableAltException(self)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignstmt(self):
            return self.getTypedRuleContext(ZCodeParser.AssignstmtContext,0)


        def forstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ForstmtContext,0)


        def ifstmt(self):
            return self.getTypedRuleContext(ZCodeParser.IfstmtContext,0)


        def breakstmt(self):
            return self.getTypedRuleContext(ZCodeParser.BreakstmtContext,0)


        def continuestmt(self):
            return self.getTypedRuleContext(ZCodeParser.ContinuestmtContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ReturnstmtContext,0)


        def funstmt(self):
            return self.getTypedRuleContext(ZCodeParser.FunstmtContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(ZCodeParser.BlockstmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = ZCodeParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_stmt)
        try:
            self.state = 227
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.assignstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.forstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 221
                self.ifstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 222
                self.breakstmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 223
                self.continuestmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 224
                self.returnstmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 225
                self.funstmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 226
                self.blockstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def exprprime(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprprimeContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprprimeContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def stmtprime(self):
            return self.getTypedRuleContext(ZCodeParser.StmtprimeContext,0)


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_forstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstmt" ):
                return visitor.visitForstmt(self)
            else:
                return visitor.visitChildren(self)




    def forstmt(self):

        localctx = ZCodeParser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_forstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(ZCodeParser.FOR)
            self.state = 230
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 233
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT, ZCodeParser.MINUS, ZCodeParser.LEFTPAREN, ZCodeParser.LEFTBRACKET, ZCodeParser.NUMBER_LITERAL, ZCodeParser.BOOLEAN_LITERAL, ZCodeParser.STRING_LITERAL, ZCodeParser.IDENTIFIER]:
                self.state = 231
                self.exprprime()
                pass
            elif token in [ZCodeParser.UNTIL, ZCodeParser.ASSIGN]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 235
                self.match(ZCodeParser.ASSIGN)
                self.state = 236
                self.exprprime()


            self.state = 239
            self.match(ZCodeParser.UNTIL)
            self.state = 240
            self.exprprime()
            self.state = 241
            self.match(ZCodeParser.BY)
            self.state = 242
            self.exprprime()
            self.state = 243
            self.stmtprime()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def exprprime(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprprimeContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprprimeContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assignstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignstmt" ):
                return visitor.visitAssignstmt(self)
            else:
                return visitor.visitChildren(self)




    def assignstmt(self):

        localctx = ZCodeParser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_assignstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 249
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NOT) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.LEFTPAREN) | (1 << ZCodeParser.LEFTBRACKET) | (1 << ZCodeParser.NUMBER_LITERAL) | (1 << ZCodeParser.BOOLEAN_LITERAL) | (1 << ZCodeParser.STRING_LITERAL) | (1 << ZCodeParser.IDENTIFIER))) != 0):
                self.state = 246
                self.exprprime()
                self.state = 251
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 252
            self.match(ZCodeParser.ASSIGN)
            self.state = 253
            self.exprprime()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def expr0(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr0Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr0Context,i)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.StmtContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.StmtContext,i)


        def ELIF(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.ELIF)
            else:
                return self.getToken(ZCodeParser.ELIF, i)

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_ifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmt" ):
                return visitor.visitIfstmt(self)
            else:
                return visitor.visitChildren(self)




    def ifstmt(self):

        localctx = ZCodeParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_ifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.match(ZCodeParser.IF)
            self.state = 256
            self.expr0()
            self.state = 257
            self.stmt()
            self.state = 265
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 259
                    self.match(ZCodeParser.ELIF)
                    self.state = 260
                    self.expr0()
                    self.state = 261
                    self.stmt() 
                self.state = 267
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

            self.state = 270
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 268
                self.match(ZCodeParser.ELSE)
                self.state = 269
                self.stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_breakstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakstmt" ):
                return visitor.visitBreakstmt(self)
            else:
                return visitor.visitChildren(self)




    def breakstmt(self):

        localctx = ZCodeParser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(ZCodeParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_continuestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinuestmt" ):
                return visitor.visitContinuestmt(self)
            else:
                return visitor.visitChildren(self)




    def continuestmt(self):

        localctx = ZCodeParser.ContinuestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(ZCodeParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def exprlist(self):
            return self.getTypedRuleContext(ZCodeParser.ExprlistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_returnstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstmt" ):
                return visitor.visitReturnstmt(self)
            else:
                return visitor.visitChildren(self)




    def returnstmt(self):

        localctx = ZCodeParser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_returnstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(ZCodeParser.RETURN)
            self.state = 277
            self.exprlist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LEFTPAREN(self):
            return self.getToken(ZCodeParser.LEFTPAREN, 0)

        def exprlist(self):
            return self.getTypedRuleContext(ZCodeParser.ExprlistContext,0)


        def RIGHTPAREN(self):
            return self.getToken(ZCodeParser.RIGHTPAREN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_funstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunstmt" ):
                return visitor.visitFunstmt(self)
            else:
                return visitor.visitChildren(self)




    def funstmt(self):

        localctx = ZCodeParser.FunstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_funstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 280
            self.match(ZCodeParser.LEFTPAREN)
            self.state = 281
            self.exprlist()
            self.state = 282
            self.match(ZCodeParser.RIGHTPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def stmtlist(self):
            return self.getTypedRuleContext(ZCodeParser.StmtlistContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_blockstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockstmt" ):
                return visitor.visitBlockstmt(self)
            else:
                return visitor.visitChildren(self)




    def blockstmt(self):

        localctx = ZCodeParser.BlockstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_blockstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.match(ZCodeParser.BEGIN)
            self.state = 285
            self.stmtlist()
            self.state = 286
            self.match(ZCodeParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprprime(self):
            return self.getTypedRuleContext(ZCodeParser.ExprprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exprlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprlist" ):
                return visitor.visitExprlist(self)
            else:
                return visitor.visitChildren(self)




    def exprlist(self):

        localctx = ZCodeParser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_exprlist)
        try:
            self.state = 290
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 288
                self.exprprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr0(self):
            return self.getTypedRuleContext(ZCodeParser.Expr0Context,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def exprprime(self):
            return self.getTypedRuleContext(ZCodeParser.ExprprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exprprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprprime" ):
                return visitor.visitExprprime(self)
            else:
                return visitor.visitChildren(self)




    def exprprime(self):

        localctx = ZCodeParser.ExprprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_exprprime)
        try:
            self.state = 297
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.expr0()
                self.state = 293
                self.match(ZCodeParser.COMMA)
                self.state = 294
                self.exprprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 296
                self.expr0()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr0Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr1Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr1Context,i)


        def CONCATENATION(self):
            return self.getToken(ZCodeParser.CONCATENATION, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr0

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr0" ):
                return visitor.visitExpr0(self)
            else:
                return visitor.visitChildren(self)




    def expr0(self):

        localctx = ZCodeParser.Expr0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_expr0)
        try:
            self.state = 304
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.expr1()
                self.state = 300
                self.match(ZCodeParser.CONCATENATION)
                self.state = 301
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 303
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr2Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr2Context,i)


        def EQUAL(self):
            return self.getToken(ZCodeParser.EQUAL, 0)

        def COMPARE(self):
            return self.getToken(ZCodeParser.COMPARE, 0)

        def NOT_EQUAL(self):
            return self.getToken(ZCodeParser.NOT_EQUAL, 0)

        def LT(self):
            return self.getToken(ZCodeParser.LT, 0)

        def GT(self):
            return self.getToken(ZCodeParser.GT, 0)

        def LTOE(self):
            return self.getToken(ZCodeParser.LTOE, 0)

        def GTOE(self):
            return self.getToken(ZCodeParser.GTOE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = ZCodeParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 311
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 306
                self.expr2(0)
                self.state = 307
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQUAL) | (1 << ZCodeParser.COMPARE) | (1 << ZCodeParser.NOT_EQUAL) | (1 << ZCodeParser.LT) | (1 << ZCodeParser.GT) | (1 << ZCodeParser.LTOE) | (1 << ZCodeParser.GTOE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 308
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 310
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(ZCodeParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(ZCodeParser.Expr2Context,0)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 321
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 316
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 317
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 318
                    self.expr3(0) 
                self.state = 323
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(ZCodeParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(ZCodeParser.Expr3Context,0)


        def PLUS(self):
            return self.getToken(ZCodeParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(ZCodeParser.MINUS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 332
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 327
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 328
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.PLUS or _la==ZCodeParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 329
                    self.expr4(0) 
                self.state = 334
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(ZCodeParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(ZCodeParser.Expr4Context,0)


        def TIMES(self):
            return self.getToken(ZCodeParser.TIMES, 0)

        def DIVIDED(self):
            return self.getToken(ZCodeParser.DIVIDED, 0)

        def MOD(self):
            return self.getToken(ZCodeParser.MOD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 343
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 338
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 339
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TIMES) | (1 << ZCodeParser.DIVIDED) | (1 << ZCodeParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 340
                    self.expr5() 
                self.state = 345
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def expr5(self):
            return self.getTypedRuleContext(ZCodeParser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = ZCodeParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_expr5)
        try:
            self.state = 349
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 346
                self.match(ZCodeParser.NOT)
                self.state = 347
                self.expr5()
                pass
            elif token in [ZCodeParser.MINUS, ZCodeParser.LEFTPAREN, ZCodeParser.LEFTBRACKET, ZCodeParser.NUMBER_LITERAL, ZCodeParser.BOOLEAN_LITERAL, ZCodeParser.STRING_LITERAL, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 348
                self.expr6()
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


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(ZCodeParser.MINUS, 0)

        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(ZCodeParser.Expr7Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = ZCodeParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_expr6)
        try:
            self.state = 354
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 351
                self.match(ZCodeParser.MINUS)
                self.state = 352
                self.expr6()
                pass
            elif token in [ZCodeParser.LEFTPAREN, ZCodeParser.LEFTBRACKET, ZCodeParser.NUMBER_LITERAL, ZCodeParser.BOOLEAN_LITERAL, ZCodeParser.STRING_LITERAL, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 353
                self.expr7()
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


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LEFTBRACKET(self):
            return self.getToken(ZCodeParser.LEFTBRACKET, 0)

        def exprprime(self):
            return self.getTypedRuleContext(ZCodeParser.ExprprimeContext,0)


        def RIGHTBRACKET(self):
            return self.getToken(ZCodeParser.RIGHTBRACKET, 0)

        def expr8(self):
            return self.getTypedRuleContext(ZCodeParser.Expr8Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = ZCodeParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_expr7)
        try:
            self.state = 362
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 356
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 357
                self.match(ZCodeParser.LEFTBRACKET)
                self.state = 358
                self.exprprime()
                self.state = 359
                self.match(ZCodeParser.RIGHTBRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 361
                self.expr8()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LEFTPAREN(self):
            return self.getToken(ZCodeParser.LEFTPAREN, 0)

        def exprlist(self):
            return self.getTypedRuleContext(ZCodeParser.ExprlistContext,0)


        def RIGHTPAREN(self):
            return self.getToken(ZCodeParser.RIGHTPAREN, 0)

        def expr9(self):
            return self.getTypedRuleContext(ZCodeParser.Expr9Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)




    def expr8(self):

        localctx = ZCodeParser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_expr8)
        try:
            self.state = 370
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 364
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 365
                self.match(ZCodeParser.LEFTPAREN)
                self.state = 366
                self.exprlist()
                self.state = 367
                self.match(ZCodeParser.RIGHTPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 369
                self.expr9()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_LITERAL(self):
            return self.getToken(ZCodeParser.NUMBER_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(ZCodeParser.STRING_LITERAL, 0)

        def BOOLEAN_LITERAL(self):
            return self.getToken(ZCodeParser.BOOLEAN_LITERAL, 0)

        def array(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def expr10(self):
            return self.getTypedRuleContext(ZCodeParser.Expr10Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr9" ):
                return visitor.visitExpr9(self)
            else:
                return visitor.visitChildren(self)




    def expr9(self):

        localctx = ZCodeParser.Expr9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_expr9)
        try:
            self.state = 378
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 372
                self.match(ZCodeParser.NUMBER_LITERAL)
                pass
            elif token in [ZCodeParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 373
                self.match(ZCodeParser.STRING_LITERAL)
                pass
            elif token in [ZCodeParser.BOOLEAN_LITERAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 374
                self.match(ZCodeParser.BOOLEAN_LITERAL)
                pass
            elif token in [ZCodeParser.LEFTBRACKET]:
                self.enterOuterAlt(localctx, 4)
                self.state = 375
                self.array()
                pass
            elif token in [ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 5)
                self.state = 376
                self.match(ZCodeParser.IDENTIFIER)
                pass
            elif token in [ZCodeParser.LEFTPAREN]:
                self.enterOuterAlt(localctx, 6)
                self.state = 377
                self.expr10()
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


    class Expr10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFTPAREN(self):
            return self.getToken(ZCodeParser.LEFTPAREN, 0)

        def expr0(self):
            return self.getTypedRuleContext(ZCodeParser.Expr0Context,0)


        def RIGHTPAREN(self):
            return self.getToken(ZCodeParser.RIGHTPAREN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr10" ):
                return visitor.visitExpr10(self)
            else:
                return visitor.visitChildren(self)




    def expr10(self):

        localctx = ZCodeParser.Expr10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_expr10)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self.match(ZCodeParser.LEFTPAREN)
            self.state = 381
            self.expr0()
            self.state = 382
            self.match(ZCodeParser.RIGHTPAREN)
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
        self._predicates[37] = self.expr2_sempred
        self._predicates[38] = self.expr3_sempred
        self._predicates[39] = self.expr4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




