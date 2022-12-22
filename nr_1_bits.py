from sys import getsizeof

# We are not able to conver negative numbers... review this
def bin_to_int(bin_str):

    # skip the sign bit
    # j = 0
    # while bin_str[j] != '1' and j < len(bin_str):
    #     j += 1
    # if j == len(bin_str):
    #     return 0
    expo = 0 
    nr = 0
    i = len(bin_str)-1
    while i >= 0:
        if bin_str[i] == '1':
#            nr += 2 ** expo
            nr |= (1 << expo)
        expo += 1
        i -= 1
    return nr 

def hamming_weight( n ):
    ones = 0
    bits_size = getsizeof(n) * 8
#    print (bits_size)
#    print ('{0:b}'.format(n))
    while bits_size >= 0:
        if ( n & 1 ):
            ones += 1
        n >>= 1
        bits_size -= 1
    return ones

print (hamming_weight( 5 ), '{0:b}'.format(5))
print (hamming_weight( 31 ), '{0:b}'.format(31))
print (hamming_weight( 128 ), '{0:b}'.format(128))
print (hamming_weight( 64 ), '{0:b}'.format(64))
print (bin_to_int('{0:b}'.format(5)) == 5, '{0:b}'.format(-5))
print (bin_to_int('{0:b}'.format(64)) == 64, '{0:b}'.format(64))
print (bin_to_int('{0:b}'.format(128)) == 128, '{0:b}'.format(128))
print (bin_to_int('{0:b}'.format(32768)) == 32768, '{0:b}'.format(32768))
print (bin_to_int('111')) 