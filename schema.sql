CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);

CREATE TABLE items (
    id INTEGER PRIMARY KEY,
    game_name TEXT,
    game_username TEXT,
    availability_time TEXT,
    platform TEXT,
    region TEXT,
    other_info TEXT,
    user_id INTEGER REFERENCES users
);