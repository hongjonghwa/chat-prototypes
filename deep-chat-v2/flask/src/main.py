
from dotenv import load_dotenv
import os
from flask_cors import CORS
from flask import Flask, request


load_dotenv()
print(os.environ.get("LANGCHAIN_TRACING_V2"))
print(os.environ.get("LANGCHAIN_API_KEY"))


app = Flask(__name__)

# this will need to be reconfigured before taking the app to production
cors = CORS(app)