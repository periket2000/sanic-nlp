from routes.api import app
import routes.healthController
import routes.nlpController

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
