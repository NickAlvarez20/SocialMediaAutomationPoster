#!/usr/bin/env python3
import os
import json
import argparse
import schedule
import time
from dotenv import load_dotenv
import tweepy

def main():
    # Load environment variables from .env file
    load_dotenv()
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    if not all([consumer_key, consumer_secret, access_token, access_token_secret]):
        print("Error: Missing API credentials in .env file.")
        exit(1)

    client = tweepy.Client(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )

    try:
        user = client.get_me()
        print(f"Authenticated as {user.data.name}")
    except tweepy.TweepyException as e:
        print(f"Authentication failed: {e}")
        exit(1)

    # Argument parser
    parser = argparse.ArgumentParser(description="Automate X posts based on a category or schedule.")
    parser.add_argument("--category", help="The category to post about immediately.")
    parser.add_argument("--index", type=int, default=None, help="Index of the post to select (0-based). Random if not specified.")
    parser.add_argument("--dry-run", action="store_true", help="Simulate posting without actually posting.")
    parser.add_argument("--run-schedule", action="store_true", help="Run scheduled posting.")
    parser.add_argument("--schedule-times", type=str, default="09:00,12:00,15:00,18:00", help="Comma-separated list of posting times (HH:MM).")
    args = parser.parse_args()

    # Load content database
    try:
        with open("content.json", "r", encoding="utf-8") as f:
            content_db = json.load(f)
    except FileNotFoundError:
        print("Error: content.json file not found.")
        exit(1)
    except json.JSONDecodeError:
        print("Error: content.json is malformed.")
        exit(1)

    if args.run_schedule:
        # Scheduling mode
        categories = list(content_db.keys())
        current_indices = {cat: 0 for cat in categories}  # Tracks current post index for each category
        current_category_index = 0  # Tracks which category to post from next

        def post_next():
            nonlocal current_category_index
            category = categories[current_category_index]
            posts = content_db[category]
            if not posts:
                print(f"No posts for category {category}")
                return
            post_index = current_indices[category]
            post = posts[post_index]
            if not args.dry_run:
                try:
                    client.create_tweet(text=post)
                    print(f"Successfully posted: {post}")
                except tweepy.TweepyException as e:
                    print(f"Error posting to X: {e}")
            else:
                print(f"Would post: {post}")
            
            # Move to the next category
            current_category_index = (current_category_index + 1) % len(categories)
            # If we've cycled through all categories, increment all indices
            if current_category_index == 0:
                for cat in categories:
                    if content_db[cat]:  # Only increment if there are posts
                        current_indices[cat] = (current_indices[cat] + 1) % len(content_db[cat])

        # Schedule posts at specified times
        times = args.schedule_times.split(",")
        for t in times:
            try:
                # Validate time format by scheduling it
                schedule.every().day.at(t).do(post_next)
            except schedule.ScheduleValueError:
                print(f"Error: Invalid time format '{t}'. Use HH:MM (e.g., 09:00).")
                exit(1)
        print(f"Scheduled posting at {', '.join(times)} daily.")

        # Run the scheduler
        while True:
            schedule.run_pending()
            time.sleep(1)

    elif args.category:
        # Immediate posting mode
        if args.category not in content_db:
            print(f"Category '{args.category}' not found in database.")
            exit(1)
        posts = content_db[args.category]
        if not posts:
            print(f"No posts available for category '{args.category}'.")
            exit(1)
        if args.index is not None:
            if args.index < 0 or args.index >= len(posts):
                print(f"Error: Index {args.index} is out of range (0 to {len(posts)-1}).")
                exit(1)
            post = posts[args.index]
        else:
            import random
            post = random.choice(posts)
        if args.dry_run:
            print(f"Would post: {post}")
        else:
            try:
                client.create_tweet(text=post)
                print(f"Successfully posted: {post}")
            except tweepy.TweepyException as e:
                print(f"Error posting to X: {e}")
    else:
        print("Error: Must specify either --category or --run-schedule")
        exit(1)

if __name__ == "__main__":
    main()
