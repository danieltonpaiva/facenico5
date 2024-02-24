#!/usr/bin/env python3

from facefusion import core
import sys
import subprocess
if __name__ == '__main__':
    lt_process = subprocess.Popen(["lt", "--port", "8501"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    lt_output, lt_error = lt_process.communicate()
    if lt_process.returncode != 0:
        print("Erro ao iniciar o LocalTunnel:", lt_error)
        exit()

    # Extrair a URL pública do output do LocalTunnel
    public_url = lt_output.decode("utf-8").strip()
    print("Public URL:", public_url)
    core.cli()
