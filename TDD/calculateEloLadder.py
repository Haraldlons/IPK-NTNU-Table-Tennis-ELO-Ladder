import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from datetime import datetime
import time
import os

def importPlayers():
	return pd.read_csv("../players.csv")