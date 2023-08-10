cube=float(input())
num_guess=0
low=0
high=cube
guess=(high+low)/2.0
if(cube<=-1):
   while(abs(guess**3-cube)>=0.001):
     if guess**3<cube :
        high=guess
     else :
        low=guess
     guess=(high+low)/2.0
     num_guess+=1
if( cube<0 and cube>-1):
    high=1
    guess=(high+low)/2.0
    while(abs(guess**3-abs(cube))>=0.001):
     if guess**3<abs(cube):
        low=guess
     else :
        high=guess
     guess=(high+low)/2.0
     num_guess+=1
    guess=-guess  
if( cube<1 and cube>0):
    high=1
    guess=(high+low)/2.0
    while(abs(guess**3-cube)>=0.001):
     if guess**3<cube :
        low=guess
     else :
        high=guess
     guess=(high+low)/2.0
     num_guess+=1     
if( cube>=1):
    while(abs(guess**3-cube)>=0.001):
     if guess**3<cube :
        low=guess
     else :
        high=guess
     guess=(high+low)/2.0
     num_guess+=1
print ('num_guess=',num_guess ) 
print  (guess,'is close to the cube root of',cube)







