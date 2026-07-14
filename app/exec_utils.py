import os
import pickle
import subprocess

import yaml


def ping_host(host):
    return os.system("ping -c 1 " + host)


def run_shell(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True)


def evaluate(expr):
    return eval(expr)


def load_session(blob):
    return pickle.loads(blob)


def load_config(text):
    return yaml.load(text)
