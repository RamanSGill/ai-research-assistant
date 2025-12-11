from retrieval.downloader import download_file
from retrieval.pdf_extractor import extract_text_from_pdf

def main():
    print("AI Research Assistant starting...")

    url = "https://arxiv.org/pdf/1706.03762.pdf"  # Example: Attention is All You Need
    save_path = "docs/sample_paper.pdf"

    print("\nDownloading file...")
    local_file = download_file(url, save_path)

    print("\nExtracting text from PDF...")
    text = extract_text_from_pdf(local_file)
    print(f"Extracted {len(text)} characters of text.")
    print(text)  # Print first 500 characters")

if __name__ == "__main__":
    main()