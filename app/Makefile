#
# This Makefile contains commands which are run inside the Docker containers,
# I do not recommend invoking these directly - see Makefile at project root instead.
#
worker-local:
	watchmedo \
	auto-restart \
	--directory /app/ \
	--recursive \
	--pattern '*.py' \
	-- \
	./manage.py qcluster


worker-prod:
	echo "Starting remote syslog" && \
	touch /var/log/celery.log && \
	remote_syslog \
	--hostname "${PAPERTRAIL_HOSTNAME}" \
	--dest-port "${PAPERTRAIL_PORT}" \
	--dest-host "${PAPERTRAIL_URL}" \
	--pid-file /var/run/remote_syslog.pid \
	./manage.py qcluster


web-local:
	./manage.py runserver 0.0.0.0:8000


web-prod:
	echo "Starting tempapp app as `whoami`" && \
	echo "Starting remote syslog" && \
	mkdir -p /var/log/gunicorn && \
	touch /var/log/gunicorn/access.log && \
	touch /var/log/gunicorn/error.log && \
	remote_syslog \
	--hostname "${PAPERTRAIL_HOSTNAME}" \
	--dest-port "${PAPERTRAIL_PORT}" \
	--dest-host "${PAPERTRAIL_URL}" \
	--pid-file /var/run/remote_syslog.pid \
	/var/log/gunicorn/access.log \
	/var/log/gunicorn/error.log && \
	echo "Running migrations" && \
	./manage.py migrate && \
	echo "Starting gunicorn" && \
	gunicorn tempapp.wsgi:application \
	--name tempapp \
	--workers 2 \
	--bind 0.0.0.0:8005 \
	--capture-output \
	--log-level info \
	--error-logfile /var/log/gunicorn/error.log \
	--access-logfile /var/log/gunicorn/access.log


# Lint Python code
lint:
	flake8 \
		--max-line-length=90 \
		--exclude='*migrations*' \
		.
	isort \
		-l 90 \
		--diff \
		--check-only \
		--skip migrations


# Auto-format Python code
format:
	black \
		--line-length 90 \
		--exclude "migrations/" \
		--skip-string-normalization \
		.
	isort \
		-l 90 \
		--skip migrations \
		--apply

test:
	pytest -s -vv --reuse-db
