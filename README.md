# etl-with-py
Extract, Transform, and Load Data using Python

## Objectives:
1. Read CSV, JSON, and XML file types.
2. Extract data from different file types.
3. Transform data to the required format.
4. Save the transformed data in a ready-to-load format, which can be loaded into an RDBMS.

## Scenario:
Data is available in different types of files. First, it should be gathered into the IDE. To download the different files needed for the project the following code is run in the terminal: wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/

The downloaded file should be unzipped to get the source files using the command: unzip source.zip 

## Set Up:
This project is done as a part of IBM Data Engineering Certification Course. It is developed and executed in a Cloud IDE. In this project, the data is extracted from CSV, JSON, and XML formats. 

To interact with the CSV and JSON files using Python, the pandas library is needed. The following command is run in the terminal to install it: python3.11 -m pip install pandas

The XML library can be used to parse the XML files. 

To access the file format information, glob library is needed.

To create a log file with the date and time information for all the steps, datetime package is needed.

## Code:
- The required libraries pandas, glob, datetime, and xml are imported.
- An empty dataframe is created with the required columns.
- Data is extracted from different file types using glob and the extracted data is concatenated to the empty dataframe.
- The extracted data is then transformed. The height in the extracted data is in inches, and the weight is in pounds. However, the height is required to be in meters, and the weight is required to be in kilograms, rounded to two decimal places. Therefore, the transformation is used to perform the unit conversion for the two parameters.
- The transformed data is loaded into a CSV file so that it can be used to load to a database if necessary.
- A log function is called before and after implementing each step to log the timestamps which are saved into log_file.txt.

## Acknowledgement
[IBM - Python Project for Data Engineering](https://www.coursera.org/programs/computer-science-comps-alternatives-zphna/learn/python-project-for-data-engineering?authProvider=ttu)

