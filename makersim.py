from model.environment import Environment
# from model.cdp import


class makersim:

    def __init__(self):
        self.env = Environment()

    def start_simulation(self):
        while True:
            self.env.update()


def main():
    # TODO - put argparse stuff here
    ms = makersim()
    ms.start_simulation()


if __name__ == '__main__':
    main()
