import json
import re

def snakify(text):
    output = []
    split_text = text.split(" ")
    for part in split_text:
        part = re.sub(r'[^A-Za-z_]', '', part)
        output.append(part.lower())
    return "_".join(output)

with open("java_data_pack_tutorial\\pages\\sidebar.html", "w") as sidebar_html:
    sidebar_html.write("")

html_output = []
toc_output = []

html_output.append(
'''
<div class="sidebar">
<!-- fa-caret-down|right symbol and showdownjs -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<link rel="stylesheet" href="/java_data_pack_tutorial/stylesheets/sidebar.css">
''')

with open("java_data_pack_tutorial\\util\\sidebar.json", "r") as sidebar_json:
    sidebar_json = json.loads(sidebar_json.read())

units = sidebar_json["units"]

has_index_page = False

for unit in units:
    unit_data = units[unit]
    unit_name = unit
    unit_index = list(units.keys()).index(unit)
    unit_number = unit_index

    if unit_data.get("is_main") == True:
        if has_index_page is False:
            html_output.append(f'<a class="single" href="/java_data_pack_tutorial/index.html">{unit_name}</a>')
            has_index_page = True
        else:
            raise SyntaxError("More than one main page specified")

    elif unit_data.get("single") == True:
        html_output.append(f'<a class="single" href="/java_data_pack_tutorial/pages/{snakify(unit)}.html">{unit_name}</a>')

    else:
        toc_output.append(f"- Unit {unit_number}: {unit_name}")

        html_output.append(
            f'''
<button class="dropdownButton" onclick="toggleDropdown(this);">Unit {unit_number}: {unit_name}
<i class="dropdownCaret fa fa-caret-right"></i>
</button>
<div class="dropdownContainer">
            '''
        )

        project_count = 1
        lesson_number = 0
        for lesson in unit_data:
            lesson_data = unit_data[lesson]
            lesson_name = lesson
            lesson_index = list(unit_data.keys()).index(lesson)
            lesson_number += 1

            if lesson_name != "_comment":
                if lesson_data.get("project") == True:
                    toc_output.append(f"\t- Project {project_count}: [{lesson_name}](/java_data_pack_tutorial/pages/{snakify(unit_name)}/{snakify(lesson_name)}.html)".expandtabs(4))

                    html_output.append(
                        f'''
<a class="lesson" href="/java_data_pack_tutorial/pages/{snakify(unit_name)}/{snakify(lesson_name)}.html"><li>Project {project_count}: {lesson_name}</li></a>
                        '''
                    )
                    
                    project_count += 1
                    lesson_number -= 1

                elif "parts" not in lesson_data:
                    toc_output.append(f"\t- Lesson {lesson_number}: [{lesson_name}](/java_data_pack_tutorial/pages/{snakify(unit_name)}/{snakify(lesson_name)}.html)".expandtabs(4))

                    html_output.append(
                        f'''
<a class="lesson" href="/java_data_pack_tutorial/pages/{snakify(unit_name)}/{snakify(lesson_name)}.html"><li>Lesson {lesson_number}: {lesson_name}</li></a>
                        '''
                    )
                else:
                    if "parts" in lesson_data:
                        if lesson_number > 1:
                            if "parts" not in list(unit_data.values())[lesson_index - 1]:
                                html_output.append("<div class=\"horizontalLine\"></div>")

                        toc_output.append(f"\t- Lesson {lesson_number}: {lesson_name}".expandtabs(4))

                        for part in lesson_data["parts"]:
                            part_data = lesson_data["parts"][part]
                            part_name = part
                            part_index = list(lesson_data["parts"].keys()).index(part)
                            part_number = part_index + 1

                            toc_output.append(f"\t\t- Lesson {lesson_number}.{part_number}: [{part_name}](/java_data_pack_tutorial/pages/{snakify(unit_name)}/{snakify(lesson_name)}/{snakify(part_name)}.html)".expandtabs(4))

                            if part_name != "_comment":
                                html_output.append(
                                    f'''
<a class="lesson" href="/java_data_pack_tutorial/pages/{snakify(unit_name)}/{snakify(lesson_name)}/{snakify(part_name)}.html"><li>Lesson {lesson_number}.{part_number}: {part_name}</li></a>
                                    '''
                                )

                    if 0 <= lesson_index + 1 < len(unit_data):
                        html_output.append("<div class=\"horizontalLine\"></div>")

        # Close out unit DIV tag
        html_output.append("</div>")
# Close out sidebar DIV tag
html_output.append("</div>")

with open("java_data_pack_tutorial\\pages\\sidebar.html", "w") as sidebar_html:
    q = []
    for element in html_output:
        q.append(element.strip())
    sidebar_html.write("\n".join(q))


with open("java_data_pack_tutorial\\guides\\home\\welcome.md", "w") as welcome_md:
    q = []
    q.append(
"""# Home
<hr>

Welcome to the **Java Data Pack Tutorial** (JDPT)! This should help to serve as a guide for newcomers, but it may also serve as a reference for experienced users. This tutorial is not a replacement of the [Official Minecraft Wiki](https://minecraft.gamepedia.com/Minecraft_Wiki), and should not be treated as such. 
This tutorial will cover all of the following:
- Minecraft Commands
- Data Packs & Functions
- Advancements
- Predicates
- Loot Tables
- Tags
- Item Modifiers
- Recipes
- Structures
- World Generation Configuration
- Custom Dimensions

As this tutorial is intended for newcomers, it should be followed in order, starting with Unit 1, Lesson 1. Completing the projects and quizzes are optional, but they will help you learn to apply the concepts you've learned into data packs.
<hr>

## Table of Contents
""")

    q.append("\n".join(toc_output))
    welcome_md.write("\n".join(q))
