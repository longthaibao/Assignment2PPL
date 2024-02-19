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
        buf.write("\u01bf\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
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
        buf.write(" \3 \3 \5 \u012b\n \3 \3 \3!\3!\3!\3!\3!\3!\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3#\3#\5#\u013d\n#\3$\3$\3$\3$\3$\3$\3$")
        buf.write("\3$\3$\3$\3$\3$\3$\3$\3$\5$\u014e\n$\3%\3%\5%\u0152\n")
        buf.write("%\3&\3&\3&\3&\3&\5&\u0159\n&\3\'\3\'\3\'\3\'\3\'\5\'\u0160")
        buf.write("\n\'\3(\3(\3(\3(\3(\5(\u0167\n(\3)\3)\3)\3)\3)\3)\7)\u016f")
        buf.write("\n)\f)\16)\u0172\13)\3*\3*\3*\3*\3*\3*\7*\u017a\n*\f*")
        buf.write("\16*\u017d\13*\3+\3+\3+\3+\3+\3+\7+\u0185\n+\f+\16+\u0188")
        buf.write("\13+\3,\3,\3,\5,\u018d\n,\3-\3-\3-\5-\u0192\n-\3.\3.\3")
        buf.write(".\3.\3.\5.\u0199\n.\3.\3.\3.\3.\3.\5.\u01a0\n.\3/\3/\3")
        buf.write("/\3/\3/\3/\5/\u01a8\n/\3\60\3\60\3\60\3\60\3\60\3\60\5")
        buf.write("\60\u01b0\n\60\3\61\3\61\3\61\3\61\3\62\3\62\5\62\u01b8")
        buf.write("\n\62\3\63\3\63\3\63\5\63\u01bd\n\63\3\63\2\5PRT\64\2")
        buf.write("\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@BDFHJLNPRTVXZ\\^`bd\2\b\5\2\r\r\22\22\26\26\4")
        buf.write("\2\t\t\16\16\4\2\36\37!%\4\2\f\f\21\21\3\2\31\32\3\2\33")
        buf.write("\35\2\u01c1\2f\3\2\2\2\4n\3\2\2\2\6r\3\2\2\2\bt\3\2\2")
        buf.write("\2\nv\3\2\2\2\fx\3\2\2\2\16\u0082\3\2\2\2\20\u0084\3\2")
        buf.write("\2\2\22\u008d\3\2\2\2\24\u008f\3\2\2\2\26\u009a\3\2\2")
        buf.write("\2\30\u009e\3\2\2\2\32\u00a4\3\2\2\2\34\u00a9\3\2\2\2")
        buf.write("\36\u00af\3\2\2\2 \u00b4\3\2\2\2\"\u00b6\3\2\2\2$\u00bf")
        buf.write("\3\2\2\2&\u00c5\3\2\2\2(\u00cc\3\2\2\2*\u00ce\3\2\2\2")
        buf.write(",\u00d9\3\2\2\2.\u00dd\3\2\2\2\60\u00ed\3\2\2\2\62\u00f8")
        buf.write("\3\2\2\2\64\u00fa\3\2\2\2\66\u010d\3\2\2\28\u0113\3\2")
        buf.write("\2\2:\u0121\3\2\2\2<\u0124\3\2\2\2>\u0127\3\2\2\2@\u012e")
        buf.write("\3\2\2\2B\u0134\3\2\2\2D\u013c\3\2\2\2F\u014d\3\2\2\2")
        buf.write("H\u0151\3\2\2\2J\u0158\3\2\2\2L\u015f\3\2\2\2N\u0166\3")
        buf.write("\2\2\2P\u0168\3\2\2\2R\u0173\3\2\2\2T\u017e\3\2\2\2V\u018c")
        buf.write("\3\2\2\2X\u0191\3\2\2\2Z\u019f\3\2\2\2\\\u01a7\3\2\2\2")
        buf.write("^\u01af\3\2\2\2`\u01b1\3\2\2\2b\u01b7\3\2\2\2d\u01bc\3")
        buf.write("\2\2\2fg\5b\62\2gh\5\4\3\2hi\7\2\2\3i\3\3\2\2\2jk\5\6")
        buf.write("\4\2kl\5\4\3\2lo\3\2\2\2mo\5\6\4\2nj\3\2\2\2nm\3\2\2\2")
        buf.write("o\5\3\2\2\2ps\5\26\f\2qs\5\"\22\2rp\3\2\2\2rq\3\2\2\2")
        buf.write("s\7\3\2\2\2tu\t\2\2\2u\t\3\2\2\2vw\t\3\2\2w\13\3\2\2\2")
        buf.write("xy\5\b\5\2yz\7/\2\2z{\7)\2\2{|\5\16\b\2|}\7*\2\2}\r\3")
        buf.write("\2\2\2~\177\7-\2\2\177\u0080\7+\2\2\u0080\u0083\5\16\b")
        buf.write("\2\u0081\u0083\7-\2\2\u0082~\3\2\2\2\u0082\u0081\3\2\2")
        buf.write("\2\u0083\17\3\2\2\2\u0084\u0085\7)\2\2\u0085\u0086\5J")
        buf.write("&\2\u0086\u0087\7*\2\2\u0087\21\3\2\2\2\u0088\u0089\5")
        buf.write("\20\t\2\u0089\u008a\7+\2\2\u008a\u008b\5\22\n\2\u008b")
        buf.write("\u008e\3\2\2\2\u008c\u008e\5\20\t\2\u008d\u0088\3\2\2")
        buf.write("\2\u008d\u008c\3\2\2\2\u008e\23\3\2\2\2\u008f\u0092\7")
        buf.write(")\2\2\u0090\u0093\5\22\n\2\u0091\u0093\5J&\2\u0092\u0090")
        buf.write("\3\2\2\2\u0092\u0091\3\2\2\2\u0093\u0094\3\2\2\2\u0094")
        buf.write("\u0095\7*\2\2\u0095\25\3\2\2\2\u0096\u009b\5\30\r\2\u0097")
        buf.write("\u009b\5\32\16\2\u0098\u009b\5\34\17\2\u0099\u009b\5\36")
        buf.write("\20\2\u009a\u0096\3\2\2\2\u009a\u0097\3\2\2\2\u009a\u0098")
        buf.write("\3\2\2\2\u009a\u0099\3\2\2\2\u009b\u009c\3\2\2\2\u009c")
        buf.write("\u009d\5d\63\2\u009d\27\3\2\2\2\u009e\u009f\5\b\5\2\u009f")
        buf.write("\u00a2\7/\2\2\u00a0\u00a1\7 \2\2\u00a1\u00a3\5 \21\2\u00a2")
        buf.write("\u00a0\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\31\3\2\2\2\u00a4")
        buf.write("\u00a5\7\t\2\2\u00a5\u00a6\7/\2\2\u00a6\u00a7\7 \2\2\u00a7")
        buf.write("\u00a8\5 \21\2\u00a8\33\3\2\2\2\u00a9\u00aa\7\16\2\2\u00aa")
        buf.write("\u00ad\7/\2\2\u00ab\u00ac\7 \2\2\u00ac\u00ae\5 \21\2\u00ad")
        buf.write("\u00ab\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\35\3\2\2\2\u00af")
        buf.write("\u00b2\5\f\7\2\u00b0\u00b1\7 \2\2\u00b1\u00b3\5L\'\2\u00b2")
        buf.write("\u00b0\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\37\3\2\2\2\u00b4")
        buf.write("\u00b5\5L\'\2\u00b5!\3\2\2\2\u00b6\u00b7\7\23\2\2\u00b7")
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
        buf.write("\u0101\u0102\5L\'\2\u0102\u0103\7\17\2\2\u0103\u0104\5")
        buf.write("L\'\2\u0104\u0105\5b\62\2\u0105\u0106\5\60\31\2\u0106")
        buf.write("\65\3\2\2\2\u0107\u010e\7/\2\2\u0108\u0109\7/\2\2\u0109")
        buf.write("\u010a\7)\2\2\u010a\u010b\5J&\2\u010b\u010c\7*\2\2\u010c")
        buf.write("\u010e\3\2\2\2\u010d\u0107\3\2\2\2\u010d\u0108\3\2\2\2")
        buf.write("\u010e\u010f\3\2\2\2\u010f\u0110\7 \2\2\u0110\u0111\5")
        buf.write("L\'\2\u0111\u0112\5d\63\2\u0112\67\3\2\2\2\u0113\u0114")
        buf.write("\7\7\2\2\u0114\u0115\7\'\2\2\u0115\u0116\5L\'\2\u0116")
        buf.write("\u0117\7(\2\2\u0117\u0118\5b\62\2\u0118\u0119\5\62\32")
        buf.write("\2\u0119\u011a\3\2\2\2\u011a\u011f\5D#\2\u011b\u011c\7")
        buf.write("\13\2\2\u011c\u011d\5b\62\2\u011d\u011e\5\62\32\2\u011e")
        buf.write("\u0120\3\2\2\2\u011f\u011b\3\2\2\2\u011f\u0120\3\2\2\2")
        buf.write("\u01209\3\2\2\2\u0121\u0122\7\24\2\2\u0122\u0123\5d\63")
        buf.write("\2\u0123;\3\2\2\2\u0124\u0125\7\27\2\2\u0125\u0126\5d")
        buf.write("\63\2\u0126=\3\2\2\2\u0127\u012a\7\5\2\2\u0128\u012b\5")
        buf.write("L\'\2\u0129\u012b\3\2\2\2\u012a\u0128\3\2\2\2\u012a\u0129")
        buf.write("\3\2\2\2\u012b\u012c\3\2\2\2\u012c\u012d\5d\63\2\u012d")
        buf.write("?\3\2\2\2\u012e\u012f\7/\2\2\u012f\u0130\7\'\2\2\u0130")
        buf.write("\u0131\5H%\2\u0131\u0132\7(\2\2\u0132\u0133\5d\63\2\u0133")
        buf.write("A\3\2\2\2\u0134\u0135\7\25\2\2\u0135\u0136\5d\63\2\u0136")
        buf.write("\u0137\5.\30\2\u0137\u0138\7\30\2\2\u0138\u0139\5d\63")
        buf.write("\2\u0139C\3\2\2\2\u013a\u013d\5F$\2\u013b\u013d\3\2\2")
        buf.write("\2\u013c\u013a\3\2\2\2\u013c\u013b\3\2\2\2\u013dE\3\2")
        buf.write("\2\2\u013e\u013f\7\20\2\2\u013f\u0140\7\'\2\2\u0140\u0141")
        buf.write("\5L\'\2\u0141\u0142\7(\2\2\u0142\u0143\5b\62\2\u0143\u0144")
        buf.write("\5\62\32\2\u0144\u0145\5F$\2\u0145\u014e\3\2\2\2\u0146")
        buf.write("\u0147\7\20\2\2\u0147\u0148\7\'\2\2\u0148\u0149\5L\'\2")
        buf.write("\u0149\u014a\7(\2\2\u014a\u014b\5b\62\2\u014b\u014c\5")
        buf.write("\62\32\2\u014c\u014e\3\2\2\2\u014d\u013e\3\2\2\2\u014d")
        buf.write("\u0146\3\2\2\2\u014eG\3\2\2\2\u014f\u0152\5J&\2\u0150")
        buf.write("\u0152\3\2\2\2\u0151\u014f\3\2\2\2\u0151\u0150\3\2\2\2")
        buf.write("\u0152I\3\2\2\2\u0153\u0154\5L\'\2\u0154\u0155\7+\2\2")
        buf.write("\u0155\u0156\5J&\2\u0156\u0159\3\2\2\2\u0157\u0159\5L")
        buf.write("\'\2\u0158\u0153\3\2\2\2\u0158\u0157\3\2\2\2\u0159K\3")
        buf.write("\2\2\2\u015a\u015b\5N(\2\u015b\u015c\7&\2\2\u015c\u015d")
        buf.write("\5N(\2\u015d\u0160\3\2\2\2\u015e\u0160\5N(\2\u015f\u015a")
        buf.write("\3\2\2\2\u015f\u015e\3\2\2\2\u0160M\3\2\2\2\u0161\u0162")
        buf.write("\5P)\2\u0162\u0163\t\4\2\2\u0163\u0164\5P)\2\u0164\u0167")
        buf.write("\3\2\2\2\u0165\u0167\5P)\2\u0166\u0161\3\2\2\2\u0166\u0165")
        buf.write("\3\2\2\2\u0167O\3\2\2\2\u0168\u0169\b)\1\2\u0169\u016a")
        buf.write("\5R*\2\u016a\u0170\3\2\2\2\u016b\u016c\f\4\2\2\u016c\u016d")
        buf.write("\t\5\2\2\u016d\u016f\5R*\2\u016e\u016b\3\2\2\2\u016f\u0172")
        buf.write("\3\2\2\2\u0170\u016e\3\2\2\2\u0170\u0171\3\2\2\2\u0171")
        buf.write("Q\3\2\2\2\u0172\u0170\3\2\2\2\u0173\u0174\b*\1\2\u0174")
        buf.write("\u0175\5T+\2\u0175\u017b\3\2\2\2\u0176\u0177\f\4\2\2\u0177")
        buf.write("\u0178\t\6\2\2\u0178\u017a\5T+\2\u0179\u0176\3\2\2\2\u017a")
        buf.write("\u017d\3\2\2\2\u017b\u0179\3\2\2\2\u017b\u017c\3\2\2\2")
        buf.write("\u017cS\3\2\2\2\u017d\u017b\3\2\2\2\u017e\u017f\b+\1\2")
        buf.write("\u017f\u0180\5V,\2\u0180\u0186\3\2\2\2\u0181\u0182\f\4")
        buf.write("\2\2\u0182\u0183\t\7\2\2\u0183\u0185\5V,\2\u0184\u0181")
        buf.write("\3\2\2\2\u0185\u0188\3\2\2\2\u0186\u0184\3\2\2\2\u0186")
        buf.write("\u0187\3\2\2\2\u0187U\3\2\2\2\u0188\u0186\3\2\2\2\u0189")
        buf.write("\u018a\7\b\2\2\u018a\u018d\5V,\2\u018b\u018d\5X-\2\u018c")
        buf.write("\u0189\3\2\2\2\u018c\u018b\3\2\2\2\u018dW\3\2\2\2\u018e")
        buf.write("\u018f\7\32\2\2\u018f\u0192\5X-\2\u0190\u0192\5Z.\2\u0191")
        buf.write("\u018e\3\2\2\2\u0191\u0190\3\2\2\2\u0192Y\3\2\2\2\u0193")
        buf.write("\u0198\7/\2\2\u0194\u0195\7\'\2\2\u0195\u0196\5H%\2\u0196")
        buf.write("\u0197\7(\2\2\u0197\u0199\3\2\2\2\u0198\u0194\3\2\2\2")
        buf.write("\u0198\u0199\3\2\2\2\u0199\u019a\3\2\2\2\u019a\u019b\7")
        buf.write(")\2\2\u019b\u019c\5J&\2\u019c\u019d\7*\2\2\u019d\u01a0")
        buf.write("\3\2\2\2\u019e\u01a0\5\\/\2\u019f\u0193\3\2\2\2\u019f")
        buf.write("\u019e\3\2\2\2\u01a0[\3\2\2\2\u01a1\u01a2\7/\2\2\u01a2")
        buf.write("\u01a3\7\'\2\2\u01a3\u01a4\5H%\2\u01a4\u01a5\7(\2\2\u01a5")
        buf.write("\u01a8\3\2\2\2\u01a6\u01a8\5^\60\2\u01a7\u01a1\3\2\2\2")
        buf.write("\u01a7\u01a6\3\2\2\2\u01a8]\3\2\2\2\u01a9\u01b0\7-\2\2")
        buf.write("\u01aa\u01b0\7.\2\2\u01ab\u01b0\7\4\2\2\u01ac\u01b0\7")
        buf.write("/\2\2\u01ad\u01b0\5\20\t\2\u01ae\u01b0\5`\61\2\u01af\u01a9")
        buf.write("\3\2\2\2\u01af\u01aa\3\2\2\2\u01af\u01ab\3\2\2\2\u01af")
        buf.write("\u01ac\3\2\2\2\u01af\u01ad\3\2\2\2\u01af\u01ae\3\2\2\2")
        buf.write("\u01b0_\3\2\2\2\u01b1\u01b2\7\'\2\2\u01b2\u01b3\5L\'\2")
        buf.write("\u01b3\u01b4\7(\2\2\u01b4a\3\2\2\2\u01b5\u01b8\5d\63\2")
        buf.write("\u01b6\u01b8\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b7\u01b6\3")
        buf.write("\2\2\2\u01b8c\3\2\2\2\u01b9\u01ba\7,\2\2\u01ba\u01bd\5")
        buf.write("d\63\2\u01bb\u01bd\7,\2\2\u01bc\u01b9\3\2\2\2\u01bc\u01bb")
        buf.write("\3\2\2\2\u01bde\3\2\2\2*nr\u0082\u008d\u0092\u009a\u00a2")
        buf.write("\u00ad\u00b2\u00bd\u00c5\u00cc\u00d5\u00d9\u00dd\u00e3")
        buf.write("\u00eb\u00ed\u00f8\u00fe\u010d\u011f\u012a\u013c\u014d")
        buf.write("\u0151\u0158\u015f\u0166\u0170\u017b\u0186\u018c\u0191")
        buf.write("\u0198\u019f\u01a7\u01af\u01b7\u01bc")
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

        def expr0(self):
            return self.getTypedRuleContext(ZCodeParser.Expr0Context,0)


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
                self.expr0()


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

        def expr0(self):
            return self.getTypedRuleContext(ZCodeParser.Expr0Context,0)


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
            self.expr0()
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

        def expr0(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr0Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr0Context,i)


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
            self.expr0()
            self.state = 256
            self.match(ZCodeParser.BY)
            self.state = 257
            self.expr0()
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

        def expr0(self):
            return self.getTypedRuleContext(ZCodeParser.Expr0Context,0)


        def nlprime(self):
            return self.getTypedRuleContext(ZCodeParser.NlprimeContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LEFTBRACKET(self):
            return self.getToken(ZCodeParser.LEFTBRACKET, 0)

        def exprprime(self):
            return self.getTypedRuleContext(ZCodeParser.ExprprimeContext,0)


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
            self.expr0()
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

        def nlprime(self):
            return self.getTypedRuleContext(ZCodeParser.NlprimeContext,0)


        def expr0(self):
            return self.getTypedRuleContext(ZCodeParser.Expr0Context,0)


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
            self.state = 296
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BOOLEAN_LITERAL, ZCodeParser.NOT, ZCodeParser.MINUS, ZCodeParser.LEFTPAREN, ZCodeParser.LEFTBRACKET, ZCodeParser.NUMBER_LITERAL, ZCodeParser.STRING_LITERAL, ZCodeParser.IDENTIFIER]:
                self.state = 294
                self.expr0()
                pass
            elif token in [ZCodeParser.NL]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 298
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
            self.state = 300
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 301
            self.match(ZCodeParser.LEFTPAREN)
            self.state = 302
            self.exprlist()
            self.state = 303
            self.match(ZCodeParser.RIGHTPAREN)
            self.state = 304
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
            self.state = 306
            self.match(ZCodeParser.BEGIN)
            self.state = 307
            self.nlprime()
            self.state = 308
            self.stmtlist()
            self.state = 309
            self.match(ZCodeParser.END)
            self.state = 310
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
            self.state = 314
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 312
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
            self.state = 331
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 316
                self.match(ZCodeParser.ELIF)
                self.state = 317
                self.match(ZCodeParser.LEFTPAREN)
                self.state = 318
                self.expr0()
                self.state = 319
                self.match(ZCodeParser.RIGHTPAREN)
                self.state = 320
                self.nllist()
                self.state = 321
                self.stmt()
                self.state = 322
                self.elprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 324
                self.match(ZCodeParser.ELIF)
                self.state = 325
                self.match(ZCodeParser.LEFTPAREN)
                self.state = 326
                self.expr0()
                self.state = 327
                self.match(ZCodeParser.RIGHTPAREN)
                self.state = 328
                self.nllist()
                self.state = 329
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
            self.state = 335
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BOOLEAN_LITERAL, ZCodeParser.NOT, ZCodeParser.MINUS, ZCodeParser.LEFTPAREN, ZCodeParser.LEFTBRACKET, ZCodeParser.NUMBER_LITERAL, ZCodeParser.STRING_LITERAL, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 333
                self.exprprime()
                pass
            elif token in [ZCodeParser.UNTIL, ZCodeParser.RIGHTPAREN]:
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
            self.state = 342
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                self.expr0()
                self.state = 338
                self.match(ZCodeParser.COMMA)
                self.state = 339
                self.exprprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 341
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
            self.state = 349
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 344
                self.expr1()
                self.state = 345
                self.match(ZCodeParser.CONCATENATION)
                self.state = 346
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 348
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
            self.state = 356
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 351
                self.expr2(0)
                self.state = 352
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.COMPARE) | (1 << ZCodeParser.EQUAL) | (1 << ZCodeParser.NOT_EQUAL) | (1 << ZCodeParser.LTOE) | (1 << ZCodeParser.GTOE) | (1 << ZCodeParser.LT) | (1 << ZCodeParser.GT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 353
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 355
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
            self.state = 359
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 366
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 361
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 362
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 363
                    self.expr3(0) 
                self.state = 368
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

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
            self.state = 370
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 377
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 372
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 373
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.PLUS or _la==ZCodeParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 374
                    self.expr4(0) 
                self.state = 379
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

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
            self.state = 381
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 388
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 383
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 384
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TIMES) | (1 << ZCodeParser.DIVIDED) | (1 << ZCodeParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 385
                    self.expr5() 
                self.state = 390
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

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
            self.state = 394
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 391
                self.match(ZCodeParser.NOT)
                self.state = 392
                self.expr5()
                pass
            elif token in [ZCodeParser.BOOLEAN_LITERAL, ZCodeParser.MINUS, ZCodeParser.LEFTPAREN, ZCodeParser.LEFTBRACKET, ZCodeParser.NUMBER_LITERAL, ZCodeParser.STRING_LITERAL, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 393
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
            self.state = 399
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 396
                self.match(ZCodeParser.MINUS)
                self.state = 397
                self.expr6()
                pass
            elif token in [ZCodeParser.BOOLEAN_LITERAL, ZCodeParser.LEFTPAREN, ZCodeParser.LEFTBRACKET, ZCodeParser.NUMBER_LITERAL, ZCodeParser.STRING_LITERAL, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 398
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
            self.state = 413
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 401
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 406
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.LEFTPAREN:
                    self.state = 402
                    self.match(ZCodeParser.LEFTPAREN)
                    self.state = 403
                    self.exprlist()
                    self.state = 404
                    self.match(ZCodeParser.RIGHTPAREN)


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
        self.enterRule(localctx, 90, self.RULE_expr8)
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
            self.state = 429
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
            elif token in [ZCodeParser.LEFTBRACKET]:
                self.enterOuterAlt(localctx, 5)
                self.state = 427
                self.array()
                pass
            elif token in [ZCodeParser.LEFTPAREN]:
                self.enterOuterAlt(localctx, 6)
                self.state = 428
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
            self.state = 431
            self.match(ZCodeParser.LEFTPAREN)
            self.state = 432
            self.expr0()
            self.state = 433
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
            self.state = 437
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 435
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
            self.state = 442
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 439
                self.match(ZCodeParser.NL)
                self.state = 440
                self.nlprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 441
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
         




