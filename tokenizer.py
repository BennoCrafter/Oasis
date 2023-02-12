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


if __name__ == "__main__":
    tokenizer = Tokenizer()
    tokens = []
    with open("example_code.os", "r") as file:
        code = file.read().split(";")
    code.pop(-1)
    new_code = []
    for line in code:
        new_code.append(tokenizer.split_string(line))
    print(new_code)