from fastapi import FastAPI
from models.intervals import IntervalSet, Interval
from handlers.mergehandler import MergeHandler
from typing import List

app = FastAPI()

merge_handler = MergeHandler()

@app.post("/api/v1/merge_intervals")
def merge_intervals_endpoint(intervals_set: IntervalSet):

    merged_intervals = merge_handler.merge_intervals(intervals_set.includes, intervals_set.excludes)

    return merged_intervals

@app.get("/api/healthchecker")
def root():
    return {"message": "The API is LIVE!!"}