# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\66")
        buf.write("\u018a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\3\2\3\2\3\2\3\2\7\2|\n\2\f\2\16\2\177\13\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3")
        buf.write("\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3")
        buf.write("\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32")
        buf.write("\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3")
        buf.write("%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3")
        buf.write("-\5-\u0125\n-\3-\5-\u0128\n-\5-\u012a\n-\3.\6.\u012d\n")
        buf.write(".\r.\16.\u012e\3/\3/\7/\u0133\n/\f/\16/\u0136\13/\3\60")
        buf.write("\3\60\5\60\u013a\n\60\3\60\6\60\u013d\n\60\r\60\16\60")
        buf.write("\u013e\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\5")
        buf.write("\61\u014a\n\61\3\62\3\62\7\62\u014e\n\62\f\62\16\62\u0151")
        buf.write("\13\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\5\63\u015a\n")
        buf.write("\63\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\5\65\u016f")
        buf.write("\n\65\3\66\6\66\u0172\n\66\r\66\16\66\u0173\3\67\3\67")
        buf.write("\7\67\u0178\n\67\f\67\16\67\u017b\13\67\38\68\u017e\n")
        buf.write("8\r8\168\u017f\38\38\39\39\39\3:\3:\3;\3;\2\2<\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-")
        buf.write("Y.[\2]\2_\2a/c\60e\2g\2i\2k\61m\62o\63q\64s\65u\66\3\2")
        buf.write("\13\4\2\f\f\17\17\3\2\62;\4\2GGgg\4\2--//\6\2\f\f\17\17")
        buf.write("$$^^\4\2))^^\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17")
        buf.write("\"\"\2\u0197\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3")
        buf.write("\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2")
        buf.write("\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2")
        buf.write("\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write("#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2a\3")
        buf.write("\2\2\2\2c\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\3w\3\2\2\2\5\u0082\3\2")
        buf.write("\2\2\7\u0089\3\2\2\2\t\u008d\3\2\2\2\13\u0090\3\2\2\2")
        buf.write("\r\u0094\3\2\2\2\17\u0098\3\2\2\2\21\u009e\3\2\2\2\23")
        buf.write("\u00a3\3\2\2\2\25\u00a7\3\2\2\2\27\u00ae\3\2\2\2\31\u00b6")
        buf.write("\3\2\2\2\33\u00b9\3\2\2\2\35\u00be\3\2\2\2\37\u00c1\3")
        buf.write("\2\2\2!\u00c6\3\2\2\2#\u00cb\3\2\2\2%\u00d1\3\2\2\2\'")
        buf.write("\u00d7\3\2\2\2)\u00de\3\2\2\2+\u00e7\3\2\2\2-\u00eb\3")
        buf.write("\2\2\2/\u00f1\3\2\2\2\61\u00f3\3\2\2\2\63\u00f5\3\2\2")
        buf.write("\2\65\u00f7\3\2\2\2\67\u00f9\3\2\2\29\u00fb\3\2\2\2;\u00fd")
        buf.write("\3\2\2\2=\u0100\3\2\2\2?\u0103\3\2\2\2A\u0106\3\2\2\2")
        buf.write("C\u0108\3\2\2\2E\u010a\3\2\2\2G\u010d\3\2\2\2I\u0110\3")
        buf.write("\2\2\2K\u0114\3\2\2\2M\u0116\3\2\2\2O\u0118\3\2\2\2Q\u011a")
        buf.write("\3\2\2\2S\u011c\3\2\2\2U\u011e\3\2\2\2W\u0120\3\2\2\2")
        buf.write("Y\u0122\3\2\2\2[\u012c\3\2\2\2]\u0130\3\2\2\2_\u0137\3")
        buf.write("\2\2\2a\u0149\3\2\2\2c\u014b\3\2\2\2e\u0159\3\2\2\2g\u015b")
        buf.write("\3\2\2\2i\u015d\3\2\2\2k\u0171\3\2\2\2m\u0175\3\2\2\2")
        buf.write("o\u017d\3\2\2\2q\u0183\3\2\2\2s\u0186\3\2\2\2u\u0188\3")
        buf.write("\2\2\2wx\7%\2\2xy\7%\2\2y}\3\2\2\2z|\n\2\2\2{z\3\2\2\2")
        buf.write("|\177\3\2\2\2}{\3\2\2\2}~\3\2\2\2~\u0080\3\2\2\2\177}")
        buf.write("\3\2\2\2\u0080\u0081\b\2\2\2\u0081\4\3\2\2\2\u0082\u0083")
        buf.write("\7t\2\2\u0083\u0084\7g\2\2\u0084\u0085\7v\2\2\u0085\u0086")
        buf.write("\7w\2\2\u0086\u0087\7t\2\2\u0087\u0088\7p\2\2\u0088\6")
        buf.write("\3\2\2\2\u0089\u008a\7h\2\2\u008a\u008b\7q\2\2\u008b\u008c")
        buf.write("\7t\2\2\u008c\b\3\2\2\2\u008d\u008e\7k\2\2\u008e\u008f")
        buf.write("\7h\2\2\u008f\n\3\2\2\2\u0090\u0091\7P\2\2\u0091\u0092")
        buf.write("\7Q\2\2\u0092\u0093\7V\2\2\u0093\f\3\2\2\2\u0094\u0095")
        buf.write("\7x\2\2\u0095\u0096\7c\2\2\u0096\u0097\7t\2\2\u0097\16")
        buf.write("\3\2\2\2\u0098\u0099\7w\2\2\u0099\u009a\7p\2\2\u009a\u009b")
        buf.write("\7v\2\2\u009b\u009c\7k\2\2\u009c\u009d\7n\2\2\u009d\20")
        buf.write("\3\2\2\2\u009e\u009f\7g\2\2\u009f\u00a0\7n\2\2\u00a0\u00a1")
        buf.write("\7u\2\2\u00a1\u00a2\7g\2\2\u00a2\22\3\2\2\2\u00a3\u00a4")
        buf.write("\7c\2\2\u00a4\u00a5\7p\2\2\u00a5\u00a6\7f\2\2\u00a6\24")
        buf.write("\3\2\2\2\u00a7\u00a8\7p\2\2\u00a8\u00a9\7w\2\2\u00a9\u00aa")
        buf.write("\7o\2\2\u00aa\u00ab\7d\2\2\u00ab\u00ac\7g\2\2\u00ac\u00ad")
        buf.write("\7t\2\2\u00ad\26\3\2\2\2\u00ae\u00af\7f\2\2\u00af\u00b0")
        buf.write("\7{\2\2\u00b0\u00b1\7p\2\2\u00b1\u00b2\7c\2\2\u00b2\u00b3")
        buf.write("\7o\2\2\u00b3\u00b4\7k\2\2\u00b4\u00b5\7e\2\2\u00b5\30")
        buf.write("\3\2\2\2\u00b6\u00b7\7d\2\2\u00b7\u00b8\7{\2\2\u00b8\32")
        buf.write("\3\2\2\2\u00b9\u00ba\7g\2\2\u00ba\u00bb\7n\2\2\u00bb\u00bc")
        buf.write("\7k\2\2\u00bc\u00bd\7h\2\2\u00bd\34\3\2\2\2\u00be\u00bf")
        buf.write("\7q\2\2\u00bf\u00c0\7t\2\2\u00c0\36\3\2\2\2\u00c1\u00c2")
        buf.write("\7d\2\2\u00c2\u00c3\7q\2\2\u00c3\u00c4\7q\2\2\u00c4\u00c5")
        buf.write("\7n\2\2\u00c5 \3\2\2\2\u00c6\u00c7\7h\2\2\u00c7\u00c8")
        buf.write("\7w\2\2\u00c8\u00c9\7p\2\2\u00c9\u00ca\7e\2\2\u00ca\"")
        buf.write("\3\2\2\2\u00cb\u00cc\7d\2\2\u00cc\u00cd\7t\2\2\u00cd\u00ce")
        buf.write("\7g\2\2\u00ce\u00cf\7c\2\2\u00cf\u00d0\7m\2\2\u00d0$\3")
        buf.write("\2\2\2\u00d1\u00d2\7d\2\2\u00d2\u00d3\7g\2\2\u00d3\u00d4")
        buf.write("\7i\2\2\u00d4\u00d5\7k\2\2\u00d5\u00d6\7p\2\2\u00d6&\3")
        buf.write("\2\2\2\u00d7\u00d8\7u\2\2\u00d8\u00d9\7v\2\2\u00d9\u00da")
        buf.write("\7t\2\2\u00da\u00db\7k\2\2\u00db\u00dc\7p\2\2\u00dc\u00dd")
        buf.write("\7i\2\2\u00dd(\3\2\2\2\u00de\u00df\7e\2\2\u00df\u00e0")
        buf.write("\7q\2\2\u00e0\u00e1\7p\2\2\u00e1\u00e2\7v\2\2\u00e2\u00e3")
        buf.write("\7k\2\2\u00e3\u00e4\7p\2\2\u00e4\u00e5\7w\2\2\u00e5\u00e6")
        buf.write("\7g\2\2\u00e6*\3\2\2\2\u00e7\u00e8\7g\2\2\u00e8\u00e9")
        buf.write("\7p\2\2\u00e9\u00ea\7f\2\2\u00ea,\3\2\2\2\u00eb\u00ec")
        buf.write("\7c\2\2\u00ec\u00ed\7t\2\2\u00ed\u00ee\7t\2\2\u00ee\u00ef")
        buf.write("\7c\2\2\u00ef\u00f0\7{\2\2\u00f0.\3\2\2\2\u00f1\u00f2")
        buf.write("\7-\2\2\u00f2\60\3\2\2\2\u00f3\u00f4\7/\2\2\u00f4\62\3")
        buf.write("\2\2\2\u00f5\u00f6\7,\2\2\u00f6\64\3\2\2\2\u00f7\u00f8")
        buf.write("\7\61\2\2\u00f8\66\3\2\2\2\u00f9\u00fa\7\'\2\2\u00fa8")
        buf.write("\3\2\2\2\u00fb\u00fc\7?\2\2\u00fc:\3\2\2\2\u00fd\u00fe")
        buf.write("\7>\2\2\u00fe\u00ff\7/\2\2\u00ff<\3\2\2\2\u0100\u0101")
        buf.write("\7?\2\2\u0101\u0102\7?\2\2\u0102>\3\2\2\2\u0103\u0104")
        buf.write("\7#\2\2\u0104\u0105\7?\2\2\u0105@\3\2\2\2\u0106\u0107")
        buf.write("\7>\2\2\u0107B\3\2\2\2\u0108\u0109\7@\2\2\u0109D\3\2\2")
        buf.write("\2\u010a\u010b\7>\2\2\u010b\u010c\7?\2\2\u010cF\3\2\2")
        buf.write("\2\u010d\u010e\7@\2\2\u010e\u010f\7?\2\2\u010fH\3\2\2")
        buf.write("\2\u0110\u0111\7\60\2\2\u0111\u0112\7\60\2\2\u0112\u0113")
        buf.write("\7\60\2\2\u0113J\3\2\2\2\u0114\u0115\7*\2\2\u0115L\3\2")
        buf.write("\2\2\u0116\u0117\7+\2\2\u0117N\3\2\2\2\u0118\u0119\7]")
        buf.write("\2\2\u0119P\3\2\2\2\u011a\u011b\7_\2\2\u011bR\3\2\2\2")
        buf.write("\u011c\u011d\7.\2\2\u011dT\3\2\2\2\u011e\u011f\7<\2\2")
        buf.write("\u011fV\3\2\2\2\u0120\u0121\7=\2\2\u0121X\3\2\2\2\u0122")
        buf.write("\u0129\5[.\2\u0123\u0125\5]/\2\u0124\u0123\3\2\2\2\u0124")
        buf.write("\u0125\3\2\2\2\u0125\u0127\3\2\2\2\u0126\u0128\5_\60\2")
        buf.write("\u0127\u0126\3\2\2\2\u0127\u0128\3\2\2\2\u0128\u012a\3")
        buf.write("\2\2\2\u0129\u0124\3\2\2\2\u0129\u012a\3\2\2\2\u012aZ")
        buf.write("\3\2\2\2\u012b\u012d\t\3\2\2\u012c\u012b\3\2\2\2\u012d")
        buf.write("\u012e\3\2\2\2\u012e\u012c\3\2\2\2\u012e\u012f\3\2\2\2")
        buf.write("\u012f\\\3\2\2\2\u0130\u0134\7\60\2\2\u0131\u0133\t\3")
        buf.write("\2\2\u0132\u0131\3\2\2\2\u0133\u0136\3\2\2\2\u0134\u0132")
        buf.write("\3\2\2\2\u0134\u0135\3\2\2\2\u0135^\3\2\2\2\u0136\u0134")
        buf.write("\3\2\2\2\u0137\u0139\t\4\2\2\u0138\u013a\t\5\2\2\u0139")
        buf.write("\u0138\3\2\2\2\u0139\u013a\3\2\2\2\u013a\u013c\3\2\2\2")
        buf.write("\u013b\u013d\t\3\2\2\u013c\u013b\3\2\2\2\u013d\u013e\3")
        buf.write("\2\2\2\u013e\u013c\3\2\2\2\u013e\u013f\3\2\2\2\u013f`")
        buf.write("\3\2\2\2\u0140\u0141\7v\2\2\u0141\u0142\7t\2\2\u0142\u0143")
        buf.write("\7w\2\2\u0143\u014a\7g\2\2\u0144\u0145\7h\2\2\u0145\u0146")
        buf.write("\7c\2\2\u0146\u0147\7n\2\2\u0147\u0148\7u\2\2\u0148\u014a")
        buf.write("\7g\2\2\u0149\u0140\3\2\2\2\u0149\u0144\3\2\2\2\u014a")
        buf.write("b\3\2\2\2\u014b\u014f\5g\64\2\u014c\u014e\5e\63\2\u014d")
        buf.write("\u014c\3\2\2\2\u014e\u0151\3\2\2\2\u014f\u014d\3\2\2\2")
        buf.write("\u014f\u0150\3\2\2\2\u0150\u0152\3\2\2\2\u0151\u014f\3")
        buf.write("\2\2\2\u0152\u0153\5g\64\2\u0153\u0154\b\62\3\2\u0154")
        buf.write("d\3\2\2\2\u0155\u015a\5i\65\2\u0156\u0157\7)\2\2\u0157")
        buf.write("\u015a\7$\2\2\u0158\u015a\n\6\2\2\u0159\u0155\3\2\2\2")
        buf.write("\u0159\u0156\3\2\2\2\u0159\u0158\3\2\2\2\u015af\3\2\2")
        buf.write("\2\u015b\u015c\7$\2\2\u015ch\3\2\2\2\u015d\u016e\7^\2")
        buf.write("\2\u015e\u015f\7\"\2\2\u015f\u0160\7d\2\2\u0160\u016f")
        buf.write("\7\"\2\2\u0161\u0162\7\"\2\2\u0162\u0163\7h\2\2\u0163")
        buf.write("\u016f\7\"\2\2\u0164\u0165\7\"\2\2\u0165\u0166\7t\2\2")
        buf.write("\u0166\u016f\7\"\2\2\u0167\u0168\7\"\2\2\u0168\u0169\7")
        buf.write("p\2\2\u0169\u016f\7\"\2\2\u016a\u016b\7\"\2\2\u016b\u016c")
        buf.write("\7v\2\2\u016c\u016f\7\"\2\2\u016d\u016f\t\7\2\2\u016e")
        buf.write("\u015e\3\2\2\2\u016e\u0161\3\2\2\2\u016e\u0164\3\2\2\2")
        buf.write("\u016e\u0167\3\2\2\2\u016e\u016a\3\2\2\2\u016e\u016d\3")
        buf.write("\2\2\2\u016fj\3\2\2\2\u0170\u0172\t\3\2\2\u0171\u0170")
        buf.write("\3\2\2\2\u0172\u0173\3\2\2\2\u0173\u0171\3\2\2\2\u0173")
        buf.write("\u0174\3\2\2\2\u0174l\3\2\2\2\u0175\u0179\t\b\2\2\u0176")
        buf.write("\u0178\t\t\2\2\u0177\u0176\3\2\2\2\u0178\u017b\3\2\2\2")
        buf.write("\u0179\u0177\3\2\2\2\u0179\u017a\3\2\2\2\u017an\3\2\2")
        buf.write("\2\u017b\u0179\3\2\2\2\u017c\u017e\t\n\2\2\u017d\u017c")
        buf.write("\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u017d\3\2\2\2\u017f")
        buf.write("\u0180\3\2\2\2\u0180\u0181\3\2\2\2\u0181\u0182\b8\2\2")
        buf.write("\u0182p\3\2\2\2\u0183\u0184\13\2\2\2\u0184\u0185\b9\4")
        buf.write("\2\u0185r\3\2\2\2\u0186\u0187\13\2\2\2\u0187t\3\2\2\2")
        buf.write("\u0188\u0189\13\2\2\2\u0189v\3\2\2\2\22\2}\u0124\u0127")
        buf.write("\u0129\u012e\u0134\u0139\u013e\u0149\u014f\u0159\u016e")
        buf.write("\u0173\u0179\u017f\5\b\2\2\3\62\2\39\3")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ZCODE_COMMENT = 1
    RETURN = 2
    FOR = 3
    IF = 4
    NOT = 5
    VAR = 6
    UNTIL = 7
    ELSE = 8
    AND = 9
    NUMBER = 10
    DYNAMIC = 11
    BY = 12
    ELIF = 13
    OR = 14
    BOOL = 15
    FUNC = 16
    BREAK = 17
    BEGIN = 18
    STRING = 19
    CONTINUE = 20
    END = 21
    ARRAY = 22
    PLUS = 23
    MINUS = 24
    TIMES = 25
    DIVIDED = 26
    MOD = 27
    EQUAL = 28
    ASSIGN = 29
    COMPARE = 30
    NOT_EQUAL = 31
    LT = 32
    GT = 33
    LTOE = 34
    GTOE = 35
    CONCATENATION = 36
    LEFTPAREN = 37
    RIGHTPAREN = 38
    LEFTBRACKET = 39
    RIGHTBRACKET = 40
    COMMA = 41
    COLON = 42
    SEMI = 43
    NUMBER_LITERAL = 44
    BOOLEAN_LITERAL = 45
    STRING_LITERAL = 46
    SIZE = 47
    IDENTIFIER = 48
    WS = 49
    ERROR_CHAR = 50
    UNCLOSE_STRING = 51
    ILLEGAL_ESCAPE = 52

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'return'", "'for'", "'if'", "'NOT'", "'var'", "'until'", "'else'", 
            "'and'", "'number'", "'dynamic'", "'by'", "'elif'", "'or'", 
            "'bool'", "'func'", "'break'", "'begin'", "'string'", "'continue'", 
            "'end'", "'array'", "'+'", "'-'", "'*'", "'/'", "'%'", "'='", 
            "'<-'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'...'", 
            "'('", "')'", "'['", "']'", "','", "':'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "ZCODE_COMMENT", "RETURN", "FOR", "IF", "NOT", "VAR", "UNTIL", 
            "ELSE", "AND", "NUMBER", "DYNAMIC", "BY", "ELIF", "OR", "BOOL", 
            "FUNC", "BREAK", "BEGIN", "STRING", "CONTINUE", "END", "ARRAY", 
            "PLUS", "MINUS", "TIMES", "DIVIDED", "MOD", "EQUAL", "ASSIGN", 
            "COMPARE", "NOT_EQUAL", "LT", "GT", "LTOE", "GTOE", "CONCATENATION", 
            "LEFTPAREN", "RIGHTPAREN", "LEFTBRACKET", "RIGHTBRACKET", "COMMA", 
            "COLON", "SEMI", "NUMBER_LITERAL", "BOOLEAN_LITERAL", "STRING_LITERAL", 
            "SIZE", "IDENTIFIER", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "ZCODE_COMMENT", "RETURN", "FOR", "IF", "NOT", "VAR", 
                  "UNTIL", "ELSE", "AND", "NUMBER", "DYNAMIC", "BY", "ELIF", 
                  "OR", "BOOL", "FUNC", "BREAK", "BEGIN", "STRING", "CONTINUE", 
                  "END", "ARRAY", "PLUS", "MINUS", "TIMES", "DIVIDED", "MOD", 
                  "EQUAL", "ASSIGN", "COMPARE", "NOT_EQUAL", "LT", "GT", 
                  "LTOE", "GTOE", "CONCATENATION", "LEFTPAREN", "RIGHTPAREN", 
                  "LEFTBRACKET", "RIGHTBRACKET", "COMMA", "COLON", "SEMI", 
                  "NUMBER_LITERAL", "INTEGERPART", "DECIMALPART", "EXPONENTPART", 
                  "BOOLEAN_LITERAL", "STRING_LITERAL", "CHARLIST", "DOUBLEQUOTE", 
                  "ESCAPE", "SIZE", "IDENTIFIER", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[48] = self.STRING_LITERAL_action 
            actions[55] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text =self.text[1:-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     


