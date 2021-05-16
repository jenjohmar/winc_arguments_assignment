# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line


def greet(name, greeting='Hello, <name>!'): #function takes a positional argument and a keyword argument
    x = greeting.replace('<name>', name)
    #replaces the string '<name>' within the greeting string passed into the call with the first argument (name)
    return x
    # returns the greeting string with '<name>' replaced by whatever string was passed as first argument


def force(mass, body='earth'):
    # dict van 11 planeten
    planets = {
        'sun': 274.0,
        'jupiter': 24.9,
        'neptune': 11.2,
        'saturn': 10.4,
        'earth': 9.8,
        'uranus': 8.9,
        'venus': 8.9,
        'mars': 3.7,
        'mercury': 3.7,
        'moon': 1.6,
        'pluto': 0.6
    }
    
    # force = mass in kg * gravity (m/square second)
    
    value_body = planets[body]
    
    sum = mass * value_body
    #formatted_sum = "{:.2f}".format(sum)
    
    return sum
    #return formatted_sum


    

def pull(m1,m2,d):

    # pull = g x ((weight_m1 x weight_m2) / d**2)
    # G is the gravitational constant, approximately 6,674×10-11 N m2/kg2
    
    g = 6.674 * (10 ** -11)
    
    sum = g * ((m1 * m2) / (d ** 2))

    return sum


