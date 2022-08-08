# Goals List
#### Video Demo:
https://youtu.be/c2BEme0XxCw

#### Description:
Goals List. Living without a vision is similar to living without a purpose — it is essentially a waste of time.However, when you stop to set goals and think about the things that you want, you stop living on auto-pilot and start living a conscious life. This app will help you get started on setting goals for yourself. The opprotunity to create and track your daily/monthly goals. Options to add and delete them.

The Project is based on Python, Flask, Html, CSS, JavaScript, Bootstrap & Jinja.
The User signs up, gets success to its account, where he can create personal list of goals, track them, add more and delete.
"Success" notifications included (when the user inserts appropriate to the parameters/demands information);
"Error" notification included (when the user inserts appropriate to the conditions information), using flash.

The main folder are included:
Static (index.js, style.css);
Templates (__init__.py, auth.py, database.db, models.py, views,py);
main.py;
models.py includes the scheme of the database storing;
views.py includes .routes-blocks with "Home", "Profile", "Home Creation" pages (json included for goals deletion);
required files .md, txt.

__init__.py combines all neccessary database, tools & frameworks imports.
main.py is the main running file, which refers __init__.py for running the app (imports create_app function from __init__.py).
auth.py includes the logical code of "sign up", "log in", "log out" (using flash partly)

### How to setup and istall the app properly
#### You should have the latest version of Python installed

pip install -r requirements.txt

### Run the App
python main.py

### View the app
Go to http://127.0.0.1:5000