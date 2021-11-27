# Manuál pro program

Tento program umí načíst soubor s příponou .csv nacházející se ve stejné složce. Soubor se musí jmenovat vstup.csv, jeho řádky musí být   v následujícm formátu, hodnoty rozděleny čárkou:

databázové číslo,označení typu dat,rok,měsíc,den,průměrný denní průtok (m3/s)

příklad:
238000,QD,2016,02,13,   8.2400

Program následně soubor přečte, a vytvoří 2 nové soubory: vystup_7dni.csv a vystup_rok.csv. Pokud nalezne chybějící hodnoty či zduplikované řádky, napíše, kde se daná chyba nachází, a ukončí se. Program navíc do terminálu (obdélník dole) napíše minimum a maximum za daný rok i se dnem, kdy jev nastal.

V souboru vystup_7dni.csv se budou vyskytovat průměrné hodnoty za každých 7 dní od začátku měření s tím, že 
v souboru bude datum prvního dne daného týdnu; když by na poslední týden nevyzbylo 7 dní, vezme všechny zbylé dny.

Soubor vystup_rok.csv bude obsahovat průměrné hodnoty za každý rok, datum roku bude datum 1. naměřené hodnoty v ten rok (pravděpodobně 1. leden). Program začíná počítat nový rok vždycky se změnou třetího sloupce (rok), ale nepozná, jestli nějaký den v roce chybí. 
