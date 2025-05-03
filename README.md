# AI LLM Playwright
- AI and Automation Test - Browser-Use Explained: The Open-Source AI Agent That Clicks, Reads, and Automates the Web
- Build an AI Agent can understand what you do in your browser.

## Browser-Use ?
- Browser-Use library: where Playwright meets GPT and the browser becomes an AI playground. Browser Use is as an open-source Python library that wraps Playwright in AI smarts and gives LLMs the keys to your browser.
- [![](https://browser-use.com/logo.svg) Browser-use](https://browser-use.com/)

## Problems and Ideal Solutions
- Web Automation Test problems and challenges: Flakiness.
- Control your Web browser by using Natural Language.

✅ Here’s what makes it different:
- Natural Language Tasking: You say “find the cheapest nonstop flight from Dubai to Cochin”, and the AI does it.
- Playwright-Powered: Under the hood, it uses Microsoft’s Playwright for robust browser automation.
- LLM-Driven: Every decision — what to click, what to read, where to go next -— is powered by an AI model like GPT-4.
- Visual + DOM Understanding: It sees both the code (DOM) and the visual layout (via screenshots), allowing it to identify elements humans would recognize — not just IDs and class names.

# Setup Python environment for our Side-Project
```
# Set up virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install playwright playwright-python openai langchain
# or 
pip install -r requirements.txt
playwright install  # Install browser binaries
```
