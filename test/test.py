from iconservice import *

TAG = 'Test'

class Test(IconScoreBase):

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)

    def on_install(self) -> None:
        super().on_install()

    def on_update(self) -> None:
        super().on_update()
    
    @external(readonly=True)
    def str_hello(self) -> str:
        Logger.debug(f'Hello, world!', TAG)
        return "Hello, nanaones!"

    @external(readonly=True)
    def bool_hello(self) -> bool:
        Logger.debug(f'Hello, world!', TAG)
        return True

    @external(readonly=True)
    def bytes_hello(self) -> bytes:
        Logger.debug(f'Hello, world!', TAG)
        return bytes(b"Hello, nanaones!")

    @external(readonly=True)
    def int_hello(self) -> int:
        Logger.debug(f'Hello, world!', TAG)
        return 19920305

    @external(readonly=True)
    def dict_hello(self) -> dict:
        Logger.debug(f'Hello, world!', TAG)
        return {"name":"nanaones", "birth":19920305}

    @external(readonly=True)
    def list_hello(self) -> list:
        Logger.debug(f'Hello, world!', TAG)
        return ["Hello", "nanaones!", 19920305, True, bytes(b"Hello, nanaones!"), {"name":"nanaones", "birth":19920305}]

    @external(readonly=True)
    def tuple_hello(self) -> str:
        Logger.debug(f'Hello, world!', TAG)
        return ("Hello, nanaones!", "nanaeons", 1)


# Not surported

    # fail
    # @external(readonly=True)
    # def None_hello_return(self) -> None:
    #     """
    #     in deploy failure massage
    #     {...
    #         "status": "0x0",
    #         "failure": {
    #             "code": "0x5",
    #             "message": "Unsupported type for 'None' at None_hello_return"
    #     ...}
    #     """
    #     Logger.debug(f'Hello, world!', TAG)
    #     return None

    # # fail
    # @external(readonly=True)
    # def None_hello_no_return(self) -> None:
    #     """
    #     in deploy failure massage
    #     ...
    #     "status": "0x0",
    #     "failure": {
    #         "code": "0x5",
    #         "message": "Unsupported type for 'None' at None_hello_no_return"
    #     ...
    #     """
    #     Logger.debug(f'Hello, world!', TAG)

    # fail
    # @external(readonly=True)
    # def None_hello_no_return_no_hint(self):
    #     """
    #     in deploy failure massage
    #     ...
    #         "status": "0x0",
    #         "failure": {
    #             "code": "0x5",
    #             "message": "Returning type should be declared in read-only functions at None_hello_no_return_no_hint"
    #         }
    #     ...
    #     """
    #     Logger.debug(f'Hello, world!', TAG)


    

