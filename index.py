from flask import request, Flask, render_template, redirect, url_for
import PySimpleGUI as sg

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():

    if request.method == "POST":
        import download_vid

        if "download_video" in request.form:
            url = request.form["url"]
            image = request.form["image"]
            tag = request.form["download_video"]
            
            return redirect(url_for("download", arg1=url, arg2=tag, img=image))


        elif "download_audio" in request.form:
            image = request.form["image"]
            url = request.form["url"]
            tag = request.form["download_audio"]
            
            return redirect(url_for("download", arg1=url, arg2=tag, img=image))

        else:

            url = request.form['video-url']
        
            try:
                cur_video = download_vid.get_video(url)

                return render_template("index.html", current_video={"video": cur_video, "url": url})

            except Exception as e:
                print("Error")
                error = True

                return render_template("index.html", error=error)

    else:
        return render_template("index.html")


@app.route("/download", methods=["GET", "POST"])
def download():
    downloaded = {"none": False, "error": ""}
    image = request.args.get("img")
    if request.method == "POST":
        import download_vid

        # url = video["url"]
        # tag = video["tag"]
        url = request.args.get("arg1")
        tag = request.args.get("arg2")
        

        try:
            # down = download_vid.download(url, tag)
            # print("Downloading...")
            loader = sg.Window('Downloading Video...', [[sg.Text('Downloading video, please wait...')]], no_titlebar=True, keep_on_top=True)

            progress = download_vid.download(url, tag)

            downloaded = {"none": True, "success": "Downloaded Successfully!!!"}
            loader.close()

            return render_template("download.html", downloaded=downloaded, image=image)

        except Exception as e:
            print(str(e))
            downloaded = {"none": False, "error": "Unable to Download, Try again!!!"}
            return render_template("download.html", downloaded=downloaded, image=image)


    return render_template("download.html", downloaded=downloaded, image=image)

