# Automated Pitch Deck Evaluation System

## Project Overview
This Carnegie Mellon Heinz College Capstone Project was developed for MMC Ventures Fund, a healthcare-focused VC firm.  
The project automated the first-line investment screening of startup pitch decks, which previously required 2–3 hours per application and created scalability bottlenecks.  

## Impact Summary

### Situation
MMC Ventures relied on manual, subjective, and time-consuming evaluation of pitch decks, limiting scalability as application volumes grew.

### Task
Design and prototype an automated screening system that reduces evaluation time while preserving quality, consistency, and fairness.

### Action
- Built a rule-based scoring engine applying standardized rubrics across 7 categories and 21 sub-criteria  
- Automated data ingestion and extraction from pitch decks and forms  
- Integrated external APIs (LinkedIn, Crunchbase, SerpAPI) for web-verified founder, market, and competitor insights  
- Prototyped a hybrid evaluation pipeline (rule-based plus RAG with LangChain and vector DB for retrieval-augmented feedback)  
- Designed a scorecard generator with category-level scoring and flagging  

### Result
- 95% reduction in review time (2–3 hours to 5–10 minutes per application)  
- $43,200 annual cost savings in analyst hours  
- Enabled 10x more applications processed with the same resources  
- Improved consistency, reduced bias, and increased decision-making transparency  

## Tech Stack

### Core Frameworks
- Python for automation, data ingestion, scoring logic  
- LangChain with RAG for retrieval-augmented evaluation and feedback  
- Docker for containerized deployment  

### Data and APIs
- SerpAPI for Google search results integration  
- Crunchbase API for company and founder data  
- LinkedIn via RapidAPI for founder background verification  

### Infrastructure
- MongoDB Atlas for structured pitch storage  
- Redis for asynchronous task management  
- Cloud hosting (AWS or GCP) for backend and React frontend  
- Security with authentication, SSL, access control  

## Deliverable Impact
- Reduced manual review workload by 1,200 hours annually  
- Saved over $43K per year in operational costs  
- Increased screening capacity 10x with no added headcount  
- Delivered a production-ready blueprint for MMC Ventures’ future intelligent screening pipeline  

## Key Learning
Automation can drastically improve efficiency and scalability, but human oversight remains essential for nuanced VC decisions.  
The system acts as a first filter, empowering analysts to focus on high-value due diligence.
