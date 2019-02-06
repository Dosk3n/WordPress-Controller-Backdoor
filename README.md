# WordPress-Controller-Backdoor
A post exploitation back door for wordpress servers

## The purpose of this tool
If you are in a situation where you managed to get in to a wordpress site and got access to the server this "back door" will allow you to get back in to wordpress control panel if they change their password.

## How it works
After you have gained access to a server with wordpress installed, or gained access to the server by going through wordpress, then you can fill out the fields in the python file to match that of the wp-config.php file and upload the php file. Any time the user changes their wordpress password you can use this program to get the current hash of the user, or replace the current hash of the user with one that would be used for the word password. You can then log in, do what you wish and then use this tool to set the hash back to what the user was using.
