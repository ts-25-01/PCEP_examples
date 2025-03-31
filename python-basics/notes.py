print("Hello world")


# Weitere Befehle

def test(x):
    print(x)
argument = "hallo"
test(argument)

def division(x,y):
    try: 
        return x // y
    except ZeroDivisionError:
        print("Wir dürfen nicht durch 0 teilen")



# Unterschied zwischen Python2 und Python3 Version
## print-Anweisung
### Python2
# print "Hello"
# 3 / 2 # Ganzzahldivision, d.h. Ergebnis 1
# range() # erzeugt in Python2 ne Liste, 
# xrange() # ist der Generator, wie in Python3 mit range() für z.B. for-Schleifen
# except Exception, e:
### Python3
print("Hello")
3 / 2 # echte Division, d.h. Ergebnis 1.5
3 // 2 # Ganzzahldivision, d.h. Ergebnis 1
round(3 / 2) # Kaufmännisches Runden, aufrunden ab >= .5, d.h. Ergebnis 2
range() # ist ein Generator für z.B. ne for-Schleife, wo wir definieren, dass wir genau 3mal rein wollen in die Schleife
# except Exception as e:
#     print("Fehler", e)

