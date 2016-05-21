#!/usr/bin/env python

"""This script uses the Trello configuration in trello.json and uses that to
put cards that are due today as todoist tasks.
"""

import os
import json
import argparse
import datetime

from trello import TrelloClient
from todoist import TodoistAPI


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument(
    'trello_board_name',
    help='name of the Trello Board that we are parsing'
)
parser.add_argument(
    'trello_username',
    help='username of the person whose cards we want to populate'
)
parser.add_argument(
    'todoist_project_name',
    help='name of the todoist project to which due cards should be assigned'
)
args = parser.parse_args()

# get credentials and instantiate the client
this_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(this_dir, 'trello.json')
with open(filename, 'r') as stream:
    credentials = json.load(stream)
client = TrelloClient(**credentials)

# find the appropriate board
board = None
for _board in client.list_boards():
    if _board.name == args.trello_board_name:
        board = _board
        break
if board is None:
    raise ValueError('board "%(trello_board_name)s" not found' % vars(args))

# find the appropriate member
member = None
for _member in board.get_members():
    if _member.username == args.trello_username:
        member = _member
        break
if member is None:
    raise ValueError('member "%(trello_username)s" not found' % vars(args))


def is_due_today(card, today=None):
    today = today or (datetime.date.today() - datetime.timedelta(seconds=86400))
    return card.due_date and card.due_date.date() == today

# find all of the cards on this board that are owned by this user and are due
# today
cards_due_today = []
for card in board.all_cards():
    if member.id in card.member_ids and is_due_today(card):
        cards_due_today.append(card)

print cards_due_today

# create an authenticated instance of the TodoistAPI
filename = os.path.join(this_dir, 'todoist.json')
with open(filename, 'r') as stream:
    credentials = json.load(stream)
todoist_api = TodoistAPI(**credentials)

# get the project id
todoist_api.projects.sync()
project_id = None
for project in todoist_api.projects.all():
    if project['name'] == args.todoist_project_name:
        project_id = project['id']
if project_id is None:
    raise ValueError((
        'did not find todoists project "%(todoist_project_name)s"'
    ) % vars(args))
print project_id

# add due cards as todoist tasks
for card in cards_due_today:
    todoist_api.add_item(
        '[%(name)s](%(url)s)' % vars(card),
        project_id=project_id,
        day_order=0,
        date_string='today',
    )
