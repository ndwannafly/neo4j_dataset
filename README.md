# LLP Datasets step-by-step guide

## Overall work plan

1. Export 2 tables as csv from the neo4j database;
2. Convert them via the python script, table by table, separately;
3. Add required edges MANUALLY as needed (try to use a query that has a really small number of results);
4. Write the query;
5. ???
6. PROFIT

## Python script

Run from within the python_script/ folder. Define the input file and the table name inside.

For ease of use, pipe output to a file:

```bash
python to_inserts.py > output.txt
```