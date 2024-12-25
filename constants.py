from helper import Helper

CHANNELS_JSON = 'data/channels.json'
POKEMON_JSON = 'data/pokemon.json'
POKETWO_USER = 716390085896962058


### EVENT ###
# event_channel_list = [1250976628763525191]

### CHANNELS ###
channels = Helper.get_json(CHANNELS_JSON)

### POKEMON_DATA ###
pokemon_data = Helper.get_json(POKEMON_JSON)
rand_stats = {
	'stat_list': ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Total', 'Height', 'Weight'],
	'stat_data': ['hp', 'attack', 'defense', 'special-attack', 'special-defense', 'speed', 'total', 'height', 'weight'],
	'selected_stats': {},
}

### POKETWO ###
trade_messages = {
	'command': ["trade", "t"],
	'completed': "🟢",
	'send': "Trade between ",
}