import json


class Interpreter:
    def __init__(self, filename):
        self.filename = filename

    def interprete(self, code_snippet):

        return code_snippet

    def read_tokens_database(self):
        with open(self.filename, "r") as file:
            self.data_token = json.load(file)
        print(self.data_token)


if __name__ == "__main__":
    interpreter = Interpreter(filename="tokens.json")
    interpreter.read_tokens_database()
    code = [['print', '"Hello World!"'], ['var', 'test', '=', '"That\'s a test value!"'], ['print', 'test'], ['for', '10', 'with', 'num', ':', '(', 'print', 'num', ')']]
    for code_snippet in code:
        print(interpreter.interprete(code_snippet=code_snippet))