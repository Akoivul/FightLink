# FightLink

### Concept
An app that helps players find opponents for fighting games with small player bases. Users can create a listing that includes their availability to play and allows them to match up with other players for online matches.

### App features
- The user can create an account and log in.
- The user can add, edit and delete listings.
- The user can view listings added by other users.
- The user can search for listings.
- The user can view other users' profiles
- The user can assign classifications to a listing (platform, region)
- The user can sign up to play via another user's listing

## Installing the app

Install the `flask`-library:

```
$ pip install flask
```

Create tables for the database:

```
$ sqlite3 database.db < schema.sql
$ sqlite3 database.db < init.sql
```

To run the app:

```
$ flask run
```
