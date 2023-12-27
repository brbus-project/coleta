from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.
import time

from cities.sao_paulo import sao_paulo
from cities.df import df
from cities.rio import rio
from cities.curitiba import curitiba

try:
	sao_paulo()
	df()
	rio() 
	curitiba()
except Exception as e:
	print(f"Error on main: {e}")