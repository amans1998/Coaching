try:
    n=10/0
    print(n)
except ZeroDivisionError:
    print("inside except")

try:
    n=10/0
    print(n)
except Exception:
    print("inside except")
try:
    n=10/0
    print(n)
except Exception:
    print("inside except")
finally:
    print("inside finally")
try:
    n=10/0
    print(n)
except ValueError:
    print("inside except")
finally:
    print("inside finally")
