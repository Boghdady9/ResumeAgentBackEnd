from data_loader import PDFTextProcessor
from Agent import agent as create_agent

# Load a resume PDF file
processer=PDFTextProcessor("pmres/Alexander_Mejia_Resume.pdf")
cv=processer.process()

# The agent processes the resume and generates a new resume
outcome=create_agent(cv)