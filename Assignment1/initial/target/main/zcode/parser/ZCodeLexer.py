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
        buf.write("\2\u0083\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3")
        buf.write("\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n")
        buf.write("\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\31")
        buf.write("\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#")
        buf.write("\3#\3$\3$\3%\3%\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*")
        buf.write("\3+\3+\3,\3,\3-\3-\3.\3.\5.\u012b\n.\3.\5.\u012e\n.\5")
        buf.write(".\u0130\n.\3/\6/\u0133\n/\r/\16/\u0134\3\60\3\60\7\60")
        buf.write("\u0139\n\60\f\60\16\60\u013c\13\60\3\61\3\61\5\61\u0140")
        buf.write("\n\61\3\61\6\61\u0143\n\61\r\61\16\61\u0144\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\5\62\u0150\n\62\3")
        buf.write("\63\3\63\7\63\u0154\n\63\f\63\16\63\u0157\13\63\3\63\3")
        buf.write("\63\3\63\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\66\3\66")
        buf.write("\5\66\u0165\n\66\3\67\3\67\3\67\38\68\u016b\n8\r8\168")
        buf.write("\u016c\39\39\79\u0171\n9\f9\169\u0174\139\3:\6:\u0177")
        buf.write("\n:\r:\16:\u0178\3:\3:\3;\3;\7;\u017f\n;\f;\16;\u0182")
        buf.write("\13;\3;\5;\u0185\n;\3;\3;\3<\3<\7<\u018b\n<\f<\16<\u018e")
        buf.write("\13<\3<\3<\3<\3=\3=\3=\2\2>\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U\2W\2Y,[-]\2_\2a\2c.e/")
        buf.write("g\2i\2k\2m\2o\2q\60s\61u\62w\63y\64\3\2\r\4\2\f\f\17\17")
        buf.write("\3\2\f\f\3\2\62;\4\2GGgg\4\2--//\t\2))^^ddhhppttvv\6\2")
        buf.write("\f\f\17\17$$^^\5\2C\\aac|\6\2\62;C\\aac|\5\2\n\13\16\17")
        buf.write("\"\"\4\3\f\f\17\17\2\u019b\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2")
        buf.write("\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2")
        buf.write("\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2")
        buf.write("\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2")
        buf.write("w\3\2\2\2\2y\3\2\2\2\3{\3\2\2\2\5\u0086\3\2\2\2\7\u008d")
        buf.write("\3\2\2\2\t\u0091\3\2\2\2\13\u0094\3\2\2\2\r\u0098\3\2")
        buf.write("\2\2\17\u009c\3\2\2\2\21\u00a2\3\2\2\2\23\u00a7\3\2\2")
        buf.write("\2\25\u00ab\3\2\2\2\27\u00b2\3\2\2\2\31\u00ba\3\2\2\2")
        buf.write("\33\u00bd\3\2\2\2\35\u00c2\3\2\2\2\37\u00c5\3\2\2\2!\u00ca")
        buf.write("\3\2\2\2#\u00cf\3\2\2\2%\u00d5\3\2\2\2\'\u00db\3\2\2\2")
        buf.write(")\u00e2\3\2\2\2+\u00eb\3\2\2\2-\u00ef\3\2\2\2/\u00f5\3")
        buf.write("\2\2\2\61\u00f7\3\2\2\2\63\u00f9\3\2\2\2\65\u00fb\3\2")
        buf.write("\2\2\67\u00fd\3\2\2\29\u00ff\3\2\2\2;\u0102\3\2\2\2=\u0104")
        buf.write("\3\2\2\2?\u0107\3\2\2\2A\u010a\3\2\2\2C\u010d\3\2\2\2")
        buf.write("E\u0110\3\2\2\2G\u0112\3\2\2\2I\u0114\3\2\2\2K\u0118\3")
        buf.write("\2\2\2M\u011a\3\2\2\2O\u011c\3\2\2\2Q\u011e\3\2\2\2S\u0120")
        buf.write("\3\2\2\2U\u0122\3\2\2\2W\u0124\3\2\2\2Y\u0126\3\2\2\2")
        buf.write("[\u0128\3\2\2\2]\u0132\3\2\2\2_\u0136\3\2\2\2a\u013d\3")
        buf.write("\2\2\2c\u014f\3\2\2\2e\u0151\3\2\2\2g\u015b\3\2\2\2i\u015d")
        buf.write("\3\2\2\2k\u0164\3\2\2\2m\u0166\3\2\2\2o\u016a\3\2\2\2")
        buf.write("q\u016e\3\2\2\2s\u0176\3\2\2\2u\u017c\3\2\2\2w\u0188\3")
        buf.write("\2\2\2y\u0192\3\2\2\2{|\7%\2\2|}\7%\2\2}\u0081\3\2\2\2")
        buf.write("~\u0080\n\2\2\2\177~\3\2\2\2\u0080\u0083\3\2\2\2\u0081")
        buf.write("\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0084\3\2\2\2\u0083")
        buf.write("\u0081\3\2\2\2\u0084\u0085\b\2\2\2\u0085\4\3\2\2\2\u0086")
        buf.write("\u0087\7t\2\2\u0087\u0088\7g\2\2\u0088\u0089\7v\2\2\u0089")
        buf.write("\u008a\7w\2\2\u008a\u008b\7t\2\2\u008b\u008c\7p\2\2\u008c")
        buf.write("\6\3\2\2\2\u008d\u008e\7h\2\2\u008e\u008f\7q\2\2\u008f")
        buf.write("\u0090\7t\2\2\u0090\b\3\2\2\2\u0091\u0092\7k\2\2\u0092")
        buf.write("\u0093\7h\2\2\u0093\n\3\2\2\2\u0094\u0095\7P\2\2\u0095")
        buf.write("\u0096\7Q\2\2\u0096\u0097\7V\2\2\u0097\f\3\2\2\2\u0098")
        buf.write("\u0099\7x\2\2\u0099\u009a\7c\2\2\u009a\u009b\7t\2\2\u009b")
        buf.write("\16\3\2\2\2\u009c\u009d\7w\2\2\u009d\u009e\7p\2\2\u009e")
        buf.write("\u009f\7v\2\2\u009f\u00a0\7k\2\2\u00a0\u00a1\7n\2\2\u00a1")
        buf.write("\20\3\2\2\2\u00a2\u00a3\7g\2\2\u00a3\u00a4\7n\2\2\u00a4")
        buf.write("\u00a5\7u\2\2\u00a5\u00a6\7g\2\2\u00a6\22\3\2\2\2\u00a7")
        buf.write("\u00a8\7c\2\2\u00a8\u00a9\7p\2\2\u00a9\u00aa\7f\2\2\u00aa")
        buf.write("\24\3\2\2\2\u00ab\u00ac\7p\2\2\u00ac\u00ad\7w\2\2\u00ad")
        buf.write("\u00ae\7o\2\2\u00ae\u00af\7d\2\2\u00af\u00b0\7g\2\2\u00b0")
        buf.write("\u00b1\7t\2\2\u00b1\26\3\2\2\2\u00b2\u00b3\7f\2\2\u00b3")
        buf.write("\u00b4\7{\2\2\u00b4\u00b5\7p\2\2\u00b5\u00b6\7c\2\2\u00b6")
        buf.write("\u00b7\7o\2\2\u00b7\u00b8\7k\2\2\u00b8\u00b9\7e\2\2\u00b9")
        buf.write("\30\3\2\2\2\u00ba\u00bb\7d\2\2\u00bb\u00bc\7{\2\2\u00bc")
        buf.write("\32\3\2\2\2\u00bd\u00be\7g\2\2\u00be\u00bf\7n\2\2\u00bf")
        buf.write("\u00c0\7k\2\2\u00c0\u00c1\7h\2\2\u00c1\34\3\2\2\2\u00c2")
        buf.write("\u00c3\7q\2\2\u00c3\u00c4\7t\2\2\u00c4\36\3\2\2\2\u00c5")
        buf.write("\u00c6\7d\2\2\u00c6\u00c7\7q\2\2\u00c7\u00c8\7q\2\2\u00c8")
        buf.write("\u00c9\7n\2\2\u00c9 \3\2\2\2\u00ca\u00cb\7h\2\2\u00cb")
        buf.write("\u00cc\7w\2\2\u00cc\u00cd\7p\2\2\u00cd\u00ce\7e\2\2\u00ce")
        buf.write("\"\3\2\2\2\u00cf\u00d0\7d\2\2\u00d0\u00d1\7t\2\2\u00d1")
        buf.write("\u00d2\7g\2\2\u00d2\u00d3\7c\2\2\u00d3\u00d4\7m\2\2\u00d4")
        buf.write("$\3\2\2\2\u00d5\u00d6\7d\2\2\u00d6\u00d7\7g\2\2\u00d7")
        buf.write("\u00d8\7i\2\2\u00d8\u00d9\7k\2\2\u00d9\u00da\7p\2\2\u00da")
        buf.write("&\3\2\2\2\u00db\u00dc\7u\2\2\u00dc\u00dd\7v\2\2\u00dd")
        buf.write("\u00de\7t\2\2\u00de\u00df\7k\2\2\u00df\u00e0\7p\2\2\u00e0")
        buf.write("\u00e1\7i\2\2\u00e1(\3\2\2\2\u00e2\u00e3\7e\2\2\u00e3")
        buf.write("\u00e4\7q\2\2\u00e4\u00e5\7p\2\2\u00e5\u00e6\7v\2\2\u00e6")
        buf.write("\u00e7\7k\2\2\u00e7\u00e8\7p\2\2\u00e8\u00e9\7w\2\2\u00e9")
        buf.write("\u00ea\7g\2\2\u00ea*\3\2\2\2\u00eb\u00ec\7g\2\2\u00ec")
        buf.write("\u00ed\7p\2\2\u00ed\u00ee\7f\2\2\u00ee,\3\2\2\2\u00ef")
        buf.write("\u00f0\7c\2\2\u00f0\u00f1\7t\2\2\u00f1\u00f2\7t\2\2\u00f2")
        buf.write("\u00f3\7c\2\2\u00f3\u00f4\7{\2\2\u00f4.\3\2\2\2\u00f5")
        buf.write("\u00f6\7-\2\2\u00f6\60\3\2\2\2\u00f7\u00f8\7/\2\2\u00f8")
        buf.write("\62\3\2\2\2\u00f9\u00fa\7,\2\2\u00fa\64\3\2\2\2\u00fb")
        buf.write("\u00fc\7\61\2\2\u00fc\66\3\2\2\2\u00fd\u00fe\7\'\2\2\u00fe")
        buf.write("8\3\2\2\2\u00ff\u0100\7?\2\2\u0100\u0101\7?\2\2\u0101")
        buf.write(":\3\2\2\2\u0102\u0103\7?\2\2\u0103<\3\2\2\2\u0104\u0105")
        buf.write("\7>\2\2\u0105\u0106\7/\2\2\u0106>\3\2\2\2\u0107\u0108")
        buf.write("\7#\2\2\u0108\u0109\7?\2\2\u0109@\3\2\2\2\u010a\u010b")
        buf.write("\7>\2\2\u010b\u010c\7?\2\2\u010cB\3\2\2\2\u010d\u010e")
        buf.write("\7@\2\2\u010e\u010f\7?\2\2\u010fD\3\2\2\2\u0110\u0111")
        buf.write("\7>\2\2\u0111F\3\2\2\2\u0112\u0113\7@\2\2\u0113H\3\2\2")
        buf.write("\2\u0114\u0115\7\60\2\2\u0115\u0116\7\60\2\2\u0116\u0117")
        buf.write("\7\60\2\2\u0117J\3\2\2\2\u0118\u0119\7*\2\2\u0119L\3\2")
        buf.write("\2\2\u011a\u011b\7+\2\2\u011bN\3\2\2\2\u011c\u011d\7]")
        buf.write("\2\2\u011dP\3\2\2\2\u011e\u011f\7_\2\2\u011fR\3\2\2\2")
        buf.write("\u0120\u0121\7.\2\2\u0121T\3\2\2\2\u0122\u0123\7<\2\2")
        buf.write("\u0123V\3\2\2\2\u0124\u0125\7=\2\2\u0125X\3\2\2\2\u0126")
        buf.write("\u0127\t\3\2\2\u0127Z\3\2\2\2\u0128\u012f\5]/\2\u0129")
        buf.write("\u012b\5_\60\2\u012a\u0129\3\2\2\2\u012a\u012b\3\2\2\2")
        buf.write("\u012b\u012d\3\2\2\2\u012c\u012e\5a\61\2\u012d\u012c\3")
        buf.write("\2\2\2\u012d\u012e\3\2\2\2\u012e\u0130\3\2\2\2\u012f\u012a")
        buf.write("\3\2\2\2\u012f\u0130\3\2\2\2\u0130\\\3\2\2\2\u0131\u0133")
        buf.write("\t\4\2\2\u0132\u0131\3\2\2\2\u0133\u0134\3\2\2\2\u0134")
        buf.write("\u0132\3\2\2\2\u0134\u0135\3\2\2\2\u0135^\3\2\2\2\u0136")
        buf.write("\u013a\7\60\2\2\u0137\u0139\t\4\2\2\u0138\u0137\3\2\2")
        buf.write("\2\u0139\u013c\3\2\2\2\u013a\u0138\3\2\2\2\u013a\u013b")
        buf.write("\3\2\2\2\u013b`\3\2\2\2\u013c\u013a\3\2\2\2\u013d\u013f")
        buf.write("\t\5\2\2\u013e\u0140\t\6\2\2\u013f\u013e\3\2\2\2\u013f")
        buf.write("\u0140\3\2\2\2\u0140\u0142\3\2\2\2\u0141\u0143\t\4\2\2")
        buf.write("\u0142\u0141\3\2\2\2\u0143\u0144\3\2\2\2\u0144\u0142\3")
        buf.write("\2\2\2\u0144\u0145\3\2\2\2\u0145b\3\2\2\2\u0146\u0147")
        buf.write("\7v\2\2\u0147\u0148\7t\2\2\u0148\u0149\7w\2\2\u0149\u0150")
        buf.write("\7g\2\2\u014a\u014b\7h\2\2\u014b\u014c\7c\2\2\u014c\u014d")
        buf.write("\7n\2\2\u014d\u014e\7u\2\2\u014e\u0150\7g\2\2\u014f\u0146")
        buf.write("\3\2\2\2\u014f\u014a\3\2\2\2\u0150d\3\2\2\2\u0151\u0155")
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
        buf.write("\u0194\b=\6\2\u0194z\3\2\2\2\24\2\u0081\u012a\u012d\u012f")
        buf.write("\u0134\u013a\u013f\u0144\u014f\u0155\u0164\u016c\u0172")
        buf.write("\u0178\u0180\u0184\u018c\7\b\2\2\3\63\2\3;\3\3<\4\3=\5")
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
    COMPARE = 28
    EQUAL = 29
    ASSIGN = 30
    NOT_EQUAL = 31
    LTOE = 32
    GTOE = 33
    LT = 34
    GT = 35
    CONCATENATION = 36
    LEFTPAREN = 37
    RIGHTPAREN = 38
    LEFTBRACKET = 39
    RIGHTBRACKET = 40
    COMMA = 41
    NL = 42
    NUMBER_LITERAL = 43
    BOOLEAN_LITERAL = 44
    STRING_LITERAL = 45
    IDENTIFIER = 46
    WS = 47
    UNCLOSE_STRING = 48
    ILLEGAL_ESCAPE = 49
    ERROR_CHAR = 50

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'return'", "'for'", "'if'", "'NOT'", "'var'", "'until'", "'else'", 
            "'and'", "'number'", "'dynamic'", "'by'", "'elif'", "'or'", 
            "'bool'", "'func'", "'break'", "'begin'", "'string'", "'continue'", 
            "'end'", "'array'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
            "'='", "'<-'", "'!='", "'<='", "'>='", "'<'", "'>'", "'...'", 
            "'('", "')'", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>",
            "ZCODE_COMMENT", "RETURN", "FOR", "IF", "NOT", "VAR", "UNTIL", 
            "ELSE", "AND", "NUMBER", "DYNAMIC", "BY", "ELIF", "OR", "BOOL", 
            "FUNC", "BREAK", "BEGIN", "STRING", "CONTINUE", "END", "ARRAY", 
            "PLUS", "MINUS", "TIMES", "DIVIDED", "MOD", "COMPARE", "EQUAL", 
            "ASSIGN", "NOT_EQUAL", "LTOE", "GTOE", "LT", "GT", "CONCATENATION", 
            "LEFTPAREN", "RIGHTPAREN", "LEFTBRACKET", "RIGHTBRACKET", "COMMA", 
            "NL", "NUMBER_LITERAL", "BOOLEAN_LITERAL", "STRING_LITERAL", 
            "IDENTIFIER", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "ZCODE_COMMENT", "RETURN", "FOR", "IF", "NOT", "VAR", 
                  "UNTIL", "ELSE", "AND", "NUMBER", "DYNAMIC", "BY", "ELIF", 
                  "OR", "BOOL", "FUNC", "BREAK", "BEGIN", "STRING", "CONTINUE", 
                  "END", "ARRAY", "PLUS", "MINUS", "TIMES", "DIVIDED", "MOD", 
                  "COMPARE", "EQUAL", "ASSIGN", "NOT_EQUAL", "LTOE", "GTOE", 
                  "LT", "GT", "CONCATENATION", "LEFTPAREN", "RIGHTPAREN", 
                  "LEFTBRACKET", "RIGHTBRACKET", "COMMA", "COLON", "SEMI", 
                  "NL", "NUMBER_LITERAL", "INTEGERPART", "DECIMALPART", 
                  "EXPONENTPART", "BOOLEAN_LITERAL", "STRING_LITERAL", "DOUBLEQUOTE", 
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
     


