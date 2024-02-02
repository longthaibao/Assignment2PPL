# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


# 2113946 - Thai Bao Long
from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\63")
        buf.write("\u0185\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\3\2\3\2\3\2\3\2\7\2z\n\2\f\2\16\2}\13\2\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u008a\n\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7")
        buf.write("\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3")
        buf.write("%\3%\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3")
        buf.write(",\5,\u0126\n,\3,\5,\u0129\n,\5,\u012b\n,\3-\6-\u012e\n")
        buf.write("-\r-\16-\u012f\3.\3.\7.\u0134\n.\f.\16.\u0137\13.\3/\3")
        buf.write("/\5/\u013b\n/\3/\6/\u013e\n/\r/\16/\u013f\3\60\3\60\7")
        buf.write("\60\u0144\n\60\f\60\16\60\u0147\13\60\3\60\3\60\3\60\3")
        buf.write("\61\3\61\3\62\3\62\3\62\3\63\3\63\3\63\3\63\5\63\u0155")
        buf.write("\n\63\3\64\3\64\3\64\3\65\6\65\u015b\n\65\r\65\16\65\u015c")
        buf.write("\3\66\3\66\7\66\u0161\n\66\f\66\16\66\u0164\13\66\3\67")
        buf.write("\6\67\u0167\n\67\r\67\16\67\u0168\3\67\3\67\38\38\78\u016f")
        buf.write("\n8\f8\168\u0172\138\38\58\u0175\n8\38\38\39\39\79\u017b")
        buf.write("\n9\f9\169\u017e\139\39\39\39\3:\3:\3:\2\2;\3\3\5\4\7")
        buf.write("\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-")
        buf.write("Y\2[\2]\2_.a\2c\2e\2g\2i\2k/m\60o\61q\62s\63\3\2\r\4\2")
        buf.write("\f\f\17\17\3\2\f\f\3\2\62;\4\2GGgg\4\2--//\t\2))^^ddh")
        buf.write("hppttvv\6\2\f\f\17\17$$^^\5\2C\\aac|\6\2\62;C\\aac|\5")
        buf.write("\2\n\13\16\17\"\"\4\3\f\f\17\17\2\u018d\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3")
        buf.write("\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2_\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2")
        buf.write("\2q\3\2\2\2\2s\3\2\2\2\3u\3\2\2\2\5\u0089\3\2\2\2\7\u008b")
        buf.write("\3\2\2\2\t\u0092\3\2\2\2\13\u0096\3\2\2\2\r\u0099\3\2")
        buf.write("\2\2\17\u009d\3\2\2\2\21\u00a1\3\2\2\2\23\u00a7\3\2\2")
        buf.write("\2\25\u00ac\3\2\2\2\27\u00b0\3\2\2\2\31\u00b7\3\2\2\2")
        buf.write("\33\u00bf\3\2\2\2\35\u00c2\3\2\2\2\37\u00c7\3\2\2\2!\u00ca")
        buf.write("\3\2\2\2#\u00cf\3\2\2\2%\u00d4\3\2\2\2\'\u00da\3\2\2\2")
        buf.write(")\u00e0\3\2\2\2+\u00e7\3\2\2\2-\u00f0\3\2\2\2/\u00f4\3")
        buf.write("\2\2\2\61\u00f6\3\2\2\2\63\u00f8\3\2\2\2\65\u00fa\3\2")
        buf.write("\2\2\67\u00fc\3\2\2\29\u00fe\3\2\2\2;\u0101\3\2\2\2=\u0103")
        buf.write("\3\2\2\2?\u0106\3\2\2\2A\u0109\3\2\2\2C\u010c\3\2\2\2")
        buf.write("E\u010f\3\2\2\2G\u0111\3\2\2\2I\u0113\3\2\2\2K\u0117\3")
        buf.write("\2\2\2M\u0119\3\2\2\2O\u011b\3\2\2\2Q\u011d\3\2\2\2S\u011f")
        buf.write("\3\2\2\2U\u0121\3\2\2\2W\u0123\3\2\2\2Y\u012d\3\2\2\2")
        buf.write("[\u0131\3\2\2\2]\u0138\3\2\2\2_\u0141\3\2\2\2a\u014b\3")
        buf.write("\2\2\2c\u014d\3\2\2\2e\u0154\3\2\2\2g\u0156\3\2\2\2i\u015a")
        buf.write("\3\2\2\2k\u015e\3\2\2\2m\u0166\3\2\2\2o\u016c\3\2\2\2")
        buf.write("q\u0178\3\2\2\2s\u0182\3\2\2\2uv\7%\2\2vw\7%\2\2w{\3\2")
        buf.write("\2\2xz\n\2\2\2yx\3\2\2\2z}\3\2\2\2{y\3\2\2\2{|\3\2\2\2")
        buf.write("|~\3\2\2\2}{\3\2\2\2~\177\b\2\2\2\177\4\3\2\2\2\u0080")
        buf.write("\u0081\7v\2\2\u0081\u0082\7t\2\2\u0082\u0083\7w\2\2\u0083")
        buf.write("\u008a\7g\2\2\u0084\u0085\7h\2\2\u0085\u0086\7c\2\2\u0086")
        buf.write("\u0087\7n\2\2\u0087\u0088\7u\2\2\u0088\u008a\7g\2\2\u0089")
        buf.write("\u0080\3\2\2\2\u0089\u0084\3\2\2\2\u008a\6\3\2\2\2\u008b")
        buf.write("\u008c\7t\2\2\u008c\u008d\7g\2\2\u008d\u008e\7v\2\2\u008e")
        buf.write("\u008f\7w\2\2\u008f\u0090\7t\2\2\u0090\u0091\7p\2\2\u0091")
        buf.write("\b\3\2\2\2\u0092\u0093\7h\2\2\u0093\u0094\7q\2\2\u0094")
        buf.write("\u0095\7t\2\2\u0095\n\3\2\2\2\u0096\u0097\7k\2\2\u0097")
        buf.write("\u0098\7h\2\2\u0098\f\3\2\2\2\u0099\u009a\7p\2\2\u009a")
        buf.write("\u009b\7q\2\2\u009b\u009c\7v\2\2\u009c\16\3\2\2\2\u009d")
        buf.write("\u009e\7x\2\2\u009e\u009f\7c\2\2\u009f\u00a0\7t\2\2\u00a0")
        buf.write("\20\3\2\2\2\u00a1\u00a2\7w\2\2\u00a2\u00a3\7p\2\2\u00a3")
        buf.write("\u00a4\7v\2\2\u00a4\u00a5\7k\2\2\u00a5\u00a6\7n\2\2\u00a6")
        buf.write("\22\3\2\2\2\u00a7\u00a8\7g\2\2\u00a8\u00a9\7n\2\2\u00a9")
        buf.write("\u00aa\7u\2\2\u00aa\u00ab\7g\2\2\u00ab\24\3\2\2\2\u00ac")
        buf.write("\u00ad\7c\2\2\u00ad\u00ae\7p\2\2\u00ae\u00af\7f\2\2\u00af")
        buf.write("\26\3\2\2\2\u00b0\u00b1\7p\2\2\u00b1\u00b2\7w\2\2\u00b2")
        buf.write("\u00b3\7o\2\2\u00b3\u00b4\7d\2\2\u00b4\u00b5\7g\2\2\u00b5")
        buf.write("\u00b6\7t\2\2\u00b6\30\3\2\2\2\u00b7\u00b8\7f\2\2\u00b8")
        buf.write("\u00b9\7{\2\2\u00b9\u00ba\7p\2\2\u00ba\u00bb\7c\2\2\u00bb")
        buf.write("\u00bc\7o\2\2\u00bc\u00bd\7k\2\2\u00bd\u00be\7e\2\2\u00be")
        buf.write("\32\3\2\2\2\u00bf\u00c0\7d\2\2\u00c0\u00c1\7{\2\2\u00c1")
        buf.write("\34\3\2\2\2\u00c2\u00c3\7g\2\2\u00c3\u00c4\7n\2\2\u00c4")
        buf.write("\u00c5\7k\2\2\u00c5\u00c6\7h\2\2\u00c6\36\3\2\2\2\u00c7")
        buf.write("\u00c8\7q\2\2\u00c8\u00c9\7t\2\2\u00c9 \3\2\2\2\u00ca")
        buf.write("\u00cb\7d\2\2\u00cb\u00cc\7q\2\2\u00cc\u00cd\7q\2\2\u00cd")
        buf.write("\u00ce\7n\2\2\u00ce\"\3\2\2\2\u00cf\u00d0\7h\2\2\u00d0")
        buf.write("\u00d1\7w\2\2\u00d1\u00d2\7p\2\2\u00d2\u00d3\7e\2\2\u00d3")
        buf.write("$\3\2\2\2\u00d4\u00d5\7d\2\2\u00d5\u00d6\7t\2\2\u00d6")
        buf.write("\u00d7\7g\2\2\u00d7\u00d8\7c\2\2\u00d8\u00d9\7m\2\2\u00d9")
        buf.write("&\3\2\2\2\u00da\u00db\7d\2\2\u00db\u00dc\7g\2\2\u00dc")
        buf.write("\u00dd\7i\2\2\u00dd\u00de\7k\2\2\u00de\u00df\7p\2\2\u00df")
        buf.write("(\3\2\2\2\u00e0\u00e1\7u\2\2\u00e1\u00e2\7v\2\2\u00e2")
        buf.write("\u00e3\7t\2\2\u00e3\u00e4\7k\2\2\u00e4\u00e5\7p\2\2\u00e5")
        buf.write("\u00e6\7i\2\2\u00e6*\3\2\2\2\u00e7\u00e8\7e\2\2\u00e8")
        buf.write("\u00e9\7q\2\2\u00e9\u00ea\7p\2\2\u00ea\u00eb\7v\2\2\u00eb")
        buf.write("\u00ec\7k\2\2\u00ec\u00ed\7p\2\2\u00ed\u00ee\7w\2\2\u00ee")
        buf.write("\u00ef\7g\2\2\u00ef,\3\2\2\2\u00f0\u00f1\7g\2\2\u00f1")
        buf.write("\u00f2\7p\2\2\u00f2\u00f3\7f\2\2\u00f3.\3\2\2\2\u00f4")
        buf.write("\u00f5\7-\2\2\u00f5\60\3\2\2\2\u00f6\u00f7\7/\2\2\u00f7")
        buf.write("\62\3\2\2\2\u00f8\u00f9\7,\2\2\u00f9\64\3\2\2\2\u00fa")
        buf.write("\u00fb\7\61\2\2\u00fb\66\3\2\2\2\u00fc\u00fd\7\'\2\2\u00fd")
        buf.write("8\3\2\2\2\u00fe\u00ff\7?\2\2\u00ff\u0100\7?\2\2\u0100")
        buf.write(":\3\2\2\2\u0101\u0102\7?\2\2\u0102<\3\2\2\2\u0103\u0104")
        buf.write("\7>\2\2\u0104\u0105\7/\2\2\u0105>\3\2\2\2\u0106\u0107")
        buf.write("\7#\2\2\u0107\u0108\7?\2\2\u0108@\3\2\2\2\u0109\u010a")
        buf.write("\7>\2\2\u010a\u010b\7?\2\2\u010bB\3\2\2\2\u010c\u010d")
        buf.write("\7@\2\2\u010d\u010e\7?\2\2\u010eD\3\2\2\2\u010f\u0110")
        buf.write("\7>\2\2\u0110F\3\2\2\2\u0111\u0112\7@\2\2\u0112H\3\2\2")
        buf.write("\2\u0113\u0114\7\60\2\2\u0114\u0115\7\60\2\2\u0115\u0116")
        buf.write("\7\60\2\2\u0116J\3\2\2\2\u0117\u0118\7*\2\2\u0118L\3\2")
        buf.write("\2\2\u0119\u011a\7+\2\2\u011aN\3\2\2\2\u011b\u011c\7]")
        buf.write("\2\2\u011cP\3\2\2\2\u011d\u011e\7_\2\2\u011eR\3\2\2\2")
        buf.write("\u011f\u0120\7.\2\2\u0120T\3\2\2\2\u0121\u0122\t\3\2\2")
        buf.write("\u0122V\3\2\2\2\u0123\u012a\5Y-\2\u0124\u0126\5[.\2\u0125")
        buf.write("\u0124\3\2\2\2\u0125\u0126\3\2\2\2\u0126\u0128\3\2\2\2")
        buf.write("\u0127\u0129\5]/\2\u0128\u0127\3\2\2\2\u0128\u0129\3\2")
        buf.write("\2\2\u0129\u012b\3\2\2\2\u012a\u0125\3\2\2\2\u012a\u012b")
        buf.write("\3\2\2\2\u012bX\3\2\2\2\u012c\u012e\t\4\2\2\u012d\u012c")
        buf.write("\3\2\2\2\u012e\u012f\3\2\2\2\u012f\u012d\3\2\2\2\u012f")
        buf.write("\u0130\3\2\2\2\u0130Z\3\2\2\2\u0131\u0135\7\60\2\2\u0132")
        buf.write("\u0134\t\4\2\2\u0133\u0132\3\2\2\2\u0134\u0137\3\2\2\2")
        buf.write("\u0135\u0133\3\2\2\2\u0135\u0136\3\2\2\2\u0136\\\3\2\2")
        buf.write("\2\u0137\u0135\3\2\2\2\u0138\u013a\t\5\2\2\u0139\u013b")
        buf.write("\t\6\2\2\u013a\u0139\3\2\2\2\u013a\u013b\3\2\2\2\u013b")
        buf.write("\u013d\3\2\2\2\u013c\u013e\t\4\2\2\u013d\u013c\3\2\2\2")
        buf.write("\u013e\u013f\3\2\2\2\u013f\u013d\3\2\2\2\u013f\u0140\3")
        buf.write("\2\2\2\u0140^\3\2\2\2\u0141\u0145\5a\61\2\u0142\u0144")
        buf.write("\5e\63\2\u0143\u0142\3\2\2\2\u0144\u0147\3\2\2\2\u0145")
        buf.write("\u0143\3\2\2\2\u0145\u0146\3\2\2\2\u0146\u0148\3\2\2\2")
        buf.write("\u0147\u0145\3\2\2\2\u0148\u0149\5a\61\2\u0149\u014a\b")
        buf.write("\60\3\2\u014a`\3\2\2\2\u014b\u014c\7$\2\2\u014cb\3\2\2")
        buf.write("\2\u014d\u014e\7^\2\2\u014e\u014f\n\7\2\2\u014fd\3\2\2")
        buf.write("\2\u0150\u0155\5g\64\2\u0151\u0152\7)\2\2\u0152\u0155")
        buf.write("\7$\2\2\u0153\u0155\n\b\2\2\u0154\u0150\3\2\2\2\u0154")
        buf.write("\u0151\3\2\2\2\u0154\u0153\3\2\2\2\u0155f\3\2\2\2\u0156")
        buf.write("\u0157\7^\2\2\u0157\u0158\t\7\2\2\u0158h\3\2\2\2\u0159")
        buf.write("\u015b\t\4\2\2\u015a\u0159\3\2\2\2\u015b\u015c\3\2\2\2")
        buf.write("\u015c\u015a\3\2\2\2\u015c\u015d\3\2\2\2\u015dj\3\2\2")
        buf.write("\2\u015e\u0162\t\t\2\2\u015f\u0161\t\n\2\2\u0160\u015f")
        buf.write("\3\2\2\2\u0161\u0164\3\2\2\2\u0162\u0160\3\2\2\2\u0162")
        buf.write("\u0163\3\2\2\2\u0163l\3\2\2\2\u0164\u0162\3\2\2\2\u0165")
        buf.write("\u0167\t\13\2\2\u0166\u0165\3\2\2\2\u0167\u0168\3\2\2")
        buf.write("\2\u0168\u0166\3\2\2\2\u0168\u0169\3\2\2\2\u0169\u016a")
        buf.write("\3\2\2\2\u016a\u016b\b\67\2\2\u016bn\3\2\2\2\u016c\u0170")
        buf.write("\7$\2\2\u016d\u016f\5e\63\2\u016e\u016d\3\2\2\2\u016f")
        buf.write("\u0172\3\2\2\2\u0170\u016e\3\2\2\2\u0170\u0171\3\2\2\2")
        buf.write("\u0171\u0174\3\2\2\2\u0172\u0170\3\2\2\2\u0173\u0175\t")
        buf.write("\f\2\2\u0174\u0173\3\2\2\2\u0175\u0176\3\2\2\2\u0176\u0177")
        buf.write("\b8\4\2\u0177p\3\2\2\2\u0178\u017c\7$\2\2\u0179\u017b")
        buf.write("\5e\63\2\u017a\u0179\3\2\2\2\u017b\u017e\3\2\2\2\u017c")
        buf.write("\u017a\3\2\2\2\u017c\u017d\3\2\2\2\u017d\u017f\3\2\2\2")
        buf.write("\u017e\u017c\3\2\2\2\u017f\u0180\5c\62\2\u0180\u0181\b")
        buf.write("9\5\2\u0181r\3\2\2\2\u0182\u0183\13\2\2\2\u0183\u0184")
        buf.write("\b:\6\2\u0184t\3\2\2\2\24\2{\u0089\u0125\u0128\u012a\u012f")
        buf.write("\u0135\u013a\u013f\u0145\u0154\u015c\u0162\u0168\u0170")
        buf.write("\u0174\u017c\7\b\2\2\3\60\2\38\3\39\4\3:\5")
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
    STRING_LITERAL = 44
    IDENTIFIER = 45
    WS = 46
    UNCLOSE_STRING = 47
    ILLEGAL_ESCAPE = 48
    ERROR_CHAR = 49

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'return'", "'for'", "'if'", "'not'", "'var'", "'until'", "'else'", 
            "'and'", "'number'", "'dynamic'", "'by'", "'elif'", "'or'", 
            "'bool'", "'func'", "'break'", "'begin'", "'string'", "'continue'", 
            "'end'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", "'='", "'<-'", 
            "'!='", "'<='", "'>='", "'<'", "'>'", "'...'", "'('", "')'", 
            "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>",
            "ZCODE_COMMENT", "BOOLEAN_LITERAL", "RETURN", "FOR", "IF", "NOT", 
            "VAR", "UNTIL", "ELSE", "AND", "NUMBER", "DYNAMIC", "BY", "ELIF", 
            "OR", "BOOL", "FUNC", "BREAK", "BEGIN", "STRING", "CONTINUE", 
            "END", "PLUS", "MINUS", "TIMES", "DIVIDED", "MOD", "COMPARE", 
            "EQUAL", "ASSIGN", "NOT_EQUAL", "LTOE", "GTOE", "LT", "GT", 
            "CONCATENATION", "LEFTPAREN", "RIGHTPAREN", "LEFTBRACKET", "RIGHTBRACKET", 
            "COMMA", "NL", "NUMBER_LITERAL", "STRING_LITERAL", "IDENTIFIER", 
            "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "ZCODE_COMMENT", "BOOLEAN_LITERAL", "RETURN", "FOR", "IF", 
                  "NOT", "VAR", "UNTIL", "ELSE", "AND", "NUMBER", "DYNAMIC", 
                  "BY", "ELIF", "OR", "BOOL", "FUNC", "BREAK", "BEGIN", 
                  "STRING", "CONTINUE", "END", "PLUS", "MINUS", "TIMES", 
                  "DIVIDED", "MOD", "COMPARE", "EQUAL", "ASSIGN", "NOT_EQUAL", 
                  "LTOE", "GTOE", "LT", "GT", "CONCATENATION", "LEFTPAREN", 
                  "RIGHTPAREN", "LEFTBRACKET", "RIGHTBRACKET", "COMMA", 
                  "NL", "NUMBER_LITERAL", "INTEGERPART", "DECIMALPART", 
                  "EXPONENTPART", "STRING_LITERAL", "DOUBLEQUOTE", "INVALID_ESC", 
                  "CHAR", "ESC", "SIZE", "IDENTIFIER", "WS", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

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
            actions[46] = self.STRING_LITERAL_action 
            actions[54] = self.UNCLOSE_STRING_action 
            actions[55] = self.ILLEGAL_ESCAPE_action 
            actions[56] = self.ERROR_CHAR_action 
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
     


