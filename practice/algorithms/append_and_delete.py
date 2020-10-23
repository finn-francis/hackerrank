def appendAndDelete(original, target, n):
    original_length = len(original)
    target_length   = len(target)

    # If n is greater than the total length of both strings or zero we know it will always be true
    if n >= original_length + target_length or n == 0:
        return "Yes"

    matching_string = ""
    for index, char in enumerate(original):
        if index < target_length and char == target[index]:
            matching_string += char
        else:
            break

    matching_length = len(matching_string)
    diff = abs(original_length - matching_length) + abs(target_length - matching_length)

    if diff == 0:
        return "Yes" if n % 2 == 0 else "No"
    # if diff is 1 we get a false positive due to the remainder always being 0
    elif n % diff == 0 and diff != 1:
        return "Yes"
    else:
        return "Yes" if n > diff and diff % 2 == n % 2 else "No"
