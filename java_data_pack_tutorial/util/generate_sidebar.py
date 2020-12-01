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
            html_output.append(f'<a href="/java_data_pack_tutorial/index.html">{unit_name}</a>')
            has_index_page = True
        else:
            raise SyntaxError("More than one main page specified")

    elif unit_data.get("single") == True:
        html_output.append(f'<a href="/java_data_pack_tutorial/pages/{snakify(unit)}.html">{unit_name}</a>')

    else:
        html_output.append(
            f'''
<button class="dropdownButton" onclick="toggleDropdown(this);">Unit {unit_number}: {unit_name}
<i class="dropdownCaret fa fa-caret-right"></i>
</button>
<div class="dropdownContainer">
            '''
        )

        for lesson in unit_data:
            lesson_data = unit_data[lesson]
            lesson_name = lesson
            lesson_index = list(unit_data.keys()).index(lesson)
            lesson_number = lesson_index + 1

            if not bool(lesson_data):
                html_output.append(
                    f'''
        <a href="/java_data_pack_tutorial/pages/unit{unit_number}/lesson{lesson_number}.html"><li>Lesson {lesson_number}: {lesson_name}</li></a>
                    '''
                )
            else:
                html_output.append(
                    f'''
<button class="dropdownButton" onclick="toggleDropdown(this);"><li>Lesson {lesson_number}: {lesson_name}</li>
<i class="dropdownCaret subDropdown fa fa-caret-right"></i>
</button>
<div class="dropdownContainer">
                    '''
                )
                for part in lesson_data["parts"]:
                    part_data = lesson_data["parts"][part]
                    part_name = part
                    part_index = list(lesson_data["parts"].keys()).index(part)
                    part_number = part_index + 1

                    html_output.append(
                        f'''
<a href="/java_data_pack_tutorial/pages/unit{unit_number}/lesson{lesson_number}/part{part_number}.html"><li>{part_name}</li></a>
                        '''
                    )

                html_output.append("</div>")
        # Close out unit DIV tag
        html_output.append("</div>")
# Close out sidebar DIV tag
html_output.append("</div>")

with open("java_data_pack_tutorial\\pages\\sidebar.html", "a") as sidebar_html:
    q = []
    for element in html_output:
        q.append(element.strip())
    sidebar_html.write("\n".join(q))