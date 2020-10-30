from helper import JiraHelper
from emailSender import Email

user_name = ""
password = ""
server = "https://jira.cybercom.com/"
jira = JiraHelper(user_name, password, server)
email = Email(jira.sprint())

jira.sprint()
email.send()

