from execute_tokens import Execute
from tokenizer import Tokenizer


class Oasis:
    def __init__(self, codes):
        self.codes = codes
        self.splitted_codes = []
        self.tokenizer = Tokenizer()
        self.executer = Execute()
        self.tokens = []

    def run(self):
        # split code
        for line in self.codes:
            self.splitted_codes.append(self.tokenizer.split_string(string=line))

        # tokenize code
        for line in self.splitted_codes:
            self.tokens.append(self.tokenizer.tokenize(string=line, tokens=self.tokens))

        # execute tokens
        self.executer.execute(tokens=self.tokens)


filename = "example_code.os"
with open(filename, "r") as file:
    codes = file.read().split("\n")
file.close()

# codes = "msg = \"hello again\"\nprint \"hello world\"\nprint msg"
oasis = Oasis(codes)
oasis.run()
