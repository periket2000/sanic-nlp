from sanic.response import json
from routes.api import app
from services.nlp import Nlp
import json as jparser

nlp_service = Nlp()

@app.route("/lang", methods=["POST",])
async def lang(request):
    try:
        assert request.body
        # Tweet can come in several ways, so first decode/ignore and then json parse strict False
        request_body = jparser.loads(request.body.decode('utf-8', 'ignore'), encoding='utf-8', strict=False)
        assert request_body is not None
        return json({"idiom": nlp_service.lang(request_body.get("sentence", None))})
    except (jparser.decoder.JSONDecodeError, AssertionError) as e:
        return json(
            {'error': 'Bad request'},
            headers={'X-Served-By': 'sanic'},
            status=400
        )
    except Exception as e:
        return json(
            {'error': 'Internal error'},
            headers={'X-Served-By': 'sanic'},
            status=500
        )
