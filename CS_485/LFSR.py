def step_forward(seed, tap_pos):
    # step 1: calculate the bit being generated
    # make seed str, so be able to fetch each digit
    bit_generated = str(int(seed[tap_pos]) ^ int(seed[-1]))
    # move right,discard the last bit
    seed = bit_generated + seed[:-1]

    return seed


def LFSR(n, init_seed, tap_pos, bits_num):
    seed = init_seed
    result = []
    for i in range(bits_num):
        seed = step_forward(seed, tap_pos)
        result.append(seed[0])
    return "".join(result)


n = 4
seed = "1101"
tap_pos = 1

print(LFSR(4, init_seed=seed, tap_pos=1, bits_num=40))