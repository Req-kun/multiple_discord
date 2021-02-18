# 使い方

## message

```py
message(引数...)
```

指定可能な引数 - discord.TextChannel.sendと同じ

## sends

```py
await discord.TextChannel.sends([message, message2...], cool=1)
await discord.ext.commands.Context.sends([message, message2...], cool=1)
```

> message - 上記のmessage関数を用いて作成  
cool - メッセージの送信間隔 初期値: 0

### 使用例

```py
import multiple_discord
@bot.command()
async def test(ctx):
    messages = [
        multiple_discord.message('first message', embed=discord.Embed(title='first', description='message')),
        multiple_discord.message('second message', embed=discord.Embed(title='second', description='message'))
    ]
    await ctx.sends(messages, cool=1)

@bot.event
async def on_message(message):
    messages = [
        multiple_discord.message('first message', embed=discord.Embed(title='first', description='message')),
        multiple_discord.message('second message', embed=discord.Embed(title='second', description='message'))
    ]
    await message.channel.sends(messages, cool=1)
```

## add_reactions

```py
await discord.Message.add_reactions([emoji, emoji2...])
```

## field

```py
field(引数...)
```

指定可能な引数 - discord.Embed.add_fieldと同じ

## add_fields

```py
await discord.Embed.add_fields([field, field2...])
```

> field - 上記のfield関数を用いて作成

### 使用例

```py
import multiple_discord
embed = discord.Embed(title='test')
fields = [
    multiple_discord.field(name='first', value='field'),
    multiple_discord.field(name='second', value='field', inline=False)
]
embed.add_fields(fields)
```
