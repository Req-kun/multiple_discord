import discord
from discord.ext import commands
from typing import Union, Optional
from asyncio import sleep


async def add_reactions(self: discord.Message, reactions: list):
    for reaction in reactions:
        await self.add_reaction(reaction)

discord.Message.add_reactions = add_reactions
commands.Context.add_reactions = add_reactions


def message(content: str, *, tts: bool = False, embed: discord.Embed = None, file: discord.File = None, files: list[discord.File] = None, delete_after: float = None, nonce: int = None, allowed_mentions: discord.AllowedMentions = None, reference: Union[discord.Message, discord.MessageReference] = None, mention_author: Optional[bool] = None):
    dict = {
        'content': content,
        'tts': tts,
        'embed': embed,
        'file': file,
        'files': files,
        'delete_after': delete_after,
        'nonce': nonce,
        'allowed_mentions': allowed_mentions,
        'reference': reference,
        'mention_author': mention_author
    }
    return dict

async def sends(self, messages: list, *, cool: Union[int, float] = 0):
    for message in messages:
        await self.send(content=message['content'], tts=message['tts'], embed=message['embed'], file=message['file'], files=message['files'], delete_after=message['delete_after'], nonce=message['nonce'], allowed_mentions=message['allowed_mentions'], reference=message['reference'], mention_author=message['mention_author'])
        await sleep(cool)

discord.TextChannel.sends = sends
commands.Context.sends = sends


def field(*, name: str = '', value: str = '', inline: bool = True):
    dict = {
        'value': value,
        'name': name,
        'inline': inline
    }
    return dict

def add_fields(self, fields: list):
    for field in fields:
        self.add_field(name=field['name'], value=field['value'], inline=field['inline'])

discord.Embed.add_fields = add_fields
