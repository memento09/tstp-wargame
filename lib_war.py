from random import shuffle


class Card:
    suits = ["spades", "hearts", "diamonds", "clubs"]
    values = [
        None,
        None,
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
        "Ace"]

    def __init__(self, v, s):
        """suit(マーク)も整数値です"""
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            return self.suit < c2.suit
            # if self.suit < c2.suit:
            #     return True
            # else:
            #     return False
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            return self.suit > c2.suit
            # if self.value > c2.value:
            #     return True
            # else:
            #     return False
        return False

    def __repr__(self):
        v = self.values[self.value] + " of " \
            + self.suits[self.suit]
        return v


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def draw(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name


class Game:
    def __init__(self):
        name1 = input("プレイヤー1の名前： ")
        name2 = input("プレイヤー2の名前： ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def print_winner(self, winner):
        print(f"このラウンドは {winner.name} が勝ちました")
        # w = f"このラウンドは {winner} が勝ちました"
        # print(w)

    def print_draw(self, p1, p2):
        print(f"{p1.name} は {p1.card}、{p2.name} は {p2.card} を引きました")
        # d = f"{p1n} は {p1c}、{p2n} は {p2c} を引きました"
        # print(d)

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "引き分け！"

    def play_game(self):
        cards = self.deck.cards
        print("戦争を始めます！")
        while len(cards) >= 2:
            m = "q で終了、それ以外のキーでPlay: "
            response = input(m)
            if response == 'q':
                break
            self.p1.card = self.deck.draw()
            self.p2.card = self.deck.draw()
            self.print_draw(self.p1, self.p2)

            # p1c = self.deck.draw()
            # p2c = self.deck.draw()
            # p1n = self.p1.name
            # p2n = self.p2.name
            # self.draw(p1n, p1c, p2n, p2c)
            if self.p1.card > self.p2.card:
                self.p1.wins += 1
                self.print_winner(self.p1)
            else:
                self.p2.wins += 1
                self.print_winner(self.p2)

        win = self.winner(self.p1, self.p2)
        print(f"ゲーム終了、{win} の勝利です！")


if __name__ == "__main__":
    card1 = Card(10, 2)
    card2 = Card(11, 3)
    card = Card(3, 2)
    print(card1 < card2)
    print(card1 > card2)
    print(card)
    deck = Deck()
    for card in deck.cards:
        print(card)
