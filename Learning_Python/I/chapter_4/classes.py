class Player():
    def __init__(self, real_name, nick_name, age):
        self.real_name = real_name
        self.nick_name = nick_name
        self.age = age

    def rename(self, new_nick_name):
        self.nick_name = new_nick_name

    def get_all_information(self):
        return [self.real_name, self.nick_name, self.age]


first_player = Player('Nick', 'predator228', 12)
second_player = Player('Bob', 'sugardaddy65', 56)
print(first_player.get_all_information(), second_player.get_all_information())
first_player.rename('therealpredator')
second_player.rename('yourbigsuggardaay')
print(first_player.get_all_information(), second_player.get_all_information())
