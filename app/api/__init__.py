from flask import Blueprint
from app.extensions import api
from app.api.namespace import register_namespaces

# 'api' という名前でBlueprintオブジェクトを作成。
# このブループリント内のルートはすべて '/api' というURLプレフィックスを持つ。
api_bp = Blueprint(
    "api",  # ブループリントの名前 (Flask内部での識別子)
    __name__,  # ブループリントが定義されているパッケージまたはモジュール名
    url_prefix="/api"  # このブループリントの全ルートに適用されるURLの接頭辞
)

# Flask-RESTXのApiインスタンスに、定義された複数の名前空間を登録する。
# register_namespaces関数内で、具体的な名前空間の登録処理が行われる。
register_namespaces(api)
