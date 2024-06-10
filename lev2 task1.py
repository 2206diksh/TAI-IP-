def luhn_check(card_number):
    """
    Validate a credit card number using the Luhn algorithm.

    :param card_number: The credit card number as a string
    :return: True if the card number is valid, False otherwise
    """
    def digits_of(n):
        return [int(d) for d in str(n)]
    
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    
    return checksum % 10 == 0

def is_valid_credit_card(card_number):
    """
    Check if the provided credit card number is valid.

    :param card_number: The credit card number as a string
    :return: True if the card number is valid, False otherwise
    """
    # Check if the card number only contains digits
    if not card_number.isdigit():
        return False

    # Perform Luhn check
    return luhn_check(card_number)
