# USD to Yen Exchange Rate

### Software Design Documentation

Project Name: USD to Yen Exchange Rate<br/>
Development Language: Python<br/><br/>
Developed By: Jones Jenkins<br/><br/><br/><br/>

1. Introduction<br/>
   1. Purpose<br/>
      a. This project documentation contains the Concept, How-To-Steps, and References for the USD to Yen Exchange Rate application. This document is intended for developers and end users.<br/>
   2. Scope<br/>
      a. This application uses web scraping to obtain the exchange rate of USD to Japanese Yen from March 3rd, 2017 to December 18th, 2019. All data was gathered from Quandl. Data gathered is plotted on a line graph.<br/>
   3. Overview<br/>
      a. This document contains:<br/>
         * Concept<br/>
         * How-To-Steps<br/>
         * References<br/>
   4. Resources<br/>
      a. The following resources were used in the production of this software application:<br/>
         * https://www.quandl.com/: Source for financial, economic, and alternative datasets. All exchange rate data was obtained from Quandl.<br/>
         * https://pandas.pydata.org/docs/: pandas reference including user guides, API references, and developer guides.<br/>
2. Concept<br/>
   - This application uses web scraping to show the exchange rate from USD to Japanese Yen from March 3rd, 2017 to December 18, 2019 (the time I lived in Japan). The data is obtained from Quandl and displayed on an easy to read line graph.<br/>
3. How-To-Steps<br/>
   1. Open the project in a Python interpreter and run “exchange_rate.py”.<br/>
   2. A pandas’ dataframe will appear displaying the USD to Japanese Yen exchange rate from March 3rd, 2017 to December 18th, 2019:<br/>
   3. The dates can be changed by modifying line 5 in the code:<br/>
      ~~~
      exchange_rate = quandl.get('FED/RXI_N_B_JA', start_date='2017-3-3', end_date='2019-12-18')<br/>
      ~~~
      *The date format is YEAR-MONTH-DAY<br/>*
