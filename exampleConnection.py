from telesql import TeleSQL

class TeleSqlClient:
    def __init__(self) -> None:
        self.connectionString = 'telesql:1BVtsOHUBuyWJGp-4TiMNQVbo42WPvPO7LAhiJNrx1c0VOK7RrwCoW1Erq4vHttFwEtdqo2Hn7MJY7W8a0V5-sXT_XN5FMOFx8R8-wQd9JDVG47JeApUJ3yzGI3hTxM4DpKa4Tw7DI2nmcjwf0615Hntgavl12cOO_MTNxNr0LY8CWtdwFT53WndGgoyP2Wp4mjPW7O2MqFsOxH7As1qQWYJHh4z9UyG3wUX3r446JklnBkj91STsOAsFTT1EL9gaW3nfNuz2chjJm4Ccks59UBRrmLgrZ_j6C1uNF0gVfcOt1xdE5-HSonstZ3t7veuuwBIBvX2HCJo0GZ3GL-ZmsL0BkN94dZc=:newDb:1BVtsO'
        self.cl = TeleSQL()

ex = TeleSqlClient()
ex.cl.client.send_message('me', "Helllllllpp")


