<h2> Command Line Interface - Password Generator</h2>

This is my mini MDG project for password generator. To access this CLI you need to open the folder containing 
the exe file at terminal and type

    ./pswdgen
 

command to see the prompt.




The commands for the CLI:

<b>gen</b> :  This command will generate password and store it in a binary non-readable format. The hashed value
     along with date and time of generation will be stored in a text file.
     
<h3><i>'purpose' is a crucial parameter for all the passwords stored as it serves as its access key.</i></h3>

    You should always state a unique purpose of each of your password as it will be the key to access
    your password in case you forget.
     
     
<b>acs</b>: This command will show your password stored in .dat file. To access password enter your purpose 
    along with command.


<b>updt</b>: This command allows you to remodify the password already saved for a particular purpose. This command will take purpose as parameter and new password as input and register the change in hash file and update the password in .dat file.

<b>desc</b>: Shows the entire binary file.



The 'hashed_script.txt" serves as a record file for all the passwords ever generated and the updates performed on them. 

The 'pass_file.dat' will include all your passwords along with particular purpose the user has assigned o it.
