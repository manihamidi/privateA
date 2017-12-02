def hello_from_a():
    print("We are in library A. \n"
          "This library is dependent on another private library: 'privatelibb'")

    try:
        from privatelibb.main import hello_from_b
        hello_from_b()
    except Exception as e:
        print("Oops! Doesn't look like the dependency got installed!")

hello_from_a()

