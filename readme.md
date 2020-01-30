3 Check the migrations
python manage.py makemigrations club_management --dry-run --verbosity 3

4 fix for django.db.migrations.exceptions.NodeNotFoundError: Migration club_management.0001_initial dependencies reference nonexistent parent node ('auth', '0012_auto_20200122_1305')

delete virtual, pycache,migrations...create a new virtual.with migrations make sure to migrate explicitly the club_management first `python manage.py makemigratiosn app_name` then also migrate explicitly the app `python manage.py migrate app_name` then migrate normally `python manage.py migrate`