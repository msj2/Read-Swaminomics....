def gcd(num1, num2, no_of_recursive_calls):
# modulo divide one by the other, if smaller number is divided by bigger, ..
        no_of_recursive_calls += 1
        print "\na = ", a, "b = ", b, "no_of_recursive_calls = ", no_of_recursive_calls
        return a if b == 0 else gcd(b, a % b, no_of_recursive_calls)

'''
GCD of 15 and 160 is
End of Call 1 160 and 15%160 which is 15 will be called. Solves for me, if lower number is called, quotient will always be lower number ,..
'''
print "GCD of 15 and 160 is ",gcd(15,160, 0)
print "GCD of 160 and 15 is ",gcd(160,15, 0)
