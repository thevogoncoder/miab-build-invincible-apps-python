start-server:
	uv run temporal server start-dev --ui-port 8080 --db-filename temporal.db

start-worker:
	uv run python iplocate/worker.py

start-app:
	uv run python iplocate/app.py