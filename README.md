

## getting started

1. instantiate virtual environment
    ```sh
    mkvirtualenv trello-todoist
    pip install -r REQUIREMENTS
    ```

1. get your trello api key and secret [from here](https://trello.com/app-key)
   and get your oauth tokens:
    ```sh
    export TRELLO_API_KEY=your-key
    export TRELLO_API_SECRET=your-secret
    export TRELLO_EXPIRATION=never
    python -m trello.util
    # follow instructions
    ```

1. place your trello credentials in a `trello.json` file in the repository root
   that looks like this:
    ```json
    {
        "api_key": "your-key",
        "api_secret": "your-secret",
        "token": "your-oauth-token-key",
        "token_secret": "your-oauth-token-secret"
    }
    ```

1. get your todoist api token from the todoist `Settings` > `Account` > `API
   token`.

1. place your todoist api token in a `todoist.json` file in the repository root
   that looks like this:
   ```json
   {
       "token": "your-token"
   }
   ```

1. :boom:
   ```sh
   ./make_due_cards_todoist_tasks.py
   ```
