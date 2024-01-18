class SoupConfiguration:
    def __hash__(self):
        pass

    def __eq__(self, other):
        pass

    def __repr__(self):
        pass


class Piece:
    def __init__(self, name, guard, action):
        self.name = name
        self.guard = guard
        self.action = action

    def enabled(self, config):
        return self.guard(config)

    def execute(self, config):
        return [self.action(config)]


class SoupSpec:
    def __init__(self, config, pieces):
            self.configs = config
            self.pieces = pieces

    def enabledPieces(self, config):
            return [filter(lambda p: p.enabled(config), self.pieces)]


class SoupSemantics():
    def __init__(self, spec):
        self.spec = spec

    def initial(self):
        return self.spec.initial()

    def actions(self, config):
        self.spec.enabledPieces(config)

    def execute(self, action, config):
        return action.execute(config)