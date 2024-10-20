import argparse
from mastodon import Mastodon
import yaml
from collections import defaultdict
import sys

def parse_arguments():
    parser = argparse.ArgumentParser(description='Download all posts for a Mastodon user and save them into a YAML file.')
    parser.add_argument('--api_base_url', default='https://mastodon.social', help='The base URL of the Mastodon instance.')
    parser.add_argument('--access_token', help='Your Mastodon API access token.')
    parser.add_argument('--user_handle', default='@pdxjohnny@mastodon.social', help='The handle of the user to fetch posts for.')
    parser.add_argument('--output_file', default='mastodon_posts.yaml', help='The output YAML file.')
    return parser.parse_args()

def get_account_id(mastodon, user_handle):
    # Remove the leading '@' if present
    if user_handle.startswith('@'):
        user_handle = user_handle[1:]
    # Use account_search to find the account
    accounts = mastodon.account_search(user_handle, limit=1)
    if not accounts:
        print(f"No account found for user handle {user_handle}")
        sys.exit(1)
    return accounts[0]['id']

def fetch_all_statuses(mastodon, account_id):
    statuses = []
    max_id = None
    while True:
        fetched_statuses = mastodon.account_statuses(account_id, max_id=max_id, limit=40)
        if not fetched_statuses:
            break
        statuses.extend(fetched_statuses)
        # Set max_id to the ID of the last status fetched, to get older statuses
        max_id = fetched_statuses[-1]['id']
    return statuses

def build_threads(statuses):
    threads = defaultdict(list)
    posts_by_id = {}
    for status in statuses:
        posts_by_id[status['id']] = status
    for status in statuses:
        in_reply_to_id = status['in_reply_to_id']
        if in_reply_to_id and in_reply_to_id in posts_by_id:
            threads[in_reply_to_id].append(status)
        else:
            threads[None].append(status)
    return threads, posts_by_id

def format_status(status):
    return {
        'id': status['id'],
        'content': status['content'],
        'created_at': status['created_at'].isoformat(),
        'replies': []
    }

def build_thread_tree(status, threads, posts_by_id):
    status_formatted = format_status(status)
    replies = threads.get(status['id'], [])
    for reply in replies:
        status_formatted['replies'].append(build_thread_tree(reply, threads, posts_by_id))
    return status_formatted

def save_to_yaml(threads, posts_by_id, output_file):
    formatted_posts = []
    for status in threads[None]:
        formatted_posts.append(build_thread_tree(status, threads, posts_by_id))
    with open(output_file, 'w', encoding='utf-8') as f:
        yaml.dump(
            formatted_posts, 
            f, 
            allow_unicode=True, 
            default_flow_style=False, 
            sort_keys=False
        )
    print(f"Saved all threads to {output_file}")

def main():
    args = parse_arguments()
    if args.access_token:
        mastodon = Mastodon(
            access_token=args.access_token,
            api_base_url=args.api_base_url
        )
    else:
        # Use unauthenticated Mastodon instance (limited to public data)
        mastodon = Mastodon(
            api_base_url=args.api_base_url
        )

    account_id = get_account_id(mastodon, args.user_handle)
    statuses = fetch_all_statuses(mastodon, account_id)
    print(f"Fetched {len(statuses)} statuses.")

    threads, posts_by_id = build_threads(statuses)
    save_to_yaml(threads, posts_by_id, args.output_file)

if __name__ == '__main__':
    main()

