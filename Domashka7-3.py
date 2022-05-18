def merge_files_into_one(dict_files, result):

    for file_name in dict_files.keys():
        lines = []
        with open(file_name) as file_obj:
            string_list = file_obj.readlines()
            lines.append(len(string_list))
            lines.append(string_list)
            dict_files[file_name] = lines

    list_files = list(dict_files.items())
    list_files.sort(key=lambda i: i[1])

    with open(result, 'a') as file_obj:
        number_iterations = 0
        for list_data in list_files:
            file_obj.write(list_data[0] + '\n')
            file_obj.write(str(list_data[1][0]) + '\n')
            number_iterations += 1
            for list_item in list_data[1][1]:
                file_obj.write(list_item)
            if number_iterations < len(list_files):
                file_obj.write('\n')

dict_files = {'1.txt': '', '2.txt': '', '3.txt': '', '4.txt': '', '5.txt': ''}
result = 'result.txt'
merge_files_into_one(dict_files, result)