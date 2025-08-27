import praw

# Replace with your credentials
client_id = 'cTWyJ6kge6S-trtz9TplnA'
client_secret = 'TGCu3QDlrSEZDNs23OANl_WwUplu9w'
user_agent = user_agent = "GenZScraper 1.0 by /u/Fantastic-Host5838"


# Initialize Reddit API
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent)

# Gen Z keywords to search
keywords = ['rizz', 'mid', 'slay', 'based', 'npc', 'vibe check', 'no cap', 'goofy', 'sus', 'bet']

word_count = 0
max_words = 5000
comments_collected = []

print("[*] Starting scrape...")

# Loop through each keyword
for keyword in keywords:
    print(f"Searching for keyword: {keyword}")
    for submission in reddit.subreddit("all").search(keyword, limit=50):
        submission.comments.replace_more(limit=0)
        for comment in submission.comments:
            text = comment.body.strip()
            if keyword in text.lower() and len(text.split()) >= 5:
                comments_collected.append(text)
                word_count += len(text.split())
                print(f"[+] {len(comments_collected)} comments, {word_count} words")
                if word_count >= max_words:
                    break
        if word_count >= max_words:
            break
    if word_count >= max_words:
        break

# Save to file
with open("reddit_genz_comments.txt", "w", encoding="utf-8") as f:
    f.write("\n---\n".join(comments_collected))

print(f"\n✅ Done! Saved {len(comments_collected)} comments ({word_count} words) to reddit_genz_comments.txt")
