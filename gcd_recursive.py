def gcd(a, b, no_of_recursive_calls):
        """The GCD (greatest common divisor) is the highest number that evenly divides both width and height."""
        no_of_recursive_calls += 1
        print "\na = ", a, "b = ", b, "no_of_recursive_calls = ", no_of_recursive_calls
        return a if b == 0 else gcd(b, a % b, no_of_recursive_calls)


print "GCD of 15 and 160 is ",gcd(15,160, 0)
print "GCD of 160 and 15 is ",gcd(160,15, 0)
