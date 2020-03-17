import configs

from instabot import Bot


class TheCosmos(Bot):

    def __init__(self):
        super().__init__()
        self.login()

    def login(self, **args):
        super().login(username=configs.USERNAME, password=configs.PASSWORD)


bot = TheCosmos()


OPTIONS = [
    ("1. Un-follow everyone.", bot.unfollow_everyone)
]


def show_menu():
    print(f"{bot.username}\n{'-'*len(bot.username)}", end="\n\n")
    for i in OPTIONS:
        print(i[0])
    print("\n")


def log_info(info):
    print(f"--- {info} ---")


if __name__ == "__main__":
    # while True:
    #     show_menu()
    #     choice = int(input(">> "))
    #     start = time.time()
    #     OPTIONS[choice - 1][1]()
    #     log_info(f"Task finished in {time.time() - start} seconds.")

    bot.unfollow_everyone()
