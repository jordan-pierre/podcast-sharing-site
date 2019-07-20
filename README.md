# podcast-sharing-site
Make it easy to share podcasts with friends.

This program is intended to make sharing podcasts with people that use different podcast streaming platforms easier.

I use Google Podcasts on my Android, but many people I want to share podcasts with use iPhones, which aren't supported by Google Podcasts.  Similarly, when I recieve an Apple Podcast URL, I cannot use it because Apple Podcasts isn't supported on Android.  

Each of us have to manually search the podcast show name and title in our podcast streaming platform of choice, which isn't efficient.

This app will read a sharing URL, detect which platform it comes from, grab the podcast name and title, search for it on the platform of choice, and return a URL to the same episode on the platform the friend uses, or return a list of URLs and the friend can pick the one from their favorite platform.

Version 1 will be in Python console and Version 2 will be an online Django web app.

EDIT: It doesn't seem possible to search Google Podcasts or Apple Podcasts via browser, so it might not be possible to get the URL to another platform.

