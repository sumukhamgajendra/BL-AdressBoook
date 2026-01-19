# Seperate Search class to preserve SOLID principle rule.
class Search:
    def __init__(self):
        self.city = {}
        self.state = {}

    def search_by_city(self, city_name: str):
        names = self.city[city_name] if city_name in self.city else []
        for name in names:
            print(name)

    def search_by_state(self, state_name: str):
        names = self.state[state_name] if state_name in self.state else []
        for name in names:
            print(name)