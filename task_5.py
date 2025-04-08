class Results:
    def __init__(self, victories, draws, losses):
        self.victories = victories
        self.draws = draws
        self.losses = losses

class Football(Results):
    def number_of_wins(self):
        return f"Футбольных побед: {self.victories}"

    def number_of_draws(self):
        return f"Футбольных ничьих: {self.draws}"

    def number_of_losses(self):
        return f"Футбольных поражений: {self.losses}"

    def total_points(self):
        total = 3 * self.victories + self.draws
        return f"Общее количество очков: {total}"

class Hockey(Results):
    def number_of_wins(self):
        return f"Хоккейных побед: {self.victories}"

    def number_of_draws(self):
        return f"Хоккейных ничьих: {self.draws}"

    def number_of_losses(self):
        return f"Хоккейных поражений: {self.losses}"

    def total_points(self):
        total = 2 * self.victories + self.draws
        return f"Общее количество очков: {total}"

football_team = Football(2, 2, 2)
hockey_team = Hockey(2, 2, 2)

football_methods = [
    football_team.number_of_wins,
    football_team.number_of_draws,
    football_team.number_of_losses,
    football_team.total_points
]

hockey_methods = [
    hockey_team.number_of_wins,
    hockey_team.number_of_draws,
    hockey_team.number_of_losses,
    hockey_team.total_points
]

for method in football_methods:
    print(method())

for method in hockey_methods:
    print(method())

    