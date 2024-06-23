import discord

class Builder:
    """
    Static method class for embed builders.
    """

    @staticmethod
    def build_a_text_embed(title, **kwargs):
        """
        :param title:
        :param kwargs:
        :return: Embed

        Creates a discord embed based on given keyword argumetns. You should include the charracteristics you want to give and their value as keyword arguments.
        """
        embed = discord.Embed(title=title)

        for field, value in kwargs.items():

            if field == 'author':
                embed.set_author(name=value)

            if field == 'description':
                embed.description = value

            if field == 'color':
                embed.colour = value

            if field == 'field':
                field_name, field_value, is_inline = value
                embed.add_field(name=field_name, value=field_value, inline=is_inline)

        return embed