"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 0123456
Name:       Xxxx Yyyyyy
Email:      xxxx.yyyyyy@tuni.fi

Project 3: ...
"""


def find_route(data, departure, destination):
    """
    This function tries to find a route between <departure>
    and <destination> cities. It assumes the existence of
    the two functions fetch_neighbours and distance_to_neighbour
    (see the assignment and the function templates below).
    They are used to get the relevant information from the data
    structure <data> for find_route to be able to do the search.

    The return value is a list of cities one must travel through
    to get from <departure> to <destination>. If for any
    reason the route does not exist, the return value is
    an empty list [].

    :param data: ?????, A data structure of an unspecified type (you decide)
           which contains the distance information between the cities.
    :param departure: str, the name of the departure city.
    :param destination: str, the name of the destination city.
    :return: list[str], a list of cities the route travels through, or
           an empty list if the route can not be found. If the departure
           and the destination cities are the same, the function returns
           a two element list where the departure city is stores twice.
    """

    # +--------------------------------------+
    # |                                      |
    # |     DO NOT MODIFY THIS FUNCTION!     |
    # |                                      |
    # +--------------------------------------+

    if departure not in data:
        return []

    elif departure == destination:
        return [departure, destination]

    greens = {departure}
    deltas = {departure: 0}
    came_from = {departure: None}

    while True:
        if destination in greens:
            break

        red_neighbours = []
        for city in greens:
            for neighbour in fetch_neighbours(data, city):
                if neighbour not in greens:
                    delta = deltas[city] + distance_to_neighbour(data, city, neighbour)
                    red_neighbours.append((city, neighbour, delta))

        if not red_neighbours:
            return []

        current_city, next_city, delta = min(red_neighbours, key=lambda x: x[2])

        greens.add(next_city)
        deltas[next_city] = delta
        came_from[next_city] = current_city

    route = []
    while True:
        route.append(destination)
        if destination == departure:
            break
        destination = came_from.get(destination)

    return list(reversed(route))


def read_distance_file(file_name):
    """
    Reads the distance information from <file_name> and stores it
    in a suitable data structure (you decide what kind of data
    structure to use). This data structure is also the return value,
    unless an error happens during the file reading operation.

    :param file_name: str, The name of the file to be read.
    :return: ????? | None: A data structure containing the information
             read from the <file_name> or None if any kind of error happens.
             The data structure to be chosen is completely up to you as long
             as all the required operations can be implemented using it.
    """

    # +----------------------------------------------------------------+
    # |                                                                |
    # |  TODO: Implement your own version of read_distance_file here.  |
    # |                                                                |
    # +----------------------------------------------------------------+

    city_dict = {}

    try:
        data_file = open(file_name, "r")
    except OSError:
        return None

    try:
        for line in data_file:
            stripped_line = line.strip()
            split_line = stripped_line.split(";")

            key_city = split_line[0]
            payload_city = split_line[1]
            distance_between_cities = split_line[2]

            city_dict[key_city] = {payload_city, distance_between_cities}

    except ValueError:
        return None

    print(city_dict)

    return city_dict


def fetch_neighbours(data, city):
    """
    Returns a list of all the cities that are directly
    connected to parameter <city>. In other words, a list
    of cities where there exist an arrow from <city> to
    each element of the returned list. Return value is
    an empty list [], if <city> is unknown or if there are no
    arrows leaving from <city>.

    :param data: ?????, A data structure containing the distance
           information between the known cities.
    :param city: str, the name of the city whose neighbours we
           are interested in.
    :return: list[str], the neighbouring city names in a list.
             Returns [], if <city> is unknown (i.e. not stored as
             a departure city in <data>) or if there are no
             arrows leaving from the <city>.
    """

    # +--------------------------------------------------------------+
    # |                                                              |
    # |  TODO: Implement your own version of fetch_neighbours here.  |
    # |                                                              |
    # +--------------------------------------------------------------+


def distance_to_neighbour(data, departure, destination):
    """
    Returns the distance between two neighbouring cities.
    Returns None if there is no direct connection from
    <departure> city to <destination> city. In other words
    if there is no arrow leading from <departure> city to
    <destination> city.

    :param data: ?????, A data structure containing the distance
           information between the known cities.
    :param departure: str, the name of the departure city.
    :param destination: str, the name of the destination city.
    :return: int | None, The distance between <departure> and
           <destination>. None if there is no direct connection
           between the two cities.
    """

    # +-------------------------------------------------------------------+
    # |                                                                   |
    # |  TODO: Implement your own version of distance_to_neighbour here.  |
    # |                                                                   |
    # +-------------------------------------------------------------------+


def main():
    input_file = input("Enter input file name: ")

    distance_data = read_distance_file(input_file)

    if distance_data is None:
        print(f"Error: '{input_file}' can not be read.")
        return

    while True:
        action = input("Enter action> ")

        if action == "":
            print("Done and done!")
            return

        elif "display".startswith(action):
            # +----------------------------------------+
            # |                                        |
            # |  TODO: Implement "display" action.     |
            # |                                        |
            # +----------------------------------------+
            ...

        elif "add".startswith(action):
            # +----------------------------------------+
            # |                                        |
            # |  TODO: Implement "add" action.         |
            # |                                        |
            # +----------------------------------------+
            ...

        elif "remove".startswith(action):
            # +----------------------------------------+
            # |                                        |
            # |  TODO: Implement "remove" action.      |
            # |                                        |
            # +----------------------------------------+
            ...

        elif "neighbours".startswith(action):
            # +----------------------------------------+
            # |                                        |
            # |  TODO: Implement "neighbours" action.  |
            # |                                        |
            # +----------------------------------------+
            ...

        elif "route".startswith(action):
            # TODO: Implement "route" action.
            # +----------------------------------------+
            # |                                        |
            # |  TODO: Implement "route" action.       |
            # |                                        |
            # +----------------------------------------+
            ...

        else:
            print(f"Error: unknown action '{action}'.")


if __name__ == "__main__":
    main()
