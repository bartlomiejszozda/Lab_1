import os

def grep_and_write_solutions_to_file(file, what_search):
    lines_with_expression=[]
    try:
        #list_of_lines = []
        file=open(file,"r")
        for line in file:
            #list_of_lines.append(line)
            if line.count(what_search[:]):
                #lines_with_expression.append(line)
                solutions_file.write(line)
        solutions_file.write('\n')
        solutions_file.write('\n')
    finally:
        file.close()
    return lines_with_expression


try:

    files=["baseline_BdJPsiKs_MagD.log"]
    files.append("DR_BdJPsiKs_MagD_1k.log")
    files.append("DR_NE_BdJPsiKs_MagD.log")
    files.append("DR_NE_BdJPsiKs_MagD_1k.log")
    search="PrChecker.Downs"
    solutions_file=open("solutions.txt","w")
    for file_name in files:
        grep_and_write_solutions_to_file(file_name, search)

    #os.system("jupyter notebook ./" + solutions_file)
finally:
    solutions_file.close()

"""
    def user_interface():
        try:
            solution_file = open("solution.txt", "w")
            print("Write phrase or mark")
            what_search = input()
            more = 'y'
            while (more == 'y'):
                print("Write file name for search")
                file = input()
                write_solution_to_file(file, what_search, solution_file)
                print("more files for search? (y/n)")
                more = input()
            print("solution is in solution.txt file")
        finally:
            solution_file.close()
"""