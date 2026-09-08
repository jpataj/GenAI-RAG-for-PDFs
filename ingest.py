import re
from pathlib import Path
from pypdf import PdfReader
from imports import ContextualRAG



crag = ContextualRAG(database = 'PDF_RAG', 
          collection='NIST', 
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


path = Path('docs/')
files = list(path.glob('*.pdf'))

for file in files:        
    document = PdfReader(file)
    name = file.name
    crag.store_embeddings(document, document_name=name, rights=rights['Customers/All'])
