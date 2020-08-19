# from Defining_Classes.guild_system_7.project.player import Player
class Guild:
    def __init__(self, guild_name, players=[]):
        self.guild_name = guild_name
        self.players = players

    def assign_player(self, player):
        if player.guild == "Unaffiliated":
            player.guild = self.guild_name
            self.players.append(player)
            return f"Welcome player {player.name} to the guild {self.guild_name}"
        if player.guild == self.guild_name:
            return f"Player {player.name} is already in the guild."
        return f"Player {player.name} is in another guild."

    def kick_player(self, player_name: str):
        for p in self.players:
            if player_name in p.name:
                self.players.remove(p)
                p.guild = "Unaffiliated"
                return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        temp1 = f"Guild: {self.guild_name}\n"
        for each in self.players:
            temp1 += f"{each.player_info()}"
        return temp1


# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
# guild = Guild("UGT")
# print(guild.assign_player(player))
# print(guild.guild_info())
