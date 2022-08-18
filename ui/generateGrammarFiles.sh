# This script generates Lexers and Parsers from the RulePad grammar.
# Run this whenever you introduce new constructs to the language
curdir=$(pwd)
frontEndDir=$curdir/frontend/src/grammar/generated
java -Xmx500M -cp "./tools/antlr-4.9-complete.jar:$CLASSPATH" org.antlr.v4.Tool -Dlanguage=JavaScript ../violation-detector/violation-detection/src/main/antlr4/ca/ualberta/grammar/RulepadGrammar.g4 -o "$frontEndDir" -Xexact-output-dir