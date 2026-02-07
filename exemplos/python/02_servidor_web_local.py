"""Servidor web local simples para aprendizado.

Objetivos:
- entender o ciclo requisição/resposta HTTP;
- praticar execução local e testes básicos com curl;
- ter uma base pequena para evoluir para APIs e aplicações maiores.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class AprendizadoHandler(BaseHTTPRequestHandler):
    """Handler HTTP com rotas didáticas."""

    def _send_json(self, payload: dict, status: int = 200) -> None:
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _send_html(self, html: str, status: int = 200) -> None:
        data = html.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self) -> None:  # noqa: N802 (padrão da stdlib)
        if self.path == "/":
            self._send_html(
                """
                <html>
                  <head><title>Servidor Web Local</title></head>
                  <body>
                    <h1>Servidor local no ar ✅</h1>
                    <p>Rotas disponíveis:</p>
                    <ul>
                      <li><code>/</code> - página HTML</li>
                      <li><code>/health</code> - status em JSON</li>
                    </ul>
                  </body>
                </html>
                """.strip()
            )
            return

        if self.path == "/health":
            self._send_json(
                {
                    "status": "ok",
                    "service": "servidor-web-local",
                    "timestamp_utc": datetime.now(timezone.utc).isoformat(),
                }
            )
            return

        self._send_json(
            {
                "status": "ok",
                "message": "Rota não mapeada no exemplo didático.",
                "path_recebido": self.path,
                "rotas_disponiveis": ["/", "/health"],
                "dica": "Use uma das rotas disponíveis para testar o servidor.",
            }
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Executa um servidor web local didático")
    parser.add_argument("--host", default="127.0.0.1", help="Host de bind (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=8000, help="Porta HTTP (default: 8000)")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    server = ThreadingHTTPServer((args.host, args.port), AprendizadoHandler)
    print(f"Servidor rodando em http://{args.host}:{args.port}")
    print("Pressione CTRL+C para encerrar.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nEncerrando servidor...")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
