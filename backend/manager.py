import project_scripts.mysqlManager as mysqlManager


def main():
    inp = input("what do you want to do ? ")
    if (inp == 'drop all tables'):
        mysqlManager.drop_all()
        print("ok")
    elif (inp == 'create all tables'):
        mysqlManager.create_all()
        print("ok")
    elif (inp == 'quit'):
        print('bye')
        return
    else:
        print("no this command")
    main()


main()

