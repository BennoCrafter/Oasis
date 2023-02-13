import ast


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
                last_elements = code_snippet[1][-3:]
                if last_elements[-1] == "]":
                    info["var_name"] = code_snippet[1][:-3]
                    delete_index = last_elements.replace("[", "").replace("]", "")
                    info["index"] = int(delete_index)
                else:
                    info["var_name"] = code_snippet[1]
                    info["index"] = None
        elif keyword == "var":
            info["var_name"] = code_snippet[1]
            info["value"] = code_snippet[3]
        elif keyword == "list":
            info["list_name"] = code_snippet[1]
            joined_list = ''.join(code_snippet[3:])
            string_as_list = ast.literal_eval(joined_list)
            info["value"] = string_as_list
        elif keyword == "for":
            info["keyword"] = "for_loop"
            info["iteration_count"] = int(code_snippet[1])
            info["var_to_iterate"] = code_snippet[3]
            code = code_snippet[6:-1]
            code_part = []
            half_splitted_code = []
            interim_storage = ""
            for element in code:
                if element[-1] == ";":
                    code_part.append(interim_storage)
                    code_part.append(element[:-1])
                    half_splitted_code.append(code_part)
                    code_part = []
                    interim_storage = ""
                else:
                    interim_storage += element
            complete_parsed_splitted_code = []
            for command in half_splitted_code:
                complete_parsed_splitted_code.append(self.get_info(code_snippet=command))
            info["code_what_will_execute"] = complete_parsed_splitted_code
        return info


if __name__ == "__main__":
    tokenizer = Tokenizer()
    tokens = []
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
    splitted_code = []
    new_code = []
    for line in codes:
        splitted_code.append(tokenizer.split_string(line))
    print(splitted_code)

    for line in splitted_code:
        new_code.append(tokenizer.get_info(code_snippet=line))

    print(new_code)