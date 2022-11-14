# LearnCpp converter

This code aims to convert the [learnCpp](https://www.learncpp.com/) website into a pdf book for offline reading.

English | [简体中文](.github/README_ZH.md)

# Methodology

1. First, this code leverages the library **pyautogui** to open the web browser to print the learnCpp website.

   This means there are two prerequisites:

   1. Place your browser icon in the first place of the dock.
   2. Use CSS to filter the unnecessary information. Mine is:

   ```css
   #wpdcom{
       display:none;
   }
   
   /* .prevnext-inline{
       display:none;
   } */
   
   /* #masthead{
       display:none;
   }
   
   .wpsolution{
       display:block !important;
   }
   
   .solution_link_show{
       display:none;
   } */
   ```

2. Collect the URLs and chapter names.
3. Use the browser to print all lessons and organize them.
4. Check if there are any missing files and reprint them.
5. Use the library **fitz** to combine these files into single PDF.

# Usage

1. Use webpage2pdf.py to download the lessons.

> Maybe there are some parameters that need to be adapted according to certain situation(e.g. time.sleep(2)).

2. Use delete_lesson.py to check the incorrect files and redownload them.
3. Use combine_pdf.py to combine files.

# WHY?

**Why not use a browser driver(e.g. using Selenium) to autonomize this process?**

The format is hard to adapt with browser driver, plus, the browser opens a page with no extensions which makes it hard to control css.

