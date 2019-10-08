import os

def read_file(file_loc):
    file_obj = open(file_loc)
    #print(file_obj.read())
    print(file_obj.readlines())
    #print(file_obj.read(10))


def write_file(file_loc):
    file_obj = open(file_loc, "w")
    file_obj.write("MY sample file for include_help\n")
    file_obj.write("I can write long long lines")
    file_obj.close()

def append_file(file_loc):
    file_obj = open(file_loc, "a")
    file_obj.write("\n appending the information")
    file_obj.close()

def with_read_operation(file_loc):
    with open(file_loc) as file_obj:
        data = file_obj.read()
    print(data)

def with_write_operation(file_loc):
    with open(file_loc, "w") as file_obj:
        file_obj.write("writing using with()")


if __name__ == '__main__':
    dir_name = os.path.dirname(__file__)
    file_name = os.path.join(dir_name, 'samples/sample_file.txt')
    read_file(file_name)
#     write_file_name = os.path.join(dir_name, 'samples/sample_file_1.txt')
#     write_file(write_file_name)
#     append_file(write_file_name)
#     read_file(write_file_name)
#     write_file_name = os.path.join(dir_name, 'samples/sample_file_2.txt')
#     with_write_operation(write_file_name)
#     with_read_operation(write_file_name)


