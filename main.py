import subprocess
import sys
import argparse
from datetime import datetime, timedelta

def get_git_commits(since_days):
    since_date = (datetime.now() - timedelta(days=since_days)).strftime('%Y-%m-%d %H:%M:%S')
    cmd = ['git', 'log', f'--since="{since_date}"', '--pretty=format:%h|%an|%s', '--no-merges']
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=False).decode('utf-8')
        return output.splitlines() if output else []
    except subprocess.CalledProcessError:
        return None

def format_report(commits):
    if commits is None:
        return "Error: Not a git repository or git not found."
    if not commits:
        return "No activity found in the specified timeframe."
    
    report = [f"--- Git Pulse Report ({len(commits)} Commits) ---"]
    authors = {}
    
    for line in commits:
        sha, author, msg = line.split('|', 2)
        if author not in authors:
            authors[author] = []
        authors[author].append(f"  - [{sha}] {msg}")
    
    for author, msgs in authors.items():
        report.append(f"\nUser: {author}")
        report.extend(msgs)
    
    return "\n".join(report)

def main():
    parser = argparse.ArgumentParser(description='Summarize recent git activity.')
    parser.add_argument('--days', type=int, default=1, help='Number of days to look back (default: 1)')
    args = parser.parse_args()
    
    result = get_git_commits(args.days)
    print(format_report(result))

if __name__ == '__main__':
    main()