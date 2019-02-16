import os
from flask import Flask, jsonify, url_for, request
app = Flask(__name__)

@app.route("/filename/", methods=['GET'])
@app.route("/filename/<string:filename>/", methods=['GET'])
def get_file_data(filename="file1.txt"):
    try:
        start_line = int(request.args.get('start_line', 0))
        end_line = int(request.args.get('end_line', 0))
    except Exception as e:
        return jsonify({"error": "invalid start/end line values."})
    tmp_dict = {}
    if not os.path.exists(filename):
        return jsonify({"error": "invalid filename: %s" % filename})
    with open(filename, 'r') as file_data:
        file_data_list = file_data.read().replace("\t", "").splitlines()
        if int(end_line) == 0:
            end_line = len(file_data_list)
        tmp_dict.update({'file_read': filename, 'number_of_lines_read': len(file_data_list), 'lines': file_data_list[int(start_line):int(end_line)+1]})
        file_data.close()
        return jsonify(tmp_dict)
app.run(debug=True)
