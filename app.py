from flask import Flask
import os, sys
from src.logger import logging
from src.exception import CustomException

app= Flask(__name__)

@app.route('/',methods = ['GET', 'POST'])
def index():
    try:
        raise Exception ("We are testing second message of logging")
    except Exception as e:
        abc = CustomException(e,sys)
        logging.info(abc.error_message)
        return "Welcome home"

if __name__ == "__main__":
    app.run(debug=True)