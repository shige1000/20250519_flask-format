from flask_restx import Namespace, Resource


ns = Namespace("v1/chat", description="Chat-related operations")


@ns.route("/")
class HelloWorld(Resource):
    def get(self):
        return {"message": "Hello, World from API!"}
