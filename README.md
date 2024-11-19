# 🎯 Ultimate Nitro Code Checker - Async Edition

A high-performance Python script for testing random 18-character alphanumeric strings against the Discord Nitro gift API. The script is optimized for speed and efficiency, using `asyncio` and `aiohttp` to send thousands of requests per second.

---

## 🚀 Features

- **Asynchronous Requests**: Built with `asyncio` and `aiohttp` for ultra-fast, non-blocking HTTP requests.
- **Massive Concurrency**: Configurable to handle thousands of simultaneous requests.
- **Webhook Integration**: Sends valid codes directly to a Discord webhook.
- **Customizable Code Length**: Generates alphanumeric codes of configurable lengths (default: 18).

---

## 📜 How It Works

1. **Random Code Generation**:
   - Generates random alphanumeric strings of 18 characters.
   - Total possible combinations: \(62^{18} \approx 4.7 \times 10^{31}\).

2. **API Requests**:
   - Checks each generated code against the Discord Nitro API.
   - Valid codes return a status code of `200`.

3. **Webhook Notification**:
   - If a valid code is found, it is sent to a configured Discord webhook.

4. **Parallel Execution**:
   - Processes thousands of codes simultaneously using asynchronous tasks.

---

## ⚙️ Script Configuration

### Dependencies

Ensure you have the following Python libraries installed:
```bash
pip install aiohttp
```

### Webhook Setup
Replace the `WEBHOOK_URL` in the script with your Discord webhook URL:
```python
WEBHOOK_URL = "https://discord.com/api/webhooks/your_webhook_id/your_webhook_token"
```

### Customization
You can adjust the following parameters:
- **Code Length**: Change the `length` argument in `generate_random_string()` (default: 18).
- **Concurrency Level**: Modify `max_concurrent_tasks` in the script to control how many requests run in parallel.

---

## 📝 Code Overview

### Crucial Components

1. **Random Code Generation**:
   ```python
   def generate_random_string(length=18):
       return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
   ```
   - Generates 18-character alphanumeric strings, which are used as potential Nitro codes.

2. **Asynchronous API Request**:
   ```python
   async def check_code(session, code):
       url = f"https://discordapp.com/api/v9/entitlements/gift-$0des/{code}?with_application=false&with_subscription_plan=true"
       async with session.get(url) as response:
           if response.status == 200:
               await send_to_webhook(session, code)
   ```
   - Sends the generated code to the Discord Nitro API endpoint.
   - Checks for a status code of `200` to identify valid codes.

3. **Webhook Notification**:
   ```python
   async def send_to_webhook(session, message):
       payload = {"content": f"Valid code found: {message}"}
       async with session.post(WEBHOOK_URL, json=payload) as response:
           if response.status == 204:
               print(f"Successfully sent to webhook: {message}")
   ```
   - Sends valid codes to a Discord webhook for notification.

4. **Concurrency Control**:
   ```python
   async def main():
       max_concurrent_tasks = 1000
       async with aiohttp.ClientSession() as session:
           while True:
               codes = [generate_random_string() for _ in range(max_concurrent_tasks)]
               tasks = [check_code(session, code) for code in codes]
               await asyncio.gather(*tasks)
   ```
   - Configurable `max_concurrent_tasks` determines the number of concurrent requests.

---

## 🔍 Efficiency Suggestions

1. **Increase Concurrency**:
   - Run multiple instances of the script to scale up the number of requests.

2. **Deploy on Cloud**:
   - Use a high-bandwidth cloud server (e.g., AWS, Google Cloud) for faster request processing.

3. **Leverage Patterns**:
   - Analyze known valid codes to narrow down potential patterns or prefixes, reducing the search space.

4. **Dynamic Throttling**:
   - Implement rate-limiting logic to adapt to API restrictions dynamically.

---

## ⚠️ Disclaimer

1. **Chances of Success**:
   - The probability of finding a valid code is extremely low due to the vast number of possible combinations (\(62^{18}\)).
   - Even with 5000 requests per second, it may take several **years** to find one valid code if only 1 exists per \(10^{12}\) combinations.

2. **Expected Time for Success**:
   - Example: With 5000 requests per second and 1 valid code per \(10^{12}\):
     \[
     \text{Estimated time} = \frac{10^{12}}{5000} \approx 6.34 \, \text{years}
     \]

3. **Legality and Ethics**:
   - Ensure compliance with Discord’s Terms of Service.
   - This script is for **educational purposes** only. Use responsibly.

---

## 📂 Repository Structure

```
.
├── .git/                  # Git metadata folder
├── .gitattributes         # Git configuration file
├── LICENSE                # License file (e.g., MIT License)
├── nitro_checker          # Python source file (the script)
├── README                 # Documentation in Markdown
```

---

## 📜 License

This project is licensed under the MIT License. Please refer to the full text of the [MIT License](https://github.com/SudiptaSaha20/Discord-Nitro-Checker/blob/main/LICENSE) for more details.

---