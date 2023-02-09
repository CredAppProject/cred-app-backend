from django.core.management.utils import get_random_secret_key  

def generateEnv():
  """
  Function to generate an .env variable and append the django secret key inside, also it creates the database credential variables.
  """
  with open('.env', 'w') as fp:
    #generate secret key automatically
    key = get_random_secret_key()
    fp.write('SECRET_KEY = "'+key+'"')
    fp.write("DEBUG = ")
    fp.write("NAME = ")
    fp.write("USER = ")
    fp.write("PASSWORD =")
    fp.write("HOST = ")
    fp.write("PORT = ")
    fp.close()

if __name__=="__main__":
    generateEnv()