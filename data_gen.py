import names 
import random

departments = {
    'Sales': {
        'salary_range': (55000, 65000),
        'weight': 16
    },
    'Marketing': {
        'salary_range': (50000, 60000),
        'weight': 8
    },
    'Technology': {
        'salary_range': (85000, 100000),
        'weight': 14
    },
    'Admin': {
        'salary_range': (45000, 52000),
        'weight': 10
    },
    'Repair': {
        'salary_range': (40000, 48000),
        'weight': 35
    },
    'Customers': {
        'salary_range': (42000, 50000),
        'weight': 16
    },
    'Management': {
        'salary_range': (110000, 130000),
        'weight': 2
    }
}

dept_lst =['Sales','Marketing','Technology','Admin','Repair','Customers','Management']
weights=[16,8,13,10,35,16,2]



def gen_name():
    fname=names.get_first_name()
    lname=names.get_last_name()
    return fname , lname 

def gen_department():
    dept_name=list(departments.keys())
    weights =[departments [dept]['weight'] for dept in dept_name]
    dept = random.choices(dept_name,weights=weights , k=1)[0]
    return dept
    
def gen_salary():
    department=gen_department()
    salary_range = departments[department]['salary_range']
    salary = round(random.uniform(*salary_range))
    return salary
    
def generate_all():
    pass


def main():
    out =gen_salary()
    print(out)

if __name__ == "__main__":
    main()