def create_shirt(size='large', message='Love is art!'):
    """Give an overview of the shirt that will be produced."""
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')
create_shirt()
create_shirt(size='medium')
create_shirt('small', 'I enjoy making art.')