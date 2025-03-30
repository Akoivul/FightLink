import db

def add_item(game_name, game_username, availability_time, availability_start, availability_end, platform, region, other_info, user_id):
    sql = """INSERT INTO items (game_name, game_username, availability_time, availability_start, availability_end, platform, region, other_info, user_id)
             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""
    db.execute(sql, [game_name, game_username, availability_time, availability_start, availability_end, platform, region, other_info, user_id])

def get_items():
    sql = "SELECT id, game_name FROM items ORDER BY id DESC"
    return db.query(sql)

def get_item(item_id):
    sql = """SELECT items.id,
                    items.game_name,
                    items.game_username,
                    items.availability_time,
                    items.availability_start,
                    items.availability_end,
                    items.platform,
                    items.region,
                    items.other_info,
                    users.id user_id,
                    users.username
             FROM items, users
             WHERE items.user_id = users.id
             AND items.id = ?"""
    return db.query(sql, [item_id])[0]

def update_item(item_id, game_name, game_username, availability_time, availability_start, availability_end, platform, region, other_info):
    sql = """UPDATE items SET game_name = ?,
                              game_username = ?,
                              availability_time = ?,
                              availability_start = ?,
                              availability_end = ?,
                              platform = ?,
                              region = ?,
                              other_info = ?
                          WHERE id = ?"""
    db.execute(sql, [game_name, game_username, availability_time, availability_start, availability_end, platform, region, other_info, item_id])

def remove_item(item_id):
    sql = "DELETE FROM items WHERE id = ?"
    db.execute(sql, [item_id])