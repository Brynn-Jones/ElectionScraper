**ENGETO Project 3** 

**Description**

This project is used to extract the voting results of the 2017 parliamentary election in the Czech Republic from the
following webpage: https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ

To extract results for all districts, use https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ

To extract results for all municipalities in a specific district, click on the X symbol in the 'Výběr obce' column,
and use the resulting link (e.g. https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103)

**Downloading from GitHub**

Download the ZIP file and extract the directory (e.g. C:\ElectionScraper-master)

**Virtual environment**

Using the Command Prompt, create a new virtual environment, e.g. in directory C:\Elect:

> python -m venv c:\Elect  

Activate the virtual environment:

> C:\Elect\Scripts\activate.bat

Change directory to C:\ElectionScraper-master:

> (Elect) C:\>cd C:\ElectionScraper-master

**Installing the libraries** 

Libraries used in the code are listed in the requirements.txt file. For installation, it is recommended to use
a new virtual environment use the following:
> (Elect) C:\ElectionScraper-master>pip install -r requirements.txt

**Running the project**

Running the election_scraper.py file from the command line requires two mandatory arguments: a link to a
district election results page, written in quotation marks, and a name of the resulting file.

Examples:

> (Elect) C:\ElectionScraper-master>election_scraper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103" results_prostejov

> (Elect) C:\ElectionScraper-master>election_scraper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2102" results_beroun

> (Elect) C:\ElectionScraper-master>election_scraper.py "https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ" results_all_regions

> (Elect) C:\ElectionScraper-master>election_scraper.py "https://volby.cz/pls/ps2017nss/ps3?xjazyk=EN" results_all_regions (English version, names without diacritics)

The extracted results are then saved as a CSV file.


**Example:**

Extracting election results for the Prostějov district:

1. arg.: `“https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103”`
2. arg.: `prostejov`

Input:

>election_scraper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103" results_prostejov

The first argument calls for the code to extract data from district number 7103, in region number 12.
The second argument determines the name of the resulting CSV file.


In progress:

`2017 Election Results Scraper`

`Extracting data...`

`Creating a CSV file...`


Output:

`Results have been successfully saved to results_prostejov.csv`

For reference, see the included example file, results_prostejov.csv.
