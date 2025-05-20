from app.api.v1.endpoints.chat import ns as chat_ns


def register_namespaces(api):
    api.add_namespace(chat_ns, path=chat_ns.path)
