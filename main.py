day = int(input("Select which day: "))

match day:
    case 1:
        import py.d01 as d01
        d01.main()
    case 2:
        import py.d02 as d02
        d02.main()
        