# Contributing
A quick-start guide (hopefully) to help you contribute. 
If you have any questions, please notify me via discord or use an issue on the GitHub repository.
Please read this entire page to get a good grasp on the standards and processes used to contribute.

---
## Terminology
First, some basic terminology. 
- Project - The java data pack tutorial as a whole
- Guide(s) or Page(s) - individual pages that make up the project
- Reviewer - Someone who makes sure that a submitted guide matches the standards
- Impersonal - Not acknowledging the reader or the writer (or any of the contributors)
- Segment - A part of a guide

---
## How To
Every guide must be submitted in markdown (`.md` files). This is the same format used to write GitHub README's. If you've never used this, you can learn about it [here](https://guides.github.com/features/mastering-markdown/). To start contributing, first make a clone of the repository which is located [here](https://github.com/DoubleF3lix/Java-Data-Pack-Tutorial). Use GitHub Desktop or Git (GitHub Desktop is much more user-friendly) and clone it, then you can start editing. 

Every guide should follow information relative to the latest release.

Every pull request you submit should not only include the markdown file as well as any extra files, but also an HTML file to link your guide to the site. A template for this guide can be found [here](https://gist.github.com/DoubleF3lix/dcdca32a1b11c18e0154e854e05a664a). The main sections of interest are line 33 and 35. You'll need to edit the first function parameter of line 33 to be the unit name, and the second parameter should be the lesson name. Do not include the file extension. Line 35 should be edited to point to the next lesson (or previous, where applicable). You can find this in the lesson plan located in `repo_folder/java_data_pack_tutorial/util/sidebar.json`. Quizzes can be added by using `<script>displayQuizbox("unitname", "lessonname");</script>` in the same way you use `displayMarkdownContent();` on line 33. This is not included in the example as you should add the quiz in the markdown file just before the "Citation" section. If the guide does not have this section, the quiz HTML can be added at the end of the markdown file.

If line breaks don't appear how you want them, use a combination of `<br>` and newlines until it looks the way you want. Custom HTML may be added within reason. Excessive use of extra HTML in guides will be rejected.

Images should go in `repo_folder/java_data_pack_tutorial/images/my_image.png`. The file name should be concise but an accurate description of the image.<br>
Quizzes go in `repo_folder/java_data_pack_tutorial/quizzes/unitname/lessonname.json`.<br> 
Guide files go in `repo_folder/java_data_pack_tutorial/guides/unitname/lessonname.md`.

Basic markdown and other formatting is discussed in the "Grammar, Spelling, and Formatting" section below.

Quizzes can be created following this template:
```jsonc
{
    // This defines how many questions from the question pool will be presented in a random order
    "questionCount": 3,
    // Define the question pool
    // Any other comments are stored in the JSON itself
    "questions": [
        {
            "type": "multiple_choice",
            "prompt": "What are the choices to this question?",
            "choices": [
                "This one",
                "That one",
                "The one above",
                "The one below"
            ],
            "answer": "this one"
        },
        {
            "type": "boolean",
            "prompt": "Boolean is just multiple choice but with answers added for you",
            "answer": "false"
        },
        {
            "type": "text",
            "prompt": "This took me too long to make :(",
            "answer": [
                "When using more than one text box, use a list to specify answers. This is the answer to box 1",
                "Answer to box 2"
            ],
            "box": "If we set the box value to a custom string, like so. We can add boxes in between text with custom length using ${}. Again, by default it is 30, but if we use ${10} then we get a custom width of 10. This prompt displays a text box with a width of 30 and another one with a width of 10."
        },
        {
            "type": "text",
            "prompt": "Text answers can be simple too",
            "answer": "If you don't want to use special formatting, you can set the custom answer box width to a number. This one has a width of 10.",
            "box": 10
        }
    ]
}
```

---
## How to Submit and Review
To submit your guide(s) for review, make sure any necessary files are in your local copy of the repository. Then, create a pull request. Other contributors and reviewers will make sure your guide meets all the following criteria:
- Accurate information
- Proper spelling and grammar
- Proper citations
- Correct formatting
- Meets the standards specified below
- Has the proper HTML, Markdown, Quiz, etc. files

When reviewing a guide, download the pull request contents into a copy of your local repository and launch an HTTP server to fully test out all changes. This is to ensure things that look right at first glance work properly (such as quizzes, hyperlinks, formatting, and images).

Any guide that plainly shows a lack of effort will be rejected.

---
## Standards
### Personal vs. Impersonal
While this guide should serve as a reference to experienced users and also a tutorial for beginners instead of just a reference (or wiki), it should still be kept as "impersonal" as possible. If this is confusing, here's a quick example the differences between a personal and impersonal segment using this paragraph. (The impersonal bit is this paragraph you're reading now, the impersonal segment is below)

> While I hope to make this guide be able to serve as a reference to experienced users and also a tutorial for beginners instead of just a reference (or wiki), I still want to keep it as "impersonal" as possible. If you find this confusing, I've made a quick example a quick example of the differences between a personal and impersonal segment using this paragraph I wrote earlier.

See the difference? If this is still confusing, just know that all text written in this part of the contribution guide is written in an impersonal format and guides should be written to try to replicate this as close as possible. If submitted guides aren't written perfectly, that's okay. Edits can be made later, and they're called first drafts for a reason. **However, just because there is a review process where changes will likely be made does not mean half-baked articles should be submitted for someone else to clean up.** 

Do note that personal talk can't always be avoided, and sometimes it just helps the article flow better. For instance, it's better to write "You should avoid using `execute as @a run`" instead of "It is advised that `execute as @a run` is not used". The impersonal part sounds extremely dry, while using the word "you" helps the flow of the sentence tremendously. A general rule of thumb is **it's okay to sometimes mention the reader, but you should always avoid mentioning the writer (I, we, etc.)**. 
<br><br>

### Citations
Any fact or statement is **not** publicly available knowleddge should be sourced at the bottom of the page. This does not apply to publicly available knowledge, such as command syntax, information derived from the game code, information stated in a help chat on MCC, etc. Things that should be cited are unique techniques that someone came up with (such as a technique for removing the numbers on the sidebar from a scoreboard), quotes from developers, etc. Note that all citations should be evaluated on a case-by-case basis.
<br>

Here's a small list of examples and how they should be cited:
<table>
    <tr>
        <th>Scenario</th>
        <th>Citation needed</th>
    </tr>
    <tr>
        <td>A user in a help chat explains how data storage can be used for RNG</td>
        <td>No</td>
    </tr>
    <tr>
        <td>Felix tweets that shaders might get more capability in the future, but it's not decided yet</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>A user publishes a video guide on how you can create a custom chat feature. You reference this video in a page and explain it in more laymans terms to the reader.</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>boq says in discord that the `item` command might get more capability in the future</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>An explanation for how overflows with the `effect` command work. This information was given to you by someone on discord.</td>
        <td>No</td>
    </tr>
    <tr>
        <td>A user on discord provides a detailed explanation for how you can get around a bug</td>
        <td>Depends</td>
    </tr>
</table>

Any citations that use a discord message should have a link to the message as well as an invite to the server in this format:
`[citation number] - [message link] (invite: [invite link]) - [message author (not nickname)], retrieved [date in format of Month D, Yr]`.<br>
Any other citation should have a direct link to the source in this format:
`[citation number] - [direct link] - [author(s)], retrieved [date in format of Month D, Yr]`.

The citation section of a guide should be separated using the line like this:
```
---
Citations:
1 - Insert Citation Here
2 - Insert Citation Here
```
Citations should be referenced with a superscript number, with a jump link to the citations section at the bottom.
<br><br>

### Grammar, Spelling, and Formatting
All guides should be written in standard american english with proper grammar and spelling. 
You can use any text editor, but Visual Studio Code has a markdown preview plugin as well as a spellchecker plugin which you can download [here](https://marketplace.visualstudio.com/items?itemName=docsmsft.docs-markdown) and [here](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker).

Every guide should begin with this:
```
# Article Name
<hr>

Contents (note the newline)
```

Tables are done with standard HTML. See [this](https://www.w3schools.com/html/html_tables.asp) page on how you can create those.<br>

Quotes can be done be preceding the line with `>`, like so:<br>
`> Hello, World!`.

Code blocks are done like so (the language can be replaced with things like `json`, a full list can be found [here](https://github.com/highlightjs/highlight.js/blob/master/SUPPORTED_LANGUAGES.md), just note that `mcfunction` is not supported):<br>
\`\`\`lang<br>
print("Hello, World!")<br>
\`\`\`

Plaintext code blocks break with `highlight.js`, so they must be done like this:
```html
<pre><p class="codeBlock">
This is a plaintext code block
    It works with indentation too
    Remember the closing brackets!
</p></pre>
```
`Inline code blocks` are done \`like this\`.<br>
It's "data pack" not "datapack".

Here's a summary of the standards:
- **Do not** submit half baked articles hoping/assuming someone else will fix it for you
- **Do** attempt to write your guides to the best of your ability
- **Do** credit any external resources where necessary
- **Do** use proper grammar and spelling
- **Do** use standard american english
- **Do not** use "datapack" over "data pack". "datapack" should only be used when referring to folder names or the `/datapack` command.
