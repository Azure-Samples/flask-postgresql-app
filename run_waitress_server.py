import sys, os  
from waitress import serve  
sys.path.insert(0, './app')
from app import APP

serve(APP,host="0.0.0.0",port=os.environ["PORT"])  