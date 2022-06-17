# Setup Env
python3.8 -m venv venv
source venv/bin/activate
export PYTHONPATH=$PWD

###########
# Avataars project
# https://github.com/fangpenlin/avataaars-generator

# Install Avataars, will start on port 3006
# Avataar server
$ git clone git@github.com:gkoberger/avataaars.git
$ cd avataaars
$ npm install
$ npm start

# Test Avataars
http://127.0.0.1:3006/?avatarStyle=Transparent&topType=ShortHairShortCurly&accessoriesType=Prescription01&hairColor=Black&facialHairType=BeardMajestic&facialHairColor=Black&clotheType=BlazerSweater&eyeType=Surprised&eyebrowType=RaisedExcited&mouthType=Twinkle&skinColor=Yellow%27



# Freeze requirements
$ pip freeze > requirements.txt

# Install Requirements
$ pip install --upgrade pip
$ pip install -r requirements.txt

# Git Commands
git add <DIR>
git commit 
git push

#Start Everything
source venv/bin/activate
export PYTHONPATH=$PWD

# Drop and recreate DB
sudo su postgres
psql
drop database your_database_name;
create database your_database_name with owner user_you_use_in_django;
\q
exit

#example
postgres=# drop database nfrank;
DROP DATABASE
postgres=# create database nfrank with owner nfrank;
CREATE DATABASE
postgres=# \q

# Generate Language file
python manage.py makemessages -a  --settings=config.settings.local

# Data Dump
#python manage.py dumpdata --settings=config.settings.local --indent 2 > ./data/dbDataDump.json

# Load Storie Objects when the data tables are empty
python manage.py loaddata --settings=config.settings.local ./data/stories_Objections.json


# Run the app
python manage.py collectstatic --settings=config.settings.local
python manage.py makemigrations --settings=config.settings.local
python manage.py migrate --settings=config.settings.local
python manage.py createsuperuser --settings=config.settings.local
python manage.py runserver --settings=config.settings.local

# Admin: nfrank:nfrank

# Test in the browser
http://localhost:8000/


