from app import app, mysql



 


@app.route("/")
def index():
    cursor = mysql.connection.cursor()
    cursor.execute(''' TRUNCATE user; ''')
    cursor.execute(''' INSERT INTO `user` (`id`, `name`, `password`) VALUES ('1', 'my_name', 'my_password'); ''')
    mysql.connection.commit()
    cursor.close()
    return "S"
