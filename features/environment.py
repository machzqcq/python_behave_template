from selenium import webdriver
from colorama import init


def before_all(context):
     print("Executing before all")
     init()

def before_feature(context, feature):
     print("Before feature\n")

#Scenario level objects are popped off context when scenario exits
def before_scenario(context,scenario):
    context.browser = webdriver.Chrome()
    print("Before scneario\n")

def after_scenario(context,scenario):
    context.browser.quit()

def after_feature(context,feature):
     print("\nAfter feature")

def after_all(context):
     print("Executing after all")

