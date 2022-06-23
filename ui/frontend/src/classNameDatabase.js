import classNameDatabase from './classNames.json';

const theDictionary = new Map(Object.entries(classNameDatabase));
const simpleClassNames = Object.keys(classNameDatabase)

function __getSimpleClassName(fullyQualifiedName) {
    return fullyQualifiedName.split(".")
        .filter(piece => piece[0] !== piece[0].toLowerCase())
        .join(".")
}

function __getLabel(fullyQualifiedName) {
    if (fullyQualifiedName.startsWith("org.eclipse.microprofile")) {
        return fullyQualifiedName.replace("org.eclipse.microprofile", "o.e.m")
    }
    return fullyQualifiedName;
}

function lookup(clue) {
    clue = clue.trim().toLowerCase()
    if (clue.length >= 2) {
        return simpleClassNames.filter(cn => cn.includes(clue))
            .map(cn => theDictionary.get(cn))
            .flat()
            .map(cn => {
                return {
                    label: __getLabel(cn),
                    simpleName: __getSimpleClassName(cn),
                    fullyQualifiedName: cn
                };
            })
    }
    return [];
}

export default lookup;