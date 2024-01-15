import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """func isPrime(number x)
func main()
begin
number x <- readNumber()
if isPrime(x) printString("Yes")
else printString("No")
end
func isPrime(number x)
begin
if x <= 1 return false
var i <- 2
for i until i > x / 2 by 1
begin
if x-i = 0 return false
end
return true
end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))