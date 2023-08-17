'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-08-16
Purpose: Create the set_pipeline_input() method in all services
-----------------------------------------------------
'''
import os


def create_parameter_definition(param_string:str):
    params = param_string.split(",")
    new_params = []
    for param in params:
        if param == "user:str":
            new_params.append("ref_name:str")
            new_params.append(param)
            continue

        if ":" in param:
            if "=" in param:
                param_name, hint_and_default = param.split(":")
                type_hint, default = hint_and_default.split("=")
                new_params.append(f"{param_name}:Union[{type_hint}, Dict]={default}")
            else:
                param_name, type_hint = param.split(":")
                new_params.append(f"{param_name}:Union[{type_hint}, Dict]")
        else:
            new_params.append(param)

    return new_params


def define_set_pipeline_input(new_params):
    parameter_definition = (", ".join(new_params))
    lines = []
    lines.extend(["\n", "\n"])
    function_definition = f"    def set_pipeline_input({parameter_definition}) -> None:\n"
    lines.append(function_definition)

    # get param names only:
    param_names = [p.split(":")[0] for p in new_params if p != "self"]
    inspect_args_params = "self.set_pipeline_input, " + ", ".join(param_names)
    source_config_line = f"        self.source_config = inspect_arguments({inspect_args_params})"
    lines.append(f"{source_config_line}\n")
    lines.append("        return super().set_pipeline_input()\n")

    return lines


def create_set_pipeline_input(file_path):
    # things to do:
    imported_typings = False
    created_new_params = False
    triple_quote_count = 0

    new_lines = []
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        for i, line in enumerate(lines):
            line: str
            # import typings
            if not imported_typings:
                if triple_quote_count < 2:
                    new_lines.append(line)
                    if "'''" in line:
                        triple_quote_count += 1
                if triple_quote_count == 2:
                    new_lines.append("from typing import Union, Dict\n")
                    imported_typings = True
                    continue
                continue

            # find call method and extract (param_name, type, default value) 
            else:
                new_lines.append(line)
                if not created_new_params:
                    if "def __call__" in line:
                        if ")" not in line:
                            print(f"Multiline: {file_path}")
                            line = line + lines[i+1]
                            line = line.replace("\n", "")
                        param_string = line.split("(")[1].split(")")[0].replace(" ", "")
                        new_params = create_parameter_definition(param_string)
                        set_pipeline_input_definition = define_set_pipeline_input(new_params)
                        created_new_params = True
            
        new_lines.extend(set_pipeline_input_definition)
        new_lines.append("")
    
    return new_lines


if __name__ == "__main__":
    directory = "../soffosai/core/services_bak/"
    files = os.listdir(directory)
    py_files = [f for f in files if f.endswith(".py") and f != "service.py" and f != "__init__.py"]

    for file_name in py_files:
        print(file_name)
        file_path = os.path.join(directory, file_name)
        new_code = create_set_pipeline_input(file_path)
        with open(f"services_with_set_pipeline_input/{file_name}", "w", encoding="utf-8") as file:
            file.write("".join(new_code))
