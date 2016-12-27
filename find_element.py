def find_element(json, path):
    '''
    Takes dumped JSON and path to item nested within it,
    returns the nested items as a generator.
    '''
    key = path[0]
    if len(path) == 1:
        if key == '*':
            for item in json:
                try:
                    yield item
                except Exception as e:
                    print e

        # Handle other keys
        else:
            try:
                yield json[key]
            except KeyError:
                pass

    elif len(path) > 1:
        # Remove front of path, since it's being worked on
        path.pop(0)
        # Do I want to work with a copy of path? 
        for n,k in enumerate(json):
            if key == '*':
                # Handle dictionaries:
                if type(json) == dict:
                    for element in find_element(json[k], path):
                        yield element
                # Handle other arrays:
                elif iter(json):
                    for element in find_element(json[n], path):
                        yield element
                # else handle strings, int, objs, etc?

            # When key is specified:
            elif k == key:
                # Handle dictionaries:
                if type(json) == dict:
                    for element in find_element(json[key], path):
                        yield element 
                # Handle other arrays:
                elif iter(json):
                    for element in find_elment(json[n], path):
                        yield element
