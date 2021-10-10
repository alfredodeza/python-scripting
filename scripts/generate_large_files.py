import os
count = 0 
with open('../large_files.py', 'w') as _files:
    _files.write('files = [\n')

with open('../large_files.py', 'a') as _files:
    
    for root, directories, files in os.walk('/Users/alfredo/Library/Application Support'):
        for _file in files:
            if count > 2000:
                break
            try:
                full_path = os.path.join(root, _file)
                size = os.path.getsize(full_path)
            except (FileNotFoundError,PermissionError):
                continue
            _files.write(f"('{full_path}', {size}),\n")
            
            count += 1
    _files.write(']')
