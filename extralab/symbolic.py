from parse_symbolic import *

#########################################################################
### part 1: derivatives of polynomials and more general expressions #####
#########################################################################

def derivative(exp):  # TODO: return the derivative exp of an arbitrary exp
    print("cannot differentiate this function yet")

def exp2polynom(exp): # TODO: all the way from Exp to a polynomial
    print("cannot convert this function to polynomialyet")

def deriv_polynom(p): # TODO: return the derivative polynomial of p
    print("cannot differentiate this polynomial yet")


###############################################
## part 2: printing and parsing expressions ###
###############################################

def show_exp_infix(level,exp): # TODO: infix printing of expressions, minimizing parentheses
    return show_exp_prefix(exp)  # default behaviour, to be replaced


def show_polynom(p): # TODO printing polynomials: use + or - between terms, ignore 0 terms, 1 coefficients, and * signs
    return p  # default behaviour, to be replaced


###############################################
## The main function: test with your own input
###############################################

# the main function: input infix expression, show tree, polynomial, 1st and 2nd derivatives, and the graph
def main(): # given, don't change
    s = input("enter expression> ")
    toks = insert_mul(lex(s))
    exp = top_parse(toks)
    print("tree:", show_exp_prefix(exp))
    print("infix:", show_exp_infix(0,exp))
    try:
        dert = derivative(exp)
        print("derivative:", show_exp_infix(0,dert))
    except:
        print("derivative not available")
    try:
        poly = exp2polynom(exp)
        print("polynomial:", show_polynom(poly))
        der = deriv_polynom(poly)
        print("derivative of polynomial:", show_polynom(der))
        polydert = exp2polynom(dert)
        print("polynomial of derivative:", show_polynom(polydert))
        der2 = deriv_polynom(der)
        print("second derivative:", show_polynom(der2))
    except:
        print("polynomial not defined")
    show_graph(exp)
    
if __name__ == "__main__":
    main()
