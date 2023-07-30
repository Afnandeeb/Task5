#print('afnan')
########Q1
name = input('inter your name : ')
age = input('enter your age : ')
street = input('enter your street : ')
city = input('enter your city : ')
country = input('enter your country : ')
########Q2
my_cv = f'''  "  Name : {name} "
    "  Age : {age} "
" Address :   {street} , {city} ,{country} " '''
print(my_cv)
age1 = int(age)-3
########Q3
pr_cv = f'''"Hello {name} Your age is {age1}, Your Address
  is {street} , {city} ,{country} . " '''
print("\""+'Hello '+"{"+name+"}"+' Your age is '+str(age1)+' Your Address '+"\n"+'is'+street+', '+city+','
 + country+'.'+"\"")
print(pr_cv)
########Q4
type1 = f'''         {type(name)} {type(age)}
         {type(street)} {type(city)}  
             {type(country)}'''
print(type1)
########Q5
p2_cv = f'''Hello '{name}', How Are You? \ """ Your Age Is "{age}""
 + And Your Country Is: {country}'''
print(p2_cv)
########Q6
p3_cv = f'''Hello '{name}', How Are You?\ 
""" Your Age Is "{age}"" + And
 Your City Is: {city}'''
print(p3_cv)
########Q7
name2 = 'Doaa Reem'
first_ch= name2[0]
third_letter = name2[2]
last_letter = (name2[len(name2)-1])
print3 = f''' First Letter Is "{first_ch}"
 Third  Letter Is "{third_letter}"
 
 Last Letter Is "{last_letter}"
'''
print(print3)
########Q8
print(name2[6:10:]+'\n'+name2[:4:]+'\n'+name2[2:7:]+'\n'+name2[8:4:-1]+'\n'+name2[::2])
########Q9
name3 = "$&$Mohammed$&$&"
print(name3.strip('$&'))
########Q10
name4 = "I %7 Python And Although I %7 GSG with \nZakaria"
print(name4.replace('%7','Love'))
########Q11
#capitalize first letter of string
str = 'geeks for geeks'
print(str.capitalize())
#title use to conver first charecter from the all word
print(str.title())
########Q12
num1="4"
num2="56"
num3="963"
num4="385"
num5="8719"
num6="87190"






