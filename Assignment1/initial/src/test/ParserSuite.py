import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """func isPrime(number x)
func main()
begin
number x <- readNumber()
if (isPrime(x)) printString("Yes")
else 

begin
number r
number s
r <- 2.0
number a[5]
number b[5]
s <- r * r * 3.14
a[0] <- s
end
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
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))