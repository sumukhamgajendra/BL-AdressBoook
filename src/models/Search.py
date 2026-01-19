# Seperate Search class to preserve SOLID principle rule.
class Search:
    def __init__(self):
        self.city = {}
        self.state = {}

    def search_by_city(self, city_name: str):
        names = self.city[city_name] if city_name in self.city else []
        for name in names:
            print(name)
            return
        print("No contacts found")

    def search_by_state(self, state_name: str):
        names = self.state[state_name] if state_name in self.state else []
        for name in names:
            print(name)
            return
        print("No contacts found")

    def display_search_results(self, results, city):
        print(f"Persons found in city: {city}")
        for names in results:
            print(f"First Name: {names.f_name}, Last Name: {names.l_name}")

    def update_city_state_dict(self, f_name, city, state):
        self.state.setdefault(state, []).append(f_name)
        self.city.setdefault(city, []).append(f_name)
