# Archive Extractor API


```bash
pip install -r requirements.txt
```

```bash
python main.py
```

The server will start on `http://localhost:8000`.

## API Usage

### Endpoint: POST /extract-archive

This endpoint accepts a ZIP file upload and returns the concatenated contents of all files within the archive.

#### Request
- Method: POST
- Content-Type: multipart/form-data
- Body: Form data with a file field named 'file' containing a ZIP file

#### Response
- Content-Type: text/plain
- Body: Concatenated contents of all files in the archive, with each file's content preceded by its filename

#### Example using curl:
```bash
curl -X POST -F "file=@your_archive.zip" http://localhost:8000/extract-archive
```
