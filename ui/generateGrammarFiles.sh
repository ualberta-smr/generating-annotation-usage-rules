curdir=$(pwd)
frontEndDir=$curdir/frontend/src/grammar/
java -Xmx500M -cp "./tools/antlr-4.9-complete.jar:$CLASSPATH" org.antlr.v4.Tool -Dlanguage=JavaScript ../violation-detection/src/main/antlr4/ca/ualberta/grammar/RulepadGrammar.g4 -o "$frontEndDir" -Xexact-output-dir