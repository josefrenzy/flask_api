class TooManyPagesReadError(ValueError):
    pass


class Book:
    def __init__(self, name: str, page_count: int) -> None:
        self.name= name
        self.pages_count= page_count
        self.pages_read = 0

    def __repr__(self) -> str:
        return (
            f"<Book name={self.name!r}, read {self.pages_read}, pages out of {self.pages_count!r}>"
        )
    def read(self, pages:int):
        if (self.pages_read + pages > self.pages_count):
            raise TooManyPagesReadError(
                f"You try to read  {self.pages_read + pages} pages, but this book only has {self.pages_count} pages."
            )
        self.pages_read += pages
        print(f"You have now read {self.pages_read} pages out of {self.pages_count}.")

python101 = Book("Python101",50)

try:
    python101.read(35)
    python101.read(50)  
except TooManyPagesReadError as e:
    print(e)

