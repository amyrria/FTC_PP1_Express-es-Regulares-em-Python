import re
strs = input()
if (strs != " " and strs != "\n"):
  if(re.match(r'\n\d\A', strs)!=True):
   strs.split(" ")  
   if re.match(r'[a-zA-Z](\d)', strs.split()[0]) != False : #verif autor
     numStr = re.findall( r'\d',strs.split()[0])
     alf = re.findall( r'[a-zA-Z]',strs.split()[0])
     tamnum = len (numStr)
     tamalf = len (alf)
     
     if(tamnum <= tamalf): 
       ip = re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', strs.split()[2]) #verif IP
       
       if ip != False:
         email = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',strs.split()[3]) # verif email
         
         if email != False:
           trans = re.match(r'(push|pull|stash|fork)',strs.split()[4])#verif transi
           
           if trans != False:
             repo = re.match(r'([a-z])',strs.split()[5]) #veri repos
             
             
             if repo != False:
                
               s = strs.split()[6]
               x = len (s)
               if x == 32:
                 hashmd = re.match(r'([a-f0-9])', strs.split()[6]) #verf hashmd
                 print (True)

             else: print (False)
           else: print (False)
         else: print (False)
       else: print (False)
     else: print (False)
   else: print (False)
  else: print (False)
else: print (False)
