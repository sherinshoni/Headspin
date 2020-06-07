current_year=2020
current_month=06
current_day=07

d=input("Enter day in DD format : ")
m=input("Enter month in MM format : ")
y=input("Enter year in YYYY format : ")

if (y>=0 and 0<m<13 and 0<d<32):
	if (y%4==0 and (y%100!=0 or y%400==0) and m==2):
		if d<=29:
	            valid=True
	        else:
		    valid=False
	elif (m in [1,3,5,7,8,10,12] and d<=31):
		valid=True
	elif (m in [4,6,9,11] and d<=30):
		valid=True
	else:
		valid=False
	if (valid==True and y<=current_year and m<=current_month and d<=current_day):
		valid=True
	else:
		valid=False
else:
	valid=False
if (valid==True):
	print("VALID DATE")
else:
	print("INVALID DATE")
		
			
			
