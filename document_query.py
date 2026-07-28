import os
#supressing absl and grpc error logs
os.environ["ABSL_LOG_LEVEL"] = "3"
os.environ["GRPC_VERBOSITY"] = "ERROR"
from imports import ContextualRAG
import requests
import argparse
import json





crag = ContextualRAG(database = 'RAG_DB', 
          collection='PDF_DOCUMENTS', 
          recreate_collection=False,
          chunk_size=500,
          chunk_overlap=0
         )

rights = {
    'Customers/All': 1,
    'Employees': 2,
    'IT Staff': 4,  
    'HR Staff': 8,
    'Security Team': 16
}


def main():
    """Main function to parse arguments"""

    
    
    
    requests.get('http://localhost:11434').content

    # TODO: Uncomment below to start LLM server if not running
    # TODO: Handle exceptions better to run the pull only if connection error occurs
    # headers = {'Content-Type': 'application/json'}  
    # data = {"name":"llama3", "stream":False}
    # url = 'http://localhost:11434/api/pull'
    # requests.post(url, headers=headers, json=data).text

    # try:
    #     requests.get('http://localhost:11434').content
    # except requests.exceptions.ConnectionError:
    #     print('Starting local LLM server...')
    #     headers = {'Content-Type': 'application/json'}  
    #     data = {"name":"llama3", "stream":False}
    #     url = 'http://localhost:11434/api/pull'
    #     requests.post(url, headers=headers, json=data).text
    # except Exception as e:
    #     print(f"An unexpected error occurred: {e}")

    # --- Argument Parsing ---
    parser = argparse.ArgumentParser(description="Find answers for your PDF Documents questions.")
    parser.add_argument("-q", "--question", help="Question you want to ask.", required=True)
    args = parser.parse_args()

    question = args.question

    print(f'\nQuestion: {question}\n\n Answer:')

    try:
        headers = {'Content-Type': 'application/json'}
        data = {"model":"llama3", "prompt": "What is 42?", "stream":False}
        requests.post('http://ollama:11434/api/generate', headers=headers, json=data ).content
    except Exception as e:
        print('Starting local LLM server...')
        headers = {'Content-Type': 'application/json'}  
        data = {"name":"llama3", "stream":False}
        url = 'http://localhost:11434/api/pull'
        requests.post(url, headers=headers, json=data).text

    crag.query(question, include_attributions=True, num_results=20, rights=255)



if __name__ == "__main__":
    main()
