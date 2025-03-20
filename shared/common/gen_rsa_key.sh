#!/usr/bin/env bash
set -euxo pipefail

openssl req -x509 -newkey rsa:2048 -keyout private.key -out public.crt -days 365 -nodes