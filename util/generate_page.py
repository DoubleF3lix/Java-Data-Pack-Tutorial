import argparse
import os

parser = argparse.ArgumentParser(description="Generate HTML file for pages")
parser.add_argument("unit", metavar="unit_name", type=str, help="The unit name the page should link to")
parser.add_argument("lesson", metavar="lesson_name", type=str, help="The lesson name the page should link to")
parser.add_argument("--main", action="store_true", help="Flag to generate the home page. Unit and lesson are ignored if this is set.")
parser.add_argument("--title", metavar="title", type=str, help="The title of the page", default="Java Data Pack Tutorial")
parser.add_argument("--prev", metavar="previous_page", type=str, help="The link to the previous page (should follow format of '/Java-Data-Pack-Tutorial/pages/unit_name/lesson_name.html')", default=None)
parser.add_argument("--next", metavar="previous_page", type=str, help="The link to the previous page (should follow format of '/Java-Data-Pack-Tutorial/pages/unit_name/lesson_name.html')", default=None)

args = parser.parse_args()
unit_name = args.unit
lesson_name = args.lesson
previous_page = args.prev
next_page = args.next

output_path = os.path.join(os.getcwd(), f"pages/{unit_name}/{lesson_name}.html") if not args.main else os.path.join(os.getcwd(), f"index.html")
md_output_path = os.path.join(os.getcwd(), f"guides/{unit_name}/{lesson_name}.md") if not args.main else None
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, "w") as outfile:
    outfile.write(
f"""<!DOCTYPE html>
<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="robots" content="index, nofollow">
        <meta charset="UTF-8">

        <!-- Primary Meta Tags -->
        <title>Java Data Pack Tutorial</title>
        <meta name="title" content="Java Data Pack Tutorial">
        <meta name="description" content="A complete online tutorial on creating Data Packs for Minecraft: Java Edition">

        <!-- Open Graph / Facebook -->
        <meta property="og:type" content="website">
        <meta property="og:url" content="https://doublef3lix.github.io/Java-Data-Pack-Tutorial">
        <meta property="og:title" content="Java Data Pack Tutorial">
        <meta property="og:description" content="A complete online tutorial on creating Data Packs for Minecraft: Java Edition">
        <meta property="og:image" content="/Java-Data-Pack-Tutorial/images/favicon.png">

        <!-- Twitter -->
        <meta property="twitter:card" content="/Java-Data-Pack-Tutorial/images/banner.png">
        <meta property="twitter:url" content="https://doublef3lix.github.io/Java-Data-Pack-Tutorial">
        <meta property="twitter:title" content="Java Data Pack Tutorial">
        <meta property="twitter:description" content="A complete online tutorial on creating Data Packs for Minecraft: Java Edition">
        <meta property="twitter:image" content="/Java-Data-Pack-Tutorial/images/favicon.png">

        <link rel="stylesheet" type="text/css" href="/Java-Data-Pack-Tutorial/stylesheets/main.css">
        <link rel="stylesheet" type="text/css" href="/Java-Data-Pack-Tutorial/stylesheets/quizzes.css">
        <link rel="stylesheet" href="/Java-Data-Pack-Tutorial/stylesheets/atom_one_dark.css">
        <link rel="icon" href="/Java-Data-Pack-Tutorial/favicon.svg" sizes="any" type="image/svg+xml">

        <script src="//cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.0.1/build/highlight.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/showdown/1.9.0/showdown.min.js"></script>
        <script src="/Java-Data-Pack-Tutorial/scripts/mcfunction-highlight.js"></script>
        <script src="/Java-Data-Pack-Tutorial/scripts/main.js"></script>
        <script src="/Java-Data-Pack-Tutorial/scripts/quizzes.js"></script>
        <script src="/Java-Data-Pack-Tutorial/scripts/sidebar.js"></script>
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

if md_output_path and not os.path.exists(md_output_path):
    with open(md_output_path, "w") as _: ...
