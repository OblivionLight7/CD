import re

Keyword = [
    "abstract",
    "do",
    "if",
    "package",
    "synchronized",
    "boolean",
    "double",
    "implements",
    "private",
    "this",
    "break",
    "else",
    "import",
    "protected",
    "throw",
    "byte",
    "extends",
    "instanceof",
    "public",
    "throws",
    "case",
    "false",
    "int",
    "return",
    "transient",
    "catch",
    "final",
    "interface",
    "short",
    "true",
    "char",
    "finally",
    "long",
    "static",
    "try",
    "class",
    "float",
    "native",
    "strictfp",
    "void",
    "const",
    "for",
    "new",
    "super",
    "volatile",
    "continue",
    "goto",
    "null",
    "switch",
    "while",
    "default",
    "assert",
    "string",
]
Operators = [
    "+",
    "-",
    "*",
    "/",
    "%",
    "<",
    "<=",
    ">",
    ">=",
    "==",
    "!=",
    "<<",
    ">>",
    ">>>",
    "=",
    "+=",
    "-=",
    "*=",
    "/=",
    "&",
    "^",
    "|",
    "&&",
    "||",
    "?:",
    "!",
    "^=",
    "|=",
    "<<=",
    ">>=",
    ">>>=",
    "++",
    "--",
]
Delimiters = [",", ";", "(", ")", "\\", "/", "{", "}", "[", "]", '"']
seperators = ["."]

Symbol = []
l = 0
a = open("prog.java", "r")
content = a.readlines()
data = []
r = "^([a-zA-Z_$][a-zA-Z\\d_$]*)$"
s = ".([^.]+)."
print(
    "\n*****************************************************************************\n"
)
print(
    "Line No\t\tLexeme\t\tToken\t\t\tToken Value\n*****************************************************************************\n"
)
for line in content:
    l += 1
    line = line.strip()
    data = line.split(" ")

    try:
        for i in range(0, 15):
            if data[i] in Delimiters:

                indk = Delimiters.index(data[i])

                print(
                    l,
                    "\t\t" + data[i] + "\t\tDelimeter\t\t(dl,",
                    indk,
                    ")\n____________________________________________________________________________\n",
                )
            elif data[i] in Operators:

                indk = Operators.index(data[i])

                print(
                    l,
                    "\t\t" + data[i] + "\t\tOperator\t\t(op,",
                    indk,
                    ")\n____________________________________________________________________________\n",
                )
            elif data[i].isnumeric():

                print(
                    l,
                    "\t\t"
                    + data[i]
                    + "\t\tConstant\t\t(c,"
                    + data[i]
                    + ")\n____________________________________________________________________________\n",
                )
            elif data[i] in Keyword:
                indk = Keyword.index(data[i])

                print(
                    l,
                    "\t\t" + data[i] + "\t\tKeyword\t\t\t(kw,",
                    indk,
                    ")\n____________________________________________________________________________\n",
                )
            elif re.search(r, data[i]):
                if data[i] not in Symbol:

                    Symbol.append(data[i])

                    indk = Symbol.index(data[i])

                    print(
                        l,
                        "\t\t" + data[i] + "\t\tIdentifier\t\t(id,",
                        indk,
                        ")\n____________________________________________________________________________\n",
                    )
                elif data[i] in Symbol:

                    indk = Symbol.index(data[i])

                    print(
                        l,
                        "\t\t" + data[i] + "\t\tIdentifier\t\t(id,",
                        indk,
                        ")\n____________________________________________________________________________\n",
                    )
            elif re.search(s, data[i]):
                new = data[i].split(".")

                for wr in new:

                    if wr not in Symbol:

                        Symbol.append(wr)

                        indk = Symbol.index(wr)

                        print(
                            l,
                            "\t\t" + wr + "\t\tidentifier\t\t(id,",
                            indk,
                            ")\n____________________________________________________________________________\n",
                        )
                    elif wr in Symbol:

                        indk = Symbol.index(wr)

                        print(
                            l,
                            "\t\t" + wr + "\t\tidentifier\t\t(id,",
                            indk,
                            ")\n____________________________________________________________________________\n",
                        )

            else:
                print(
                    "error at\t"
                    + data[i]
                    + "\n____________________________________________________________________________\n"
                )

    except:
        pass
print("\n\n*******************************************************************\n\n")
print(
    "\t\t\tSYMBOL TABLE\n\n*******************************************************************\n"
)
print("\t\tSymbol\t\t\tIndex\n\t\t*****************************************\n")
for word in Symbol:
    i = Symbol.index(word)
    print(
        "\t\t" + word + "\t\t\t", i, "\n\t\t_________________________________________\n"
    )
