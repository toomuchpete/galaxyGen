import smhasher, math, random, time

GLOBAL_SEED = None

def getSeed():
    global GLOBAL_SEED
    if GLOBAL_SEED == None:
        setSeed(str(time.time()))

    return GLOBAL_SEED

def setSeed(new_seed):
    global GLOBAL_SEED
    GLOBAL_SEED = new_seed

def random2d(x, y, seed = ''):
    hashval = smhasher.murmur3_x86_128(getSeed() + "_" + seed + "_" + str(x) + "_" + str(y))
    return float(hashval) / (2 ** 128)