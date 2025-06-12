import os

def get_files_info(working_directory, directory=None):
    try:
        if not os.path.isdir(working_directory):
            return 'Error: Working directory invalid'

        # Resolve and validate target directory
        target_directory = working_directory

        if directory:
            full_path = os.path.abspath(os.path.join(working_directory, directory))
            working_directory_abs = os.path.abspath(working_directory)

            # Prevent escape via path traversal
            if not full_path.startswith(working_directory_abs):
                return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

            if not os.path.isdir(full_path):
                return f'Error: "{directory}" is not a directory'

            target_directory = full_path

        # Build output listing
        result = []
        for item in os.listdir(target_directory):
            item_path = os.path.join(target_directory, item)
            size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)
            result.append(f'- {item}: file_size={size} bytes, is_dir={is_dir}')

        return "\n".join(result)

    except (FileNotFoundError, PermissionError, NotADirectoryError, OSError) as e:
        return f"Error: {str(e)}"
