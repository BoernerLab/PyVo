# Nützliche Bibliotheken

Folgende Bibliotheken finden in PyVo Verwendung, sind jedoch ebenfalls im Allgemeinen in den Data Sciences nützlich. Bei Benutzung von PyVo müssen die folgenden Bibliotheken **nicht** zusätzlich installiert werden, da dies während der PyVo-Installation bei der Erstellung des Environments automatisch geschieht. Das Importieren in den Notebooks ist weiterhin notwendig.

**csv** für das Einlesen und Abspeichern von CSV-Dateien<br> 
- Lesen und Schreiben von CSV-Dateien möglich, auch ohne genaue Details zum csv-Format zu kennen<br> 
Einbindung `import csv`<br> 
Funktionen `csv.reader(), csv.writer()`, mehr unter [csv](https://docs.python.org/3/library/csv.html).

**numpy** für wissenschaftliche Berechnungen
- Bearbeitung von multidimensionalen Arrays und Matrizen
- bietet mathematische Funktionen für das Arbeiten mit Arrays und Matrizen<br>

Einbindung `import numpy as np`<br>
Funktionen `np.append()`, mehr unter [numpy](https://numpy.org/doc/stable/reference/).

**pandas** zur Datenanalyse und Datenanalyse
- bietet praktische Datenstrukturen (zB das Dataframe ("Datentabelle"))
- Datenverwaltung mittels Funktionen zur Verarbeitung von Dataframes<br>
Einbindung `import pandas as pd`<br>
Funktionen `pd.read_csv(), pd.DataFrame()`, mehr unter [pandas](https://pandas.pydata.org/docs/reference/index.html).

**math** für mathematische Funktionen
- enthält Funktionen wie Logarithmus- oder Exponentialfunktion, Winkelumrechnung, Wurzel/Potenzen uvm.
- Konstanten pi, e und Eulersche Zahl vordefiniert<br>
Einbindung `import math`<br>
Funktionen `math.exp(), math.log(), math.sqrt()`, mehr unter [math](https://docs.python.org/3/library/math.html).

**scipy** für wissenschaftliches Rechnen
- bietet verschiedenste Module für numerische Integration/Optimierung, Interpolation, algebraische Gleichungen, Differentialgleichungen, statistische Funktionen, Signal- und Bildverarbeitung uvm.<br>
Einbindung `import scipy`<br>
Funktionen `describe(), chisquare()`, mehr unter [SciPy](https://docs.scipy.org/doc/scipy/tutorial/general.html).

**matplotlib** für 2D/3D Datenvisualisierung
- verschiedene Arten von Diagrammen möglich<br>
Einbindung `import matplotlib.pyplot as plt`<br>
Funktionen `plt.plot(), plt.scatter()`, mehr unter [Matplotlib](https://matplotlib.org/3.1.1/api/pyplot_summary.html).


Weitere Funktionen, Erklärungen und Informationen zu Python unter [The Python Standard Library](https://docs.python.org/3/library/).