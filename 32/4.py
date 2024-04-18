class DigitRetrieve:
    def __call__(self, value: str):
        try:
            return int(value)
        except ValueError:
            return None


if __name__ == "__main__":
    dg = DigitRetrieve()
    st = ["123", "abc", "-56.4", "0", "-5"]
    digits = list(map(dg, st))  # [123, None, None, 0, -5]
    print(digits)
