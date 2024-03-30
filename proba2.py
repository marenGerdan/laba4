# 117

def find_subsequences(sequence, M, greater_than_2M_indices):
    """
    Finds all maximum length subsequences within a circular sequence whose sum
    falls within the range [M, 2M].
    Arguments:
         sequence: a list of numbers representing a cyclic sequence.
         M: An integer specifying the range [M, 2M] for the sum of the subsequences.

    Returns:
        tuple containing:
            - a list of tuples (start_index, length), where start_index is the index
               beginning of the subsequence in the sequence, and length is its length.
            - maximum length of found subsequences
    """
    n = len(sequence)
    left = 0
    right = 0
    current_sum = 0
    max_length = 0
    max_length_subsequences = []

    for i in range(n):
        if sequence[i] > 2 * M:
            greater_than_2M_indices.add(i)

    for right in range(2 * n):
        current_sum += sequence[right % n]

        if current_sum > 2 * M:
            current_sum -= sequence[left % n]
            if left % n in greater_than_2M_indices:
                greater_than_2M_indices.remove(left % n)
            left += 1
        if M <= current_sum <= 2 * M:
            length = (right - left + 1) % n
            if length > max_length:
                max_length = length
                max_length_subsequences = [(left % n, length)]
            elif length == max_length:
                max_length_subsequences.append((left % n, length))

    return max_length_subsequences, max_length


def main():
    """
    Monitors program flow, processes user input and output, and manages possible errors.
    """
    print("The author of this program is Kukhelna Oleksandra.")
    print("Variant 117. This program searches for subsequences with the maximum sum in the range.")
    print("Початок роботи програми.")
    try:
        M = int(input("Введіть значення M: "))
        if M < 2:
            raise ValueError("M має бути цілим числом не менше 2")

        sequence = list(map(int, input("Введіть послідовність чисел через пробіл: ").split()))
        if not sequence:
            raise ValueError("Послідовність не може бути пустою")

        greater_than_2M_indices = set()
        max_length_subsequences, max_length = find_subsequences(sequence, M, greater_than_2M_indices)
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