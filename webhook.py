from discord_webhook import DiscordWebhook, DiscordEmbed

def alert(url: str, country: str, cases: int, new: int):
    """
        Send request to the discord webhook to alert the user
    """
    webhook = DiscordWebhook(url=url)

    # create embed object for webhook
    embed = DiscordEmbed(title="New Covid Case Reported in {}".format(country.lower().capitalize()), description='{} New Cases \n{} Total Cases'.format(new, cases), color=0xff0033)

    # add embed object to webhook
    webhook.add_embed(embed)

    response = webhook.execute()