
# Acquiring and processing information on world's largest banks

This project compiles a list of the top 10 largest banks in the world ranked by market capitalization (in billion USD). The objective is to acquire the relevant data and transform it for storage in multiple currencies, specifically GBP, EUR, and INR, using exchange rate information provided in a CSV file.

## Table of Contents

1. [Objectives](#objectives)
2. [Key Features](#key-features)
3. [Technology Stack](#technology-stack)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Screenshots](#screenshots)
7. [License](#license)
8. [Contact](#contact)



## Objectives

- **Data Acquisition**: Retrieve data on the largest banks based on market capitalization.

- **Data Transformation**: Convert market capitalization values from USD to GBP, EUR, and INR using the provided exchange rates.

- **Data Storage**: Save the processed information both in a local CSV file and as a table in a database.

- **ETL pipeline**: Developed an ETL pipeline in Python to extract, transform, and load data on the top 10 largest banks by market capitalization from a Wikipedia page.

- **Web Scrapping**: Use Webscraping techniques to extract information from any website as per requirement.

- **Python libraries usage**: Use Pandas data frames and dictionaries to transform data as per requirement.

- **Querying**: Query the database tables using SQLite3 and pandas libraries.

- **Log the proccess of the ETL pipeline**: Log the progress of the code properly


## Key Features

- **Data Acquisition**: Fetch and compile data for the largest banks by market capitalization from this Wikipedia page: [List of largest Banks in the world](https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks).
- **Data Transformation**: Convert monetary values to different currencies based on exchange rates.
- **Data Storage**: Store the transformed data in a structured CSV format for easy access. 
- **Data Storage in Database**: Save the processed data in a SQLite database table for further analysis

## Technology Stack

- **Language:** Python
- **Libraries:** Pandas, Numpy, datetime, BeautifulSoup
- **Database:** SQLite3
- **Deployment:**: SN Labs

## Installation

Follow these steps to set up and run the project.

### Prerequisites

Make sure you have the following installed:
- [Python](https://www.python.org/downloads/)

### Required Python Libraries

Ensure the following libraries are installed:

- ```requests```: For accessing web data.
- ```bs4 (BeautifulSoup)```: For web scraping and parsing HTML.
- ```pandas```: For data processing, formatting, and database communication.
- ```sqlite3```: For establishing a connection with the SQLite database.
- ```numpy```: For performing mathematical operations like rounding.
- ```datetime```: For extracting timestamps for logging purposes.

### Installation Instructions

Use the following command to install each library from your terminal:

```bash
python3.11 -m pip install <library_name>
```
Replace ```<library_name>``` with the name of each required library (e.g., ```requests```, ```bs4```, ```pandas```).


### Downloading the Exchange Rate Data

```bash
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv
```

### Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/jestebanpelaez18/WorldsLargestBanks-DataProcessing.git
cd repo-name
```

If you choose to clone this repository, make sure to delete the following files: ```Banks.db``` , ```code_log.txt``` and ```Largest_banks_data.csv```. These files are included in the main repository for demonstration purposes and represent the expected output of the project. Removing them allows you to run the ETL process from scratch and generate fresh results.

### Run the Code

```bash
python banks_project.py
```


## Usage

Running the code will generate the following outputs:

1. **Code Log File**: A detailed log recording each stage of the ETL process, ensuring transparency and easy troubleshooting. 
2. **Largest banks data CSV**: A CSV file named ```Largest_banks_data.csv``` containing the processed and transformed data
2. **Largest banks database**: An SQLite database named ```Banks.db```, storing the transformed data for efficient querying and analysis. 


## License

This project is licensed under the MIT License. See the [LICENSE](https://choosealicense.com/licenses/mit/) file for more details. 




## Contact

Contact me via linkedin.

- [Juan Esteban Pelaez](https://www.linkedin.com/in/jestebanpelaez18/)
