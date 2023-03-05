import os
from django.core.management.utils import get_random_secret_key  

def generateEnv():
  """
  Function to generate an .env variable and append the django secret key inside, also it creates the database credential variables.
  """

  #returns if .env already exist.
  if os.path.exists(".env"):
    print(".env variable already exist")
    return

  with open('.env', 'w') as fp:
    #generate secret key automatically
    key = get_random_secret_key()
    fp.write('SECRET_KEY = "'+key+'"')
    fp.write('\nDEBUG = ')
    fp.write('\nNAME = ')
    fp.write('\nDB_USER = ')
    fp.write('\nPASSWORD = ')
    fp.write('\nHOST = ')
    fp.write('\nPORT = ')
    print(".env generated at "+os.getcwd())
    fp.close()

if __name__=="__main__":
    generateEnv()