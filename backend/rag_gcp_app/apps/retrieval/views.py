from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

from langchain.llms import openai
from langchain.chains import llm_checker 
# Create your views here.

llm = openai.OpenAI(openai_api_key="")
chain = llm_checker(llm = llm ) 
