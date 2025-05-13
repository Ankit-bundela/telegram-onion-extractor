# Telegram .onion Link Extractor
This project is a Python-based tool that extracts `.onion` links from a public Telegram channel using the [Telethon](https://github.com/LonamiWebs/Telethon) library.

---






## Project Structure
telegram-onion-extractor/



	├──extractor.py # Main script
	├──requirements.txt # Python dependencies
	├──README.md # Project info and usage
	└──images/
	└──screenshot.png # Terminal output screenshot

-----

#Setup Instructions


	1. **Install dependencies**
 
	2. Make sure you're in your virtual environment, then run:
 
		```bash
  
		   pip install -r requirements.txt

2. Configure API credentials
#Open extractor.py and update these lines with your own Telegram API details:
	api_id = YOUR_API_ID
	api_hash = 'YOUR_API_HASH'


3. Run This Script
	#python extractor.py

4. Sample Output
	Fetching messages from channel: toronionlinks ...
	----------------------------------------------------------------------
	http://example1.onion/
	http://example2.onion/
	...
5.Screenshot
	#A sample terminal output screenshot is available in the images/ folder.
