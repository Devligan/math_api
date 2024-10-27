import flask
from flask import request, jsonify
import math
app = flask.Flask(__name__)
@app.route('/area/square', methods=['GET'])
def areasquare():
    s = request.args.get('s')
    if s is None:
        return jsonify({"error": "Invalid or missing 's' parameter"}), 400
    try:
        s = float(s)
    except ValueError:
        return jsonify({"error": "Invalid value for 's' parameter"}), 400
    a = s * s
    return jsonify({"a": a, "s": s}), 200

@app.route('/area/rectangle', methods=['GET'])
def areaRectange():
    l = request.args.get('l')
    w = request.args.get('w')
    if l is None or w is None:
        return jsonify({"error": "Invalid or missing 's' parameter"}), 400
    try:
        l = float(l)
        w = float(w)
    except ValueError:
        return jsonify({"error": "Invalid value for parameters"}), 400
    a = l * w
    return jsonify({"a": a, "l": l, "w": w}), 200

@app.route('/area/triangle', methods=['GET'])
def areaTriangle():
    b = request.args.get('b')
    h = request.args.get('h')
    if h is None or b is None:
        return jsonify({"error": "Invalid or missing 's' parameter"}), 400
    try:
        b = float(b)
        h = float(h)
    except ValueError:
        return jsonify({"error": "Invalid value for parameters"}), 400
    a = (b * h) / 2
    return jsonify({"a": a, "b": b, "h": h}), 200

@app.route('/area/heron', methods=['GET'])
def heronForm():
    x = request.args.get('x')
    y = request.args.get('y')
    z = request.args.get('z')
    if x is None or y is None or z is None:
        return jsonify({"error": "Invalid or missing 's' parameter"}), 400
    try:
        x = int(x)
        y = int(y)
        z = int(z)
    except ValueError:
        return jsonify({"error": "Invalid value for parameters"}), 400
    s = (x + y + z) / 2
    a = math.sqrt((s * (s - x) * (s - y) * (s - z)))
    return jsonify({"x": x, "y": y, "z": z, "s": s, "a": a}), 200

@app.route('/area/parallelogram', methods=['GET'])
def areaParallelogram():
    b = request.args.get('b')
    h = request.args.get('h')
    if h is None or b is None:
        return jsonify({"error": "Invalid or missing 's' parameter"}), 400
    try:
        b = float(b)
        h = float(h)
    except ValueError:
        return jsonify({"error": "Invalid value for parameters"}), 400
    a = b * h
    return jsonify({"a": a, "b": b, "h": h}), 200

@app.route('/area/circle', methods=['GET'])
def areaCircle():
    r = request.args.get('r')
    if r is None:
        return jsonify({"error": "Invalid or missing 's' parameter"}), 400
    try:
        r = float(r)
    except ValueError:
        return jsonify({"error": "Invalid value for 's' parameter"}), 400
    a = math.pi * math.pow(r, 2)
    return jsonify({"a": a, "r": r}), 200

@app.route('/area/trapezoid', methods=['GET'])
def areaTrapezoid():
    b1 = request.args.get('b1')
    b2 = request.args.get('b2')
    h = request.args.get('h')
    if b1 is None or b2 is None or h is None:
        return jsonify({"error": "Invalid or missing 's' parameter"}), 400
    try:
        b1 = float(b1)
        b2 = float(b2)
        h = float(h)
    except ValueError:
        return jsonify({"error": "Invalid value for 's' parameter"}), 400
    a = ((b1 + b2) / 2) * h
    return jsonify({"a": a, "b1": b1, "b2": b2, "h": h}), 200

@app.route('/surface/cube', methods=['GET'])
def surfaceCube():
    s = request.args.get('s')
    if s is None:
        return jsonify({"error": "Invalid or missing 's' parameter"}), 400
    try:
        s = float(s)
    except ValueError:
        return jsonify({"error": "Invalid value for 's' parameter"}), 400
    sa = s * s * 6
    return jsonify({"sa": sa, "s": s}), 200

@app.route('/surface/sphere', methods=['GET'])
def surfaceSphere():
    r = request.args.get('r')
    if r is None:
        return jsonify({"error": "Invalid or missing 's' parameter"}), 400
    try:
        r = float(r)
    except ValueError:
        return jsonify({"error": "Invalid value for 's' parameter"}), 400
    sa = math.pi * math.pow(r, 2) * 4
    return jsonify({"sa": sa, "r": r}), 200

@app.route('/surface/cylinder', methods=['GET'])
def surfaceCylinder():
    r = request.args.get('r')
    h = request.args.get('h')
    if r is None or h is None:
        return jsonify({"error": "Invalid or missing 's' parameter"}), 400
    try:
        r = float(r)
        h = float(h)
    except ValueError:
        return jsonify({"error": "Invalid value for 's' parameter"}), 400
    sa = (2 * math.pi * r* h) + (2 * (math.pi * math.pow(r, 2)))
    return jsonify({"sa": sa, "r": r, "h": h}), 200

@app.route('/perimeter/square', methods=['GET'])
def perimeterSquare():
    s = request.args.get('s')
    if s is None:
        return jsonify({"error": "Invalid or missing 's' parameter"}), 400
    try:
        s = float(s)
    except ValueError:
        return jsonify({"error": "Invalid value for 's' parameter"}), 400
    p = s * 4
    return jsonify({"p": p, "s": s}), 200
@app.route('/perimeter/rectangle', methods=['GET'])
def perimeterRectangle():
    l = request.args.get('l')
    w = request.args.get('w')
    if l is None or w is None:
        return jsonify({"error": "Invalid or missing 's' parameter"}), 400
    try:
        l = float(l)
        w = float(w)
    except ValueError:
        return jsonify({"error": "Invalid value for parameters"}), 400
    p = (2 * l) + (2 * w)
    return jsonify({"p": p, "l": l, "w": w}), 200

@app.route('/perimeter/triangle', methods=['GET'])
def perimeterTriangle():
    s1 = request.args.get('s1')
    s2 = request.args.get('s2')
    s3 = request.args.get('s3')
    if s1 is None or s2 is None or s3 is None:
        return jsonify({"error": "Invalid or missing 's' parameter"}), 400
    try:
        s1 = float(s1)
        s2 = float(s2)
        s3 = float(s3)
    except ValueError:
        return jsonify({"error": "Invalid value for parameters"}), 400
    p = s1 + s2 + s3
    return jsonify({"p": p, "s1": s1, "s2": s2, "s3": s3}), 200

@app.route('/perimeter/circle', methods=['GET'])
def calculate_perimeter_circle():
    d = request.args.get('d')
    if d is None:
        return jsonify({"error": "Invalid or missing 'd' parameter"}), 400
    try:
        d = int(float(d))
    except ValueError:
        return jsonify({"error": "Invalid value for 'd' parameter"}), 400
    c = round(math.pi * d, 3)
    return jsonify({"c": c, "d": d}), 200

@app.route('/volume/cube', methods=['GET'])
def volumeCube():
    s = request.args.get('s')
    if s is None:
        return jsonify({"error": "Invalid or missing 's' parameter"}), 400
    try:
        s = float(s)
    except ValueError:
        return jsonify({"error": "Invalid value for 's' parameter"}), 400
    v = s * s * s
    return jsonify({"v": v, "s": s}), 200

@app.route('/volume/prism', methods=['GET'])
def volumePrisim():
    l = request.args.get('l')
    w = request.args.get('w')
    h = request.args.get('h')
    if l is None or w is None or h is None:
        return jsonify({"error": "Invalid or missing 's' parameter"}), 400
    try:
        l = float(l)
        w = float(w)
        h = float(h)
    except ValueError:
        return jsonify({"error": "Invalid value for parameters"}), 400
    v = l * w * h
    return jsonify({"v": v, "l": l, "w": w, "h": h}), 200

@app.route('/volume/pyramid', methods=['GET'])
def volumePyramid():
    b = request.args.get('b')
    h = request.args.get('h')
    if h is None or b is None:
        return jsonify({"error": "Invalid or missing 's' parameter"}), 400
    try:
        b = float(b)
        h = float(h)
    except ValueError:
        return jsonify({"error": "Invalid value for parameters"}), 400
    v = (b * b * h) / 3
    return jsonify({"v": v, "b": b, "h": h}), 200

@app.route('/volume/cylinder', methods=['GET'])
def volumeCylinder():
    r = request.args.get('r')
    h = request.args.get('h')
    if r is None or h is None:
        return jsonify({"error": "Invalid or missing 's' parameter"}), 400
    try:
        r = float(r)
        h = float(h)
    except ValueError:
        return jsonify({"error": "Invalid value for 's' parameter"}), 400
    v = math.pi * r * r * h
    return jsonify({"v": v, "r": r, "h": h}), 200

@app.route('/volume/cone', methods=['GET'])
def volumeCone():
    r = request.args.get('r')
    h = request.args.get('h')
    if r is None or h is None:
        return jsonify({"error": "Invalid or missing 's' parameter"}), 400
    try:
        r = float(r)
        h = float(h)
    except ValueError:
        return jsonify({"error": "Invalid value for 's' parameter"}), 400
    v = (math.pi * r * r  * h) / 3
    return jsonify({"v": v, "r": r, "h": h}), 200

@app.route('/volume/sphere', methods=['GET'])
def volumeSphere():
    r = request.args.get('r')
    if r is None:
        return jsonify({"error": "Invalid or missing 's' parameter"}), 400
    try:
        r = float(r)
    except ValueError:
        return jsonify({"error": "Invalid value for 's' parameter"}), 400
    v = (4 * math.pi * r * r * r) / 3
    return jsonify({"v": v, "r": r}), 200

@app.route('/distance', methods=['GET'])
def distance():
    x1 = request.args.get('x1')
    y1 = request.args.get('y1')
    x2 = request.args.get('x2')
    y2 = request.args.get('y2')
    if x1 is None or y1 is None or x2 is None or y2 is None:
        return jsonify({"error": "Invalid or missing parameters"}), 400
    try:
        x1 = float(x1)
        y1 = float(y1)
        x2 = float(x2)
        y2 = float(y2)
    except ValueError:
        return jsonify({"error": "Invalid value for parameters"}), 400
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return jsonify({"x1": x1, "y1": y1, "x2": x2, "y2": y2, "d": d}), 200

@app.route('/slope', methods=['GET'])
def calculate_slope():
    x1 = request.args.get('x1')
    y1 = request.args.get('y1')
    x2 = request.args.get('x2')
    y2 = request.args.get('y2')
    if x1 is None or y1 is None or x2 is None or y2 is None:
        return jsonify({"error": "Invalid or missing parameters"}), 400
    try:
        x1 = float(x1)
        y1 = float(y1)
        x2 = float(x2)
        y2 = float(y2)
    except ValueError:
        return jsonify({"error": "Invalid value for parameters"}), 400
    if x2 - x1 == 0:
        m = 'undefined'
    else:
        m = (y2 - y1) / (x2 - x1)
    return jsonify({"x1": x1, "y1": y1, "x2": x2, "y2": y2, "m": m})
@app.route('/pythag', methods=['GET'])
def calculate_pythag():
    a = request.args.get('a')
    b = request.args.get('b')
    c = request.args.get('c')
    if (a is None and b is None) or (a is None and c is None) or (b is None and c is None):
        return jsonify({"error": "Invalid combination of parameters"}), 400
    if a is not None:
        try:
            a = float(a)
        except ValueError:
            return jsonify({"error": "Invalid value for 'a' parameter"}), 400
    if b is not None:
        try:
            b = float(b)
        except ValueError:
            return jsonify({"error": "Invalid value for 'b' parameter"}), 400
    if c is not None:
        try:
            c = float(c)
        except ValueError:
            return jsonify({"error": "Invalid value for 'c' parameter"}), 400
    if a is None:
        a = math.sqrt(c ** 2 - b ** 2)
    if b is None:
        b = math.sqrt(c ** 2 - a ** 2)
    if c is None:
        c = math.sqrt(a ** 2 + b ** 2)
    return jsonify({"a": round(a, 3), "b": round(b, 3), "c": round(c, 3)}), 200

@app.route('/average', methods=['GET'])
def calculate_average():
    nums = request.args.get('nums')
    if nums is None:
        return jsonify({"error": "Invalid or missing 'nums' parameter"}), 400
    num_list = list(map(int, nums.split(',')))
    return jsonify({"avg": sum(num_list) / len(num_list), "nums": num_list}), 200

app.run(host='127.0.0.1', port=3001)




