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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\63")
        buf.write("\u01bc\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\3\2\3\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\5\3o\n\3\3\4\3\4\5\4s\n\4\3\5\3")
        buf.write("\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\5\b")
        buf.write("\u0083\n\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\5\n\u008e")
        buf.write("\n\n\3\13\3\13\3\13\5\13\u0093\n\13\3\13\3\13\3\f\3\f")
        buf.write("\3\f\3\f\5\f\u009b\n\f\3\f\3\f\3\r\3\r\3\r\3\r\5\r\u00a3")
        buf.write("\n\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\5\17")
        buf.write("\u00ae\n\17\3\20\3\20\3\20\5\20\u00b3\n\20\3\21\3\21\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u00be\n\22\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\5\24\u00c6\n\24\3\25\3\25\3")
        buf.write("\25\3\25\3\25\5\25\u00cd\n\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\5\26\u00d6\n\26\3\27\3\27\5\27\u00da\n\27\3")
        buf.write("\30\3\30\5\30\u00de\n\30\3\31\3\31\3\31\3\31\5\31\u00e4")
        buf.write("\n\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u00ec\n\31\5")
        buf.write("\31\u00ee\n\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\5\32\u00f9\n\32\3\33\3\33\3\33\3\33\5\33\u00ff\n")
        buf.write("\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\5\34\u010e\n\34\3\34\3\34\3\34\3\34\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\5\35\u0120\n\35\3\36\3\36\3\36\3\37\3\37\3\37\3")
        buf.write(" \3 \3 \3 \3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("#\3#\5#\u013a\n#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3")
        buf.write("$\3$\3$\5$\u014b\n$\3%\3%\5%\u014f\n%\3&\3&\3&\3&\3&\5")
        buf.write("&\u0156\n&\3\'\3\'\3\'\3\'\3\'\5\'\u015d\n\'\3(\3(\3(")
        buf.write("\3(\3(\5(\u0164\n(\3)\3)\3)\3)\3)\3)\7)\u016c\n)\f)\16")
        buf.write(")\u016f\13)\3*\3*\3*\3*\3*\3*\7*\u0177\n*\f*\16*\u017a")
        buf.write("\13*\3+\3+\3+\3+\3+\3+\7+\u0182\n+\f+\16+\u0185\13+\3")
        buf.write(",\3,\3,\5,\u018a\n,\3-\3-\3-\5-\u018f\n-\3.\3.\3.\3.\3")
        buf.write(".\5.\u0196\n.\3.\3.\3.\3.\3.\5.\u019d\n.\3/\3/\3/\3/\3")
        buf.write("/\3/\5/\u01a5\n/\3\60\3\60\3\60\3\60\3\60\3\60\5\60\u01ad")
        buf.write("\n\60\3\61\3\61\3\61\3\61\3\62\3\62\5\62\u01b5\n\62\3")
        buf.write("\63\3\63\3\63\5\63\u01ba\n\63\3\63\2\5PRT\64\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<")
        buf.write(">@BDFHJLNPRTVXZ\\^`bd\2\b\5\2\r\r\22\22\26\26\4\2\t\t")
        buf.write("\16\16\4\2\36\37!%\4\2\f\f\21\21\3\2\31\32\3\2\33\35\2")
        buf.write("\u01bd\2f\3\2\2\2\4n\3\2\2\2\6r\3\2\2\2\bt\3\2\2\2\nv")
        buf.write("\3\2\2\2\fx\3\2\2\2\16\u0082\3\2\2\2\20\u0084\3\2\2\2")
        buf.write("\22\u008d\3\2\2\2\24\u008f\3\2\2\2\26\u009a\3\2\2\2\30")
        buf.write("\u009e\3\2\2\2\32\u00a4\3\2\2\2\34\u00a9\3\2\2\2\36\u00af")
        buf.write("\3\2\2\2 \u00b4\3\2\2\2\"\u00b6\3\2\2\2$\u00bf\3\2\2\2")
        buf.write("&\u00c5\3\2\2\2(\u00cc\3\2\2\2*\u00ce\3\2\2\2,\u00d9\3")
        buf.write("\2\2\2.\u00dd\3\2\2\2\60\u00ed\3\2\2\2\62\u00f8\3\2\2")
        buf.write("\2\64\u00fa\3\2\2\2\66\u010d\3\2\2\28\u0113\3\2\2\2:\u0121")
        buf.write("\3\2\2\2<\u0124\3\2\2\2>\u0127\3\2\2\2@\u012b\3\2\2\2")
        buf.write("B\u0131\3\2\2\2D\u0139\3\2\2\2F\u014a\3\2\2\2H\u014e\3")
        buf.write("\2\2\2J\u0155\3\2\2\2L\u015c\3\2\2\2N\u0163\3\2\2\2P\u0165")
        buf.write("\3\2\2\2R\u0170\3\2\2\2T\u017b\3\2\2\2V\u0189\3\2\2\2")
        buf.write("X\u018e\3\2\2\2Z\u019c\3\2\2\2\\\u01a4\3\2\2\2^\u01ac")
        buf.write("\3\2\2\2`\u01ae\3\2\2\2b\u01b4\3\2\2\2d\u01b9\3\2\2\2")
        buf.write("fg\5b\62\2gh\5\4\3\2hi\7\2\2\3i\3\3\2\2\2jk\5\6\4\2kl")
        buf.write("\5\4\3\2lo\3\2\2\2mo\5\6\4\2nj\3\2\2\2nm\3\2\2\2o\5\3")
        buf.write("\2\2\2ps\5\26\f\2qs\5\"\22\2rp\3\2\2\2rq\3\2\2\2s\7\3")
        buf.write("\2\2\2tu\t\2\2\2u\t\3\2\2\2vw\t\3\2\2w\13\3\2\2\2xy\5")
        buf.write("\b\5\2yz\7/\2\2z{\7)\2\2{|\5\16\b\2|}\7*\2\2}\r\3\2\2")
        buf.write("\2~\177\7-\2\2\177\u0080\7+\2\2\u0080\u0083\5\16\b\2\u0081")
        buf.write("\u0083\7-\2\2\u0082~\3\2\2\2\u0082\u0081\3\2\2\2\u0083")
        buf.write("\17\3\2\2\2\u0084\u0085\7)\2\2\u0085\u0086\5J&\2\u0086")
        buf.write("\u0087\7*\2\2\u0087\21\3\2\2\2\u0088\u0089\5\20\t\2\u0089")
        buf.write("\u008a\7+\2\2\u008a\u008b\5\22\n\2\u008b\u008e\3\2\2\2")
        buf.write("\u008c\u008e\5\20\t\2\u008d\u0088\3\2\2\2\u008d\u008c")
        buf.write("\3\2\2\2\u008e\23\3\2\2\2\u008f\u0092\7)\2\2\u0090\u0093")
        buf.write("\5\22\n\2\u0091\u0093\5J&\2\u0092\u0090\3\2\2\2\u0092")
        buf.write("\u0091\3\2\2\2\u0093\u0094\3\2\2\2\u0094\u0095\7*\2\2")
        buf.write("\u0095\25\3\2\2\2\u0096\u009b\5\30\r\2\u0097\u009b\5\32")
        buf.write("\16\2\u0098\u009b\5\34\17\2\u0099\u009b\5\36\20\2\u009a")
        buf.write("\u0096\3\2\2\2\u009a\u0097\3\2\2\2\u009a\u0098\3\2\2\2")
        buf.write("\u009a\u0099\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u009d\5")
        buf.write("d\63\2\u009d\27\3\2\2\2\u009e\u009f\5\b\5\2\u009f\u00a2")
        buf.write("\7/\2\2\u00a0\u00a1\7 \2\2\u00a1\u00a3\5 \21\2\u00a2\u00a0")
        buf.write("\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\31\3\2\2\2\u00a4\u00a5")
        buf.write("\7\t\2\2\u00a5\u00a6\7/\2\2\u00a6\u00a7\7 \2\2\u00a7\u00a8")
        buf.write("\5 \21\2\u00a8\33\3\2\2\2\u00a9\u00aa\7\16\2\2\u00aa\u00ad")
        buf.write("\7/\2\2\u00ab\u00ac\7 \2\2\u00ac\u00ae\5 \21\2\u00ad\u00ab")
        buf.write("\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\35\3\2\2\2\u00af\u00b2")
        buf.write("\5\f\7\2\u00b0\u00b1\7 \2\2\u00b1\u00b3\5\24\13\2\u00b2")
        buf.write("\u00b0\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\37\3\2\2\2\u00b4")
        buf.write("\u00b5\5H%\2\u00b5!\3\2\2\2\u00b6\u00b7\7\23\2\2\u00b7")
        buf.write("\u00b8\7/\2\2\u00b8\u00bd\5$\23\2\u00b9\u00ba\5b\62\2")
        buf.write("\u00ba\u00bb\5,\27\2\u00bb\u00be\3\2\2\2\u00bc\u00be\5")
        buf.write("d\63\2\u00bd\u00b9\3\2\2\2\u00bd\u00bc\3\2\2\2\u00be#")
        buf.write("\3\2\2\2\u00bf\u00c0\7\'\2\2\u00c0\u00c1\5&\24\2\u00c1")
        buf.write("\u00c2\7(\2\2\u00c2%\3\2\2\2\u00c3\u00c6\5(\25\2\u00c4")
        buf.write("\u00c6\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c5\u00c4\3\2\2\2")
        buf.write("\u00c6\'\3\2\2\2\u00c7\u00c8\5*\26\2\u00c8\u00c9\7+\2")
        buf.write("\2\u00c9\u00ca\5(\25\2\u00ca\u00cd\3\2\2\2\u00cb\u00cd")
        buf.write("\5*\26\2\u00cc\u00c7\3\2\2\2\u00cc\u00cb\3\2\2\2\u00cd")
        buf.write(")\3\2\2\2\u00ce\u00d5\5\b\5\2\u00cf\u00d6\7/\2\2\u00d0")
        buf.write("\u00d1\7/\2\2\u00d1\u00d2\7)\2\2\u00d2\u00d3\5J&\2\u00d3")
        buf.write("\u00d4\7*\2\2\u00d4\u00d6\3\2\2\2\u00d5\u00cf\3\2\2\2")
        buf.write("\u00d5\u00d0\3\2\2\2\u00d6+\3\2\2\2\u00d7\u00da\5> \2")
        buf.write("\u00d8\u00da\5B\"\2\u00d9\u00d7\3\2\2\2\u00d9\u00d8\3")
        buf.write("\2\2\2\u00da-\3\2\2\2\u00db\u00de\5\60\31\2\u00dc\u00de")
        buf.write("\3\2\2\2\u00dd\u00db\3\2\2\2\u00dd\u00dc\3\2\2\2\u00de")
        buf.write("/\3\2\2\2\u00df\u00e4\5\62\32\2\u00e0\u00e1\5\26\f\2\u00e1")
        buf.write("\u00e2\5d\63\2\u00e2\u00e4\3\2\2\2\u00e3\u00df\3\2\2\2")
        buf.write("\u00e3\u00e0\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\u00e6\5")
        buf.write("\60\31\2\u00e6\u00ee\3\2\2\2\u00e7\u00ec\5\62\32\2\u00e8")
        buf.write("\u00e9\5\26\f\2\u00e9\u00ea\5d\63\2\u00ea\u00ec\3\2\2")
        buf.write("\2\u00eb\u00e7\3\2\2\2\u00eb\u00e8\3\2\2\2\u00ec\u00ee")
        buf.write("\3\2\2\2\u00ed\u00e3\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ee")
        buf.write("\61\3\2\2\2\u00ef\u00f9\5\66\34\2\u00f0\u00f9\5\64\33")
        buf.write("\2\u00f1\u00f9\58\35\2\u00f2\u00f9\5:\36\2\u00f3\u00f9")
        buf.write("\5<\37\2\u00f4\u00f9\5> \2\u00f5\u00f9\5@!\2\u00f6\u00f9")
        buf.write("\5B\"\2\u00f7\u00f9\5\26\f\2\u00f8\u00ef\3\2\2\2\u00f8")
        buf.write("\u00f0\3\2\2\2\u00f8\u00f1\3\2\2\2\u00f8\u00f2\3\2\2\2")
        buf.write("\u00f8\u00f3\3\2\2\2\u00f8\u00f4\3\2\2\2\u00f8\u00f5\3")
        buf.write("\2\2\2\u00f8\u00f6\3\2\2\2\u00f8\u00f7\3\2\2\2\u00f9\63")
        buf.write("\3\2\2\2\u00fa\u00fb\7\6\2\2\u00fb\u00fe\7/\2\2\u00fc")
        buf.write("\u00fd\7 \2\2\u00fd\u00ff\5H%\2\u00fe\u00fc\3\2\2\2\u00fe")
        buf.write("\u00ff\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\u0101\7\n\2\2")
        buf.write("\u0101\u0102\5J&\2\u0102\u0103\7\17\2\2\u0103\u0104\5")
        buf.write("J&\2\u0104\u0105\5b\62\2\u0105\u0106\5\60\31\2\u0106\65")
        buf.write("\3\2\2\2\u0107\u010e\7/\2\2\u0108\u0109\7/\2\2\u0109\u010a")
        buf.write("\7)\2\2\u010a\u010b\5J&\2\u010b\u010c\7*\2\2\u010c\u010e")
        buf.write("\3\2\2\2\u010d\u0107\3\2\2\2\u010d\u0108\3\2\2\2\u010e")
        buf.write("\u010f\3\2\2\2\u010f\u0110\7 \2\2\u0110\u0111\5J&\2\u0111")
        buf.write("\u0112\5d\63\2\u0112\67\3\2\2\2\u0113\u0114\7\7\2\2\u0114")
        buf.write("\u0115\7\'\2\2\u0115\u0116\5L\'\2\u0116\u0117\7(\2\2\u0117")
        buf.write("\u0118\5b\62\2\u0118\u0119\5\62\32\2\u0119\u011a\3\2\2")
        buf.write("\2\u011a\u011f\5D#\2\u011b\u011c\7\13\2\2\u011c\u011d")
        buf.write("\5b\62\2\u011d\u011e\5\62\32\2\u011e\u0120\3\2\2\2\u011f")
        buf.write("\u011b\3\2\2\2\u011f\u0120\3\2\2\2\u01209\3\2\2\2\u0121")
        buf.write("\u0122\7\24\2\2\u0122\u0123\5d\63\2\u0123;\3\2\2\2\u0124")
        buf.write("\u0125\7\27\2\2\u0125\u0126\5d\63\2\u0126=\3\2\2\2\u0127")
        buf.write("\u0128\7\5\2\2\u0128\u0129\5H%\2\u0129\u012a\5d\63\2\u012a")
        buf.write("?\3\2\2\2\u012b\u012c\7/\2\2\u012c\u012d\7\'\2\2\u012d")
        buf.write("\u012e\5H%\2\u012e\u012f\7(\2\2\u012f\u0130\5d\63\2\u0130")
        buf.write("A\3\2\2\2\u0131\u0132\7\25\2\2\u0132\u0133\5d\63\2\u0133")
        buf.write("\u0134\5.\30\2\u0134\u0135\7\30\2\2\u0135\u0136\5d\63")
        buf.write("\2\u0136C\3\2\2\2\u0137\u013a\5F$\2\u0138\u013a\3\2\2")
        buf.write("\2\u0139\u0137\3\2\2\2\u0139\u0138\3\2\2\2\u013aE\3\2")
        buf.write("\2\2\u013b\u013c\7\20\2\2\u013c\u013d\7\'\2\2\u013d\u013e")
        buf.write("\5L\'\2\u013e\u013f\7(\2\2\u013f\u0140\5b\62\2\u0140\u0141")
        buf.write("\5\62\32\2\u0141\u0142\5F$\2\u0142\u014b\3\2\2\2\u0143")
        buf.write("\u0144\7\20\2\2\u0144\u0145\7\'\2\2\u0145\u0146\5L\'\2")
        buf.write("\u0146\u0147\7(\2\2\u0147\u0148\5b\62\2\u0148\u0149\5")
        buf.write("\62\32\2\u0149\u014b\3\2\2\2\u014a\u013b\3\2\2\2\u014a")
        buf.write("\u0143\3\2\2\2\u014bG\3\2\2\2\u014c\u014f\5J&\2\u014d")
        buf.write("\u014f\3\2\2\2\u014e\u014c\3\2\2\2\u014e\u014d\3\2\2\2")
        buf.write("\u014fI\3\2\2\2\u0150\u0151\5L\'\2\u0151\u0152\7+\2\2")
        buf.write("\u0152\u0153\5J&\2\u0153\u0156\3\2\2\2\u0154\u0156\5L")
        buf.write("\'\2\u0155\u0150\3\2\2\2\u0155\u0154\3\2\2\2\u0156K\3")
        buf.write("\2\2\2\u0157\u0158\5N(\2\u0158\u0159\7&\2\2\u0159\u015a")
        buf.write("\5N(\2\u015a\u015d\3\2\2\2\u015b\u015d\5N(\2\u015c\u0157")
        buf.write("\3\2\2\2\u015c\u015b\3\2\2\2\u015dM\3\2\2\2\u015e\u015f")
        buf.write("\5P)\2\u015f\u0160\t\4\2\2\u0160\u0161\5P)\2\u0161\u0164")
        buf.write("\3\2\2\2\u0162\u0164\5P)\2\u0163\u015e\3\2\2\2\u0163\u0162")
        buf.write("\3\2\2\2\u0164O\3\2\2\2\u0165\u0166\b)\1\2\u0166\u0167")
        buf.write("\5R*\2\u0167\u016d\3\2\2\2\u0168\u0169\f\4\2\2\u0169\u016a")
        buf.write("\t\5\2\2\u016a\u016c\5R*\2\u016b\u0168\3\2\2\2\u016c\u016f")
        buf.write("\3\2\2\2\u016d\u016b\3\2\2\2\u016d\u016e\3\2\2\2\u016e")
        buf.write("Q\3\2\2\2\u016f\u016d\3\2\2\2\u0170\u0171\b*\1\2\u0171")
        buf.write("\u0172\5T+\2\u0172\u0178\3\2\2\2\u0173\u0174\f\4\2\2\u0174")
        buf.write("\u0175\t\6\2\2\u0175\u0177\5T+\2\u0176\u0173\3\2\2\2\u0177")
        buf.write("\u017a\3\2\2\2\u0178\u0176\3\2\2\2\u0178\u0179\3\2\2\2")
        buf.write("\u0179S\3\2\2\2\u017a\u0178\3\2\2\2\u017b\u017c\b+\1\2")
        buf.write("\u017c\u017d\5V,\2\u017d\u0183\3\2\2\2\u017e\u017f\f\4")
        buf.write("\2\2\u017f\u0180\t\7\2\2\u0180\u0182\5V,\2\u0181\u017e")
        buf.write("\3\2\2\2\u0182\u0185\3\2\2\2\u0183\u0181\3\2\2\2\u0183")
        buf.write("\u0184\3\2\2\2\u0184U\3\2\2\2\u0185\u0183\3\2\2\2\u0186")
        buf.write("\u0187\7\b\2\2\u0187\u018a\5V,\2\u0188\u018a\5X-\2\u0189")
        buf.write("\u0186\3\2\2\2\u0189\u0188\3\2\2\2\u018aW\3\2\2\2\u018b")
        buf.write("\u018c\7\32\2\2\u018c\u018f\5X-\2\u018d\u018f\5Z.\2\u018e")
        buf.write("\u018b\3\2\2\2\u018e\u018d\3\2\2\2\u018fY\3\2\2\2\u0190")
        buf.write("\u0195\7/\2\2\u0191\u0192\7\'\2\2\u0192\u0193\5H%\2\u0193")
        buf.write("\u0194\7(\2\2\u0194\u0196\3\2\2\2\u0195\u0191\3\2\2\2")
        buf.write("\u0195\u0196\3\2\2\2\u0196\u0197\3\2\2\2\u0197\u0198\7")
        buf.write(")\2\2\u0198\u0199\5J&\2\u0199\u019a\7*\2\2\u019a\u019d")
        buf.write("\3\2\2\2\u019b\u019d\5\\/\2\u019c\u0190\3\2\2\2\u019c")
        buf.write("\u019b\3\2\2\2\u019d[\3\2\2\2\u019e\u019f\7/\2\2\u019f")
        buf.write("\u01a0\7\'\2\2\u01a0\u01a1\5H%\2\u01a1\u01a2\7(\2\2\u01a2")
        buf.write("\u01a5\3\2\2\2\u01a3\u01a5\5^\60\2\u01a4\u019e\3\2\2\2")
        buf.write("\u01a4\u01a3\3\2\2\2\u01a5]\3\2\2\2\u01a6\u01ad\7-\2\2")
        buf.write("\u01a7\u01ad\7.\2\2\u01a8\u01ad\7\4\2\2\u01a9\u01ad\7")
        buf.write("/\2\2\u01aa\u01ad\5\20\t\2\u01ab\u01ad\5`\61\2\u01ac\u01a6")
        buf.write("\3\2\2\2\u01ac\u01a7\3\2\2\2\u01ac\u01a8\3\2\2\2\u01ac")
        buf.write("\u01a9\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ac\u01ab\3\2\2\2")
        buf.write("\u01ad_\3\2\2\2\u01ae\u01af\7\'\2\2\u01af\u01b0\5L\'\2")
        buf.write("\u01b0\u01b1\7(\2\2\u01b1a\3\2\2\2\u01b2\u01b5\5d\63\2")
        buf.write("\u01b3\u01b5\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b4\u01b3\3")
        buf.write("\2\2\2\u01b5c\3\2\2\2\u01b6\u01b7\7,\2\2\u01b7\u01ba\5")
        buf.write("d\63\2\u01b8\u01ba\7,\2\2\u01b9\u01b6\3\2\2\2\u01b9\u01b8")
        buf.write("\3\2\2\2\u01bae\3\2\2\2)nr\u0082\u008d\u0092\u009a\u00a2")
        buf.write("\u00ad\u00b2\u00bd\u00c5\u00cc\u00d5\u00d9\u00dd\u00e3")
        buf.write("\u00eb\u00ed\u00f8\u00fe\u010d\u011f\u0139\u014a\u014e")
        buf.write("\u0155\u015c\u0163\u016d\u0178\u0183\u0189\u018e\u0195")
        buf.write("\u019c\u01a4\u01ac\u01b4\u01b9")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'return'", 
                     "'for'", "'if'", "'not'", "'var'", "'until'", "'else'", 
                     "'and'", "'number'", "'dynamic'", "'by'", "'elif'", 
                     "'or'", "'bool'", "'func'", "'break'", "'begin'", "'string'", 
                     "'continue'", "'end'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'=='", "'='", "'<-'", "'!='", "'<='", "'>='", 
                     "'<'", "'>'", "'...'", "'('", "')'", "'['", "']'", 
                     "','" ]

    symbolicNames = [ "<INVALID>", "ZCODE_COMMENT", "BOOLEAN_LITERAL", "RETURN", 
                      "FOR", "IF", "NOT", "VAR", "UNTIL", "ELSE", "AND", 
                      "NUMBER", "DYNAMIC", "BY", "ELIF", "OR", "BOOL", "FUNC", 
                      "BREAK", "BEGIN", "STRING", "CONTINUE", "END", "PLUS", 
                      "MINUS", "TIMES", "DIVIDED", "MOD", "COMPARE", "EQUAL", 
                      "ASSIGN", "NOT_EQUAL", "LTOE", "GTOE", "LT", "GT", 
                      "CONCATENATION", "LEFTPAREN", "RIGHTPAREN", "LEFTBRACKET", 
                      "RIGHTBRACKET", "COMMA", "NL", "NUMBER_LITERAL", "STRING_LITERAL", 
                      "IDENTIFIER", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

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
    RULE_elstmt = 33
    RULE_elprime = 34
    RULE_exprlist = 35
    RULE_exprprime = 36
    RULE_expr0 = 37
    RULE_expr1 = 38
    RULE_expr2 = 39
    RULE_expr3 = 40
    RULE_expr4 = 41
    RULE_expr5 = 42
    RULE_expr6 = 43
    RULE_expr7 = 44
    RULE_expr8 = 45
    RULE_expr9 = 46
    RULE_expr10 = 47
    RULE_nllist = 48
    RULE_nlprime = 49

    ruleNames =  [ "program", "decllist", "decl", "primitype", "implitype", 
                   "arraytype", "sizelist", "array", "listofArray", "arrayvalue", 
                   "vardecl", "vardecl1", "vardecl2", "vardecl3", "vardecl4", 
                   "initval", "funcdecl", "paramdecl", "paramlist", "paramprime", 
                   "param", "bodyfunc", "stmtlist", "stmtprime", "stmt", 
                   "forstmt", "assignstmt", "ifstmt", "breakstmt", "continuestmt", 
                   "returnstmt", "funstmt", "blockstmt", "elstmt", "elprime", 
                   "exprlist", "exprprime", "expr0", "expr1", "expr2", "expr3", 
                   "expr4", "expr5", "expr6", "expr7", "expr8", "expr9", 
                   "expr10", "nllist", "nlprime" ]

    EOF = Token.EOF
    ZCODE_COMMENT=1
    BOOLEAN_LITERAL=2
    RETURN=3
    FOR=4
    IF=5
    NOT=6
    VAR=7
    UNTIL=8
    ELSE=9
    AND=10
    NUMBER=11
    DYNAMIC=12
    BY=13
    ELIF=14
    OR=15
    BOOL=16
    FUNC=17
    BREAK=18
    BEGIN=19
    STRING=20
    CONTINUE=21
    END=22
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
    STRING_LITERAL=44
    IDENTIFIER=45
    WS=46
    UNCLOSE_STRING=47
    ILLEGAL_ESCAPE=48
    ERROR_CHAR=49

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

        def nllist(self):
            return self.getTypedRuleContext(ZCodeParser.NllistContext,0)


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
            self.state = 100
            self.nllist()
            self.state = 101
            self.decllist()
            self.state = 102
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
            self.state = 108
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.decl()
                self.state = 105
                self.decllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 107
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
            self.state = 112
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.VAR, ZCodeParser.NUMBER, ZCodeParser.DYNAMIC, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.vardecl()
                pass
            elif token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 111
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
            self.state = 114
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
            self.state = 116
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
            self.state = 118
            self.primitype()
            self.state = 119
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 120
            self.match(ZCodeParser.LEFTBRACKET)
            self.state = 121
            self.sizelist()
            self.state = 122
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
            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.match(ZCodeParser.NUMBER_LITERAL)
                self.state = 125
                self.match(ZCodeParser.COMMA)
                self.state = 126
                self.sizelist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
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
            self.state = 130
            self.match(ZCodeParser.LEFTBRACKET)

            self.state = 131
            self.exprprime()
            self.state = 132
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
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.array()
                self.state = 135
                self.match(ZCodeParser.COMMA)
                self.state = 136
                self.listofArray()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
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
        self.enterRule(localctx, 18, self.RULE_arrayvalue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(ZCodeParser.LEFTBRACKET)
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 142
                self.listofArray()
                pass

            elif la_ == 2:
                self.state = 143
                self.exprprime()
                pass


            self.state = 146
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

        def nlprime(self):
            return self.getTypedRuleContext(ZCodeParser.NlprimeContext,0)


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
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 148
                self.vardecl1()
                pass

            elif la_ == 2:
                self.state = 149
                self.vardecl2()
                pass

            elif la_ == 3:
                self.state = 150
                self.vardecl3()
                pass

            elif la_ == 4:
                self.state = 151
                self.vardecl4()
                pass


            self.state = 154
            self.nlprime()
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
            self.state = 156
            self.primitype()
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
            self.state = 162
            self.match(ZCodeParser.VAR)
            self.state = 163
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 164
            self.match(ZCodeParser.ASSIGN)
            self.state = 165
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
            self.state = 167
            self.match(ZCodeParser.DYNAMIC)
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
            self.state = 173
            self.arraytype()
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 174
                self.match(ZCodeParser.ASSIGN)
                self.state = 175
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
            self.state = 178
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


        def nlprime(self):
            return self.getTypedRuleContext(ZCodeParser.NlprimeContext,0)


        def nllist(self):
            return self.getTypedRuleContext(ZCodeParser.NllistContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(ZCodeParser.FUNC)
            self.state = 181
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 182
            self.paramdecl()
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 183
                self.nllist()
                self.state = 184
                self.bodyfunc()
                pass

            elif la_ == 2:
                self.state = 186
                self.nlprime()
                pass


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
            self.state = 189
            self.match(ZCodeParser.LEFTPAREN)
            self.state = 190
            self.paramlist()
            self.state = 191
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
            self.state = 195
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
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
            self.state = 202
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.param()
                self.state = 198
                self.match(ZCodeParser.COMMA)
                self.state = 199
                self.paramprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
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
            self.state = 204
            self.primitype()
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 205
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 206
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 207
                self.match(ZCodeParser.LEFTBRACKET)
                self.state = 208
                self.exprprime()
                self.state = 209
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
            self.state = 215
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.returnstmt()
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 214
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
            self.state = 219
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN, ZCodeParser.FOR, ZCodeParser.IF, ZCodeParser.VAR, ZCodeParser.NUMBER, ZCodeParser.DYNAMIC, ZCodeParser.BOOL, ZCodeParser.BREAK, ZCodeParser.BEGIN, ZCodeParser.STRING, ZCodeParser.CONTINUE, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
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
        self.enterRule(localctx, 46, self.RULE_stmtprime)
        try:
            self.state = 235
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                if la_ == 1:
                    self.state = 221
                    self.stmt()
                    pass

                elif la_ == 2:
                    self.state = 222
                    self.vardecl()
                    self.state = 223
                    self.nlprime()
                    pass


                self.state = 227
                self.stmtprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                if la_ == 1:
                    self.state = 229
                    self.stmt()
                    pass

                elif la_ == 2:
                    self.state = 230
                    self.vardecl()
                    self.state = 231
                    self.nlprime()
                    pass


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


        def vardecl(self):
            return self.getTypedRuleContext(ZCodeParser.VardeclContext,0)


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
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 237
                self.assignstmt()
                pass

            elif la_ == 2:
                self.state = 238
                self.forstmt()
                pass

            elif la_ == 3:
                self.state = 239
                self.ifstmt()
                pass

            elif la_ == 4:
                self.state = 240
                self.breakstmt()
                pass

            elif la_ == 5:
                self.state = 241
                self.continuestmt()
                pass

            elif la_ == 6:
                self.state = 242
                self.returnstmt()
                pass

            elif la_ == 7:
                self.state = 243
                self.funstmt()
                pass

            elif la_ == 8:
                self.state = 244
                self.blockstmt()
                pass

            elif la_ == 9:
                self.state = 245
                self.vardecl()
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


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def exprlist(self):
            return self.getTypedRuleContext(ZCodeParser.ExprlistContext,0)


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
            self.state = 248
            self.match(ZCodeParser.FOR)
            self.state = 249
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 252
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 250
                self.match(ZCodeParser.ASSIGN)
                self.state = 251
                self.exprlist()


            self.state = 254
            self.match(ZCodeParser.UNTIL)
            self.state = 255
            self.exprprime()
            self.state = 256
            self.match(ZCodeParser.BY)
            self.state = 257
            self.exprprime()
            self.state = 258
            self.nllist()
            self.state = 259
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

        def exprprime(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprprimeContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprprimeContext,i)


        def nlprime(self):
            return self.getTypedRuleContext(ZCodeParser.NlprimeContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LEFTBRACKET(self):
            return self.getToken(ZCodeParser.LEFTBRACKET, 0)

        def RIGHTBRACKET(self):
            return self.getToken(ZCodeParser.RIGHTBRACKET, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 261
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 262
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 263
                self.match(ZCodeParser.LEFTBRACKET)
                self.state = 264
                self.exprprime()
                self.state = 265
                self.match(ZCodeParser.RIGHTBRACKET)
                pass


            self.state = 269
            self.match(ZCodeParser.ASSIGN)
            self.state = 270
            self.exprprime()
            self.state = 271
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

        def LEFTPAREN(self):
            return self.getToken(ZCodeParser.LEFTPAREN, 0)

        def expr0(self):
            return self.getTypedRuleContext(ZCodeParser.Expr0Context,0)


        def RIGHTPAREN(self):
            return self.getToken(ZCodeParser.RIGHTPAREN, 0)

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
        self.enterRule(localctx, 54, self.RULE_ifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.match(ZCodeParser.IF)
            self.state = 274
            self.match(ZCodeParser.LEFTPAREN)
            self.state = 275
            self.expr0()
            self.state = 276
            self.match(ZCodeParser.RIGHTPAREN)
            self.state = 277
            self.nllist()
            self.state = 278
            self.stmt()
            self.state = 280
            self.elstmt()
            self.state = 285
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 281
                self.match(ZCodeParser.ELSE)
                self.state = 282
                self.nllist()
                self.state = 283
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
        self.enterRule(localctx, 56, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(ZCodeParser.BREAK)
            self.state = 288
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
        self.enterRule(localctx, 58, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.match(ZCodeParser.CONTINUE)
            self.state = 291
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
        self.enterRule(localctx, 60, self.RULE_returnstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(ZCodeParser.RETURN)
            self.state = 294
            self.exprlist()
            self.state = 295
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
        self.enterRule(localctx, 62, self.RULE_funstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 298
            self.match(ZCodeParser.LEFTPAREN)
            self.state = 299
            self.exprlist()
            self.state = 300
            self.match(ZCodeParser.RIGHTPAREN)
            self.state = 301
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
        self.enterRule(localctx, 64, self.RULE_blockstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(ZCodeParser.BEGIN)
            self.state = 304
            self.nlprime()
            self.state = 305
            self.stmtlist()
            self.state = 306
            self.match(ZCodeParser.END)
            self.state = 307
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
        self.enterRule(localctx, 66, self.RULE_elstmt)
        try:
            self.state = 311
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 309
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

        def LEFTPAREN(self):
            return self.getToken(ZCodeParser.LEFTPAREN, 0)

        def expr0(self):
            return self.getTypedRuleContext(ZCodeParser.Expr0Context,0)


        def RIGHTPAREN(self):
            return self.getToken(ZCodeParser.RIGHTPAREN, 0)

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
        self.enterRule(localctx, 68, self.RULE_elprime)
        try:
            self.state = 328
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 313
                self.match(ZCodeParser.ELIF)
                self.state = 314
                self.match(ZCodeParser.LEFTPAREN)
                self.state = 315
                self.expr0()
                self.state = 316
                self.match(ZCodeParser.RIGHTPAREN)
                self.state = 317
                self.nllist()
                self.state = 318
                self.stmt()
                self.state = 319
                self.elprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 321
                self.match(ZCodeParser.ELIF)
                self.state = 322
                self.match(ZCodeParser.LEFTPAREN)
                self.state = 323
                self.expr0()
                self.state = 324
                self.match(ZCodeParser.RIGHTPAREN)
                self.state = 325
                self.nllist()
                self.state = 326
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
        self.enterRule(localctx, 70, self.RULE_exprlist)
        try:
            self.state = 332
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BOOLEAN_LITERAL, ZCodeParser.NOT, ZCodeParser.MINUS, ZCodeParser.LEFTPAREN, ZCodeParser.LEFTBRACKET, ZCodeParser.NUMBER_LITERAL, ZCodeParser.STRING_LITERAL, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 330
                self.exprprime()
                pass
            elif token in [ZCodeParser.UNTIL, ZCodeParser.RIGHTPAREN, ZCodeParser.NL]:
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
        self.enterRule(localctx, 72, self.RULE_exprprime)
        try:
            self.state = 339
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.expr0()
                self.state = 335
                self.match(ZCodeParser.COMMA)
                self.state = 336
                self.exprprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 338
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
        self.enterRule(localctx, 74, self.RULE_expr0)
        try:
            self.state = 346
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 341
                self.expr1()
                self.state = 342
                self.match(ZCodeParser.CONCATENATION)
                self.state = 343
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 345
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
        self.enterRule(localctx, 76, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 353
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 348
                self.expr2(0)
                self.state = 349
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.COMPARE) | (1 << ZCodeParser.EQUAL) | (1 << ZCodeParser.NOT_EQUAL) | (1 << ZCodeParser.LTOE) | (1 << ZCodeParser.GTOE) | (1 << ZCodeParser.LT) | (1 << ZCodeParser.GT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 350
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 352
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
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 363
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 358
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 359
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 360
                    self.expr3(0) 
                self.state = 365
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
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 374
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 369
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 370
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.PLUS or _la==ZCodeParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 371
                    self.expr4(0) 
                self.state = 376
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
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 385
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 380
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 381
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TIMES) | (1 << ZCodeParser.DIVIDED) | (1 << ZCodeParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 382
                    self.expr5() 
                self.state = 387
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
        self.enterRule(localctx, 84, self.RULE_expr5)
        try:
            self.state = 391
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 388
                self.match(ZCodeParser.NOT)
                self.state = 389
                self.expr5()
                pass
            elif token in [ZCodeParser.BOOLEAN_LITERAL, ZCodeParser.MINUS, ZCodeParser.LEFTPAREN, ZCodeParser.LEFTBRACKET, ZCodeParser.NUMBER_LITERAL, ZCodeParser.STRING_LITERAL, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 390
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
        self.enterRule(localctx, 86, self.RULE_expr6)
        try:
            self.state = 396
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 393
                self.match(ZCodeParser.MINUS)
                self.state = 394
                self.expr6()
                pass
            elif token in [ZCodeParser.BOOLEAN_LITERAL, ZCodeParser.LEFTPAREN, ZCodeParser.LEFTBRACKET, ZCodeParser.NUMBER_LITERAL, ZCodeParser.STRING_LITERAL, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 395
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

        def LEFTPAREN(self):
            return self.getToken(ZCodeParser.LEFTPAREN, 0)

        def exprlist(self):
            return self.getTypedRuleContext(ZCodeParser.ExprlistContext,0)


        def RIGHTPAREN(self):
            return self.getToken(ZCodeParser.RIGHTPAREN, 0)

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
        self.enterRule(localctx, 88, self.RULE_expr7)
        self._la = 0 # Token type
        try:
            self.state = 410
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 398
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 403
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.LEFTPAREN:
                    self.state = 399
                    self.match(ZCodeParser.LEFTPAREN)
                    self.state = 400
                    self.exprlist()
                    self.state = 401
                    self.match(ZCodeParser.RIGHTPAREN)


                self.state = 405
                self.match(ZCodeParser.LEFTBRACKET)
                self.state = 406
                self.exprprime()
                self.state = 407
                self.match(ZCodeParser.RIGHTBRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 409
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
        self.enterRule(localctx, 90, self.RULE_expr8)
        try:
            self.state = 418
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 412
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 413
                self.match(ZCodeParser.LEFTPAREN)
                self.state = 414
                self.exprlist()
                self.state = 415
                self.match(ZCodeParser.RIGHTPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 417
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

        def array(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayContext,0)


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
        self.enterRule(localctx, 92, self.RULE_expr9)
        try:
            self.state = 426
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 420
                self.match(ZCodeParser.NUMBER_LITERAL)
                pass
            elif token in [ZCodeParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 421
                self.match(ZCodeParser.STRING_LITERAL)
                pass
            elif token in [ZCodeParser.BOOLEAN_LITERAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 422
                self.match(ZCodeParser.BOOLEAN_LITERAL)
                pass
            elif token in [ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 4)
                self.state = 423
                self.match(ZCodeParser.IDENTIFIER)
                pass
            elif token in [ZCodeParser.LEFTBRACKET]:
                self.enterOuterAlt(localctx, 5)
                self.state = 424
                self.array()
                pass
            elif token in [ZCodeParser.LEFTPAREN]:
                self.enterOuterAlt(localctx, 6)
                self.state = 425
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
        self.enterRule(localctx, 94, self.RULE_expr10)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            self.match(ZCodeParser.LEFTPAREN)
            self.state = 429
            self.expr0()
            self.state = 430
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
        self.enterRule(localctx, 96, self.RULE_nllist)
        try:
            self.state = 434
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 432
                self.nlprime()
                pass
            elif token in [ZCodeParser.RETURN, ZCodeParser.FOR, ZCodeParser.IF, ZCodeParser.VAR, ZCodeParser.NUMBER, ZCodeParser.DYNAMIC, ZCodeParser.BOOL, ZCodeParser.FUNC, ZCodeParser.BREAK, ZCodeParser.BEGIN, ZCodeParser.STRING, ZCodeParser.CONTINUE, ZCodeParser.IDENTIFIER]:
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
        self.enterRule(localctx, 98, self.RULE_nlprime)
        try:
            self.state = 439
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 436
                self.match(ZCodeParser.NL)
                self.state = 437
                self.nlprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 438
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
        self._predicates[39] = self.expr2_sempred
        self._predicates[40] = self.expr3_sempred
        self._predicates[41] = self.expr4_sempred
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
         




