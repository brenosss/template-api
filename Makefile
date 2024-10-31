run:
	cd app && docker compose -p app --env-file .env -f compose.yml up -d --remove-orphans

add-dependency:
	cd app && docker compose run web bash -c "poetry add $(dep)"

rebuild:
	cd app && docker compose build

restart:
	cd app && docker compose restart

restart-web:
	cd app && docker compose restart web

down:
	cd app && docker compose down

integration-tests:
	cd integration_tests && docker compose -p integration_tests up web --build -d --remove-orphans
	sleep 5
	cd integration_tests && docker compose up tests --build
	
