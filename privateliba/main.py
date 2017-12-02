def hello_from_a():
    print("We are in library A. \n"
          "This library is dependent on another private library: 'privatelibb'")

    from privatelibb.main import hello_from_b
    hello_from_b()

hello_from_a()

