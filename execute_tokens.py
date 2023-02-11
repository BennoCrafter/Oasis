class Execute:
    def __init__(self):
        pass

    def execute(self, tokens):
        for line in tokens:
            if not line.get("Error") and line.get("important"):
                execution_command = line.get("keyword")
                if execution_command == "print":
                    print(line.get("output").replace("\"", ""))


if __name__ == "__main__":
    execute_object = Execute()
    tokens = [{'Error': False, 'keyword': 'var', 'var_name': 'test', 'var_value': '"Das ist ein Test value!"', "important": False}, {'Error': False, 'keyword': 'print', 'output_a_var': False, 'output': '"Hey! Noch mehr Zeug"', "important": True}, {'Error': False, 'keyword': 'print', 'output_a_var': True, 'output': '"Das ist ein Test value!"', "important": True}]
    execute_object.execute(tokens=tokens)
