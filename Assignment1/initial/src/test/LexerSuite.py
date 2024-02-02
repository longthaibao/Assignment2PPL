import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase): 
    def test_case_100(self):
        input = """	= return
bool	until	* *
end by	number number	bool
continue
- not	+	else	continue var bool	false
break	<=
string break
continue
string < var	]	continue
func *	*	else ] not	func -
if	string 
 [ until
]	else	return
    """
        expect = "=,return,\n,bool,until,*,*,\n,end,by,number,number,bool,\n,continue,\n,-,not,+,else,continue,var,bool,false,\n,break,<=,\n,string,break,\n,continue,\n,string,<,var,],continue,\n,func,*,*,else,],not,func,-,\n,if,string,\n,[,until,\n,],else,return,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,100))
        
    def test_case_101(self):
        input = """ )	< elif end
"abcd"	until	var
false	and <-	<=	return >= 
 != = ,	by	== true /	begin func
if elif %	)	elif >=
= != 109.64E-64	,
func for + > !=	[ dynamic number (
+ true	<= == continue	<= 105.85e8100	by >
break if
    """
        expect = "),<,elif,end,\n,abcd,until,var,\n,false,and,<-,<=,return,>=,\n,!=,=,,,by,==,true,/,begin,func,\n,if,elif,%,),elif,>=,\n,=,!=,109.64E-64,,,\n,func,for,+,>,!=,[,dynamic,number,(,\n,+,true,<=,==,continue,<=,105.85e8100,by,>,\n,break,if,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,101))
        
    def test_case_102(self):
        input = """
<= string * a1
elif
!=
true string	[	<- number	end *	< for a1	true , / var 
 (	return var ==
or	not
69.48e6400	var string	var	by	* ... ) = [	if >	begin number	a1 begin
= by
    """
        expect = "\n,<=,string,*,a1,\n,elif,\n,!=,\n,true,string,[,<-,number,end,*,<,for,a1,true,,,/,var,\n,(,return,var,==,\n,or,not,\n,69.48e6400,var,string,var,by,*,...,),=,[,if,>,begin,number,a1,begin,\n,=,by,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,102))
        
    def test_case_103(self):
        input = """	break	if <=
, end	not "abcd"	"abcd" ,	for end elif begin false
    """
        expect = "break,if,<=,\n,,,end,not,abcd,abcd,,,for,end,elif,begin,false,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,103))
        
    def test_case_104(self):
        input = """ break + <= >=	] %	by	(	var [
    """
        expect = "break,+,<=,>=,],%,by,(,var,[,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,104))
        
    def test_case_105(self):
        input = """
break	end dynamic
,	< true	,	"abcd" true
"abcd"	... or	>= < begin "abcd" ... continue != var >	*	"abcd" dynamic
...	and	dynamic	else	end	"abcd" > by if
...	>= bool = number	
 ( 122e8464
for /	( number /
= else
!= !=
func
% + func *	... var
< begin
for or until <= elif if	and else	"abcd"
func continue
    """
        expect = "\n,break,end,dynamic,\n,,,<,true,,,abcd,true,\n,abcd,...,or,>=,<,begin,abcd,...,continue,!=,var,>,*,abcd,dynamic,\n,...,and,dynamic,else,end,abcd,>,by,if,\n,...,>=,bool,=,number,\n,(,122e8464,\n,for,/,(,number,/,\n,=,else,\n,!=,!=,\n,func,\n,%,+,func,*,...,var,\n,<,begin,\n,for,or,until,<=,elif,if,and,else,abcd,\n,func,continue,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,105))
        
    def test_case_106(self):
        input = """
until end true	and	(
"abcd"	continue	+
not	bool
    """
        expect = "\n,until,end,true,and,(,\n,abcd,continue,+,\n,not,bool,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,106))
        
    def test_case_107(self):
        input = """ number ]	string	break	<	>=
%	for > ...	true a1 by	by bool <= %	- < return	!= end	and	>= *
<
by return	and or	or	bool begin
a1 <- break var -	number
begin	*	for	!= !=	and	==	false	else - var > true
true	for number
86.26	,
-	true else
by	number

 until bool or else	<- ,	continue
dynamic	or
false )	dynamic string
/	[ <= "abcd"	string	>=	%
]	continue "abcd"	return
    """
        expect = "number,],string,break,<,>=,\n,%,for,>,...,true,a1,by,by,bool,<=,%,-,<,return,!=,end,and,>=,*,\n,<,\n,by,return,and,or,or,bool,begin,\n,a1,<-,break,var,-,number,\n,begin,*,for,!=,!=,and,==,false,else,-,var,>,true,\n,true,for,number,\n,86.26,,,\n,-,true,else,\n,by,number,\n,\n,until,bool,or,else,<-,,,continue,\n,dynamic,or,\n,false,),dynamic,string,\n,/,[,<=,abcd,string,>=,%,\n,],continue,abcd,return,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,107))
        
    def test_case_108(self):
        input = """ dynamic % for	)


"abcd" a1 func	func	if	<-	for	112	if	dynamic break return return
[ <-	<=
, + >
>= <
>= ,	... a1 by
false true
string	not
<=	for == true	until
<=	==	by for	[
false	*	a1 string false
20.8e-9801 dynamic else ]	72 %	[ "abcd"	and
break
    """
        expect = "dynamic,%,for,),\n,\n,\n,abcd,a1,func,func,if,<-,for,112,if,dynamic,break,return,return,\n,[,<-,<=,\n,,,+,>,\n,>=,<,\n,>=,,,...,a1,by,\n,false,true,\n,string,not,\n,<=,for,==,true,until,\n,<=,==,by,for,[,\n,false,*,a1,string,false,\n,20.8e-9801,dynamic,else,],72,%,[,abcd,and,\n,break,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,108))
        
    def test_case_109(self):
        input = """ func	begin	if a1 end not string
, and	+	/ ) string
bool "abcd" "abcd"
-	, until 
 <	else continue	string end	elif	> *	if for continue 98.44	!= dynamic ==	/	string >	a1 "abcd"	not <=
!= true	number and	continue , continue	
 ] (
if ...	... !=	true or	>	!=	>= continue	by if
- ...	begin true
* return	]	dynamic >=
    """
        expect = "func,begin,if,a1,end,not,string,\n,,,and,+,/,),string,\n,bool,abcd,abcd,\n,-,,,until,\n,<,else,continue,string,end,elif,>,*,if,for,continue,98.44,!=,dynamic,==,/,string,>,a1,abcd,not,<=,\n,!=,true,number,and,continue,,,continue,\n,],(,\n,if,...,...,!=,true,or,>,!=,>=,continue,by,if,\n,-,...,begin,true,\n,*,return,],dynamic,>=,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,109))
        
    def test_case_110(self):
        input = """dynamic a438hfd
    """
        expect = "dynamic,a438hfd,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,110))
        
    def test_case_111(self):
        input = """dynamic 32372shd
    """
        expect = "dynamic,32372,shd,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,111))
        
    def test_case_112(self):
        input = """dynamic 246.01e3abc
    """
        expect = "dynamic,246.01e3,abc,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,112))
        
    def test_case_113(self):
        input = """dynamic dsfhds#
    """
        expect = "dynamic,dsfhds,Error Token #"
        self.assertTrue(TestLexer.test(input,expect,113))
        
    def test_case_114(self):
        input = """dynamic _sh73
    """
        expect = "dynamic,_sh73,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,114))
        
    def test_case_115(self):
        input = """dynamic shd"""
        expect = "dynamic,shd,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,115))
    def test_case_116(self):
        input = """dynamic shd"""
        expect = "dynamic,shd,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,116))
    def test_case_117(self):
        input = """dynamic shd"""
        expect = "dynamic,shd,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,117))
    def test_case_118(self):
        input = """dynamic shd"""
        expect = "dynamic,shd,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,118))
    def test_case_119(self):
        input = """dynamic shd"""
        expect = "dynamic,shd,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,119))
    def test_case_120(self):
        input = """string a<-"Idbr'\"s a
    """
        expect = "string,a,<-,Unclosed String: Idbr'\"s a"
        self.assertTrue(TestLexer.test(input,expect,120))
        
    def test_case_121(self):
        input = """string a<-"Ifwa\"s\n\"a
    """
        expect = "string,a,<-,Ifwa,s,\n,Unclosed String: a"
        self.assertTrue(TestLexer.test(input,expect,121))
        
    def test_case_122(self):
        input = """string a<-"dtsE\"s\"
    """
        expect = "string,a,<-,dtsE,s,Unclosed String: "
        self.assertTrue(TestLexer.test(input,expect,122))
        
    def test_case_123(self):
        input = """string a<-"2BP0'\"s\"
    """
        expect = "string,a,<-,2BP0'\"s,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,123))
        
    def test_case_124(self):
        input = """string a<-"ZOMZ\"s\"
    """
        expect = "string,a,<-,ZOMZ,s,Unclosed String: "
        self.assertTrue(TestLexer.test(input,expect,124))
        
    def test_case_125(self):
        input = """string a<-"ApUw'\"s\n\"a
    """
        expect = "string,a,<-,Unclosed String: ApUw'\"s"
        self.assertTrue(TestLexer.test(input,expect,125))
        
    def test_case_126(self):
        input = """string a<-"iYd1\"s\"
    """
        expect = "string,a,<-,iYd1,s,Unclosed String: "
        self.assertTrue(TestLexer.test(input,expect,126))
        
    def test_case_127(self):
        input = """string a<-"O79f'\"s a
    """
        expect = "string,a,<-,Unclosed String: O79f'\"s a"
        self.assertTrue(TestLexer.test(input,expect,127))
        
    def test_case_128(self):
        input = """string a<-"dImJ'\"s\"
    """
        expect = "string,a,<-,dImJ'\"s,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,128))
        
    def test_case_129(self):
        input = """string a<-"J3O4\"s\"
    """
        expect = "string,a,<-,J3O4,s,Unclosed String: "
        self.assertTrue(TestLexer.test(input,expect,129))
        
    def test_case_130(self):
        input = """ number }
    """
        expect = "number,Error Token }"
        self.assertTrue(TestLexer.test(input,expect,130))
        
    def test_case_131(self):
        input = """ for for not != number bool break and func ;
    """
        expect = "for,for,not,!=,number,bool,break,and,func,Error Token ;"
        self.assertTrue(TestLexer.test(input,expect,131))
        
    def test_case_132(self):
        input = """ ... }
    """
        expect = "...,Error Token }"
        self.assertTrue(TestLexer.test(input,expect,132))
        
    def test_case_133(self):
        input = """ IDENTIFIER <- + true &
    """
        expect = "IDENTIFIER,<-,+,true,Error Token &"
        self.assertTrue(TestLexer.test(input,expect,133))
        
    def test_case_134(self):
        input = """ dynamic >= begin true until and <= bool |
    """
        expect = "dynamic,>=,begin,true,until,and,<=,bool,Error Token |"
        self.assertTrue(TestLexer.test(input,expect,134))
        
    def test_case_135(self):
        input = """ bool / until dynamic '
    """
        expect = "bool,/,until,dynamic,Error Token '"
        self.assertTrue(TestLexer.test(input,expect,135))
        
    def test_case_136(self):
        input = """ <= }
    """
        expect = "<=,Error Token }"
        self.assertTrue(TestLexer.test(input,expect,136))
        
    def test_case_137(self):
        input = """ - / dynamic ^
    """
        expect = "-,/,dynamic,Error Token ^"
        self.assertTrue(TestLexer.test(input,expect,137))
        
    def test_case_138(self):
        input = """ string by ) STRINGLIT not {
    """
        expect = "string,by,),STRINGLIT,not,Error Token {"
        self.assertTrue(TestLexer.test(input,expect,138))
        
    def test_case_139(self):
        input = """ ) true / >= '
    """
        expect = "),true,/,>=,Error Token '"
        self.assertTrue(TestLexer.test(input,expect,139))
        
    def test_case_140(self):
        input = """ var @
    """
        expect = "var,Error Token @"
        self.assertTrue(TestLexer.test(input,expect,140))
        
    def test_case_141(self):
        input = """ func elif &
    """
        expect = "func,elif,Error Token &"
        self.assertTrue(TestLexer.test(input,expect,141))
        
    def test_case_142(self):
        input = """ IDENTIFIER ^
    """
        expect = "IDENTIFIER,Error Token ^"
        self.assertTrue(TestLexer.test(input,expect,142))
        
    def test_case_143(self):
        input = """ until var or ) ) var until / elif |
    """
        expect = "until,var,or,),),var,until,/,elif,Error Token |"
        self.assertTrue(TestLexer.test(input,expect,143))
        
    def test_case_144(self):
        input = """ false == not + true bool number #
    """
        expect = "false,==,not,+,true,bool,number,Error Token #"
        self.assertTrue(TestLexer.test(input,expect,144))
        
    def test_case_145(self):
        input = """ @
    """
        expect = "Error Token @"
        self.assertTrue(TestLexer.test(input,expect,145))
        
    def test_case_146(self):
        input = """ begin <= string &
    """
        expect = "begin,<=,string,Error Token &"
        self.assertTrue(TestLexer.test(input,expect,146))
        
    def test_case_147(self):
        input = """ true <= IDENTIFIER = bool == + <= @
    """
        expect = "true,<=,IDENTIFIER,=,bool,==,+,<=,Error Token @"
        self.assertTrue(TestLexer.test(input,expect,147))
        
    def test_case_148(self):
        input = """ not return &
    """
        expect = "not,return,Error Token &"
        self.assertTrue(TestLexer.test(input,expect,148))
        
    def test_case_149(self):
        input = """ > bool STRINGLIT [ if else = by #
    """
        expect = ">,bool,STRINGLIT,[,if,else,=,by,Error Token #"
        self.assertTrue(TestLexer.test(input,expect,149))
        
    def test_case_150(self):
        input = """string s <- " f \\# "
    """
        expect = "string,s,<-,Illegal Escape In String:  f \\#"
        self.assertTrue(TestLexer.test(input,expect,150))
        
    def test_case_151(self):
        input = """string s <- " Dpshv \\- "
    """
        expect = "string,s,<-,Illegal Escape In String:  Dpshv \\-"
        self.assertTrue(TestLexer.test(input,expect,151))
        
    def test_case_152(self):
        input = """string s <- " jJI \\= "
    """
        expect = "string,s,<-,Illegal Escape In String:  jJI \\="
        self.assertTrue(TestLexer.test(input,expect,152))
        
    def test_case_153(self):
        input = """string s <- " 2rnOaSLCf \\? "
    """
        expect = "string,s,<-,Illegal Escape In String:  2rnOaSLCf \\?"
        self.assertTrue(TestLexer.test(input,expect,153))
        
    def test_case_154(self):
        input = """string s <- " uydUGC75o \\d "
    """
        expect = "string,s,<-,Illegal Escape In String:  uydUGC75o \\d"
        self.assertTrue(TestLexer.test(input,expect,154))
        
    def test_case_155(self):
        input = """string s <- " m \\= "
    """
        expect = "string,s,<-,Illegal Escape In String:  m \\="
        self.assertTrue(TestLexer.test(input,expect,155))
        
    def test_case_156(self):
        input = """string s <- " UFxWIPss6 \\\" "
    """
        expect = "string,s,<-,Illegal Escape In String:  UFxWIPss6 \\\""
        self.assertTrue(TestLexer.test(input,expect,156))
        
    def test_case_157(self):
        input = """string s <- " 6 \\? "
    """
        expect = "string,s,<-,Illegal Escape In String:  6 \\?"
        self.assertTrue(TestLexer.test(input,expect,157))
        
    def test_case_158(self):
        input = """string s <- " zRWIqjY5S \\( "
    """
        expect = "string,s,<-,Illegal Escape In String:  zRWIqjY5S \\("
        self.assertTrue(TestLexer.test(input,expect,158))
        
    def test_case_159(self):
        input = """string s <- " phtTo \\< "
    """
        expect = "string,s,<-,Illegal Escape In String:  phtTo \\<"
        self.assertTrue(TestLexer.test(input,expect,159))
        
    def test_case_160(self):
        input = """string s <- " eRoDp \\9 "
    """
        expect = "string,s,<-,Illegal Escape In String:  eRoDp \\9"
        self.assertTrue(TestLexer.test(input,expect,160))
        
    def test_case_161(self):
        input = """string s <- " 1Rs092Mqq \\1 "
    """
        expect = "string,s,<-,Illegal Escape In String:  1Rs092Mqq \\1"
        self.assertTrue(TestLexer.test(input,expect,161))
        
    def test_case_162(self):
        input = """string s <- " pajHVtLKf \\? "
    """
        expect = "string,s,<-,Illegal Escape In String:  pajHVtLKf \\?"
        self.assertTrue(TestLexer.test(input,expect,162))
        
    def test_case_163(self):
        input = """string s <- " ykb17JZd \\( "
    """
        expect = "string,s,<-,Illegal Escape In String:  ykb17JZd \\("
        self.assertTrue(TestLexer.test(input,expect,163))
        
    def test_case_164(self):
        input = """string s <- " JLVCWyE \\~ "
    """
        expect = "string,s,<-,Illegal Escape In String:  JLVCWyE \\~"
        self.assertTrue(TestLexer.test(input,expect,164))
        
    def test_case_165(self):
        input = """string s <- " gfJFW \\a "
    """
        expect = "string,s,<-,Illegal Escape In String:  gfJFW \\a"
        self.assertTrue(TestLexer.test(input,expect,165))
        
    def test_case_166(self):
        input = """string s <- " c0qY5gVd \\A "
    """
        expect = "string,s,<-,Illegal Escape In String:  c0qY5gVd \\A"
        self.assertTrue(TestLexer.test(input,expect,166))
        
    def test_case_167(self):
        input = """string s <- " PEgzT \\? "
    """
        expect = "string,s,<-,Illegal Escape In String:  PEgzT \\?"
        self.assertTrue(TestLexer.test(input,expect,167))
        
    def test_case_168(self):
        input = """string s <- " x0uK \\( "
    """
        expect = "string,s,<-,Illegal Escape In String:  x0uK \\("
        self.assertTrue(TestLexer.test(input,expect,168))
        
    def test_case_169(self):
        input = """string s <- " pOHQPy \\# "
    """
        expect = "string,s,<-,Illegal Escape In String:  pOHQPy \\#"
        self.assertTrue(TestLexer.test(input,expect,169))
        
    def test_case_170(self):
        input = """elseei
    """
        expect = "elseei,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,170))
        
    def test_case_171(self):
        input = """andFy
    """
        expect = "andFy,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,171))
        
    def test_case_172(self):
        input = """beginnt
    """
        expect = "beginnt,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,172))
        
    def test_case_173(self):
        input = """orh3
    """
        expect = "orh3,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,173))
        
    def test_case_174(self):
        input = """boolHR
    """
        expect = "boolHR,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,174))
        
    def test_case_175(self):
        input = """dynamic96
    """
        expect = "dynamic96,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,175))
        
    def test_case_176(self):
        input = """notvN
    """
        expect = "notvN,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,176))
        
    def test_case_177(self):
        input = """not4U
    """
        expect = "not4U,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,177))
        
    def test_case_178(self):
        input = """andXH
    """
        expect = "andXH,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,178))
        
    def test_case_179(self):
        input = """beginvE
    """
        expect = "beginvE,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,179))
        
    def test_case_180(self):
        input = """vqJSByA <-1682
    """
        expect = "vqJSByA,<-,1682,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,180))
        
    def test_case_181(self):
        input = """var v3LUkSb <--910
    """
        expect = "var,v3LUkSb,<-,-,910,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,181))
        
    def test_case_182(self):
        input = """vzLWaRt <-357
    """
        expect = "vzLWaRt,<-,357,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,182))
        
    def test_case_183(self):
        input = """dynamic vJT68eY <--1996
    """
        expect = "dynamic,vJT68eY,<-,-,1996,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,183))
        
    def test_case_184(self):
        input = """boolean vgVQtc3 <-2581
    """
        expect = "boolean,vgVQtc3,<-,2581,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,184))
        
    def test_case_185(self):
        input = """number vEHTZsK <-1206
    """
        expect = "number,vEHTZsK,<-,1206,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,185))
        
    def test_case_186(self):
        input = """var vec9qXO <-802
    """
        expect = "var,vec9qXO,<-,802,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,186))
        
    def test_case_187(self):
        input = """vElpjE1 <-2756
    """
        expect = "vElpjE1,<-,2756,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,187))
        
    def test_case_188(self):
        input = """func f5rD0JX(pf9izMs,pNVYRR4) \n begin \nfunc fhMHr1f(pgLbWLT,pPQCTyu,pOuqYuP) \n begin \nboolean vXZzyCG <--1584\n end\n end
    """
        expect = "func,f5rD0JX,(,pf9izMs,,,pNVYRR4,),\n,begin,\n,func,fhMHr1f,(,pgLbWLT,,,pPQCTyu,,,pOuqYuP,),\n,begin,\n,boolean,vXZzyCG,<-,-,1584,\n,end,\n,end,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,188))
        
    def test_case_189(self):
        input = """func fix9gnC(p4Rf3wz,poovRd3,pgRhBpR,p5wZD7m) \n begin \nstring vUioJNU <--1627\n end
    """
        expect = "func,fix9gnC,(,p4Rf3wz,,,poovRd3,,,pgRhBpR,,,p5wZD7m,),\n,begin,\n,string,vUioJNU,<-,-,1627,\n,end,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,189))
        
    def test_case_190(self):
        input = """dynamic v4zDg6L <-1912
    """
        expect = "dynamic,v4zDg6L,<-,1912,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,190))
        
    def test_case_191(self):
        input = """string vn0AmFi <--421
    """
        expect = "string,vn0AmFi,<-,-,421,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,191))
        
    def test_case_192(self):
        input = """func fng0eH8(pYOhQ1k,pCCMHvT) \n begin \nfunc f0EAfGN() \n begin \nboolean vDavDHp <-35\n end\n end
    """
        expect = "func,fng0eH8,(,pYOhQ1k,,,pCCMHvT,),\n,begin,\n,func,f0EAfGN,(,),\n,begin,\n,boolean,vDavDHp,<-,35,\n,end,\n,end,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,192))
        
    def test_case_193(self):
        input = """string votRnS6 <--1305
    """
        expect = "string,votRnS6,<-,-,1305,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,193))
        
    def test_case_194(self):
        input = """string vXXBmBo <-561
    """
        expect = "string,vXXBmBo,<-,561,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,194))
        
    def test_case_195(self):
        input = """func f6Hwoj6(pQ4Wud7) \n begin \nstring vnZHBcP <-2101\n end
    """
        expect = "func,f6Hwoj6,(,pQ4Wud7,),\n,begin,\n,string,vnZHBcP,<-,2101,\n,end,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,195))
        
    def test_case_196(self):
        input = """dynamic vnO86ug <--315
    """
        expect = "dynamic,vnO86ug,<-,-,315,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,196))
        
    def test_case_197(self):
        input = """func f25NQdl(pMeMT0G,pWlIFAO,ppGWPHD) \n begin \ndynamic v1dzrvd <-2253\n end
    """
        expect = "func,f25NQdl,(,pMeMT0G,,,pWlIFAO,,,ppGWPHD,),\n,begin,\n,dynamic,v1dzrvd,<-,2253,\n,end,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,197))
        
    def test_case_198(self):
        input = """func flEQy4E(pX1wOJg,pFGi4K8,pGwMwVw,pydWdw1) \n begin \nvar v5lCS13 <-2282\n end
    """
        expect = "func,flEQy4E,(,pX1wOJg,,,pFGi4K8,,,pGwMwVw,,,pydWdw1,),\n,begin,\n,var,v5lCS13,<-,2282,\n,end,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,198))
        
    def test_case_199(self):
        input = """func fxhcp9y(p64YRnr,plSOHfA) \n begin \nv2idhiC <-2799\n end
    """
        expect = "func,fxhcp9y,(,p64YRnr,,,plSOHfA,),\n,begin,\n,v2idhiC,<-,2799,\n,end,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,199))
        