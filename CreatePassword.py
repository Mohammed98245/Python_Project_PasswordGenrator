import string    #importing stringle module to get string constant
import random    #module implements pseudo-random number generators for various distributions
import pickle    #The pickle module implements binary protocols for serializing and de-serializing
info={}     #creating a empty dictionary
# with open("game.p","br") as readfile:  #opening the file in read mode
#     info = pickle.load(readfile)

if __name__ == "__main__":
    s1 = string.ascii_lowercase  #Give lower ascii which is in format abcd....
    s2 = string.ascii_uppercase  #Give upper ascii which is in format ABCD....
    s3 = string.digits           #Give digit '0123456789'
    s4 = string.punctuation      #Give punctuation '!@#$^*..'
    len_password = int(input("Enter password length:\n")) #take the length from the user
    s = []   #creating a blank list
    s.extend(list(s1))  #concatenating the string s1 and converting into list
    s.extend(list(s2))  #concatenating the string s2 and converting into list
    s.extend(list(s3))  #concatenating the string s3 and converting into list
    s.extend(list(s4))  #concatenating the string s4 and converting into list
    print("Your password is: ")
    password=("".join(random.sample(s,len_password))) #taking the random sample from s
    print(password)

Answer=input("would you like to keep this password:") # taking the input user
if("yes" in Answer):  #checking the condition
  account_name = input("Enter the account name:")
  info[account_name]=password
  with open("game.p","bw") as filewrite:  #opening the file and writing in it
      pickle.dump(info,filewrite,protocol=2)
else:
  print("OK")