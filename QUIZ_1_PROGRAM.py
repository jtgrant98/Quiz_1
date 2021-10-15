import QUIZ_1_CLASS as x

def main():

    project_1 = x.Project(1001,'SAP Implementation',25,'09/30/2022')
    project_2 = x.Project(1002,'Migration to CRM',10,'06/30/2022')

    print(project_1.get_projID())
    print(project_1.get_projDesc())
    print(project_1.get_consultants())
    print(project_1.get_dueDate())


    print(project_2.get_projID())
    print(project_2.get_projDesc())
    print(project_2.get_consultants())
    print(project_2.get_dueDate())





dict = {
    'Proj1' : {'dueDate' : '09/30/2022'},
    'Proj2' : {'dueDate' : '06/30/2022'}}


print(dict)
main()