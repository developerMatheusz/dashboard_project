#!/bin/bash

echo "Parando containers antigos..."
docker compose down

echo "Buildando imagem..."
docker compose build --no-cache

echo "Subindo aplicação..."
docker compose up -d

echo "Deploy finalizado."
