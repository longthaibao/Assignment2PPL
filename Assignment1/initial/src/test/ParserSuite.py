import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """##aaaaaaaaaaaaaaa











func main()      begin
    number a
    var a <- 12
    var b <- "something you must check '" \\r \\n \\t \\f \\b \\''""
    dynamic cajfs____90928__
    string ___________
    number b[1, 2, 3, 0] <- [[1],[21324], [2123, 2, 1], [1, 2]]
    return 0
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))