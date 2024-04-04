def improvement(filename):
    """
    Find all students who have shown an improvement
    
    Argument:
        filename: string, path to file
    Return: 
        count: integer
    """
    with open(filename, 'r') as file:
            heading = file.readline()
            with open('python.csv', 'w') as python_file:
                python_file.write(heading)
                
                for line in file:
                    seqno, name, gender, ct, python, pdsa = line.strip().split(',')
                    if gender == 'M' and int(python) >= 70:
                        python_file.write(line)
