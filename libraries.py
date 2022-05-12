from headless import windowsHeadless
from headless import linuxHeadless
from selenium import webdriver
from time import sleep
import datetime 
import csv
import os
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from utilities import verify_file, update_csv, new_csv