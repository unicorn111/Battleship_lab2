class Player:
    without_ships = []

    def __init__(self, __name):
        self.__name = __name

    def read_position(self):
        position = input('{0}, enter move: '.formate(self.__name))
        Player.without_ships.append(position[0], int(position[1:]))
        return (position[0], int(position[1:]))


class Field(Player):
    new_field = []

    def __init__(self, __ships):
        self.__ships = __ships
        Player.__init__(self, name)

    def generate_field(self):
        return field

    def shoot_at(position):
        '''(tuple) -> (bool)
        Returns True, if ship is in that position.
        If there is no ship, returns False.
        0 is for ' ' 1 is for  '*' 2 s for 'X'
        '''
        board = generate_field(self)
        for i in board:
            if position in i:
                if i[-1] == 0:
                    return('False')
                elif i[-1] == 1:
                    i[-1] = 2
                    Field.new_field.append(board)
                elif i[-1] == 2:
                    return('True')
            if position in i:
                if i[-1] == 2:
                    return('True')

        def field_without_ships(self):
            return Player.without_ships

        def field_with_ships(self):
            return Field.new_field


class Ship(Field):
    def __init__(self=0, bow=0, horizontal=0, __length=0, __hit=0):
        self.bow = bow
        self.horizontal = horizontal
        self.__length = __length
        self.__hit = __hit
        Field.__init__(self, __ships)

    def shoot_at(self, coordinates):
        Field._shoot_at(self, coordinates)


class Game(Field):
    def __init__(self, __field, __players, __current_player):
        Player.__init__(self, __name)
        Field.__init__(self, __ships)
        self.__field = __field
        self.__players = __players
        self.__current_player = __current_player

    def read_position(self):
        pos = Player.read_position(self)
        return pos

    def field_without_ships(self, index):
        field_s = Field.field_without_ships(self)
        return 'Player {}, {}'.format(index, field_s)

    def field_with_ships(self):
        fields = Field.field_with_ships(self, index)
        return 'Player {}, {}'.format(index, field_s)

