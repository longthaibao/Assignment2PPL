# Generated from /Users/macbookpro/Documents/Assignment_PPL/Assignment1/initial/src/main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
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
    return [
        4,0,49,392,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,1,0,1,0,1,0,1,0,
        5,0,120,8,0,10,0,12,0,123,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,3,1,136,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,
        3,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,
        7,1,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,
        10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,
        12,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,
        15,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,18,1,
        18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,20,1,
        20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,22,1,
        22,1,23,1,23,1,24,1,24,1,25,1,25,1,26,1,26,1,27,1,27,1,27,1,28,1,
        28,1,29,1,29,1,29,1,30,1,30,1,30,1,31,1,31,1,31,1,32,1,32,1,32,1,
        33,1,33,1,34,1,34,1,35,1,35,1,35,1,35,1,36,1,36,1,37,1,37,1,38,1,
        38,1,39,1,39,1,40,1,40,1,41,1,41,1,41,1,41,1,41,3,41,293,8,41,1,
        42,1,42,3,42,297,8,42,1,42,3,42,300,8,42,3,42,302,8,42,1,43,4,43,
        305,8,43,11,43,12,43,306,1,44,1,44,5,44,311,8,44,10,44,12,44,314,
        9,44,1,45,1,45,3,45,318,8,45,1,45,4,45,321,8,45,11,45,12,45,322,
        1,46,1,46,5,46,327,8,46,10,46,12,46,330,9,46,1,46,1,46,1,46,1,47,
        1,47,1,48,1,48,1,48,1,49,1,49,1,49,1,49,3,49,344,8,49,1,50,1,50,
        1,50,1,51,4,51,350,8,51,11,51,12,51,351,1,52,1,52,5,52,356,8,52,
        10,52,12,52,359,9,52,1,53,4,53,362,8,53,11,53,12,53,363,1,53,1,53,
        1,54,1,54,5,54,370,8,54,10,54,12,54,373,9,54,1,54,3,54,376,8,54,
        1,54,1,54,1,55,1,55,5,55,382,8,55,10,55,12,55,385,9,55,1,55,1,55,
        1,55,1,56,1,56,1,56,0,0,57,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,
        9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,33,17,35,18,37,19,39,
        20,41,21,43,22,45,23,47,24,49,25,51,26,53,27,55,28,57,29,59,30,61,
        31,63,32,65,33,67,34,69,35,71,36,73,37,75,38,77,39,79,40,81,41,83,
        42,85,43,87,0,89,0,91,0,93,44,95,0,97,0,99,0,101,0,103,0,105,45,
        107,46,109,47,111,48,113,49,1,0,10,1,0,10,10,1,0,48,57,2,0,69,69,
        101,101,2,0,43,43,45,45,7,0,39,39,92,92,98,98,102,102,110,110,114,
        114,116,116,4,0,10,10,13,13,34,34,92,92,3,0,65,90,95,95,97,122,4,
        0,48,57,65,90,95,95,97,122,3,0,8,9,12,12,32,32,2,1,10,10,13,13,401,
        0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,
        1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,
        1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,
        1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,
        1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,
        1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,
        1,0,0,0,0,63,1,0,0,0,0,65,1,0,0,0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,
        1,0,0,0,0,73,1,0,0,0,0,75,1,0,0,0,0,77,1,0,0,0,0,79,1,0,0,0,0,81,
        1,0,0,0,0,83,1,0,0,0,0,85,1,0,0,0,0,93,1,0,0,0,0,105,1,0,0,0,0,107,
        1,0,0,0,0,109,1,0,0,0,0,111,1,0,0,0,0,113,1,0,0,0,1,115,1,0,0,0,
        3,135,1,0,0,0,5,137,1,0,0,0,7,144,1,0,0,0,9,148,1,0,0,0,11,151,1,
        0,0,0,13,155,1,0,0,0,15,159,1,0,0,0,17,165,1,0,0,0,19,170,1,0,0,
        0,21,174,1,0,0,0,23,181,1,0,0,0,25,189,1,0,0,0,27,192,1,0,0,0,29,
        197,1,0,0,0,31,200,1,0,0,0,33,205,1,0,0,0,35,210,1,0,0,0,37,216,
        1,0,0,0,39,222,1,0,0,0,41,229,1,0,0,0,43,238,1,0,0,0,45,242,1,0,
        0,0,47,244,1,0,0,0,49,246,1,0,0,0,51,248,1,0,0,0,53,250,1,0,0,0,
        55,252,1,0,0,0,57,255,1,0,0,0,59,257,1,0,0,0,61,260,1,0,0,0,63,263,
        1,0,0,0,65,266,1,0,0,0,67,269,1,0,0,0,69,271,1,0,0,0,71,273,1,0,
        0,0,73,277,1,0,0,0,75,279,1,0,0,0,77,281,1,0,0,0,79,283,1,0,0,0,
        81,285,1,0,0,0,83,292,1,0,0,0,85,294,1,0,0,0,87,304,1,0,0,0,89,308,
        1,0,0,0,91,315,1,0,0,0,93,324,1,0,0,0,95,334,1,0,0,0,97,336,1,0,
        0,0,99,343,1,0,0,0,101,345,1,0,0,0,103,349,1,0,0,0,105,353,1,0,0,
        0,107,361,1,0,0,0,109,367,1,0,0,0,111,379,1,0,0,0,113,389,1,0,0,
        0,115,116,5,35,0,0,116,117,5,35,0,0,117,121,1,0,0,0,118,120,8,0,
        0,0,119,118,1,0,0,0,120,123,1,0,0,0,121,119,1,0,0,0,121,122,1,0,
        0,0,122,124,1,0,0,0,123,121,1,0,0,0,124,125,6,0,0,0,125,2,1,0,0,
        0,126,127,5,116,0,0,127,128,5,114,0,0,128,129,5,117,0,0,129,136,
        5,101,0,0,130,131,5,102,0,0,131,132,5,97,0,0,132,133,5,108,0,0,133,
        134,5,115,0,0,134,136,5,101,0,0,135,126,1,0,0,0,135,130,1,0,0,0,
        136,4,1,0,0,0,137,138,5,114,0,0,138,139,5,101,0,0,139,140,5,116,
        0,0,140,141,5,117,0,0,141,142,5,114,0,0,142,143,5,110,0,0,143,6,
        1,0,0,0,144,145,5,102,0,0,145,146,5,111,0,0,146,147,5,114,0,0,147,
        8,1,0,0,0,148,149,5,105,0,0,149,150,5,102,0,0,150,10,1,0,0,0,151,
        152,5,110,0,0,152,153,5,111,0,0,153,154,5,116,0,0,154,12,1,0,0,0,
        155,156,5,118,0,0,156,157,5,97,0,0,157,158,5,114,0,0,158,14,1,0,
        0,0,159,160,5,117,0,0,160,161,5,110,0,0,161,162,5,116,0,0,162,163,
        5,105,0,0,163,164,5,108,0,0,164,16,1,0,0,0,165,166,5,101,0,0,166,
        167,5,108,0,0,167,168,5,115,0,0,168,169,5,101,0,0,169,18,1,0,0,0,
        170,171,5,97,0,0,171,172,5,110,0,0,172,173,5,100,0,0,173,20,1,0,
        0,0,174,175,5,110,0,0,175,176,5,117,0,0,176,177,5,109,0,0,177,178,
        5,98,0,0,178,179,5,101,0,0,179,180,5,114,0,0,180,22,1,0,0,0,181,
        182,5,100,0,0,182,183,5,121,0,0,183,184,5,110,0,0,184,185,5,97,0,
        0,185,186,5,109,0,0,186,187,5,105,0,0,187,188,5,99,0,0,188,24,1,
        0,0,0,189,190,5,98,0,0,190,191,5,121,0,0,191,26,1,0,0,0,192,193,
        5,101,0,0,193,194,5,108,0,0,194,195,5,105,0,0,195,196,5,102,0,0,
        196,28,1,0,0,0,197,198,5,111,0,0,198,199,5,114,0,0,199,30,1,0,0,
        0,200,201,5,98,0,0,201,202,5,111,0,0,202,203,5,111,0,0,203,204,5,
        108,0,0,204,32,1,0,0,0,205,206,5,102,0,0,206,207,5,117,0,0,207,208,
        5,110,0,0,208,209,5,99,0,0,209,34,1,0,0,0,210,211,5,98,0,0,211,212,
        5,114,0,0,212,213,5,101,0,0,213,214,5,97,0,0,214,215,5,107,0,0,215,
        36,1,0,0,0,216,217,5,98,0,0,217,218,5,101,0,0,218,219,5,103,0,0,
        219,220,5,105,0,0,220,221,5,110,0,0,221,38,1,0,0,0,222,223,5,115,
        0,0,223,224,5,116,0,0,224,225,5,114,0,0,225,226,5,105,0,0,226,227,
        5,110,0,0,227,228,5,103,0,0,228,40,1,0,0,0,229,230,5,99,0,0,230,
        231,5,111,0,0,231,232,5,110,0,0,232,233,5,116,0,0,233,234,5,105,
        0,0,234,235,5,110,0,0,235,236,5,117,0,0,236,237,5,101,0,0,237,42,
        1,0,0,0,238,239,5,101,0,0,239,240,5,110,0,0,240,241,5,100,0,0,241,
        44,1,0,0,0,242,243,5,43,0,0,243,46,1,0,0,0,244,245,5,45,0,0,245,
        48,1,0,0,0,246,247,5,42,0,0,247,50,1,0,0,0,248,249,5,47,0,0,249,
        52,1,0,0,0,250,251,5,37,0,0,251,54,1,0,0,0,252,253,5,61,0,0,253,
        254,5,61,0,0,254,56,1,0,0,0,255,256,5,61,0,0,256,58,1,0,0,0,257,
        258,5,60,0,0,258,259,5,45,0,0,259,60,1,0,0,0,260,261,5,33,0,0,261,
        262,5,61,0,0,262,62,1,0,0,0,263,264,5,60,0,0,264,265,5,61,0,0,265,
        64,1,0,0,0,266,267,5,62,0,0,267,268,5,61,0,0,268,66,1,0,0,0,269,
        270,5,60,0,0,270,68,1,0,0,0,271,272,5,62,0,0,272,70,1,0,0,0,273,
        274,5,46,0,0,274,275,5,46,0,0,275,276,5,46,0,0,276,72,1,0,0,0,277,
        278,5,40,0,0,278,74,1,0,0,0,279,280,5,41,0,0,280,76,1,0,0,0,281,
        282,5,91,0,0,282,78,1,0,0,0,283,284,5,93,0,0,284,80,1,0,0,0,285,
        286,5,44,0,0,286,82,1,0,0,0,287,293,5,10,0,0,288,289,5,13,0,0,289,
        290,5,10,0,0,290,291,1,0,0,0,291,293,6,41,1,0,292,287,1,0,0,0,292,
        288,1,0,0,0,293,84,1,0,0,0,294,301,3,87,43,0,295,297,3,89,44,0,296,
        295,1,0,0,0,296,297,1,0,0,0,297,299,1,0,0,0,298,300,3,91,45,0,299,
        298,1,0,0,0,299,300,1,0,0,0,300,302,1,0,0,0,301,296,1,0,0,0,301,
        302,1,0,0,0,302,86,1,0,0,0,303,305,7,1,0,0,304,303,1,0,0,0,305,306,
        1,0,0,0,306,304,1,0,0,0,306,307,1,0,0,0,307,88,1,0,0,0,308,312,5,
        46,0,0,309,311,7,1,0,0,310,309,1,0,0,0,311,314,1,0,0,0,312,310,1,
        0,0,0,312,313,1,0,0,0,313,90,1,0,0,0,314,312,1,0,0,0,315,317,7,2,
        0,0,316,318,7,3,0,0,317,316,1,0,0,0,317,318,1,0,0,0,318,320,1,0,
        0,0,319,321,7,1,0,0,320,319,1,0,0,0,321,322,1,0,0,0,322,320,1,0,
        0,0,322,323,1,0,0,0,323,92,1,0,0,0,324,328,3,95,47,0,325,327,3,99,
        49,0,326,325,1,0,0,0,327,330,1,0,0,0,328,326,1,0,0,0,328,329,1,0,
        0,0,329,331,1,0,0,0,330,328,1,0,0,0,331,332,3,95,47,0,332,333,6,
        46,2,0,333,94,1,0,0,0,334,335,5,34,0,0,335,96,1,0,0,0,336,337,5,
        92,0,0,337,338,8,4,0,0,338,98,1,0,0,0,339,344,3,101,50,0,340,341,
        5,39,0,0,341,344,5,34,0,0,342,344,8,5,0,0,343,339,1,0,0,0,343,340,
        1,0,0,0,343,342,1,0,0,0,344,100,1,0,0,0,345,346,5,92,0,0,346,347,
        7,4,0,0,347,102,1,0,0,0,348,350,7,1,0,0,349,348,1,0,0,0,350,351,
        1,0,0,0,351,349,1,0,0,0,351,352,1,0,0,0,352,104,1,0,0,0,353,357,
        7,6,0,0,354,356,7,7,0,0,355,354,1,0,0,0,356,359,1,0,0,0,357,355,
        1,0,0,0,357,358,1,0,0,0,358,106,1,0,0,0,359,357,1,0,0,0,360,362,
        7,8,0,0,361,360,1,0,0,0,362,363,1,0,0,0,363,361,1,0,0,0,363,364,
        1,0,0,0,364,365,1,0,0,0,365,366,6,53,0,0,366,108,1,0,0,0,367,371,
        5,34,0,0,368,370,3,99,49,0,369,368,1,0,0,0,370,373,1,0,0,0,371,369,
        1,0,0,0,371,372,1,0,0,0,372,375,1,0,0,0,373,371,1,0,0,0,374,376,
        7,9,0,0,375,374,1,0,0,0,376,377,1,0,0,0,377,378,6,54,3,0,378,110,
        1,0,0,0,379,383,5,34,0,0,380,382,3,99,49,0,381,380,1,0,0,0,382,385,
        1,0,0,0,383,381,1,0,0,0,383,384,1,0,0,0,384,386,1,0,0,0,385,383,
        1,0,0,0,386,387,3,97,48,0,387,388,6,55,4,0,388,112,1,0,0,0,389,390,
        9,0,0,0,390,391,6,56,5,0,391,114,1,0,0,0,19,0,121,135,292,296,299,
        301,306,312,317,322,328,343,351,357,363,371,375,383,6,6,0,0,1,41,
        0,1,46,1,1,54,2,1,55,3,1,56,4
    ]

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
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[41] = self.NL_action 
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


    def NL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = '\n'
     

    def STRING_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text =self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	if self.text[-1] in ['\n','\r','EOF']:
            		raise UncloseString(self.text[1:-1])
            	else:
            		raise UncloseString(self.text[1:])
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            	illegal_str_from_beginning = str(self.text)
            	raise IllegalEscape(illegal_str_from_beginning[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise ErrorToken(self.text)
     


