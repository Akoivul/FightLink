import db

def get_all_classes():
    sql = "SELECT title, value FROM classes ORDER BY id"
    result = db.query(sql)

    classes = {}
    for title, value in result:
        classes[title] = []
    for title, value in result:
        classes[title].append(value)

    return classes

def add_item(game_name, game_username, availability_time, availability_start, availability_end, other_info, user_id, classes):
    sql = """INSERT INTO items (game_name, game_username, availability_time, availability_start, availability_end, other_info, user_id)
             VALUES (?, ?, ?, ?, ?, ?, ?)"""
    db.execute(sql, [game_name, game_username, availability_time, availability_start, availability_end, other_info, user_id])
    
    item_id = db.last_insert_id()

    sql = "INSERT INTO item_classes (item_id, title, value) VALUES (?, ?, ?)"
    for class_title, class_value in classes:
        db.execute(sql, [item_id, class_title, class_value])

def add_signup(item_id, user_id, signup):
    sql = """INSERT INTO signups (item_id, user_id, game_username)
             VALUES (?, ?, ?)"""
    db.execute(sql, [item_id, user_id, signup])

def get_signups(item_id):
    sql = """SELECT signups.game_username, users.id user_id, users.username
             FROM signups, users
             WHERE signups.item_id = ? AND signups.user_id = users.id
             ORDER BY signups.id DESC"""
    return db.query(sql, [item_id])

def remove_signup(item_id, user_id):
    sql = "DELETE FROM signups WHERE item_id = ? AND user_id = ?"
    db.execute(sql, [item_id, user_id])

def get_classes(item_id):
    sql = "SELECT title, value FROM item_classes WHERE item_id = ?"
    return db.query(sql, [item_id])

def get_items():
    sql = "SELECT id, game_name, availability_time FROM items ORDER BY id DESC"
    return db.query(sql)

def get_item(item_id):
    sql = """SELECT items.id,
                    items.game_name,
                    items.game_username,
                    items.availability_time,
                    items.availability_start,
                    items.availability_end,
                    items.other_info,
                    users.id user_id,
                    users.username
             FROM items, users
             WHERE items.user_id = users.id
             AND items.id = ?"""
    result = db.query(sql, [item_id])
    return result[0] if result else None

def update_item(item_id, game_name, game_username, availability_time, availability_start, availability_end, other_info, classes):
    sql = """UPDATE items SET game_name = ?,
                              game_username = ?,
                              availability_time = ?,
                              availability_start = ?,
                              availability_end = ?,
                              other_info = ?
                          WHERE id = ?"""
    db.execute(sql, [game_name, game_username, availability_time, availability_start, availability_end, other_info, item_id])

    sql = "DELETE FROM item_classes WHERE item_id = ?"
    db.execute(sql, [item_id])

    sql = "INSERT INTO item_classes (item_id, title, value) VALUES (?, ?, ?)"
    for class_title, class_value in classes:
        db.execute(sql, [item_id, class_title, class_value])

def remove_item(item_id):
    sql = "DELETE FROM signups WHERE item_id = ?"
    db.execute(sql, [item_id])
    sql = "DELETE FROM item_classes WHERE item_id = ?"
    db.execute(sql, [item_id])
    sql = "DELETE FROM items WHERE id = ?"
    db.execute(sql, [item_id])

def find_items(query):
    sql = """SELECT DISTINCT items.id, items.game_name
             FROM items
             LEFT JOIN item_classes ON items.id = item_classes.item_id
             WHERE items.game_name LIKE ? OR items.other_info LIKE ? OR item_classes.value LIKE ?
             ORDER BY items.id DESC"""
    like = "%" + query + "%"
    return db.query(sql, [like, like, like])