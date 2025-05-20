from flask_restx import Api


api = Api(
    title="Sample API",
    version="1.0",
    description="Hello World API via Swagger",
    doc="/api/docs"  # Swagger UI path
)
