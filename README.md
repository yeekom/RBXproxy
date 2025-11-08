# RBXproxy

A tool that connects mitmproxy to Roblox's process, enabling network traffic analysis and debugging through automatic certificate generation and custom addon support.

## Features

- 🔒 Automatic certificate generation and management
- 🔌 Seamless integration with Roblox's process
- 🧩 Support for custom mitmproxy addons
- 🛠️ Network traffic analysis and debugging
- 📊 API call monitoring and inspection

## Use Cases

- Debugging Roblox network traffic
- Analyzing API calls
- Security research
- Modding and development

## Requirements

- Python (3.8 or newer recommended)
- Windows (currently Windows-only support)
- Dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/RBXproxy.git
cd RBXproxy
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run RBXproxy by executing the main script:
```bash
python main.py
```

### How to Know It's Working

When RBXproxy is running correctly, you'll see the mitmproxy window open. Certificates are automatically generated and loaded on first run—no manual configuration needed!

## Custom Addons

RBXproxy supports custom mitmproxy addons to extend functionality.

### Addon Structure

Place your addons in the `Scripts` folder with the following structure:

```
Scripts/
└── YourAddonName/
    ├── addon.py          # Required: Main addon file (loaded by mitmproxy)
    └── other_files.py    # Optional: Any additional files
```

**Requirements:**
- Must be contained in a folder under `Scripts/`
- Must have an `addon.py` file (this is what mitmproxy loads)
- Folder and additional files can have any name

## Known Limitations

⚠️ **Performance Impact**: RBXproxy introduces latency to Roblox:
- ~100ms additional ping
- Occasional lag spikes
- Slightly slower asset loading times
- Joining large games may take up to 5 minutes while assets load

⚠️ **Platform**: Currently only supports Windows. MacOS and Linux support may come in future updates.

⚠️ **Terms of Service**: Use responsibly and be aware of Roblox's Terms of Service when using network analysis tools.

## Troubleshooting

**Stuck on joining game for several minutes?**
- This is normal for large games due to asset loading through the proxy. Wait up to 5 minutes.

**Mitmproxy window not appearing?**
- Ensure all dependencies are installed correctly
- Try running as administrator
- Check that no other proxy is interfering

**High ping/lag?**
- This is expected behavior due to the proxy layer. The ~100ms latency is normal.

## License

[Add your license here]

---

**Disclaimer**: This tool is for educational and debugging purposes. Users are responsible for ensuring their use complies with Roblox's Terms of Service.
