from bs4 import BeautifulSoup
import requests
import re
from config import *

def get_yearlyTheme(core_version):  
  core_version_float = float(0)

  if (core_version.count(".") == 1): core_version_float = (float(core_version.replace('.', '')) * 10)
  elif (core_version.count(".") == 2): core_version_float = (float(core_version.replace('.', '')) * 1)

  if core_version_float > 640:
    url = "https://wordpress.org/themes/twentytwentyfour/"
  elif core_version_float > 610 and core_version_float < 640:
    url = "https://wordpress.org/themes/twentytwentythree/"
  yearly_theme = url.split("/")[-2:][0]
  response = requests.get(url)
  if response.status_code == 200:
    return yearly_theme, response.text
  else:
    raise ValueException("Error fetching webpage: " + str(response.status_code))

def get_versionYearlyTheme(core_version):
  yearly_theme, page_content = get_yearlyTheme(core_version)
  
  soup = BeautifulSoup(page_content, 'html.parser')
  version_element = soup.select_one(".theme-meta-info").text
  version_parts = version_element.split("Version:", 1)
  if len(version_parts) == 2:
    version = version_parts[1].strip().split(":")[0].strip()[:10]
    version = version.replace(" ", "").replace("\n", "")
    pattern = r"^\s+|\s+$"
    version = re.sub(pattern, "", version, flags=re.MULTILINE)
    return yearly_theme, version
  else:
    version = None

def get_webpageCore(array):
  url = "https://developer.wordpress.org/block-editor/contributors/versions-in-wordpress/"
  response = requests.get(url)
  if response.status_code == 200:
    return response.text
  else:
    raise ValueException("Error fetching webpage: " + str(response.status_code))

def get_versionCore(array):
  page_content = get_webpageCore(array)

  if (MANUAL_LATEST_RELEASE != ""):
    latest_release = MANUAL_LATEST_RELEASE
    return latest_release
  
  soup = BeautifulSoup(page_content, 'html.parser')
  version_element = soup.select_one("figure.wp-block-table table tbody tr td:nth-child(2)").text
  return version_element

# Find Plugin on WordPress Plugin Website
def get_webpageWP(plugin_name):
  url = f"https://wordpress.org/plugins/{plugin_name}/"
  response = requests.get(url)
  if response.status_code == 200:
    return response.text
  else:
    raise ValueError(f"Error fetching webpage: {response.status_code}")

# Get Version Handler for Plugin (Fetches website)
def get_versionWP(plugin_name):
  page_content = get_webpageWP(plugin_name)
  soup = BeautifulSoup(page_content, "html.parser")

  version_element = soup.select_one(".entry-meta").text

  version_parts = version_element.split("Version:", 1)
  if len(version_parts) == 2:
    version = version_parts[1].strip().split(":")[0].strip()[:10]
    version = version.replace(" ", "").replace("\n", "")
    pattern = r"^\s+|\s+$"
    version = re.sub(pattern, "", version, flags=re.MULTILINE)
    return version
  else:
    version = None

# Find Plugin on Company Plugin Website
def get_webpageC(plugin_name):
  url = f"REDACTED URL"
  # URL fetches like, f"https//:www.google.com/plugins/{plugin_name}/"
  response = requests.get(url)
  if response.status_code == 200:
    return response.text
  else:
    raise ValueError(f"Error fetching webpage: {response.status_code} for {plugin_name}")

def get_versionC(plugin_name):
  page_content = get_webpageC(plugin_name)
  soup = BeautifulSoup(page_content, "html.parser")

  # Find the element containing the version string
  version_element = soup.select_one("table").text
  for line in reversed(version_element.splitlines()):
    if line:
      version = line.split(".zip")[0]
      return version
      break
  else:
    print("No non-empty line found.")