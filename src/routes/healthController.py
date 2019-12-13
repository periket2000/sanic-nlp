from sanic.response import text
from routes.api import app

@app.route("/health")
async def health(request):
    return text("OK")

