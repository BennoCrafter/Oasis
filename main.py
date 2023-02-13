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
        # run
        for code_snippet in self.parsed_codes:
            self.interpreter.interprete(code_snippet=code_snippet)

        self.interpreter.print_output()


filename = "example_code.os"
with open(filename, "r") as file:
    codes = file.read().split(";")
file.close()
codes.pop(-1)

oasis = Oasis(codes)
oasis.run()
