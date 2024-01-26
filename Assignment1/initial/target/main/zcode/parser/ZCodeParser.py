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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\64")
        buf.write("\u01be\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3p\n\3\3\4\3\4\3\4\5\4")
        buf.write("u\n\4\3\5\3\5\3\6\3\6\3\7\3\7\5\7}\n\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\5\t\u008e")
        buf.write("\n\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\5\13\u0099")
        buf.write("\n\13\3\f\3\f\3\f\5\f\u009e\n\f\3\f\3\f\3\r\3\r\3\r\3")
        buf.write("\r\5\r\u00a6\n\r\3\r\3\r\3\16\3\16\3\16\3\16\5\16\u00ae")
        buf.write("\n\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\5\20")
        buf.write("\u00b9\n\20\3\21\3\21\3\21\5\21\u00be\n\21\3\21\3\21\3")
        buf.write("\21\3\21\5\21\u00c4\n\21\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\5\23\u00ce\n\23\3\23\3\23\3\24\3\24\3\24\3")
        buf.write("\24\3\25\3\25\5\25\u00d8\n\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\5\26\u00df\n\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5")
        buf.write("\27\u00e8\n\27\3\30\3\30\5\30\u00ec\n\30\3\31\3\31\5\31")
        buf.write("\u00f0\n\31\3\32\3\32\3\32\3\32\5\32\u00f6\n\32\3\32\3")
        buf.write("\32\3\32\3\32\3\32\3\32\5\32\u00fe\n\32\5\32\u0100\n\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u010a\n")
        buf.write("\33\3\34\3\34\3\34\3\34\5\34\u0110\n\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\5\35\u011d\n")
        buf.write("\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\5\36\u012d\n\36\3\37\3\37\3\37\3")
        buf.write(" \3 \3 \3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3")
        buf.write("#\3#\3#\3$\3$\5$\u0147\n$\3%\3%\3%\3%\3%\3%\3%\3%\3%\3")
        buf.write("%\3%\5%\u0154\n%\3&\3&\5&\u0158\n&\3\'\3\'\3\'\3\'\3\'")
        buf.write("\5\'\u015f\n\'\3(\3(\3(\3(\3(\5(\u0166\n(\3)\3)\3)\3)")
        buf.write("\3)\5)\u016d\n)\3*\3*\3*\3*\3*\3*\7*\u0175\n*\f*\16*\u0178")
        buf.write("\13*\3+\3+\3+\3+\3+\3+\7+\u0180\n+\f+\16+\u0183\13+\3")
        buf.write(",\3,\3,\3,\3,\3,\7,\u018b\n,\f,\16,\u018e\13,\3-\3-\3")
        buf.write("-\5-\u0193\n-\3.\3.\3.\5.\u0198\n.\3/\3/\3/\3/\3/\3/\5")
        buf.write("/\u01a0\n/\3\60\3\60\3\60\3\60\3\60\3\60\5\60\u01a8\n")
        buf.write("\60\3\61\3\61\3\61\3\61\3\61\5\61\u01af\n\61\3\62\3\62")
        buf.write("\3\62\3\62\3\63\3\63\5\63\u01b7\n\63\3\64\3\64\3\64\5")
        buf.write("\64\u01bc\n\64\3\64\2\5RTV\65\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVX")
        buf.write("Z\\^`bdf\2\b\5\2\f\f\21\21\25\25\4\2\b\b\r\r\4\2\36\37")
        buf.write("!%\4\2\13\13\20\20\3\2\31\32\3\2\33\35\2\u01be\2h\3\2")
        buf.write("\2\2\4o\3\2\2\2\6t\3\2\2\2\bv\3\2\2\2\nx\3\2\2\2\f|\3")
        buf.write("\2\2\2\16\u0083\3\2\2\2\20\u008d\3\2\2\2\22\u008f\3\2")
        buf.write("\2\2\24\u0098\3\2\2\2\26\u009a\3\2\2\2\30\u00a5\3\2\2")
        buf.write("\2\32\u00a9\3\2\2\2\34\u00af\3\2\2\2\36\u00b4\3\2\2\2")
        buf.write(" \u00c3\3\2\2\2\"\u00c5\3\2\2\2$\u00c7\3\2\2\2&\u00d1")
        buf.write("\3\2\2\2(\u00d7\3\2\2\2*\u00de\3\2\2\2,\u00e0\3\2\2\2")
        buf.write(".\u00eb\3\2\2\2\60\u00ef\3\2\2\2\62\u00ff\3\2\2\2\64\u0109")
        buf.write("\3\2\2\2\66\u010b\3\2\2\28\u011c\3\2\2\2:\u0122\3\2\2")
        buf.write("\2<\u012e\3\2\2\2>\u0131\3\2\2\2@\u0134\3\2\2\2B\u0138")
        buf.write("\3\2\2\2D\u013e\3\2\2\2F\u0146\3\2\2\2H\u0153\3\2\2\2")
        buf.write("J\u0157\3\2\2\2L\u015e\3\2\2\2N\u0165\3\2\2\2P\u016c\3")
        buf.write("\2\2\2R\u016e\3\2\2\2T\u0179\3\2\2\2V\u0184\3\2\2\2X\u0192")
        buf.write("\3\2\2\2Z\u0197\3\2\2\2\\\u019f\3\2\2\2^\u01a7\3\2\2\2")
        buf.write("`\u01ae\3\2\2\2b\u01b0\3\2\2\2d\u01b6\3\2\2\2f\u01bb\3")
        buf.write("\2\2\2hi\5\4\3\2ij\7\2\2\3j\3\3\2\2\2kl\5\6\4\2lm\5\4")
        buf.write("\3\2mp\3\2\2\2np\5\6\4\2ok\3\2\2\2on\3\2\2\2p\5\3\2\2")
        buf.write("\2qu\5\30\r\2ru\5$\23\2su\7,\2\2tq\3\2\2\2tr\3\2\2\2t")
        buf.write("s\3\2\2\2u\7\3\2\2\2vw\t\2\2\2w\t\3\2\2\2xy\t\3\2\2y\13")
        buf.write("\3\2\2\2z}\5\b\5\2{}\7\r\2\2|z\3\2\2\2|{\3\2\2\2}~\3\2")
        buf.write("\2\2~\177\7\60\2\2\177\u0080\7)\2\2\u0080\u0081\5\20\t")
        buf.write("\2\u0081\u0082\7*\2\2\u0082\r\3\2\2\2\u0083\u0084\7\b")
        buf.write("\2\2\u0084\u0085\7\60\2\2\u0085\u0086\7)\2\2\u0086\u0087")
        buf.write("\5\20\t\2\u0087\u0088\7*\2\2\u0088\17\3\2\2\2\u0089\u008a")
        buf.write("\7-\2\2\u008a\u008b\7+\2\2\u008b\u008e\5\20\t\2\u008c")
        buf.write("\u008e\7-\2\2\u008d\u0089\3\2\2\2\u008d\u008c\3\2\2\2")
        buf.write("\u008e\21\3\2\2\2\u008f\u0090\7)\2\2\u0090\u0091\5L\'")
        buf.write("\2\u0091\u0092\7*\2\2\u0092\23\3\2\2\2\u0093\u0094\5\22")
        buf.write("\n\2\u0094\u0095\7+\2\2\u0095\u0096\5\24\13\2\u0096\u0099")
        buf.write("\3\2\2\2\u0097\u0099\5\22\n\2\u0098\u0093\3\2\2\2\u0098")
        buf.write("\u0097\3\2\2\2\u0099\25\3\2\2\2\u009a\u009d\7)\2\2\u009b")
        buf.write("\u009e\5\24\13\2\u009c\u009e\5L\'\2\u009d\u009b\3\2\2")
        buf.write("\2\u009d\u009c\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a0")
        buf.write("\7*\2\2\u00a0\27\3\2\2\2\u00a1\u00a6\5\32\16\2\u00a2\u00a6")
        buf.write("\5\34\17\2\u00a3\u00a6\5\36\20\2\u00a4\u00a6\5 \21\2\u00a5")
        buf.write("\u00a1\3\2\2\2\u00a5\u00a2\3\2\2\2\u00a5\u00a3\3\2\2\2")
        buf.write("\u00a5\u00a4\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00a8\5")
        buf.write("d\63\2\u00a8\31\3\2\2\2\u00a9\u00aa\5\b\5\2\u00aa\u00ad")
        buf.write("\7\60\2\2\u00ab\u00ac\7 \2\2\u00ac\u00ae\5\"\22\2\u00ad")
        buf.write("\u00ab\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\33\3\2\2\2\u00af")
        buf.write("\u00b0\7\b\2\2\u00b0\u00b1\7\60\2\2\u00b1\u00b2\7 \2\2")
        buf.write("\u00b2\u00b3\5\"\22\2\u00b3\35\3\2\2\2\u00b4\u00b5\7\r")
        buf.write("\2\2\u00b5\u00b8\7\60\2\2\u00b6\u00b7\7 \2\2\u00b7\u00b9")
        buf.write("\5\"\22\2\u00b8\u00b6\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9")
        buf.write("\37\3\2\2\2\u00ba\u00bd\5\f\7\2\u00bb\u00bc\7 \2\2\u00bc")
        buf.write("\u00be\5\26\f\2\u00bd\u00bb\3\2\2\2\u00bd\u00be\3\2\2")
        buf.write("\2\u00be\u00c4\3\2\2\2\u00bf\u00c0\5\16\b\2\u00c0\u00c1")
        buf.write("\7 \2\2\u00c1\u00c2\5\26\f\2\u00c2\u00c4\3\2\2\2\u00c3")
        buf.write("\u00ba\3\2\2\2\u00c3\u00bf\3\2\2\2\u00c4!\3\2\2\2\u00c5")
        buf.write("\u00c6\5J&\2\u00c6#\3\2\2\2\u00c7\u00c8\7\22\2\2\u00c8")
        buf.write("\u00c9\7\60\2\2\u00c9\u00ca\5&\24\2\u00ca\u00cd\5d\63")
        buf.write("\2\u00cb\u00ce\5.\30\2\u00cc\u00ce\3\2\2\2\u00cd\u00cb")
        buf.write("\3\2\2\2\u00cd\u00cc\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf")
        buf.write("\u00d0\5d\63\2\u00d0%\3\2\2\2\u00d1\u00d2\7\'\2\2\u00d2")
        buf.write("\u00d3\5(\25\2\u00d3\u00d4\7(\2\2\u00d4\'\3\2\2\2\u00d5")
        buf.write("\u00d8\5*\26\2\u00d6\u00d8\3\2\2\2\u00d7\u00d5\3\2\2\2")
        buf.write("\u00d7\u00d6\3\2\2\2\u00d8)\3\2\2\2\u00d9\u00da\5,\27")
        buf.write("\2\u00da\u00db\7+\2\2\u00db\u00dc\5*\26\2\u00dc\u00df")
        buf.write("\3\2\2\2\u00dd\u00df\5,\27\2\u00de\u00d9\3\2\2\2\u00de")
        buf.write("\u00dd\3\2\2\2\u00df+\3\2\2\2\u00e0\u00e7\5\b\5\2\u00e1")
        buf.write("\u00e8\7\60\2\2\u00e2\u00e3\7\60\2\2\u00e3\u00e4\7)\2")
        buf.write("\2\u00e4\u00e5\5L\'\2\u00e5\u00e6\7*\2\2\u00e6\u00e8\3")
        buf.write("\2\2\2\u00e7\u00e1\3\2\2\2\u00e7\u00e2\3\2\2\2\u00e8-")
        buf.write("\3\2\2\2\u00e9\u00ec\5@!\2\u00ea\u00ec\5D#\2\u00eb\u00e9")
        buf.write("\3\2\2\2\u00eb\u00ea\3\2\2\2\u00ec/\3\2\2\2\u00ed\u00f0")
        buf.write("\5\62\32\2\u00ee\u00f0\3\2\2\2\u00ef\u00ed\3\2\2\2\u00ef")
        buf.write("\u00ee\3\2\2\2\u00f0\61\3\2\2\2\u00f1\u00f6\5\64\33\2")
        buf.write("\u00f2\u00f3\5\30\r\2\u00f3\u00f4\5f\64\2\u00f4\u00f6")
        buf.write("\3\2\2\2\u00f5\u00f1\3\2\2\2\u00f5\u00f2\3\2\2\2\u00f6")
        buf.write("\u00f7\3\2\2\2\u00f7\u00f8\5\62\32\2\u00f8\u0100\3\2\2")
        buf.write("\2\u00f9\u00fe\5\64\33\2\u00fa\u00fb\5\30\r\2\u00fb\u00fc")
        buf.write("\5f\64\2\u00fc\u00fe\3\2\2\2\u00fd\u00f9\3\2\2\2\u00fd")
        buf.write("\u00fa\3\2\2\2\u00fe\u0100\3\2\2\2\u00ff\u00f5\3\2\2\2")
        buf.write("\u00ff\u00fd\3\2\2\2\u0100\63\3\2\2\2\u0101\u010a\58\35")
        buf.write("\2\u0102\u010a\5\66\34\2\u0103\u010a\5:\36\2\u0104\u010a")
        buf.write("\5<\37\2\u0105\u010a\5> \2\u0106\u010a\5@!\2\u0107\u010a")
        buf.write("\5B\"\2\u0108\u010a\5D#\2\u0109\u0101\3\2\2\2\u0109\u0102")
        buf.write("\3\2\2\2\u0109\u0103\3\2\2\2\u0109\u0104\3\2\2\2\u0109")
        buf.write("\u0105\3\2\2\2\u0109\u0106\3\2\2\2\u0109\u0107\3\2\2\2")
        buf.write("\u0109\u0108\3\2\2\2\u010a\65\3\2\2\2\u010b\u010c\7\5")
        buf.write("\2\2\u010c\u010d\7\60\2\2\u010d\u010f\5J&\2\u010e\u0110")
        buf.write("\7 \2\2\u010f\u010e\3\2\2\2\u010f\u0110\3\2\2\2\u0110")
        buf.write("\u0111\3\2\2\2\u0111\u0112\5J&\2\u0112\u0113\3\2\2\2\u0113")
        buf.write("\u0114\7\t\2\2\u0114\u0115\5L\'\2\u0115\u0116\7\16\2\2")
        buf.write("\u0116\u0117\5L\'\2\u0117\u0118\5d\63\2\u0118\u0119\5")
        buf.write("\62\32\2\u0119\67\3\2\2\2\u011a\u011d\7\60\2\2\u011b\u011d")
        buf.write("\5\\/\2\u011c\u011a\3\2\2\2\u011c\u011b\3\2\2\2\u011d")
        buf.write("\u011e\3\2\2\2\u011e\u011f\7 \2\2\u011f\u0120\5L\'\2\u0120")
        buf.write("\u0121\5f\64\2\u01219\3\2\2\2\u0122\u0123\7\6\2\2\u0123")
        buf.write("\u0124\5N(\2\u0124\u0125\5d\63\2\u0125\u0126\5\64\33\2")
        buf.write("\u0126\u0127\3\2\2\2\u0127\u012c\5F$\2\u0128\u0129\7\n")
        buf.write("\2\2\u0129\u012a\5d\63\2\u012a\u012b\5\64\33\2\u012b\u012d")
        buf.write("\3\2\2\2\u012c\u0128\3\2\2\2\u012c\u012d\3\2\2\2\u012d")
        buf.write(";\3\2\2\2\u012e\u012f\7\23\2\2\u012f\u0130\5f\64\2\u0130")
        buf.write("=\3\2\2\2\u0131\u0132\7\26\2\2\u0132\u0133\5f\64\2\u0133")
        buf.write("?\3\2\2\2\u0134\u0135\7\4\2\2\u0135\u0136\5J&\2\u0136")
        buf.write("\u0137\5f\64\2\u0137A\3\2\2\2\u0138\u0139\7\60\2\2\u0139")
        buf.write("\u013a\7\'\2\2\u013a\u013b\5J&\2\u013b\u013c\7(\2\2\u013c")
        buf.write("\u013d\5f\64\2\u013dC\3\2\2\2\u013e\u013f\7\24\2\2\u013f")
        buf.write("\u0140\5f\64\2\u0140\u0141\5\60\31\2\u0141\u0142\7\27")
        buf.write("\2\2\u0142\u0143\5f\64\2\u0143E\3\2\2\2\u0144\u0147\5")
        buf.write("H%\2\u0145\u0147\3\2\2\2\u0146\u0144\3\2\2\2\u0146\u0145")
        buf.write("\3\2\2\2\u0147G\3\2\2\2\u0148\u0149\7\17\2\2\u0149\u014a")
        buf.write("\5N(\2\u014a\u014b\5d\63\2\u014b\u014c\5\64\33\2\u014c")
        buf.write("\u014d\5H%\2\u014d\u0154\3\2\2\2\u014e\u014f\7\17\2\2")
        buf.write("\u014f\u0150\5N(\2\u0150\u0151\5d\63\2\u0151\u0152\5\64")
        buf.write("\33\2\u0152\u0154\3\2\2\2\u0153\u0148\3\2\2\2\u0153\u014e")
        buf.write("\3\2\2\2\u0154I\3\2\2\2\u0155\u0158\5L\'\2\u0156\u0158")
        buf.write("\3\2\2\2\u0157\u0155\3\2\2\2\u0157\u0156\3\2\2\2\u0158")
        buf.write("K\3\2\2\2\u0159\u015a\5N(\2\u015a\u015b\7+\2\2\u015b\u015c")
        buf.write("\5L\'\2\u015c\u015f\3\2\2\2\u015d\u015f\5N(\2\u015e\u0159")
        buf.write("\3\2\2\2\u015e\u015d\3\2\2\2\u015fM\3\2\2\2\u0160\u0161")
        buf.write("\5P)\2\u0161\u0162\7&\2\2\u0162\u0163\5P)\2\u0163\u0166")
        buf.write("\3\2\2\2\u0164\u0166\5P)\2\u0165\u0160\3\2\2\2\u0165\u0164")
        buf.write("\3\2\2\2\u0166O\3\2\2\2\u0167\u0168\5R*\2\u0168\u0169")
        buf.write("\t\4\2\2\u0169\u016a\5R*\2\u016a\u016d\3\2\2\2\u016b\u016d")
        buf.write("\5R*\2\u016c\u0167\3\2\2\2\u016c\u016b\3\2\2\2\u016dQ")
        buf.write("\3\2\2\2\u016e\u016f\b*\1\2\u016f\u0170\5T+\2\u0170\u0176")
        buf.write("\3\2\2\2\u0171\u0172\f\4\2\2\u0172\u0173\t\5\2\2\u0173")
        buf.write("\u0175\5T+\2\u0174\u0171\3\2\2\2\u0175\u0178\3\2\2\2\u0176")
        buf.write("\u0174\3\2\2\2\u0176\u0177\3\2\2\2\u0177S\3\2\2\2\u0178")
        buf.write("\u0176\3\2\2\2\u0179\u017a\b+\1\2\u017a\u017b\5V,\2\u017b")
        buf.write("\u0181\3\2\2\2\u017c\u017d\f\4\2\2\u017d\u017e\t\6\2\2")
        buf.write("\u017e\u0180\5V,\2\u017f\u017c\3\2\2\2\u0180\u0183\3\2")
        buf.write("\2\2\u0181\u017f\3\2\2\2\u0181\u0182\3\2\2\2\u0182U\3")
        buf.write("\2\2\2\u0183\u0181\3\2\2\2\u0184\u0185\b,\1\2\u0185\u0186")
        buf.write("\5X-\2\u0186\u018c\3\2\2\2\u0187\u0188\f\4\2\2\u0188\u0189")
        buf.write("\t\7\2\2\u0189\u018b\5X-\2\u018a\u0187\3\2\2\2\u018b\u018e")
        buf.write("\3\2\2\2\u018c\u018a\3\2\2\2\u018c\u018d\3\2\2\2\u018d")
        buf.write("W\3\2\2\2\u018e\u018c\3\2\2\2\u018f\u0190\7\7\2\2\u0190")
        buf.write("\u0193\5X-\2\u0191\u0193\5Z.\2\u0192\u018f\3\2\2\2\u0192")
        buf.write("\u0191\3\2\2\2\u0193Y\3\2\2\2\u0194\u0195\7\32\2\2\u0195")
        buf.write("\u0198\5Z.\2\u0196\u0198\5\\/\2\u0197\u0194\3\2\2\2\u0197")
        buf.write("\u0196\3\2\2\2\u0198[\3\2\2\2\u0199\u019a\7\60\2\2\u019a")
        buf.write("\u019b\7)\2\2\u019b\u019c\5L\'\2\u019c\u019d\7*\2\2\u019d")
        buf.write("\u01a0\3\2\2\2\u019e\u01a0\5^\60\2\u019f\u0199\3\2\2\2")
        buf.write("\u019f\u019e\3\2\2\2\u01a0]\3\2\2\2\u01a1\u01a2\7\60\2")
        buf.write("\2\u01a2\u01a3\7\'\2\2\u01a3\u01a4\5J&\2\u01a4\u01a5\7")
        buf.write("(\2\2\u01a5\u01a8\3\2\2\2\u01a6\u01a8\5`\61\2\u01a7\u01a1")
        buf.write("\3\2\2\2\u01a7\u01a6\3\2\2\2\u01a8_\3\2\2\2\u01a9\u01af")
        buf.write("\7-\2\2\u01aa\u01af\7/\2\2\u01ab\u01af\7.\2\2\u01ac\u01af")
        buf.write("\7\60\2\2\u01ad\u01af\5b\62\2\u01ae\u01a9\3\2\2\2\u01ae")
        buf.write("\u01aa\3\2\2\2\u01ae\u01ab\3\2\2\2\u01ae\u01ac\3\2\2\2")
        buf.write("\u01ae\u01ad\3\2\2\2\u01afa\3\2\2\2\u01b0\u01b1\7\'\2")
        buf.write("\2\u01b1\u01b2\5N(\2\u01b2\u01b3\7(\2\2\u01b3c\3\2\2\2")
        buf.write("\u01b4\u01b7\5f\64\2\u01b5\u01b7\3\2\2\2\u01b6\u01b4\3")
        buf.write("\2\2\2\u01b6\u01b5\3\2\2\2\u01b7e\3\2\2\2\u01b8\u01b9")
        buf.write("\7,\2\2\u01b9\u01bc\5f\64\2\u01ba\u01bc\7,\2\2\u01bb\u01b8")
        buf.write("\3\2\2\2\u01bb\u01ba\3\2\2\2\u01bcg\3\2\2\2*ot|\u008d")
        buf.write("\u0098\u009d\u00a5\u00ad\u00b8\u00bd\u00c3\u00cd\u00d7")
        buf.write("\u00de\u00e7\u00eb\u00ef\u00f5\u00fd\u00ff\u0109\u010f")
        buf.write("\u011c\u012c\u0146\u0153\u0157\u015e\u0165\u016c\u0176")
        buf.write("\u0181\u018c\u0192\u0197\u019f\u01a7\u01ae\u01b6\u01bb")
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
                     "'array'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
                     "'='", "'<-'", "'!='", "'<='", "'>='", "'<'", "'>'", 
                     "'...'", "'('", "')'", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>", "ZCODE_COMMENT", "RETURN", "FOR", "IF", 
                      "NOT", "VAR", "UNTIL", "ELSE", "AND", "NUMBER", "DYNAMIC", 
                      "BY", "ELIF", "OR", "BOOL", "FUNC", "BREAK", "BEGIN", 
                      "STRING", "CONTINUE", "END", "ARRAY", "PLUS", "MINUS", 
                      "TIMES", "DIVIDED", "MOD", "COMPARE", "EQUAL", "ASSIGN", 
                      "NOT_EQUAL", "LTOE", "GTOE", "LT", "GT", "CONCATENATION", 
                      "LEFTPAREN", "RIGHTPAREN", "LEFTBRACKET", "RIGHTBRACKET", 
                      "COMMA", "NL", "NUMBER_LITERAL", "BOOLEAN_LITERAL", 
                      "STRING_LITERAL", "IDENTIFIER", "WS", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decllist = 1
    RULE_decl = 2
    RULE_primitype = 3
    RULE_implitype = 4
    RULE_arraytype = 5
    RULE_vararraytype = 6
    RULE_sizelist = 7
    RULE_array = 8
    RULE_listofArray = 9
    RULE_arrayvalue = 10
    RULE_vardecl = 11
    RULE_vardecl1 = 12
    RULE_vardecl2 = 13
    RULE_vardecl3 = 14
    RULE_vardecl4 = 15
    RULE_initval = 16
    RULE_funcdecl = 17
    RULE_paramdecl = 18
    RULE_paramlist = 19
    RULE_paramprime = 20
    RULE_param = 21
    RULE_bodyfunc = 22
    RULE_stmtlist = 23
    RULE_stmtprime = 24
    RULE_stmt = 25
    RULE_forstmt = 26
    RULE_assignstmt = 27
    RULE_ifstmt = 28
    RULE_breakstmt = 29
    RULE_continuestmt = 30
    RULE_returnstmt = 31
    RULE_funstmt = 32
    RULE_blockstmt = 33
    RULE_elstmt = 34
    RULE_elprime = 35
    RULE_exprlist = 36
    RULE_exprprime = 37
    RULE_expr0 = 38
    RULE_expr1 = 39
    RULE_expr2 = 40
    RULE_expr3 = 41
    RULE_expr4 = 42
    RULE_expr5 = 43
    RULE_expr6 = 44
    RULE_expr7 = 45
    RULE_expr8 = 46
    RULE_expr9 = 47
    RULE_expr10 = 48
    RULE_nllist = 49
    RULE_nlprime = 50

    ruleNames =  [ "program", "decllist", "decl", "primitype", "implitype", 
                   "arraytype", "vararraytype", "sizelist", "array", "listofArray", 
                   "arrayvalue", "vardecl", "vardecl1", "vardecl2", "vardecl3", 
                   "vardecl4", "initval", "funcdecl", "paramdecl", "paramlist", 
                   "paramprime", "param", "bodyfunc", "stmtlist", "stmtprime", 
                   "stmt", "forstmt", "assignstmt", "ifstmt", "breakstmt", 
                   "continuestmt", "returnstmt", "funstmt", "blockstmt", 
                   "elstmt", "elprime", "exprlist", "exprprime", "expr0", 
                   "expr1", "expr2", "expr3", "expr4", "expr5", "expr6", 
                   "expr7", "expr8", "expr9", "expr10", "nllist", "nlprime" ]

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
    COMPARE=28
    EQUAL=29
    ASSIGN=30
    NOT_EQUAL=31
    LTOE=32
    GTOE=33
    LT=34
    GT=35
    CONCATENATION=36
    LEFTPAREN=37
    RIGHTPAREN=38
    LEFTBRACKET=39
    RIGHTBRACKET=40
    COMMA=41
    NL=42
    NUMBER_LITERAL=43
    BOOLEAN_LITERAL=44
    STRING_LITERAL=45
    IDENTIFIER=46
    WS=47
    UNCLOSE_STRING=48
    ILLEGAL_ESCAPE=49
    ERROR_CHAR=50

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
            self.state = 102
            self.decllist()
            self.state = 103
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
            self.state = 109
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.decl()
                self.state = 106
                self.decllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 108
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


        def NL(self):
            return self.getToken(ZCodeParser.NL, 0)

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
            self.state = 114
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.VAR, ZCodeParser.NUMBER, ZCodeParser.DYNAMIC, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.vardecl()
                pass
            elif token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 112
                self.funcdecl()
                pass
            elif token in [ZCodeParser.NL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 113
                self.match(ZCodeParser.NL)
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
            self.state = 116
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
            self.state = 118
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

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LEFTBRACKET(self):
            return self.getToken(ZCodeParser.LEFTBRACKET, 0)

        def sizelist(self):
            return self.getTypedRuleContext(ZCodeParser.SizelistContext,0)


        def RIGHTBRACKET(self):
            return self.getToken(ZCodeParser.RIGHTBRACKET, 0)

        def primitype(self):
            return self.getTypedRuleContext(ZCodeParser.PrimitypeContext,0)


        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

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
            self.state = 122
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.state = 120
                self.primitype()
                pass
            elif token in [ZCodeParser.DYNAMIC]:
                self.state = 121
                self.match(ZCodeParser.DYNAMIC)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 124
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 125
            self.match(ZCodeParser.LEFTBRACKET)
            self.state = 126
            self.sizelist()
            self.state = 127
            self.match(ZCodeParser.RIGHTBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VararraytypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LEFTBRACKET(self):
            return self.getToken(ZCodeParser.LEFTBRACKET, 0)

        def sizelist(self):
            return self.getTypedRuleContext(ZCodeParser.SizelistContext,0)


        def RIGHTBRACKET(self):
            return self.getToken(ZCodeParser.RIGHTBRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_vararraytype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVararraytype" ):
                return visitor.visitVararraytype(self)
            else:
                return visitor.visitChildren(self)




    def vararraytype(self):

        localctx = ZCodeParser.VararraytypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_vararraytype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(ZCodeParser.VAR)
            self.state = 130
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 131
            self.match(ZCodeParser.LEFTBRACKET)
            self.state = 132
            self.sizelist()
            self.state = 133
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
        self.enterRule(localctx, 14, self.RULE_sizelist)
        try:
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.match(ZCodeParser.NUMBER_LITERAL)
                self.state = 136
                self.match(ZCodeParser.COMMA)
                self.state = 137
                self.sizelist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
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
        self.enterRule(localctx, 16, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(ZCodeParser.LEFTBRACKET)

            self.state = 142
            self.exprprime()
            self.state = 143
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
        self.enterRule(localctx, 18, self.RULE_listofArray)
        try:
            self.state = 150
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.array()
                self.state = 146
                self.match(ZCodeParser.COMMA)
                self.state = 147
                self.listofArray()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
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

        def RIGHTBRACKET(self):
            return self.getToken(ZCodeParser.RIGHTBRACKET, 0)

        def listofArray(self):
            return self.getTypedRuleContext(ZCodeParser.ListofArrayContext,0)


        def exprprime(self):
            return self.getTypedRuleContext(ZCodeParser.ExprprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayvalue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayvalue" ):
                return visitor.visitArrayvalue(self)
            else:
                return visitor.visitChildren(self)




    def arrayvalue(self):

        localctx = ZCodeParser.ArrayvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_arrayvalue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(ZCodeParser.LEFTBRACKET)
            self.state = 155
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.LEFTBRACKET]:
                self.state = 153
                self.listofArray()
                pass
            elif token in [ZCodeParser.NOT, ZCodeParser.MINUS, ZCodeParser.LEFTPAREN, ZCodeParser.NUMBER_LITERAL, ZCodeParser.BOOLEAN_LITERAL, ZCodeParser.STRING_LITERAL, ZCodeParser.IDENTIFIER]:
                self.state = 154
                self.exprprime()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 157
            self.match(ZCodeParser.RIGHTBRACKET)
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

        def nllist(self):
            return self.getTypedRuleContext(ZCodeParser.NllistContext,0)


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
        self.enterRule(localctx, 22, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 159
                self.vardecl1()
                pass

            elif la_ == 2:
                self.state = 160
                self.vardecl2()
                pass

            elif la_ == 3:
                self.state = 161
                self.vardecl3()
                pass

            elif la_ == 4:
                self.state = 162
                self.vardecl4()
                pass


            self.state = 165
            self.nllist()
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
        self.enterRule(localctx, 24, self.RULE_vardecl1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.primitype()
            self.state = 168
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 169
                self.match(ZCodeParser.ASSIGN)
                self.state = 170
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
        self.enterRule(localctx, 26, self.RULE_vardecl2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(ZCodeParser.VAR)
            self.state = 174
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 175
            self.match(ZCodeParser.ASSIGN)
            self.state = 176
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
        self.enterRule(localctx, 28, self.RULE_vardecl3)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(ZCodeParser.DYNAMIC)
            self.state = 179
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 180
                self.match(ZCodeParser.ASSIGN)
                self.state = 181
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


        def vararraytype(self):
            return self.getTypedRuleContext(ZCodeParser.VararraytypeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_vardecl4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl4" ):
                return visitor.visitVardecl4(self)
            else:
                return visitor.visitChildren(self)




    def vardecl4(self):

        localctx = ZCodeParser.Vardecl4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_vardecl4)
        self._la = 0 # Token type
        try:
            self.state = 193
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.DYNAMIC, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.arraytype()
                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.ASSIGN:
                    self.state = 185
                    self.match(ZCodeParser.ASSIGN)
                    self.state = 186
                    self.arrayvalue()


                pass
            elif token in [ZCodeParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                self.vararraytype()

                self.state = 190
                self.match(ZCodeParser.ASSIGN)
                self.state = 191
                self.arrayvalue()
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
        self.enterRule(localctx, 32, self.RULE_initval)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
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


        def nllist(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.NllistContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.NllistContext,i)


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
        self.enterRule(localctx, 34, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(ZCodeParser.FUNC)
            self.state = 198
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 199
            self.paramdecl()
            self.state = 200
            self.nllist()
            self.state = 203
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN, ZCodeParser.BEGIN]:
                self.state = 201
                self.bodyfunc()
                pass
            elif token in [ZCodeParser.EOF, ZCodeParser.VAR, ZCodeParser.NUMBER, ZCodeParser.DYNAMIC, ZCodeParser.BOOL, ZCodeParser.FUNC, ZCodeParser.STRING, ZCodeParser.NL]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 205
            self.nllist()
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
        self.enterRule(localctx, 36, self.RULE_paramdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(ZCodeParser.LEFTPAREN)
            self.state = 208
            self.paramlist()
            self.state = 209
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
        self.enterRule(localctx, 38, self.RULE_paramlist)
        try:
            self.state = 213
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
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
        self.enterRule(localctx, 40, self.RULE_paramprime)
        try:
            self.state = 220
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.param()
                self.state = 216
                self.match(ZCodeParser.COMMA)
                self.state = 217
                self.paramprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 219
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
        self.enterRule(localctx, 42, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.primitype()
            self.state = 229
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 223
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 224
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 225
                self.match(ZCodeParser.LEFTBRACKET)
                self.state = 226
                self.exprprime()
                self.state = 227
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
        self.enterRule(localctx, 44, self.RULE_bodyfunc)
        try:
            self.state = 233
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.returnstmt()
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 232
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
        self.enterRule(localctx, 46, self.RULE_stmtlist)
        try:
            self.state = 237
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN, ZCodeParser.FOR, ZCodeParser.IF, ZCodeParser.VAR, ZCodeParser.NUMBER, ZCodeParser.DYNAMIC, ZCodeParser.BOOL, ZCodeParser.BREAK, ZCodeParser.BEGIN, ZCodeParser.STRING, ZCodeParser.CONTINUE, ZCodeParser.LEFTPAREN, ZCodeParser.NUMBER_LITERAL, ZCodeParser.BOOLEAN_LITERAL, ZCodeParser.STRING_LITERAL, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
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


        def nlprime(self):
            return self.getTypedRuleContext(ZCodeParser.NlprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmtprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtprime" ):
                return visitor.visitStmtprime(self)
            else:
                return visitor.visitChildren(self)




    def stmtprime(self):

        localctx = ZCodeParser.StmtprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_stmtprime)
        try:
            self.state = 253
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.RETURN, ZCodeParser.FOR, ZCodeParser.IF, ZCodeParser.BREAK, ZCodeParser.BEGIN, ZCodeParser.CONTINUE, ZCodeParser.LEFTPAREN, ZCodeParser.NUMBER_LITERAL, ZCodeParser.BOOLEAN_LITERAL, ZCodeParser.STRING_LITERAL, ZCodeParser.IDENTIFIER]:
                    self.state = 239
                    self.stmt()
                    pass
                elif token in [ZCodeParser.VAR, ZCodeParser.NUMBER, ZCodeParser.DYNAMIC, ZCodeParser.BOOL, ZCodeParser.STRING]:
                    self.state = 240
                    self.vardecl()
                    self.state = 241
                    self.nlprime()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 245
                self.stmtprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 251
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.RETURN, ZCodeParser.FOR, ZCodeParser.IF, ZCodeParser.BREAK, ZCodeParser.BEGIN, ZCodeParser.CONTINUE, ZCodeParser.LEFTPAREN, ZCodeParser.NUMBER_LITERAL, ZCodeParser.BOOLEAN_LITERAL, ZCodeParser.STRING_LITERAL, ZCodeParser.IDENTIFIER]:
                    self.state = 247
                    self.stmt()
                    pass
                elif token in [ZCodeParser.VAR, ZCodeParser.NUMBER, ZCodeParser.DYNAMIC, ZCodeParser.BOOL, ZCodeParser.STRING]:
                    self.state = 248
                    self.vardecl()
                    self.state = 249
                    self.nlprime()
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
        self.enterRule(localctx, 50, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 255
                self.assignstmt()
                pass

            elif la_ == 2:
                self.state = 256
                self.forstmt()
                pass

            elif la_ == 3:
                self.state = 257
                self.ifstmt()
                pass

            elif la_ == 4:
                self.state = 258
                self.breakstmt()
                pass

            elif la_ == 5:
                self.state = 259
                self.continuestmt()
                pass

            elif la_ == 6:
                self.state = 260
                self.returnstmt()
                pass

            elif la_ == 7:
                self.state = 261
                self.funstmt()
                pass

            elif la_ == 8:
                self.state = 262
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

        def nllist(self):
            return self.getTypedRuleContext(ZCodeParser.NllistContext,0)


        def stmtprime(self):
            return self.getTypedRuleContext(ZCodeParser.StmtprimeContext,0)


        def exprlist(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprlistContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprlistContext,i)


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
        self.enterRule(localctx, 52, self.RULE_forstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(ZCodeParser.FOR)
            self.state = 266
            self.match(ZCodeParser.IDENTIFIER)

            self.state = 267
            self.exprlist()

            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 268
                self.match(ZCodeParser.ASSIGN)


            self.state = 271
            self.exprlist()
            self.state = 273
            self.match(ZCodeParser.UNTIL)
            self.state = 274
            self.exprprime()
            self.state = 275
            self.match(ZCodeParser.BY)
            self.state = 276
            self.exprprime()
            self.state = 277
            self.nllist()
            self.state = 278
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

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def exprprime(self):
            return self.getTypedRuleContext(ZCodeParser.ExprprimeContext,0)


        def nlprime(self):
            return self.getTypedRuleContext(ZCodeParser.NlprimeContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def expr7(self):
            return self.getTypedRuleContext(ZCodeParser.Expr7Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assignstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignstmt" ):
                return visitor.visitAssignstmt(self)
            else:
                return visitor.visitChildren(self)




    def assignstmt(self):

        localctx = ZCodeParser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 280
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 281
                self.expr7()
                pass


            self.state = 284
            self.match(ZCodeParser.ASSIGN)
            self.state = 285
            self.exprprime()
            self.state = 286
            self.nlprime()
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

        def elstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ElstmtContext,0)


        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def expr0(self):
            return self.getTypedRuleContext(ZCodeParser.Expr0Context,0)


        def nllist(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.NllistContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.NllistContext,i)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.StmtContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.StmtContext,i)


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
        self.enterRule(localctx, 56, self.RULE_ifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.match(ZCodeParser.IF)
            self.state = 289
            self.expr0()
            self.state = 290
            self.nllist()
            self.state = 291
            self.stmt()
            self.state = 293
            self.elstmt()
            self.state = 298
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 294
                self.match(ZCodeParser.ELSE)
                self.state = 295
                self.nllist()
                self.state = 296
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

        def nlprime(self):
            return self.getTypedRuleContext(ZCodeParser.NlprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_breakstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakstmt" ):
                return visitor.visitBreakstmt(self)
            else:
                return visitor.visitChildren(self)




    def breakstmt(self):

        localctx = ZCodeParser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(ZCodeParser.BREAK)
            self.state = 301
            self.nlprime()
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

        def nlprime(self):
            return self.getTypedRuleContext(ZCodeParser.NlprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_continuestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinuestmt" ):
                return visitor.visitContinuestmt(self)
            else:
                return visitor.visitChildren(self)




    def continuestmt(self):

        localctx = ZCodeParser.ContinuestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(ZCodeParser.CONTINUE)
            self.state = 304
            self.nlprime()
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


        def nlprime(self):
            return self.getTypedRuleContext(ZCodeParser.NlprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_returnstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstmt" ):
                return visitor.visitReturnstmt(self)
            else:
                return visitor.visitChildren(self)




    def returnstmt(self):

        localctx = ZCodeParser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_returnstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.match(ZCodeParser.RETURN)
            self.state = 307
            self.exprlist()
            self.state = 308
            self.nlprime()
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

        def nlprime(self):
            return self.getTypedRuleContext(ZCodeParser.NlprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_funstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunstmt" ):
                return visitor.visitFunstmt(self)
            else:
                return visitor.visitChildren(self)




    def funstmt(self):

        localctx = ZCodeParser.FunstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_funstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 311
            self.match(ZCodeParser.LEFTPAREN)
            self.state = 312
            self.exprlist()
            self.state = 313
            self.match(ZCodeParser.RIGHTPAREN)
            self.state = 314
            self.nlprime()
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

        def nlprime(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.NlprimeContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.NlprimeContext,i)


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
        self.enterRule(localctx, 66, self.RULE_blockstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.match(ZCodeParser.BEGIN)
            self.state = 317
            self.nlprime()
            self.state = 318
            self.stmtlist()
            self.state = 319
            self.match(ZCodeParser.END)
            self.state = 320
            self.nlprime()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elprime(self):
            return self.getTypedRuleContext(ZCodeParser.ElprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElstmt" ):
                return visitor.visitElstmt(self)
            else:
                return visitor.visitChildren(self)




    def elstmt(self):

        localctx = ZCodeParser.ElstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_elstmt)
        try:
            self.state = 324
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 322
                self.elprime()
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


    class ElprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def expr0(self):
            return self.getTypedRuleContext(ZCodeParser.Expr0Context,0)


        def nllist(self):
            return self.getTypedRuleContext(ZCodeParser.NllistContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def elprime(self):
            return self.getTypedRuleContext(ZCodeParser.ElprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElprime" ):
                return visitor.visitElprime(self)
            else:
                return visitor.visitChildren(self)




    def elprime(self):

        localctx = ZCodeParser.ElprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_elprime)
        try:
            self.state = 337
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 326
                self.match(ZCodeParser.ELIF)
                self.state = 327
                self.expr0()
                self.state = 328
                self.nllist()
                self.state = 329
                self.stmt()
                self.state = 330
                self.elprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 332
                self.match(ZCodeParser.ELIF)
                self.state = 333
                self.expr0()
                self.state = 334
                self.nllist()
                self.state = 335
                self.stmt()
                pass


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
        self.enterRule(localctx, 72, self.RULE_exprlist)
        try:
            self.state = 341
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 339
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
        self.enterRule(localctx, 74, self.RULE_exprprime)
        try:
            self.state = 348
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 343
                self.expr0()
                self.state = 344
                self.match(ZCodeParser.COMMA)
                self.state = 345
                self.exprprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 347
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
        self.enterRule(localctx, 76, self.RULE_expr0)
        try:
            self.state = 355
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 350
                self.expr1()
                self.state = 351
                self.match(ZCodeParser.CONCATENATION)
                self.state = 352
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 354
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
        self.enterRule(localctx, 78, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 362
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 357
                self.expr2(0)
                self.state = 358
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.COMPARE) | (1 << ZCodeParser.EQUAL) | (1 << ZCodeParser.NOT_EQUAL) | (1 << ZCodeParser.LTOE) | (1 << ZCodeParser.GTOE) | (1 << ZCodeParser.LT) | (1 << ZCodeParser.GT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 359
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 361
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
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 372
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 367
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 368
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 369
                    self.expr3(0) 
                self.state = 374
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

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
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 383
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 378
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 379
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.PLUS or _la==ZCodeParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 380
                    self.expr4(0) 
                self.state = 385
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

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
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 394
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 389
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 390
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TIMES) | (1 << ZCodeParser.DIVIDED) | (1 << ZCodeParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 391
                    self.expr5() 
                self.state = 396
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

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
        self.enterRule(localctx, 86, self.RULE_expr5)
        try:
            self.state = 400
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 397
                self.match(ZCodeParser.NOT)
                self.state = 398
                self.expr5()
                pass
            elif token in [ZCodeParser.MINUS, ZCodeParser.LEFTPAREN, ZCodeParser.NUMBER_LITERAL, ZCodeParser.BOOLEAN_LITERAL, ZCodeParser.STRING_LITERAL, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 399
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
        self.enterRule(localctx, 88, self.RULE_expr6)
        try:
            self.state = 405
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 402
                self.match(ZCodeParser.MINUS)
                self.state = 403
                self.expr6()
                pass
            elif token in [ZCodeParser.LEFTPAREN, ZCodeParser.NUMBER_LITERAL, ZCodeParser.BOOLEAN_LITERAL, ZCodeParser.STRING_LITERAL, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 404
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
        self.enterRule(localctx, 90, self.RULE_expr7)
        try:
            self.state = 413
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 407
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 408
                self.match(ZCodeParser.LEFTBRACKET)
                self.state = 409
                self.exprprime()
                self.state = 410
                self.match(ZCodeParser.RIGHTBRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 412
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
        self.enterRule(localctx, 92, self.RULE_expr8)
        try:
            self.state = 421
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 415
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 416
                self.match(ZCodeParser.LEFTPAREN)
                self.state = 417
                self.exprlist()
                self.state = 418
                self.match(ZCodeParser.RIGHTPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 420
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
        self.enterRule(localctx, 94, self.RULE_expr9)
        try:
            self.state = 428
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 423
                self.match(ZCodeParser.NUMBER_LITERAL)
                pass
            elif token in [ZCodeParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 424
                self.match(ZCodeParser.STRING_LITERAL)
                pass
            elif token in [ZCodeParser.BOOLEAN_LITERAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 425
                self.match(ZCodeParser.BOOLEAN_LITERAL)
                pass
            elif token in [ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 4)
                self.state = 426
                self.match(ZCodeParser.IDENTIFIER)
                pass
            elif token in [ZCodeParser.LEFTPAREN]:
                self.enterOuterAlt(localctx, 5)
                self.state = 427
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
        self.enterRule(localctx, 96, self.RULE_expr10)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 430
            self.match(ZCodeParser.LEFTPAREN)
            self.state = 431
            self.expr0()
            self.state = 432
            self.match(ZCodeParser.RIGHTPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NllistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nlprime(self):
            return self.getTypedRuleContext(ZCodeParser.NlprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_nllist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNllist" ):
                return visitor.visitNllist(self)
            else:
                return visitor.visitChildren(self)




    def nllist(self):

        localctx = ZCodeParser.NllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_nllist)
        try:
            self.state = 436
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 434
                self.nlprime()
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


    class NlprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NL(self):
            return self.getToken(ZCodeParser.NL, 0)

        def nlprime(self):
            return self.getTypedRuleContext(ZCodeParser.NlprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_nlprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNlprime" ):
                return visitor.visitNlprime(self)
            else:
                return visitor.visitChildren(self)




    def nlprime(self):

        localctx = ZCodeParser.NlprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_nlprime)
        try:
            self.state = 441
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 438
                self.match(ZCodeParser.NL)
                self.state = 439
                self.nlprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 440
                self.match(ZCodeParser.NL)
                pass


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
        self._predicates[40] = self.expr2_sempred
        self._predicates[41] = self.expr3_sempred
        self._predicates[42] = self.expr4_sempred
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
         




