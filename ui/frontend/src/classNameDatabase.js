import classNameDatabase from './classNames.json';

// create the dictionary of simplename => fully qualified names
const theDictionary = new Map(Object.entries(classNameDatabase));
// list of only simple names
const simpleClassNames = Object.keys(classNameDatabase);
// fully qualified names split into pieces by dots
const packagePieces = Array.from(theDictionary.values()).flat().map(fqn => {
    const pieces = fqn.split(".").filter(piece => piece[0] === piece[0].toLowerCase());
    pieces.push(__getSimpleClassName(fqn))
    return pieces;
});

// Trie Node
class TrieNode {
    constructor(value) {
        this.value = value;
        this.children = []
    }

    getChild(key) {
        for (let child of this.children) {
            if (child.value === key) {
                return child
            }
        }
        return null
    }

    append(newChild) {
        this.children.push(newChild)
    }

}

// inserts the pieces into the trie
function __insert(pieces, start, root) {
    if (start < pieces.length) {
        const child = root.getChild(pieces[start])
        if (child) {
            __insert(pieces, start + 1, child)
        } else {
            const newChild = new TrieNode(pieces[start])
            root.append(newChild)
            __insert(pieces, start + 1, newChild)
        }
    }
}

// searches elements in the trie
function __search(pieces, start, root) {
    if (start < pieces.length) {
        const init = pieces[start]
        
        for (let child of root.children) {
            if (child.value === init) {
                return __search(pieces, start + 1, child)
            }
        }

        return []
    }

    return root.children.map(e => e.value)
}

// create the trie
const root = new TrieNode(null)
packagePieces.forEach(p => __insert(p, 0, root))

function lookup(clue, wordBetweenQuotes) {
    const suggestionsBasedOnClue = __lookupWithClue(clue);
    if (suggestionsBasedOnClue.length === 0) {
        let word = wordBetweenQuotes.trim()
        if (word.endsWith(".")) {
            word = word.slice(0, word.length - 1)
        }
        const pieces = word.split(".")
        return __search(pieces, 0, root).map(cn => {
            return {
                label: cn,
                simpleName: cn,
                fullyQualifiedName: cn
            };
        });
    }
    return suggestionsBasedOnClue;
}

function __lookupWithClue(clue) {
    clue = clue.trim().toLowerCase()
    if (clue.length >= 2) {
        return simpleClassNames.filter(cn => cn.includes(clue))
            .map(cn => theDictionary.get(cn))
            .flat()
            .map(cn => {
                return {
                    label: cn,
                    simpleName: __getSimpleClassName(cn),
                    fullyQualifiedName: cn
                };
            })
    }
    return [];
}

function __getSimpleClassName(fullyQualifiedName) {
    return fullyQualifiedName.split(".")
        .filter(piece => piece[0] !== piece[0].toLowerCase())
        .join(".")
}

export default lookup;