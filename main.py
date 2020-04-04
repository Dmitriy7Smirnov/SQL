import postgresql

def main():
    user = 'postgres'
    password = 'password'
    host = 'localhost'
    port = '5432'
    database = 'postgres'

    db = postgresql.open('pq://{0}:{1}@{2}:{3}/{4}'.format(user, password, host, port, database))

    query  = 'SELECT name, department, salary ' \
             'FROM employee ' \
             'WHERE salary IN(SELECT MAX(salary) FROM employee GROUP BY department)' \
             'ORDER BY salary DESC, name ASC'

    employees = db.query(query)
    print('(name, department, salary)\n')

    for employee in employees:
        print(employee)

if __name__ == '__main__':
    main()