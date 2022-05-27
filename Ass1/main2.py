import re
delimiters = ['(','.', ')', '{', '}', ';', ',', '"', "'", ':',' ']
keys = ["abstract","do","if","package","synchronized","boolean","double","implements","private","this","break", "else","import","protected",
            "throw","byte","extends","instanceof","public","throws","case","false","int","return","transient","catch","final","interface","short",
            "true","char","finally","long","static","try","class","float","native","strictfp","void","const","for","new","super","volatile","continue",
            "goto","null","switch","while","default","assert","string"]
opts = ['=', '+', '-', '*', '/', '%', '++', '--', '==', '!=', '<', '>', '<=', '>=', '&&', '||', '!']
 

myProgram= open('ass1.java', 'r')
inputLines = [line.strip() for line in myProgram.readlines()]
 
outputTable = []
currentLexeme = ''
 
for line_no in range(len(inputLines)):
    charIter = iter(range(len(inputLines[line_no])))
    for index in charIter:
        char = inputLines[line_no][index]
        if (char in delimiters):
            if (len(currentLexeme) != 0):
                if (currentLexeme in keys):
                    token = 'Keyword'
                elif (currentLexeme in opts):
                    token = 'Operator'
                else:
                    if (currentLexeme.isnumeric()):
                        token = 'Constant'
                    else:
                        token = 'Identifier'
 
                outputTable.append({'line': line_no + 1, 'lexeme': currentLexeme, 'token': token})
                currentLexeme = ''
            if (char != ' '):
                outputTable.append({'line': line_no + 1, 'lexeme': char, 'token': 'Delimiter'})
        
        else:
            currentLexeme += char
            
 
with open(r'C:\Users\hp\Documents\Out.txt','w') as outFile:
    print(f"{'LINE NUMBER':<{20}}{'LEXEME':{20}}{'TOKEN':{20}}", file=outFile)
    for line in outputTable:
        print(f"{line['line']:<{20}}{line['lexeme']:{20}}{line['token']:{20}}", file=outFile)
