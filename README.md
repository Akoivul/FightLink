# FightLink

### Concept
An app that helps players find opponents for fighting games with small player bases. Users can create a listing that includes their availability to play and allows them to match up with other players for online matches.

### App features
- The user can create an account and log in to the app.
- The user can add, edit and delete listings. Each listing includes the name of a fighting game, the time the user is available to play and their in-game username so they can be invited.
- The user can view other listings added to the app.
- The user can search for listings by game name or search for user profiles.
- The app includes user profiles that display the fighting games users play and their listings.
- The user can assign one or more tags (rank, region, platform) to their listing.
- The user can sign up to play with another player by interacting with their listing.

### Current status
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
