<projekt>
<app_beschreibung>
<zweck>
Ich möchte eine App, mit der ich eine .ods Datei hochladen und aus dieser Datei ein ganz bestimmtes Ergebnis auslesen kann.
</zweck>
<anforderungen>
<mobilität>Die App soll auch mobil sein.</mobilität>
<architektur>
Erstelle die App in unserem Backend und verknüpfe unser bereits vorhandenes Frontend.
</architektur>
<frontend>
Über das Frontend lade ich die Datei hoch. Nutze dazu das fileupload_2 Component.
</frontend>
</anforderungen>
</app_beschreibung>

<datei_verarbeitung>
<datei_struktur>
<spalten_und_zeilen>
Die Datei, die ich hochladen möchte, besteht aus mehreren Spalten und Zeilen. In der ersten Spalte steht ein Name, in den weiteren Spalten steht eine Dezimalzahl. 
Die Dezimalzahl kann auch eine Nachkommastelle haben.
</spalten_und_zeilen>
<spezielle_werte>
In den Spalten mit den Dezimalzahlen kann auch das Wort "Teiler" vorkommen. Wenn dieses Wort in einer Zelle steht, möchte ich, dass das Wort "Teiler" gelöscht wird und nur die Dezimalzahl bleibt.
</spezielle_werte>
<leere_elemente>
<zeilen>
Nicht alle Zeilen haben in jeder Spalte einen Wert.
Es gibt auch leere Zeilen.
Die leeren Zeilen möchte ich am Ende nicht haben.
</zeilen>
<spalten>
Es gibt auch leere Spalten.
Die leeren Spalten möchte ich am Ende nicht haben.
</spalten>
</leere_elemente>
<kopfzeilen>
Es kann vorkommen, dass in den ersten Zeilen nur Text steht und die Spalten in diesen Zeilen zusammengefasst sind.
</kopfzeilen>
<endformat>
Am Ende steht in der ersten Spalte die Namen und in den folgenden Spalten Dezimalzahlen mit einer Nachkommastelle.
</endformat>
</datei_struktur>
</datei_verarbeitung>

<datenanalyse>
<suche_und_ausgabe>
Suche in der gesamten Tabelle die 12 kleinste Zahl und gebe den zugehörigen Namen und die Zahl aus.
Suche in der gesamten Tabelle die 11 kleinste Zahl und gebe den zugehörigen Namen und die Zahl aus.
Suche in der gesamten Tabelle die 10 kleinste Zahl und gebe den zugehörigen Namen und die Zahl aus.
Suche in der gesamten Tabelle die 9 kleinste Zahl und gebe den zugehörigen Namen und die Zahl aus.
Suche in der gesamten Tabelle die 8 kleinste Zahl und gebe den zugehörigen Namen und die Zahl aus.
Suche in der gesamten Tabelle die 7 kleinste Zahl und gebe den zugehörigen Namen und die Zahl aus.
Suche in der gesamten Tabelle die 6 kleinste Zahl und gebe den zugehörigen Namen und die Zahl aus.
Suche in der gesamten Tabelle die 5 kleinste Zahl und gebe den zugehörigen Namen und die Zahl aus.
Suche in der gesamten Tabelle die 4 kleinste Zahl und gebe den zugehörigen Namen und die Zahl aus.
Suche in der gesamten Tabelle die 3 kleinste Zahl und gebe den zugehörigen Namen und die Zahl aus.
Suche in der gesamten Tabelle die 2 kleinste Zahl und gebe den zugehörigen Namen und die Zahl aus.
Suche in der gesamten Tabelle die 1 kleinste Zahl und gebe den zugehörigen Namen und die Zahl aus.
</suche_und_ausgabe>
</datenanalyse>

<ergebnis_darstellung>
<liste>
Erstelle eine nummerierte Liste mit den 12 Namen und Zahlen.
Zeige diese Liste als Ergebnis im Frontend an.
</liste>
<download>
Zeige unterhalb der Liste einen Download Button.
Die Datei soll als .csv Datei heruntergeladen werden können.
</download>
</ergebnis_darstellung>

<technische_anforderungen>
<programmiersprache>
Der Code soll in Python geschrieben werden.
</programmiersprache>
<code_qualität>
Baue den Code modular und einfach zu verstehen auf und natürlich so effektiv und sicher wie nur möglich.
</code_qualität>
</technische_anforderungen>

<projekt_struktur>
<anweisung>
Gib die Ordnerstruktur des Projekts mit XML-Tags aus.
</anweisung>
</projekt_struktur>
</projekt>
