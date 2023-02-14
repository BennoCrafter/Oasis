import json


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
                    self.print_outputs.append(var_value.replace("\"", ""))
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
            if "\"" == var_value[0]:
                # is a string
                self.vars[code_snippet.get("var_name")] = var_value
            elif var_value in self.vars.keys():
                # is a var
                self.vars[code_snippet.get("var_name")] = self.vars.get(var_value)
            elif var_value in self.lists.keys():
                # is a list
                self.lists[code_snippet.get("var_name")] = self.lists.get(var_value)

        elif keyword == "list":
            self.lists[code_snippet.get("list_name")] = code_snippet.get("value")
        elif keyword == "for_loop":
            self.vars[code_snippet["var_to_iterate"]] = 0
            for i in range(code_snippet["iteration_count"]):
                self.vars[code_snippet["var_to_iterate"]] += 1
                for deeper_code_snippet in code_snippet["code_what_will_execute"]:
                    self.deeper_interprete(deeper_code_snippet=deeper_code_snippet)
        elif keyword == "if_condition":
            pass
            #todo

    def deeper_interprete(self, deeper_code_snippet):
        self.interprete(code_snippet=deeper_code_snippet)

    def print_output(self):
        for element in self.print_outputs:
            print(element)

    def whats_it(self, snippet):
        if snippet in self.vars.values():
            return "var"
        elif snippet in self.lists.values():
            return "list"
        elif "\"" in snippet:
            return "string"


if __name__ == "__main__":
    interpreter = Interpreter()
    code = [{"keyword": "write", "value": '"Test Output!"'},
            {"keyword": 'var', "var_name": 'test', 'value': '"That\'s a test value!"'},
            {"keyword": 'write_var', "var_name": "test"},
            {"keyword": 'for_loop', "iteration_count": 2, "var_to_iterate": 'num',
             "code_what_will_execute": [{"keyword": 'write', "value": '"Hello World!"'},
                                        {"keyword": "write_var", "var_name": "num"}]},
            {"keyword": "list", "list_name": "test_list", "value": ['first element', 'second element', 'thrid element']},
            {"keyword": "write_var", "var_name": "test_list", "index": None},
            {"keyword": "if_condition", "first parameter": "test_list[1]", "second_parameter": '"first element"', "code_what_will_execute": [{"keyword": 'write', "value": '"True!"'}]},
            {"keyword": "var", "var_name": "alsotest", "value": "test"},
            {"keyword": "write_var", "var_name": "alsotest"}]
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