def identify_visitors():
    kenyan_visitors = [4]
    ugandan_visitors = [2]

    num_visitors = 6
    count = 0

    while count < num_visitors:
        nationality = input("Enter the nationality of visitor {}: ".format(count + 1))

        if nationality.lower() == "kenya":
            kenyan_visitors.append("Visitor {}".format(count + 1))
        elif nationality.lower() == "uganda":
            ugandan_visitors.append("Visitor {}".format(count + 1))

        count += 1

    print("\nKenyan Visitors:")
    for visitor in kenyan_visitors:
        print(visitor)

    print("\nUgandan Visitors:")
    for visitor in ugandan_visitors:
        print(visitor)


if __name__ == "__main__":
    identify_visitors()



for x in range(2, 30, 3):
  print(x)
