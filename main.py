from tokenizer import Tokenizer


class Oasis:
    def __init__(self, codes):
        self.codes = codes
        self.splitted_codes = []
        self.tokenizer = Tokenizer()
        self.tokens = []

    def run(self):
        # split code
        for line in self.codes:
            self.splitted_codes.append(self.tokenizer.split_string(string=line))
        print(self.splitted_codes)


filename = "example_code.os"
with open(filename, "r") as file:
    codes = file.read().split(";")
file.close()

oasis = Oasis(codes)
oasis.run()
