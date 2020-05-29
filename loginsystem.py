from getpass import getpass as gp
def login(store):
  flag=0
  user=input("Enter the username :")
  psw=gp(prompt="Enter password :")
  if user in store:
    print("That user already exist!")
    return 0
  else:
    for i in range(len(psw)):
      if(psw[i]=='@' or psw[i]=='#' or  psw[i]=='$' or  psw[i]=='%' or  psw[i]=='&' or  psw[i]=='*' or  psw[i]=='!'):
        flag+=1
    if(flag>0):
      store[user]=psw
      return 1
    else:
      return 0

global_store=dict()
n=int(input("Enter The no: of Logins :"))
print("Your password must contain a special character!")
i=0
while(i<n):
  if(login(global_store)==1):
   if(i!=(n-1)):
    print("Please Enter username and password of next person")
   i=i+1
  else:
   print("Invalid Username or Password,Try next.")
print("Process Finished")
print(global_store)     
exit= input("Select Enter key")    

