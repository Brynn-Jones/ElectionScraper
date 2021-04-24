**ENGETO Project 3** 

**Description**

This project is used to extract the voting results of the 2017 parliamentary election in the Czech Republic from the
following webpage: https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ


**Installing the libraries** 

Libraries used in the code are listed in the requirements.txt file. For installation, it is recommended to use
a new virtual environment and use the following:
> pip install –r requirements.txt

**Running the project**

Running the election_scraper.py file from the command line requires two mandatory arguments: a link to a
district election results page, written in quotation marks, and a name of the resulting file. The extracted
results are then saved as a CSV file.

**Example:**

Extracting election results for the Prostějov district:

1. arg.: `“https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103”`
2. arg.: `prostejov`

In progress:

`2017 Election Results Scraper`

`Extracting data...`

`Creating a CSV file...
`

Output:

`Results have been successfully saved to prostejov.csv`

For reference, see the included example file, prostejov.csv.
