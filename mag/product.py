import json


class Product:
    def __init__(self, category: str, brand: str, model: str, price: int, quantity: int) -> None:
        self.category = category
        self.brand = brand
        self.model = model
        self.price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f'{self.category} brand:{self.brand} model:{self.model} qty:{self.quantity} price:{self.price} '


class Tv(Product):
    def __init__(self, category: str = '', brand: str = '', model: str = '', price: int = 0, quantity: int = 0,
                 diagonal: int = 0, resolution: str = '') -> None:
        super().__init__(category, brand, model, price, quantity)
        self.diagonal = diagonal
        self.resolution = resolution

    def __str__(self) -> str:
        return super().__str__() + f'diagonal:{self.diagonal} resolution:{self.resolution} '


class Refrigerator(Product):
    def __init__(self, category: str = '', brand: str = '', model: str = '', price: int = 0, quantity: int = 0,
                 volume: int = 0, height: int = 0) -> None:
        super().__init__(category, brand, model, price, quantity)
        self.volume = volume
        self.height = height

    def __str__(self) -> str:
        return super().__str__() + f'volume:{self.volume} height:{self.height} '


class Washer(Product):
    def __init__(self, category: str = '', brand: str = '', model: str = '', price: int = 0, quantity: int = 0,
                 maxWeight: int = 0, klass: str = '') -> None:
        super().__init__(category, brand, model, price, quantity)
        self.maxWeight = maxWeight
        self.klass = klass

    def __str__(self) -> str:
        return super().__str__() + f'maxWeight:{self.maxWeight} class:{self.klass} '


class CustomEncoder(json.JSONEncoder):
    def default(self, o):
        return {'__{}__'.format(o.__class__.__name__): o.__dict__}


def decode(obj):
    if '__Tv__' in obj:
        new = Tv()
        new.__dict__.update(obj['__Tv__'])
        return new

    if '__Refrigerator__' in obj:
        new = Refrigerator()
        new.__dict__.update(obj['__Refrigerator__'])
        return new

    if '__Washer__' in obj:
        new = Washer()
        new.__dict__.update(obj['__Washer__'])
        return new
