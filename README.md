# Headspin
----------------------------------------------------------------------------------------------------------------------------------------

The following link is used to run and visualize the python code:  http://pythontutor.com/visualize.html#mode=edit



Q1. 

check_date.py


The file check_date.py accepts a date from the user and checks if that date is valid or not.

Step 1.'current_year', 'current_month' and 'current_day' is initialised to present year, month and day respectively.
Step 2.User is asked to input day, month and year.
Step 3.If the date lies between the limit:
                  >>>>Leap year condition is checked and also checks if month = 2 and if day lies below 30.
		            >>>>Then the variable 'valid' is initialised to True.
		  >>>>else if the month=2 and is not a leap year:
		            >>>>Then the variable 'valid' is initialised to True.
                  >>>>else if month lies in [1,3,5,7,8,10,12] and day lies below 32:
                            >>>>variable 'valid' is initialised to True.
                  >>>>else if month lies in [4,6,9,11] and day lies below 31:
                            >>>>variable 'valid' is initialised to True.
                  >>>>else  
                            >>>>variable 'valid' is initialised to False.
                  >>>>The date is checked if it is future date or not.If it is not a future date:
                            >>>>Then variable 'valid' is initialised to True.
                  >>>>else 
                            >>>>The variable 'valid' is initialised to False.
		
Step 4.else
                  >>>>variable 'valid' is initialised to False.
Step 5.If valid=True
                  >>>>then print "VALID DATE"
       else 
                  >>>>print "INVALID DATE"




----------------------------------------------------------------------------------------------------------------------------------------

Q2. 

words_rectangle.py


The file words_rectangle.py accepts a list of words and prints one word a line in the given format

 Eg:  List: [“Hello”,”World”,”in”,”a”,”Frame”]
 
           
            Output:    *********
                       * Hello *
                       * World *
	               * in    *
	               * a     *
	               * frame *
                       *********
                
		
Function used: rect_frame().
Argument of the function: list that is accepted from the user 'element_list'.

Step 1.User is asked to input the number of words 'n'.
Step 2.An empty list is created in the name 'list1'.
Step 3.Inside the for loop that ranges from 1 to n :
                                                   >>>>User is asked to input each word.
                                                   >>>>Each word is appended to the list 'list1'.
                                               
Step 4.The function rect_frame() is called passing the list 'list1'.
Step 5.Working of the function :
                               >>>>Length of the largest word is found out.
                               >>>>Using corresponding print statements, the pattern asked for, is printed.
                       
                       
                       
----------------------------------------------------------------------------------------------------------------------------------------             
Q3.

sum_series.py


The file sum_series.py accepts a number N from the user and prints the following series

Series: 1/1! + 2/2! +3/3! + …. + N/N!

Function used: sum_series().
Argument of the function: the number accepted from the user 'num'.

Step 1.A number 'num' is accepted from the user.
Step 2.The function sum_series() is called.

Step 3.Execution of the function:

                         >>> A variable 'sum' is initialised to 0.
			 >>> Variable 'fact' is initialised to 1.
			 >>> In the for loop that ranges from 1 to num :
			 
			                                                >>> Factorial is calculated.
								        >>> Sum is calculated.
								     
			 >>> Sum is returned to the calling function.
			 
Step 4.Sum of the series is printed..

    
   
    
    
   
![alt text](https://github.com/sherinshoni/Headspin/blob/master/image1.png)

![alt text](https://github.com/sherinshoni/Headspin/blob/master/image2.png)














