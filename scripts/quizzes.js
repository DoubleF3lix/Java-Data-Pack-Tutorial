function shuffleList(list) {
    // Make a copy of the list so the original isn't modified
    let listCopy = list.slice();

    // Taken from https://stackoverflow.com/a/12646864
    for (let i = listCopy.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [listCopy[i], listCopy[j]] = [listCopy[j], listCopy[i]];
    }
    return listCopy;
}

function getRandomElements(list, count) {
    // Make a copy of the list so the original isn't modified
    let listCopy = list.slice();
    listCopy = shuffleList(listCopy);

    // If the count is equal or higher than the length of the list, return the shuffled list
    if (count >= listCopy.length) {
        return listCopy;
    // Otherwise, shuffle the list and return the first <count> elements
    } else {
        return listCopy.slice(0, count)
    }
}

function buildQuiz(questions) {
    let HTMLOutput = [];
    let questionCount = 0;
    // Loop through each question
    HTMLOutput.push("<h2>Exercise:</h2>");
    HTMLOutput.push("<div id=\"questions\">");
    questions.forEach(function (question, index) {
        // Increment the index so it starts at 1 instead of 0
        index++;

        HTMLOutput.push(`<div id="question${index}">`);

        // Store the question ID, type, and answer
        let tempStorage = JSON.parse(sessionStorage.getItem("questions"));
        if (Array.isArray(question.answer)) {
            tempStorage[`question${index}`] = JSON.stringify({"type": question.type, "isList": true, "listLength": question.answer.length, "answer": btoa(question.answer)});
        } else {
            tempStorage[`question${index}`] = JSON.stringify({"type": question.type, "isList": false, "answer": btoa(question.answer)});
        }
        sessionStorage.setItem("questions", JSON.stringify(tempStorage));

        // Add the question prompt
        HTMLOutput.push(`<p>${question.prompt}</p>`);

        HTMLOutput.push("<div class=\"questionStyling\">")
        // Add the appropriate input boxes
        if (question.type === "boolean") {
            HTMLOutput.push(`<label><input type="radio" name="question${index}" value="true">True</label><br>`);
            HTMLOutput.push(`<label><input type="radio" name="question${index}" value="false">False</label><br>`);

        } else if (question.type === "multiple_choice") {
            // Loop through each possible choice and add a new button
            question.choices.forEach(function (choice, useless) {
                HTMLOutput.push(`<label><input type="radio" name="question${index}" value="${choice}">${choice}</label><br>`);
            });

        } else if (question.type === "text") {
            // If the box parameter was specified
            if ("box" in question) {
                // Set the box width to the box parameter if it's a number
                if (typeof(question.box) === "number") {
                    boxWidth = question.box;
                    HTMLOutput.push(`<p><input type="text" id="output" size="${boxWidth}"></p>`);

                // Thanks Princess :) (she wrote this)
                } else if (typeof(question.box) === "string") {
                    const defaultWidth = "30";
                    let boxString = "";
                    // Loop while the regex matches
                    for (let i = 0, matchList; matchList = question.box.match(/\$\{(\d*)\}/); ++i) {
                        let width = defaultWidth; 

                        // Matches without numbers will be an empty string
                        if (matchList[1].length > 0) {
                            width = matchList[1];
                        }

                        // Saves joining an array later, just builds it now.
                        boxString += question.box.substr(0, matchList.index) + `<input type="box" id="output${i}" size="${width}">`;

                        // Erase everything up to the match text
                        question.box = question.box.substr(matchList.index + matchList[0].length);
                    }
                    HTMLOutput.push(`<p>${boxString}${question.box}<p>`);
                }
            // Set the box with the default width if it wasn't defined
            } else {
                HTMLOutput.push(`<p><input type="text" id="output" size="30"><p>`);
            }
        }
        // Close out the question + index seperate
        HTMLOutput.push("</div></div>");

        // Increment the question count
        questionCount++;
    });

    // Close out the questions and questionStyling tag
    HTMLOutput.push("</div></div>");

    // Add the submit button
    HTMLOutput.push("<button type=\"button\" id=\"submitButton\">Submit</button>");

    // Store the question count
    sessionStorage.setItem("questionCount", questionCount);

    return HTMLOutput.join("");
}

function getSelectedRadioValue(ID) {
    let radioButtons = document.getElementsByName(`question${ID}`);
    for (let i = 0; i < radioButtons.length; i++) {
        if (radioButtons[i].checked) {
            return radioButtons[i].value;
        }
    } 
}

function checkQuizAnswer(ID) {
    let questionsInStorage = JSON.parse(sessionStorage.getItem("questions"));
    let questionAnswer = JSON.parse(questionsInStorage[`question${ID}`]).answer;
    let questionIsList = JSON.parse(questionsInStorage[`question${ID}`]).isList;
    let questionType = JSON.parse(questionsInStorage[`question${ID}`]).type;

    let submittedAnswer = "";

    // The procedure for checking multiple choice is the same as boolean
    if (questionType === "boolean" || questionType === "multiple_choice") {
        submittedAnswer = getSelectedRadioValue(ID);

        // Convert the answer from base64 to text
        questionAnswer = atob(questionAnswer);

    } else if (questionType == "text") {
        // There is more than one text box
        if (questionIsList) {
            // Convert the answer from base64 to text
            questionAnswer = atob(questionAnswer);

            // Store the list length
            let questionListLength = JSON.parse(questionsInStorage[`question${ID}`]).listLength;

            // Get each text box value and put them into a list
            submittedAnswer = [];
            for (let i = 0; i < questionListLength; i++) {
                submittedAnswer.push(document.getElementById(`output${i}`).value);
            }
            submittedAnswer = String(submittedAnswer);
        // There is only one text box
        } else {
            submittedAnswer = document.getElementById("output").value;
            questionAnswer = atob(questionAnswer);
        }
    }
    
    if (submittedAnswer.toLowerCase() === questionAnswer.toLowerCase()) {
        return true;
    }
    return false;
}

function changeShownQuestion(ID) {
    // Get each child element and sort out the questions
    let questionChildren = document.getElementById("questions").children;
    for (var i = 0; i < questionChildren.length; i++) {
        // Hide all the questions except the one with the matching ID
        if (questionChildren[i].id.startsWith("question")) {
            if (questionChildren[i].id.endsWith(String(ID))) {
                questionChildren[i].style.display = "block";
            } else {
                questionChildren[i].style.display = "none";
            }
        }
    }
}

async function displayQuizbox(unit_name, lesson_name) {
    // Get the exercise box element
    let quizbox = document.getElementById("quizbox");

    // Get the exercise contents
    const quizJSONContent = await fetch(`/Java-Data-Pack-Tutorial/quizzes/${unit_name}/${lesson_name}.json`).then(r => r.json());
    let selectedQuestions = getRandomElements(quizJSONContent.questions, quizJSONContent.questionCount);

    // Compile each question into HTML
    quizbox.innerHTML = buildQuiz(selectedQuestions, quizJSONContent);

    let currentQuestionID = 1;
    changeShownQuestion(1);
    document.getElementById("submitButton").onclick = function() {
        if (checkQuizAnswer(currentQuestionID)) {
            currentQuestionID++;
            // Make sure the user isn't going to a question that doesn't exist
            if (currentQuestionID > Number(sessionStorage.getItem("questionCount"))) {
                alert("Quiz complete!");
                quizbox.style.display = "none";
            } else {
                alert("Correct!");
                changeShownQuestion(currentQuestionID);
            }
        } else {
            alert("Incorrect!");
        }
    }
}