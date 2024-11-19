import asyncio
import aiohttp
import random
import string

# Configure your Discord webhook URL here
WEBHOOK_URL = "https://discord.com/api/webhooks/your_webhook_id/your_webhook_token"

# Function to generate a random alphanumeric string of a specified length
def generate_random_string(length=18):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Async function to check a single code
async def check_code(session, code):
    url = f"https://discordapp.com/api/v9/entitlements/gift-$0des/{code}?with_application=false&with_subscription_plan=true"
    try:
        async with session.get(url) as response:
            if response.status == 200:
                print(f"Valid code found: {code}")
                await send_to_webhook(session, code)
            else:
                print(f"Invalid code: {code} (Status: {response.status})")
    except Exception as e:
        print(f"Error during request for code {code}: {e}")

# Async function to send a message to the Discord webhook
async def send_to_webhook(session, message):
    payload = {"content": f"Valid code found: {message}"}
    try:
        async with session.post(WEBHOOK_URL, json=payload) as response:
            if response.status == 204:
                print(f"Successfully sent to webhook: {message}")
            else:
                print(f"Failed to send to webhook (Status: {response.status})")
    except Exception as e:
        print(f"Error during webhook POST: {e}")

# Main coroutine to manage the tasks
async def main():
    # Number of concurrent workers
    max_concurrent_tasks = 1000

    # Create a single session for reusing connections
    async with aiohttp.ClientSession() as session:
        while True:
            # Generate a batch of random codes
            codes = [generate_random_string() for _ in range(max_concurrent_tasks)]

            # Create tasks for the codes
            tasks = [check_code(session, code) for code in codes]

            # Run the tasks concurrently
            await asyncio.gather(*tasks)

# Run the asyncio event loop
if __name__ == "__main__":
    asyncio.run(main())
