#!/bin/bash
# Startup script for backend server

# Load environment variables if .env exists
if [ -f .env ]; then
    export $(cat .env | grep -v '^#' | xargs)
fi

# Start the server
uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}

