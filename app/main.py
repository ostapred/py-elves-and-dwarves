from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players: list[Player]) -> int:
    team_toral_rating = 0
    for player in players:
        team_toral_rating += player.get_rating()
    return team_toral_rating


def elves_concert(participants: list[Elf]) -> list[str]:
    all_songs = [participant.play_elf_song() for participant in participants]
    return all_songs


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> list[str]:
    dishes = [dwarf.eat_favourite_dish() for dwarf in dwarves]
    return dishes
