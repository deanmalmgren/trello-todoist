Trello's email reminder system is broken (in my view); it sends email reminders
the day before you specify a due date. I can imagine scenarios where this is
nice, but it is very counterintuitive to me. Trello also doesn't have webhooks
associated with due dates, so services like IFTTT or Zapier are unable to
accomplish the functionality I want: add todoist tasks from Trello on the day
they are due.

`trello-todoist` is a hack to add trello cards to todoist on the day that they
are due. It is intended to be set up as a cronjob with a crontab entry like:

```
53 3 * * * trello-todoist 'trello board' 'trello username' 'todoist project'
```

which runs `trello-todoist` every morning at 3:53 a.m. By default, this adds
all trello cards that are due today from board `trello board` of which `trello
username` is a member as a task to the corresponding `todoist project`.
Depending on the version of `requests` that is installed via python
dependencies, you may also want to use `PYTHONWARNINGS=ignore` somewhere in
your crontab to avoid being sent warnings every time the script is run.

## quick start

1. install `trello-todoist` from pypi:
    ```sh
    pip install trello-todoist
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

1. get your todoist api token from the todoist `Settings` > `Account` > `API
   token`.

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

1. place your todoist api token in a `todoist.json` file in the repository root
   that looks like this:
   ```json
   {
       "token": "your-token"
   }
   ```

1. :boom: For usage instructions, see
  ```sh
  trello-todoist -h
  ```


## development

1. instantiate virtual environment
    ```sh
    mkvirtualenv trello-todoist
    pip install -r requirements/python-dev
    ```

1. follow the quick start instructions above to get your trello and todoist
   credentials.
