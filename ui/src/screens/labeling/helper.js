import data from "./data";

export const highlightWords = (string) => {
    string = string.replace(/<[^>]*>?/gm, "");

    string = string.replace(
        /((class|declaration statement|function|annotation))/g,
        `<span class="hl-italic">$1</span>`
    );

    string = string.replace(
        /((must have))/g,
        `<span class="hl-blue-bg">$1</span>`
    );
    const matches = string.match(/("[a-zA-Z]+")/g)
    if (matches == null) return string;
    let set = new Set();
    for (let item of matches) {
        set.add(item);
    }
    for (let item of set) {
        string = string.replaceAll(item, `<span class="hl-red">${item}</span>`);
    }
    return string;
};

let currentRuleIndex = -1;

export function getNextRuleToLabel() {
    if (currentRuleIndex + 1 < data.length) {
        currentRuleIndex += 1;
    }
    const rule = data[currentRuleIndex];
    return rule;
}

export function getPreviousRuleToLabel() {
    if (currentRuleIndex - 1 >= 0) {
        currentRuleIndex -= 1;
    }
    if (currentRuleIndex < 0) return null;
    const rule = data[currentRuleIndex];
    return rule;
}

export function updateRule(ruleToUpdate) {
    const i = data.findIndex(rule => ruleToUpdate.id === rule.id)
    if (i !== -1) {
        data[i] = ruleToUpdate;
    }
}