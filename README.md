# Date Extractor

The project involves extraction of dates from sentences consisting of a date or a keyword relating to some date. The output date is displayed in DD-MM-YYYY format. It displays date for all the tokens that can be tagged to some date.

#### Instructions for Usage 
For using the script, you must have Python's nltk library installed. Use the following command for installing nltk.  
   
    $ sudo pip3 install nltk
    
Clone the repository by using the following command:

    $ git clone https://github.com/ankit0905/date-extractor.git

Git must be installed for the above command to work.
After you have cloned the repo, cd to the cloned directory.

    $ python3 main.py 

When you run, you will get a prompt asking for input. A sample output is displayed below.

	$ python3 main.py
    Enter Input: We went to the mall on 2nd and will go again tomorrow.
    
	tomorrow  =>  07-07-2017
	2nd  =>  02-07-2017
    


## Project Documentation

The project has been done in Python3 and using its modules - datetime, nltk (natural language processing toolkit) and re (regular expressions). 

### Class Reference

The project consists on only one class as for now - namely the CustomDate class.

#### CustomDate Class

**Methods**  
* `__ init __(self, user_input)`
* `convert(self)`
* `getDate(self)`
* `next_weekday(self, d, weekday)`
* `previous_weekday(self, d, weekday)`

**Class Description:**  
The CustomDate class is responsible for converting a date in some format or some keyword relating to a date to DD-MM-YYYY format date. The class uses Python's datetime library in the process.


**Method Documentation**  
1. **__ init __ (self, user_input)**  
   This is the constructor method for the CustomDate class. The only parameter it takes in the user_input which is actually the processed form of user_input after using tokenization and n-grams. In the constuctor, several initializations of the member variables - output_date, date, month, year, errors take place.
   
2. **convert(self)**  
   The method is used only when the user_input passed to the class constructor method consists of numeric values. If there is some valid date, the method will process it accordingly and convert it into DD-MM-YYYY format date.
   
3. **getDate(self)**  
   This is the complementary method of self.convert() - used only when there are no numeric value in the input sequence. It checks if the input is a valid combination of keywords that relates to a date. If a valid date is obtained, it stores the date in DD-MM-YY format in the member variable called self.output_date. Otherwise, the self.errors member varibale in set indicating invalid input.
   
4. **next_weekday(self, d, weekday)**  
   Given some date (d here) and the weekday required, it returns the date in DD-MM-YYYY format for the coming weekday.
   
5. **previous_weekday(self, d, weekday)**  
   Given some date (d here) and the weekday required, it returns the date in DD-MM-YYYY format for the last weekday.
   
___

**NOTE**:
1. The project has scope for further improvements, some of which are:
	* Distinguishing Names from Months  
	  **ex:** "April" can be a name of some person and also is a month name.  
    * Identifying Tense in the sentence for more appropriate outputs.  
      **ex:** Consider the sentence: "I went to the mall on Monday". A valid output here should be the date of last monday, but currently it outputs the date of coming Monday.

2. Any suggestions for improvements are welcome.
