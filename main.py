from functions import *
from webscraping import *
from config import *

print("Script Author: Samuel Bunker" + "\n" + "Script Version: " + SCRIPT_VERSION + "\n" + "Description: " + SCRIPT_DESCRIPTION + "\n\n" + PERSONAL_AD + "\n")

# Version 2.0
before_build, build, plugins, themes = split_the_file("txts/yml-paste.txt")

new_build = get_versionCore(get_build_version(build))
print("2. Fetched Latest Core Version")

wordpress, company, wp_disabled, company_disabled = categorize_plugins(get_versions_from_array(plugins))
print("3. Fetched Plugins and their Versions")

yearly_theme, theme_version = get_versionYearlyTheme(new_build)
chopped_themes, yearly_inactive = strip_themes(themes, yearly_theme)
print("4. Fetched Latest Twenty Theme")

print("5. Fetching Wordpress Plugins")
for plugin_name in wordpress:
  version = get_versionWP(plugin_name)
  if version:
    if plugin_name in wp_disabled:
      s.append(plugin_name + ":\n            version: " + version + "\n            inactive: true")
    else:
      s.append(plugin_name + ": " + version)
  else:
    print(f"Version for {plugin_name}: not found.")

print("6. Now fetching Company Plugins")
for plugin_name in company:
  version = get_versionC(plugin_name)
  if version:
    if plugin_name in company_disabled:
      s.append(plugin_name + ":\n            version: " + version + "\n            source: jpl" + "\n            inactive: true")
    else:
      s.append(plugin_name + ":\n            version: " + version + "\n            source: jpl")
  else:
    print(f"Version for {plugin_name}: not found.")

def build_the_file(before_build, build, plugins, themes):
  contents = []
  for line in before_build:
    contents.append(line.replace("\n", ""))
  contents.append("build:")
  contents.append("    core: " + build.strip())
  contents.append("    plugins:")
  plugins.sort()
  tab = "    "
  for line in plugins:
      contents.append("{}{}{}".format(tab, tab, line))
  contents.append("    themes:")
  for line in chopped_themes:
    contents.append("{}".format(line.replace("\n", "")))
  contents.append("        " + yearly_theme + ":")
  contents.append("            " + "version: " + theme_version)
  if yearly_inactive:
    contents.append("            inactive: true")
  write_to_file(contents)
  print("✅ Script Completed with 0 Errors")

build_the_file(before_build, new_build, s, themes)