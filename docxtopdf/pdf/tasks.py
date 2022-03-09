import os.path

from celery import shared_task
import subprocess


@shared_task
def convert(filepath):
    outdir = os.path.split(filepath)[0]
    cmd = ["soffice", "--headless", "--convert-to", "pdf", filepath, "--outdir", outdir]
    subprocess.run(cmd)
    #return returncode