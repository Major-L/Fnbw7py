#Advanced String Options 

# Indexing in Strings will start at 0 and -1 represents the last character 

message = 'Hello'
print (message [0]) # Prints First Character in the String 
print (message [1]) # Prints Second Character in the String 
print (message [-1]) # Prints Last Characer in the String 


print (len(message)) # When running LEN Function note that a space is also counted as part of the string 


message = ' Hello, World! '
print(message.strip()) #.strip will remove leading and trailing white spaces in a string 
print(message.lower()) #convert all characters to lowercase
print(message.upper()) #convert all characters to uppercase
print(message.split(',')) #Will split a string into a list based on the comma 
print(message.replace("World", "Craig"))# Replacing a string value with a new string walue note either value needs to be in double quotes seperated by a comma 
