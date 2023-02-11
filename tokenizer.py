class Tokenizer:
    def __init__(self):
        self.objects_to_split = [" ", "(", ")", ":", "\n", "\t"]
        self.output = []
        self.BUILT_IN_KEYWORDS = ["print", "var"]

    def split_string(self, string):
        self.output = []
        output_clipboard = ""
        qoutes = 0
        for element in string:
            if element == "\"":
                qoutes += 1
            if element in self.objects_to_split:
                if qoutes != 1:
                    self.output.append(output_clipboard)
                    if element != " ":
                        self.output.append(element)
                    output_clipboard = ""
                    qoutes = 0
                else:
                    output_clipboard += element
            else:
                output_clipboard += element

        self.output.append(output_clipboard)
        # delete free spaces
        self.output = [x for x in self.output if x or x == 0]
        return self.output

    def tokenize(self, string, tokens):
        if string[0] in self.BUILT_IN_KEYWORDS:
            keyword = string[0]
            if keyword == "var":
                return {"Error": False, "keyword": keyword, "var_name": string[1], "var_value": string[3], "important": False}
            elif keyword == "print":
                if "\"" in string[1]:
                    return {"Error": False, "keyword": keyword, "output_a_var": False, "output": string[1], "important": True}
                else:
                    all_variables = self.get_all_variables(tokens=tokens)
                    if string[1] in all_variables.keys():
                        return {"Error": False, "keyword": keyword, "output_a_var": True, "output": all_variables.get(string[1]), "important": True}
                    else:
                        return {"Error": True, "exception": "Unkown variable", "important": False}

        else:
            return {"Error": True, "exception": "Unkown"}

    def get_all_variables(self, tokens):
        variables = {}
        for line in tokens:
            if line.get("keyword") == "var":
                variables[line.get("var_name")] = line.get("var_value")
        return variables


if __name__ == "__main__":
    tokenizer = Tokenizer()
    tokens = []
    code = [['var', 'test', '=', '"Das ist ein Test value!"'], ['print', '"Hey! Noch mehr Zeug"'], "print", "test"]
    for line in code:
        tokens.append(tokenizer.tokenize(string=line, tokens=tokens))
    print(tokens)