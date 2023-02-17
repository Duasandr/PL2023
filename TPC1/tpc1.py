import sys

from myheart import MyHeart


def main():
    arguments = sys.argv[1:]

    if len(arguments) > 1:
        data = MyHeart(arguments[0])

        if arguments[1] == "--age" or arguments[1] == "-a":
            if len(arguments) > 2 and (arguments[2] == "--graph" or arguments[2] == "-g"):
                data.ageDist.show_graph()
            else:
                print(data.ageDist)
            return

        if arguments[1] == "--gender" or arguments[1] == "-gen":
            if len(arguments) > 2 and (arguments[2] == "--graph" or arguments[2] == "-g"):
                data.genderDist.show_graph()
            else:
                print(data.genderDist)
            return

        if arguments[1] == "--cholesterol" or arguments[1] == "-col":
            if len(arguments) > 2 and (arguments[2] == "--graph" or arguments[2] == "-g"):
                data.cholesterolDist.show_graph()
            else:
                print(data.cholesterolDist)
            return


if __name__ == "__main__":
    main()
