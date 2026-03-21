def Add(numbers):

    if not numbers:
        return 0

    if ",\n" in numbers or "\n," in numbers:
        raise ValueError("Nieprawidłowy format separatorów")

    normalized_numbers = numbers.replace("\n", ",")

    parts = normalized_numbers.split(",")

    try:
        return sum(int(n) for n in parts)
    except ValueError:
        raise ValueError("Wprowadzono nieprawidłowe dane!")