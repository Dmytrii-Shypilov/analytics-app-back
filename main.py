from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from io import StringIO


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins or specify allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods or specify allowed methods
    allow_headers=["*"],  # Allow all headers or specify allowed headers
)

# file arg should be of the same name as 'file' in formData
@app.post('/upload')
async def get_file(file: UploadFile):
    print("REQUEST")
    try:
        # Read the file content as bytes
        content_bytes = await file.read()
        

        # Decode bytes to string
        content_str = content_bytes.decode('utf-8')
        print(content_str)
        # Use StringIO to convert the string to a file-like object
        csv_file = StringIO(content_str)

        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(csv_file)

        table = df.to_json(orient='records')


        return table
    
    except Exception as e:
        print(f"Error: {e}")
        return {"error": str(e)}