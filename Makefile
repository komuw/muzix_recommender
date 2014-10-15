shell:
	@python manage.py shell_plus --settings=settings.development

run:
	@pip install -r requirements/development.txt &
	@python manage.py validate --settings=settings.development &
	@python manage.py collectstatic --noinput --settings=settings.development  &
	@python manage.py migrate --settings=settings.development --verbosity 3 &
	@python manage.py runserver 0.0.0.0:5700 --settings=settings.development 

mk:
	@python manage.py makemigrations --settings=settings.development 

# use sqlite for tests, its faster.
test:
	@python manage.py test core --settings=settings.development

flush:
	@python manage.py flush --no-initial-data --settings=settings.development

ssh:
	@ssh -o ServerAliveInterval=20 root@someIPaddress

deploy:
	@ansible-playbook devops/site.yml -i devops/inventory/staging --limit=all -vvvv
