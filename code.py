def count_frequencies(sequence):
    """
    Count the frequency of each character in the given sequence.

    Args:
        sequence (str): The input sequence of characters.

    Returns:
        dict: A dictionary with characters as keys and their frequencies as values.
    """
    frequency_dict = {}
    for char in sequence:
        if char not in frequency_dict:
            frequency_dict[char] = 1
        else:
            frequency_dict[char] += 1
    return frequency_dict

def print_frequencies(frequency_dict):
    """
    Print the relative frequencies of characters in the given frequency dictionary.

    Args:
        frequency_dict (dict): A dictionary with characters as keys and their frequencies as values.
    """
    print('Frequencies:')
    total_count = float(sum(frequency_dict.values()))
    for char, count in frequency_dict.items():
        print(f'{char}: {count / total_count:.3f}')

print_frequencies(count_frequencies('ATCTGACGCGCGCCGC'))
