hljs.registerLanguage("mcfunction", function() {
    "use strict";
    return function(e) {
        return {
            name: "MCFunction",
            aliases: ["mcfunction", "mc"],
            case_insensitive: !0,
            contains: [{
                className: "comment",
                begin: /^\s*#>/,
                end: /$/,
                contains: [{
                    className: "doctag",
                    begin: /.+/
                }],
                relevance: 5
            }, {
                className: "comment",
                begin: /^\s*#.+/,
                relevance: 1
            }, e.QUOTE_STRING_MODE, e.APOS_STRING_MODE, {
                className: "literal",
                begin: /[a-f0-9]+-[a-f0-9]+-[a-f0-9]+-[a-f0-9]+-[a-f0-9]+/,
                relevance: 15
            }, {
                className: "symbol",
                begin: /[a-z0-9_]+:[a-z_][a-z0-9_/]+/,
                relevance: 15
            }, {
                className: "literal",
                begin: /@[parse]\b/,
                relevance: 10
            }, {
                className: null,
                begin: /[a-z]+=/,
                end: /[\],\{]/,
                contains: [{
                    className: "number",
                    begin: /-?\d+(\.\d+)?/
                }, {
                    className: "symbol",
                    begin: /#?[a-z0-9_]+:[a-z_][a-z0-9_/]+/,
                    relevance: 10
                }, {
                    className: "literal",
                    begin: /\b(true|false)\b/
                }, {
                    className: "string",
                    begin: /[a-z_0-9$]+/
                }],
                relevance: 2
            }, {
                className: "None",
                begin: /run /,
                end: / |$/,
                contains: [{
                    className: "keyword",
                    begin: /[a-z_0-9$]+/
                }],
                relevance: 5
            }, {
                className: "number",
                variants: [{
                    begin: /-?\b(\.\d+|\d+(\.\d+)?)[bdfils]?/
                }, {
                    begin: /[~^](-?\.\d+|\d+(\.\d+)?)?/
                }],
                relevance: 0
            }, {
                className: "literal",
                begin: /\b(true|false)\b/,
                relevance: 0
            }, {
                className: "keyword",
                begin: /^\s*[a-z]+/,
                relevance: 0
            }]
        }
    }
}());