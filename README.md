# Malicious_URL_zdm_new_features
## About 
This project extends previous work by extracting new kind of features.<br>
Two main goals of this project are:
1. Improve the excellent results achieved by previous work.
2. Extract new robust features to reduce dependency in non-robust features.

## Our New Features
Our new additional features are in addition to the features from previous work.<br>
The idea is to take a domain and get all possible information about it with API request sent to "BuiltWith" site. <br>
This request returns text contains information about available tools in site, number and kind of analytics tools, number of JavaScripts and much more, check it out https://api.builtwith.com/. <br>
Our assumption is that benign URL will probably contain much more content (analytics tools, JavaScripts and more) than malicious URL. <br>
Therefore we thought this is a good idea of extracting new features.<br>
Inside Tools directory you can find builtwith.py script you have the ability to give it list of domains and it will check for each domain if available for check in BuiltWith, if no it will mark it with "-1". <br>
In builtwithExtractor.py script we go over all avaiable domains and creating a txt file for each domain contains all information for BuiltWith API request. <br>
After that we go over and extract two features- Length of the content and number of analytics tool. <br>
We did very basic work and a great extension can be exploring the content and then extracting new kind of features.

## Notes
1. API used in the code might be out of date, you can get your own api easily from https://api.builtwith.com/.
2. Malicious URLs are getting blocked very quickly therefore you must use crawler from previous work and renew the Data.
3. The final dataset we've created can be found in superFinal.csv file. 
4. Many paths specified in the script need to be tuned to your relevant paths, read the comments in code and change it to use. 

