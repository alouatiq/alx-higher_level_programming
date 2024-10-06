#!/usr/bin/python3
text_indentation = __import__('5-text_indentation').text_indentation

text_indentation("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? Non autem hoc: igitur ne illud quidem.")
print("")
text_indentation("Hello:  There")
print("")

try:
    text_indentation(123)
except Exception as e:
    print(e)
