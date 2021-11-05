def db(mysql, email, password):

    cursor = mysql.connection.cursor()
    #cursor.execute(''' TRUNCATE user; ''') to empty the table
    

    cursor.execute("SELECT COUNT(email) FROM `user`")
    result=cursor.fetchone()
    next_id = result[0] + 1
    
    cursor.execute(" INSERT INTO `user` VALUES (%s, %s, %s)", (next_id, email, password))
    mysql.connection.commit()
    cursor.close()