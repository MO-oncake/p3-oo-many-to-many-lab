class Author:
    all_authors = []

    def __init__(self, name=""):
        self.name = name
        self._contracts = []
        Author.all_authors.append(self)

    def contracts(self):
        # Returns a list of related contracts
        return self._contracts

    def books(self):
        # Returns a list of related books using the Contract class as an intermediary
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date, royalties):
        # Creates and returns a new Contract object between the author and the specified book
        if not isinstance(book, Book):
            raise Exception("Invalid book.")
        if not isinstance(royalties, int) or royalties < 0:
            raise Exception("Invalid royalties value.")
        new_contract = Contract(self, book, date, royalties)
        self._contracts.append(new_contract)
        return new_contract

    def total_royalties(self):
        # Returns the total amount of royalties that the author has earned from all contracts
        return sum(contract.royalties for contract in self._contracts)


class Book:
    all_books = []

    def __init__(self, title=""):
        self.title = title
        self._contracts = []
        Book.all_books.append(self)

    def contracts(self):
        # Returns a list of related contracts
        return self._contracts

    def authors(self):
        # Returns a list of related authors using the Contract class as an intermediary
        return [contract.author for contract in self._contracts]


class Contract:
    all_contracts = []

    def __init__(self, author, book, date="", royalties=0):
        if not isinstance(author, Author):
            raise Exception("Invalid author.")
        if not isinstance(book, Book):
            raise Exception("Invalid book.")
        if not isinstance(date, str):
            raise Exception("Invalid date.")
        if not isinstance(royalties, int) or royalties < 0:
            raise Exception("Invalid royalties value.")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        # Add contract to related author and book
        self.author._contracts.append(self)
        self.book._contracts.append(self)
        Contract.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        # Filter contracts by the given date
        filtered_contracts = [contract for contract in cls.all_contracts if contract.date == date]
        # Sort contracts by date
        return sorted(filtered_contracts, key=lambda contract: contract.date)