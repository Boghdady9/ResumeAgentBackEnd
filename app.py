from flask import Flask, request, Response
from data_loader import PDFTextProcessor
from Agent import agent as create_agent

# Initialize the Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Resume Transformer API"

@app.route('/process_resume', methods=['POST'])
def process_resume():
    # Check if the request contains files
    if not request.files:
        return Response("No file provided", status=400)

    # Get the first file from the request (you can extend this if you have multiple files)
    file = list(request.files.values())[0]
    if not file:
        return Response("No file provided", status=400)

    # Process the file
    processor = PDFTextProcessor(file)
    cv = processor.process()

    # Run your agent on the processed resume
    outcome = create_agent("Can you transform this into a PM Resume" + cv)

    # Return the outcome as plain text
    return Response(outcome, mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True, port=5000)