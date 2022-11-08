import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if not os.path.isdir(path):
        return []
    
    files = os.listdir(path)
    if not len(files):
        return []
    
    results = []
    
    for file in files:
        if file.endswith(suffix):
            results.append(file)
            continue
            
        f_path = os.path.join(path, file)
        if os.path.isdir(f_path):
            results.extend(find_files(suffix, f_path))
    
    return results

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
print(find_files(".c", "./testdir"))

# Test Case 2
print(find_files(".h", "./testdir"))

# Test Case 3
print(find_files(".py", "./testdir"))

# Test Case 3
print(find_files(".py", "./no-thing"))