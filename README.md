**Dynamic DNS with Cloudflare (ddns-cloudflare)**

---

### Introduction
This script provides a simple solution for updating your Cloudflare DNS records dynamically using the Cloudflare API. It's particularly useful for users with dynamic IP addresses who want to ensure that their domain always points to the correct IP address.

### Features
- Automatic detection and update of your current IP address on Cloudflare DNS records.
- Simple configuration via environment variables.
- Supports both IPv4 and IPv6 addresses.

### Prerequisites
1. **Cloudflare Account**: You'll need an account on Cloudflare with a domain added to manage DNS records.
2. **API Token**: Generate an API token with permissions to edit DNS records.
3. **Python 3.x**: Ensure you have Python 3.x installed on your system.

### Installation
1. Clone this repository:
   ```
   git clone https://github.com/username/ddns-cloudflare.git
   ```
2. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```

### Configuration
1. **Environment Variables**:
   - `ZONE_IDENTIFIER`: The Zone ID of your domain in Cloudflare.
   - `INTERVAL`: Time interval (in minutes) for updating the DNS record.
   - `DOMAIN_NAME`: The domain name you want to update.
   - `EMAIL`: Your Cloudflare account email address.
   - `API_KEY`: Your Cloudflare API key.
   
2. **Update Script**:
   You can directly modify the `ddns_cloudflare.py` script if you prefer not to use environment variables for configuration. Simply replace the variables at the top of the script with your Cloudflare details.

### Usage
1. Run the script:
   ```
   python main.py
   ```

### Automation
To ensure your IP address is always up to date, you can set up a cron job or schedule a task to run the script at regular intervals.

### Troubleshooting
- If you encounter any issues, ensure your API token and zone details are correct.
- Check your Cloudflare account for any rate limits or restrictions that may affect API access.

### Contributions
Contributions are welcome! Feel free to submit issues or pull requests on GitHub.

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Disclaimer
This script comes with no warranty or support. Use it at your own risk. Always ensure you understand the implications of automatically updating DNS records before deploying in a production environment.

