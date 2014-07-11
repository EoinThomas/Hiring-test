# -*- coding: utf-8 -*-
"""
Return top airports as a web service
Basing code on flask examples

With bookings.csv in the same folder, run:
python topairports_service.py
then access the service in a browser at:
http://127.0.0.1:5000/
"""


from flask import Flask, jsonify, render_template, request
import werkzeug
import pandas as pd
app = Flask(__name__)


def get_topn_airports(n):
    data_bookings = pd.read_csv('bookings.csv',sep = '^', usecols = ['arr_port','pax'])
    data_bookings.arr_port = data_bookings.arr_port.str.slice(start = 0,stop = 3)

    gby_arr_port = data_bookings.groupby('arr_port')
    pax_per_port = gby_arr_port.pax.sum()
    pax_per_port.sort(ascending = 0)
    return pax_per_port[0:n].to_json()


@app.route('/_top_airports')
def top_airports():
    a = request.args.get('a', 0, type=int)
	
    return jsonify(result = get_topn_airports(a))


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('127.0.0.1', 5000, app, use_debugger=True, use_reloader=True)