import os

def get_work_path(*sub_dir_paths):
    work_dir_path = os.path.dirname((os.path.dirname(os.path.realpath(__file__))))
    if sub_dir_paths:
        return os.path.join(work_dir_path, *sub_dir_paths)
    else:
        return work_dir_path
