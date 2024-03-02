from urllib.parse import quote

import requests

API_KEY = "RGAPI-f6591a1d-7714-4b17-87ac-a6b62bea4e2f"


class Player:
    def __init__(self, player_name: str, player_tag: str, region: str) -> None:
        # Remove white space of player_name and concatentate with player_tag
        self.player_name = player_name
        self.player_tag = player_tag

        # Basic error checking
        assert region.lower() in ["americas", "asia", "esports", "europe"]
        self.region = region.lower()

        # Get puuid, an unique identifier
        self.init_puuid()

    @property
    def puuid(self):
        return self._puuid

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

    def _concat_name_and_tag(self) -> str:
        """Return a concatenated name
        Ex. Hide on bush#KR1 -> Hide%20on%20bush/KR1
        """
        return


faker = Player("Hide on bush", "KR1", "Asia")
print(faker.puuid)

canyon = Player("JUGKING", "KR1", "Asia")
print(canyon.puuid)
