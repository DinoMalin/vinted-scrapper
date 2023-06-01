class Item:
    def __init__(self, name: str, keywords: list[str], price_range: tuple) -> None:
        self.name = name
        self.keywords = keywords
        self.price_range = price_range

    def __str__(self) -> str:
        return f"Item(name={self.name}, keywords={self.keywords}, price_range={self.price_range})"


class Account:
    def __init__(self) -> None:
        self.id = None
        self.username = None
        self.profile_picture = []

    def __str__(self) -> str:
        return f"Account(id={self.id}, username={self.username}, profile_picture={self.profile_picture})"


class Ad:
    def __init__(self) -> None:
        self.id = None
        self.title = None
        self.url = None
        self.price = None
        self.images = []
        self.account = Account()

    def __str__(self) -> str:
        return f"Ad(id={self.id}, title={self.title}, url={self.url}, price={self.price}, images={self.images}, account={self.account})"
