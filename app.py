## Define the streamlit application

import streamlit as st
import os
from dotenv import load_dotenv
from agents import ResearchAgent # Calling the ResearchAgent class from agents.py file
from data_loader import DataLoader # Calling the DataLoader class from data_loader.py file
load_dotenv()

## Streamlit UI Title
st.title("Student Research Assistance")

# Retrive the API key from environment variables
groq_api_key = os.getenv("GROQ_API_KEY")

# Check if the API key is set , else stop execution
if not groq_api_key:
    st.error("GROQ_API_KEY is missing. Please set it in the environment variables.")
    st.stop()

# Initialize AI Agents for summarization and analysis
resAgent = ResearchAgent()


# Initialize DataLoader for fetching research paper
data_loader = DataLoader()

# Input field for the user to enter a research topic
input_query = st.text_input("Enter a research topic:")

# When the user clicks "Search"
if st.button("Search"):
    with st.spinner("Fetching research papers..."): # Display a loading pinner

    # Fetch research papers from ArXiv and Google Scholar
        arxiv_papers = data_loader.fetch_arxiv_papers(input_query)
        all_papers = arxiv_papers

        # if no paper are found, display an error message
        if not all_papers:
            st.error("Failed to fetch papers. Try again!")
        else:
            processed_papers = []

            # Process each paper: generate summary and analyze advantages / disadvantages

            for paper in all_papers:
                summary = resAgent.summarize_paper(paper['summary']) # Generate Summary
                adv_dis = resAgent.analyze_advantages_disadvantages(summary) # Analyze advantages and disadvantages

                processed_papers.append({
                    "title": paper["title"],
                    "link": paper["link"],
                    "summary": summary,
                    "advantages_disadvantages": adv_dis
                })
            
            # Display the processed research papers
            st.subheader("Top Research Papers:")
            for i, paper in enumerate(processed_papers, 1):
                st.markdown(f"### {i}. {paper['title']}")  # Paper title
                st.markdown(f"[Read Paper]({paper['link']})")  # Paper link
                st.write(f"**Summary:** {paper['summary']}")  # Paper summary
                st.write(f"{paper['advantages_disadvantages']}")  # Pros/cons analysis
                st.markdown("---")  # Separator between papers

