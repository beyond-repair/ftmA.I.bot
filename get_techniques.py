def get_techniques():
    techniques = []
    with open('techniques.txt') as f:
        for line in f:
            techniques.append(line.strip())
    return techniques
