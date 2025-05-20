# はじめに

- プロジェクト名：
- 担当者：
- 本資料作成日・作成者：
- 本資料最終更新日・更新者：

## 本案件の目的

## 用語集

| 用語 | 概要 |
| :--- | :--- |
| FE | フロントエンド |
| BE | バックエンド |
| DB | データベース |
| BQ | Big Query |

## フェーズ分け

### フェーズ1

### フェーズ2

### 重要事項

## 技術選定

- 使用技術

| 項目 | 値 | 備考 |
| :--- | :--- | :--- |
| プログラミング言語 | python | 3.12.1以上 |
| フレームワーク | Flask | - |
| データベース | なし | - |
| BigQuery | なし | - |
| インフラ | GCP | Cloud DNS</br>Cloud Run</br>VPN</br>OAuth2.0</br>Cloud Monitoring</br>Cloud Logging |
| 外部API | Slack API | 通知用 |
| 外部API | Gemini API | 質問内容回答用 |
| その他 | Docker | Cloud Run用 |

## アーキテクチャ

### フェーズ1


### フェーズ2

## フォルダ構成

今回、flaskを利用します。
フォルダの構造は以下の通りです。

```bash
project-root/
│
├── docker/
│   ├── Dockerfile                    # アプリケーションのビルド・実行環境定義
│   ├── docker-compose.yml            # 複数コンテナの構成・連携を定義
│   └── nginx/                        # Nginxの設定ファイル格納ディレクトリ
│       └── nginx.conf                # Nginxの設定（リバースプロキシ、SSL等）
│
├── app/
│   ├── __init__.py                   # アプリケーションファクトリとアプリ初期化
│   ├── config.py                     # 環境別設定（開発/テスト/本番）の定義
│   ├── extensions.py                 # Flask拡張の初期化（Flask-RESTX, SQLAlchemy等）
│
│   ├── api/                          # 完全REST化されたAPIエンドポイント（Swagger対応）
│   │   ├── __init__.py               # APIモジュールの初期化
│   │   ├── namespace.py              # APIネームスペース登録（Flask-RESTX）
│   │   ├── v1/                       # バージョンごとのAPI管理（将来v2も追加可）
│   │   │   ├── __init__.py           # v1 APIの初期化と名前空間登録
│   │   │   ├── endpoints/            # エンドポイントごとのAPI
│   │   │   │   ├── chat.py           # チャット関連APIエンドポイント定義
│   │   │   │   └── auth.py           # 認証関連APIエンドポイント定義
│   │   │   └── schemas/              # リクエスト/レスポンスのスキーマ
│   │   │       └── __init__.py       # APIモデル定義（Swagger用）
│
│   ├── frontend/                     # Flask上でテンプレートとして動作するFE
│   │   ├── views/                    # HTML返す画面表示用ロジック（APIを内部で呼び出す）
│   │   │   ├── __init__.py           # フロントエンドBlueprintの登録
│   │   │   └── home.py               # ホーム画面やその他のページルートハンドラ
│   │   ├── templates/                # Jinja2テンプレートディレクトリ
│   │   │   ├── base.html             # 共通レイアウト用ベーステンプレート
│   │   │   └── chat.html             # チャット画面用テンプレート
│   │   └── static/                   # 静的ファイル格納ディレクトリ
│   │       ├── js/                   # JavaScriptファイル（APIとの通信など）
│   │       ├── css/                  # CSSスタイルシート
│   │       └── images/               # 画像ファイル（ロゴ、アイコン等）
│
│   ├── common/                       # 共通機能（チャットロジック、ユーティリティ）
│   │   ├── chatbot_core.py           # チャットボットのコア機能実装
│   │   └── utils.py                  # 汎用ユーティリティ関数
│
│   ├── departments/                  # 部署ごとのBotロジック（sales/hrなど）
│   │   ├── sales/                    # 営業部門用チャットボットロジック
│   │   │   └── __init__.py           # 営業部門モジュール初期化
│   │   └── hr/                       # 人事部門用チャットボットロジック
│   │       └── __init__.py           # 人事部門モジュール初期化
│
│   ├── models/                       # DBモデル
│   │   ├── __init__.py               # モデルパッケージ初期化
│   │   ├── user.py                   # ユーザーモデル定義
│   │   └── chat.py                   # チャットメッセージモデル定義
│   │
│   └── services/                     # 業務ロジック
│       ├── __init__.py               # サービスパッケージ初期化
│       ├── auth_service.py           # 認証・認可サービス
│       └── chat_service.py           # チャット処理サービス
│
├── migrations/                       # データベースマイグレーション管理
│   └── versions/                     # マイグレーションスクリプト格納ディレクトリ
│
├── tests/                            # テストコード
│   ├── test_api/                     # API機能のテスト
│   │   ├── __init__.py               # APIテストパッケージ初期化
│   │   ├── test_chat_api.py          # チャットAPIのテスト
│   │   └── test_auth_api.py          # 認証APIのテスト
│   ├── test_views/                   # フロントエンドのテスト
│   │   ├── __init__.py               # ビューテストパッケージ初期化
│   │   └── test_home.py              # ホーム画面のテスト
│   └── conftest.py                   # Pytestの共通フィクスチャと設定
│
├── docs/                             # OpenAPI仕様書・設計ドキュメントなど
│   └── openapi.yaml                  # OpenAPI/Swagger仕様定義
│
├── .env.example                      # 環境変数サンプルファイル
├── .gitignore                        # Gitで無視するファイル・ディレクトリ指定
├── requirements.txt                  # Pythonパッケージ依存関係
├── setup.py                          # Pythonパッケージ化の設定
└── wsgi.py                           # WSGIアプリケーションエントリーポイント
```

- メモ
- API分離：app/api/ に完全REST設計で切り分ける。将来FastAPIとうに移行が簡単。
- Swagger対応：Flask-RESTX 使えば /docs でSwagger UIを自動生成。
- フロント分離設計：今は frontend/ 以下でFlaskテンプレート動かすけど、VueやReactに移行する時もAPI呼び出し構造だから簡単。
- バージョン管理：api/v1/ という構造にしとくことで、将来のAPI互換性管理が楽。

## 起動方法

### ローカルPC（Dockerなし）

のちのち、Dockerを利用して実行します。

```bash
pip install requirements.txt

pip
```
