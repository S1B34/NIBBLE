
# Nibble 🐭

**A sleek tool to scan, count, and effortlessly download files from any website with precision and style.**  
Built by the one and only **S1B34**, who knows how to nibble through the web like a pro! 🕵️‍♂️

---

## Features 🌟

- **Scan Websites**: Nibble through the web to find and count files by type (PDFs, images, videos, and more!).
- **Download Files**: Grab files directly from any website—just tell Nibble what you’re hungry for.
- **Support for Popular Extensions**: Handles `.pdf`, `.jpg`, `.mp4`, `.rar`, and more!
- **ASCII Art Coolness**: Because tools without a banner are just boring.

---

## How to Use It 🛠️

1. Clone this repo:
   ```bash
   git clone https://github.com/S1B34/Nibble.git
   cd Nibble
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run **Nibble**:
   ```bash
   python nibble.py
   ```

4. Follow the on-screen instructions and let Nibble do its thing. 🐭

---

## Examples 🚀

### **Example 1: Scan and Download PDFs**
- Target URL: `https://example.com`
- File type: `pdf`

```plaintext
Welcome to Nibble! Let's nibble some files off the web (legally, of course).
Enter the target URL: https://example.com
[INFO] Scanning the website for available file types...
[INFO] Found the following file types:
  .pdf: 15
  .jpg: 5
Enter file extensions to download (comma-separated, e.g., pdf,exe,txt): pdf
[INFO] Searching for files with extensions: .pdf...
[INFO] Found 15 file(s). Starting downloads...
[INFO] File downloaded: downloads/file1.pdf
[INFO] File downloaded: downloads/file2.pdf
...
[INFO] Download process complete! Time to enjoy your nibbled files. 😎
```

---

### **Example 2: Nibble Some WinRAR Files**
- Target URL: `https://fileshare.com`
- File type: `rar`

```plaintext
Welcome to Nibble! Let's nibble some files off the web (legally, of course).
Enter the target URL: https://fileshare.com
[INFO] Scanning the website for available file types...
[INFO] Found the following file types:
  .rar: 10
  .mp4: 3
Enter file extensions to download (comma-separated, e.g., pdf,exe,txt): rar
[INFO] Searching for files with extensions: .rar...
[INFO] Found 10 file(s). Starting downloads...
[INFO] File downloaded: downloads/archive1.rar
[INFO] File downloaded: downloads/archive2.rar
...
[INFO] Download process complete! Time to enjoy your nibbled files. 😎
```

---

## FAQ 🤔

### 1. **Why is it called Nibble?**
Because it "nibbles" through websites to grab the files you want. Plus, it’s a cute name, right? 🐭

### 2. **Does it work on any website?**
It works on most websites, but keep in mind that some sites may block automated requests. Nibble doesn’t do illegal stuff, so don’t ask it to hack NASA. 😜

### 3. **What file types can Nibble detect?**
Nibble supports any file type you specify, but it's particularly good with `.pdf`, `.jpg`, `.mp4`, `.rar`, `.exe`, and `.txt`.

### 4. **I found a bug. What should I do?**
Report it in the Issues section, and S1B34 will fix it faster than Nibble can chew through a webpage!

---

## Known Limitations 🚧

- Nibble doesn’t follow links recursively (yet). If the files you want are deep in the site structure, you may need to grab them manually.
- Websites with advanced anti-bot measures might block Nibble. But hey, at least you tried. 😅

---

## Credits 🙌

- Developed with ❤️ and humor by **S1B34**.
- Inspired by a love for automation, good ASCII art, and nibbling through the web.

---

## License 📜

**Nibble** is open-source and free to use. Just don’t use it for anything illegal, okay? S1B34 doesn’t want to see this on the news. 😉

---

Happy nibbling! 🐭
