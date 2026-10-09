#!/usr/bin/env bash
set -e

cd "$(dirname "$0")"

mkdir -p db files
chown 1000 db files
docker compose up -d

tries=0
until curl -sf http://localhost:8080/api/v1/info > /dev/null; do
	tries=$((tries + 1))
	if [ "$tries" -ge 30 ]; then
		echo "Vikunja did not answer after 30 seconds. Run: docker logs vikunja" >&2
		exit 1
	fi
	sleep 1
done

curl -si --fail-with-body -X POST http://localhost:8080/api/v1/register \
  -H 'Content-Type: application/json' \
  -d '{"email": "testuser@example.com", "username": "testuser", "password": "testpassword123"}'
