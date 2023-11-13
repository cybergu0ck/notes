## Description

mathfield element is unrenderable in the browser provided by QT 5.12.7 framework(using QWebEngineView class).

<br>

### Steps to Reproduce

1. Create the html file with the template code from [getting started](https://cortexjs.io/mathlive/guides/getting-started/) page of cortexjs.io website.

   ```html
   <!DOCTYPE html>
   <html>
     <head>
       <meta charset="utf-8" />
       <title>untitled</title>
       <script defer src="//unpkg.com/mathlive"></script>
     </head>
     <body>
       <math-field>x=\frac{-b\pm \sqrt{b^2-4ac}}{2a}</math-field>
     </body>
   </html>
   ```

2. Use this file to render the html in QT browser (The browser that is provided by QT 5.12.7 framework, using QWebEngineView class). The following is the cpp code that renders the content of the html file in a browser window.

   ```cpp
   #include "qt_browser.h"
   #include <QtWidgets/QApplication>
   #include <QtWebEngineWidgets/QWebEngineView>

   int main(int argc, char *argv[])
   {
       QApplication a(argc, argv);

       // Create a QWebEngineView widget
       QWebEngineView view;

       // Set the URL to your HTML file
       view.setUrl(QUrl::fromLocalFile("path/to/index.html"));

       // Show the widget
       view.show();

       return a.exec();
   }
   ```

<br>

### Actual Behavior

The math-field element is not rendered completely, only plain text of the latex expression is rendered.

![2023-11-10 11_41_40-qt_browser - Microsoft Visual Studio](https://github.com/arnog/mathlive/assets/89940933/d6b311ea-e29b-4ead-b141-92238ac30dff)

<br>

### Expected Behavior

Render the mathfield element. The following image is the output when run on browsers like Edge and Chrome.

![2023-11-10 11_45_01-untitled and 10 more pages - Work - Microsoft​ Edge](https://github.com/arnog/mathlive/assets/89940933/47c6b242-95a1-42ab-8ae9-13189b796422)

<br>

### Environment

**MathLive version**: 0.95.5

**Operating System**: Windows 10

**Browser**: Browser shipped with QT 5.12.7 framework (QWebEngineView); I have inserted its details below.

```
appName : Netscape
appVersion : 5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) QtWebEngine/5.12.7 Chrome/69.0.3497.128 Safari/537.36
userAgent : Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) QtWebEngine/5.12.7 Chrome/69.0.3497.128 Safari/537.36
platform : Win32
language : en-US
cookiesEnabled : true
online : true
```
