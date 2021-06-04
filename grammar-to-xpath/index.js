const fs = require("fs");
const { EOL } = require("os");
const { exit } = require("process");

const { antlr } = require("./languageProcessing");

const convert = (line, words) => {
    let { quantifier, constraint } = antlr(line).results;

    for (let word of words) {
        let re = new RegExp(`\\[${word}\\]`, "g");
        quantifier = quantifier.replace(re, `[src:name[text()='${word}']]`);
        constraint = constraint.replace(re, `[src:name[text()='${word}']]`);
    }

    return {
        quantifier,
        constraint,
    };
};

const main = (readFrom, writeTo) => {
    let array = JSON.parse(fs.readFileSync(readFrom).toString())

    let result = array.map((a) => {
        let line = a.rule;

        let words = line.match(/"[a-zA-Z]+"/g);
        words = words.map((a) => a.replace(/['"]+/g, ""));
        let set = new Set();
        words.forEach((e) => set.add(e));
        let obj = convert(line, set);
        obj["candidate-id"] = a.id;
        obj["grammar"] = line;
        return obj;
    });

    fs.writeFileSync(writeTo, JSON.stringify(result));
};

// node index.js "./data/input.txt" "./data/results.json"
if (require.main === module) {
    const args = process.argv.slice(2)
    if (args.length != 2) {
        console.error(`2 arguments expected: [from file] [to file]`)
        exit(2)
    }
    const [from, to] = args;
    main(from, to);
}
