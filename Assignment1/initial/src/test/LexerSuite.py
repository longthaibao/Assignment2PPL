# import unittest
# from TestUtils import TestLexer

# class LexerSuite(unittest.TestCase): 

#     def test_case_0(self):
#         input = """ or % / else	break	by	+	< !=	until	and
# end begin	func
# + +	>
# -
# == elif <- <= (	break ( [	<-	for begin elif	and	"abcd"
# by	end / "abcd" string	,	104 elif = and != false	not	else [ else
# ... /	if < until by for return until	<= 
# else <=	[ != >=	- < 36
# return >= begin	"abcd" = 
# <	func	begin
# break
#     """
#         expect = "or,%,/,else,break,by,+,<,!=,until,and,\n,end,begin,func,\n,+,+,>,\n,-,\n,==,elif,<-,<=,(,break,(,[,<-,for,begin,elif,and,abcd,\n,by,end,/,abcd,string,,,104,elif,=,and,!=,false,not,else,[,else,\n,...,/,if,<,until,by,for,return,until,<=,\n,else,<=,[,!=,>=,-,<,36,\n,return,>=,begin,abcd,=,\n,<,func,begin,\n,break,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,100))
#         except:
#             print("fail testcase 0")
        
#     def test_case_1(self):
#         input = """	

# ==	func
# >= var
# ...	break	not 105 <-	=	]	string "abcd" ] until	<
# begin ) "abcd" != continue


# "abcd" number >=	break var bool end , < break end	- 33.53e324	!= not

# 	]
# string (
# bool [ number
# ==	(
# begin
# by	if -	if	>=
# 24.69	false +	/ not continue	and ]	]
# <= end bool	<-	continue
# (
# bool else not ==
# begin for
# if true	=	func begin ...
# ( * or	for until elif	[
# ) for
#     """
#         expect = "\n,\n,==,func,\n,>=,var,\n,...,break,not,105,<-,=,],string,abcd,],until,<,\n,begin,),abcd,!=,continue,\n,\n,\n,abcd,number,>=,break,var,bool,end,,,<,break,end,-,33.53e324,!=,not,\n,\n,],\n,string,(,\n,bool,[,number,\n,==,(,\n,begin,\n,by,if,-,if,>=,\n,24.69,false,+,/,not,continue,and,],],\n,<=,end,bool,<-,continue,\n,(,\n,bool,else,not,==,\n,begin,for,\n,if,true,=,func,begin,...,\n,(,*,or,for,until,elif,[,\n,),for,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,101))
#         except:
#             print("fail testcase 1")
        
#     def test_case_2(self):
#         input = """
# =	begin + dynamic 
#  -	*
# return	/ - break
# = 14 return else return 
#  <-
# or *	+	elif	string >	bool	continue	77E5776 a1 or
# <- == or continue	true /	continue	continue func
# string	break "abcd"
# >=	==
# until	-	/ bool	begin
# <- ( 
#  ) ==	by
# and and	!=	if false
# a1 >=	<=	(
# %	not dynamic
# * until	continue
# for return	return	] <-	end	func <=	var or	> if	dynamic
# break	begin dynamic	continue	127e-6561	begin
#     """
#         expect = "\n,=,begin,+,dynamic,\n,-,*,\n,return,/,-,break,\n,=,14,return,else,return,\n,<-,\n,or,*,+,elif,string,>,bool,continue,77E5776,a1,or,\n,<-,==,or,continue,true,/,continue,continue,func,\n,string,break,abcd,\n,>=,==,\n,until,-,/,bool,begin,\n,<-,(,\n,),==,by,\n,and,and,!=,if,false,\n,a1,>=,<=,(,\n,%,not,dynamic,\n,*,until,continue,\n,for,return,return,],<-,end,func,<=,var,or,>,if,dynamic,\n,break,begin,dynamic,continue,127e-6561,begin,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,102))
#         except:
#             print("fail testcase 2")
        
#     def test_case_3(self):
#         input = """ , by	,
# /	until	false ]
# -	= and =	return dynamic	continue	or	>	<- <= a1	by ) % ) break a1	/ ,	>= string true	] by [	/	return + for +	break a1	( >
# >
# )	+	
# 	, number until 118e-3025 bool 

# =	>= func end bool *
# ==	true
# end end	<= number -	>=	
# 	)	
#  %	
# 	not + true
# , <= not bool	>
# until % +
#     """
#         expect = ",,by,,,\n,/,until,false,],\n,-,=,and,=,return,dynamic,continue,or,>,<-,<=,a1,by,),%,),break,a1,/,,,>=,string,true,],by,[,/,return,+,for,+,break,a1,(,>,\n,>,\n,),+,\n,,,number,until,118e-3025,bool,\n,\n,=,>=,func,end,bool,*,\n,==,true,\n,end,end,<=,number,-,>=,\n,),\n,%,\n,not,+,true,\n,,,<=,not,bool,>,\n,until,%,+,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,103))
#         except:
#             print("fail testcase 3")
        
#     def test_case_4(self):
#         input = """
# elif not	true break	false !=	by	) 21.75	not	if	, <- ,	a1 == ,	>	/ /
# by true begin < <=	(	or until	,	var	else -
# , "abcd" string
# (	by	continue elif until elif ==	<= not	

# not	break	if
# if begin
# % true [	a1	88E-400 func begin bool	
# 	== true	* -
#     """
#         expect = "\n,elif,not,true,break,false,!=,by,),21.75,not,if,,,<-,,,a1,==,,,>,/,/,\n,by,true,begin,<,<=,(,or,until,,,var,else,-,\n,,,abcd,string,\n,(,by,continue,elif,until,elif,==,<=,not,\n,\n,not,break,if,\n,if,begin,\n,%,true,[,a1,88E-400,func,begin,bool,\n,==,true,*,-,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,104))
#         except:
#             print("fail testcase 4")
        
#     def test_case_5(self):
#         input = """	<=	/ -
# bool	until

#  by a1 bool	"abcd" elif , *
# var or
# if * ==	for until
# not	!=
#     """
#         expect = "<=,/,-,\n,bool,until,\n,\n,by,a1,bool,abcd,elif,,,*,\n,var,or,\n,if,*,==,for,until,\n,not,!=,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,105))
#         except:
#             print("fail testcase 5")
        
#     def test_case_6(self):
#         input = """ or bool
# string	>
# <= var ...
# number	/ string +	begin	begin	return	/	else	... by
# break	until	[ [ ] / string
# for true == for != =
# break
# or
# end ...
# by return ... func or continue
# if end until
# if else ==	<=
# ... 
# 	)	<- <=	"abcd" and
# "abcd"	a1
# ]	- return [	else break
#     """
#         expect = "or,bool,\n,string,>,\n,<=,var,...,\n,number,/,string,+,begin,begin,return,/,else,...,by,\n,break,until,[,[,],/,string,\n,for,true,==,for,!=,=,\n,break,\n,or,\n,end,...,\n,by,return,...,func,or,continue,\n,if,end,until,\n,if,else,==,<=,\n,...,\n,),<-,<=,abcd,and,\n,abcd,a1,\n,],-,return,[,else,break,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,106))
#         except:
#             print("fail testcase 6")
        
#     def test_case_7(self):
#         input = """	)	until return 140.52E-900 =
# number	,
# a1 and	86e-9025
# - for (	) < dynamic / "abcd" 
# 	"abcd"	!= continue < != string break return var ]	bool *
# else break	if	% % var
#     """
#         expect = "),until,return,140.52E-900,=,\n,number,,,\n,a1,and,86e-9025,\n,-,for,(,),<,dynamic,/,abcd,\n,abcd,!=,continue,<,!=,string,break,return,var,],bool,*,\n,else,break,if,%,%,var,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,107))
#         except:
#             print("fail testcase 7")
        
#     def test_case_8(self):
#         input = """ func	true	continue	or	or elif	<=
# -
# dynamic
# ==	elif	<=	<- end	<- dynamic bool	+ or a1 true break until
# *	% ==
# dynamic	*	not or	var 14e-3844	a1 begin elif = ]
# bool for "abcd"	until	number end	(
# elif
#     """
#         expect = "func,true,continue,or,or,elif,<=,\n,-,\n,dynamic,\n,==,elif,<=,<-,end,<-,dynamic,bool,+,or,a1,true,break,until,\n,*,%,==,\n,dynamic,*,not,or,var,14e-3844,a1,begin,elif,=,],\n,bool,for,abcd,until,number,end,(,\n,elif,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,108))
#         except:
#             print("fail testcase 8")
        
#     def test_case_9(self):
#         input = """	>= )	-	] elif until else	<= string
# %	dynamic	string + false	a1
# ,
# % continue begin != else
# + ] < func else
# [	if for	17E-1764 func dynamic	"abcd" number
# until , ) != break
# if
# var	> [	func	string 61e625
#     """
#         expect = ">=,),-,],elif,until,else,<=,string,\n,%,dynamic,string,+,false,a1,\n,,,\n,%,continue,begin,!=,else,\n,+,],<,func,else,\n,[,if,for,17E-1764,func,dynamic,abcd,number,\n,until,,,),!=,break,\n,if,\n,var,>,[,func,string,61e625,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,109))
#         except:
#             print("fail testcase 9")
        
#     def test_case_10(self):
#         input = """dynamic abc123
#     """
#         expect = "dynamic,abc123,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,110))
#         except:
#             print("fail testcase 10")
        
#     def test_case_11(self):
#         input = """dynamic 1ae
#     """
#         expect = "dynamic,1,ae,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,111))
#         except:
#             print("fail testcase 11")
        
#     def test_case_12(self):
#         input = """dynamic 1.232eabc
#     """
#         expect = "dynamic,1.232,eabc,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,112))
#         except:
#             print("fail testcase 12")
        
#     def test_case_13(self):
#         input = """dynamic abC1#
#     """
#         expect = "dynamic,abC1,Error Token #"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,113))
#         except:
#             print("fail testcase 13")
        
#     def test_case_14(self):
#         input = """dynamic _abt
#     """
#         expect = "dynamic,_abt,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,114))
#         except:
#             print("fail testcase 14")
        
#     def test_case_15(self):
#         input = """
# ## comment
# func main()
# begin 
#               ##hello
# ## "hello"
# var a <- "## comment in string"    
# end

#     """
#         expect = "\n,## comment,\n,func,main,(,),\n,begin,\n,##hello,\n,## \"hello\",\n,var,a,<-,## comment in string,\n,end,\n,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,115))
#         except:
#             print("fail testcase 15")
        
#     def test_case_16(self):
#         input = """

# func main()
# begin ## comment
#               ##hello
# ## "hello"
# var a <- "## comment in string"    
# end

#     """
#         expect = "\n,\n,func,main,(,),\n,begin,## comment,\n,##hello,\n,## \"hello\",\n,var,a,<-,## comment in string,\n,end,\n,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,116))
#         except:
#             print("fail testcase 16")
        
#     def test_case_17(self):
#         input = """

# func main()
# begin 
#              ## comment ##hello
# ## "hello"
# var a <- "## comment in string"    
# end

#     """
#         expect = "\n,\n,func,main,(,),\n,begin,\n,## comment ##hello,\n,## \"hello\",\n,var,a,<-,## comment in string,\n,end,\n,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,117))
#         except:
#             print("fail testcase 17")
        
#     def test_case_18(self):
#         input = """

# func main()
# begin 
#               ##hello
# ## "hello"
# var a <- "## comment in string"    ## comment
# end

#     """
#         expect = "\n,\n,func,main,(,),\n,begin,\n,##hello,\n,## \"hello\",\n,var,a,<-,## comment in string,## comment,\n,end,\n,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,118))
#         except:
#             print("fail testcase 18")
        
#     def test_case_19(self):
#         input = """

# func main()
# begin 
#               ##hello
# ## "hello"
# var a <- "## comment in string"    
# end
# ## comment
#     """
#         expect = "\n,\n,func,main,(,),\n,begin,\n,##hello,\n,## \"hello\",\n,var,a,<-,## comment in string,\n,end,\n,## comment,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,119))
#         except:
#             print("fail testcase 19")
        
#     def test_case_20(self):
#         input = """string a<-"k0ZZ'\"s a
#     """
#         expect = "string,a,<-,Unclosed String: k0ZZ'\"s a"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,120))
#         except:
#             print("fail testcase 20")
        
#     def test_case_21(self):
#         input = """string a<-"q0Fk'\"s\n\"a
#     """
#         expect = "string,a,<-,Unclosed String: q0Fk'\"s"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,121))
#         except:
#             print("fail testcase 21")
        
#     def test_case_22(self):
#         input = """string a<-"g55p'\"s\"
#     """
#         expect = "string,a,<-,g55p'\"s,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,122))
#         except:
#             print("fail testcase 22")
        
#     def test_case_23(self):
#         input = """string a<-"Z7M8'\"s a
#     """
#         expect = "string,a,<-,Unclosed String: Z7M8'\"s a"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,123))
#         except:
#             print("fail testcase 23")
        
#     def test_case_24(self):
#         input = """string a<-"ZWGi'\"s\n\"a
#     """
#         expect = "string,a,<-,Unclosed String: ZWGi'\"s"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,124))
#         except:
#             print("fail testcase 24")
        
#     def test_case_25(self):
#         input = """string a<-"wCbw'\"s a
#     """
#         expect = "string,a,<-,Unclosed String: wCbw'\"s a"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,125))
#         except:
#             print("fail testcase 25")
        
#     def test_case_26(self):
#         input = """string a<-"I84x\"s a
#     """
#         expect = "string,a,<-,I84x,s,a,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,126))
#         except:
#             print("fail testcase 26")
        
#     def test_case_27(self):
#         input = """string a<-"RcMC'\"s\"
#     """
#         expect = "string,a,<-,RcMC'\"s,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,127))
#         except:
#             print("fail testcase 27")
        
#     def test_case_28(self):
#         input = """string a<-"UjdZ'\"s a
#     """
#         expect = "string,a,<-,Unclosed String: UjdZ'\"s a"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,128))
#         except:
#             print("fail testcase 28")
        
#     def test_case_29(self):
#         input = """string a<-"RL9u'\"s a
#     """
#         expect = "string,a,<-,Unclosed String: RL9u'\"s a"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,129))
#         except:
#             print("fail testcase 29")
        
#     def test_case_30(self):
#         input = """ if by dynamic if }
#     """
#         expect = "if,by,dynamic,if,Error Token }"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,130))
#         except:
#             print("fail testcase 30")
        
#     def test_case_31(self):
#         input = """ ( == / true )
#  if |
#     """
#         expect = "(,==,/,true,),\n,if,Error Token |"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,131))
#         except:
#             print("fail testcase 31")
        
#     def test_case_32(self):
#         input = """ % string / , , + ... > break {
#     """
#         expect = "%,string,/,,,,,+,...,>,break,Error Token {"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,132))
#         except:
#             print("fail testcase 32")
        
#     def test_case_33(self):
#         input = """ func false bool func dynamic for < func '
#     """
#         expect = "func,false,bool,func,dynamic,for,<,func,Error Token '"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,133))
#         except:
#             print("fail testcase 33")
        
#     def test_case_34(self):
#         input = """ and for until dynamic ;
#     """
#         expect = "and,for,until,dynamic,Error Token ;"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,134))
#         except:
#             print("fail testcase 34")
        
#     def test_case_35(self):
#         input = """ until {
#     """
#         expect = "until,Error Token {"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,135))
#         except:
#             print("fail testcase 35")
        
#     def test_case_36(self):
#         input = """ ~
#     """
#         expect = "Error Token ~"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,136))
#         except:
#             print("fail testcase 36")
        
#     def test_case_37(self):
#         input = """ false ( false var for - $
#     """
#         expect = "false,(,false,var,for,-,Error Token $"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,137))
#         except:
#             print("fail testcase 37")
        
#     def test_case_38(self):
#         input = """ or or true % else [ == var }
#     """
#         expect = "or,or,true,%,else,[,==,var,Error Token }"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,138))
#         except:
#             print("fail testcase 38")
        
#     def test_case_39(self):
#         input = """ ) {
#     """
#         expect = "),Error Token {"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,139))
#         except:
#             print("fail testcase 39")
        
#     def test_case_40(self):
#         input = """
#  |
#     """
#         expect = "\n,Error Token |"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,140))
#         except:
#             print("fail testcase 40")
        
#     def test_case_41(self):
#         input = """ @
#     """
#         expect = "Error Token @"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,141))
#         except:
#             print("fail testcase 41")
        
#     def test_case_42(self):
#         input = """ ] not * continue string < var * by '
#     """
#         expect = "],not,*,continue,string,<,var,*,by,Error Token '"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,142))
#         except:
#             print("fail testcase 42")
        
#     def test_case_43(self):
#         input = """ by ) ] - - !
#     """
#         expect = "by,),],-,-,Error Token !"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,143))
#         except:
#             print("fail testcase 43")
        
#     def test_case_44(self):
#         input = """ < elif * ... <- {
#     """
#         expect = "<,elif,*,...,<-,Error Token {"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,144))
#         except:
#             print("fail testcase 44")
        
#     def test_case_45(self):
#         input = """ number not == string STRINGLIT or $
#     """
#         expect = "number,not,==,string,STRINGLIT,or,Error Token $"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,145))
#         except:
#             print("fail testcase 45")
        
#     def test_case_46(self):
#         input = """
#  string by
#  STRINGLIT ~
#     """
#         expect = "\n,string,by,\n,STRINGLIT,Error Token ~"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,146))
#         except:
#             print("fail testcase 46")
        
#     def test_case_47(self):
#         input = """ / >= ] return break not !
#     """
#         expect = "/,>=,],return,break,not,Error Token !"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,147))
#         except:
#             print("fail testcase 47")
        
#     def test_case_48(self):
#         input = """ ( + - else $
#     """
#         expect = "(,+,-,else,Error Token $"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,148))
#         except:
#             print("fail testcase 48")
        
#     def test_case_49(self):
#         input = """ NUMLIT % % for return , &
#     """
#         expect = "NUMLIT,%,%,for,return,,,Error Token &"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,149))
#         except:
#             print("fail testcase 49")
        
#     def test_case_50(self):
#         input = """string s <- " pfaHa6A \\c "
#     """
#         expect = "string,s,<-,Illegal Escape In String:  pfaHa6A \\c"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,150))
#         except:
#             print("fail testcase 50")
        
#     def test_case_51(self):
#         input = """string s <- " Sp \\  "
#     """
#         expect = "string,s,<-,Illegal Escape In String:  Sp \\ "
#         try:
#             self.assertTrue(TestLexer.test(input,expect,151))
#         except:
#             print("fail testcase 51")
        
#     def test_case_52(self):
#         input = """string s <- " n5dejFXJ \\A "
#     """
#         expect = "string,s,<-,Illegal Escape In String:  n5dejFXJ \\A"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,152))
#         except:
#             print("fail testcase 52")
        
#     def test_case_53(self):
#         input = """string s <- " bY6pC \\( "
#     """
#         expect = "string,s,<-,Illegal Escape In String:  bY6pC \\("
#         try:
#             self.assertTrue(TestLexer.test(input,expect,153))
#         except:
#             print("fail testcase 53")
        
#     def test_case_54(self):
#         input = """string s <- " Qv2yi \\A "
#     """
#         expect = "string,s,<-,Illegal Escape In String:  Qv2yi \\A"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,154))
#         except:
#             print("fail testcase 54")
        
#     def test_case_55(self):
#         input = """string s <- " 9b8m \\c "
#     """
#         expect = "string,s,<-,Illegal Escape In String:  9b8m \\c"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,155))
#         except:
#             print("fail testcase 55")
        
#     def test_case_56(self):
#         input = """string s <- "  \\~ "
#     """
#         expect = "string,s,<-,Illegal Escape In String:   \\~"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,156))
#         except:
#             print("fail testcase 56")
        
#     def test_case_57(self):
#         input = """string s <- " PqYGo \\z "
#     """
#         expect = "string,s,<-,Illegal Escape In String:  PqYGo \\z"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,157))
#         except:
#             print("fail testcase 57")
        
#     def test_case_58(self):
#         input = """string s <- " prDy \\( "
#     """
#         expect = "string,s,<-,Illegal Escape In String:  prDy \\("
#         try:
#             self.assertTrue(TestLexer.test(input,expect,158))
#         except:
#             print("fail testcase 58")
        
#     def test_case_59(self):
#         input = """string s <- " w \\\" "
#     """
#         expect = "string,s,<-,Illegal Escape In String:  w \\\""
#         try:
#             self.assertTrue(TestLexer.test(input,expect,159))
#         except:
#             print("fail testcase 59")
        
#     def test_case_60(self):
#         input = """string s <- " 4tSQ8 \\# "
#     """
#         expect = "string,s,<-,Illegal Escape In String:  4tSQ8 \\#"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,160))
#         except:
#             print("fail testcase 60")
        
#     def test_case_61(self):
#         input = """string s <- "  \\- "
#     """
#         expect = "string,s,<-,Illegal Escape In String:   \\-"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,161))
#         except:
#             print("fail testcase 61")
        
#     def test_case_62(self):
#         input = """string s <- " EV4j \\A "
#     """
#         expect = "string,s,<-,Illegal Escape In String:  EV4j \\A"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,162))
#         except:
#             print("fail testcase 62")
        
#     def test_case_63(self):
#         input = """string s <- " t1rbSu6Nd \\9 "
#     """
#         expect = "string,s,<-,Illegal Escape In String:  t1rbSu6Nd \\9"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,163))
#         except:
#             print("fail testcase 63")
        
#     def test_case_64(self):
#         input = """string s <- " hVSqKvSF \\( "
#     """
#         expect = "string,s,<-,Illegal Escape In String:  hVSqKvSF \\("
#         try:
#             self.assertTrue(TestLexer.test(input,expect,164))
#         except:
#             print("fail testcase 64")
        
#     def test_case_65(self):
#         input = """string s <- " JUwKZ \\| "
#     """
#         expect = "string,s,<-,Illegal Escape In String:  JUwKZ \\|"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,165))
#         except:
#             print("fail testcase 65")
        
#     def test_case_66(self):
#         input = """string s <- " 8 \\z "
#     """
#         expect = "string,s,<-,Illegal Escape In String:  8 \\z"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,166))
#         except:
#             print("fail testcase 66")
        
#     def test_case_67(self):
#         input = """string s <- " THZ6RJ \\a "
#     """
#         expect = "string,s,<-,Illegal Escape In String:  THZ6RJ \\a"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,167))
#         except:
#             print("fail testcase 67")
        
#     def test_case_68(self):
#         input = """string s <- " IqO6TFT4 \\| "
#     """
#         expect = "string,s,<-,Illegal Escape In String:  IqO6TFT4 \\|"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,168))
#         except:
#             print("fail testcase 68")
        
#     def test_case_69(self):
#         input = """string s <- " t \\\" "
#     """
#         expect = "string,s,<-,Illegal Escape In String:  t \\\""
#         try:
#             self.assertTrue(TestLexer.test(input,expect,169))
#         except:
#             print("fail testcase 69")
        
#     def test_case_70(self):
#         input = """numberC0
#     """
#         expect = "numberC0,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,170))
#         except:
#             print("fail testcase 70")
        
#     def test_case_71(self):
#         input = """continue0i
#     """
#         expect = "continue0i,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,171))
#         except:
#             print("fail testcase 71")
        
#     def test_case_72(self):
#         input = """andTr
#     """
#         expect = "andTr,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,172))
#         except:
#             print("fail testcase 72")
        
#     def test_case_73(self):
#         input = """falseRX
#     """
#         expect = "falseRX,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,173))
#         except:
#             print("fail testcase 73")
        
#     def test_case_74(self):
#         input = """untill2
#     """
#         expect = "untill2,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,174))
#         except:
#             print("fail testcase 74")
        
#     def test_case_75(self):
#         input = """until6W
#     """
#         expect = "until6W,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,175))
#         except:
#             print("fail testcase 75")
        
#     def test_case_76(self):
#         input = """boolzo
#     """
#         expect = "boolzo,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,176))
#         except:
#             print("fail testcase 76")
        
#     def test_case_77(self):
#         input = """falsePY
#     """
#         expect = "falsePY,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,177))
#         except:
#             print("fail testcase 77")
        
#     def test_case_78(self):
#         input = """breakMm
#     """
#         expect = "breakMm,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,178))
#         except:
#             print("fail testcase 78")
        
#     def test_case_79(self):
#         input = """falsecc
#     """
#         expect = "falsecc,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,179))
#         except:
#             print("fail testcase 79")
        
#     def test_case_80(self):
#         input = """func fvqncn5(ptUUivo,pt9ChWy) \n begin \nvaU7DLz <--855\n end
#     """
#         expect = "func,fvqncn5,(,ptUUivo,,,pt9ChWy,),\n,begin,\n,vaU7DLz,<-,-,855,\n,end,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,180))
#         except:
#             print("fail testcase 80")
        
#     def test_case_81(self):
#         input = """dynamic veW6opk <--2684
#     """
#         expect = "dynamic,veW6opk,<-,-,2684,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,181))
#         except:
#             print("fail testcase 81")
        
#     def test_case_82(self):
#         input = """var vu7gJDP <--2198
#     """
#         expect = "var,vu7gJDP,<-,-,2198,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,182))
#         except:
#             print("fail testcase 82")
        
#     def test_case_83(self):
#         input = """boolean vcyRO8h <--602
#     """
#         expect = "boolean,vcyRO8h,<-,-,602,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,183))
#         except:
#             print("fail testcase 83")
        
#     def test_case_84(self):
#         input = """func fBCSTGA() \n begin \nvruhQfr <--1594\n end
#     """
#         expect = "func,fBCSTGA,(,),\n,begin,\n,vruhQfr,<-,-,1594,\n,end,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,184))
#         except:
#             print("fail testcase 84")
        
#     def test_case_85(self):
#         input = """vKnuTA5 <-1692
#     """
#         expect = "vKnuTA5,<-,1692,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,185))
#         except:
#             print("fail testcase 85")
        
#     def test_case_86(self):
#         input = """func fyaWVXf(pASAqXI,pddN5GE,pBkmU5b,pUmCUbw) \n begin \nboolean v9gbiqR <-1567\n end
#     """
#         expect = "func,fyaWVXf,(,pASAqXI,,,pddN5GE,,,pBkmU5b,,,pUmCUbw,),\n,begin,\n,boolean,v9gbiqR,<-,1567,\n,end,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,186))
#         except:
#             print("fail testcase 86")
        
#     def test_case_87(self):
#         input = """func fbGxRrI(pY3P53C,pTBwimE,p5wpsJ9,pIOdPI7) \n begin \nfunc f966j3M(pYGGpUM) \n begin \nnumber veAcmxu <--1305\n end\n end
#     """
#         expect = "func,fbGxRrI,(,pY3P53C,,,pTBwimE,,,p5wpsJ9,,,pIOdPI7,),\n,begin,\n,func,f966j3M,(,pYGGpUM,),\n,begin,\n,number,veAcmxu,<-,-,1305,\n,end,\n,end,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,187))
#         except:
#             print("fail testcase 87")
        
#     def test_case_88(self):
#         input = """var vEUOiSM <-1954
#     """
#         expect = "var,vEUOiSM,<-,1954,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,188))
#         except:
#             print("fail testcase 88")
        
#     def test_case_89(self):
#         input = """func f5sDsfe(pcJahdt,pYxCvWJ,p57SP6i) \n begin \nvar vMs8lZD <-1400\n end
#     """
#         expect = "func,f5sDsfe,(,pcJahdt,,,pYxCvWJ,,,p57SP6i,),\n,begin,\n,var,vMs8lZD,<-,1400,\n,end,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,189))
#         except:
#             print("fail testcase 89")
        
#     def test_case_90(self):
#         input = """dynamic v0R1Fkf <--2682
#     """
#         expect = "dynamic,v0R1Fkf,<-,-,2682,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,190))
#         except:
#             print("fail testcase 90")
        
#     def test_case_91(self):
#         input = """vRRAldr <-892
#     """
#         expect = "vRRAldr,<-,892,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,191))
#         except:
#             print("fail testcase 91")
        
#     def test_case_92(self):
#         input = """dynamic vS3cy5G <--955
#     """
#         expect = "dynamic,vS3cy5G,<-,-,955,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,192))
#         except:
#             print("fail testcase 92")
        
#     def test_case_93(self):
#         input = """vCEm26B <--2185
#     """
#         expect = "vCEm26B,<-,-,2185,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,193))
#         except:
#             print("fail testcase 93")
        
#     def test_case_94(self):
#         input = """string vX1tzDl <-2639
#     """
#         expect = "string,vX1tzDl,<-,2639,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,194))
#         except:
#             print("fail testcase 94")
        
#     def test_case_95(self):
#         input = """number vrL1Gnl <--422
#     """
#         expect = "number,vrL1Gnl,<-,-,422,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,195))
#         except:
#             print("fail testcase 95")
        
#     def test_case_96(self):
#         input = """func f34EcjP(pr8awFc,plW6yde,pVcaEGI) \n begin \nboolean vkalqR0 <-1266\n end
#     """
#         expect = "func,f34EcjP,(,pr8awFc,,,plW6yde,,,pVcaEGI,),\n,begin,\n,boolean,vkalqR0,<-,1266,\n,end,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,196))
#         except:
#             print("fail testcase 96")
        
#     def test_case_97(self):
#         input = """func fZqIQfa(pHpoVVB,pHtEA1E,pEBXR5t) \n begin \nvVsy9Pd <--305\n end
#     """
#         expect = "func,fZqIQfa,(,pHpoVVB,,,pHtEA1E,,,pEBXR5t,),\n,begin,\n,vVsy9Pd,<-,-,305,\n,end,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,197))
#         except:
#             print("fail testcase 97")
        
#     def test_case_98(self):
#         input = """vuUubbN <--2292
#     """
#         expect = "vuUubbN,<-,-,2292,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,198))
#         except:
#             print("fail testcase 98")
        
#     def test_case_99(self):
#         input = """func fZLeUdZ(ptrxFis,pj5FrHz) \n begin \nfunc f00OuIX(pA5rlvz,p9NPDXK,pnUWwcQ) \n begin \nfunc fs1jLiX(pTsNij3,pmJ1zAf) \n begin \nfunc fDjZ5Vv(ppESuLq,pWRHLi6,pzj9Fj1) \n begin \nvSSETUv <--2462\n end\n end\n end\n end
#     """
#         expect = "func,fZLeUdZ,(,ptrxFis,,,pj5FrHz,),\n,begin,\n,func,f00OuIX,(,pA5rlvz,,,p9NPDXK,,,pnUWwcQ,),\n,begin,\n,func,fs1jLiX,(,pTsNij3,,,pmJ1zAf,),\n,begin,\n,func,fDjZ5Vv,(,ppESuLq,,,pWRHLi6,,,pzj9Fj1,),\n,begin,\n,vSSETUv,<-,-,2462,\n,end,\n,end,\n,end,\n,end,\n,<EOF>"
#         try:
#             self.assertTrue(TestLexer.test(input,expect,199))
#         except:
#             print("fail testcase 99")
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
        