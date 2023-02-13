class Tokenizer:
    def __init__(self):
        self.objects_to_split = [" ", "(", ")", ":", "\n", "\t"]
        self.objects_to_delete = [" ", "\n"]
        self.output = []
        self.BUILT_IN_KEYWORDS = ["print", "var", "for"]

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
                    if element not in self.objects_to_delete:
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

    def get_info(self, code_snippet):
        info = {}
        keyword = code_snippet[0]
        info["keyword"] = keyword
        if keyword == "write":
            if code_snippet[1][0] == "\"" and code_snippet[1][-1] == "\"" or code_snippet[1][0] == "\'" and code_snippet[1][-1] == "\'":
                info["value"] = code_snippet[1]
            else:
                info["keyword"] = "write_var"
                info["var_name"] = code_snippet[1]
        elif keyword == "var":
            info["var_name"] = code_snippet[1]
            info["value"] = code_snippet[3]
        elif keyword == "for":
            info["iteration_count"] = int(code_snippet[1])
            info["var_to_iterate"] = code_snippet[3]
        return info


if __name__ == "__main__":
    tokenizer = Tokenizer()
    tokens = []
    with open("example_code.os", "r") as file:
        code = file.read().split(";")
    code.pop(-1)
    splitted_code = []
    new_code = []
    for line in code:
        splitted_code.append(tokenizer.split_string(line))
    print(splitted_code)

    for line in splitted_code:
        new_code.append(tokenizer.get_info(code_snippet=line))

    print(new_code)