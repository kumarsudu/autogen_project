## Define the streamlit application

import streamlit as st
import os
from dotenv import load_dotenv
from agents import ResearchAgent # Calling the ResearchAgent class from agents.py file
from data_loader import DataLoader # Calling the DataLoader class from data_loader.py file
load_dotenv()

print("Working fine in app.py")