

class Interpreter:
    def __init__(self):
        self.python_code = []
        self.vars = {}
        self.lists = {}
        self.print_outputs = []

    def interprete(self, code_snippet):
        keyword = code_snippet.get("keyword")
        if keyword == "write":
            self.print_outputs.append(code_snippet["value"].replace("\"", ""))
        elif keyword == "write_var":
            if code_snippet["var_name"] in self.vars.keys():
                var_value = self.vars.get(code_snippet["var_name"])
                if isinstance(var_value, str):
                    if code_snippet["index"] is None:
                        self.print_outputs.append(var_value)
                    else:
                        # why do i use here no -1? bcz of the "
                        var_value = var_value.replace("\"", "")
                        self.print_outputs.append(var_value[code_snippet["index"]-1])
                else:
                    self.print_outputs.append(var_value)
            else:
                if code_snippet["var_name"] in self.lists.keys():
                    list_value = self.lists.get(code_snippet["var_name"])
                    if code_snippet["index"] is None:
                        self.print_outputs.append(list_value)
                    else:
                        self.print_outputs.append(list_value[code_snippet["index"] - 1])
                else:
                    # do exeception
                    pass
        elif keyword == "var":
            var_value = code_snippet.get("value")
            index = code_snippet.get("index")
            if index is None:
                if "\"" == var_value[0]:
                    # is a string
                    self.vars[code_snippet.get("var_name")] = var_value
                elif var_value in self.vars.keys():
                    # is a var
                    self.vars[code_snippet.get("var_name")] = self.vars.get(var_value)
                elif var_value in self.lists.keys():
                    # is a list
                    self.lists[code_snippet.get("var_name")] = self.lists.get(var_value)
            else:
                if var_value in self.vars.keys():
                    # is a var
                    self.vars[code_snippet.get("var_name")] = self.vars.get(var_value).replace("\"", "")[index-1]
                elif var_value in self.lists.keys():
                    # is a list
                    self.vars[code_snippet.get("var_name")] = self.lists.get(var_value)[index-1]

        elif keyword == "list":
            if not isinstance(code_snippet["value"], list):
                self.lists[code_snippet.get("list_name")] = self.lists.get(code_snippet["value"])
            else:
                self.lists[code_snippet.get("list_name")] = code_snippet.get("value")

        elif keyword == "for_loop":
            self.vars[code_snippet["var_to_iterate"]] = 0
            for i in range(code_snippet["iteration_count"]):
                self.vars[code_snippet["var_to_iterate"]] += 1
                for deeper_code_snippet in code_snippet["code_what_will_execute"]:
                    self.deeper_interprete(deeper_code_snippet=deeper_code_snippet)
        elif keyword == "if_condition":
            result1 = self.whats_it(snippet=code_snippet.get("first_parameter"))
            result2 = self.whats_it(snippet=code_snippet.get("second_parameter"))
            correct = False
            if code_snippet["art"] == "comparing":
                if result1[1] == result2[1]:
                    correct = True
            if correct:
                for deeper_code_snippet in code_snippet["code_what_will_execute"]:
                    self.deeper_interprete(deeper_code_snippet=deeper_code_snippet)

    def deeper_interprete(self, deeper_code_snippet):
        self.interprete(code_snippet=deeper_code_snippet)

    def print_output(self):
        for element in self.print_outputs:
            print(element)

    def whats_it(self, snippet):
        if snippet[-1] == "]":
            indx = snippet.find("[")
            name = snippet[:indx]
            index = snippet[indx:].replace("[", "").replace("]", "")
        else:
            name = snippet
        if name in self.vars.keys():
            return "var", self.vars.get(name)[int(index)-1]
        elif name in self.lists.keys():
            return "list", self.lists.get(name)[int(index)-1]
        elif "\"" in name:
            return "string", snippet.replace("\"", "")
        else:
            return "unkown", snippet


if __name__ == "__main__":
    interpreter = Interpreter()
    code = [{"keyword": "write", "value": '"Test Output!"', "index": None},
            {"keyword": 'var', "var_name": 'test', 'value': '"That\'s a test value!"', "index": None},
            {"keyword": 'write_var', "var_name": "test", "index": None},
            {"keyword": "list", "list_name": "test_list",
             "value": ['first element', 'second element', 'thrid element'], "index": None},
            {"keyword": "write_var", "var_name": "test_list", "index": None},
            {"keyword": "if_condition", "first_parameter": "test_list[1]", "second_parameter": '"first element"', "art": "comparing",
             "code_what_will_execute": [{"keyword": 'write', "value": '"True!"'}]}]
    # Output should be:
    # Test Output!
    # That's a test value!
    # Hello World
    # 1
    # ...
    for code_snippet in code:
        interpreter.interprete(code_snippet=code_snippet)

    interpreter.print_output()
    print(interpreter.vars)
