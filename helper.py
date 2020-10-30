from jira import JIRA


class JiraHelper:

    def __init__(self, user_name, password, server):
        self.jira = JIRA(basic_auth=(user_name, password), options={"server": server})


    def search(self):
        issue = self.jira.projects()
        print(issue)

    def sprint(self):
        issues = []
        count=0
        issues_in_project = self.jira.search_issues(
            'project=23240 AND SPRINT not in closedSprints() AND sprint not in futureSprints()')
        issues.extend(issues_in_project)
        #print(issues_in_project)
        for i in issues:
            if i.fields.assignee is None:
                count = count+1
        print(count)
        return str(count)
