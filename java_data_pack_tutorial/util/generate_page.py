import argparse
import os

parser = argparse.ArgumentParser(description="Generate HTML file for pages")
parser.add_argument("unit", metavar="unit_name", type=str, help="The unit name the page should link to")
parser.add_argument("lesson", metavar="lesson_name", type=str, help="The lesson name the page should link to")
parser.add_argument("--main", action="store_true", help="Flag to generate the home page. Unit and lesson are ignored if this is set.")
parser.add_argument("--title", metavar="title", type=str, help="The title of the page", default="Java Data Pack Tutorial")
parser.add_argument("--prev", metavar="previous_page", type=str, help="The link to the previous page (should follow format of '/java_data_pack_tutorial/pages/unit_name/lesson_name.html')", default=None)
parser.add_argument("--next", metavar="previous_page", type=str, help="The link to the previous page (should follow format of '/java_data_pack_tutorial/pages/unit_name/lesson_name.html')", default=None)

args = parser.parse_args()
unit_name = args.unit
lesson_name = args.lesson
previous_page = args.prev
next_page = args.next

output_path = os.path.join(os.getcwd(), f"java_data_pack_tutorial/pages/{unit_name}/{lesson_name}.html") if not args.main else os.path.join(os.getcwd(), f"java_data_pack_tutorial/index.html")
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, "w") as outfile:
    outfile.write(
f"""<!DOCTYPE html>
<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <link rel="stylesheet" type="text/css" href="/java_data_pack_tutorial/stylesheets/main.css">
        <link rel="stylesheet" type="text/css" href="/java_data_pack_tutorial/stylesheets/quizzes.css">
        <link rel="stylesheet" href="/java_data_pack_tutorial/stylesheets/atom_one_dark.css">
        <link rel="icon" href="/java_data_pack_tutorial/favicon.svg" sizes="any" type="image/svg+xml">

        <script src="//cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.0.1/build/highlight.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/showdown/1.9.0/showdown.min.js"></script>
        <script src="/java_data_pack_tutorial/scripts/mcfunction-highlight.js"></script>
        <script src="/java_data_pack_tutorial/scripts/main.js"></script>
        <script src="/java_data_pack_tutorial/scripts/quizzes.js"></script>
        <script src="/java_data_pack_tutorial/scripts/sidebar.js"></script>
        <script>clearStorage();</script>

        <title>
            {args.title}
        </title>
    </head>

    <body>
        <div id="sidebar"></div>
        <script>displaySidebar();</script>

        <!-- The main content -->
        <div class="content" id="content">
            <!-- Display the markdown file -->
            <div id="display_guide"></div>
            <script>displayMarkdownContent("{unit_name}", "{lesson_name}");</script>
            {f'<a href="{previous_page}" class="changePage"><< Previous</a>' if previous_page else ''}
            {f'<a href="{next_page}" class="changePage">Next >></a>' if next_page else ''}
        </div>

        <script>hljs.highlightAll();</script>
    </body>
</html>
""")
