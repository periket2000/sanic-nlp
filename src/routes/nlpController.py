from sanic.exceptions import ServerError
from sanic.response import json
from routes.api import app
from services.nlp import Nlp
import json as jparser

nlp_service = Nlp()

@app.route("/lang", methods=["POST",])
async def lang(request):
    try:
        assert request.body
        request_body = jparser.loads(request.body)
        assert request_body is not None
        return json({"idiom": nlp_service.lang(request_body.get("sentence", None))})
    except (jparser.decoder.JSONDecodeError, AssertionError) as e:
        raise ServerError("Bad request", status_code=400)
