grammar RulepadGrammar;

inputSentence
    : (emptyLine* | mustClause) end? NL* EOF
    ;

mustClause
    : functions must have functionExpression
    | constructors must have constructorExpression
    | classes must have classExpression
    | declarationStatements must have declarationStatementExpression
    ;

/*
    Constants
*/
SPACE
    : (' ' | '\t')+
    ;


combinatorialWords
    : '"' (Alphabet | symbols | SPACE)+ '"'
    ;

symbols
    : '.' | '=' | '>' | '<' | '(' | ')' | '\'' | '&' | '|' | '[' | ']'
    ;

Alphabet
    : [a-zA-Z0-9_-]
    ;
end
    : '.'
    ;

NL
    : '\r' | '\n'
    ;

emptyLine
    : NL
    ;

/*
    connectors
*/

must
    : 'must '
    ;

of
    : 'of '
    ;


and_
    :  'and '
    ;

or_
    :  'or '
    ;

have
    : 'have '
    ;

withWord
    : 'with '
    ;


binary
    : and_ | or_
    ;

LPAREN
    : '('
    ;

RPAREN
    : ')'
    ;

/*
    ------------------
*/

/*
    names
*/

NAME
    : 'name '
    ;

names
    : NAME nameCondition
    ;

nameCondition
    : combinatorialWords SPACE
    ;

/*
    values
*/

VALUE
    : 'value '
    ;

values
    : VALUE valueCondition
    ;

valueCondition
    : combinatorialWords SPACE
    ;


/*
    annotations
*/

ANNOTATION
    : 'annotation '
    ;

annotations
    : ANNOTATION annotationCondition
    ;

annotationCondition
    : combinatorialWords SPACE annotationConditionTransition?
    | annotationConditionTransition
    ;

annotationConditionTransition
    : withWord annotationExpression
    ;

annotationExpression
    : LPAREN annotationExpression RPAREN
    | left=annotationExpression op=binary right=annotationExpression
    | ( parameters)
    | annotationExpression SPACE
    ;


/*
    extensions
*/

EXTENSION
    : 'extension '
    ;

SUPERCLASS
    : 'Superclass'
    ;

extensions
    : EXTENSION extensionCondition
    ;

extensionCondition
    : of ( combinatorialWords SPACE | SUPERCLASS)
    ;


/*
    implements
*/

IMPLEMENTATION
    : 'implementation '
    ;

INTERFACE
    : 'Interface '
    ;

implementations
    : IMPLEMENTATION implementationCondition
    ;

implementationCondition
    : of ( combinatorialWords SPACE | INTERFACE )
    ;


/*
    functions
*/

FUNCTION
    : 'function '
    | 'method '
    ;

functions
    : FUNCTION functionCondition
    ;

functionCondition
    : withWord functionExpression
    ;

functionExpression
    : LPAREN functionExpression RPAREN
    | left=functionExpression op=binary right=functionExpression
    | ( annotations | returnTypes | functionParameters | configurationFiles )
    | functionExpression SPACE
    ;

/*
    return types
*/

RETURN_TYPES
    : 'return type '
    ;

returnTypes
    : RETURN_TYPES returnTypeCondition
    ;

returnTypeCondition
    : combinatorialWords SPACE;

/*
    constructors
*/

CONSTRUCTOR
    : 'constructor '
    ;

constructors
    : CONSTRUCTOR constructorCondition
    ;

constructorOf
    : of classes
    ;

constructorCondition
    : withWord constructorExpression
    ;

constructorExpression
    : LPAREN constructorExpression RPAREN
    | left=constructorExpression op=binary right=constructorExpression
    | ( annotations | functionParameters )
    | constructorExpression SPACE
    ;

/*
    parameters-> mainly annotations for now 
*/

PARAMETER
    :  'parameter '
    ;

parameters
    : PARAMETER parameterCondition
    ;

parameterCondition
    : combinatorialWords SPACE parameterConditionTransition?
    | parameterConditionTransition
    ;

parameterConditionTransition
    : withWord parameterExpression;

parameterExpression
    : LPAREN parameterExpression RPAREN
    | left=parameterExpression op=binary right=parameterExpression
    | ( types | names | values )
    | parameterExpression SPACE
    ;
/*
    function parameters

    function with parameter "String value" with annotation "a.b.c.Hello"
    function with parameter with (type "String" and name "value" and annotation "a.b.c.Hello" )
*/

functionParameters
    : PARAMETER functionParameterCondition?
    ;

functionParameterCondition
    : combinatorialWords SPACE functionParameterConditionTransition?
    | functionParameterConditionTransition
    ;

functionParameterConditionTransition
    : withWord functionParameterExpression
    ;

functionParameterExpression
    : LPAREN functionParameterExpression RPAREN
    | left=functionParameterExpression op=binary right=functionParameterExpression
    | ( types | names | annotations )
    | functionParameterExpression SPACE
    ;

/*
    types
*/

TYPES
    : 'type '
    ;

types
    : TYPES typeCondition
    ;

typeCondition
    : combinatorialWords SPACE
    ;


/*
    declarationStatements
*/

DeclarationStatement
    : 'declaration statement '
    | 'field '
    ;

declarationStatements
    : DeclarationStatement declarationStatementCondition
    ;

declarationStatementCondition
    : withWord declarationStatementExpression
    ;

declarationStatementExpression
    : LPAREN declarationStatementExpression RPAREN
    | left=declarationStatementExpression op=binary right=declarationStatementExpression
    | ( annotations | types | configurationFiles )
    | declarationStatementExpression SPACE
    ;

/*
    configurationFile
*/

ConfigurationFile
    : 'configuration file '
    ;

configurationFiles
    : ConfigurationFile configurationFileCondition
    ;

configurationFileCondition
    : withWord configurationFileExpression
    ;

configurationFileExpression
    : LPAREN configurationFileExpression RPAREN
    | left=configurationFileExpression op=binary right=configurationFileExpression
    | ( configurationProperties)
    | configurationFileExpression SPACE
    ;

/*
    configurationProperties
*/

CONFIGURATION_PROPERTIES
    :  'property '
    ;

configurationProperties
    : CONFIGURATION_PROPERTIES configurationPropertyCondition
    ;

configurationPropertyCondition
    : combinatorialWords SPACE configurationPropertyConditionTransition?
    | configurationPropertyConditionTransition
    ;

configurationPropertyConditionTransition
    : withWord configurationPropertyExpression
    ;

configurationPropertyExpression
    : LPAREN configurationPropertyExpression RPAREN
    | left=configurationPropertyExpression op=binary right=configurationPropertyExpression
    | ( types | names | values )
    | configurationPropertyExpression SPACE
    ;


/*
    classes
*/

CLASSES
    : 'class '
    ;

classes
    : CLASSES classCondition
    ;

classCondition
    : withWord classExpression
    ;

classExpression
    : LPAREN classExpression RPAREN
    | left=classExpression op=binary right=classExpression
    | ( annotations | extensions | implementations | functions | constructors | declarationStatements | configurationFiles | beans | beansFile)
    | classExpression SPACE
    ;

/*
    bean declaration
 */

 BEAN_DECL
    : 'bean declaration '
    ;

beans
    : BEAN_DECL
    ;

BEANS_FILE
    : 'beans file'
    ;

beansFile
    : BEANS_FILE
    ;