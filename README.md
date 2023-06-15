# text_recognition_app

This is a simple application designed to get text included in images. It is based on Tesseract-OCR.
---
# Table of contents
1. [How it works](#how-it-works)
2. [Example Input/Output](#example-inputoutput)
3. [Libraries Used](#libraries-used)
4. [Getting Started](#getting-started)
5. [Automating the process](#automating-the-process)
6. [TODO](#todo)
---
## How it works


---

## Example Input/Output


---
## Libraries Used
- PyQt
- OpenCV
- Pytesseract - the easiest installation and configuration comes from this [repo](https://github.com/simonflueckiger/tesserocr-windows_build)
- Leptonica

---
## Getting Started
* be aware some websites could change their html so might not work anymore
* you can start collecting your data as soon as you start the app
* requires installating additional libraries mentioned above

---
## Automating the process
There are many different ways you can automate collecting the data. Two most obvious one's are:
* you can prepare a script in Linux to exec one of the site-getters files every day or every hour for example
* you can add some variation of the following code:
```python

    def on_start(self):
        threading.Thread(target=self.schedule_task).start()

    def schedule_task(self):
        now = datetime.datetime.now()
        target_time = datetime.datetime(now.year, now.month, now.day, 20, 0, 0)
        if now > target_time:
            target_time += datetime.timedelta(days=1)
        time_delta = target_time - now
        seconds = time_delta.total_seconds()
        threading.Timer(seconds, self.run_task).start()

    def run_task(self):
        # Here you can place which data getter you want to use
        print("I am automatically data collecting")

```

---
## TODO
* add more websites
* also I am preparing a version of the app that will be colecting data automatically, you will just need to paste a link or a screenshot with your fragrance. It will be pusblished soon
* add fmale fragrance handling

---
