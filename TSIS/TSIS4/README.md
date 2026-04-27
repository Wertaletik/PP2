# TSIS 4 Snake — PostgreSQL version

## Install
```bash
pip install -r requirements.txt
```

## Database setup
Edit `config.py` with your PostgreSQL database name, user, password, host, and port.

The game creates these tables automatically on startup:
- `players`
- `game_sessions`

If you prefer to create them manually in pgAdmin4, run `schema.sql`.

## pgAdmin4 actions needed
1. Create a PostgreSQL database for the project, for example `snake_game`.
2. Create or reuse a PostgreSQL user and make sure it can connect to that database.
3. Update `config.py` (or environment variables) so the credentials match your setup.
4. Run `schema.sql` if you want to create the tables manually before launching the game.

## Run
```bash
python main.py
```
