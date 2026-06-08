#!/usr/bin/env python3
"""启动本地 HTTP 服务，在浏览器中打开疫情可视化大屏。"""

import http.server
import socketserver
import webbrowser
from pathlib import Path

PORT = 8765
ROOT = Path(__file__).resolve().parent


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)
    
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()


def main() -> None:
    url = f"http://127.0.0.1:{PORT}/index.html?v=2"
    with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
        print(f"大屏地址: {url}")
        print("按 Ctrl+C 停止服务")
        webbrowser.open(url)
        httpd.serve_forever()


if __name__ == "__main__":
    main()
