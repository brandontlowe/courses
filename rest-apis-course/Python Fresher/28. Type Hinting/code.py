# Example 1
def list_avg(sequence: list) -> float:
    return sum(sequence) / len(sequence)

list_avg(123)

# Example 2
class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count