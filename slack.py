from slacker import Slacker

slack = Slacker('xoxb-2200325338311-2215264887379-7AhtyJ7JF7Rx9rJWkZgnSvyR')

# Send a message to #general channel
slack.chat.post_message('#bitcoin', 'Hello fellow slackers!')