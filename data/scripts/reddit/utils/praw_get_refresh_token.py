import praw
import urllib.parse
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
CLIENT_SECRET = os.getenv('REDDIT_CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDDIT_REDIRECT_URI')
USER_AGENT = os.getenv('REDDIT_USER_AGENT')

# Set up the scope for Reddit (e.g., identity and read permissions)
SCOPES = ['identity', 'read']

# HTTP server to handle the OAuth redirect
class RedditAuthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(parsed_path.query)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'You can close this window.')

        if 'code' in query:
            code = query['code'][0]
            print(f"Authorization code received: {code}")
            self.server.auth_code = code

# Generate the authorization URL and open the browser
def generate_authorization_url():
    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        user_agent=USER_AGENT,
    )
    auth_url = reddit.auth.url(scopes=SCOPES, state='unique_state', duration='permanent')
    print(f"Please visit this URL to authorize the app: {auth_url}")
    webbrowser.open(auth_url)
    return auth_url

# Start an HTTP server to capture the authorization code
def wait_for_auth_code():
    server = HTTPServer(('localhost', 8080), RedditAuthHandler)
    server.handle_request()
    return server.auth_code

# Exchange the authorization code for a refresh token
def get_refresh_token(auth_code):
    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        user_agent=USER_AGENT,
    )
    refresh_token = reddit.auth.authorize(auth_code)
    return refresh_token

if __name__ == "__main__":
    # Step 1: Generate authorization URL
    generate_authorization_url()

    # Step 2: Wait for the authorization code from Reddit
    print("Waiting for the authorization code...")
    auth_code = wait_for_auth_code()

    # Step 3: Exchange the authorization code for a refresh token
    refresh_token = get_refresh_token(auth_code)
    print(f"Your refresh token is: {refresh_token}")
