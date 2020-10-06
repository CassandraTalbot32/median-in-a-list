Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import statistics
>>> 
>>> my_list = [75, 89, 36, 47. 1024, 456, 987]
SyntaxError: invalid syntax
>>> my_list = [75, 57, 89, 47, 1024, 456, 987]
>>> 
>>> statistics.median(my_list)
89
>>> 
