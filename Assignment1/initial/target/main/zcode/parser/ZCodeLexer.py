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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\64")
        buf.write("\u0195\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\3\2\3\2\3\2\3\2\7\2\u0080\n\2\f\2\16")
        buf.write("\2\u0083\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\5\3\u0090\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5")
        buf.write("\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\32\3\32")
        buf.write("\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3%\3%\3")
        buf.write("&\3&\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3")
        buf.write("-\3.\3.\3/\3/\5/\u0136\n/\3/\5/\u0139\n/\5/\u013b\n/\3")
        buf.write("\60\6\60\u013e\n\60\r\60\16\60\u013f\3\61\3\61\7\61\u0144")
        buf.write("\n\61\f\61\16\61\u0147\13\61\3\62\3\62\5\62\u014b\n\62")
        buf.write("\3\62\6\62\u014e\n\62\r\62\16\62\u014f\3\63\3\63\7\63")
        buf.write("\u0154\n\63\f\63\16\63\u0157\13\63\3\63\3\63\3\63\3\64")
        buf.write("\3\64\3\65\3\65\3\65\3\66\3\66\3\66\3\66\5\66\u0165\n")
        buf.write("\66\3\67\3\67\3\67\38\68\u016b\n8\r8\168\u016c\39\39\7")
        buf.write("9\u0171\n9\f9\169\u0174\139\3:\6:\u0177\n:\r:\16:\u0178")
        buf.write("\3:\3:\3;\3;\7;\u017f\n;\f;\16;\u0182\13;\3;\5;\u0185")
        buf.write("\n;\3;\3;\3<\3<\7<\u018b\n<\f<\16<\u018e\13<\3<\3<\3<")
        buf.write("\3=\3=\3=\2\2>\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26")
        buf.write("+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#")
        buf.write("E$G%I&K\'M(O)Q*S+U,W\2Y\2[-]._\2a\2c\2e/g\2i\2k\2m\2o")
        buf.write("\2q\60s\61u\62w\63y\64\3\2\r\4\2\f\f\17\17\3\2\f\f\3\2")
        buf.write("\62;\4\2GGgg\4\2--//\t\2))^^ddhhppttvv\6\2\f\f\17\17$")
        buf.write("$^^\5\2C\\aac|\6\2\62;C\\aac|\5\2\n\13\16\17\"\"\4\3\f")
        buf.write("\f\17\17\2\u019b\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2")
        buf.write("e\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2")
        buf.write("\2y\3\2\2\2\3{\3\2\2\2\5\u008f\3\2\2\2\7\u0091\3\2\2\2")
        buf.write("\t\u0098\3\2\2\2\13\u009c\3\2\2\2\r\u009f\3\2\2\2\17\u00a3")
        buf.write("\3\2\2\2\21\u00a7\3\2\2\2\23\u00ad\3\2\2\2\25\u00b2\3")
        buf.write("\2\2\2\27\u00b6\3\2\2\2\31\u00bd\3\2\2\2\33\u00c5\3\2")
        buf.write("\2\2\35\u00c8\3\2\2\2\37\u00cd\3\2\2\2!\u00d0\3\2\2\2")
        buf.write("#\u00d5\3\2\2\2%\u00da\3\2\2\2\'\u00e0\3\2\2\2)\u00e6")
        buf.write("\3\2\2\2+\u00ed\3\2\2\2-\u00f6\3\2\2\2/\u00fa\3\2\2\2")
        buf.write("\61\u0100\3\2\2\2\63\u0102\3\2\2\2\65\u0104\3\2\2\2\67")
        buf.write("\u0106\3\2\2\29\u0108\3\2\2\2;\u010a\3\2\2\2=\u010d\3")
        buf.write("\2\2\2?\u010f\3\2\2\2A\u0112\3\2\2\2C\u0115\3\2\2\2E\u0118")
        buf.write("\3\2\2\2G\u011b\3\2\2\2I\u011d\3\2\2\2K\u011f\3\2\2\2")
        buf.write("M\u0123\3\2\2\2O\u0125\3\2\2\2Q\u0127\3\2\2\2S\u0129\3")
        buf.write("\2\2\2U\u012b\3\2\2\2W\u012d\3\2\2\2Y\u012f\3\2\2\2[\u0131")
        buf.write("\3\2\2\2]\u0133\3\2\2\2_\u013d\3\2\2\2a\u0141\3\2\2\2")
        buf.write("c\u0148\3\2\2\2e\u0151\3\2\2\2g\u015b\3\2\2\2i\u015d\3")
        buf.write("\2\2\2k\u0164\3\2\2\2m\u0166\3\2\2\2o\u016a\3\2\2\2q\u016e")
        buf.write("\3\2\2\2s\u0176\3\2\2\2u\u017c\3\2\2\2w\u0188\3\2\2\2")
        buf.write("y\u0192\3\2\2\2{|\7%\2\2|}\7%\2\2}\u0081\3\2\2\2~\u0080")
        buf.write("\n\2\2\2\177~\3\2\2\2\u0080\u0083\3\2\2\2\u0081\177\3")
        buf.write("\2\2\2\u0081\u0082\3\2\2\2\u0082\u0084\3\2\2\2\u0083\u0081")
        buf.write("\3\2\2\2\u0084\u0085\b\2\2\2\u0085\4\3\2\2\2\u0086\u0087")
        buf.write("\7v\2\2\u0087\u0088\7t\2\2\u0088\u0089\7w\2\2\u0089\u0090")
        buf.write("\7g\2\2\u008a\u008b\7h\2\2\u008b\u008c\7c\2\2\u008c\u008d")
        buf.write("\7n\2\2\u008d\u008e\7u\2\2\u008e\u0090\7g\2\2\u008f\u0086")
        buf.write("\3\2\2\2\u008f\u008a\3\2\2\2\u0090\6\3\2\2\2\u0091\u0092")
        buf.write("\7t\2\2\u0092\u0093\7g\2\2\u0093\u0094\7v\2\2\u0094\u0095")
        buf.write("\7w\2\2\u0095\u0096\7t\2\2\u0096\u0097\7p\2\2\u0097\b")
        buf.write("\3\2\2\2\u0098\u0099\7h\2\2\u0099\u009a\7q\2\2\u009a\u009b")
        buf.write("\7t\2\2\u009b\n\3\2\2\2\u009c\u009d\7k\2\2\u009d\u009e")
        buf.write("\7h\2\2\u009e\f\3\2\2\2\u009f\u00a0\7p\2\2\u00a0\u00a1")
        buf.write("\7q\2\2\u00a1\u00a2\7v\2\2\u00a2\16\3\2\2\2\u00a3\u00a4")
        buf.write("\7x\2\2\u00a4\u00a5\7c\2\2\u00a5\u00a6\7t\2\2\u00a6\20")
        buf.write("\3\2\2\2\u00a7\u00a8\7w\2\2\u00a8\u00a9\7p\2\2\u00a9\u00aa")
        buf.write("\7v\2\2\u00aa\u00ab\7k\2\2\u00ab\u00ac\7n\2\2\u00ac\22")
        buf.write("\3\2\2\2\u00ad\u00ae\7g\2\2\u00ae\u00af\7n\2\2\u00af\u00b0")
        buf.write("\7u\2\2\u00b0\u00b1\7g\2\2\u00b1\24\3\2\2\2\u00b2\u00b3")
        buf.write("\7c\2\2\u00b3\u00b4\7p\2\2\u00b4\u00b5\7f\2\2\u00b5\26")
        buf.write("\3\2\2\2\u00b6\u00b7\7p\2\2\u00b7\u00b8\7w\2\2\u00b8\u00b9")
        buf.write("\7o\2\2\u00b9\u00ba\7d\2\2\u00ba\u00bb\7g\2\2\u00bb\u00bc")
        buf.write("\7t\2\2\u00bc\30\3\2\2\2\u00bd\u00be\7f\2\2\u00be\u00bf")
        buf.write("\7{\2\2\u00bf\u00c0\7p\2\2\u00c0\u00c1\7c\2\2\u00c1\u00c2")
        buf.write("\7o\2\2\u00c2\u00c3\7k\2\2\u00c3\u00c4\7e\2\2\u00c4\32")
        buf.write("\3\2\2\2\u00c5\u00c6\7d\2\2\u00c6\u00c7\7{\2\2\u00c7\34")
        buf.write("\3\2\2\2\u00c8\u00c9\7g\2\2\u00c9\u00ca\7n\2\2\u00ca\u00cb")
        buf.write("\7k\2\2\u00cb\u00cc\7h\2\2\u00cc\36\3\2\2\2\u00cd\u00ce")
        buf.write("\7q\2\2\u00ce\u00cf\7t\2\2\u00cf \3\2\2\2\u00d0\u00d1")
        buf.write("\7d\2\2\u00d1\u00d2\7q\2\2\u00d2\u00d3\7q\2\2\u00d3\u00d4")
        buf.write("\7n\2\2\u00d4\"\3\2\2\2\u00d5\u00d6\7h\2\2\u00d6\u00d7")
        buf.write("\7w\2\2\u00d7\u00d8\7p\2\2\u00d8\u00d9\7e\2\2\u00d9$\3")
        buf.write("\2\2\2\u00da\u00db\7d\2\2\u00db\u00dc\7t\2\2\u00dc\u00dd")
        buf.write("\7g\2\2\u00dd\u00de\7c\2\2\u00de\u00df\7m\2\2\u00df&\3")
        buf.write("\2\2\2\u00e0\u00e1\7d\2\2\u00e1\u00e2\7g\2\2\u00e2\u00e3")
        buf.write("\7i\2\2\u00e3\u00e4\7k\2\2\u00e4\u00e5\7p\2\2\u00e5(\3")
        buf.write("\2\2\2\u00e6\u00e7\7u\2\2\u00e7\u00e8\7v\2\2\u00e8\u00e9")
        buf.write("\7t\2\2\u00e9\u00ea\7k\2\2\u00ea\u00eb\7p\2\2\u00eb\u00ec")
        buf.write("\7i\2\2\u00ec*\3\2\2\2\u00ed\u00ee\7e\2\2\u00ee\u00ef")
        buf.write("\7q\2\2\u00ef\u00f0\7p\2\2\u00f0\u00f1\7v\2\2\u00f1\u00f2")
        buf.write("\7k\2\2\u00f2\u00f3\7p\2\2\u00f3\u00f4\7w\2\2\u00f4\u00f5")
        buf.write("\7g\2\2\u00f5,\3\2\2\2\u00f6\u00f7\7g\2\2\u00f7\u00f8")
        buf.write("\7p\2\2\u00f8\u00f9\7f\2\2\u00f9.\3\2\2\2\u00fa\u00fb")
        buf.write("\7c\2\2\u00fb\u00fc\7t\2\2\u00fc\u00fd\7t\2\2\u00fd\u00fe")
        buf.write("\7c\2\2\u00fe\u00ff\7{\2\2\u00ff\60\3\2\2\2\u0100\u0101")
        buf.write("\7-\2\2\u0101\62\3\2\2\2\u0102\u0103\7/\2\2\u0103\64\3")
        buf.write("\2\2\2\u0104\u0105\7,\2\2\u0105\66\3\2\2\2\u0106\u0107")
        buf.write("\7\61\2\2\u01078\3\2\2\2\u0108\u0109\7\'\2\2\u0109:\3")
        buf.write("\2\2\2\u010a\u010b\7?\2\2\u010b\u010c\7?\2\2\u010c<\3")
        buf.write("\2\2\2\u010d\u010e\7?\2\2\u010e>\3\2\2\2\u010f\u0110\7")
        buf.write(">\2\2\u0110\u0111\7/\2\2\u0111@\3\2\2\2\u0112\u0113\7")
        buf.write("#\2\2\u0113\u0114\7?\2\2\u0114B\3\2\2\2\u0115\u0116\7")
        buf.write(">\2\2\u0116\u0117\7?\2\2\u0117D\3\2\2\2\u0118\u0119\7")
        buf.write("@\2\2\u0119\u011a\7?\2\2\u011aF\3\2\2\2\u011b\u011c\7")
        buf.write(">\2\2\u011cH\3\2\2\2\u011d\u011e\7@\2\2\u011eJ\3\2\2\2")
        buf.write("\u011f\u0120\7\60\2\2\u0120\u0121\7\60\2\2\u0121\u0122")
        buf.write("\7\60\2\2\u0122L\3\2\2\2\u0123\u0124\7*\2\2\u0124N\3\2")
        buf.write("\2\2\u0125\u0126\7+\2\2\u0126P\3\2\2\2\u0127\u0128\7]")
        buf.write("\2\2\u0128R\3\2\2\2\u0129\u012a\7_\2\2\u012aT\3\2\2\2")
        buf.write("\u012b\u012c\7.\2\2\u012cV\3\2\2\2\u012d\u012e\7<\2\2")
        buf.write("\u012eX\3\2\2\2\u012f\u0130\7=\2\2\u0130Z\3\2\2\2\u0131")
        buf.write("\u0132\t\3\2\2\u0132\\\3\2\2\2\u0133\u013a\5_\60\2\u0134")
        buf.write("\u0136\5a\61\2\u0135\u0134\3\2\2\2\u0135\u0136\3\2\2\2")
        buf.write("\u0136\u0138\3\2\2\2\u0137\u0139\5c\62\2\u0138\u0137\3")
        buf.write("\2\2\2\u0138\u0139\3\2\2\2\u0139\u013b\3\2\2\2\u013a\u0135")
        buf.write("\3\2\2\2\u013a\u013b\3\2\2\2\u013b^\3\2\2\2\u013c\u013e")
        buf.write("\t\4\2\2\u013d\u013c\3\2\2\2\u013e\u013f\3\2\2\2\u013f")
        buf.write("\u013d\3\2\2\2\u013f\u0140\3\2\2\2\u0140`\3\2\2\2\u0141")
        buf.write("\u0145\7\60\2\2\u0142\u0144\t\4\2\2\u0143\u0142\3\2\2")
        buf.write("\2\u0144\u0147\3\2\2\2\u0145\u0143\3\2\2\2\u0145\u0146")
        buf.write("\3\2\2\2\u0146b\3\2\2\2\u0147\u0145\3\2\2\2\u0148\u014a")
        buf.write("\t\5\2\2\u0149\u014b\t\6\2\2\u014a\u0149\3\2\2\2\u014a")
        buf.write("\u014b\3\2\2\2\u014b\u014d\3\2\2\2\u014c\u014e\t\4\2\2")
        buf.write("\u014d\u014c\3\2\2\2\u014e\u014f\3\2\2\2\u014f\u014d\3")
        buf.write("\2\2\2\u014f\u0150\3\2\2\2\u0150d\3\2\2\2\u0151\u0155")
        buf.write("\5g\64\2\u0152\u0154\5k\66\2\u0153\u0152\3\2\2\2\u0154")
        buf.write("\u0157\3\2\2\2\u0155\u0153\3\2\2\2\u0155\u0156\3\2\2\2")
        buf.write("\u0156\u0158\3\2\2\2\u0157\u0155\3\2\2\2\u0158\u0159\5")
        buf.write("g\64\2\u0159\u015a\b\63\3\2\u015af\3\2\2\2\u015b\u015c")
        buf.write("\7$\2\2\u015ch\3\2\2\2\u015d\u015e\7^\2\2\u015e\u015f")
        buf.write("\n\7\2\2\u015fj\3\2\2\2\u0160\u0165\5m\67\2\u0161\u0162")
        buf.write("\7)\2\2\u0162\u0165\7$\2\2\u0163\u0165\n\b\2\2\u0164\u0160")
        buf.write("\3\2\2\2\u0164\u0161\3\2\2\2\u0164\u0163\3\2\2\2\u0165")
        buf.write("l\3\2\2\2\u0166\u0167\7^\2\2\u0167\u0168\t\7\2\2\u0168")
        buf.write("n\3\2\2\2\u0169\u016b\t\4\2\2\u016a\u0169\3\2\2\2\u016b")
        buf.write("\u016c\3\2\2\2\u016c\u016a\3\2\2\2\u016c\u016d\3\2\2\2")
        buf.write("\u016dp\3\2\2\2\u016e\u0172\t\t\2\2\u016f\u0171\t\n\2")
        buf.write("\2\u0170\u016f\3\2\2\2\u0171\u0174\3\2\2\2\u0172\u0170")
        buf.write("\3\2\2\2\u0172\u0173\3\2\2\2\u0173r\3\2\2\2\u0174\u0172")
        buf.write("\3\2\2\2\u0175\u0177\t\13\2\2\u0176\u0175\3\2\2\2\u0177")
        buf.write("\u0178\3\2\2\2\u0178\u0176\3\2\2\2\u0178\u0179\3\2\2\2")
        buf.write("\u0179\u017a\3\2\2\2\u017a\u017b\b:\2\2\u017bt\3\2\2\2")
        buf.write("\u017c\u0180\7$\2\2\u017d\u017f\5k\66\2\u017e\u017d\3")
        buf.write("\2\2\2\u017f\u0182\3\2\2\2\u0180\u017e\3\2\2\2\u0180\u0181")
        buf.write("\3\2\2\2\u0181\u0184\3\2\2\2\u0182\u0180\3\2\2\2\u0183")
        buf.write("\u0185\t\f\2\2\u0184\u0183\3\2\2\2\u0185\u0186\3\2\2\2")
        buf.write("\u0186\u0187\b;\4\2\u0187v\3\2\2\2\u0188\u018c\7$\2\2")
        buf.write("\u0189\u018b\5k\66\2\u018a\u0189\3\2\2\2\u018b\u018e\3")
        buf.write("\2\2\2\u018c\u018a\3\2\2\2\u018c\u018d\3\2\2\2\u018d\u018f")
        buf.write("\3\2\2\2\u018e\u018c\3\2\2\2\u018f\u0190\5i\65\2\u0190")
        buf.write("\u0191\b<\5\2\u0191x\3\2\2\2\u0192\u0193\13\2\2\2\u0193")
        buf.write("\u0194\b=\6\2\u0194z\3\2\2\2\24\2\u0081\u008f\u0135\u0138")
        buf.write("\u013a\u013f\u0145\u014a\u014f\u0155\u0164\u016c\u0172")
        buf.write("\u0178\u0180\u0184\u018c\7\b\2\2\3\63\2\3;\3\3<\4\3=\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ZCODE_COMMENT = 1
    BOOLEAN_LITERAL = 2
    RETURN = 3
    FOR = 4
    IF = 5
    NOT = 6
    VAR = 7
    UNTIL = 8
    ELSE = 9
    AND = 10
    NUMBER = 11
    DYNAMIC = 12
    BY = 13
    ELIF = 14
    OR = 15
    BOOL = 16
    FUNC = 17
    BREAK = 18
    BEGIN = 19
    STRING = 20
    CONTINUE = 21
    END = 22
    ARRAY = 23
    PLUS = 24
    MINUS = 25
    TIMES = 26
    DIVIDED = 27
    MOD = 28
    COMPARE = 29
    EQUAL = 30
    ASSIGN = 31
    NOT_EQUAL = 32
    LTOE = 33
    GTOE = 34
    LT = 35
    GT = 36
    CONCATENATION = 37
    LEFTPAREN = 38
    RIGHTPAREN = 39
    LEFTBRACKET = 40
    RIGHTBRACKET = 41
    COMMA = 42
    NL = 43
    NUMBER_LITERAL = 44
    STRING_LITERAL = 45
    IDENTIFIER = 46
    WS = 47
    UNCLOSE_STRING = 48
    ILLEGAL_ESCAPE = 49
    ERROR_CHAR = 50

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'return'", "'for'", "'if'", "'not'", "'var'", "'until'", "'else'", 
            "'and'", "'number'", "'dynamic'", "'by'", "'elif'", "'or'", 
            "'bool'", "'func'", "'break'", "'begin'", "'string'", "'continue'", 
            "'end'", "'array'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
            "'='", "'<-'", "'!='", "'<='", "'>='", "'<'", "'>'", "'...'", 
            "'('", "')'", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>",
            "ZCODE_COMMENT", "BOOLEAN_LITERAL", "RETURN", "FOR", "IF", "NOT", 
            "VAR", "UNTIL", "ELSE", "AND", "NUMBER", "DYNAMIC", "BY", "ELIF", 
            "OR", "BOOL", "FUNC", "BREAK", "BEGIN", "STRING", "CONTINUE", 
            "END", "ARRAY", "PLUS", "MINUS", "TIMES", "DIVIDED", "MOD", 
            "COMPARE", "EQUAL", "ASSIGN", "NOT_EQUAL", "LTOE", "GTOE", "LT", 
            "GT", "CONCATENATION", "LEFTPAREN", "RIGHTPAREN", "LEFTBRACKET", 
            "RIGHTBRACKET", "COMMA", "NL", "NUMBER_LITERAL", "STRING_LITERAL", 
            "IDENTIFIER", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "ZCODE_COMMENT", "BOOLEAN_LITERAL", "RETURN", "FOR", "IF", 
                  "NOT", "VAR", "UNTIL", "ELSE", "AND", "NUMBER", "DYNAMIC", 
                  "BY", "ELIF", "OR", "BOOL", "FUNC", "BREAK", "BEGIN", 
                  "STRING", "CONTINUE", "END", "ARRAY", "PLUS", "MINUS", 
                  "TIMES", "DIVIDED", "MOD", "COMPARE", "EQUAL", "ASSIGN", 
                  "NOT_EQUAL", "LTOE", "GTOE", "LT", "GT", "CONCATENATION", 
                  "LEFTPAREN", "RIGHTPAREN", "LEFTBRACKET", "RIGHTBRACKET", 
                  "COMMA", "COLON", "SEMI", "NL", "NUMBER_LITERAL", "INTEGERPART", 
                  "DECIMALPART", "EXPONENTPART", "STRING_LITERAL", "DOUBLEQUOTE", 
                  "INVALID_ESC", "CHAR", "ESC", "SIZE", "IDENTIFIER", "WS", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

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
            actions[49] = self.STRING_LITERAL_action 
            actions[57] = self.UNCLOSE_STRING_action 
            actions[58] = self.ILLEGAL_ESCAPE_action 
            actions[59] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text =self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            	if self.text[-1] in ['\n','\r','EOF']:
            		raise UncloseString(self.text[1:-1])
            	else:
            		raise UncloseString(self.text[1:])
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	illegal_str_from_beginning = str(self.text)
            	raise IllegalEscape(illegal_str_from_beginning[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


