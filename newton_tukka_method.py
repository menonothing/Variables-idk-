#do proper algebra and sorting

#get input of equation and variable currently single variable
print("enclose functions in brackets, (sinx) and not sinx, so as to not confuse computer between genuine variables(s,i,n,x) and functions")
print("x(sinx) and not xsinx")
print("(sinx**2) for sin of (x raised to power two) and not sin of x, sin squared=> (sinx)**2")
print("(x**2sinx) for x raised to power 2 sinx, and not (x**2)sinx which means x raised to power 2 multiplied by sinx, please be concise so as to not get wrong results")
fx= input("enter equation  ")
Fx=[]
recognisedfuctions=["sin","cos","tan","cot","sec","cosec","log"]

#to convert string into usable format(list) and getting expressions together(not including exponents)    
c=0
bracket=""
h=0
isfunction=""
for i in fx:
    if h!=0:
         h=h-1
         continue
    elif i==" ":
        continue
    elif i=="(":
        c=c+1
        bracket= bracket+"("
        if c>1:
            bracket= bracket + i       
    elif i==")":     
        bracket=bracket+")"
        c=c-1
        if c==0:
            exp=fx.index(i)
            try:
                while fx[exp+1]==" ":
                   exp=exp+1
                expstring=fx[exp+1]+fx[exp+2]
                h=h+2
                if "**" not in expstring:
                   Fx.append(bracket)
                else:
                   bracket=bracket+expstring
                   for j in fx[exp+3:len(fx)]:
                       if j==" ":
                             Fx.append(bracket)      
                             break
                       bracket=bracket+j
                       h=h+1    
            except IndexError:
                 continue
            bracket=""
        else:
            bracket=bracket + i
    elif c>0:
        bracket=bracket + i
    else:
        try:
            index=fx.index(i)
            isfunction=fx[index]+fx[index+1]+fx[index+2]
            if isfunction.lower() not in recognisedfuctions and isfunction[1:3]!="**":
                Fx.append(i)
            else:
                h=h+2
                for j in fx[index+3:len(fx)]:
                    h+=1
                    if j=="(":
                        c=c+1
                        isfunction=isfunction+"("  
                    elif j==")":
                        
                         c=c-1
                         isfunction=isfunction+j
                         if c==0:
                              Fx.append(isfunction)
                              break
                    elif j==" " and c==0:
                         Fx.append(isfunction)
                         
                         break
                    elif c==0:
                        if j=="+" or j=="-":
                             Fx.append(isfunction)    
                             h-=1
                             break
                    else:
                        isfunction=isfunction+j
                           
        except IndexError:
            continue

#to get list of expression=[term,term,term,term,[sign,number,function,function,function] 
c=0
f=[]
terms=[]
if Fx[0].isalnum():
    Fx.insert(0,"+")
Fx.append("+")#to get the last term to register in terms, as +/- is the indicator for end of term and trigger to dump value
f.append(Fx[0])
for i in Fx[1:len(Fx)]:
    if i=="+" or i=="-":        
        terms.append(f.copy())        
        f.clear()
        f.append(i)
    else:
        f.append(i)
del(f)
del(Fx)#to save space ig

#[[+,3,4,sinx],[-,9,7,(67+97)]] current scenario, modify downwards to unify functions, [3,4]=>[34]
#convert symbol and numbers at first positions to int along with joing ex-3,4=>34
#for this stuff, add index+index(+1)+index(+2) etc till numbers
#iterate to find other numbers in list and convert them too(not part of bracket) but stuff like [8,7,(sinx),1,9]=>[87,(sinx),19]=>[1653,(sinx)]
#multiply all such numbers and put it in front of bracket

x=True
while x: 
    #run is_brac_or_exponent
    x=False#done by is_brac_or_exponent
    break

def is_brac_or_exponent(listElement):
    #check if bracket[")" in listElement] and index of outmost bracket end point
    #check if exponent["**" in listElement] present, and index of outmost exponent
    #compare index of both to find which one to call using if statement
    #call respective exponents or brackets functions
    #if no bracket and exponent left=> x=False
    return(None)

def brackets(list_of_terms_elementTerm,index_of_bracket, index_of_term):
    #just open bracket in the outmost place, that you can split as it is and not mess maths
    #(x+(y))=> x, +, (y)
    #bracket multiplication a subpart of this function
    #copy all other elements in list other than the list you are working on and make a list to dump it in LISTbrac,--
    #-- find int and actually multiple if intergers present
    #LISTbrac .append all separated elements and .copy() to add elements into terms list 
    #pop list_of_terms_elementTerm
    return(None)

def exponents(list_of_terms_elementTerm,index_of_exponent,index_of_term):
    #just pop out whole number exponents=exponent and pop out** too
    #something flag like if non whole number exponents so that you can use it later if you decide for graph to solve and find similarities 
    #LISTexpo copies the thing, then pop list from terms list
    #i=0
    #while exponent>0:  exponent-=1  terms.insert(index_of_term+i,LISTexpo)  i+=1
    return(None)
    
#before sorting, simplify expressions into smallest possible, ie def bracket and def exponents;;;;   sort function
#since terms are sorted and symbilified, act of adding common terms is simplified