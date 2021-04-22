1. Display all the data from the houseware table.

```sql
select *
from houseware
```

2. Get just the name of every houseware.

```sql
select name
from houseware
```

3. Get just the name and price of every houseware.

Not sure which price, so went with both:

```sql
select name, buy_price, sell_price
from houseware
```

4. [DISTINCT] Get the name of every recipe material (no duplicates).

```sql
select distinct material
from recipe
```

5. [WHERE] What houseware items can be sold for at least 1000 bells? 

Only name no price:
```sql
select name
from houseware
where sell_price>1000
```

Can add extra columns in select for more info.

6. [WHERE] I want to find any houseware that can fit in a 1x1 space (width x height) that costs less than 1000 bells.

```sql
select name
from houseware
where sell_price>1000 and width*height<=1
```

7. [WHERE, LIKE] I'm looking for stuff that involves the word office, but there's no office tag. Get me a list of all the names that involve the word 'office'.

```sql
select *
from houseware
where name like '%office%'
```
Looks like theres an office tag, but hey only have to change the where name to where tag

8. [COUNT] How many houseware items are there?

```sql
select count(name)
from houseware
```

Gives 613 different items

9. [WHERE with COUNT] How many many items can be bought for less than 1000 bells?

```sql
select count(name)
from houseware
where buy_price < 1000
```
Gives only 18 items, guess things are pricey.

10. [AGGREGATION] How much is the average buying price divided by selling price?

```sql
select AVG(buy_price/sell_price)
from houseware
```
Gives 4.0. 

Sounds like a bit of a ripoff.

11. [AGGREGATION, TYPES] How much is the average selling price divided by buying price, rounded to two decimal places?

```sql
select round(avg(cast(sell_price as real)/buy_price),2)
from houseware
```

As expected, gives 0.25

12. [ORDER] Produce a list of all the names of the houseware items and their sell price, ordered by their sell price.

```sql

```

13. [ORDER, LIMIT] Now produce the list of names+buy_price, ordered by buy_price descending, limited to the top 10.

```sql

```

14. [ORDER, ALIAS] The hha_base is a number indicating how "nice" the item is. I want to find items that are have a higher hha_base per square unit of space. Produce a list of the names of items, sorted by their hha_base divided by the area they take up.

```sql

```

15. [GROUP BY] How many houseware items are in each tag? Make sure you order them by frequency!

```sql

```

16. [GROUP BY, ALIAS] There's actually only a few different possible areas for the given objects. How many are there of each possible area?

```sql

```

17. [GROUP BY, AGGREGATION] How much would it cost to buy all the items, within each tag? For example, the Audio tag's items would cumulatively cost 103600

```sql

```

18. [GROUP BY, WHERE, AGGREGATION] How much area would all the interactable houseware items take, within each tag?

```sql

```

19. [JOIN, GROUP BY] For each item, how many distinct materials does it require?

```sql

```

20 [GROUP BY, ORDER, LIMIT] What are the top 10 materials used in recipes (calculated by totaling the amounts per material).

```sql

```

21. [JOIN, WHERE] List all the recipes that require at least 10 star fragments

```sql

```

22. [JOIN, WHERE, GROUP BY, ORDER] What tag has the most recipes that require 'stone'?

```sql

```

23. [JOIN, WHERE] Get the names and colors of all housewares.

```sql

```