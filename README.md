* Sanic API for detecting the idiom of a sentence

** Run it
```
python src/app.py
```
Open the url http://localhost:8000/health

````
Request: http://localhost:8000/lang 
Method : POST
Body   : application/json
Body example:
{
"sentence": "the sentence you want to know the idiom about"
}
```
