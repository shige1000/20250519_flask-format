import os
import sys

# このファイル (wsgi.py) があるディレクトリ (src/project) の
# 2つ上のディレクトリ (プロジェクトルート) をsys.pathに追加します。
# これにより、'from src.app import create_app' が正しく動作するようになります。
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src.app import create_app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
