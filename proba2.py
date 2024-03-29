# 117

def find_subsequences(sequence, M):
    n = len(sequence)
    left = 0
    right = 0
    current_sum = 0
    max_length = 0
    max_length_subsequences = []

    while right < n:
        current_sum += sequence[right]
        right += 1

        while current_sum > 2 * M:
            current_sum -= sequence[left]
            left += 1

        if M <= current_sum <= 2 * M:
            length = right - left
            if length > max_length:
                max_length = length
                max_length_subsequences = [(left, length)]
            elif length == max_length:
                max_length_subsequences.append((left, length))

    return max_length_subsequences, max_length


def main():
    """
    This function controls the operation of the program, inputs data and outputs results.
    """
    print("The author of this program is Kukhelna Oleksandra.")
    print("Variant 117. This program searches for subsequences with the maximum sum in the range.")
    print("Початок роботи програми.")
    try:
        M = int(input("Введіть значення M: "))
        if M < 2:
            raise ValueError("M має бути цілим числом не менше 2")

        sequence = list(map(int, input("Введіть послідовність чисел через пробіл: ").split()))
        sequence_copy = sequence.copy()
        sequence.extend(sequence_copy)

        max_length_subsequences, max_length = find_subsequences(sequence, M)
        print("THE WORK IS DONE")
        for subsequence in max_length_subsequences:
            start_index, length = subsequence
            end_index = (start_index + length - 1)
            print(f"{start_index} - {end_index} ({length})")
    except KeyboardInterrupt:
        print('\nprogram aborted')
    except (ValueError, EOFError, IOError) as e:
        print(f"***** error: {e}")


if __name__ == "__main__":
    main()