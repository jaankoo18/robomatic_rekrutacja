import os
import datetime as dt

def sort_files(path):

    roots_dict = {}

    for (root, dirs, files) in os.walk(path, topdown=True):
        roots_dict[root] = (dirs, files)

    #files
    changed_files_counter = 0
    for i in roots_dict:
        for j in roots_dict[i][1]:
            path = i +'\\' + j
            time = dt.datetime.fromtimestamp(os.path.getctime(path))
            time = time.strftime("%Y-%m-%d")
            if not str(j).startswith(time + "_"):
                os.rename(path, i + '\\' + time + '_' + j)
                changed_files_counter += 1

    #dict
    changed_dir_counter = 0
    for path in reversed(roots_dict):
        time = dt.datetime.fromtimestamp(os.path.getctime(path))
        time = time.strftime("%Y-%m-%d")

        name_dir = str(path)[str(path).rfind('\\')+1:]
        path_front = str(path)[:str(path).rfind("\\")]
        new_path = path_front + '\\' + time + '_' + name_dir
        if not name_dir.startswith(time + '_'):
            os.rename(path, new_path)
            changed_dir_counter += 1

    return f"Number of changed files is {changed_files_counter}. \nNumber of changed directories is {changed_dir_counter}. \n"
