import argparse
from typing import Optional
from drillsrs.cmd.command_base import CommandBase
from drillsrs import db


class UpdateTagCommand(CommandBase):
    names = ['edit-tag', 'update-tag']
    description = 'edit a single tag'

    def decorate_arg_parser(self, parser: argparse.ArgumentParser) -> None:
        parser.add_argument('deck', help='choose the deck of the tag')
        parser.add_argument('tag', help='choose the tag to edit')
        parser.add_argument('-n', '--name', help='set the new tag name')

    def run(self, args: argparse.Namespace) -> None:
        deck_name: str = args.deck
        tag_name: str = args.tag
        new_tag_name: Optional[str] = args.name

        with db.session_scope() as session:
            deck = db.get_deck_by_name(session, deck_name)
            tag = db.get_tag_by_name(session, deck, tag_name)

            if new_tag_name is not None:
                tag.name = new_tag_name
