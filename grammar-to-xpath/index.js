const fs = require("fs");
const { EOL } = require("os");
const { exit } = require("process");

const { antlr } = require("./languageProcessing");

const convert = (line, words) => {
    console.log(line);
    let { quantifier, constraint } = antlr(line).results;

    for (let word of words) {
        const wordPieces = word.split(".");
        const lastWord = wordPieces[wordPieces.length - 1];
        const isSpecial = lastWord[0] === '<' && lastWord[lastWord.length - 1] === '>'
        let condition;
        if (isSpecial) {
            let root = wordPieces
                        .slice(0, wordPieces.length - 1)
                        .map((value, i) => `src:name[${i+1}][text()='${value}']`)
                        .join(" and ")
            let replaceableOnes = lastWord
                .slice(1, lastWord.length - 1)
                .split(",")
                .map(value => `src:name[${wordPieces.length - 1}][text()='${value}']`)
                .join(" or ")
            condition = `${root} and (${replaceableOnes})`
        } else {
            condition = wordPieces.map((value, i) => `src:name[${i+1}][text()='${value}']`).join(" and ")
        }
        let re = new RegExp(`\\[${word}\\]`, "g");
        quantifier = quantifier.replace(re, `[src:name[(${condition})]]`);
        constraint = constraint.replace(re, `[src:name[(${condition})]]`);
    }

    return {
        quantifier,
        constraint,
    };
};

const extractsWordsFromLine = (line) => {
    let words = line.match(/"[a-zA-Z.<>,]+"/g);
    words = words.map((a) => a.replace(/['"]+/g, ""));
    let set = new Set();
    words.forEach((e) => set.add(e));
    return words;
};

const lineToXPaths = (line) => {
    const set = extractsWordsFromLine(line);
    return convert(line, set);
};

const main = (readFrom, writeTo) => {
    let array = JSON.parse(fs.readFileSync(readFrom).toString());

    let result = array.map((a) => {
        let constraint = lineToXPaths(a.rule).constraint;
        let quantifier = lineToXPaths(a.antecedent_origin).quantifier;
        let candidate_id = a.id;
        let grammar = a.rule;
        return {
            quantifier,
            constraint,
            candidate_id,
            grammar,
        };
    });

    fs.writeFileSync(writeTo, JSON.stringify(result));
};

// node index.js "./data/input.txt" "./data/results.json"
if (require.main === module) {
    const args = process.argv.slice(2);
    if (args.length != 2) {
        console.error(`2 arguments expected: [from file] [to file]`);
        exit(2);
    }
    const [from, to] = args;
    main(from, to);
}
