Aquí están los Snippets que más uso:

{
    "Print with f-string": {
        "prefix": "pr",
        "body": [
            "print(f\"$1\")"
        ],
        "description": "Atajo para print con f-string"
    },

	"Input String": {
        "prefix": "inp",
        "body": [
            "input(\"$1\")"
        ],
        "description": "Atajo para input que recibe String"
    },

    "Input con entero": {
        "prefix": "intp",
        "body": [
            "int(input(\"$1\"))"
        ],
        "description": "Atajo para input convertido a entero"
    },

	"Try Except": {
        "prefix": ".try",
        "body": [
            "try:",
            "    $1",
            "except ValueError:",
            "    print(f\"Error:\")"
        ],
        "description": "Atajo para try except con ValueError"
    },

	"For Loop": {
        "prefix": ".for",
        "body": [
            "for ${1:item} in ${2:iterable}:",
            "    $3"
        ],
        "description": "Atajo para bucle for"
    },

	"Function": {
        "prefix": "def",
        "body": [
            "def ${1:function_name}(${2:params}):",
            "    $3",
            "    return"
        ],
        "description": "Atajo para definir una función"
    }

}