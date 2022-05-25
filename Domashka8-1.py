import requests
from pprint import pprint


class Superhero:

    def __init__(self, name):
        self.name = name
        self.url_search = 'https://superheroapi.com/api/2619421814940190/search/'

    def get_character_id(self):
        response = requests.get(self.url_search + self.name)
        #print(response.url)
        return response.json()

    def intelligence(self):
        result = self.get_character_id()['results']
        if len(result) > 1:
            for res in result:
                if res['name'] == self.name:
                    intelligence = res["powerstats"]['intelligence']
        else:
            intelligence = result[0]["powerstats"]['intelligence']
        return intelligence

def winner_intelligence(superhero_list):
    max_result = 0
    for super_hero in superhero_list:
        print(super_hero.name, ' - ', super_hero.intelligence())
        if int(super_hero.intelligence()) > max_result:
            max_result = int(super_hero.intelligence())
            winner = super_hero
    return print(f'\nСамый умный у нас {winner.name} с результатом {winner.intelligence()} баллов\n')


if __name__ == '__main__':

    hulk = Superhero('Hulk')
    captain_america = Superhero('Captain America')
    thanos = Superhero('Thanos')
    superhero_list = [hulk, captain_america, thanos]

    # print(hulk.intelligence(), hulk.name)
    # print(captain_america.intelligence(), captain_america.name)
    # print(thanos.intelligence(), thanos.name)
    #print(superhero_list)
    winner_intelligence(superhero_list)