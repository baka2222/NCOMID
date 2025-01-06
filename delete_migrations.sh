#!/usr/bin/bash

echo "Привет, это скрипт для удаления миграций"

set -e

find . -path "./venv" -prune -o -path "*/migrations/*.py" -not -name "__init__.py" -exec rm -f {} \;

find . -path "./venv" -prune -o -path "*/migrations/*.pyc" -exec rm -f {} \;

echo "Миграции удалены."
