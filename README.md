# はじめに

- プロジェクト名：業務アシスタントBot
- 担当者：川合、辻野
- 本資料作成日・作成者：2025/05/23・辻野
- 本資料最終更新日・更新者：

## 本案件の目的

- このプロジェクトでは業務のアシスタントbotを作成します。
- このbotは特定のGドライブに保存している資料を参考に質問内容を回答します。

## 用語集

| 用語 | 概要 |
| :--- | :--- |
| FE | フロントエンド |
| BE | バックエンド |
| DB | データベース |
| BQ | Big Query |

## フェーズ分け

| フェーズ | 内容 |
| :--- | :--- |
| フェーズ1 | FE：アプリ（Flask）、BE：アプリ（Flask） |
| フェーズ2 | FE：Slackのワークフロー、BE：アプリ（Flask）|

初期段階では、アプリでチャットボットを作成します。
将来的には、Slackのワークフローを活用します。

### フェーズ1

必要昨日は以下の通りです。
- ログイン管理機能。
- プロンプト自動作成機能。
- 回答用資料の自動文字成型機能。
- プロンプト保存機能。
- 問い合わせ内容をスプレッドに出力する機能。
- Slackチャンネル連携（未決。検討中）

### フェーズ2

フェーズ1との変更点は以下の通りです。
- ログイン機能の削除。ユーザーはSlackのチャンネルで管理。
- Slackのワークフロー作成。ワークフローの内容からSlackに問い合せ。APIを経由してSlackに回答。

### 重要事項

フェーズ2に移行する場合、画面は不要となります。
よって、フェーズ1では後々、APIとして利用する意識をした作りにする必要があります。

## 技術選定

- 使用技術

| 項目 | 値 | 備考 |
| :--- | :--- | :--- |
| プログラミング言語 | python | 3.12.1以上 |
| フレームワーク | Flask | ー |
| データベース | なし | ー |
| BigQuery | なし | ー |
| インフラ | GCP | Cloud DNS、Cloud Run、VPN、OAuth2.0、Cloud Monitoring、Cloud Logging |
| 外部API | Slack API | 通知用、アプリ連携用 |
| 外部API | Gemini API | 質問内容生成用 |
| その他 | Docker | Cloud Run用 |

## アーキテクチャ

### フェーズ1

[アーキテクチャ図リンク](https://drive.google.com/file/d/1NzfxS4oN1SjFcCfQ4y6oAmfIPMiWKdEH/view?usp=sharing)

社内向けアプリで小規模のため以下、仕様で考えております。
- フロントエンドサーバーとバックエンドサーバーを分けない。モノリシックアーキテクチャ。
- DBサーバー、BQ連携は2025年05月23日現在不要。
- ログイン条件ははメールアドレスの後が「@sungrove.co.jp」であるか判別。
- 利用ログはspread sheetに吐き出す。

### フェーズ2

2025年05月23日現在、未作成


## フォルダ構成

今回、flaskを利用します。
フォルダの構造は以下の通りです。
こちらはあくまで参考で動的に変更する可能性が高いです。

```bash
project-root/
│
├── docker/                                 # Docker関連ファイル
│   ├── local/                              # ローカル開発環境用
│   │   ├── be/
│   │   │   └── Dockerfile                  # PythonバックENDアプリケーション用 Dockerfile
│   │   └── mysql/
│   │       └── Dockerfile                  # MySQLデータベース用 Dockerfile
│   ├── docker-compose.yml                  # ローカル開発環境用 Docker Compose定義
# │   └── nginx/                              # Nginx関連ファイル (現在は未使用)
# │       └── nginx.conf                      # Nginxの設定ファイル（リバースプロキシ、SSL対応など）
│
├── src/                                    # Pythonバックエンドアプリケーションのソースコード
│   ├── app/                                # Flaskアプリケーション全体のルート
│   │   ├── __init__.py                     # アプリケーションファクトリ初期化処理
│   │   ├── config.py                       # 開発・本番環境ごとの設定値定義
│   │   ├── extensions.py                   # Flask拡張機能（DB, CORS, Swagger等）の初期化
│   │   │
│   │   ├── api/                            # REST API層
│   │   │   ├── __init__.py                 # APIモジュール初期化
│   │   │   ├── namespace.py                # APIネームスペース登録（Flask-RESTX）
│   │   │   ├── common/                     # API内部専用の共通処理群（認証、バリデーション等）
│   │   │   │   ├── decorators.py           # 認可・ロギング用デコレータ
│   │   │   │   └── validators.py           # 入力チェックなどの共通バリデータ
│   │   │   └── v1/                         # APIバージョン別モジュール（v1対応）
│   │   │       ├── __init__.py             # v1 APIの初期化とルーティング
│   │   │       ├── endpoints/              # 実際のAPI定義（各機能単位）
│   │   │       │   ├── chat.py             # チャット機能API
│   │   │       │   └── auth.py             # 認証・ログインAPI
│   │   │       ├── schemas/                # リクエスト/レスポンススキーマ定義（Swagger用）
│   │   │       │   └── __init__.py
│   │   │       └── departments/            # 部署ごとに異なるBotロジックを格納
│   │   │           ├── sales/
│   │   │           │   └── __init__.py     # 営業部門専用Bot初期化
│   │   │           └── hr/
│   │   │               └── __init__.py     # 人事部門専用Bot初期化
│   │   │
│   │   ├── frontend/                       # HTMLベース画面（Jinja2テンプレート）
│   │   │   ├── views/                      # 画面ルーティング（Blueprintベース）
│   │   │   │   ├── __init__.py
│   │   │   │   └── home.py                 # ホーム画面用ルート
│   │   │   ├── common/                     # テンプレート内専用の共通処理（フィルタなど）
│   │   │   │   ├── filters.py              # 日付・フォーマットなどテンプレートフィルタ
│   │   │   │   └── helpers.py              # UI表示補助用のヘルパー関数
│   │   │   ├── templates/                  # Jinja2テンプレートファイル
│   │   │   │   ├── base.html               # レイアウト共通ベーステンプレート
│   │   │   │   └── chat.html               # チャット画面テンプレート
│   │   │   └── static/                     # 静的ファイル格納（CSS、JS、画像）
│   │   │       ├── js/
│   │   │       ├── css/
│   │   │       └── images/
│   │   │
│   │   ├── common/                         # アプリ全体で共通利用するロジックやユーティリティ
│   │   │   ├── chatbot_core.py             # チャットボットの主要ロジック
│   │   │   └── utils.py                    # 汎用関数・共通処理など
│   │   │
│   │   │
│   │   ├── models/                         # ORMモデル定義（SQLAlchemy等）
│   │   │   ├── __init__.py
│   │   │   ├── user.py                     # ユーザーモデル
│   │   │   └── chat.py                     # チャットメッセージモデル
│   │   │
│   │   ├── services/                       # サービス層：業務処理ロジック
│   │   │   ├── __init__.py
│   │   │   ├── auth_service.py             # 認証・ユーザー管理処理
│   │   │   └── chat_service.py             # チャット処理サービス
│   │   │
│   │   ├── wsgi.py                         # GunicornなどからのWSGI起動ポイント
│   │   └── runner.py                       # バッチ処理やCLI起動用スクリプト
│   │
│   ├── project/                            # アプリケーション起動や統合ポイント
│   │   ├── __init__.py
│   │   ├── wsgi.py                         # GunicornなどからのWSGI起動ポイント
│   │   └── runner.py                       # バッチ処理やCLI起動用スクリプト
│
│   └── migrations/                         # AlembicによるDBマイグレーション管理
│       ├── env.py                          # Alembicの設定エントリーポイント
│       ├── script.py.mako                  # マイグレーションスクリプトのテンプレート
│       └── versions/                       # 各バージョンのマイグレーション履歴ファイル
│
├── tests/                                  # pytest用のテストコード群（src外に配置）
│   ├── test_api/                           # API関連のユニットテスト
│   ├── test_views/                         # フロント画面の表示ロジックのテスト
│   └── conftest.py                         # pytest用の共通フィクスチャ定義
│
├── docs/                                   # ドキュメントエリア（設計書や仕様など）
│   └── openapi.yaml                        # OpenAPI (Swagger) 定義ファイル
│
├── .env.example                            # 環境変数のサンプルファイル（本番前に.envへコピー）
├── .gitignore                              # Gitで無視すべきファイル・フォルダ定義
├── requirements.txt                        # Pythonパッケージの依存関係リスト
├── setup.py                                # Pythonパッケージ定義ファイル（オプション）
└── README.md                               # プロジェクトの概要・利用方法説明
```

- 設計のポイント
    - Swagger対応：API用。
    - フロント分離設計：将来フロントエンドが不要になる可能性があるため。
    - API分離：src/app/api/ に完全REST設計で切り分ける。
    - バージョン管理：src/api/v1/のようにメジャーバージョンを管理。
    - 部署ごとのBotロジック切替：src/app/api/v1/departments/ に部署別の処理を分離する。

## 起動方法

### ローカル環境（個人PC）
- ブラントの習得：git clone [リポジトリURL]
- docker/local/へ移動：cd docker/local
- 初回のdocker-composeの実行：docker-compose -f .\docker-compose.local.yml up --build
- 二回目移行のdocker-composeの実行：docker-compose -f .\docker-compose.local.yml up
- サイトを表示（Swagger画面）：http://127.0.0.1:8000/api/docs
- サイトを表示（画面サンプル）：http://127.0.0.1:8000/v1/chat/

### 開発環境

2025年05月23日現在、未作成

### 本番環境

2025年05月23日現在、未作成
