```
**Project Explanation**

This project is building a Student Research Assistance application using Streamlit as UI and the Autogen as agentic AI framework. It aims to help students with their research by:

**Fetching Research Papers**: It uses a DataLoader class to retrieve relevant papers from sources like arXiv based on a user's query.
**Summarizing and Analyzing**: It utilizes a ResearchAgent class to summarize the fetched papers and potentially analyze their advantages and disadvantages.
**Presenting Results**: It leverages Streamlit's interactive UI elements to display the search results, summaries, and analysis to the user in a user-friendly way.
 
# Student Research Assistance

This application is designed to assist students in their research endeavors. It leverages AI and web scraping to fetch relevant research papers, generate concise summaries, and potentially analyze the advantages and disadvantages of the research presented.

## Features

* **Search Functionality:** Users can input a research topic and retrieve related papers from sources like arXiv.
* **AI-Powered Summarization:** Each fetched paper is automatically summarized using a research agent.
* **Advantages/Disadvantages Analysis:** The research agent may also analyze the advantages and disadvantages of the research discussed in the papers.
* **Interactive UI:** The application provides a user-friendly interface built with Streamlit, allowing for easy navigation and exploration of research findings.

## Usage

1. **Clone the repository:** `git clone https://github.com/kumarsudu/autogen_project.git`
2. **Install dependencies:** `pip install -r requirements.txt`
3. **Set the GROQ_API_KEY environment variable:**
   - Create a `.env` file in the project root.
   - Add the line `GROQ_API_KEY=<your_api_key>` to the `.env` file.
4. **Run the application:** `streamlit run app.py`

## XML Sample
http://export.arxiv.org/api/query?search_query=all:machine%20learning&start=0&max_results=5
```
