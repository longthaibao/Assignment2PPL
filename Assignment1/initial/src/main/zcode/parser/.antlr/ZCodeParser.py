# Generated from /Users/macbookpro/Documents/Assignment_PPL/Assignment1/initial/src/main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,50,444,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,1,0,1,0,1,0,1,1,1,1,
        1,1,1,1,3,1,110,8,1,1,2,1,2,1,2,3,2,115,8,2,1,3,1,3,1,4,1,4,1,5,
        1,5,3,5,123,8,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,
        1,7,1,7,1,7,3,7,140,8,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,3,9,
        151,8,9,1,10,1,10,1,10,3,10,156,8,10,1,10,1,10,1,11,1,11,1,11,1,
        11,3,11,164,8,11,1,11,1,11,1,12,1,12,1,12,1,12,3,12,172,8,12,1,13,
        1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,3,14,183,8,14,1,15,1,15,
        1,15,3,15,188,8,15,1,15,1,15,1,15,1,15,3,15,194,8,15,1,16,1,16,1,
        17,1,17,1,17,1,17,1,17,1,17,3,17,204,8,17,1,17,1,17,1,18,1,18,1,
        18,1,18,1,19,1,19,3,19,214,8,19,1,20,1,20,1,20,1,20,1,20,3,20,221,
        8,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,3,21,230,8,21,1,22,1,22,
        3,22,234,8,22,1,23,1,23,3,23,238,8,23,1,24,1,24,1,24,1,24,3,24,244,
        8,24,1,24,1,24,1,24,1,24,1,24,1,24,3,24,252,8,24,3,24,254,8,24,1,
        25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,3,25,264,8,25,1,26,1,26,1,
        26,1,26,3,26,270,8,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,
        26,1,27,1,27,3,27,283,8,27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,
        28,1,28,1,28,1,28,1,28,1,28,1,28,3,28,299,8,28,1,29,1,29,1,29,1,
        30,1,30,1,30,1,31,1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,32,1,32,1,
        33,1,33,1,33,1,33,1,33,1,33,1,34,1,34,3,34,325,8,34,1,35,1,35,1,
        35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,3,35,338,8,35,1,36,1,
        36,3,36,342,8,36,1,37,1,37,1,37,1,37,1,37,3,37,349,8,37,1,38,1,38,
        1,38,1,38,1,38,3,38,356,8,38,1,39,1,39,1,39,1,39,1,39,3,39,363,8,
        39,1,40,1,40,1,40,1,40,1,40,1,40,5,40,371,8,40,10,40,12,40,374,9,
        40,1,41,1,41,1,41,1,41,1,41,1,41,5,41,382,8,41,10,41,12,41,385,9,
        41,1,42,1,42,1,42,1,42,1,42,1,42,5,42,393,8,42,10,42,12,42,396,9,
        42,1,43,1,43,1,43,3,43,401,8,43,1,44,1,44,1,44,3,44,406,8,44,1,45,
        1,45,1,45,1,45,1,45,1,45,3,45,414,8,45,1,46,1,46,1,46,1,46,1,46,
        1,46,3,46,422,8,46,1,47,1,47,1,47,1,47,1,47,3,47,429,8,47,1,48,1,
        48,1,48,1,48,1,49,1,49,3,49,437,8,49,1,50,1,50,1,50,3,50,442,8,50,
        1,50,0,3,80,82,84,51,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,
        32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,
        76,78,80,82,84,86,88,90,92,94,96,98,100,0,6,3,0,10,10,15,15,19,19,
        2,0,6,6,11,11,2,0,28,29,31,35,2,0,9,9,14,14,1,0,23,24,1,0,25,27,
        444,0,102,1,0,0,0,2,109,1,0,0,0,4,114,1,0,0,0,6,116,1,0,0,0,8,118,
        1,0,0,0,10,122,1,0,0,0,12,129,1,0,0,0,14,139,1,0,0,0,16,141,1,0,
        0,0,18,150,1,0,0,0,20,152,1,0,0,0,22,163,1,0,0,0,24,167,1,0,0,0,
        26,173,1,0,0,0,28,178,1,0,0,0,30,193,1,0,0,0,32,195,1,0,0,0,34,197,
        1,0,0,0,36,207,1,0,0,0,38,213,1,0,0,0,40,220,1,0,0,0,42,222,1,0,
        0,0,44,233,1,0,0,0,46,237,1,0,0,0,48,253,1,0,0,0,50,263,1,0,0,0,
        52,265,1,0,0,0,54,282,1,0,0,0,56,288,1,0,0,0,58,300,1,0,0,0,60,303,
        1,0,0,0,62,306,1,0,0,0,64,310,1,0,0,0,66,316,1,0,0,0,68,324,1,0,
        0,0,70,337,1,0,0,0,72,341,1,0,0,0,74,348,1,0,0,0,76,355,1,0,0,0,
        78,362,1,0,0,0,80,364,1,0,0,0,82,375,1,0,0,0,84,386,1,0,0,0,86,400,
        1,0,0,0,88,405,1,0,0,0,90,413,1,0,0,0,92,421,1,0,0,0,94,428,1,0,
        0,0,96,430,1,0,0,0,98,436,1,0,0,0,100,441,1,0,0,0,102,103,3,2,1,
        0,103,104,5,0,0,1,104,1,1,0,0,0,105,106,3,4,2,0,106,107,3,2,1,0,
        107,110,1,0,0,0,108,110,3,4,2,0,109,105,1,0,0,0,109,108,1,0,0,0,
        110,3,1,0,0,0,111,115,3,22,11,0,112,115,3,34,17,0,113,115,5,42,0,
        0,114,111,1,0,0,0,114,112,1,0,0,0,114,113,1,0,0,0,115,5,1,0,0,0,
        116,117,7,0,0,0,117,7,1,0,0,0,118,119,7,1,0,0,119,9,1,0,0,0,120,
        123,3,6,3,0,121,123,5,11,0,0,122,120,1,0,0,0,122,121,1,0,0,0,123,
        124,1,0,0,0,124,125,5,46,0,0,125,126,5,39,0,0,126,127,3,14,7,0,127,
        128,5,40,0,0,128,11,1,0,0,0,129,130,5,6,0,0,130,131,5,46,0,0,131,
        132,5,39,0,0,132,133,3,14,7,0,133,134,5,40,0,0,134,13,1,0,0,0,135,
        136,5,43,0,0,136,137,5,41,0,0,137,140,3,14,7,0,138,140,5,43,0,0,
        139,135,1,0,0,0,139,138,1,0,0,0,140,15,1,0,0,0,141,142,5,39,0,0,
        142,143,3,74,37,0,143,144,5,40,0,0,144,17,1,0,0,0,145,146,3,16,8,
        0,146,147,5,41,0,0,147,148,3,18,9,0,148,151,1,0,0,0,149,151,3,16,
        8,0,150,145,1,0,0,0,150,149,1,0,0,0,151,19,1,0,0,0,152,155,5,39,
        0,0,153,156,3,18,9,0,154,156,3,74,37,0,155,153,1,0,0,0,155,154,1,
        0,0,0,156,157,1,0,0,0,157,158,5,40,0,0,158,21,1,0,0,0,159,164,3,
        24,12,0,160,164,3,26,13,0,161,164,3,28,14,0,162,164,3,30,15,0,163,
        159,1,0,0,0,163,160,1,0,0,0,163,161,1,0,0,0,163,162,1,0,0,0,164,
        165,1,0,0,0,165,166,3,98,49,0,166,23,1,0,0,0,167,168,3,6,3,0,168,
        171,5,46,0,0,169,170,5,30,0,0,170,172,3,32,16,0,171,169,1,0,0,0,
        171,172,1,0,0,0,172,25,1,0,0,0,173,174,5,6,0,0,174,175,5,46,0,0,
        175,176,5,30,0,0,176,177,3,32,16,0,177,27,1,0,0,0,178,179,5,11,0,
        0,179,182,5,46,0,0,180,181,5,30,0,0,181,183,3,32,16,0,182,180,1,
        0,0,0,182,183,1,0,0,0,183,29,1,0,0,0,184,187,3,10,5,0,185,186,5,
        30,0,0,186,188,3,20,10,0,187,185,1,0,0,0,187,188,1,0,0,0,188,194,
        1,0,0,0,189,190,3,12,6,0,190,191,5,30,0,0,191,192,3,20,10,0,192,
        194,1,0,0,0,193,184,1,0,0,0,193,189,1,0,0,0,194,31,1,0,0,0,195,196,
        3,72,36,0,196,33,1,0,0,0,197,198,5,16,0,0,198,199,5,46,0,0,199,200,
        3,36,18,0,200,203,3,98,49,0,201,204,3,44,22,0,202,204,1,0,0,0,203,
        201,1,0,0,0,203,202,1,0,0,0,204,205,1,0,0,0,205,206,3,98,49,0,206,
        35,1,0,0,0,207,208,5,37,0,0,208,209,3,38,19,0,209,210,5,38,0,0,210,
        37,1,0,0,0,211,214,3,40,20,0,212,214,1,0,0,0,213,211,1,0,0,0,213,
        212,1,0,0,0,214,39,1,0,0,0,215,216,3,42,21,0,216,217,5,41,0,0,217,
        218,3,40,20,0,218,221,1,0,0,0,219,221,3,42,21,0,220,215,1,0,0,0,
        220,219,1,0,0,0,221,41,1,0,0,0,222,229,3,6,3,0,223,230,5,46,0,0,
        224,225,5,46,0,0,225,226,5,39,0,0,226,227,3,74,37,0,227,228,5,40,
        0,0,228,230,1,0,0,0,229,223,1,0,0,0,229,224,1,0,0,0,230,43,1,0,0,
        0,231,234,3,62,31,0,232,234,3,66,33,0,233,231,1,0,0,0,233,232,1,
        0,0,0,234,45,1,0,0,0,235,238,3,48,24,0,236,238,1,0,0,0,237,235,1,
        0,0,0,237,236,1,0,0,0,238,47,1,0,0,0,239,244,3,50,25,0,240,241,3,
        22,11,0,241,242,3,100,50,0,242,244,1,0,0,0,243,239,1,0,0,0,243,240,
        1,0,0,0,244,245,1,0,0,0,245,246,3,48,24,0,246,254,1,0,0,0,247,252,
        3,50,25,0,248,249,3,22,11,0,249,250,3,100,50,0,250,252,1,0,0,0,251,
        247,1,0,0,0,251,248,1,0,0,0,252,254,1,0,0,0,253,243,1,0,0,0,253,
        251,1,0,0,0,254,49,1,0,0,0,255,264,3,54,27,0,256,264,3,52,26,0,257,
        264,3,56,28,0,258,264,3,58,29,0,259,264,3,60,30,0,260,264,3,62,31,
        0,261,264,3,64,32,0,262,264,3,66,33,0,263,255,1,0,0,0,263,256,1,
        0,0,0,263,257,1,0,0,0,263,258,1,0,0,0,263,259,1,0,0,0,263,260,1,
        0,0,0,263,261,1,0,0,0,263,262,1,0,0,0,264,51,1,0,0,0,265,266,5,3,
        0,0,266,267,5,46,0,0,267,269,3,72,36,0,268,270,5,30,0,0,269,268,
        1,0,0,0,269,270,1,0,0,0,270,271,1,0,0,0,271,272,3,72,36,0,272,273,
        1,0,0,0,273,274,5,7,0,0,274,275,3,74,37,0,275,276,5,12,0,0,276,277,
        3,74,37,0,277,278,3,98,49,0,278,279,3,48,24,0,279,53,1,0,0,0,280,
        283,5,46,0,0,281,283,3,90,45,0,282,280,1,0,0,0,282,281,1,0,0,0,283,
        284,1,0,0,0,284,285,5,30,0,0,285,286,3,74,37,0,286,287,3,100,50,
        0,287,55,1,0,0,0,288,289,5,4,0,0,289,290,3,76,38,0,290,291,3,98,
        49,0,291,292,3,50,25,0,292,293,1,0,0,0,293,298,3,68,34,0,294,295,
        5,8,0,0,295,296,3,98,49,0,296,297,3,50,25,0,297,299,1,0,0,0,298,
        294,1,0,0,0,298,299,1,0,0,0,299,57,1,0,0,0,300,301,5,17,0,0,301,
        302,3,100,50,0,302,59,1,0,0,0,303,304,5,20,0,0,304,305,3,100,50,
        0,305,61,1,0,0,0,306,307,5,2,0,0,307,308,3,72,36,0,308,309,3,100,
        50,0,309,63,1,0,0,0,310,311,5,46,0,0,311,312,5,37,0,0,312,313,3,
        72,36,0,313,314,5,38,0,0,314,315,3,100,50,0,315,65,1,0,0,0,316,317,
        5,18,0,0,317,318,3,100,50,0,318,319,3,46,23,0,319,320,5,21,0,0,320,
        321,3,100,50,0,321,67,1,0,0,0,322,325,3,70,35,0,323,325,1,0,0,0,
        324,322,1,0,0,0,324,323,1,0,0,0,325,69,1,0,0,0,326,327,5,13,0,0,
        327,328,3,76,38,0,328,329,3,98,49,0,329,330,3,50,25,0,330,331,3,
        70,35,0,331,338,1,0,0,0,332,333,5,13,0,0,333,334,3,76,38,0,334,335,
        3,98,49,0,335,336,3,50,25,0,336,338,1,0,0,0,337,326,1,0,0,0,337,
        332,1,0,0,0,338,71,1,0,0,0,339,342,3,74,37,0,340,342,1,0,0,0,341,
        339,1,0,0,0,341,340,1,0,0,0,342,73,1,0,0,0,343,344,3,76,38,0,344,
        345,5,41,0,0,345,346,3,74,37,0,346,349,1,0,0,0,347,349,3,76,38,0,
        348,343,1,0,0,0,348,347,1,0,0,0,349,75,1,0,0,0,350,351,3,78,39,0,
        351,352,5,36,0,0,352,353,3,78,39,0,353,356,1,0,0,0,354,356,3,78,
        39,0,355,350,1,0,0,0,355,354,1,0,0,0,356,77,1,0,0,0,357,358,3,80,
        40,0,358,359,7,2,0,0,359,360,3,80,40,0,360,363,1,0,0,0,361,363,3,
        80,40,0,362,357,1,0,0,0,362,361,1,0,0,0,363,79,1,0,0,0,364,365,6,
        40,-1,0,365,366,3,82,41,0,366,372,1,0,0,0,367,368,10,2,0,0,368,369,
        7,3,0,0,369,371,3,82,41,0,370,367,1,0,0,0,371,374,1,0,0,0,372,370,
        1,0,0,0,372,373,1,0,0,0,373,81,1,0,0,0,374,372,1,0,0,0,375,376,6,
        41,-1,0,376,377,3,84,42,0,377,383,1,0,0,0,378,379,10,2,0,0,379,380,
        7,4,0,0,380,382,3,84,42,0,381,378,1,0,0,0,382,385,1,0,0,0,383,381,
        1,0,0,0,383,384,1,0,0,0,384,83,1,0,0,0,385,383,1,0,0,0,386,387,6,
        42,-1,0,387,388,3,86,43,0,388,394,1,0,0,0,389,390,10,2,0,0,390,391,
        7,5,0,0,391,393,3,86,43,0,392,389,1,0,0,0,393,396,1,0,0,0,394,392,
        1,0,0,0,394,395,1,0,0,0,395,85,1,0,0,0,396,394,1,0,0,0,397,398,5,
        5,0,0,398,401,3,86,43,0,399,401,3,88,44,0,400,397,1,0,0,0,400,399,
        1,0,0,0,401,87,1,0,0,0,402,403,5,24,0,0,403,406,3,88,44,0,404,406,
        3,90,45,0,405,402,1,0,0,0,405,404,1,0,0,0,406,89,1,0,0,0,407,408,
        5,46,0,0,408,409,5,39,0,0,409,410,3,74,37,0,410,411,5,40,0,0,411,
        414,1,0,0,0,412,414,3,92,46,0,413,407,1,0,0,0,413,412,1,0,0,0,414,
        91,1,0,0,0,415,416,5,46,0,0,416,417,5,37,0,0,417,418,3,72,36,0,418,
        419,5,38,0,0,419,422,1,0,0,0,420,422,3,94,47,0,421,415,1,0,0,0,421,
        420,1,0,0,0,422,93,1,0,0,0,423,429,5,43,0,0,424,429,5,45,0,0,425,
        429,5,44,0,0,426,429,5,46,0,0,427,429,3,96,48,0,428,423,1,0,0,0,
        428,424,1,0,0,0,428,425,1,0,0,0,428,426,1,0,0,0,428,427,1,0,0,0,
        429,95,1,0,0,0,430,431,5,37,0,0,431,432,3,76,38,0,432,433,5,38,0,
        0,433,97,1,0,0,0,434,437,3,100,50,0,435,437,1,0,0,0,436,434,1,0,
        0,0,436,435,1,0,0,0,437,99,1,0,0,0,438,439,5,42,0,0,439,442,3,100,
        50,0,440,442,5,42,0,0,441,438,1,0,0,0,441,440,1,0,0,0,442,101,1,
        0,0,0,40,109,114,122,139,150,155,163,171,182,187,193,203,213,220,
        229,233,237,243,251,253,263,269,282,298,324,337,341,348,355,362,
        372,383,394,400,405,413,421,428,436,441
    ]

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
        self.checkVersion("4.13.1")
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




    def decl(self):

        localctx = ZCodeParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 114
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 10, 11, 15, 19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.vardecl()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 112
                self.funcdecl()
                pass
            elif token in [42]:
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




    def primitype(self):

        localctx = ZCodeParser.PrimitypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_primitype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 558080) != 0)):
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




    def implitype(self):

        localctx = ZCodeParser.ImplitypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_implitype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            _la = self._input.LA(1)
            if not(_la==6 or _la==11):
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




    def arraytype(self):

        localctx = ZCodeParser.ArraytypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_arraytype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10, 15, 19]:
                self.state = 120
                self.primitype()
                pass
            elif token in [11]:
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
            if token in [39]:
                self.state = 153
                self.listofArray()
                pass
            elif token in [5, 24, 37, 43, 44, 45, 46]:
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
            if _la==30:
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
            if _la==30:
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




    def vardecl4(self):

        localctx = ZCodeParser.Vardecl4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_vardecl4)
        self._la = 0 # Token type
        try:
            self.state = 193
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10, 11, 15, 19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.arraytype()
                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==30:
                    self.state = 185
                    self.match(ZCodeParser.ASSIGN)
                    self.state = 186
                    self.arrayvalue()


                pass
            elif token in [6]:
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
            if token in [2, 18]:
                self.state = 201
                self.bodyfunc()
                pass
            elif token in [-1, 6, 10, 11, 15, 16, 19, 42]:
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




    def paramlist(self):

        localctx = ZCodeParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_paramlist)
        try:
            self.state = 213
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10, 15, 19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.paramprime()
                pass
            elif token in [38]:
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




    def bodyfunc(self):

        localctx = ZCodeParser.BodyfuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_bodyfunc)
        try:
            self.state = 233
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.returnstmt()
                pass
            elif token in [18]:
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




    def stmtlist(self):

        localctx = ZCodeParser.StmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_stmtlist)
        try:
            self.state = 237
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3, 4, 6, 10, 11, 15, 17, 18, 19, 20, 37, 43, 44, 45, 46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.stmtprime()
                pass
            elif token in [21]:
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
                if token in [2, 3, 4, 17, 18, 20, 37, 43, 44, 45, 46]:
                    self.state = 239
                    self.stmt()
                    pass
                elif token in [6, 10, 11, 15, 19]:
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
                if token in [2, 3, 4, 17, 18, 20, 37, 43, 44, 45, 46]:
                    self.state = 247
                    self.stmt()
                    pass
                elif token in [6, 10, 11, 15, 19]:
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
            if _la==30:
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
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 67377299456) != 0)):
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
                    if not(_la==9 or _la==14):
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
                    if not(_la==23 or _la==24):
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
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 234881024) != 0)):
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




    def expr5(self):

        localctx = ZCodeParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_expr5)
        try:
            self.state = 400
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 397
                self.match(ZCodeParser.NOT)
                self.state = 398
                self.expr5()
                pass
            elif token in [24, 37, 43, 44, 45, 46]:
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




    def expr6(self):

        localctx = ZCodeParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_expr6)
        try:
            self.state = 405
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 402
                self.match(ZCodeParser.MINUS)
                self.state = 403
                self.expr6()
                pass
            elif token in [37, 43, 44, 45, 46]:
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




    def expr9(self):

        localctx = ZCodeParser.Expr9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_expr9)
        try:
            self.state = 428
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [43]:
                self.enterOuterAlt(localctx, 1)
                self.state = 423
                self.match(ZCodeParser.NUMBER_LITERAL)
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 2)
                self.state = 424
                self.match(ZCodeParser.STRING_LITERAL)
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 3)
                self.state = 425
                self.match(ZCodeParser.BOOLEAN_LITERAL)
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 4)
                self.state = 426
                self.match(ZCodeParser.IDENTIFIER)
                pass
            elif token in [37]:
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
         




