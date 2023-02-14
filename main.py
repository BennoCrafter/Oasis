from tokenizer import Tokenizer
from interprete import Interpreter


class Oasis:
    def __init__(self, codes):
        self.codes = codes
        self.splitted_codes = []
        self.tokenizer = Tokenizer()
        self.interpreter = Interpreter()
        self.tokens = []
        self.parsed_codes = []

    def run(self):
        # split code
        for line in self.codes:
            self.splitted_codes.append(self.tokenizer.split_string(string=line))
        print(self.splitted_codes)
        # find keyword
        for line in self.splitted_codes:
            self.parsed_codes.append(self.tokenizer.get_info(code_snippet=line))
        print(self.parsed_codes)
        # run
        for code_snippet in self.parsed_codes:
            self.interpreter.interprete(code_snippet=code_snippet)

        self.interpreter.print_output()
        print(self.interpreter.vars)


filename = "example_code.os"
with open(filename, "r") as file:
    codes = file.read()
file.close()
delimeter = ";"
bracket_info = ""
clipboard = ""
splitted = []

for char in codes:
    if char == "(":
        bracket_info = "("
    elif char == ")":
        bracket_info = ")"
    if char == delimeter and bracket_info != "(":
        splitted.append(clipboard)
        clipboard = ""
    else:
        clipboard += char

codes = splitted
oasis = Oasis(codes)
oasis.run()
