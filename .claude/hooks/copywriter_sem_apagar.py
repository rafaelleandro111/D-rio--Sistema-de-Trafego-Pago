"""Guarda do Copywriter: bloqueia qualquer comando ou escrita que apague arquivo.

Recebe o pedido do Claude Code em JSON (stdin). Sai com código 2 pra bloquear
(a mensagem no stderr é o que o agente vê) e 0 pra liberar.
"""
import json
import os
import re
import sys

APAGAR = re.compile(
    r"(?ix)"
    r"(^|[\s;&|(`])(rm|rmdir|rd|del|erase|unlink|shred|truncate)(\s|$)"
    r"|remove-item|clear-content|\bri\s"
    r"|git\s+(clean|rm|reset\s+--hard|checkout\s+--|restore)"
    r"|shutil\.rmtree|os\.remove|os\.unlink|os\.rmdir|\.unlink\(|\.rmdir\("
    r"|\bmv\b|move-item|\bmove\s"            # mover pode sobrescrever outro arquivo
    r"|(^|[^>2&])>(?!>)\s*[^\s&|]"           # '>' sobrescreve arquivo (>> acrescentar é liberado)
    r"|-delete\b|--force\b"
)


def bloquear(msg):
    print(f"Bloqueado pela guarda do Copywriter: {msg}. Esse agente não pode apagar nem "
          "sobrescrever arquivos. Salve com um nome novo ou peça ao chefe.", file=sys.stderr)
    sys.exit(2)


def main():
    dados = json.load(sys.stdin)
    ferramenta = dados.get("tool_name", "")
    entrada = dados.get("tool_input", {}) or {}

    if ferramenta in ("Bash", "PowerShell"):
        if APAGAR.search(entrada.get("command", "")):
            bloquear("comando que apaga, move ou sobrescreve arquivo")

    if ferramenta == "Write":
        caminho = entrada.get("file_path", "")
        if caminho and os.path.exists(caminho):
            bloquear(f"o arquivo já existe ({caminho})")

    sys.exit(0)


if __name__ == "__main__":
    main()
