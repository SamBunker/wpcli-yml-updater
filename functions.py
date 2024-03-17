captured_lines = []

# Change from is __ in line to checking if the line matches the regex of the original file. Otherwise the script won't read the file properly.
def split_the_file(filename):
  before_build = []
  build = []
  plugins = []
  themes = []
  current_section = "before_build"
  try:
    with open(filename, "r") as f:
      for line in f:
        if "build:" in line:
          current_section = "build"
        elif "plugins:" in line:
          current_section = "plugins"
        elif "themes:" in line:
          current_section = "themes"

        match current_section:
          case "before_build":
            before_build.append(line)
          case "build":
            build.append(line)
          case "plugins":
            plugins.append(line)
          case "themes":
            themes.append(line)

    print("1. File Successfully Loaded and Split")
    return before_build, build, plugins, themes
  except FileNotFoundError:
    print(f"File '{filename}' not found.")
    return []

def get_build_version(array):
  try:
    lines = [line.strip() for line in array]
    lines.pop(0)
  except:
    print(f"Array '{array}' is empty.")
    return []

def get_versions_from_array(array):
  try:
    plugin_names = [line.strip() for line in array]
    plugin_names.pop(0)
    return plugin_names
  except FileNotFoundError:
    print("Error: Plugin names array not found!")
    return []

def write_to_file(array):
  print("7. Exporting Everything to Output File")
  try:
    with open("txts/export.txt", "w") as f:
      for text in array:
        f.write(f"{text}\n")
  except FileNotFoundError:
    print("Error: Export file not found!")

s = []

def categorize_plugins(text):
  wordpress = []
  company = []
  temp = []
  wp_disabled = []
  company_disabled = []
  for line in text:
    if line.strip():
      parts = line.split(":")
      temp.append(parts)

  def pop_enumerate(int):
    for i in range(int):
      temp.pop(0)
  
  while len(temp) > 0:
    try:
      if temp[0][1] == "":
        if temp[1][0] == "version" and temp[2][0] == "source":
          try:
            if temp[3][0] != None and temp[3][0] == "inactive":
              company_disabled.append(temp[0][0])
              pop_enumerate(4)
            else:
              company.append(temp[0][0])
              pop_enumerate(3)
          except IndexError:
            company.append(temp[0][0])
            pop_enumerate(3)
            pass
        if temp[1][0] == "version" and temp[2][0] == "inactive":
          wordpress.append(temp[0][0])
          wp_disabled.append(temp[0][0])
          pop_enumerate(3)
      if temp[0][1] != "":
        if temp[0][0] != "source" and temp[0][0] != "version" and temp[0][0] != "inactive":
          wordpress.append(temp[0][0])
          pop_enumerate(1)
    except IndexError:
      pass

  return wordpress, company, wp_disabled, company_disabled

def strip_themes(array, yearly_theme):
  themes = []
  for line in array:
    themes.append(line)

  temp = [line.strip() for line in array]
  themes.pop(0)
  temp.pop(0)
  
  def pop_enumerate(int, index):
    for i in range(int):
      themes.pop(index)

  yearlys = ['twentytwenty', 'twentytwentyone', 'twentytwentytwo', 'twentytwentythree', 'twentytwentyfour']
  for year in yearlys:
    if (year + ":") in temp:
      yearly_inactive = True
      index = temp.index(year + ":")
      try:
        if "version" in temp[index + 1]:
          try:
            if "inactive" in temp[index + 2]:
              check_inactive = temp[index + 2].split(":")
              if "true" in check_inactive[1]:
                yearly_inactive = True
              else:
                yearly_inactive = False
              pop_enumerate(3, index)
            else:
              pop_enumerate(2, index)
              yearly_inactive = False
          except IndexError:
            pop_enumerate(2, index)
            yearly_inactive = False
            pass
      except IndexError:
        pop_enumerate(1, index)
        pass

  return themes, yearly_inactive