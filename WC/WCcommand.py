def WC(file, what_search):

    try:
        how_many = 0
        file=open(file,"r")
        for line in file:
            how_many+=line.count(what_search[:])
    finally:
        file.close()
    return how_many


def write_solution_to_file(file, what_search,solution_file):
    try:
        solution_file.write("Phrase ")
        solution_file.write(what_search)
        solution_file.write(" was found ")
        solution_file.write(str(WC(file, what_search)))
        solution_file.write(" times'\n'")
    except:
        print("something go wrong")




def user_interface():
    try:
        solution_file = open("solution.txt", "w")
        print("Write phrase or mark")
        what_search=input()
        more='y'
        while( more=='y'):
            print("Write file name for search")
            file=input()
            write_solution_to_file(file, what_search,solution_file)
            print("more files for search? (y/n)")
            more=input()
        print("solution is in solution.txt file")
    finally:
        solution_file.close()

user_interface()