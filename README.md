# Brazil Phone Codes

## Video Demo: (https://youtu.be/8Crj6WOpa34)
### Description:
    This program was made to help identify phone codes in Brazil, more specificaly, the location of faux messages on Whatsapp.
    It's main objective is to help people not to be scammed when they recieve a message from someone in their "family" asking for money by recognizing that the phone that is sending them those messages, although has the profile picture of someone from their family, doesn't have the same phone code that person would be using, even in the happenstance of having to change their number.
### Breaking it down:
#### **"get_brazil_phone_codes()":**
    this function returns a dictionary containing all states of Brazil, their phone codes and the phone code of the capital city of each state.
#### **"search_by_state(brazil_phone_codes, state)":**
    This function searches for the phone code of a particular state in the 'brazil_phone_codes' dict. It takes two parameters: brazil_phone_codes' (the dict returned by the function 'get_brazil_phone_codes') and 'state' (the name of the state it should search for). It returns 'True' if the state is found and 'False' otherwise.
#### **'search_by_capital(brazil_phone_codes, capital)':**
    This function searches for the phone code of a capital city in the 'brazil_phone_codes' dict. Taking again two parameters: 'brazil_phone_codes' and 'capital' (the name of the capital city to search for). Returns 'True' if the capital city is found and 'False' otherwise.
#### **'search_by_phone_code(brazil_phone_codes, phone_code)':**
    This function searches for the state related with the phone code in the 'brazil_phone_codes' dict. It takes two parameters: 'brazil_phone_codes' and 'phone_codes'. Returns 'True' if the phone code is found and 'False' otherwise.
#### **'main()':**
    The 'main' function is the entry point of the code. It contains a while loop that will, repeatedly, prompt the user to enter a state, capital city or phone code to search for. The user's input will be stored in the 'option' variable. The program then will check the value of 'option' and call the appropriate function based on the user's input. If the user enters the state option, the function 'search_by_state()' is called and the phone codes related with that state are printed to the terminal. If the user choose the 'capital' option, the function 'search_by_capital()' is called and the phone code related with that capital is printed to the terminal. If the user choose the 'phone code' option, the function 'search_by_phone_code()' is called and the state related to that phone code is printed to the terminal. If the user's input is not recognized, the program will print an error message and contine to prompt the user for a new input. The while loop will continue to run until the user chose the option to 'Exit' the program.
### TODO:

#### Usage:
##### Run the program python script project.py by python
    python project.py
##### Select one of the four options for search
    1. Search by state (only acronym)
    2. Search by capital
    3. Search by phone code
    4. Exit (to close the program)
##### Example with system output
    Choose an option:
    1. Search by State
    2. Search by capital
    3. Search by phone code
    4. Exit
    Enter the number of your option: 1
    Enter the state: SP
    Phone codes for state SP: ['11', '12', '13', '14', '15', '16', '17', '18']



#### Conclusion:
    The first objective of the program was to build a library to capture all the 5.370 cities in Brazil and their specific phone code. Following up with it I noticed that without a GPS to support it with  triangulation, it would be ineffective, since many cities in a state can have the same phone code. The next issue was the amount of data and the lack of trustworthy sources. With that in mind I decided to decrease it's reach in order to understand how to make it work and possibly work on it again in the future when I have more tools on my disposition.

    The final design for the program came after a debate I had with a friend about the issues I was having when trying to get an output from the system when I changed the type of information I was giving it as an input. That way I created the option menu, making it easier to code and also easier for the user to work with it.

