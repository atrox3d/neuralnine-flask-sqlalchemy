flask --app main db init
flask --app main db migrate
flask --app main db upgrade

flask --app main:default_app db init
flask --app main:default_app db migrate
flask --app main:default_app db upgrade