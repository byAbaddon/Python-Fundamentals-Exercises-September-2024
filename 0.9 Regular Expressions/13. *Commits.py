import re

pattern = re.compile(r"^https://github\.com/(?P<name>[A-Za-z\d\-]+)/"
                     r"(?P<repo>[A-Za-z_\-]+)/commit/(?P<hash>[A-Fa-f\d]{40}),(?P<message>.+),"
                     r"(?P<additions>\d+),(?P<deletions>\d+)$")

commits = {}
insert_order = 0

while True:
    line = input()
    if line == "git push":
        break

    match = re.fullmatch(pattern, line)
    if not match:
        continue

    user = match.group("name")
    repo = match.group("repo")
    commit_hash = match.group("hash")
    message = match.group("message")
    additions = int(match.group("additions"))
    deletions = int(match.group("deletions"))

    if user not in commits:
        commits[user] = {}
    if repo not in commits[user]:
        commits[user][repo] = []

    insert_order += 1
    commit = {
        "hash": commit_hash,
        "message": message,
        "additions": additions,
        "deletions": deletions,
        "order": insert_order
    }
    commits[user][repo].append(commit)

sorted_users = dict(sorted(commits.items()))

for user, repos in sorted_users.items():
    print(f"{user}:")
    sorted_repos = dict(sorted(repos.items()))
    for repo, commit_list in sorted_repos.items():
        print(f"  {repo}:")
        total_additions = total_deletions = 0
        sorted_commits = sorted(commit_list, key=lambda c: c["order"])
        for commit in sorted_commits:
            print(f"    commit {commit['hash']}: {commit['message']} "
                  f"({commit['additions']} additions, {commit['deletions']} deletions)")
            total_additions += commit["additions"]
            total_deletions += commit["deletions"]
        print(f"    Total: {total_additions} additions, {total_deletions} deletions")

