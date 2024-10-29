def load_text_file(file_path):
  """
  Function to load and read a text file.
  
  Parameters:
  file_path (str): Path to the text file to load.
  
  Returns:
  str: Contents of the text file.
  """
  try:
      with open(file_path, 'r', encoding='utf-8') as file:
          file_content = file.read()
      return file_content
  except FileNotFoundError:
      return f"Error: File '{file_path}' not found."
  except Exception as e:
      return f"An error occurred: {e}"

