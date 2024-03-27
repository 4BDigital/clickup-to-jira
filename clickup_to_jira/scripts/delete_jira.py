import os

from clickup_to_jira.handlers import JIRAHandler

jira_handler = JIRAHandler(
    os.getenv("JIRA_URL"),
    basic_auth=(os.getenv("JIRA_USER"), os.getenv("JIRA_API_KEY")),
)

i=900
while i < 1000:
    try:
        print(i)
        jira_handler.delete_issue(f"PRO-{i}")
    except Exception as e:
        print(e)
    i+=1
