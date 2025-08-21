import streamlit as st
from scrape_fixed import (scrape_website, split_dom_content,
clean_body_content, extract_body_content
)
from parse import parse_with_openai

# Page configuration
st.set_page_config(
    page_title="AI Web Scraper",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Web Scraper")
st.markdown("---")

# Sidebar for settings
with st.sidebar:
    st.header("⚙️ Settings")
    st.info("""
    **Features:**
    - Multiple scraping methods
    - Error handling & fallbacks
    - Cloud environment support
    - Rate limiting protection
    """)

# Main interface
url = st.text_input("Enter a website URL:", placeholder="https://example.com")

if st.button("🚀 Start Scraping", type="primary"):
    if not url:
        st.error("Please enter a valid URL")
    else:
        with st.spinner("🔄 Scraping website..."):
            try:
                # Scrape the website
                result = scrape_website(url)
                
                # Process the content
                body_content = extract_body_content(result)
                cleaned_content = clean_body_content(body_content)
                
                # Store in session state
                st.session_state.dom_content = cleaned_content
                
                # Success message
                st.success("✅ Website scraped successfully!")
                
                # Display content preview
                with st.expander("📄 View DOM Content", expanded=False):
                    st.text_area("Content Preview", cleaned_content, height=300)
                    
                # Show content stats
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Characters", len(cleaned_content))
                with col2:
                    st.metric("Words", len(cleaned_content.split()))
                with col3:
                    st.metric("Lines", len(cleaned_content.splitlines()))
                    
            except Exception as e:
                st.error(f"❌ Scraping failed: {str(e)}")
                st.info("""
                **Troubleshooting tips:**
                - Check if the URL is accessible
                - Try a different website
                - The site might have anti-bot protection
                """)

# Parse content section
if "dom_content" in st.session_state:
    st.markdown("---")
    st.header("🔍 Parse Content")
    
    parse_description = st.text_area(
        "Describe what you want to parse:",
        placeholder="e.g., Extract all product names and prices, find contact information, etc.",
        height=100
    )
    
    if st.button("🎯 Parse Content", type="secondary"):
        if parse_description:
            with st.spinner("🔄 Parsing content with AI..."):
                try:
                    # Split content into chunks
                    dom_chunks = split_dom_content(st.session_state.dom_content)
                    
                    # Parse with AI
                    result, error = parse_with_ollama(dom_chunks, parse_description)
                    
                    if error:
                        st.error(f"❌ Parsing failed: {error}")
                    else:
                        st.success("✅ Content parsed successfully!")
                        
                        # Display results
                        st.markdown("### 📊 Parsed Results")
                        st.write(result)
                        
                        # Download button
                        st.download_button(
                            label="📥 Download Results",
                            data=result,
                            file_name="parsed_content.txt",
                            mime="text/plain"
                        )
                        
                except Exception as e:
                    st.error(f"❌ Parsing error: {str(e)}")
        else:
            st.warning("Please describe what you want to parse")

# Footer
st.markdown("---")
st.caption("Built with Streamlit, Selenium, and OpenAI")
