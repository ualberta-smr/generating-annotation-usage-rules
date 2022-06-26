import MappingsDatabase from './packageToDocsMapping.json';

export default function getDocumentationLink(fullyQualifiedName) {
    // we pick the longest matching prefix
    let matchedPrefixes = Object.keys(MappingsDatabase)
            .filter(packName => fullyQualifiedName.startsWith(packName))
            .sort((a, b) => b.length - a.length)
    
    if (matchedPrefixes.length > 0) {
        const packageName = matchedPrefixes[0]
        return `${MappingsDatabase[packageName]}/${fullyQualifiedName.replaceAll(".", "/")}.html`
    }

    return null
}