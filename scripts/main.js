function clearStorage() {
    sessionStorage.clear();
    sessionStorage.setItem("questions", "{}");
}

async function getFileContent(url) {
    const response = await fetch(url);
    if (response.ok) {
        return response.text()
    } else {
        throw ReferenceError;
    }
}

async function displayMarkdownContent(unit_name, lesson_name) {
    showdown.extension('highlightjs', function () {
        return [{
            type: "output",
            filter: function (text, converter, options) {
                var left = "<pre><code\\b[^>]*>",
                    right = "</code></pre>",
                    flags = "g";
                var replacement = function (wholeMatch, match, left, right) {
                    var lang = (left.match(/class=\"([^ \"]+)/) || [])[1];
                    left = left.slice(0, 18) + 'hljs ' + left.slice(18);
                    if (lang && hljs.getLanguage(lang)) {
                        return left + hljs.highlight(lang, match).value + right;
                    } else {
                        return left + hljs.highlightAuto(match).value + right;
                    }
                };
                return showdown.helper.replaceRecursiveRegExp(text, replacement, left, right, flags);
            }
        }];
    });
    let markdownOutput;
    try {
        let markdownText = await getFileContent(`/java_data_pack_tutorial/guides/${unit_name}/${lesson_name}.md`);
        markdownOutput = new showdown.Converter({extensions: ["highlightjs"], tasklists: true, simpleLineBreaks: true, backslashEscapesHTMLTags: true}).makeHtml(markdownText);
    } catch (e) {
        markdownOutput = `<h1>Uh-oh! This content could not be loaded</h1><p>Have this cat picture instead</p><img src="https://images.pexels.com/photos/416160/pexels-photo-416160.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=375&w=630" alt="A very cute cat">`;
    }
    document.getElementById(`display_guide`).innerHTML = markdownOutput;
}