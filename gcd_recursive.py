def gcd(a, b, no_of_recursive_calls):
        """The GCD (greatest common divisor) is the highest number that evenly divides both width and height."""
        no_of_recursive_calls += 1
        print "\nCalled with a = ", a, "b = ", b, "no_of_recursive_calls = ", no_of_recursive_calls, "Next call will be b, a%b"
        return a if b == 0 else gcd(b, a % b, no_of_recursive_calls)
'''
GCD of 15 and 160 is
End of Call 1 160 and 15%160 which is 15 will be called. Solves for me, if lower number is called, quotient will always be lower number ,..
'''

print "GCD of 15 and 160 is ",gcd(15,160, 0)
print "GCD of 160 and 15 is ",gcd(160,15, 0)
print "GCD of 160 and 159 is ",gcd(160,159, 0)
print "GCD of 160000 and 159000 is ",gcd(160000,159000, 0)
