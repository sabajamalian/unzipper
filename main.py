from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import PlainTextResponse
import zipfile
import io
import os

app = FastAPI()

@app.post("/extract-archive", response_class=PlainTextResponse)
async def extract_archive(file: UploadFile):
    if not file.filename.endswith('.zip'):
        raise HTTPException(status_code=400, detail="Only ZIP files are supported")
    
    try:
        content = await file.read()
        zip_buffer = io.BytesIO(content)

        with zipfile.ZipFile(zip_buffer, 'r') as zip_ref:            
            all_contents = []
            
            for file_info in zip_ref.infolist():
                if not file_info.is_dir():
                    file_name = file_info.filename
                    
                    with zip_ref.open(file_info) as f:
                        file_content = f.read().decode('utf-8', errors='replace')
                    all_contents.append(f"=== File: {file_name} ===\n{file_content}\n")
            
            return "\n".join(all_contents)
            
    except zipfile.BadZipFile:
        raise HTTPException(status_code=400, detail="Invalid ZIP file")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 