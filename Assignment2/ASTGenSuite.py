import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    # Test simple VarDecl 
    def test_ast_0(self):
        input = input = """func inc(number a) return a + 1
func main() begin
var a <- 1
inc(a)
writeNumber(a)
end
"""
        expect = """Program([FuncDecl(Id(inc), [VarDecl(Id(a), NumberType, None, None)], Return(BinaryOp(+, Id(a), NumLit(1.0)))), FuncDecl(Id(main), [], Block([VarDecl(Id(a), None, var, NumLit(1.0)), CallStmt(Id(inc), [Id(a)]), CallStmt(Id(writeNumber), [Id(a)])]))])"""
        self.assertTrue(TestAST.test(input,expect,401))
    def test_ast_1(self):
        input = """number a
        """
        expect = """Program([VarDecl(Id(a), NumberType, None, None)])"""
        self.assertTrue(TestAST.test(input,expect,301))
    def test_ast_2(self):
        input = """string _zcode231
        """
        expect = """Program([VarDecl(Id(_zcode231), StringType, None, None)])"""
        self.assertTrue(TestAST.test(input,expect,302))
    def test_ast_3(self):
        input = """bool abc <- true
        """
        expect = """Program([VarDecl(Id(abc), BoolType, None, BooleanLit(True))])"""
        self.assertTrue(TestAST.test(input,expect,303))
    def test_ast_4(self):
        input = """var a <- 1
        """
        expect = """Program([VarDecl(Id(a), None, var, NumLit(1.0))])"""
        self.assertTrue(TestAST.test(input,expect,304))
    def test_ast_5(self):
        input = """dynamic a <- 1+213/2
        """
        expect = """Program([VarDecl(Id(a), None, dynamic, BinaryOp(+, NumLit(1.0), BinaryOp(/, NumLit(213.0), NumLit(2.0))))])"""
        self.assertTrue(TestAST.test(input,expect,305))
    def test_ast_6(self):
        input = """dynamic b
        """
        expect = """Program([VarDecl(Id(b), None, dynamic, None)])"""
        self.assertTrue(TestAST.test(input,expect,306))
    # Simple FuncDecl
    def test_ast_7(self):
        input = """func main() begin 
        end
        """
        expect = "Program([FuncDecl(Id(main), [], Block([]))])"
        self.assertTrue(TestAST.test(input,expect,307))
    def test_ast_8(self):
        input = """func main() return 1
        """
        expect = """Program([FuncDecl(Id(main), [], Return(NumLit(1.0)))])"""
        self.assertTrue(TestAST.test(input,expect,308))
    def test_ast_9(self):
        input = """func main()
        """
        expect = """Program([FuncDecl(Id(main), [], None)])"""
        self.assertTrue(TestAST.test(input,expect,309))
    def test_ast_10(self):
        input = """
        ## simple func
        func main() return [1,2,3]
        """
        expect = """Program([FuncDecl(Id(main), [], Return(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0))))])"""
        self.assertTrue(TestAST.test(input,expect,310))
        
    #COMPLEX FUNCDECL
    def test_ast_11(self):
        input = """
## this is pre-declaration func
func main()


## this is function definition
func main()     begin
    number a <- 1.2e-12
    number c <- (b + a) / c * a - d + goo()[1, 2, 3] * goo(a + b) * a[1, foo(), _c]
    foo()
    number k <- goo()[a + b, foo(), 1e-1]
    return a
end
"""
        expect = """Program([FuncDecl(Id(main), [], None), FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, NumLit(1.2e-12)), VarDecl(Id(c), NumberType, None, BinaryOp(+, BinaryOp(-, BinaryOp(*, BinaryOp(/, BinaryOp(+, Id(b), Id(a)), Id(c)), Id(a)), Id(d)), BinaryOp(*, BinaryOp(*, ArrayCell(CallExpr(Id(goo), []), [NumLit(1.0), NumLit(2.0), NumLit(3.0)]), CallExpr(Id(goo), [BinaryOp(+, Id(a), Id(b))])), ArrayCell(Id(a), [NumLit(1.0), CallExpr(Id(foo), []), Id(_c)])))), CallStmt(Id(foo), []), VarDecl(Id(k), NumberType, None, ArrayCell(CallExpr(Id(goo), []), [BinaryOp(+, Id(a), Id(b)), CallExpr(Id(foo), []), NumLit(0.1)])), Return(Id(a))]))])"""
        self.assertTrue(TestAST.test(input,expect,311))

    def test_ast_12(self):
        input = """
func test_looping(string a[1, 2], number __[0], bool cc_c)
begin
    if (a > b)
        for a until a + 1 by b + 1 if (a > b)
                if (a > b) number c
                elif (a > b) number c
                elif (a > b) number c
                else number c
            else
                break
    else
        for a until a > b by a * b / c
            for a until ssss[1, 2] by foo("hey", true, false, 1.e-3)
                if (a > b) number c
                else number c
end
"""
        expect = """Program([FuncDecl(Id(test_looping), [VarDecl(Id(a), ArrayType([1.0, 2.0], StringType), None, None), VarDecl(Id(__), ArrayType([0.0], NumberType), None, None), VarDecl(Id(cc_c), BoolType, None, None)], Block([If(BinaryOp(>, Id(a), Id(b)), For(Id(a), BinaryOp(+, Id(a), NumLit(1.0)), BinaryOp(+, Id(b), NumLit(1.0)), If(BinaryOp(>, Id(a), Id(b)), If(BinaryOp(>, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None)), [(BinaryOp(>, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None)), (BinaryOp(>, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None))], VarDecl(Id(c), NumberType, None, None)), [], Break)), [], For(Id(a), BinaryOp(>, Id(a), Id(b)), BinaryOp(/, BinaryOp(*, Id(a), Id(b)), Id(c)), For(Id(a), ArrayCell(Id(ssss), [NumLit(1.0), NumLit(2.0)]), CallExpr(Id(foo), [StringLit(hey), BooleanLit(True), BooleanLit(False), NumLit(0.001)]), If(BinaryOp(>, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None)), [], VarDecl(Id(c), NumberType, None, None)))]))])"""
        self.assertTrue(TestAST.test(input,expect,312))
    def test_ast_13(self):
        input = """func main(number a, number b) begin
number a[1, 2] <- [[2, 3]]
string b <- 1.e-12
bool c <- "abc"
return main(a, 3, d, b)
end
"""
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Block([VarDecl(Id(a), ArrayType([1.0, 2.0], NumberType), None, ArrayLit(ArrayLit(NumLit(2.0), NumLit(3.0)))), VarDecl(Id(b), StringType, None, NumLit(1e-12)), VarDecl(Id(c), BoolType, None, StringLit(abc)), Return(CallExpr(Id(main), [Id(a), NumLit(3.0), Id(d), Id(b)]))]))])"""
        self.assertTrue(TestAST.test(input,expect,313))
    def test_ast_14(self):
        input = """
        func test_exp()
begin
    bool a <- not not a and b or not not c or d or e and b < not not not c and d or e or not not e
    return a
end
        """
        expect = """Program([FuncDecl(Id(test_exp), [], Block([VarDecl(Id(a), BoolType, None, BinaryOp(<, BinaryOp(and, BinaryOp(or, BinaryOp(or, BinaryOp(or, BinaryOp(and, UnaryOp(not, UnaryOp(not, Id(a))), Id(b)), UnaryOp(not, UnaryOp(not, Id(c)))), Id(d)), Id(e)), Id(b)), BinaryOp(or, BinaryOp(or, BinaryOp(and, UnaryOp(not, UnaryOp(not, UnaryOp(not, Id(c)))), Id(d)), Id(e)), UnaryOp(not, UnaryOp(not, Id(e)))))), Return(Id(a))]))])"""
        self.assertTrue(TestAST.test(input,expect,314))
    def test_ast_15(self):
        input = """
func test_exp()
begin
    bool a <- a <= (b = ((k > (h == (b < c))) < (d > (e == f))))
    return a
end
"""
        expect = """Program([FuncDecl(Id(test_exp), [], Block([VarDecl(Id(a), BoolType, None, BinaryOp(<=, Id(a), BinaryOp(=, Id(b), BinaryOp(<, BinaryOp(>, Id(k), BinaryOp(==, Id(h), BinaryOp(<, Id(b), Id(c)))), BinaryOp(>, Id(d), BinaryOp(==, Id(e), Id(f))))))), Return(Id(a))]))])"""
        self.assertTrue(TestAST.test(input,expect,315))
    def test_ast_16(self):
        input = """
func test_exp()
begin
    number a <- a[1, [1, 2]]
end
"""
        expect = """Program([FuncDecl(Id(test_exp), [], Block([VarDecl(Id(a), NumberType, None, ArrayCell(Id(a), [NumLit(1.0), ArrayLit(NumLit(1.0), NumLit(2.0))]))]))])"""
        self.assertTrue(TestAST.test(input,expect,316))
    def test_ast_17(self):
        input = """
func test_exp()
begin
    number a <- [1, [1], [[1]], [[[1]]], [[[[1]]]]]
end
"""
        expect = """Program([FuncDecl(Id(test_exp), [], Block([VarDecl(Id(a), NumberType, None, ArrayLit(NumLit(1.0), ArrayLit(NumLit(1.0)), ArrayLit(ArrayLit(NumLit(1.0))), ArrayLit(ArrayLit(ArrayLit(NumLit(1.0)))), ArrayLit(ArrayLit(ArrayLit(ArrayLit(NumLit(1.0)))))))]))])"""
        self.assertTrue(TestAST.test(input,expect,317))
    def test_ast_18(self):
        input = """
        func main() begin 
        end
        func main() 
            begin 
                ## comment0
            end
        func main()
            ## comment1
            begin
                ## comment2
                
                ## comment3
                abcxyz <- 1 + 2 + fun()
                abcxyz[1+a] <- 1
                
                ## comment4
                abcxyz[3+4,2,4] <- 1
                
                ## comment5
            end
            ## comment
        """
        expect = """Program([FuncDecl(Id(main), [], Block([])), FuncDecl(Id(main), [], Block([])), FuncDecl(Id(main), [], Block([AssignStmt(Id(abcxyz), BinaryOp(+, BinaryOp(+, NumLit(1.0), NumLit(2.0)), CallExpr(Id(fun), []))), AssignStmt(ArrayCell(Id(abcxyz), [BinaryOp(+, NumLit(1.0), Id(a))]), NumLit(1.0)), AssignStmt(ArrayCell(Id(abcxyz), [BinaryOp(+, NumLit(3.0), NumLit(4.0)), NumLit(2.0), NumLit(4.0)]), NumLit(1.0))]))])"""
        self.assertTrue(TestAST.test(input,expect,318))
    def test_ast_19(self):
        input = """
        func main()
            begin   
                if(1+1) api <- 1
                ## comment0
                
                if(1+1) 
                    ## comment1
                    
                    api <- 1
                    ## comment2
                else api <- 1
                ## comment3
                
                if (1) api <- 1
                elif (1 ... 2)
                    ## comment1
                    
                    api <- 1
                    ## comment2
                elif (1) api <- 1
                
                if (1) api <- 1
                elif (1 ... 2) api <- 1
                elif (1) api <- 1
                else api <- 1   
            end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([If(BinaryOp(+, NumLit(1.0), NumLit(1.0)), AssignStmt(Id(api), NumLit(1.0))), [], None, If(BinaryOp(+, NumLit(1.0), NumLit(1.0)), AssignStmt(Id(api), NumLit(1.0))), [], AssignStmt(Id(api), NumLit(1.0)), If(NumLit(1.0), AssignStmt(Id(api), NumLit(1.0))), [(BinaryOp(..., NumLit(1.0), NumLit(2.0)), AssignStmt(Id(api), NumLit(1.0))), (NumLit(1.0), AssignStmt(Id(api), NumLit(1.0)))], None, If(NumLit(1.0), AssignStmt(Id(api), NumLit(1.0))), [(BinaryOp(..., NumLit(1.0), NumLit(2.0)), AssignStmt(Id(api), NumLit(1.0))), (NumLit(1.0), AssignStmt(Id(api), NumLit(1.0)))], AssignStmt(Id(api), NumLit(1.0))]))])"""
        self.assertTrue(TestAST.test(input,expect,319))
    def test_ast_20(self):
        input = """
        func main()
        begin 
            break
            continue
            for i until i >= 10 by 1 + 1 ... 3 / 2
                begin
                    break
                    continue
                end
                
            for i until i >= 10 by 1 print(1)
            for i until i >= 10 by 1 
                print(1)
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([Break, Continue, For(Id(i), BinaryOp(>=, Id(i), NumLit(10.0)), BinaryOp(..., BinaryOp(+, NumLit(1.0), NumLit(1.0)), BinaryOp(/, NumLit(3.0), NumLit(2.0))), Block([Break, Continue])), For(Id(i), BinaryOp(>=, Id(i), NumLit(10.0)), NumLit(1.0), CallStmt(Id(print), [NumLit(1.0)])), For(Id(i), BinaryOp(>=, Id(i), NumLit(10.0)), NumLit(1.0), CallStmt(Id(print), [NumLit(1.0)]))]))])"""
        self.assertTrue(TestAST.test(input,expect,320))
    def test_ast_21(self):
        input = """
        func main()
            begin
            main()
            end
        """    
        expect = """Program([FuncDecl(Id(main), [], Block([CallStmt(Id(main), [])]))])"""
        self.assertTrue(TestAST.test(input,expect,321))
    def test_ast_22(self):
        input = """
        func main()
        begin 
            return ([1,2,3]) + 1
            return main()
            main(1,2)
            fun()
            main([1,2,3], 1+2, a, c ... e)
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([Return(BinaryOp(+, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), NumLit(1.0))), Return(CallExpr(Id(main), [])), CallStmt(Id(main), [NumLit(1.0), NumLit(2.0)]), CallStmt(Id(fun), []), CallStmt(Id(main), [ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), BinaryOp(+, NumLit(1.0), NumLit(2.0)), Id(a), BinaryOp(..., Id(c), Id(e))])]))])"""
        self.assertTrue(TestAST.test(input,expect,322))
    def test_ast_23(self):
        input = """
        func areDivisors(number num1, number num2)
            return (num1 % num2 = 0 ... num2 % num1 = 0)
        func main()
            begin
                var num1 <- readNumber()
                var num2 <- readNumber()
                if (areDivisors(num1, num2)) printString("Yes")
                else printString("No")
            end
        """
        expect = """Program([FuncDecl(Id(areDivisors), [VarDecl(Id(num1), NumberType, None, None), VarDecl(Id(num2), NumberType, None, None)], Return(BinaryOp(..., BinaryOp(=, BinaryOp(%, Id(num1), Id(num2)), NumLit(0.0)), BinaryOp(=, BinaryOp(%, Id(num2), Id(num1)), NumLit(0.0))))), FuncDecl(Id(main), [], Block([VarDecl(Id(num1), None, var, CallExpr(Id(readNumber), [])), VarDecl(Id(num2), None, var, CallExpr(Id(readNumber), [])), If(CallExpr(Id(areDivisors), [Id(num1), Id(num2)]), CallStmt(Id(printString), [StringLit(Yes)])), [], CallStmt(Id(printString), [StringLit(No)])]))])"""
        self.assertTrue(TestAST.test(input,expect,323))
    def test_ast_24(self):
        input = """
            func isPrime(number x)
            func main()
                begin
                    number x <- readNumber()
                    if (isPrime(x)) printString("Yes")
                    else printString("No")
                end
            func isPrime(number x)
            begin
            if (x <= 1) return false
            var i <- 2
            for i until i > x / 2 by 1
            begin
            if (x % i = 0) return false
            end
            return true
            
            
            for i until i > x / 2 by 1 + 1 var c <- 1
            end
        """
        expect = """Program([FuncDecl(Id(isPrime), [VarDecl(Id(x), NumberType, None, None)], None), FuncDecl(Id(main), [], Block([VarDecl(Id(x), NumberType, None, CallExpr(Id(readNumber), [])), If(CallExpr(Id(isPrime), [Id(x)]), CallStmt(Id(printString), [StringLit(Yes)])), [], CallStmt(Id(printString), [StringLit(No)])])), FuncDecl(Id(isPrime), [VarDecl(Id(x), NumberType, None, None)], Block([If(BinaryOp(<=, Id(x), NumLit(1.0)), Return(BooleanLit(False))), [], None, VarDecl(Id(i), None, var, NumLit(2.0)), For(Id(i), BinaryOp(>, Id(i), BinaryOp(/, Id(x), NumLit(2.0))), NumLit(1.0), Block([If(BinaryOp(=, BinaryOp(%, Id(x), Id(i)), NumLit(0.0)), Return(BooleanLit(False))), [], None])), Return(BooleanLit(True)), For(Id(i), BinaryOp(>, Id(i), BinaryOp(/, Id(x), NumLit(2.0))), BinaryOp(+, NumLit(1.0), NumLit(1.0)), VarDecl(Id(c), None, var, NumLit(1.0)))]))])"""
        self.assertTrue(TestAST.test(input,expect,324))
    def test_ast_25(self):
        input = """dynamic a
var b<-2
func main()
	begin
if (b=2)
	a <- b
elif (b=3)
	a <- b*2 + 1
else a <- -1
return
end
        """
        expect = """Program([VarDecl(Id(a), None, dynamic, None), VarDecl(Id(b), None, var, NumLit(2.0)), FuncDecl(Id(main), [], Block([If(BinaryOp(=, Id(b), NumLit(2.0)), AssignStmt(Id(a), Id(b))), [(BinaryOp(=, Id(b), NumLit(3.0)), AssignStmt(Id(a), BinaryOp(+, BinaryOp(*, Id(b), NumLit(2.0)), NumLit(1.0))))], AssignStmt(Id(a), UnaryOp(-, NumLit(1.0))), Return()]))])"""
        self.assertTrue(TestAST.test(input,expect,325))
    def test_ast_26(self):
        input = """ func main()
begin
##this test case is to test if else
dynamic a <- readNumber()
if ((a>0) and (a<10))
	a<-a*2
else if ((a>10) and (a<20) )
a<-a*3
else a <- a*4
return
end
 
 """
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), None, dynamic, CallExpr(Id(readNumber), [])), If(BinaryOp(and, BinaryOp(>, Id(a), NumLit(0.0)), BinaryOp(<, Id(a), NumLit(10.0))), AssignStmt(Id(a), BinaryOp(*, Id(a), NumLit(2.0)))), [], If(BinaryOp(and, BinaryOp(>, Id(a), NumLit(10.0)), BinaryOp(<, Id(a), NumLit(20.0))), AssignStmt(Id(a), BinaryOp(*, Id(a), NumLit(3.0)))), [], AssignStmt(Id(a), BinaryOp(*, Id(a), NumLit(4.0))), Return()]))])"""
        self.assertTrue(TestAST.test(input,expect,326))
