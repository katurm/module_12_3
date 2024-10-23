import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
        return finishers

def skip_if_frozen(method):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
             return method(self, *args, **kwargs)
    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_walk(self):
        run_1 = Runner('Run1')
        for i in range(10):
            run_1.walk()
        self.assertEqual((run_1.distance), 50)

    @skip_if_frozen
    def test_run(self):
        run_2 = Runner('Run2')
        for i in range(10):
            run_2.run()
        self.assertEqual((run_2.distance), 100)

    @skip_if_frozen
    def test_challenge(self):
        run_3 = Runner('Run3')
        run_4 = Runner('Run4')
        for i in range(10):
            run_3.run()
            run_4.walk()

        self.assertNotEqual(run_3.distance, run_4.distance)


if __name__ == '__main__':
    unittest.main()

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @skip_if_frozen
    def setUp(self):
        self.runer_1 = Runner('Усэйн', 10)
        self.runer_2 = Runner('Андрей', 9)
        self.runer_3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):

        for test_key, test_value in cls.all_results.items():
            print(f'Тест: {test_key}')
            for key, value in test_value.items():
                print(f'\t{key}: {value.name}')

    @skip_if_frozen
    def test_turn1(self):
        turn_1 = Tournament(90, self.runer_1, self.runer_3)
        result = turn_1.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_turn1'] = result

    @skip_if_frozen
    def test_turn2(self):
        turn_2 = Tournament(90, self.runer_2, self.runer_3)
        result = turn_2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_turn2'] = result

    @skip_if_frozen
    def test_turn3(self):
        turn_3 = Tournament(90, self.runer_1, self.runer_2, self.runer_3)
        result = turn_3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_turn3'] = result

if __name__ == '__main__':
    unittest.main()