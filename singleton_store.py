class SingletonStore:
    _instances = {}

    def __init__(self, **kwargs) -> None:
        raise Exception(f'cannot instantiate {SingletonStore.__name__}')
        # SingletonStore.__instances.update(**kwargs)
    
    @classmethod
    def get(cls, key):
        return cls._instances[key]

    @classmethod
    def add(cls, key, value):
        store = cls._instances
        if value in store.values():
            key = [k for k, v in store.items() if v is value][0]
            raise ValueError(f'object {value} already present with {key=}')
        if key in store:
            raise KeyError(f'key {key} already present with value={store[key]}')
        store[key] = value
    
    @classmethod
    def items(cls):
        return cls._instances.items()
    
    @classmethod
    def dict(cls):
        return cls._instances

    @classmethod
    def add_values(cls, **kwargs):
        for key, value in kwargs.items():
            cls.add(key, value)

if __name__ == '__main__':
    try:
        app = SingletonStore(name='hello', x='greetings')
    except Exception as e:
        print(e)
        SingletonStore.add_values(name='hello', x='greetings')

    print(SingletonStore.get('name'))
    print(SingletonStore.get('x'))
    try:
        SingletonStore.add('x', 'hello')
    except ValueError as ve:
        print(ve)
    try:
        SingletonStore.add('x', 'wooooo')
    except KeyError as ke:
        print(ke)

    print(SingletonStore.items())
    print(SingletonStore.dict())


