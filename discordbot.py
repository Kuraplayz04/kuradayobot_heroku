# Discord.pyの読み込み
import discord

# Discordへ接続するのに必要
client = discord.Client(activity=discord.Game(name='青鬼基幹システム v1.7'))

# 自分のBotのアクセストークンを記入
TOKEN = "ODQyNzM1NDQxOTQxMTAyNjAy.YJ5oig.3UZkcAZSP7cNJKcQg2enzzanSpo"

@client.event
async def on_member_join(member):
    channel = client.get_channel(825992683701010450)
    await channel.send(f'{member} joined on {member.joined_at}')

# Bot起動時に実行される
@client.event
async def on_ready():
    print('ログインしました')


# メッセージを取得した時に実行される
@client.event
async def on_message(message, lastmessage=None):
    # Botのメッセージは除外
    if message.author.bot:
        return

    # 条件に当てはまるメッセージかチェックし正しい場合は返す
    def check(msg):
        return msg.author == message.author

    # /getとチャンネル上に打ち込むとBotが反応を示す
    if message.content.startswith("/f3"):
        await message.delete()
        # /getと打ち込まれたチャンネル上に下記の文章を出力

        # ユーザーからのメッセージを待つ
        wait_message = await client.wait_for("message", check=check)
        an0 = '<@&825992683465080845>'
        an1 = '\n青鬼ごっこやります。（'
        an2 = '）\nサーバー: EventServer\nID:KuraPlayz04\n\nver1.16.2'

        # メッセージを打ち込まれたのを確認すると下記の文章を出力
        channel = client.get_channel(825992683701010449)
        await channel.send(an0 + an1 + wait_message.content + an2)
        embed_r_3 = discord.Embed(title="アナウンス完了!", description="Tier3チャット\nメンションアナウンス",color=discord.Colour.dark_blue())
        await message.channel.send(embed=embed_r_3)

    if message.content.startswith("/f2"):
        await message.delete()
            # /getと打ち込まれたチャンネル上に下記の文章を出力

            # ユーザーからのメッセージを待つ
        wait_message = await client.wait_for("message", check=check)
        an0 = '<@&825992683465080845>'
        an1 = '\n青鬼ごっこやります。（'
        an2 = '）\nサーバー: EventServer\nID:KuraPlayz04\n\nver1.16.2'

            # メッセージを打ち込まれたのを確認すると下記の文章を出力
        channel = client.get_channel(825992683701010450)
        await channel.send(an0 + an1 + wait_message.content + an2)
        embed_r_2 = discord.Embed(title="アナウンス完了!", description="Tier2チャット\nメンションアナウンス",color=discord.Colour.red())
        await message.channel.send(embed=embed_r_2)


    if message.content.startswith("/f1"):
        await message.delete()
                # /getと打ち込まれたチャンネル上に下記の文章を出力

                # ユーザーからのメッセージを待つ
        wait_message = await client.wait_for("message", check=check)
        an0 = '<@&825992683465080845>'
        an1 = '\n青鬼ごっこやります。（'
        an2 = '）\nサーバー: EventServer\nID:KuraPlayz04\n\nver1.16.2'

                # メッセージを打ち込まれたのを確認すると下記の文章を出力
        channel = client.get_channel(825992683701010451)
        await channel.send(an0 + an1 + wait_message.content + an2)
        embed_r_1 = discord.Embed(title="アナウンス完了!", description="Tier1チャット\nメンションアナウンス",color=discord.Colour.purple())
        await message.channel.send(embed=embed_r_1)

    if message.content.startswith("/n3"):
        await message.delete()

        # ユーザーからのメッセージを待つ
        wait_message = await client.wait_for("message", check=check)
        ans1 = '\n次どぞ（'
        ans2 = '）'

        # メッセージを打ち込まれたのを確認すると下記の文章を出力
        channel = client.get_channel(825992683701010449)
        await channel.send(ans1 + wait_message.content + ans2)
        embed_r_3 = discord.Embed(title="アナウンス完了!", description="Tier3チャット\nネクストアナウンス",color=discord.Colour.dark_blue())
        await message.channel.send(embed=embed_r_3)

    if message.content.startswith("/n2"):
        await message.delete()

            # ユーザーからのメッセージを待つ
        wait_message = await client.wait_for("message", check=check)
        ans1 = '\n次どぞ（'
        ans2 = '）'

            # メッセージを打ち込まれたのを確認すると下記の文章を出力
        channel = client.get_channel(825992683701010450)
        await channel.send(ans1 + wait_message.content + ans2)
        embed_r_2 = discord.Embed(title="アナウンス完了!", description="Tier2チャット\nネクストアナウンス",color=discord.Colour.red())
        await message.channel.send(embed=embed_r_2)

    if message.content.startswith("/n1"):
        await message.delete()

                # ユーザーからのメッセージを待つ
        wait_message = await client.wait_for("message", check=check)
        ans1 = '\n次どぞ（'
        ans2 = '）'

                # メッセージを打ち込まれたのを確認すると下記の文章を出力
        channel = client.get_channel(825992683701010451)
        await channel.send(ans1 + wait_message.content + ans2)
        embed_r_1 = discord.Embed(title="アナウンス完了!", description="Tier1チャット\nネクストアナウンス",color=discord.Colour.purple())
        await message.channel.send(embed=embed_r_1)

    if message.content.startswith("/l3"):
        await message.delete()

        # ユーザーからのメッセージを待つ
        wait_message = await client.wait_for("message", check=check)
        ansl1 = 'ラストどうぞ（'
        ansl2 = '）'

        # メッセージを打ち込まれたのを確認すると下記の文章を出力
        channel = client.get_channel(825992683701010449)
        await channel.send(ansl1 + wait_message.content + ansl2)
        embed_r_3 = discord.Embed(title="アナウンス完了!", description="Tier3チャット\nラストアナウンス",color=discord.Colour.dark_blue())
        await message.channel.send(embed=embed_r_3)

    if message.content.startswith("/l2"):
        await message.delete()

            # ユーザーからのメッセージを待つ
        wait_message = await client.wait_for("message", check=check)
        ansl1 = '\nラストどうぞ（'
        ansl2 = '）'

            # メッセージを打ち込まれたのを確認すると下記の文章を出力
        channel = client.get_channel(825992683701010450)
        await channel.send(ansl1 + wait_message.content + ansl2)
        embed_r_2 = discord.Embed(title="アナウンス完了!", description="Tier2チャット\nラストアナウンス",color=discord.Colour.red())
        await message.channel.send(embed=embed_r_2)

    if message.content.startswith("/l1"):
        await message.delete()

                # ユーザーからのメッセージを待つ
        wait_message = await client.wait_for("message", check=check)
        ansl1 = '\nラストどうぞ（'
        ansl2 = '）'

                # メッセージを打ち込まれたのを確認すると下記の文章を出力
        channel = client.get_channel(825992683701010451)
        await channel.send(ansl1 + wait_message.content + ansl2)
        embed_r_1 = discord.Embed(title="アナウンス完了!", description="Tier1チャット\nラストアナウンス",color=discord.Colour.purple())
        await message.channel.send(embed=embed_r_1)

# Botの実行
client.run(TOKEN)

