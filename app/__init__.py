from flask import Flask
from app.config import Config
from app.extensions import api as rest_api
from app.api import api_bp


# アプリケーションファクトリ関数
def create_app():
    """Flaskアプリケーションインスタンスを作成し、設定を適用します。"""
    # Flaskアプリケーションのインスタンスを作成
    app = Flask(__name__)

    # 設定オブジェクトからアプリケーション設定を読み込み
    app.config.from_object(Config)

    # API拡張機能（Flask-RESTXなど）をアプリケーションに初期化・登録
    rest_api.init_app(app)

    # APIブループリントをアプリケーションに登録
    app.register_blueprint(api_bp)

    # 設定済みのアプリケーションインスタンスを返す
    return app
