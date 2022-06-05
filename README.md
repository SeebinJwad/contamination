# CONTAMINATION ALGORITHM


Creation of the database:
unique id will be 4 columns not one column
taking a file, for this 'mEERf-5E'
sorting the file by unique id, chromosome pos, ref alt
start end only start is used for pos

chr only accepts 1-22 X Y, sort function sorts in that order
looks for #CHROM, POS, REF, ALT column names because thats the standard vcf file, if different must be specified

running sample file against database
1) sort sample file based on chr-pos-ref-alt
2) add sample file to database - add chr pos ref alt rows at bottom and create a column with header name of sample and values of 0 until the bottom where the added rows are, there add 1s until the very bottom (0 means not in that row of database, 1 means is in that row)
3) create a separate dataframe that has the rows of duplicate values with values
4) remove first occurence duplicate values of rows (row meaning chr pos ref alt) in database
5) sort database

ACTUAL FUNCTION PSEUDOCODE
def add_to_database(df):
uqids = chr pos ref alt columns
create ref df pd merge of uqids in both sample and database with those values in ref df 
need the non duplicate rows: create isin column df of sample columns in ref df
take the false uqids and add them to ref df with values of 0 for all columns
add sample header name column with all 1s
add column sample name header in database df with all 0s
append ref df to bottom of database df
remove duplicate rows first occurence in database df
sort database df based on uqid
