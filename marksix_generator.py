import random
import math

FIXED_LEN = 6  # The fixed length of each generated set
# Mark Six range: 1 - 49
MIN_NUM = 1  # The minimum number for random generation
MAX_NUM = 49  # The maximum number for random generation


def generate_set(customized_nums):
    """
    Generates a single set of unique numbers.

    Args:
        customized_nums (set): Set of customized numbers provided by the user.

    Returns:
        sorted_tuple (tuple): Tuple of sorted unique numbers.
    """
    customized_nums_copy = customized_nums.copy()
    while len(customized_nums_copy) < FIXED_LEN:
        random_num = random.randint(MIN_NUM, MAX_NUM)
        if random_num not in customized_nums_copy:
            customized_nums_copy.add(random_num)
    sorted_tuple = tuple(sorted(customized_nums_copy))
    return sorted_tuple


def generate_sets(customized_nums):
    """
    Generates sets of unique numbers based on user input.

    Args:
        customized_nums (set): Set of customized numbers provided by the user.

    Returns:
        generated_sets (set): Set of generated sets.
    """
    max_sets_size = math.comb(
        MAX_NUM - len(customized_nums), FIXED_LEN - len(customized_nums))
    sets_size = get_valid_number("How many sets do you want? \nMin: 0; Max: {} : ".format(
        max_sets_size), 0, max_sets_size)
    generated_sets = set()
    while len(generated_sets) < sets_size:
        add_set = generate_set(customized_nums)
        generated_sets.add(add_set)
    return generated_sets


def create_customized_numbers(preferred_count):
    """
    Creates a set of customized numbers based on user input.

    Args:
        preferred_count (int): Number of preferred numbers to be entered by the user.

    Returns:
        customized_nums (set): Set of customized numbers.
    """
    customized_nums = set()
    while len(customized_nums) < preferred_count:
        num = get_valid_number("Number {}: ".format(
            len(customized_nums) + 1), MIN_NUM, MAX_NUM)
        num = check_duplicate_number(num, customized_nums)
        if num is not None:
            customized_nums.add(num)
    return customized_nums


def get_valid_number(prompt, min_val, max_val):
    """
    Gets a valid number from user input within a specified range.

    Args:
        prompt (str): The prompt message for the user.
        min_val (int): The minimum allowed value for the number.
        max_val (int): The maximum allowed value for the number.

    Returns:
        num (int): The validated number if it is within the specified range.
    """
    while True:
        try:
            num = int(input(prompt))
            if min_val <= num <= max_val:
                return num
            else:
                print("Invalid number input. Please enter a number between {} and {}.".format(
                    min_val, max_val))
        except ValueError:
            print("Invalid number input. Please enter a valid integer.")


def check_duplicate_number(num, num_set):
    """
    Checks whether a number is a duplicate in a set of customized integers.

    Args:
        num (int): User input number.
        num_set (set): A set of customized integers.

    Returns:
        num (int): A unique integer to be added to the set, or None if the input number is already in the set.
    """
    if num not in num_set:
        return num
    else:
        print("Duplicate number entered. Please enter a unique number.")



def write_tickets_to_file(all_sets, filename):
    """
    Writes the generated sets to a text file.

    Args:
        all_sets (set): Set of generated sets.
        filename (str): Name of the file to write the sets to.

    Returns:
        None
    """
    with open(filename, 'w') as file:
        file.write("Generated Sets:\n")
        numbers_line = "Number:\t\t\t\t{}\n\n".format(
            "| ".join("{:02d}".format(num) for num in range(1, FIXED_LEN + 1)))
        file.write(numbers_line)
        sorted_sets = sorted(all_sets, key=lambda x: (sorted(x), x))
        
        for i, sorted_set in enumerate(sorted_sets, 1):
            formatted_set = "| ".join(
                "{:02d}".format(num) for num in sorted_set)
            file.write("Ticket {:02d}:\t\t{}\n".format(i, formatted_set))
            
        file.close()


def main():
    """
    Main function to generate sets of unique numbers and write them to a file.
    """
    preferred_count = get_valid_number(
        "How many preferred numbers do you have? ", 0, FIXED_LEN)
    customized_nums = create_customized_numbers(preferred_count)
    all_sets = generate_sets(customized_nums)
    write_tickets_to_file(all_sets, "JACKPOT.txt")
    print("*************************************************")
    print("* Numbers have been generated.\t\t\t*\n* Please check the text file named 'JACKPOT'.\t*\n* Thank you for using the service.\t\t*")
    print("*************************************************")


if __name__ == "__main__":
    main()


