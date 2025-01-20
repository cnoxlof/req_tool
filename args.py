
commands = [
    "command -x --output result.txt --input input.txt",
    "command -v --verbose --output output.log",
    "command --example --input data.txt --output result.csv",
    "command --verbose --input file.txt",
    "command -x --verbose --output log.txt"
]


test = "command -x --output result.txt --input input.txt"

def parse_args(data):
    data = data.split(' ')
    cmd = data[0]

    flags = []


    for i in range(len(data)):
        if data[i][0] == '-':
            if i != len(data):
                if data[i+1][0] != '-':
                    flags.append((f'[{data[i]}]',data[i+1]))
                else:
                    flags.append(f'[{data[i]}]')



                
            





    print(cmd,flags)


parse_args(test)
