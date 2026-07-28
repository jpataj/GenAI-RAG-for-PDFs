# GenAI RAG FOR PDFs


Overview
This is a Python-based Retrieval-Augmented Generation (RAG) pipeline designed to turn static PDF documents into a searchable, interactive knowledge base. By leveraging vector embeddings and a high-performance local vector database, this tool ensures that local LLM responses are strictly constrained to the context provided in your uploaded files, eliminating generic AI hallucinations.

Key Features
PDF Ingestion & Chunking: Efficiently parses complex PDF structures and breaks them into semantically meaningful segments.
Vector Storage: Utilizes a vector database to store document embeddings for lightning-fast similarity searches.
Strict Context Grounding: Configured to answer questions only using the ingested data. If the answer isn't in the PDFs, the AI will let you know.
Query-to-Source Attribution: Designed to bridge the gap between raw data and actionable insights.



## Prerequisites

* Python 3.6 or later
* pip (Python package installer)
* Rancher Desktop


## Setup
To make it easy for you to get started with python tools, here's a list of recommended next steps.

## Setup

1.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    ```

2.  **Activate the virtual environment:**

    * On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

    * On Windows:

        ```bash
        venv\Scripts\activate
        ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Start docker containers**

    ```bash
    docker compose up
    ```

## Usage

### Create verctors for your PDFs
* To ingest the PDFs, use the following command:

    ```bash
    python ingest.py
    ```


#### Query your documents

    ```bash
    python document_query.py -q "Your question."
    ```

#### Example

    ```bash
    python document_query.py -q "Do I need to audit accounts?"
    ```
