# AI-Web-Scraper-using-LLM

This AI web scraper project combines several modern technologies to create a powerful yet user-friendly data extraction tool. Each technology was carefully selected to handle specific challenges in web scraping and make the overall system reliable and easy to use.

Programming Language - Python

Python serves as the foundation of this project because of its simplicity and extensive library support. Python is beginner-friendly, has excellent documentation, and offers numerous pre-built tools for web scraping, data processing, and AI integration. Its readable syntax makes the code easier to maintain and debug, which is crucial for a project involving multiple complex components.

Web Scraping Technology - Selenium WebDriver

Selenium WebDriver is the core technology used for accessing websites and downloading their content. Unlike traditional scraping methods that simply download HTML files, Selenium actually controls a real web browser (Chrome in this case) and interacts with websites just like a human would.

Proxy Service - Bright Data

Bright Data provides proxy services that help the scraper access websites without getting blocked. When websites detect too many requests from the same location, they often block access. Proxies act like intermediaries, making requests appear to come from different locations around the world.
The service also includes automatic CAPTCHA solving, which handles those "I'm not a robot" challenges that many websites display. This ensures smooth operation without manual intervention.

Content Processing - Beautiful Soup

Beautiful Soup is a Python library specifically designed for parsing HTML and XML documents. It takes the raw website code and makes it easy to extract specific elements like text, links, or images. In this project, Beautiful Soup cleans up the downloaded content by removing unnecessary elements like advertisements, navigation menus, and styling code, leaving only the meaningful text.

Artificial Intelligence - OpenAI GPT-3.5

The AI component uses OpenAI's GPT-3.5 model to understand user requests and extract specific information from website content. This is revolutionary because users can describe what they want in plain English instead of writing complex code or rules.
For example, a user can simply type "find all phone numbers" or "extract product prices," and the AI understands exactly what to look for. The model processes the cleaned website content and returns only the requested information, making data extraction accessible to non-technical users.

User Interface - Streamlit

Streamlit creates the web-based user interface that makes the entire system accessible through a web browser. Streamlit was chosen because it allows rapid development of professional-looking web applications using only Python code, without requiring knowledge of HTML, CSS, or JavaScript.
