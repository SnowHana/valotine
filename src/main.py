from urllib.parse import quote
from opgg.opgg import OPGG
from opgg.params import Region
from opgg.summoner import Summoner
import requests

API_KEY = "RGAPI-f6591a1d-7714-4b17-87ac-a6b62bea4e2f"


class Player:
    def __init__(
        self, player_name: str, player_tag: str, region: str, detailed_region: str
    ) -> None:
        # Remove white space of player_name and concatentate with player_tag
        self._puuid = None
        self._player_name = player_name
        self.player_tag = player_tag

        # Basic error checking
        assert region.lower() in ["americas", "asia", "esports", "europe"]
        self.region = region.lower()
        self.detailed_region = detailed_region.lower()

        # Set puuid, an unique identifier
        self.init_puuid()

    @property
    def puuid(self):
        return self._puuid

    @property
    def player_name(self):
        return self._player_name

    def init_puuid(self):
        """Get puuid of player based on their ingame name and tag
        https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/Hide%20on%20bush/KR1
        """
        api_url = (
            "https://"
            + self.region
            + ".api.riotgames.com/riot/account/v1/accounts/by-riot-id/"
            + quote(self.player_name)
            + "/"
            + quote(self.player_tag)
            + "?api_key="
            + API_KEY
        )

        resp = requests.get(api_url)
        player_info = resp.json()
        self._puuid = player_info["puuid"]


class PlayerData(Player):

    def __init__(
        self, player_name: str, player_tag: str, region: str, detailed_region: str
    ):
        super().__init__(player_name, player_tag, region, detailed_region)

    @staticmethod
    def opgg_extract_player(self):
        """Extract the exact player (player_name#player_tag) from oppg api"""
        # If error happens just remove staticmethod
        opgg = OPGG(None, Region.KR)

        summoner: Summoner
        for summoner in opgg.search(["Peyz#KR11"], Region.KR):
            print(summoner)
        print(len(opgg.search(["Peyz#KR1"], Region.KR)))
        # exact_summoner = list(
        #     filter(
        #         lambda x: x.acct_id == self.puuid, opgg.search(["JUGKING"], Region.KR)
        #     )
        # )

    # def get_match_ids(self):
    #     api_url = (
    #         "https://"
    #         + mass_region
    #         + ".api.riotgames.com/lol/match/v5/matches/by-puuid/"
    #         + puuid
    #         + "/ids?start=0&count=20"
    #         + "&api_key="
    #         + api_key
    #     )
    #
    #     print(api_url)
    #
    #     resp = requests.get(api_url)
    #     match_ids = resp.json()
    #     return match_ids


faker = Player("Hide on bush", "KR1", "Asia", "kr")
print(faker.puuid)

canyon = Player("Peyz", "KR11", "Asia", "kr")

print(canyon.puuid)
canyon_data = PlayerData(
    canyon.player_name, canyon.player_tag, canyon.region, canyon.detailed_region
)
canyon_data.opgg_extract_player(canyon_data)
