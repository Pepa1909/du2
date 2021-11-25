**Manuál pro program**

Tento program umí načíst soubor s příponou .csv nacházející se ve stejné složce. Tento program se musí jmenovat vstup.csv a jeho sloupce musí být v následujícm formátu, rozděleny čárkou:

238000,QD,2016,02,13,   8.2400

Program následně soubor přečte, nalezne chybějící či zduplikované hodnoty a vytvoří 2 nové soubory: vystup_7dni.csv a vystup_rok.csv
V prvním zmíněném souboru se budou vyskytovat průměrné hodnoty za každých 7 dní od začátku měření, když by na poslední týden nevyzbylo 7 dní, vezme, kolik dní zbyde.
Druhý soubor vypočítá průměrné hodnoty za každý rok. Program nepozná, kolik hodnot v roce je, nový rok rpo něj začíná novou hodnotou sloupce 3. 