# Feel free to add as much lines as you want between ## START CODE HERE and ## END CODE HERE.
# Please donot write code outside this boundry or you may fail the test.

# start by importing the necessary documents

import random
import string 

def rank(pwd: str) -> str:
    '''
    Ranker function that ranks the password based on the assigned criteria

    Input: pwd -> character or string

    The following are the requirements for POOR / MODERATE / STRONG password.

    Passwords can contain (not required) any of the following requirements:  
    i. Lower case letters (a – z).       iii) Numbers ( 0 – 9 ).  
    ii. Upper case letters (A – Z).      iv) Symbols ( ! + - = ? # % * @ & ^ $ _ )

    1. A POOR Password is defined as: 
    a. Contains less than 3 from the above 4 items ( i – iv ).  
    b. Less than 8 characters in length.

    2. A MODERATE Password is defined as:  
    a. Contains 3 from the above 4 items ( i – iv )  
    b. Between 8 to 10 characters in length.

    3. A STRONG Password is defined as:  
    a. Meets all 4 of the above items ( i – iv )  
    b. Greater than 10 characters in length.

    Returns: rank -> rank of password; POOR / MODERATE / STRONG
    '''
    ## Start code here
    rank = ""
    
    # Request password from user
    pwd = input("Enter password: ")
    
    # Check for POOR password
    if any(char.islower() for char in pwd) and any(char.isdigit() for char in pwd) and len(pwd) < 8:
        rank = "POOR"
        return rank
    
    # Check for MODERATE password
    if any(char.islower() for char in pwd) and any(char.isdigit() for char in pwd) and any(char.isupper() for char in pwd) and 8 <= len(pwd) <= 10:
        rank = "MODERATE"
        return rank
    
    # Check for STRONG password
    if any(char.islower() for char in pwd) and any(char.isdigit() for char in pwd) and any(char.isupper() for char in pwd) and any(char in string.punctuation for char in pwd) and len(pwd) > 10:
        rank = "STRONG"
        return rank
    ## End code here
    # i use the any() function to check if the password contains at least one lowercase letter, one digit, one uppercase letter,
    #and one symbol from the string.punctuation string. It also uses the islower(), isdigit(), and isupper() string methods 
    #to check the type of each character in the password.
    return rank
   

def option1():
    '''
    Helper function that will be executed when user selects option 1 in the initial case.
    '''
    # Steps to follow:
    # 1. Ask user to rank password from either Users-Pwds.txt or a custom file (second part for bonus only you can skip this)
    # 2. Open the file containing username and password in each line and a file to store the ranked password information(Users-Pwds-Chked.txt).
    # 2.1 ## !IMPORTANT ## Store the list of username,passwords in a variable called usrpwds. 
    # 3. Use the rank() function to rank the password
    # 4. Write to the Users-Pwds-Chked.txt file (username,password,rank) in each line as string. Omit the brackets and only fill up the actual values. 
    # 5. Close necessary files and print to terminal.
    
    ## START CODE HERE
    # Ask user for input file
    filename = input("Enter file name containing username and password: ")

    # Open input file and output file
    with open(filename, "r") as infile, open("Users-Pwds-Chked.txt", "w") as outfile:
    # Read and store lines from input file
            usrpwds = infile.readlines()
    
    # Iterate over lines
    for line in usrpwds:
        # Split line into username and password
        username, password = line.strip().split(",")
        
        # Rank password
        pwd_rank = rank(password)
        
        # Write to output file
        outfile.write(f"{username},{password},{pwd_rank}\n")

        # Print to terminal
    print("Username and password information written to Users-Pwds-Chked.txt")

    ## END CODE HERE

print('#'*80)
 # [INFO] Be sure to change userpwds with the name of variable that you give to the list of passwords
 print('[INFO] '+'Number of passwords checked:',str(len(usrpwds))) 
print('[INFO] '+'The given rankings can be found in Users-Pwds-Chked.txt')
print('#'*80)

def option2():
    '''
    Function to be executed when the user selects option 2 (generate password) in the main loop.
    
    Steps to follow:
        Prompt the user for a username (No more the 20 characters in length).
        Create a Function that will have no (zero) arguments. (generate)
        The Function will randomly generate a STRONG password (Meeting the STRONG Requirments).
        Ask the user if they would like this saved (Y or N).
        If Y: Open the Input file (Users-Pwds.txt) and append the username,password to the EOF.
        If N: Ask if they would like to generate a different password for this user (Y or N).
        Then the program loops back to the menu again offering displaying and offering to select 1, 2 or 3.
    '''

    def generate() -> str:
        '''
        Helper function to generate password.
        Returns: A string pwd with strong ranking in our ranking system.
        '''
        # Starter code, Ualphabets contains all upper case alphabets
        # Lalphabets condains all lowercase alphabets
        # chars contains all special characters and digits contains all numeric digits
        Ualphabets = string.ascii_uppercase
        Lalphabets = string.ascii_lowercase
        chars = string.punctuation
        digits = string.digits
        pwd = ''
        # Hint: user random.choice to select a random Upperalphabet(Ualphabet), Lalphabet, chars, and digits. Join then all together in pwd and check ranking
        # While the required ranking is not met continue joining new Ualphabet, Lalphabet, chars and digits.
        
        ## START CODE HERE
    while not (any(char.islower() for char in pwd) and any(char.isdigit() for char in pwd) and any(char.isupper() for char in pwd) and any(char in string.punctuation for char in pwd) and len(pwd) > 10):
        pwd = ''
        pwd += random.choice(Ualphabets)
        pwd += random.choice(Lalphabets)
        pwd += random.choice(chars)
        pwd += random.choice(digits)
        for i in range(random.randint(4, 8)):
            pwd += random.choice(Ualphabets + Lalphabets + chars + digits)

        ## END CODE HERE
        return pwd
    
    # Ask for username and check 20 character limits

    ## START CODE HERE
    username = input("Enter username (max 20 characters): ")
    while len(username) > 20:
        print("Username must be 20 characters or less.")
    username = input("Enter username (max 20 characters): ")

    ## END CODE HERE

    # Generate the password using generate() and follow the steps as guided in the function header. 

    ## START CODE HERE
    password = generate()
save = input("Save password for user? (Y/N): ")

if save == "Y":
    # Open Users-Pwds.txt file and append username and password
    with open("Users-Pwds.txt", "a") as f:
        f.write(f"{username},{password}\n")
    print("Password saved for user.")
else:
    # Ask if user wants to generate different password
    generate_different = input("Generate different password for user? (Y/N): ")
    if generate_different == "Y":
        password = generate()
        print("New password generated:", password)
    else:
        print("Password not saved for user.")

    ## END CODE HERE

def main():

    print('Welcome to my password ranking program')
while True:
    print('-'*40)
    print('Please select one of 3 options')
    print('option1. Rank password from an existing file \t option2. Generate a strong password \noption3. exit the program')
    inp = input("Enter your option here:")
    
    # try converting the inp to integer form and then check condition if input was either option1, 2, 3 or something else. 
    # exit the loop by using the break command if the user selects 3 other wise use option1() and option 2() function 
     ## START CODE HERE
    try:
        inp = int(inp)
        if inp == 1:
            option1()
        elif inp == 2:
            option2()
        elif inp == 3:
            break
        else:
            print("Invalid option. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid option.")
        ## END CODE HERE


# DONOT TOUCH THESE LINES
if __name__=='__main__':
    main()