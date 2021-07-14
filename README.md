* Sanic API for detecting the idiom of a sentence

# Run it
```
python src/app.py
```
Open the url http://localhost:8000/health

```
Request: http://localhost:8000/lang 
Method : POST
Body   : application/json
Body example:
{
"sentence": "the sentence you want to know the idiom about"
}
```

# Ask the artifact
```
curl -i -X POST -H "Content-Type: application/json" -d "{\"sentence\": \"how are you doing?\"}" http://localhost:8000/lang
```
