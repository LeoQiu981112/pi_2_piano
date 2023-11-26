DIGITS = 1000

def pi_digits(x):
    """Generate x digits of Pi."""
    k,a,b,a1,b1 = 2,4,1,12,4
    while x > 0:
        p,q,k = k * k, 2 * k + 1, k + 1
        a,b,a1,b1 = a1, b1, p*a + q*a1, p*b + q*b1
        d,d1 = a/b, a1/b1
        while d == d1 and x > 0:
            yield int(d)
            x -= 1
            a,a1 = 10*(a % b), 10*(a1 % b1)
            d,d1 = a/b, a1/b1


def find_closest_next_note(last_note: float, current_digit: int, scale):
    current_note = scale[current_digit]
    if abs(current_note - last_note) <= 6.:
        return current_note

    # 1-7 
    # cur_note 1-7
    # previous 0,8,9

    if current_note > last_note:
        current_note -= int( (current_note - last_note + 6)/12 ) * 12.
        return current_note

    current_note += int( (last_note - current_note + 6)/12 ) * 12.
    return current_note