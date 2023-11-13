def describe_city(city, country='Uk'):
    """Describe a city."""
    msg = city + " is in " + country + "."
    print(msg)

describe_city('London')
describe_city('roma', 'Italy')
describe_city('England')