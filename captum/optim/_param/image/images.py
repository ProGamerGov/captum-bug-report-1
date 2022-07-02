def test_func3(x: int) -> int:
    """
    Return an integer value.

    Args:

        x (int): An integer value

    Returns:
        x (int): The input value.
    """
    return x


class TestClass3:
    """
    A test class.
    """

    def __init__(self, x: int) -> None:
        """
        Args:

            x (int): An integer value.
        """
        super().__init__()
        self.x = x




__all__ = [
"test_func3",
"TestClass3",
]